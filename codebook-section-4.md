```python
%matplotlib inline
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pysentani import find_survey
from sentani_temp import pie_chart_boolean
```

# Code Book for Lake Sentani survey data

This document briefly describes the data for each of the columns in this survey.
The original questions can be found in the sentani_lake_form_v11.xls document.
For each column of the data, this document will describe the question and a
brief summary or description of the results.

The document will also point out any fields that need further analysis or appear
to need inspection to remove errors.

```python
survey = find_survey('../sentani')
print('number of entries =', len(survey))
print('number of columns =', len(survey.columns))
```

## section_04

## gasoline_price
TODO: flag these as not making sense since they range from 10 to 710,000.
Should be in units of price per liter.

English:  How much does a liter of bensin cost in this location (Rp/liter)?

Indonesian: Berapa harga satu liter bensin di lokasi ini (Rp/liter)?

```python
survey['gasoline_price'].describe()
```

## diesel_price

Units of price per liter.

English: How much does a liter of solar cost in this location (Rp/liter)?

Indonesian: Berapa harga satu liter solar di lokasi ini (Rp/liter)?

```python
survey['diesel_price'].value_counts(dropna=False)
```

## kerosene_price

Lots of variation here.  Should be in units of price per liter.

English: How much does a liter of kerosene cost in this location (Rp/liter)?

Indonesian: Berapa harga satu liter minyak tanah di lokasi ini (Rp/liter)?

```python
survey['kerosene_price'].value_counts(dropna=False)
survey['kerosene_price'].describe()
```

##candle_price

English: How much does a candle cost in this location (Rp/candle)?

Indonesian: Berapa harga satu batang lilin di lokasi ini (Rp/lilin)?

```python
survey['candle_price'].value_counts(dropna=False)
survey['candle_price'].describe()
```

## non_electrice_light_expenditures

English: How much money do you spend each week on NON-electric lighting
(Rp/week)?

Indonesian: Berapa biaya yang anda habiskan setiap minggu untuk pelita, lampu
petromax, dan lilin (Rp/minggu)?

```python
survey['non_electrice_light_expenditures'].describe()
```

## battery_price

English: How much do dry cell (D, large) batteries cost in this location
(Rp/battery)?

Indonesian: Berapa harga baterai besar di lokasi ini (Rp/baterai)?

```python
survey['battery_price'].value_counts(dropna=False)
survey['battery_price'].describe()
```

## HP_charging_price

English: How much does it cost to charge a HP (Rp/charge)?

Indonesian: Berapa biaya untuk mengisi baterai HP (Rp/isi)?

```python
survey['HP_charging_price'].describe()
```

## lanterns

English: How many kerosene lanterns do you own?

Indonesian: Berapa banyak lampu yang menggunakan minyak tanah yang anda miliki?

```python
survey['lanterns'].describe()
```

## HP_charging_frequency

English: How often do you charge your HP per month (charges/week)?

Indonesian: Seberapa sering anda mengisi Hp anda setiap bulan (isi/minggu)?

```python
survey['HP_charging_frequency'].value_counts(dropna=False)
survey['HP_charging_frequency'].describe()
```

##HP_quantity

English: How many HP's do you have?

Indonesian: Berapa banyak HP yang anda miliki?

```python
survey['HP_quantity'].describe()
```
