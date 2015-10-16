```python
%matplotlib inline
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pysentani import find_survey
from sentani_temp import pie_chart_boolean
```

#Code Book for Lake Sentani survey data

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

#Section 2

##demand_point

English: Type of demand point.

Indonesian: Jenis tempat.

```python
survey['demand_point'].value_counts(dropna=False)
```

```python
sns.set(style="darkgrid")
dp = sns.countplot(x="demand_point", data=survey)
```

##demand_point_other

English: Please describe what you meant by "other."

Indonesian: Jelaskanlah apa yang anda maksud dengan "lain - lain."

TODO: figure this out. do we use this to augment the enumerated types in
demand_point

```python
series = survey['demand_point_other'].value_counts(dropna=True)
df = pd.DataFrame(series)
df.rename(columns = {0:'count'})
```

##primary_contact

English: Name of head of houshold or primary contact. (Needs to be kept secure)

Indonesian: Nama kepala rumah tangga atau orang kontak utama.

##HP_y_n

English: Does the household posess a cell phone?

Indonesian: Apakah orang kontak utama memiliki HP?

```python
survey['HP_y_n'].value_counts(dropna=False)
```

```python
x = pie_chart_boolean('HP_y_n',survey)
```

##HP

English: Mobile phone number. (needs to be kept secure)

Indonesian: Nomor HP.

##wall

English: What type of wall does the demand point have?

Indonesian: Apakah jenis tembok dari bangunan tersebut?

```python
survey['wall'].value_counts(dropna=False)
```

```python
sns.set(style="darkgrid")
wallg = sns.countplot(x="wall", data=survey)
```

## wall_other

TODO: wall materials not listed in the survey choices.  Should correspond with
'other' category.

English: Please describe what you meant by "other."

Indonesian: Jelaskanlah apa yang anda maksud dengan "lain - lain."


```python
survey['wall_other'].value_counts(dropna=False)
```

##roof

English: What type of roof does the demand point have?

Indonesian: Apakah jenis atap yang dimiliki bangunan tersebut?

```python
survey['roof'].value_counts(dropna=False)
```

```python
roofg = sns.countplot(x="roof", data=survey)
```

##roof_other

English: Please describe what you meant by "other."

Indonesian: Jelaskanlah apa yang anda maksud dengan "lain - lain."

```python
survey['roof_other'].value_counts(dropna=False)
```

```python
roof_other_g = sns.countplot(x="roof_other", data=survey)
```

##building_condition

English: General condition of the building?

Indonesian: Keadaan umum bangunan?

```python
survey['building_condition'].value_counts(dropna=False)
```

```python
bcg = sns.countplot(x="building_condition", data=survey)

```

##assets

English: Select any assets that are owned by people living in the demand point.

Indonesian: Pilih aset apapun yang dimiliki oleh orang-orang yang tinggal di
bangunan tersebut.

```python
survey['assets'].value_counts(dropna=False)
```

```python
asset_g  = sns.countplot(x="assets", data=survey)
```

##assets/livestock

English: Select any assets that are owned by people living in the demand point.

Indonesian: Masukkan kuantitas setiap jenis ternak.

```python
survey['assets/livestock'].value_counts(dropna=False)
```

```python
aslig = pie_chart_boolean('assets/livestock',survey, dropna=False)
```

##assets/machinery

English: What type of machinery assets do they own?

Indonesian: Jenis mesin - mesin apa yang mereka miliki sebagai aset?

```python
survey['assets/machinery'].value_counts(dropna=False)
```

```python
assets_machinery_pie = pie_chart_boolean('assets/machinery',survey, dropna=False)
```

##assets/other

English: Please describe what you meant by "other durable goods assets."

Indonesian: Jelaskanlah apa yang anda maksud dengan "aset yang bagus dan tahan
lama lainnya."

```python
survey['assets/other'].value_counts(dropna=False)
```

```python
assets_other= pie_chart_boolean('assets/other',survey, False)
```

##group_livestock_quantity/pigs



English: Enter the quantity of each livestock type: pigs.

Indonesian: Masukkan kuantitas setiap jenis ternak: babi.

```python
survey['group_livestock_quantity/pigs'].describe()
```

##group_livestock_quantity/chickens

English: Enter the quantity of each livestock type: chickens.

Indonesian: Masukkan kuantitas setiap jenis ternak: ayam.

```python
survey['group_livestock_quantity/chickens'].describe()
```

##group_livestock_quantity/goats

English: Enter the quantity of each livestock type: goats.

Indonesian: Masukkan kuantitas setiap jenis ternak: kambing.

```python
survey['group_livestock_quantity/goats'].describe()
```

##group_livestock_quantity/fish

English: Enter the quantity of each livestock type: fish.

Indonesian: Masukkan kuantitas setiap jenis ternak: ikan.

```python
survey['group_livestock_quantity/fish'].describe()
```

##group_livestock_quantity/cows

English: Enter the quantity of each livestock type: cows.

Indonesian: Masukkan kuantitas setiap jenis ternak: sapi.

```python
survey['group_livestock_quantity/cows'].describe()
```

##group_livestock_quantity/other

English: Enter the quantity of each livestock type: other.

Indonesian: Masukkan kuantitas setiap jenis ternak: lain-lain.

```python
survey['group_livestock_quantity/other'].unique()
```

##machinery

This text field needs to be split out for analysis.

English: What type of machinery assets do they own?

Indonesian: Jenis mesin - mesin apa yang mereka miliki sebagai aset?

```python
survey['machinery'].unique()
```

##asset_other

TODO: this field is another 'lumped together' field that will need to be parsed

English: Please describe what you meant by "other durable good assets."

Indonesian: Jelaskanlah apa yang anda maksud dengan "aset yang bagus dan tahan
lama lainnya."

```python
survey['asset_other'].unique()
```

##job

English: What is your primary job? Where does your primary income come from?

Indonesian: Apa pekerjaan Anda?  Dari mana sumber pendapatan Anda?

```python
survey['job'].value_counts(dropna=False)
```

```python
jobsg = sns.countplot(x="job", data=survey)
```

##jobs_other

English: Please describe what you meant by "other."

Indonesian: Jelaskanlah apa yang anda maksud dengan "lain - lain."

```python
survey['jobs_other'].unique()
```

##group_income_reg/electiric_income

Despite the name, I think this is the household income.  I'm inclined to change
this field descriptor.

English: Please describe your regular income. Amount of income (Rp)?

Indonesian: Berapa besar pendapatan Anda? Jumlah pendapatan (Rp)?

```python
survey['group_income_reg/electric_income'].describe()
```

##group_income_reg/electric_income_freq

English: Please describe your regular income. Frequency of income?

Indonesian: Berapa besar pendapatan Anda? Frekuensi pendapatan?

```python
survey['group_income_reg/electric_income_freq'].describe()
```
