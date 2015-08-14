```python
%matplotlib inline
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from pysentani import find_survey, create_village_name_map
from sentani_temp import pie_chart_boolean, create_village_map
from bokeh.plotting import show, output_notebook

from bokeh.browserlib import view
from bokeh.document import Document
from bokeh.embed import file_html

from bokeh.resources import INLINE
output_notebook()
```

```python
survey = find_survey('../sentani')
print('number of entries =', len(survey))
print('number of columns =', len(survey.columns))
```

# Section 1
## section_01

This section contains village and location information for each surveyed
household.

## village_name

```python
survey['village_name'].value_counts(dropna=False)
```

## gps_point

This is a string with all values on a line in the format "latitude longitude
altitude precision".

```python
survey[['gps_point']].head()
```

#_gps_point_lat...','_gps_point_lon...','_gps_point_alt...','_gps_point_prec...'

```python
survey[['_gps_point_latitude','_gps_point_longitude','_gps_point_altitude','_gps_point_precision' ]].describe()
```

#Village Locations
Created grouping by column 'village_name'

```python
s = survey[["village_name", "_gps_point_latitude","_gps_point_longitude"]]
g = s.groupby("village_name")
g.agg([np.mean])

```

```python
plot = create_village_map(survey)
show(plot)
```

## image

File name of associated photo taken at the time of the survey.

```python
survey['image'].head()
```
