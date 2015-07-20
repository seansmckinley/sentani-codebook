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

## section_06

This section asks households about what appliances they are interested in
purchasing in the future.

```python
survey['app_buy'].value_counts(dropna=False)
#survey['app_buy'].describe()
```

```python
## app_buy/lighting
survey['app_buy/lighting'].value_counts(dropna=False)

```

```python
## app_buy/TV
survey['app_buy/TV'].value_counts(dropna=False)
```

```python
## app_buy/radio
survey['app_buy/radio'].value_counts(dropna=False)
```

```python
## app_buy/fridge
survey['app_buy/fridge'].value_counts(dropna=False)
```

```python
## app_buy/fan
survey['app_buy/fan'].value_counts(dropna=False)
```

```python
## app_buy/rice_cooker
survey['app_buy/rice_cooker'].value_counts(dropna=False)
```

```python
## app_buy/other_cooking
survey['app_buy/other_cooking'].value_counts(dropna=False)
```

```python
## app_buy/welder
survey['app_buy/welder'].value_counts(dropna=False)
```

```python
## app_buy/grinder
survey['app_buy/grinder'].value_counts(dropna=False)
```

```python
## app_buy/saw
survey['app_buy/saw'].value_counts(dropna=False)
```

```python
## app_buy/other_tools
survey['app_buy/other_tools'].value_counts(dropna=False)
```

```python
## app_buy/other
survey['app_buy/other'].value_counts(dropna=False)
```

```python
## app_buy_other
survey['app_buy_other'].value_counts(dropna=False)
```

```python
## app_buy_if_elec_imm
survey['app_buy_if_elec_imm'].value_counts(dropna=False)
```

```python
## app_buy_if_elec_imm/lighting
survey['app_buy_if_elec_imm/lighting'].value_counts(dropna=False)
```

```python
## app_buy_if_elec_imm/TV
survey['app_buy_if_elec_imm/TV'].value_counts(dropna=False)
```

```python
## app_buy_if_elec_imm/radio
survey['app_buy_if_elec_imm/radio'].value_counts(dropna=False)
```

```python
## app_buy_if_elec_imm/fridge
survey['app_buy_if_elec_imm/fridge'].value_counts(dropna=False)
```

```python
## app_buy_if_elec_imm/fan
survey['app_buy_if_elec_imm/fan'].value_counts(dropna=False)
## app_buy_if_elec_imm/rice_cooker
survey['app_buy_if_elec_imm/rice_cooker'].value_counts(dropna=False)
## app_buy_if_elec_imm/other_cooking
survey['app_buy_if_elec_imm/other_cooking'].value_counts(dropna=False)
## app_buy_if_elec_imm/welder
survey['app_buy_if_elec_imm/welder'].value_counts(dropna=False)
## app_buy_if_elec_imm/grinder
survey['app_buy_if_elec_imm/grinder'].value_counts(dropna=False)
## app_buy_if_elec_imm/saw
survey['app_buy_if_elec_imm/saw'].value_counts(dropna=False)
## app_buy_if_elec_imm/other_tools
survey['app_buy_if_elec_imm/other_tools'].value_counts(dropna=False)
survey['app_buy_if_elec_imm/other_tools'].describe()
## app_buy_if_elec_imm/other
survey['app_buy_if_elec_imm/other'].value_counts(dropna=False)
survey['app_buy_if_elec_imm/other'].describe()
## app_buy_if_elec_imm_other
survey['app_buy_if_elec_imm_other'].value_counts(dropna=False)
survey['app_buy_if_elec_imm_other'].describe()
## app_buy_if_elec_year
survey['app_buy_if_elec_year'].value_counts(dropna=False)
survey['app_buy_if_elec_year'].describe()
## app_buy_if_elec_year/lighting
survey['app_buy_if_elec_year/lighting'].value_counts(dropna=False)
survey['app_buy_if_elec_year/lighting'].describe()
## app_buy_if_elec_year/TV
survey['app_buy_if_elec_year/TV'].value_counts(dropna=False)
survey['app_buy_if_elec_year/TV'].describe()
## app_buy_if_elec_year/radio
survey['app_buy_if_elec_year/radio'].value_counts(dropna=False)
survey['app_buy_if_elec_year/radio'].describe()
## app_buy_if_elec_year/fridge
survey['app_buy_if_elec_year/fridge'].value_counts(dropna=False)
survey['app_buy_if_elec_year/fridge'].describe()
## app_buy_if_elec_year/fan
survey['app_buy_if_elec_year/fan'].value_counts(dropna=False)
survey['app_buy_if_elec_year/fan'].describe()
## app_buy_if_elec_year/rice_cooker
survey['app_buy_if_elec_year/rice_cooker'].value_counts(dropna=False)
survey['app_buy_if_elec_year/rice_cooker'].describe()
## app_buy_if_elec_year/other_cooking
survey['app_buy_if_elec_year/other_cooking'].value_counts(dropna=False)
survey['app_buy_if_elec_year/other_cooking'].describe()
## app_buy_if_elec_year/welder
survey['app_buy_if_elec_year/welder'].value_counts(dropna=False)
survey['app_buy_if_elec_year/welder'].describe()
## app_buy_if_elec_year/grinder
survey['app_buy_if_elec_year/grinder'].value_counts(dropna=False)
survey['app_buy_if_elec_year/grinder'].describe()
## app_buy_if_elec_year/saw
survey['app_buy_if_elec_year/saw'].value_counts(dropna=False)
survey['app_buy_if_elec_year/saw'].describe()
## app_buy_if_elec_year/other_tools
survey['app_buy_if_elec_year/other_tools'].value_counts(dropna=False)
survey['app_buy_if_elec_year/other_tools'].describe()
## app_buy_if_elec_year/other
survey['app_buy_if_elec_year/other'].value_counts(dropna=False)
survey['app_buy_if_elec_year/other'].describe()
## app_buy_if_elec_year_other
survey['app_buy_if_elec_year_other'].value_counts(dropna=False)
survey['app_buy_if_elec_year_other'].describe()
## app_type_important
survey['app_type_important'].value_counts(dropna=False)
survey['app_type_important'].describe()
## app_type_important_other
survey['app_type_important_other'].value_counts(dropna=False)
survey['app_type_important_other'].describe()
## app_future
survey['app_future'].value_counts(dropna=False)
survey['app_future'].describe()
```
