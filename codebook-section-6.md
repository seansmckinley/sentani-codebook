```{.python .input  n=1}
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

```{.python .input  n=2}
survey = get_survey()
print('number of entries =', len(survey))
print('number of columns =', len(survey.columns))
```

```{.json .output n=2}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "number of entries = 1184\nnumber of columns = 274\n"
 }
]
```

## section_06

This section asks households about what appliances they are interested in
purchasing in the future.

##app_buy
English: What additional appliances do you plan to buy, or would like to buy?

Indonesian: Peralatan tambahan apa yang anda rencanakan untuk dibeli, atau ingin
anda beli?

```{.python .input  n=3}
survey['app_buy'].value_counts(dropna=False)
#survey['app_buy'].describe()
```

```{.json .output n=3}
[
 {
  "data": {
   "text/plain": "NaN                                                                       386\nother                                                                     142\nfridge                                                                     84\nTV                                                                         40\nfridge other                                                               38\nfridge rice_cooker                                                         34\nlighting other                                                             26\nlighting fridge other                                                      19\nlighting TV                                                                18\nTV fridge                                                                  18\nrice_cooker                                                                14\nfridge fan                                                                 14\nlighting                                                                   12\nfridge other_tools                                                         11\nother_tools                                                                11\nother_cooking                                                              10\nfan rice_cooker                                                            10\nlighting TV radio                                                           9\nTV other                                                                    9\nTV fridge rice_cooker                                                       9\nlighting fridge fan rice_cooker other                                       9\nlighting fridge                                                             8\nTV radio                                                                    8\nfridge rice_cooker other                                                    8\nlighting fan                                                                7\nfridge fan rice_cooker                                                      7\nradio fridge                                                                6\nfridge rice_cooker other_cooking                                            5\nlighting fridge fan rice_cooker                                             5\nradio                                                                       5\n                                                                         ... \nTV fridge other_cooking                                                     1\nlighting welder other                                                       1\nlighting TV fridge fan rice_cooker other_cooking other                      1\nfan grinder                                                                 1\nlighting fan rice_cooker                                                    1\nfridge grinder                                                              1\nlighting radio fridge fan rice_cooker other                                 1\nradio rice_cooker                                                           1\nlighting TV fan other                                                       1\nother_cooking other                                                         1\nradio other_cooking                                                         1\nlighting TV radio fridge other                                              1\nradio fridge rice_cooker other                                              1\nTV fridge fan rice_cooker                                                   1\nlighting fridge other_tools other                                           1\nlighting TV fridge fan                                                      1\nlighting TV radio fan rice_cooker other                                     1\nTV other_cooking                                                            1\nlighting TV radio fridge fan rice_cooker other_tools                        1\nlighting fan other_tools                                                    1\nfridge fan saw                                                              1\nfridge fan rice_cooker other_cooking                                        1\nlighting radio fridge fan other                                             1\nlighting radio fridge rice_cooker                                           1\nlighting TV fridge fan rice_cooker other_tools                              1\nfan other_cooking other_tools                                               1\nTV radio fridge fan rice_cooker other_cooking saw other                     1\nfridge welder saw                                                           1\nlighting TV radio fridge fan rice_cooker other_cooking saw other_tools      1\nTV fridge other_tools                                                       1\ndtype: int64"
  },
  "execution_count": 3,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy/lighting
English: Lighting.

Indonesian: P
enerangan.

```{.python .input  n=4}
survey['app_buy/lighting'].value_counts(dropna=False)
```

```{.json .output n=4}
[
 {
  "data": {
   "text/plain": " 0     575\nNaN    386\n 1     223\ndtype: int64"
  },
  "execution_count": 4,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy/TV
English: TV.

Indonesian: TV.

```{.python .input  n=5}
survey['app_buy/TV'].value_counts(dropna=False)
```

```{.json .output n=5}
[
 {
  "data": {
   "text/plain": " 0     614\nNaN    386\n 1     184\ndtype: int64"
  },
  "execution_count": 5,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy/radio
English: Radio.

Indonesian: Radio.

```{.python .input  n=6}
survey['app_buy/radio'].value_counts(dropna=False)
```

```{.json .output n=6}
[
 {
  "data": {
   "text/plain": " 0     696\nNaN    386\n 1     102\ndtype: int64"
  },
  "execution_count": 6,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy/fridge
English: Fridge.

Indonesian: Kulkas.

```{.python .input  n=7}
survey['app_buy/fridge'].value_counts(dropna=False)
```

```{.json .output n=7}
[
 {
  "data": {
   "text/plain": " 0     427\nNaN    386\n 1     371\ndtype: int64"
  },
  "execution_count": 7,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy/fan
English: Fan.

Indonesian: Kipas angin.

```{.python .input  n=8}
survey['app_buy/fan'].value_counts(dropna=False)
```

```{.json .output n=8}
[
 {
  "data": {
   "text/plain": " 0     647\nNaN    386\n 1     151\ndtype: int64"
  },
  "execution_count": 8,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

##app_buy/rice_cooker
English: Rice Cooker.

Indonesian: Penanak nasi.

```{.python .input  n=9}
survey['app_buy/rice_cooker'].value_counts(dropna=False)
```

```{.json .output n=9}
[
 {
  "data": {
   "text/plain": " 0     606\nNaN    386\n 1     192\ndtype: int64"
  },
  "execution_count": 9,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy/other_cooking
English: Other cooking related.

Indonesian: Masakan lain yang sejenis.

```{.python .input  n=10}
survey['app_buy/other_cooking'].value_counts(dropna=False)
```

```{.json .output n=10}
[
 {
  "data": {
   "text/plain": " 0     743\nNaN    386\n 1      55\ndtype: int64"
  },
  "execution_count": 10,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy/welder
English: Welder.

Indonesian: Mesin las.

```{.python .input  n=11}
survey['app_buy/welder'].value_counts(dropna=False)
```

```{.json .output n=11}
[
 {
  "data": {
   "text/plain": " 0     795\nNaN    386\n 1       3\ndtype: int64"
  },
  "execution_count": 11,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

##app_buy/grinder
English: Grinder.

Indonesian: Mesin penggiling.

```{.python .input  n=12}
survey['app_buy/grinder'].value_counts(dropna=False)
```

```{.json .output n=12}
[
 {
  "data": {
   "text/plain": " 0     795\nNaN    386\n 1       3\ndtype: int64"
  },
  "execution_count": 12,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy/saw
English: Saw.

Indonesian: Mesin gergaji.

```{.python .input  n=13}
survey['app_buy/saw'].value_counts(dropna=False)
```

```{.json .output n=13}
[
 {
  "data": {
   "text/plain": " 0     787\nNaN    386\n 1      11\ndtype: int64"
  },
  "execution_count": 13,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

##app_buy/other_tools
English: Other tools related.

Indonesian: Alat - alat lain yang sejenis.

```{.python .input  n=14}
survey['app_buy/other_tools'].value_counts(dropna=False)
```

```{.json .output n=14}
[
 {
  "data": {
   "text/plain": " 0     751\nNaN    386\n 1      47\ndtype: int64"
  },
  "execution_count": 14,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

##app_buy/other
English: Any other.

Indonesian: Ada yang lain.

```{.python .input  n=15}
survey['app_buy/other'].value_counts(dropna=False)
```

```{.json .output n=15}
[
 {
  "data": {
   "text/plain": " 0     471\nNaN    386\n 1     327\ndtype: int64"
  },
  "execution_count": 15,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_other
English: Please describe what you meant by "other."

Indonesian: Jelaskanlah apa yang anda maksud dengan "lain - lain."

```{.python .input  n=16}
survey['app_buy_other'].value_counts(dropna=False)
```

```{.json .output n=16}
[
 {
  "data": {
   "text/plain": "NaN                                                 859\nMesin cuci                                          100\nMesin cuci.                                          14\nDispenser                                            10\nKentinting                                            8\nMesin Cuci                                            7\nGengset                                               7\nGenset                                                3\nTidak ada                                             3\nVcd                                                   3\nOven listrik                                          2\nMesin dap                                             2\nDigital                                               2\nMesin cuci dan msn pompa air.                         2\nMesin cuci pakean                                     2\nSound system                                          2\nPompa air                                             2\nMesin Air                                             2\nIngin punya meteran sendiri                           2\nMotor jonson                                          2\nJonson                                                2\nMesin cuci dan dispenser.                             2\nMotor jonson atau motor tempel                        2\nSpeaker                                               2\nMesin cuci pakaian                                    1\nSound System                                          1\nFriser (pendingin/pembeku)                            1\nMesin sensor kayu                                     1\nMesin dap/pompa air dan mesin cuci.                   1\nDap atau mesin air ( Sanyo ) ,mesin cuci pakaian      1\n                                                   ... \nMesin cuci,kulkas                                     1\nAmplifier  dan Mesin Cuci                             1\nKurinda batu, mesin cuci                              1\nMesin cuci,penanak nasi kulkas                        1\nDvd, dispenser dan mesin cuci.                        1\nDispenser                                             1\nMesin cuci dan mesin jahit                            1\nDispenser.                                            1\nPerbaiki tv yang rusak                                1\nStrika listrik, teap,mesin Cuci,                      1\nMesin cuci, dispenser dan reskuker.                   1\nParabola dan resifer.                                 1\nGengset pribadi                                       1\nToa                                                   1\nWidsed                                                1\nMesin cuci dan msn dap/pompa air.                     1\nMesin sagu                                            1\nDvd, kulkas, penanas masi dan mesin cuci.             1\nSkap srom                                             1\nSpiker/salon. Mesin cuci.                             1\nDvd dan mesin cuci.                                   1\nKeyboard ( Organ )\\nMesin Cuci                        1\nMesin cuci dan strika.                                1\nDispenser dan reskuker.                               1\nStrika                                                1\nParabola. Mesin cuci. Dispenser.                      1\nJaring, mesin cuci                                    1\nSpiket.                                               1\nSpeaker Aktif                                         1\nKetinting gengset                                     1\ndtype: int64"
  },
  "execution_count": 16,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_imm
English: If you had electricity, which appliances would you buy immediately?

Indonesian: Jika anda punya listrik, peralatan yang mana  yang mau anda beli
segera?

```{.python .input  n=17}
survey['app_buy_if_elec_imm'].value_counts(dropna=False)
```

```{.json .output n=17}
[
 {
  "data": {
   "text/plain": "NaN                                                   1122\nfridge other                                             5\nother                                                    5\nTV                                                       5\nlighting TV radio                                        4\nlighting                                                 3\nother_tools                                              3\nlighting TV rice_cooker                                  2\nfan                                                      2\nlighting TV other                                        2\nTV radio                                                 2\nfridge rice_cooker other_cooking other                   2\nTV other                                                 2\nfridge fan rice_cooker                                   2\nfridge fan rice_cooker other                             1\nrice_cooker other                                        1\nradio                                                    1\nfridge fan rice_cooker other_tools                       1\nTV fridge fan                                            1\nTV fridge                                                1\nTV radio fridge fan rice_cooker saw other                1\nlighting TV fridge rice_cooker other_cooking other       1\nlighting fan other                                       1\nlighting TV radio fridge fan other                       1\nfridge rice_cooker other                                 1\nfridge                                                   1\nlighting fridge                                          1\nlighting TV fridge                                       1\nfridge rice_cooker                                       1\nradio rice_cooker other_tools                            1\nTV radio other                                           1\nlighting radio fridge fan                                1\nlighting TV radio other                                  1\nlighting TV fridge rice_cooker                           1\nrice_cooker                                              1\nwelder other_tools                                       1\nlighting TV                                              1\ndtype: int64"
  },
  "execution_count": 17,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_imm/lighting
English: Lighting.

Indonesian: Penerangan.

```{.python .input  n=18}
survey['app_buy_if_elec_imm/lighting'].value_counts(dropna=False)
```

```{.json .output n=18}
[
 {
  "data": {
   "text/plain": "NaN    1122\n 0       42\n 1       20\ndtype: int64"
  },
  "execution_count": 18,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_imm/TV
English: TV.

Indonesian: TV.

```{.python .input  n=19}
survey['app_buy_if_elec_imm/TV'].value_counts(dropna=False)
```

```{.json .output n=19}
[
 {
  "data": {
   "text/plain": "NaN    1122\n 0       35\n 1       27\ndtype: int64"
  },
  "execution_count": 19,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_imm/radio
English: Radio.

Indonesian: Radio.

```{.python .input  n=20}
survey['app_buy_if_elec_imm/radio'].value_counts(dropna=False)
```

```{.json .output n=20}
[
 {
  "data": {
   "text/plain": "NaN    1122\n 0       49\n 1       13\ndtype: int64"
  },
  "execution_count": 20,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_imm/fridge
English: Fridge.

Indonesian: Kulkas.

```{.python .input  n=21}
survey['app_buy_if_elec_imm/fridge'].value_counts(dropna=False)
```

```{.json .output n=21}
[
 {
  "data": {
   "text/plain": "NaN    1122\n 0       39\n 1       23\ndtype: int64"
  },
  "execution_count": 21,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_imm/fan
English: Fan.

Indonesian: Kipas angin.

```{.python .input  n=22}
survey['app_buy_if_elec_imm/fan'].value_counts(dropna=False)
```

```{.json .output n=22}
[
 {
  "data": {
   "text/plain": "NaN    1122\n 0       51\n 1       11\ndtype: int64"
  },
  "execution_count": 22,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_imm/rice_cooker
English: Rice cooker.

Indonesian: Penanak nasi.

```{.python .input  n=24}
survey['app_buy_if_elec_imm/rice_cooker'].value_counts(dropna=False)
```

```{.json .output n=24}
[
 {
  "data": {
   "text/plain": "NaN    1122\n 0       46\n 1       16\ndtype: int64"
  },
  "execution_count": 24,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_imm/other_cooking
English: Other cooking related.

Indonesian: Masakan lain yang sejenis.

```{.python .input  n=25}
survey['app_buy_if_elec_imm/other_cooking'].value_counts(dropna=False)
```

```{.json .output n=25}
[
 {
  "data": {
   "text/plain": "NaN    1122\n 0       59\n 1        3\ndtype: int64"
  },
  "execution_count": 25,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_imm/welder
English: Welder.

Indonesian: Mesin las.

```{.python .input  n=26}
survey['app_buy_if_elec_imm/welder'].value_counts(dropna=False)
```

```{.json .output n=26}
[
 {
  "data": {
   "text/plain": "NaN    1122\n 0       61\n 1        1\ndtype: int64"
  },
  "execution_count": 26,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_imm/grinder
English: Grinder.

Indonesian: Mesin penggiling.

```{.python .input  n=27}
survey['app_buy_if_elec_imm/grinder'].value_counts(dropna=False)
```

```{.json .output n=27}
[
 {
  "data": {
   "text/plain": "NaN    1122\n 0       62\ndtype: int64"
  },
  "execution_count": 27,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_imm/saw
English: Saw.

Indonesian: Mesin gergaji.

```{.python .input  n=28}
survey['app_buy_if_elec_imm/saw'].value_counts(dropna=False)
```

```{.json .output n=28}
[
 {
  "data": {
   "text/plain": "NaN    1122\n 0       61\n 1        1\ndtype: int64"
  },
  "execution_count": 28,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_imm/other_tools
English: Other tools related.

Indonesian: Alat - alat lain yang sejenis.

```{.python .input  n=32}
survey['app_buy_if_elec_imm/other_tools'].value_counts(dropna=False)
##survey['app_buy_if_elec_imm/other_tools'].describe()
```

```{.json .output n=32}
[
 {
  "data": {
   "text/plain": "NaN    1122\n 0       56\n 1        6\ndtype: int64"
  },
  "execution_count": 32,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_imm/other
English: Any other.

Indonesian: Ada yang lain.

```{.python .input  n=34}
survey['app_buy_if_elec_imm/other'].value_counts(dropna=False)
##survey['app_buy_if_elec_imm/other'].describe()
```

```{.json .output n=34}
[
 {
  "data": {
   "text/plain": "NaN    1122\n 0       37\n 1       25\ndtype: int64"
  },
  "execution_count": 34,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_imm_other
English: Please describe what you meant by "other."

Indonesian: Jelaskanlah apa yang anda maksud dengan "lain - lain."

```{.python .input  n=40}
##survey['app_buy_if_elec_imm_other'].value_counts(dropna=False)
survey['app_buy_if_elec_imm_other'].describe()
```

```{.json .output n=40}
[
 {
  "data": {
   "text/plain": "count             25\nunique            17\ntop       Mesin cuci\nfreq               9\nName: app_buy_if_elec_imm_other, dtype: object"
  },
  "execution_count": 40,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_year
English: If you had electricity, which appliances would you buy in the first
year?

Indonesian: Jika anda punya listrik, peralatan yang mana yang mau anda beli pada
tahun pertama?

```{.python .input  n=41}
##survey['app_buy_if_elec_year'].value_counts(dropna=False)
survey['app_buy_if_elec_year'].describe()
```

```{.json .output n=41}
[
 {
  "data": {
   "text/plain": "count        913\nunique       109\ntop       fridge\nfreq         201\nName: app_buy_if_elec_year, dtype: object"
  },
  "execution_count": 41,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_year/lighting
English: Lighting.

Indonesian: Penerangan.

```{.python .input  n=43}
survey['app_buy_if_elec_year/lighting'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/lighting'].describe()
```

```{.json .output n=43}
[
 {
  "data": {
   "text/plain": " 0     672\nNaN    271\n 1     241\ndtype: int64"
  },
  "execution_count": 43,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_year/TV
English: TV.

Indonesian: TV.

```{.python .input  n=45}
survey['app_buy_if_elec_year/TV'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/TV'].describe()
```

```{.json .output n=45}
[
 {
  "data": {
   "text/plain": " 0     710\nNaN    271\n 1     203\ndtype: int64"
  },
  "execution_count": 45,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_year/radio
English: Radio.

Indonesian: Radio.

```{.python .input  n=47}
survey['app_buy_if_elec_year/radio'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/radio'].describe()
```

```{.json .output n=47}
[
 {
  "data": {
   "text/plain": " 0     827\nNaN    271\n 1      86\ndtype: int64"
  },
  "execution_count": 47,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_year/fridge
English: Fridge.

Indonesian: Kulkas.

```{.python .input  n=49}
survey['app_buy_if_elec_year/fridge'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/fridge'].describe()
```

```{.json .output n=49}
[
 {
  "data": {
   "text/plain": " 0     458\n 1     455\nNaN    271\ndtype: int64"
  },
  "execution_count": 49,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_year/fan
English: Fan.

Indonesian: Kipas angin.

```{.python .input  n=51}
survey['app_buy_if_elec_year/fan'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/fan'].describe()
```

```{.json .output n=51}
[
 {
  "data": {
   "text/plain": " 0     788\nNaN    271\n 1     125\ndtype: int64"
  },
  "execution_count": 51,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_year/rice_cooker
English: Rice cooker.

Indonesian: Penanak nasi.

```{.python .input  n=53}
survey['app_buy_if_elec_year/rice_cooker'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/rice_cooker'].describe()
```

```{.json .output n=53}
[
 {
  "data": {
   "text/plain": " 0     737\nNaN    271\n 1     176\ndtype: int64"
  },
  "execution_count": 53,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_year/other_cooking
English: Other cooking related.

Indonesian: Masakan lain yang sejenis.

```{.python .input  n=55}
survey['app_buy_if_elec_year/other_cooking'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/other_cooking'].describe()
```

```{.json .output n=55}
[
 {
  "data": {
   "text/plain": " 0     863\nNaN    271\n 1      50\ndtype: int64"
  },
  "execution_count": 55,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_year/welder
English: Welder.

Indonesian: Mesin las.

```{.python .input  n=57}
survey['app_buy_if_elec_year/welder'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/welder'].describe()
```

```{.json .output n=57}
[
 {
  "data": {
   "text/plain": " 0     907\nNaN    271\n 1       6\ndtype: int64"
  },
  "execution_count": 57,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_year/grinder
English: Grinder.

Indonesian: Mesin penggiling.

```{.python .input  n=59}
survey['app_buy_if_elec_year/grinder'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/grinder'].describe()
```

```{.json .output n=59}
[
 {
  "data": {
   "text/plain": " 0     913\nNaN    271\ndtype: int64"
  },
  "execution_count": 59,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_year/saw
English: Saw.

Indonesian: Mesin gergaji.

```{.python .input  n=61}
survey['app_buy_if_elec_year/saw'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/saw'].describe()
```

```{.json .output n=61}
[
 {
  "data": {
   "text/plain": " 0     902\nNaN    271\n 1      11\ndtype: int64"
  },
  "execution_count": 61,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_year/other_tools
English: Other tools related.

Indonesian: Alat - alat lain yang sejenis.

```{.python .input  n=81}
survey['app_buy_if_elec_year/other_tools'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/other_tools'].describe()
```

```{.json .output n=81}
[
 {
  "data": {
   "text/plain": " 0     884\nNaN    271\n 1      29\ndtype: int64"
  },
  "execution_count": 81,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_year/other
English: Any other.

Indonesian: Ada yang lain.

```{.python .input  n=65}
survey['app_buy_if_elec_year/other'].value_counts(dropna=False)
##survey['app_buy_if_elec_year/other'].describe()
```

```{.json .output n=65}
[
 {
  "data": {
   "text/plain": " 0     647\nNaN    271\n 1     266\ndtype: int64"
  },
  "execution_count": 65,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_buy_if_elec_year_other
English: Please describe what you meant by "other."

Indonesian: Jelaskanlah apa yang anda maksud dengan "lain - lain."

```{.python .input  n=69}
##survey['app_buy_if_elec_year_other'].value_counts(dropna=False)
survey['app_buy_if_elec_year_other'].describe()
```

```{.json .output n=69}
[
 {
  "data": {
   "text/plain": "count            264\nunique            92\ntop       Mesin cuci\nfreq             114\nName: app_buy_if_elec_year_other, dtype: object"
  },
  "execution_count": 69,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_type_important
English: Access to which types of appliances is most important to you?

Indonesian: Akses untuk jenis - jenis peralatan yang mana yang paling penting
buat anda?

```{.python .input  n=71}
survey['app_type_important'].value_counts(dropna=False)
##survey['app_type_important'].describe()
```

```{.json .output n=71}
[
 {
  "data": {
   "text/plain": "entertainment    636\nhousehold        267\nwork             176\nNaN               70\nother             35\ndtype: int64"
  },
  "execution_count": 71,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_type_important_other
English: Please describe what you meant by "other."

Indonesian: Jelaskanlah apa yang anda maksud dengan :lain - lain."

```{.python .input  n=77}
##survey['app_type_important_other'].value_counts(dropna=False)
survey['app_type_important_other'].describe()
```

```{.json .output n=77}
[
 {
  "data": {
   "text/plain": "count              35\nunique             30\ntop       Jual pinang\nfreq                2\nName: app_type_important_other, dtype: object"
  },
  "execution_count": 77,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_future
English:  What will future appliances allow you to do that you can't do now?

Indonesian: Perkakas apa yang akan anda sediakan kelak untuk melakukan apa yang
tidak dapat anda lakukan sekarang?

```{.python .input  n=82}
##survey['app_future'].value_counts(dropna=False)
survey['app_future'].describe()
```

```{.json .output n=82}
[
 {
  "data": {
   "text/plain": "count                 510\nunique                261\ntop       Mesin pompa air\nfreq                   53\nName: app_future, dtype: object"
  },
  "execution_count": 82,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input}

```
