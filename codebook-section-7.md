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

## section_07

## willingness_monthly
How much are you willing to pay monthly for electricity (Rp/month)?

```python
survey['willingness_monthly'].describe()
```

## willingness_connect
How much are you willing to pay upfront for a connection (Rp)?

```python
survey['willingness_connect'].describe()
```

## willingness_fridge
How much are you willing to pay for electricity per month for a refrigerator
(Rp/month)?

```python
survey['willingness_fridge'].describe()
```

## willingness_other
How much are you willing to pay for electricity for other household elecronics
(Rp/month)?

```python
survey['willingness_other'].describe()
```

## finished
Dummy column in survey

```python
## start
survey['start'].value_counts(dropna=False)
```

## end
Time of end of survey

```python
## today
survey['today'].value_counts(dropna=False)
survey['today'].describe()
```

```python
## deviceid
survey['deviceid'].value_counts(dropna=False)
```

```python
## simserial
survey['simserial'].value_counts(dropna=False)
```

```python
## phonenumber
survey['phonenumber'].value_counts(dropna=False)
survey['phonenumber'].describe()
## meta_data
survey['meta_data'].value_counts(dropna=False)
survey['meta_data'].describe()
## meta/instanceID
survey['meta/instanceID'].value_counts(dropna=False)
survey['meta/instanceID'].describe()
## _id
survey['_id'].value_counts(dropna=False)
survey['_id'].describe()
## _uuid
survey['_uuid'].value_counts(dropna=False)
survey['_uuid'].describe()
## _submission_time
survey['_submission_time'].value_counts(dropna=False)
survey['_submission_time'].describe()
## _index
survey['_index'].value_counts(dropna=False)
survey['_index'].describe()
## _parent_table_name
survey['_parent_table_name'].value_counts(dropna=False)
survey['_parent_table_name'].describe()
## _parent_index
survey['_parent_index'].value_counts(dropna=False)
survey['_parent_index'].describe()
## _tags
survey['_tags'].value_counts(dropna=False)
survey['_tags'].describe()
## _notes
survey['_notes'].value_counts(dropna=False)
survey['_notes'].describe()
## _version
survey['_version'].value_counts(dropna=False)
#survey['_version'].describe()
```
