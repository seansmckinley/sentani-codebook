'''
sentani_temp.py
functions in this file may or may not end up as part of pysentani
'''

from __future__ import print_function
from bokeh.plotting import *
from bokeh import session
import os.path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.models.glyphs import Circle, Line, Text
from bokeh.models import(
    GMapPlot, Range1d, ColumnDataSource, LinearAxis,
    PanTool, WheelZoomTool, BoxZoomTool, ResetTool, ResizeTool, BoxSelectTool, HoverTool,
    BoxSelectionOverlay, GMapOptions,
    NumeralTickFormatter, PrintfTickFormatter)
from bokeh.resources import INLINE

from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

def pie_chart_boolean(col, df, dropna=True):
    '''
    Usage: new_pie_chart = pie_chart_boolean("column_string", dataframe, dropnulls)
    "column_string" will be a string column from your dataframe.
    dataframe is your pandas dataframe.
    dropnulls will be either True or False.
    
    '''
    vc = df[col].value_counts(normalize=True, dropna=dropna)
    yes = vc.get(1)
    no = vc.get(0)
    if dropna != True:
        NaN = sum(vc) - vc[0] - vc[1]
        labels = ['Yes', 'No', 'No Response']
        colors = ['green', 'red', 'lightcoral']
        sizes = [int(yes*100),int(no*100),int(NaN*100)]
        explode = (0.1, 0, 0)
    else:
        labels = ['Yes', 'No']
        colors = ['green', 'red']
        sizes = [int(yes*100),int(no*100)]
        explode = (0.1, 0)
    p = plt.pie(sizes, explode, labels, colors, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    return p

def create_village_map(survey):
    s = survey[["village_name", "_gps_point_latitude" , "_gps_point_longitude"]]
    g = s.groupby("village_name")
    mean = g.agg([np.mean])
    mean = mean.reset_index()
    mean.columns = ['_'.join(col).strip() for col in mean.columns.values]
    mean.columns = ['vn', 'lat_mean', 'lon_mean']
    x_range = Range1d()
    y_range = Range1d()
    map_options = GMapOptions(lat= -2.588, lng=140.5170, zoom=11)
    plot = GMapPlot(
        x_range = x_range,
        y_range = y_range,
        map_options=map_options,
        title = "Lake Sentani"
    )
    dot_source = ColumnDataSource(
        data=dict(
            lat = [float(x) for x in survey['_gps_point_latitude']],
            lon = [float(y) for y in survey['_gps_point_longitude']],
            uuid = [str(x) for x in survey['_uuid']],
            vName = [str(x) for x in survey['village_name']],
            size = [.0001 for x in survey['_uuid']],
        )
    )
    plot.map_options.map_type="terrain"
    circle = Circle(x='lon', y='lat', radius='size', fill_color = 'red', fill_alpha = 0.9)
    plot.add_glyph(dot_source, circle)
    text_source = ColumnDataSource(
        data=dict(
            vn = [str(x) for x in mean['vn']],
            lat = [float(x) for x in mean['lat_mean']],
            lon = [float(x) for x in mean['lon_mean']]
        )
    )
    text = Text(x="lon", y="lat", text="vn", text_color="maroon")
    plot.add_glyph(text_source, text)
    reset = ResetTool()
    pan = PanTool()
    wheel_zoom = WheelZoomTool()
    box_zoom = BoxZoomTool()

    plot.add_tools(pan, wheel_zoom, box_zoom, reset)

    xaxis = LinearAxis(axis_label="lon.", major_tick_in=0)
    plot.add_layout(xaxis, 'below')
    yaxis = LinearAxis(axis_label="lat.", major_tick_in=0)
    plot.add_layout(yaxis, 'left')
    return plot



def add_village_latitude_longitude(survey):
    survey["village_lat"], survey["village_lon"] = 0.0, 0.0
    s = survey[["village_name", "_gps_point_latitude" , "_gps_point_longitude" ]]
    g = s.groupby("village_name")
    mean = g.agg([np.mean])
    mean = mean.reset_index()
    mean.columns = ['_'.join(col).strip() for col in mean.columns.values]
    mean.columns = ['vn', 'lat_mean', 'lon_mean']
    for i, ix in enumerate(survey):
        v = survey["village_name"][i]
        uuid = survey["_uuid"][i]
        v_lat, v_lon = "village_lat", "village_lon"
        lat, lon = "_gps_point_latitude", "_gps_point_longitude"
        survey.loc[uuid,v_lon] = float(mean[mean["vn"] == v]["lon_mean"])
        survey.loc[uuid,v_lat] = float(mean[mean["vn"] == v]["lat_mean"])
    return survey

def add_village_distance_to_grids(survey):
    survey["dist_v2j_grid"], survey["dist_v2g_grid"] = 0.0, 0.0
    s = survey[["village_name", "_gps_point_latitude" , "_gps_point_longitude", 
           "dist_v2j_grid","dist_v2g_grid" ]]
    g = s.groupby("village_name")
    mean = g.agg([np.mean])
    mean = mean.reset_index()
    mean.columns = ['_'.join(col).strip() for col in mean.columns.values]
    mean.columns = ['vn', 'lat_mean', 'lon_mean', 'dist_mean', 'dv2j','dv2g']
    add_village_latitude_longitude(survey)
    plnj_lat, plng_lat = -2.533, -2.467
    plnj_lon, plng_lon = 140.716, 140.0145
    for i, ix in enumerate(survey):
        v = survey["village_name"][i]
        uuid = survey["_uuid"][i]
        lat, lon = "_gps_point_latitude","_gps_point_longitude"
        v2j, v2g = "dist_v2j_grid","dist_v2g_grid"
        survey.loc[uuid,v2j] = haversine (survey.loc[uuid,v_lon], survey.loc[uuid,v_lat],
                                          plnj_lon, plnj_lat)
        survey.loc[uuid,v2g] = haversine (survey.loc[uuid,v_lon], survey.loc[uuid,v_lat],
                                          plng_lon, plng_lat) 
    #needs a step to remove village_latitude and longitude
    return survey

def add_dp_distance_to_village_center(survey):
    survey["distance_to_village_center"] = 0.0
    s = survey[["village_name", "_gps_point_latitude", "_gps_point_longitude",
                "distance_to_village_center"]]
    g = s.groupby("village_name")
    mean = g.agg([np.mean])
    mean = mean.reset_index()
    mean.columns = ['_'.join(col).strip() for col in mean.columns.values]
    mean.columns = ['vn', 'lat_mean', 'lon_mean','d2vc_mean']
    v = survey["village_name"][i]
    uuid = survey["_uuid"][i]
    v_lat, v_lon = "village_lat", "village_lon"
    lat, lon = "_gps_point_latitude","_gps_point_longitude"
    dist = "distance_to_village_center"
    survey.loc[uuid,v_lon] = float(mean[mean["vn"] == v]["lon_mean"])
    survey.loc[uuid,v_lat] = float(mean[mean["vn"] == v]["lat_mean"])
    survey.loc[uuid,dist] = haversine (survey.loc[uuid,v_lon], survey.loc[uuid,v_lat],
                                       survey.loc[uuid,lon], survey.loc[uuid,lat])
    #needs a step to remove village_latitude and longitude
    return survey