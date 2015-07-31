```python
%matplotlib inline
import pandas as pd
import seaborn as sns
import sentani as sti
from sentani import get_survey
survey = sti.get_survey()
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

## section_07

## willingness_monthly
English: How much are you willing to pay monthly for electricity (Rp/month)?

Indonesian: Berapa biaya listrik yang bersedia anda bayar setiap bulan
(Rp/bulan)?

```python
survey['willingness_monthly'].describe()
```

## willingness_connect
English: How much are you willing to pay upfront for a connection (Rp)?

Indonesian: Berapa biaya yang bersedia anda bayar dimuka untuk pemasangan (Rp)?

```python
survey['willingness_connect'].describe()
```

## willingness_fridge
English: How much are you willing to pay for electricity per month for a
refrigerator (Rp/month)?

Indonesian: Berapa biaya listrik yang bersedia anda bayar setiap bulan untuk
kulkas (Rp/bulan)?

```python
survey['willingness_fridge'].describe()
```

## willingness_other
English: How much are you willing to pay for electricity for other household
elecronics (Rp/month)?

Indonesian: Berapa biaya listrik yang bersedia anda bayar untuk barang - barang
elektronik yang anda gunakan atau ada di rumah anda (Rp/bulan)?

```python
survey['willingness_other'].describe()
```

## finished
Dummy column in survey


## start

```python
pd.set_option('display.max_rows', 4)
survey['start'].value_counts(dropna=False)
```

## end
Time of end of survey

## today

```python
pd.set_option('display.max_rows', 4)
survey['today'].value_counts(dropna=False)
#survey['today'].describe()
```

## deviceid

```python
survey['deviceid'].value_counts(dropna=False)
```

## simserial

```python
survey['simserial'].value_counts(dropna=False)
```

## phonenumber

```python
survey['phonenumber'].head()
```

## meta_data

```python
survey['meta_data'].head()
#survey['meta_data'].describe()
```

```python
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

```python

```
