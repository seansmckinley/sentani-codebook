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

## section_05

This section surveys appliance ownership information.

## app_now
English: Please select which existing electric appliances you currently own?

Indonesian: Pilihlah peralatan listrik yang ada yang anda miliki sekarang?

```python
## app_now
survey['app_now'].value_counts(dropna=False)
#survey['app_now'].describe()
```

## app_now/lighting
English: Lighting.

Indonesian: Penerangan.

```python
## app_now/lighting
survey['app_now/lighting'].value_counts(dropna=False)
#survey['app_now/lighting'].describe()
```

```python
a = pie_chart_boolean('app_now/lighting', survey, False)
```

## app_now/TV
English: TV.

Indonesian: TV.

```python
## app_now/TV
survey['app_now/TV'].value_counts(dropna=False)
```

```python
aa = pie_chart_boolean('app_now/TV', survey, False)
```

## app_now/radio
English: Radio.

Indonesian: Radio.

```python
## app_now/radio
survey['app_now/radio'].value_counts(dropna=False)
```

```python
ab = pie_chart_boolean('app_now/radio', survey, False)
```

## app_now/fridge
English: Refrigerator.

Indonesian: Kulkas.

```python
## app_now/fridge
survey['app_now/fridge'].value_counts(dropna=False)
```

```python
bb = pie_chart_boolean('app_now/fridge', survey, False)
```

##app_now/fan
English: Fan.

Indonesian: Kipas.

```python
## app_now/fan
survey['app_now/fan'].value_counts(dropna=False)
```

```python
bc= pie_chart_boolean('app_now/fan', survey, False)
```

##app_now/rice_cooker
English: Rice cooker.

Indonesian: Penanak nasi.

```python
## app_now/rice_cooker
survey['app_now/rice_cooker'].value_counts(dropna=False)
```

```python
aba = pie_chart_boolean('app_now/rice_cooker', survey,False)
```

##app_now/other_cooking
English: Other cooking related.

Indonesian: "Masakan lain yang sejenis."

```python
## app_now/other_cooking
survey['app_now/other_cooking'].value_counts(dropna=False)
```

```python
eb = pie_chart_boolean('app_now/other_cooking', survey, False)
```

## app_now/welder
English: Welder.

Indonesian: Mesin las.

```python
## app_now/welder
survey['app_now/welder'].value_counts(dropna=False)
```

```python
welder = pie_chart_boolean('app_now/welder', survey, False)
```

##app_now/grinder
English: Grinder.

Indonesian: Mesin penggiling.

```python
## app_now/grinder
survey['app_now/grinder'].value_counts(dropna=False)
```

```python
grinder = pie_chart_boolean('app_now/grinder', survey, False)
```

## app_now/saw
English: Saw.

Indonesian: Mesin gergaji.

```python
## app_now/saw
survey['app_now/saw'].value_counts(dropna=False)
```

```python
saw = pie_chart_boolean('app_now/saw', survey, False)
```

##app_now/other_tools
English: Other tools related.

Indonesian: Alat - alat lain yang sejenis.

```python
## app_now/other_tools
survey['app_now/other_tools'].value_counts(dropna=False)
```

```python
ot = pie_chart_boolean('app_now/other_tools', survey, False)
```

##app_now/other
English: Any other.

Indonesian: Ada yang lain.

```python
## app_now/other
survey['app_now/other'].value_counts(dropna=False)
```

```python
saw = pie_chart_boolean('app_now/other', survey, False)
```

## app_other_cooking_desc
English: Please describe what you meant by "other cooking related."

Indonesian: Jelaskanlah apa yang anda maksud dengan "masakan lain yang sejenis."

```python
## app_other_cooking_desc
survey['app_other_cooking_desc'].value_counts(dropna=False)
#survey['app_other_cooking_desc'].describe()
```

## app_other_tools_desc
English: Please describe what you meant by "other tools related."

Indonesian: Jelaskanlah apa yang anda maksud dengan "alat - alat lain yang
sejenis."

```python
## app_other_tools_desc
survey['app_other_tools_desc'].value_counts(dropna=False)
#survey['app_other_tools_desc'].describe()
```

##app_other_desc
English: Please describe what you meant by "any other."

Indonesian: Jelaskanlah apa yang anda maksud dengan "ada yang lain."

```python
## app_other_desc
survey['app_other_desc'].value_counts(dropna=False)
#survey['app_other_desc'].describe()
```

## app_lighting_per_wk
English: For lighting, how many times a week do you use it?

Indonesian: Untuk penerangan, berapa kali seminggu anda menggunakannya?

```python
## app_lighting_per_wk
survey['app_lighting_per_wk'].value_counts(dropna=False)
survey['app_lighting_per_wk'].describe()
```

## app_lighting_hrs
English: For lighting, each time you use it, how many hours do you use it for?

Indonesian: Untuk penerangan, selama berapa jam setiap kali anda menggunakannya?

```python
## app_lighting_hrs
survey['app_lighting_hrs'].value_counts(dropna=False)
survey['app_lighting_hrs'].describe()
```

## app_lighting_use_times
English: For lighting, what time of the day do you typically use it?

Indonesian: Untuk penerangan, pada jam berapa biasanya anda menggunakannya?

```python
## app_lighting_use_times
survey['app_lighting_use_times'].value_counts(dropna=False)
#survey['app_lighting_use_times'].describe()
```

## app_lighting_use_times/morning

```python
## app_lighting_use_times/morning
survey['app_lighting_use_times/morning'].value_counts(dropna=False)
#survey['app_lighting_use_times/morning'].describe()
```

```python
appmd= pie_chart_boolean('app_lighting_use_times/morning', survey, False)
```

## app_lighting_use_times/mid_day

```python
## app_lighting_use_times/mid_day
survey['app_lighting_use_times/mid_day'].value_counts(dropna=False)
#survey['app_lighting_use_times/mid_day'].describe()
```

## app_lighting_use_times/afternoon

```python
## app_lighting_use_times/afternoon
survey['app_lighting_use_times/afternoon'].value_counts(dropna=False)
#survey['app_lighting_use_times/afternoon'].describe()
```

```python
appaf= pie_chart_boolean('app_lighting_use_times/afternoon', survey, False)
```

## app_lighting_use_times/night

```python
## app_lighting_use_times/night
survey['app_lighting_use_times/night'].value_counts(dropna=False)
```

```python
appn= pie_chart_boolean('app_lighting_use_times/night', survey,False)
```

## app_TV_per_wk
English: For TV, how many times a week do you use it?

Indonesian: Untuk TV, berapa kali seminggu anda menggunakannya?

```python
## app_TV_per_wk
#survey['app_TV_per_wk'].value_counts(dropna=False)
survey['app_TV_per_wk'].describe()
```

## app_TV_hrs
English: For TV, each time you use it, how many hours do you use it for?

Indonesian: Untuk TV, selama berapa jam setiap kali anda menggunakannya?

```python
## app_TV_hrs
survey['app_TV_hrs'].value_counts(dropna=False)
survey['app_TV_hrs'].describe()
```

## app_TV_use_times
English: For TV, what time of the day do you typically use it?

Indonesian: Untuk TV, pada jam berapa biasanya anda menggunakannya?

```python
## app_TV_use_times
survey['app_TV_use_times'].value_counts(dropna=False)
#survey['app_TV_use_times'].describe()
```

## app_TV_use_times/morning

```python
## app_TV_use_times/morning
survey['app_TV_use_times/morning'].value_counts(dropna=False)
#survey['app_TV_use_times/morning'].describe()
```

```python
appmorning= pie_chart_boolean('app_TV_use_times/morning', survey, False)
```

## app_TV_use_times/mid_day

```python
## app_TV_use_times/mid_day
survey['app_TV_use_times/mid_day'].value_counts(dropna=False)
#survey['app_TV_use_times/mid_day'].describe()
```

```python
appTVmd= pie_chart_boolean('app_TV_use_times/mid_day', survey, False)
```

## app_TV_use_times/afternoon

```python
## app_TV_use_times/afternoon
survey['app_TV_use_times/afternoon'].value_counts(dropna=False)
#survey['app_TV_use_times/afternoon'].describe()
```

```python
appTVaftern= pie_chart_boolean('app_TV_use_times/afternoon', survey, False)
```

## app_TV_use_times/night

```python
## app_TV_use_times/night
survey['app_TV_use_times/night'].value_counts(dropna=False)
#survey['app_TV_use_times/night'].describe()
```

```python
appTVutn= pie_chart_boolean('app_TV_use_times/night', survey, False)
```

## app_radio_per_wk
English: For radio, how many times a week do you use it?

Indonesian: Untuk radio, berapa kali seminggu anda menggunakannya?

```python
## app_radio_per_wk
survey['app_radio_per_wk'].value_counts(dropna=False)
survey['app_radio_per_wk'].describe()
```

## app_radio_hrs
English: For radio, each time you use it, how many hours do you use it for?

Indonesian: Untuk radio, selama berapa jam setiap kali anda menggunakannya?

```python
## app_radio_hrs
survey['app_radio_hrs'].describe()
```

## app_radio_use_times
English: For radio, what time of the day do you typically use it?

Indonesian: Untuk radio, pada jam berapa biasanya anda menggunakannya?

```python
## app_radio_use_times
survey['app_radio_use_times'].value_counts(dropna=False)
```

## app_radio_use_times/morning

```python
## app_radio_use_times/morning
survey['app_radio_use_times/morning'].value_counts(dropna=False)
```

```python
apprutp= pie_chart_boolean('app_radio_use_times/morning', survey,False)
```

## app_radio_use_times/mid_day

```python
## app_radio_use_times/mid_day
survey['app_radio_use_times/mid_day'].value_counts(dropna=False)
```

```python
apprutmd= pie_chart_boolean('app_radio_use_times/mid_day', survey,False)
```

## app_radio_use_times/afternoon

```python
## app_radio_use_times/afternoon
survey['app_radio_use_times/afternoon'].value_counts(dropna=False)
```

```python
apprutaf= pie_chart_boolean('app_radio_use_times/afternoon', survey,False)
```

## app_radio_use_times/night

```python
## app_radio_use_times/night
survey['app_radio_use_times/night'].value_counts(dropna=False)
```

```python
apprutn= pie_chart_boolean('app_radio_use_times/night', survey,False)
```

## app_fridge_per_wk
TODO: deal with obvious outlier

English: For fridge, how many times a week do you use it?

Indonesian: Untuk kulkas, berapa kali seminggu anda menggunakannya?

```python
## app_fridge_per_wk
survey['app_fridge_per_wk'].value_counts(dropna=False)
#survey['app_fridge_per_wk'].describe()
```

## app_fridge_hrs
English: For fridge, each time you use it, how many hours do you use it for?

Indonesian: Untuk kulkas, selama berapa jam setiap kali anda menggunakannya?

```python
## app_fridge_hrs
survey['app_fridge_hrs'].value_counts(dropna=False)
```

## app_fridge_use_times
English: For fridge, what time of the day do you typically use it?

Indonesian: Untuk kulkas, pada jam berapa biasanya anda menggunakannya?

```python
## app_fridge_use_times
survey['app_fridge_use_times'].value_counts(dropna=False)
```

## app_fridge_use_times/morning

```python
## app_fridge_use_times/morning
survey['app_fridge_use_times/morning'].value_counts(dropna=False)
```

```python
appfutm= pie_chart_boolean('app_fridge_use_times/morning', survey,False)
```

## app_fridge_use_times/mid_day

```python
## app_fridge_use_times/mid_day
survey['app_fridge_use_times/mid_day'].value_counts(dropna=False)
```

```python
appfutmd= pie_chart_boolean('app_fridge_use_times/mid_day', survey,False)
```

## app_fridge_use_times/afternoon

```python
## app_fridge_use_times/afternoon
survey['app_fridge_use_times/afternoon'].value_counts(dropna=False)
```

```python
appfutm= pie_chart_boolean('app_fridge_use_times/afternoon', survey,False)
```

## app_fridge_use_times/night

```python
## app_fridge_use_times/night
survey['app_fridge_use_times/night'].value_counts(dropna=False)
```

```python
appfutn= pie_chart_boolean('app_fridge_use_times/night', survey,False)
```

## app_fan_per_wk
English: For fan, how many times a week do you use it?

Indonesian: Untuk kipas angin, berapa kali seminggu anda menggunakannya?

```python
## app_fan_per_wk
survey['app_fan_per_wk'].value_counts(dropna=False)
```

## app_fan_hrs
English: For fan, each time you use it, how many hours do you use it for?

Indonesian: Untuk kipas angin, selama berapa jam setiap kali anda
menggunakannya?

```python
## app_fan_hrs
survey['app_fan_hrs'].describe()
```

## app_fan_use_times
English: For fan, what time of the day do you typically use it?

Indonesian: Untuk kipas angin, pada jam berapa biasanya anda menggunakannya?

```python
## app_fan_use_times
survey['app_fan_use_times'].value_counts(dropna=False)
```

## app_fan_use_times/morning

```python
## app_fan_use_times/morning
survey['app_fan_use_times/morning'].value_counts(dropna=False)
```

```python
appFANuta= pie_chart_boolean('app_fan_use_times/morning', survey, False)
```

## app_fan_use_times/mid_day

```python
## app_fan_use_times/mid_day
survey['app_fan_use_times/mid_day'].value_counts(dropna=False)
```

```python
appFANutmd= pie_chart_boolean('app_fan_use_times/mid_day', survey, False)
```

## app_fan_use_times/afternoon

```python
## app_fan_use_times/afternoon
survey['app_fan_use_times/afternoon'].value_counts(dropna=False)
```

```python
appFANutaf= pie_chart_boolean('app_fan_use_times/afternoon', survey, False)
```

## app_fan_use_times/night

```python
## app_fan_use_times/night
survey['app_fan_use_times/night'].value_counts(dropna=False)
```

```python
appFANutnight= pie_chart_boolean('app_fan_use_times/night', survey, False)
```

## app_rice_cooker_per_wk
English: For rice cooker, how many times a week do you use it?

Indonesian: Untuk penanak nasi, berapa kali seminggu anda menggunakannya?

```python
## app_rice_cooker_per_wk
survey['app_rice_cooker_per_wk'].value_counts(dropna=False)
survey['app_rice_cooker_per_wk'].describe()
```

## app_rice_cooker_hrs
English: For rice cooker, each time you use it, how many hours do you use it
for?

Indonesian: Untuk penanak nasi, selama berapa jam setiap kali anda
menggunakannya?

```python
## app_rice_cooker_hrs
survey['app_rice_cooker_hrs'].value_counts(dropna=False)
survey['app_rice_cooker_hrs'].describe()
```

## app_rice_cooker_use_times
English: For rice cooker, what time of the day do you typically use it?

Indonesian: Untuk penanak nasi, pada jam berapa biasanya anda menggunakannya?

```python
## app_rice_cooker_use_times
survey['app_rice_cooker_use_times'].value_counts(dropna=False)
```

## app_rice_cooker_use_times/morning

```python
## app_rice_cooker_use_times/morning
survey['app_rice_cooker_use_times/morning'].value_counts(dropna=False)
```

```python
appRCutm= pie_chart_boolean('app_rice_cooker_use_times/morning', survey, False)
```

## app_rice_cooker_use_times/mid_day

```python
## app_rice_cooker_use_times/mid_day
survey['app_rice_cooker_use_times/mid_day'].value_counts(dropna=False)
```

```python
appRCutmd= pie_chart_boolean('app_rice_cooker_use_times/mid_day', survey, False)
```

## app_rice_cooker_use_times/afternoon

```python
## app_rice_cooker_use_times/afternoon
survey['app_rice_cooker_use_times/afternoon'].value_counts(dropna=False)
```

```python
appRCutaf= pie_chart_boolean('app_rice_cooker_use_times/afternoon', survey, False)
```

## app_rice_cooker_use_times/night

```python
## app_rice_cooker_use_times/night
survey['app_rice_cooker_use_times/night'].value_counts(dropna=False)
```

```python
appRCutn= pie_chart_boolean('app_rice_cooker_use_times/night', survey, False)
```

## app_other_cooking_per_wk
English: For ${app_other_cooking_desc} ("other cooking"), how many times a week
do you use it?

Indonesian: Untuk ${app_other_cooking_desc} (masakan yang lain), berapakali
seminggu anda menggunakannya?

```python
## app_other_cooking_per_wk
survey['app_other_cooking_per_wk'].value_counts(dropna=False)
survey['app_other_cooking_per_wk'].describe()
```

## app_other_cooking_hrs
English:  For ${app_other_cooking_desc} ("other cooking"), each time you use it,
how many hours do you use it for?

Indonesian: Untuk ${app_other_cooking_desc} (masakan yang lain), selama berapa
jam setiap kali anda menggunakannya?

```python
## app_other_cooking_hrs
survey['app_other_cooking_hrs'].value_counts(dropna=False)
survey['app_other_cooking_hrs'].describe()
```

## app_other_cooking_use_times
English: For ${app_other_cooking_desc} ("other cooking"), what time of the day
do you typically use it?

Indonesian: Untuk ${app_other_cooking_desc} (masakan yang lain), pada jam berapa
biasanya anda menggunakannya?

```python
## app_other_cooking_use_times
survey['app_other_cooking_use_times'].value_counts(dropna=False)
```

## app_other_cooking_use_times/morning

```python
## app_other_cooking_use_times/morning
survey['app_other_cooking_use_times/morning'].value_counts(dropna=False)
```

## app_other_cooking_use_times/mid_day

```python
## app_other_cooking_use_times/mid_day
survey['app_other_cooking_use_times/mid_day'].value_counts(dropna=False)
```

## app_other_cooking_use_times/afternoon

```python
## app_other_cooking_use_times/afternoon
survey['app_other_cooking_use_times/afternoon'].value_counts(dropna=False)
```

## app_other_cooking_use_times/night

```python
## app_other_cooking_use_times/night
survey['app_other_cooking_use_times/night'].value_counts(dropna=False)
```

## app_welder_per_wk
English: For welder, how many times a week do you use it?

Indonesian: Untuk mesin las, berapa kali seminggu anda menggunakannya?

```python
## app_welder_per_wk
survey['app_welder_per_wk'].value_counts(dropna=False)
survey['app_welder_per_wk'].describe()
```

## app_welder_hrs
English:  For welder, each time you use it, how many hours do you use it for?

Indonesian: Untuk mesin las, selama berapa jam setiap kali anda menggunakannya?

```python
## app_welder_hrs
survey['app_welder_hrs'].value_counts(dropna=False)
survey['app_welder_hrs'].describe()
```

## app_welder_use_times
English: For welder, what time of the day do you typically use it?

Indonesian: Untuk mesin las, pada jam berapa biasanya anda menggunakannya?

```python
## app_welder_use_times
survey['app_welder_use_times'].value_counts(dropna=False)
#survey['app_welder_use_times'].describe()
```

## app_welder_use_times/morning

```python
## app_welder_use_times/morning
survey['app_welder_use_times/morning'].value_counts(dropna=False)
```

## app_welder_use_times/mid_day

```python
## app_welder_use_times/mid_day
survey['app_welder_use_times/mid_day'].value_counts(dropna=False)
```

## app_welder_use_times/afternoon

```python
## app_welder_use_times/afternoon
survey['app_welder_use_times/afternoon'].value_counts(dropna=False)
```

## app_welder_use_times/night

```python
## app_welder_use_times/night
survey['app_welder_use_times/night'].value_counts(dropna=False)
```

## app_grinder_per_wk
English: For grinder, how many times a week do you use it?

Indonesian: Untuk mesin penggiling, berapa kali seminggu anda menggunakannya?

```python
## app_grinder_per_wk
survey['app_grinder_per_wk'].value_counts(dropna=False)
survey['app_grinder_per_wk'].describe()
```

## app_grinder_hrs
English: For grinder, each time you use it, how many hours do you use it for?

Indonesian: Untuk mesin penggiling, selama berapa jam setiap kali anda
menggunakannya?

```python
## app_grinder_hrs
survey['app_grinder_hrs'].value_counts(dropna=False)
```

## app_grinder_use_times
English: For grinder, what time of the day do you typically use it?

Indonesian: Untuk mesin penggiling, pada jam berapa biasanya anda
menggunakannya?

```python
## app_grinder_use_times
survey['app_grinder_use_times'].value_counts(dropna=False)
```

## app_grinder_use_times/morning

```python
## app_grinder_use_times/morning
survey['app_grinder_use_times/morning'].value_counts(dropna=False)
```

## app_grinder_use_times/mid_day

```python
## app_grinder_use_times/mid_day
survey['app_grinder_use_times/mid_day'].value_counts(dropna=False)
```

## app_grinder_use_times/afternoon

```python
## app_grinder_use_times/afternoon
survey['app_grinder_use_times/afternoon'].value_counts(dropna=False)
```

## app_grinder_use_times/night

```python
## app_grinder_use_times/night
survey['app_grinder_use_times/night'].value_counts(dropna=False)
```

## app_saw_per_wk
English:  For saw, how many times a week do you use it?

Indonesian: Untuk mesin gergaji, berapa kali seminggu anda menggunakannya?

```python
## app_saw_per_wk
survey['app_saw_per_wk'].value_counts(dropna=False)
survey['app_saw_per_wk'].describe()
```

## app_saw_hrs
English: For saw, each time you use it, how many hours do you use it for?

Indonesian: Untuk mesin gergaji, selama berapa jam setiap kali anda
menggunakannya?

```python
## app_saw_hrs
survey['app_saw_hrs'].value_counts(dropna=False)
survey['app_saw_hrs'].describe()
```

## app_saw_use_times
English: For saw, what time of the day do you typically use it?

Indonesian: Untuk mesin gergaji, pada jam berapa biasanya anda menggunakannya?

```python
## app_saw_use_times
survey['app_saw_use_times'].value_counts(dropna=False)
```

## app_saw_use_times/morning

```python
## app_saw_use_times/morning
survey['app_saw_use_times/morning'].value_counts(dropna=False)
```

## app_saw_use_times/mid_day

```python
## app_saw_use_times/mid_day
survey['app_saw_use_times/mid_day'].value_counts(dropna=False)
```

## app_saw_use_times/afternoon

```python
## app_saw_use_times/afternoon
survey['app_saw_use_times/afternoon'].value_counts(dropna=False)
```

## app_saw_use_times/night

```python
## app_saw_use_times/night
survey['app_saw_use_times/night'].value_counts(dropna=False)
```

## app_other_tools_per_wk
English: For ${app_other_tools_desc} ("other tools") how many times a week do
you use it?

Indonesian: Untuk ${app_other_tools_desc} (alat-alat lain") berapa kali seminggu
anda menggunakannya?

```python
## app_other_tools_per_wk
survey['app_other_tools_per_wk'].value_counts(dropna=False)
survey['app_other_tools_per_wk'].describe()
```

## app_other_tools_hrs
English: For ${app_other_tools_desc} ("other tools"), each time you use it, how
many hours do you use it for?

Indonesian: Untuk ${app_other_tools_desc} (alat-alat lain"), selama berapa jam
setiap kali anda menggunakannya?

```python
## app_other_tools_hrs
survey['app_other_tools_hrs'].value_counts(dropna=False)
survey['app_other_tools_hrs'].describe()
```

## app_other_tools_use_times
English: For ${app_other_tools_desc} ("other tools"), what time of the day do
you typically use it?

Indonesian: Untuk ${app_other_tools_desc} (alat-alat lain"), jam berapa biasanya
anda menggunakannya?

```python
## app_other_tools_use_times
survey['app_other_tools_use_times'].value_counts(dropna=False)
```

## app_other_tools_use_times/morning

```python
## app_other_tools_use_times/morning
survey['app_other_tools_use_times/morning'].value_counts(dropna=False)
```

## app_other_tools_use_times/mid_day

```python
## app_other_tools_use_times/mid_day
survey['app_other_tools_use_times/mid_day'].value_counts(dropna=False)
```

## app_other_tools_use_times/afternoon

```python
## app_other_tools_use_times/afternoon
survey['app_other_tools_use_times/afternoon'].value_counts(dropna=False)
```

## app_other_tools_use_times/night

```python
## app_other_tools_use_times/night
survey['app_other_tools_use_times/night'].value_counts(dropna=False)
```

## app_other_per_wk
English: For ${app_other_desc} ("any other"), how many times a week do you use
it?

Indonesian: Untuk ${app_other_desc} ("ada yang lain"), berapa kali seminggu anda
menggunakannya?

```python
## app_other_per_wk
survey['app_other_per_wk'].value_counts(dropna=False)
survey['app_other_per_wk'].describe()
```

## app_other_hrs
English:  For ${app_other_desc} ("any other"), each time you use it, how many
hours do you use it for?

Indonesian: Untuk ${app_other_desc} ("ada yang lain"), selama berapa jam setiap
kali anda menggunakannya?

```python
## app_other_hrs
survey['app_other_hrs'].value_counts(dropna=False)
survey['app_other_hrs'].describe()
```

## app_other_use_times
English:  For ${app_other_desc} ("any other"), what time of the day do you
typically use it?

Indonesian: Untuk ${app_other_desc} ("ada yang lain"), jam berapa biasannya anda
menggunakannya?

```python
## app_other_use_times
survey['app_other_use_times'].value_counts(dropna=False)
```

## app_other_use_times/morning

```python
## app_other_use_times/morning
survey['app_other_use_times/morning'].value_counts(dropna=False)
```

## app_other_use_times/mid_day

```python
## app_other_use_times/mid_day
survey['app_other_use_times/mid_day'].value_counts(dropna=False)
```

## app_other_use_times/afternoon

```python
## app_other_use_times/afternoon
survey['app_other_use_times/afternoon'].value_counts(dropna=False)
```

## app_other_use_times/night

```python
## app_other_use_times/night
survey['app_other_use_times/night'].value_counts(dropna=False)
```
