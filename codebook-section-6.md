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

## section_06

This section asks households about what appliances they are interested in
purchasing in the future.

##app_buy
English: What additional appliances do you plan to buy, or would like to buy?

Indonesian: Peralatan tambahan apa yang anda rencanakan untuk dibeli, atau ingin
anda beli?

```python
survey['app_buy'].value_counts(dropna=False)
#survey['app_buy'].describe()
```

## app_buy/lighting
English: Lighting.

Indonesian: P
enerangan.

```python
survey['app_buy/lighting'].value_counts(dropna=False)
```

```python
ablp = pie_chart_boolean('app_buy/lighting', survey, False)
```

## app_buy/TV
English: TV.

Indonesian: TV.

```python
survey['app_buy/TV'].value_counts(dropna=False)
```

```python
abTVp = pie_chart_boolean('app_buy/TV', survey, False)
```

## app_buy/radio
English: Radio.

Indonesian: Radio.

```python
survey['app_buy/radio'].value_counts(dropna=False)
```

```python
abR = pie_chart_boolean('app_buy/radio', survey, False)
```

## app_buy/fridge
English: Fridge.

Indonesian: Kulkas.

```python
survey['app_buy/fridge'].value_counts(dropna=False)
```

```python
abF = pie_chart_boolean('app_buy/fridge', survey, False)
```

## app_buy/fan
English: Fan.

Indonesian: Kipas angin.

```python
survey['app_buy/fan'].value_counts(dropna=False)
```

```python
abF = pie_chart_boolean('app_buy/fan', survey, False)
```

##app_buy/rice_cooker
English: Rice Cooker.

Indonesian: Penanak nasi.

```python
survey['app_buy/rice_cooker'].value_counts(dropna=False)
```

```python
abRC = pie_chart_boolean('app_buy/rice_cooker', survey, False)
```

## app_buy/other_cooking
English: Other cooking related.

Indonesian: Masakan lain yang sejenis.

```python
survey['app_buy/other_cooking'].value_counts(dropna=False)
```

```python
abOC = pie_chart_boolean('app_buy/other_cooking', survey, False)
```

## app_buy/welder
English: Welder.

Indonesian: Mesin las.

```python
survey['app_buy/welder'].value_counts(dropna=False)
```

```python
abW = pie_chart_boolean('app_buy/welder', survey, False)
```

##app_buy/grinder
English: Grinder.

Indonesian: Mesin penggiling.

```python
survey['app_buy/grinder'].value_counts(dropna=False)
```

```python
abG = pie_chart_boolean('app_buy/grinder', survey, False)
```

## app_buy/saw
English: Saw.

Indonesian: Mesin gergaji.

```python
survey['app_buy/saw'].value_counts(dropna=False)
```

```python
abS = pie_chart_boolean('app_buy/saw', survey, False)
```

##app_buy/other_tools
English: Other tools related.

Indonesian: Alat - alat lain yang sejenis.

```python
survey['app_buy/other_tools'].value_counts(dropna=False)
```

```python
abOT = pie_chart_boolean('app_buy/other_tools', survey, False)
```

##app_buy/other
English: Any other.

Indonesian: Ada yang lain.

```python
survey['app_buy/other'].value_counts(dropna=False)
```

```python
abO = pie_chart_boolean('app_buy/other', survey, False)
```

## app_buy_other
English: Please describe what you meant by "other."

Indonesian: Jelaskanlah apa yang anda maksud dengan "lain - lain."

```python
survey['app_buy_other'].value_counts(dropna=False)
```

## app_buy_if_elec_imm
English: If you had electricity, which appliances would you buy immediately?

Indonesian: Jika anda punya listrik, peralatan yang mana  yang mau anda beli
segera?

```python
survey['app_buy_if_elec_imm'].value_counts(dropna=False)
```

## app_buy_if_elec_imm/lighting
English: Lighting.

Indonesian: Penerangan.

```python
survey['app_buy_if_elec_imm/lighting'].value_counts(dropna=False)
```

## app_buy_if_elec_imm/TV
English: TV.

Indonesian: TV.

```python
survey['app_buy_if_elec_imm/TV'].value_counts(dropna=False)
```

## app_buy_if_elec_imm/radio
English: Radio.

Indonesian: Radio.

```python
survey['app_buy_if_elec_imm/radio'].value_counts(dropna=False)
```

## app_buy_if_elec_imm/fridge
English: Fridge.

Indonesian: Kulkas.

```python
survey['app_buy_if_elec_imm/fridge'].value_counts(dropna=False)
```

## app_buy_if_elec_imm/fan
English: Fan.

Indonesian: Kipas angin.

```python
survey['app_buy_if_elec_imm/fan'].value_counts(dropna=False)
```

## app_buy_if_elec_imm/rice_cooker
English: Rice cooker.

Indonesian: Penanak nasi.

```python
survey['app_buy_if_elec_imm/rice_cooker'].value_counts(dropna=False)
```

## app_buy_if_elec_imm/other_cooking
English: Other cooking related.

Indonesian: Masakan lain yang sejenis.

```python
survey['app_buy_if_elec_imm/other_cooking'].value_counts(dropna=False)
```

## app_buy_if_elec_imm/welder
English: Welder.

Indonesian: Mesin las.

```python
survey['app_buy_if_elec_imm/welder'].value_counts(dropna=False)
```

## app_buy_if_elec_imm/grinder
English: Grinder.

Indonesian: Mesin penggiling.

```python
survey['app_buy_if_elec_imm/grinder'].value_counts(dropna=False)
```

## app_buy_if_elec_imm/saw
English: Saw.

Indonesian: Mesin gergaji.

```python
survey['app_buy_if_elec_imm/saw'].value_counts(dropna=False)
```

## app_buy_if_elec_imm/other_tools
English: Other tools related.

Indonesian: Alat - alat lain yang sejenis.

```python
survey['app_buy_if_elec_imm/other_tools'].value_counts(dropna=False)
##survey['app_buy_if_elec_imm/other_tools'].describe()
```

## app_buy_if_elec_imm/other
English: Any other.

Indonesian: Ada yang lain.

```python
survey['app_buy_if_elec_imm/other'].value_counts(dropna=False)
##survey['app_buy_if_elec_imm/other'].describe()
```

## app_buy_if_elec_imm_other
English: Please describe what you meant by "other."

Indonesian: Jelaskanlah apa yang anda maksud dengan "lain - lain."

```python
##survey['app_buy_if_elec_imm_other'].value_counts(dropna=False)
survey['app_buy_if_elec_imm_other'].describe()
```

## app_buy_if_elec_year
English: If you had electricity, which appliances would you buy in the first
year?

Indonesian: Jika anda punya listrik, peralatan yang mana yang mau anda beli pada
tahun pertama?

```python
##survey['app_buy_if_elec_year'].value_counts(dropna=False)
survey['app_buy_if_elec_year'].describe()
```

## app_buy_if_elec_year/lighting
English: Lighting.

Indonesian: Penerangan.

```python
survey['app_buy_if_elec_year/lighting'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/lighting'].describe()
```

## app_buy_if_elec_year/TV
English: TV.

Indonesian: TV.

```python
survey['app_buy_if_elec_year/TV'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/TV'].describe()
```

## app_buy_if_elec_year/radio
English: Radio.

Indonesian: Radio.

```python
survey['app_buy_if_elec_year/radio'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/radio'].describe()
```

## app_buy_if_elec_year/fridge
English: Fridge.

Indonesian: Kulkas.

```python
survey['app_buy_if_elec_year/fridge'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/fridge'].describe()
```

## app_buy_if_elec_year/fan
English: Fan.

Indonesian: Kipas angin.

```python
survey['app_buy_if_elec_year/fan'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/fan'].describe()
```

## app_buy_if_elec_year/rice_cooker
English: Rice cooker.

Indonesian: Penanak nasi.

```python
survey['app_buy_if_elec_year/rice_cooker'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/rice_cooker'].describe()
```

## app_buy_if_elec_year/other_cooking
English: Other cooking related.

Indonesian: Masakan lain yang sejenis.

```python
survey['app_buy_if_elec_year/other_cooking'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/other_cooking'].describe()
```

## app_buy_if_elec_year/welder
English: Welder.

Indonesian: Mesin las.

```python
survey['app_buy_if_elec_year/welder'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/welder'].describe()
```

## app_buy_if_elec_year/grinder
English: Grinder.

Indonesian: Mesin penggiling.

```python
survey['app_buy_if_elec_year/grinder'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/grinder'].describe()
```

## app_buy_if_elec_year/saw
English: Saw.

Indonesian: Mesin gergaji.

```python
survey['app_buy_if_elec_year/saw'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/saw'].describe()
```

## app_buy_if_elec_year/other_tools
English: Other tools related.

Indonesian: Alat - alat lain yang sejenis.

```python
survey['app_buy_if_elec_year/other_tools'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/other_tools'].describe()
```

## app_buy_if_elec_year/other
English: Any other.

Indonesian: Ada yang lain.

```python
survey['app_buy_if_elec_year/other'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/other'].describe()
```

## app_buy_if_elec_year_other
English: Please describe what you meant by "other."

Indonesian: Jelaskanlah apa yang anda maksud dengan "lain - lain."

```python
##survey['app_buy_if_elec_year_other'].value_counts(dropna=False)
survey['app_buy_if_elec_year_other'].describe()
```

## app_type_important
English: Access to which types of appliances is most important to you?

Indonesian: Akses untuk jenis - jenis peralatan yang mana yang paling penting
buat anda?

```python
survey['app_type_important'].value_counts(dropna=False)
##survey['app_type_important'].describe()
```

## app_type_important_other
English: Please describe what you meant by "other."

Indonesian: Jelaskanlah apa yang anda maksud dengan :lain - lain."

```python
##survey['app_type_important_other'].value_counts(dropna=False)
survey['app_type_important_other'].describe()
```

## app_future
English:  What will future appliances allow you to do that you can't do now?

Indonesian: Perkakas apa yang akan anda sediakan kelak untuk melakukan apa yang
tidak dapat anda lakukan sekarang?

```python
##survey['app_future'].value_counts(dropna=False)
survey['app_future'].describe()
```
