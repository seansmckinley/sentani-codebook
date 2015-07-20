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

## section_05

This section surveys appliance ownership information.

## app_now

select_multiple appliance_list

```python
## app_now
survey['app_now'].value_counts(dropna=False)
#survey['app_now'].describe()
```

## app_now/lighting

```python
## app_now/lighting
survey['app_now/lighting'].value_counts(dropna=False)
#survey['app_now/lighting'].describe()
```

## app_now/TV

```python
## app_now/TV
survey['app_now/TV'].value_counts(dropna=False)
```

## app_now/radio

```python
## app_now/radio
survey['app_now/radio'].value_counts(dropna=False)
```

## app_now/fridge

```python
## app_now/fridge
survey['app_now/fridge'].value_counts(dropna=False)
```

## app_now/fan

```python
## app_now/fan
survey['app_now/fan'].value_counts(dropna=False)
```

## app_now/rice_cooker

```python
## app_now/rice_cooker
survey['app_now/rice_cooker'].value_counts(dropna=False)
```

## app_now/other_cooking

```python
## app_now/other_cooking
survey['app_now/other_cooking'].value_counts(dropna=False)
```

## app_now/welder

```python
## app_now/welder
survey['app_now/welder'].value_counts(dropna=False)
```

## app_now/grinder

```python
## app_now/grinder
survey['app_now/grinder'].value_counts(dropna=False)
```

## app_now/saw

```python
## app_now/saw
survey['app_now/saw'].value_counts(dropna=False)
```

## app_now/other_tools

```python
## app_now/other_tools
survey['app_now/other_tools'].value_counts(dropna=False)
```

## app_now/other

```python
## app_now/other
survey['app_now/other'].value_counts(dropna=False)
```

## app_other_cooking_desc

```python
## app_other_cooking_desc
survey['app_other_cooking_desc'].value_counts(dropna=False)
#survey['app_other_cooking_desc'].describe()
```

## app_other_tools_desc

```python
## app_other_tools_desc
survey['app_other_tools_desc'].value_counts(dropna=False)
#survey['app_other_tools_desc'].describe()
```

## app_other_desc

```python
## app_other_desc
survey['app_other_desc'].value_counts(dropna=False)
#survey['app_other_desc'].describe()
```

## app_lighting_per_wk
Question: For lighting, how many times a week do you use it?

```python
## app_lighting_per_wk
survey['app_lighting_per_wk'].value_counts(dropna=False)
survey['app_lighting_per_wk'].describe()
```

## app_lighting_hrs
Question: For lighting, each time you use it, how many hours do you use it for?

```python
## app_lighting_hrs
survey['app_lighting_hrs'].value_counts(dropna=False)
survey['app_lighting_hrs'].describe()
```

## app_lighting_use_times

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

## app_lighting_use_times/night

```python
## app_lighting_use_times/night
survey['app_lighting_use_times/night'].value_counts(dropna=False)

```

## app_TV_per_wk

```python
## app_TV_per_wk
#survey['app_TV_per_wk'].value_counts(dropna=False)
survey['app_TV_per_wk'].describe()
```

## app_TV_hrs

```python
## app_TV_hrs
survey['app_TV_hrs'].value_counts(dropna=False)
survey['app_TV_hrs'].describe()
```

## app_TV_use_times

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

## app_TV_use_times/mid_day

```python
## app_TV_use_times/mid_day
survey['app_TV_use_times/mid_day'].value_counts(dropna=False)
#survey['app_TV_use_times/mid_day'].describe()
```

## app_TV_use_times/afternoon

```python
## app_TV_use_times/afternoon
survey['app_TV_use_times/afternoon'].value_counts(dropna=False)
#survey['app_TV_use_times/afternoon'].describe()
```

## app_TV_use_times/night

```python
## app_TV_use_times/night
survey['app_TV_use_times/night'].value_counts(dropna=False)
#survey['app_TV_use_times/night'].describe()
```

## app_radio_per_wk

```python
## app_radio_per_wk
survey['app_radio_per_wk'].value_counts(dropna=False)
survey['app_radio_per_wk'].describe()
```

## app_radio_hrs

```python
## app_radio_hrs
survey['app_radio_hrs'].describe()
```

## app_radio_use_times

```python
## app_radio_use_times
survey['app_radio_use_times'].value_counts(dropna=False)
```

## app_radio_use_times/morning

```python
## app_radio_use_times/morning
survey['app_radio_use_times/morning'].value_counts(dropna=False)
```

## app_radio_use_times/mid_day

```python
## app_radio_use_times/mid_day
survey['app_radio_use_times/mid_day'].value_counts(dropna=False)
```

## app_radio_use_times/afternoon

```python
## app_radio_use_times/afternoon
survey['app_radio_use_times/afternoon'].value_counts(dropna=False)
```

## app_radio_use_times/night

```python
## app_radio_use_times/night
survey['app_radio_use_times/night'].value_counts(dropna=False)
```

## app_fridge_per_wk

TODO: deal with obvious outlier

```python
## app_fridge_per_wk
survey['app_fridge_per_wk'].value_counts(dropna=False)
#survey['app_fridge_per_wk'].describe()
```

## app_fridge_hrs

```python
## app_fridge_hrs
survey['app_fridge_hrs'].value_counts(dropna=False)
```

## app_fridge_use_times

```python
## app_fridge_use_times
survey['app_fridge_use_times'].value_counts(dropna=False)
```

## app_fridge_use_times/morning

```python
## app_fridge_use_times/morning
survey['app_fridge_use_times/morning'].value_counts(dropna=False)
```

## app_fridge_use_times/mid_day

```python
## app_fridge_use_times/mid_day
survey['app_fridge_use_times/mid_day'].value_counts(dropna=False)
```

## app_fridge_use_times/afternoon

```python
## app_fridge_use_times/afternoon
survey['app_fridge_use_times/afternoon'].value_counts(dropna=False)
```

## app_fridge_use_times/night

```python
## app_fridge_use_times/night
survey['app_fridge_use_times/night'].value_counts(dropna=False)
```

## app_fan_per_wk

```python
## app_fan_per_wk
survey['app_fan_per_wk'].value_counts(dropna=False)
```

## app_fan_hrs

```python
## app_fan_hrs
survey['app_fan_hrs'].describe()
```

## app_fan_use_times

```python
## app_fan_use_times
survey['app_fan_use_times'].value_counts(dropna=False)
```

## app_fan_use_times/morning

```python
## app_fan_use_times/morning
survey['app_fan_use_times/morning'].value_counts(dropna=False)
```

## app_fan_use_times/mid_day

```python
## app_fan_use_times/mid_day
survey['app_fan_use_times/mid_day'].value_counts(dropna=False)
```

## app_fan_use_times/afternoon

```python
## app_fan_use_times/afternoon
survey['app_fan_use_times/afternoon'].value_counts(dropna=False)
```

## app_fan_use_times/night

```python
## app_fan_use_times/night
survey['app_fan_use_times/night'].value_counts(dropna=False)
```

## app_rice_cooker_per_wk

```python
## app_rice_cooker_per_wk
survey['app_rice_cooker_per_wk'].value_counts(dropna=False)
survey['app_rice_cooker_per_wk'].describe()
```

## app_rice_cooker_hrs

```python
## app_rice_cooker_hrs
survey['app_rice_cooker_hrs'].value_counts(dropna=False)
survey['app_rice_cooker_hrs'].describe()
```

## app_rice_cooker_use_times

```python
## app_rice_cooker_use_times
survey['app_rice_cooker_use_times'].value_counts(dropna=False)
```

## app_rice_cooker_use_times/morning

```python
## app_rice_cooker_use_times/morning
survey['app_rice_cooker_use_times/morning'].value_counts(dropna=False)
```

## app_rice_cooker_use_times/mid_day

```python
## app_rice_cooker_use_times/mid_day
survey['app_rice_cooker_use_times/mid_day'].value_counts(dropna=False)
```

## app_rice_cooker_use_times/afternoon

```python
## app_rice_cooker_use_times/afternoon
survey['app_rice_cooker_use_times/afternoon'].value_counts(dropna=False)
```

## app_rice_cooker_use_times/night

```python
## app_rice_cooker_use_times/night
survey['app_rice_cooker_use_times/night'].value_counts(dropna=False)
```

## app_other_cooking_per_wk

```python
## app_other_cooking_per_wk
survey['app_other_cooking_per_wk'].value_counts(dropna=False)
survey['app_other_cooking_per_wk'].describe()
```

## app_other_cooking_hrs

```python
## app_other_cooking_hrs
survey['app_other_cooking_hrs'].value_counts(dropna=False)
survey['app_other_cooking_hrs'].describe()
```

## app_other_cooking_use_times

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

```python
## app_welder_per_wk
survey['app_welder_per_wk'].value_counts(dropna=False)
survey['app_welder_per_wk'].describe()
```

## app_welder_hrs

```python
## app_welder_hrs
survey['app_welder_hrs'].value_counts(dropna=False)
survey['app_welder_hrs'].describe()
```

## app_welder_use_times

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

```python
## app_grinder_per_wk
survey['app_grinder_per_wk'].value_counts(dropna=False)
survey['app_grinder_per_wk'].describe()
```

## app_grinder_hrs

```python
## app_grinder_hrs
survey['app_grinder_hrs'].value_counts(dropna=False)
```

## app_grinder_use_times

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

```python
## app_saw_per_wk
survey['app_saw_per_wk'].value_counts(dropna=False)
survey['app_saw_per_wk'].describe()
```

## app_saw_hrs

```python
## app_saw_hrs
survey['app_saw_hrs'].value_counts(dropna=False)
survey['app_saw_hrs'].describe()
```

## app_saw_use_times

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

```python
## app_other_tools_per_wk
survey['app_other_tools_per_wk'].value_counts(dropna=False)
survey['app_other_tools_per_wk'].describe()
```

## app_other_tools_hrs

```python
## app_other_tools_hrs
survey['app_other_tools_hrs'].value_counts(dropna=False)
survey['app_other_tools_hrs'].describe()
```

## app_other_tools_use_times

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

```python
## app_other_per_wk
survey['app_other_per_wk'].value_counts(dropna=False)
survey['app_other_per_wk'].describe()
```

## app_other_hrs

```python
## app_other_hrs
survey['app_other_hrs'].value_counts(dropna=False)
survey['app_other_hrs'].describe()
```

## app_other_use_times

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
