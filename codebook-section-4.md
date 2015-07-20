```python
%matplotlib inline
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sentani import get_survey
```

# Code Book for Lake Sentani survey data

This document briefly describes the data for each of the columns in this survey.
The original questions can be found in the sentani_lake_form_v11.xls document.
For each column of the data, this document will describe the question and a
brief summary or description of the results.

The document will also point out any fields that need further analysis or appear
to need inspection to remove errors.

```python
survey = get_survey()
print('number of entries =', len(survey))
print('number of columns =', len(survey.columns))
```

## section_04

## gasoline_price
TODO: flag these as not making sense since they range from 10 to 710,000.
Should be in units of price per liter.

```python
survey['gasoline_price'].describe()
```

## diesel_price

Units of price per liter.

```python
survey['diesel_price'].value_counts(dropna=False)
```

## kerosene_price

Lots of variation here.  Should be in units of price per liter.

```python
## kerosene_price
survey['kerosene_price'].value_counts(dropna=False)
survey['kerosene_price'].describe()
```

## candle_price

```python
## candle_price
survey['candle_price'].value_counts(dropna=False)
survey['candle_price'].describe()
```

## non_electrice_light_expenditures

```python
## non_electrice_light_expenditures
#survey['non_electrice_light_expenditures'].value_counts(dropna=False)
survey['non_electrice_light_expenditures'].describe()
```

## battery_price

```python
## battery_price
survey['battery_price'].value_counts(dropna=False)
survey['battery_price'].describe()
```

## HP_charging_price

```python
## HP_charging_price
#survey['HP_charging_price'].value_counts(dropna=False)
survey['HP_charging_price'].describe()
```

## lanterns
Number of kerosene lanterns owned.

```python
## lanterns
#survey['lanterns'].value_counts(dropna=False)
survey['lanterns'].describe()
```

## HP_charging_frequency
Question: How often do you charge your HP per month (charges/week)?

```python
## HP_charging_frequency
survey['HP_charging_frequency'].value_counts(dropna=False)
survey['HP_charging_frequency'].describe()
```

## HP_quantity
Question: How many HP's do you have?

```python
## HP_quantity
#survey['HP_quantity'].value_counts(dropna=False)
survey['HP_quantity'].describe()
```
