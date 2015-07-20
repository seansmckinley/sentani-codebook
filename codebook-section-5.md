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

## section_05

This section surveys appliance ownership information.

## app_now
English: Please select which existing electric appliances you currently own?

Indonesian: Pilihlah peralatan listrik yang ada yang anda miliki sekarang?

```{.python .input  n=3}
## app_now
survey['app_now'].value_counts(dropna=False)
#survey['app_now'].describe()
```

```{.json .output n=3}
[
 {
  "data": {
   "text/plain": "lighting TV                                                          193\nNaN                                                                  149\nlighting TV other                                                    137\nlighting TV radio other                                               86\nlighting TV radio                                                     84\nlighting                                                              74\nlighting TV fridge rice_cooker                                        27\nlighting radio                                                        27\nlighting other                                                        21\nlighting TV fridge                                                    19\nlighting TV fridge fan                                                16\nTV                                                                    16\nlighting TV rice_cooker                                               13\nlighting TV rice_cooker other                                         12\nlighting TV fridge fan rice_cooker                                    12\nother                                                                 12\nlighting TV fridge other                                              11\nlighting TV fridge rice_cooker other                                  11\nTV radio                                                              11\nlighting TV other_tools                                               11\nTV other                                                              10\nlighting radio other                                                   9\nlighting TV radio fridge rice_cooker other                             8\nlighting TV radio rice_cooker other                                    8\nlighting TV fan other                                                  8\nlighting TV radio fan                                                  7\nlighting TV radio fridge other                                         7\nlighting TV radio fridge                                               7\nlighting TV radio fridge fan rice_cooker                               7\nlighting TV radio fan other                                            7\n                                                                    ... \nlighting fridge fan other                                              1\nlighting TV radio other_cooking other                                  1\nlighting TV radio fridge fan rice_cooker grinder saw                   1\nrice_cooker other_tools other                                          1\nlighting TV radio fan rice_cooker other_cooking other_tools other      1\nlighting TV radio rice_cooker other_tools other                        1\nlighting TV fridge fan rice_cooker other_tools other                   1\nTV fridge rice_cooker                                                  1\nlighting fridge rice_cooker                                            1\nlighting radio fan                                                     1\nlighting TV fridge rice_cooker other_tools                             1\nlighting TV fan other_tools                                            1\nlighting fridge                                                        1\nlighting TV radio fan rice_cooker other_tools                          1\nlighting TV radio fridge fan rice_cooker grinder other                 1\nlighting radio rice_cooker other                                       1\nlighting TV radio fridge rice_cooker other_tools                       1\nlighting TV fridge other_tools                                         1\nTV rice_cooker                                                         1\nTV fan                                                                 1\nlighting radio fan other                                               1\nTV radio fridge fan rice_cooker other_tools                            1\nTV other_tools                                                         1\nTV radio fridge                                                        1\nlighting TV fridge fan rice_cooker other_tools                         1\nTV radio rice_cooker other                                             1\nlighting fan                                                           1\nlighting other_tools other                                             1\nTV radio fan rice_cooker other                                         1\nTV fridge rice_cooker other_tools                                      1\ndtype: int64"
  },
  "execution_count": 3,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_now/lighting
English: Lighting.

Indonesian: Penerangan.

```{.python .input  n=4}
## app_now/lighting
survey['app_now/lighting'].value_counts(dropna=False)
#survey['app_now/lighting'].describe()
```

```{.json .output n=4}
[
 {
  "data": {
   "text/plain": " 1     951\nNaN    149\n 0      84\ndtype: int64"
  },
  "execution_count": 4,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_now/TV
English: TV.

Indonesian: TV.

```{.python .input  n=5}
## app_now/TV
survey['app_now/TV'].value_counts(dropna=False)
```

```{.json .output n=5}
[
 {
  "data": {
   "text/plain": " 1     844\n 0     191\nNaN    149\ndtype: int64"
  },
  "execution_count": 5,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_now/radio
English: Radio.

Indonesian: Radio.

```{.python .input  n=6}
## app_now/radio
survey['app_now/radio'].value_counts(dropna=False)
```

```{.json .output n=6}
[
 {
  "data": {
   "text/plain": " 0     683\n 1     352\nNaN    149\ndtype: int64"
  },
  "execution_count": 6,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_now/fridge
English: Refrigerator.

Indonesian: Kulkas.

```{.python .input  n=7}
## app_now/fridge
survey['app_now/fridge'].value_counts(dropna=False)
```

```{.json .output n=7}
[
 {
  "data": {
   "text/plain": " 0     837\n 1     198\nNaN    149\ndtype: int64"
  },
  "execution_count": 7,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

##app_now/fan
English: Fan.

Indonesian: Kipas.

```{.python .input  n=8}
## app_now/fan
survey['app_now/fan'].value_counts(dropna=False)
```

```{.json .output n=8}
[
 {
  "data": {
   "text/plain": " 0     905\nNaN    149\n 1     130\ndtype: int64"
  },
  "execution_count": 8,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

##app_now/rice_cooker
English: Rice cooker.

Indonesian: Penanak nasi.

```{.python .input  n=9}
## app_now/rice_cooker
survey['app_now/rice_cooker'].value_counts(dropna=False)
```

```{.json .output n=9}
[
 {
  "data": {
   "text/plain": " 0     861\n 1     174\nNaN    149\ndtype: int64"
  },
  "execution_count": 9,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

##app_now/other_cooking
English: Other cooking related.

Indonesian: "Masakan lain yang sejenis."

```{.python .input  n=10}
## app_now/other_cooking
survey['app_now/other_cooking'].value_counts(dropna=False)
```

```{.json .output n=10}
[
 {
  "data": {
   "text/plain": " 0     1021\nNaN     149\n 1       14\ndtype: int64"
  },
  "execution_count": 10,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_now/welder
English: Welder.

Indonesian: Mesin las.

```{.python .input  n=11}
## app_now/welder
survey['app_now/welder'].value_counts(dropna=False)
```

```{.json .output n=11}
[
 {
  "data": {
   "text/plain": " 0     1034\nNaN     149\n 1        1\ndtype: int64"
  },
  "execution_count": 11,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

##app_now/grinder
English: Grinder.

Indonesian: Mesin penggiling.

```{.python .input  n=12}
## app_now/grinder
survey['app_now/grinder'].value_counts(dropna=False)
```

```{.json .output n=12}
[
 {
  "data": {
   "text/plain": " 0     1033\nNaN     149\n 1        2\ndtype: int64"
  },
  "execution_count": 12,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_now/saw
English: Saw.

Indonesian: Mesin gergaji.

```{.python .input  n=13}
## app_now/saw
survey['app_now/saw'].value_counts(dropna=False)
```

```{.json .output n=13}
[
 {
  "data": {
   "text/plain": " 0     1025\nNaN     149\n 1       10\ndtype: int64"
  },
  "execution_count": 13,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

##app_now/other_tools
English: Other tools related.

Indonesian: Alat - alat lain yang sejenis.

```{.python .input  n=14}
## app_now/other_tools
survey['app_now/other_tools'].value_counts(dropna=False)
```

```{.json .output n=14}
[
 {
  "data": {
   "text/plain": " 0     972\nNaN    149\n 1      63\ndtype: int64"
  },
  "execution_count": 14,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

##app_now/other
English: Any other.

Indonesian: Ada yang lain.

```{.python .input  n=15}
## app_now/other
survey['app_now/other'].value_counts(dropna=False)
```

```{.json .output n=15}
[
 {
  "data": {
   "text/plain": " 0     605\n 1     430\nNaN    149\ndtype: int64"
  },
  "execution_count": 15,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_cooking_desc
English: Please describe what you meant by "other cooking related."

Indonesian: Jelaskanlah apa yang anda maksud dengan "masakan lain yang sejenis."

```{.python .input  n=16}
## app_other_cooking_desc
survey['app_other_cooking_desc'].value_counts(dropna=False)
#survey['app_other_cooking_desc'].describe()
```

```{.json .output n=16}
[
 {
  "data": {
   "text/plain": "NaN                                1170\nDispenser ( Pemanas Air )             2\nDispenser                             1\nMejik jer                             1\nDisfenser                             1\nBlender, disfenser                    1\nDap mesin air                         1\nMixer\\nBlender\\nPembakaran roti       1\nBlender\\nMixer\\n                      1\nMixer\\nBlender                        1\nPemanas Air                           1\nMixer                                 1\nPemanas air                           1\nReskuker                              1\ndtype: int64"
  },
  "execution_count": 16,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_tools_desc
English: Please describe what you meant by "other tools related."

Indonesian: Jelaskanlah apa yang anda maksud dengan "alat - alat lain yang
sejenis."

```{.python .input  n=17}
## app_other_tools_desc
survey['app_other_tools_desc'].value_counts(dropna=False)
#survey['app_other_tools_desc'].describe()
```

```{.json .output n=17}
[
 {
  "data": {
   "text/plain": "NaN                                                                                                                                        1121\nPompa air                                                                                                                                    11\nMesin cuci                                                                                                                                    7\nDisfenser                                                                                                                                     4\nPompa air\\nMesin cuci                                                                                                                         4\nMesin Air ( Dap )                                                                                                                             2\nMesin Cuci                                                                                                                                    2\nSpeaker dat                                                                                                                                   1\nSekaf listrik, Bor Listrik, \\n\\n Gurinda listrik ( Fungsinya untuk memotong batu dan bisa juga menjadi harta untuk membayar mas kawin )       1\nMesin Air                                                                                                                                     1\nKulkas                                                                                                                                        1\nDispenser.                                                                                                                                    1\nMesin air ( Dap )                                                                                                                             1\nKurinda                                                                                                                                       1\nToa konputer printer                                                                                                                          1\nMesin  cuci                                                                                                                                   1\nKiboar.band.gtar strom                                                                                                                        1\nSpeaker \\nPompa air                                                                                                                           1\nMesin penggiling                                                                                                                              1\nVcd, Laptop                                                                                                                                   1\nVcd, speaker                                                                                                                                  1\nPeralatan salon                                                                                                                               1\nMesin cuci ,dispenser                                                                                                                         1\nDispenser                                                                                                                                     1\nMesin dap Sanyo                                                                                                                               1\nMesin pompa air                                                                                                                               1\nSpeaker\\nVcd                                                                                                                                  1\nSanyo                                                                                                                                         1\nGurinda listrik                                                                                                                               1\nBor listrik\\nGurinda mesin                                                                                                                    1\nLaptop                                                                                                                                        1\nSpeaker\\nDat                                                                                                                                  1\nDispenser ( Pemanas Air )                                                                                                                     1\nMesin Air ( Dap Sanyo )                                                                                                                       1\nPompa air dan disfenser                                                                                                                       1\nMesin cetakan batu bata                                                                                                                       1\nVcd                                                                                                                                           1\nGurinda listrik sering di kenak oleh warga setempat denhan Pemotong batu.                                                                     1\nDigital receiver                                                                                                                              1\nDvd                                                                                                                                           1\ndtype: int64"
  },
  "execution_count": 17,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

##app_other_desc
English: Please describe what you meant by "any other."

Indonesian: Jelaskanlah apa yang anda maksud dengan "ada yang lain."

```{.python .input  n=18}
## app_other_desc
survey['app_other_desc'].value_counts(dropna=False)
#survey['app_other_desc'].describe()
```

```{.json .output n=18}
[
 {
  "data": {
   "text/plain": "NaN                                                        756\nVcd                                                         43\nMesin cuci                                                  35\nPompa air                                                   28\nDispenser                                                   25\nSpeaker                                                     11\nDvd                                                         11\nDisfenser                                                    9\nSpiker                                                       8\nLaptop                                                       7\nDigital Receiver                                             6\nDvd dan spiker.                                              6\nDvd dan digital.                                             4\nDigital                                                      4\nTep                                                          3\nSpiker, dvd dan digital.                                     3\nSpeaker dat                                                  3\nMesin air                                                    3\nMesin cuci,                                                  2\nDvd dan digital                                              2\nVcd, Receiver ( Digital )                                    2\nVcd\\nSpeaker                                                 2\nSanyo                                                        2\nTeap                                                         2\nStrika baju                                                  2\nVcd, mesin cuci                                              2\nDvd dan spiker                                               2\nMesin Cuci                                                   2\nDvd, resiver                                                 2\nGengset                                                      2\n                                                          ... \nVcd, Digital Receiver                                        1\nLaptop,digital,vcd, mesin cuci                               1\nDvd dan indovidion                                           1\nMesin cuci, strika, resifer, spiker dan ampli.               1\nSpeaker\\nLaptop                                              1\nSound system,digital receiver,Vcd                            1\nPerlengkapan karaoke                                         1\nAmplifier                                                    1\nTape                                                         1\nLaptop dan prin                                              1\nDvd, ampli, spiker, plestesien dan senter cas.               1\nDvd dan ampli                                                1\nDpiket dan dvd                                               1\nSetrika Pakaian Listrik                                      1\nVcd,mp4 music player, sound system atau pengeras suara.      1\nSpeaker Aktif                                                1\nToptv digital                                                1\nAmpli, DVD, matrikx dan spiker.                              1\nDigital dan dvd                                              1\nDispenser Pemanas Air                                        1\nKeyboard ( organ ) ampliflier                                1\nDvd pleyer, leptop, komputer                                 1\nDvd dan spker                                                1\nAmplufiier dan vcd                                           1\nTop tv\\nSpeaker\\nDvd                                         1\nMesin cuci dan digital.                                      1\nMixer                                                        1\nSetrika,Amplifier, Vcd, Indovision ( Digital )               1\nDispenser, mikser, blender dan spiker.                       1\nDvd. Mikser dan blender.                                     1\ndtype: int64"
  },
  "execution_count": 18,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_lighting_per_wk
English: For lighting, how many times a week do you use it?

Indonesian: Untuk penerangan, berapa kali seminggu anda menggunakannya?

```{.python .input  n=19}
## app_lighting_per_wk
survey['app_lighting_per_wk'].value_counts(dropna=False)
survey['app_lighting_per_wk'].describe()
```

```{.json .output n=19}
[
 {
  "data": {
   "text/plain": "count       927.000000\nmean        222.338727\nstd        6568.645346\nmin           0.000000\n25%           7.000000\n50%           7.000000\n75%           7.000000\nmax      200000.000000\nName: app_lighting_per_wk, dtype: float64"
  },
  "execution_count": 19,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_lighting_hrs
English: For lighting, each time you use it, how many hours do you use it for?

Indonesian: Untuk penerangan, selama berapa jam setiap kali anda menggunakannya?

```{.python .input  n=20}
## app_lighting_hrs
survey['app_lighting_hrs'].value_counts(dropna=False)
survey['app_lighting_hrs'].describe()
```

```{.json .output n=20}
[
 {
  "data": {
   "text/plain": "count      929.000000\nmean        22.559742\nstd        393.424423\nmin          0.000000\n25%          6.000000\n50%          7.000000\n75%         12.000000\nmax      12000.000000\nName: app_lighting_hrs, dtype: float64"
  },
  "execution_count": 20,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_lighting_use_times
English: For lighting, what time of the day do you typically use it?

Indonesian: Untuk penerangan, pada jam berapa biasanya anda menggunakannya?

```{.python .input  n=21}
## app_lighting_use_times
survey['app_lighting_use_times'].value_counts(dropna=False)
#survey['app_lighting_use_times'].describe()
```

```{.json .output n=21}
[
 {
  "data": {
   "text/plain": "night                              528\nNaN                                255\nafternoon night                    155\nmorning night                      139\nmorning mid_day afternoon night     81\nmid_day night                       17\nmid_day afternoon night              4\nmorning mid_day night                1\nafternoon                            1\nmorning mid_day                      1\nmorning afternoon night              1\nmorning                              1\ndtype: int64"
  },
  "execution_count": 21,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_lighting_use_times/morning

```{.python .input  n=22}
## app_lighting_use_times/morning
survey['app_lighting_use_times/morning'].value_counts(dropna=False)
#survey['app_lighting_use_times/morning'].describe()
```

```{.json .output n=22}
[
 {
  "data": {
   "text/plain": " 0     705\nNaN    255\n 1     224\ndtype: int64"
  },
  "execution_count": 22,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_lighting_use_times/mid_day

```{.python .input  n=23}
## app_lighting_use_times/mid_day
survey['app_lighting_use_times/mid_day'].value_counts(dropna=False)
#survey['app_lighting_use_times/mid_day'].describe()
```

```{.json .output n=23}
[
 {
  "data": {
   "text/plain": " 0     825\nNaN    255\n 1     104\ndtype: int64"
  },
  "execution_count": 23,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_lighting_use_times/afternoon

```{.python .input  n=24}
## app_lighting_use_times/afternoon
survey['app_lighting_use_times/afternoon'].value_counts(dropna=False)
#survey['app_lighting_use_times/afternoon'].describe()
```

```{.json .output n=24}
[
 {
  "data": {
   "text/plain": " 0     687\nNaN    255\n 1     242\ndtype: int64"
  },
  "execution_count": 24,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_lighting_use_times/night

```{.python .input  n=25}
## app_lighting_use_times/night
survey['app_lighting_use_times/night'].value_counts(dropna=False)
```

```{.json .output n=25}
[
 {
  "data": {
   "text/plain": " 1     926\nNaN    255\n 0       3\ndtype: int64"
  },
  "execution_count": 25,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_TV_per_wk
English: For TV, how many times a week do you use it?

Indonesian: Untuk TV, berapa kali seminggu anda menggunakannya?

```{.python .input  n=26}
## app_TV_per_wk
#survey['app_TV_per_wk'].value_counts(dropna=False)
survey['app_TV_per_wk'].describe()
```

```{.json .output n=26}
[
 {
  "data": {
   "text/plain": "count    810.000000\nmean       6.488889\nstd        1.529439\nmin        0.000000\n25%        7.000000\n50%        7.000000\n75%        7.000000\nmax       24.000000\nName: app_TV_per_wk, dtype: float64"
  },
  "execution_count": 26,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_TV_hrs
English: For TV, each time you use it, how many hours do you use it for?

Indonesian: Untuk TV, selama berapa jam setiap kali anda menggunakannya?

```{.python .input  n=27}
## app_TV_hrs
survey['app_TV_hrs'].value_counts(dropna=False)
survey['app_TV_hrs'].describe()
```

```{.json .output n=27}
[
 {
  "data": {
   "text/plain": "count    811.000000\nmean       6.903822\nstd        4.524078\nmin        0.000000\n25%        4.000000\n50%        6.000000\n75%        8.000000\nmax       24.000000\nName: app_TV_hrs, dtype: float64"
  },
  "execution_count": 27,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_TV_use_times
English: For TV, what time of the day do you typically use it?

Indonesian: Untuk TV, pada jam berapa biasanya anda menggunakannya?

```{.python .input  n=28}
## app_TV_use_times
survey['app_TV_use_times'].value_counts(dropna=False)
#survey['app_TV_use_times'].describe()
```

```{.json .output n=28}
[
 {
  "data": {
   "text/plain": "NaN                                376\nnight                              303\nmorning mid_day afternoon night    264\nafternoon night                     62\nmorning mid_day night               58\nmid_day night                       45\nmorning night                       34\nmid_day afternoon night             20\nmorning afternoon night             17\nmorning mid_day afternoon            2\nmid_day afternoon                    1\nmorning mid_day                      1\nmorning                              1\ndtype: int64"
  },
  "execution_count": 28,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_TV_use_times/morning

```{.python .input  n=29}
## app_TV_use_times/morning
survey['app_TV_use_times/morning'].value_counts(dropna=False)
#survey['app_TV_use_times/morning'].describe()
```

```{.json .output n=29}
[
 {
  "data": {
   "text/plain": " 0     431\n 1     377\nNaN    376\ndtype: int64"
  },
  "execution_count": 29,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_TV_use_times/mid_day

```{.python .input  n=30}
## app_TV_use_times/mid_day
survey['app_TV_use_times/mid_day'].value_counts(dropna=False)
#survey['app_TV_use_times/mid_day'].describe()
```

```{.json .output n=30}
[
 {
  "data": {
   "text/plain": " 0     417\n 1     391\nNaN    376\ndtype: int64"
  },
  "execution_count": 30,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_TV_use_times/afternoon

```{.python .input  n=31}
## app_TV_use_times/afternoon
survey['app_TV_use_times/afternoon'].value_counts(dropna=False)
#survey['app_TV_use_times/afternoon'].describe()
```

```{.json .output n=31}
[
 {
  "data": {
   "text/plain": " 0     442\nNaN    376\n 1     366\ndtype: int64"
  },
  "execution_count": 31,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_TV_use_times/night

```{.python .input  n=32}
## app_TV_use_times/night
survey['app_TV_use_times/night'].value_counts(dropna=False)
#survey['app_TV_use_times/night'].describe()
```

```{.json .output n=32}
[
 {
  "data": {
   "text/plain": " 1     803\nNaN    376\n 0       5\ndtype: int64"
  },
  "execution_count": 32,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_radio_per_wk
English: For radio, how many times a week do you use it?

Indonesian: Untuk radio, berapa kali seminggu anda menggunakannya?

```{.python .input  n=33}
## app_radio_per_wk
survey['app_radio_per_wk'].value_counts(dropna=False)
survey['app_radio_per_wk'].describe()
```

```{.json .output n=33}
[
 {
  "data": {
   "text/plain": "count    342.000000\nmean       5.517544\nstd        2.262401\nmin        0.000000\n25%        4.000000\n50%        7.000000\n75%        7.000000\nmax       24.000000\nName: app_radio_per_wk, dtype: float64"
  },
  "execution_count": 33,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_radio_hrs
English: For radio, each time you use it, how many hours do you use it for?

Indonesian: Untuk radio, selama berapa jam setiap kali anda menggunakannya?

```{.python .input  n=34}
## app_radio_hrs
survey['app_radio_hrs'].describe()
```

```{.json .output n=34}
[
 {
  "data": {
   "text/plain": "count    341.000000\nmean       4.108504\nstd        4.031124\nmin        0.000000\n25%        2.000000\n50%        3.000000\n75%        5.000000\nmax       24.000000\nName: app_radio_hrs, dtype: float64"
  },
  "execution_count": 34,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_radio_use_times
English: For radio, what time of the day do you typically use it?

Indonesian: Untuk radio, pada jam berapa biasanya anda menggunakannya?

```{.python .input  n=35}
## app_radio_use_times
survey['app_radio_use_times'].value_counts(dropna=False)
```

```{.json .output n=35}
[
 {
  "data": {
   "text/plain": "NaN                                844\nnight                               80\nmorning mid_day afternoon night     71\nmorning                             59\nmorning night                       29\nmorning mid_day                     24\nmorning mid_day afternoon           18\nmorning afternoon                   13\nmorning mid_day night               11\nmorning afternoon night             11\nmid_day night                        9\nafternoon night                      9\nmid_day afternoon                    2\nmid_day afternoon night              2\nmid_day                              2\ndtype: int64"
  },
  "execution_count": 35,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_radio_use_times/morning

```{.python .input  n=36}
## app_radio_use_times/morning
survey['app_radio_use_times/morning'].value_counts(dropna=False)
```

```{.json .output n=36}
[
 {
  "data": {
   "text/plain": "NaN    844\n 1     236\n 0     104\ndtype: int64"
  },
  "execution_count": 36,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_radio_use_times/mid_day

```{.python .input  n=37}
## app_radio_use_times/mid_day
survey['app_radio_use_times/mid_day'].value_counts(dropna=False)
```

```{.json .output n=37}
[
 {
  "data": {
   "text/plain": "NaN    844\n 0     201\n 1     139\ndtype: int64"
  },
  "execution_count": 37,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_radio_use_times/afternoon

```{.python .input  n=38}
## app_radio_use_times/afternoon
survey['app_radio_use_times/afternoon'].value_counts(dropna=False)
```

```{.json .output n=38}
[
 {
  "data": {
   "text/plain": "NaN    844\n 0     214\n 1     126\ndtype: int64"
  },
  "execution_count": 38,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_radio_use_times/night

```{.python .input  n=39}
## app_radio_use_times/night
survey['app_radio_use_times/night'].value_counts(dropna=False)
```

```{.json .output n=39}
[
 {
  "data": {
   "text/plain": "NaN    844\n 1     222\n 0     118\ndtype: int64"
  },
  "execution_count": 39,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_fridge_per_wk
TODO: deal with obvious outlier

English: For fridge, how many times a week do you use it?

Indonesian: Untuk kulkas, berapa kali seminggu anda menggunakannya?

```{.python .input  n=40}
## app_fridge_per_wk
survey['app_fridge_per_wk'].value_counts(dropna=False)
#survey['app_fridge_per_wk'].describe()
```

```{.json .output n=40}
[
 {
  "data": {
   "text/plain": "NaN       991\n 7        176\n 6          8\n 24         5\n 20000      1\n 3          1\n 1          1\n 0          1\ndtype: int64"
  },
  "execution_count": 40,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_fridge_hrs
English: For fridge, each time you use it, how many hours do you use it for?

Indonesian: Untuk kulkas, selama berapa jam setiap kali anda menggunakannya?

```{.python .input  n=41}
## app_fridge_hrs
survey['app_fridge_hrs'].value_counts(dropna=False)
```

```{.json .output n=41}
[
 {
  "data": {
   "text/plain": "NaN    991\n 24    180\n 7       7\n 6       4\n 12      1\n 0       1\ndtype: int64"
  },
  "execution_count": 41,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_fridge_use_times
English: For fridge, what time of the day do you typically use it?

Indonesian: Untuk kulkas, pada jam berapa biasanya anda menggunakannya?

```{.python .input  n=42}
## app_fridge_use_times
survey['app_fridge_use_times'].value_counts(dropna=False)
```

```{.json .output n=42}
[
 {
  "data": {
   "text/plain": "NaN                                990\nmorning mid_day afternoon night    183\nnight                                7\nafternoon night                      3\nmid_day afternoon                    1\ndtype: int64"
  },
  "execution_count": 42,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_fridge_use_times/morning

```{.python .input  n=43}
## app_fridge_use_times/morning
survey['app_fridge_use_times/morning'].value_counts(dropna=False)
```

```{.json .output n=43}
[
 {
  "data": {
   "text/plain": "NaN    990\n 1     183\n 0      11\ndtype: int64"
  },
  "execution_count": 43,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_fridge_use_times/mid_day

```{.python .input  n=44}
## app_fridge_use_times/mid_day
survey['app_fridge_use_times/mid_day'].value_counts(dropna=False)
```

```{.json .output n=44}
[
 {
  "data": {
   "text/plain": "NaN    990\n 1     184\n 0      10\ndtype: int64"
  },
  "execution_count": 44,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_fridge_use_times/afternoon

```{.python .input  n=45}
## app_fridge_use_times/afternoon
survey['app_fridge_use_times/afternoon'].value_counts(dropna=False)
```

```{.json .output n=45}
[
 {
  "data": {
   "text/plain": "NaN    990\n 1     187\n 0       7\ndtype: int64"
  },
  "execution_count": 45,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_fridge_use_times/night

```{.python .input  n=46}
## app_fridge_use_times/night
survey['app_fridge_use_times/night'].value_counts(dropna=False)
```

```{.json .output n=46}
[
 {
  "data": {
   "text/plain": "NaN    990\n 1     193\n 0       1\ndtype: int64"
  },
  "execution_count": 46,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_fan_per_wk
English: For fan, how many times a week do you use it?

Indonesian: Untuk kipas angin, berapa kali seminggu anda menggunakannya?

```{.python .input  n=47}
## app_fan_per_wk
survey['app_fan_per_wk'].value_counts(dropna=False)
```

```{.json .output n=47}
[
 {
  "data": {
   "text/plain": "NaN    1057\n 7       83\n 3       15\n 4       13\n 5        5\n 6        4\n 2        4\n 1        2\n 0        1\ndtype: int64"
  },
  "execution_count": 47,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_fan_hrs
English: For fan, each time you use it, how many hours do you use it for?

Indonesian: Untuk kipas angin, selama berapa jam setiap kali anda
menggunakannya?

```{.python .input  n=48}
## app_fan_hrs
survey['app_fan_hrs'].describe()
```

```{.json .output n=48}
[
 {
  "data": {
   "text/plain": "count    128.000000\nmean       6.507812\nstd        6.062660\nmin        0.000000\n25%        2.000000\n50%        3.500000\n75%        7.250000\nmax       24.000000\nName: app_fan_hrs, dtype: float64"
  },
  "execution_count": 48,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_fan_use_times
English: For fan, what time of the day do you typically use it?

Indonesian: Untuk kipas angin, pada jam berapa biasanya anda menggunakannya?

```{.python .input  n=49}
## app_fan_use_times
survey['app_fan_use_times'].value_counts(dropna=False)
```

```{.json .output n=49}
[
 {
  "data": {
   "text/plain": "NaN                                1057\nmid_day night                        34\nmid_day                              28\nnight                                26\nmorning mid_day afternoon night      12\nmid_day afternoon night              10\nmid_day afternoon                     9\nafternoon night                       3\nmorning mid_day night                 2\nmorning mid_day                       1\nmorning mid_day afternoon             1\nmorning night                         1\ndtype: int64"
  },
  "execution_count": 49,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_fan_use_times/morning

```{.python .input  n=50}
## app_fan_use_times/morning
survey['app_fan_use_times/morning'].value_counts(dropna=False)
```

```{.json .output n=50}
[
 {
  "data": {
   "text/plain": "NaN    1057\n 0      110\n 1       17\ndtype: int64"
  },
  "execution_count": 50,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_fan_use_times/mid_day

```{.python .input  n=51}
## app_fan_use_times/mid_day
survey['app_fan_use_times/mid_day'].value_counts(dropna=False)
```

```{.json .output n=51}
[
 {
  "data": {
   "text/plain": "NaN    1057\n 1       97\n 0       30\ndtype: int64"
  },
  "execution_count": 51,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_fan_use_times/afternoon

```{.python .input  n=52}
## app_fan_use_times/afternoon
survey['app_fan_use_times/afternoon'].value_counts(dropna=False)
```

```{.json .output n=52}
[
 {
  "data": {
   "text/plain": "NaN    1057\n 0       92\n 1       35\ndtype: int64"
  },
  "execution_count": 52,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_fan_use_times/night

```{.python .input  n=53}
## app_fan_use_times/night
survey['app_fan_use_times/night'].value_counts(dropna=False)
```

```{.json .output n=53}
[
 {
  "data": {
   "text/plain": "NaN    1057\n 1       88\n 0       39\ndtype: int64"
  },
  "execution_count": 53,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_rice_cooker_per_wk
English: For rice cooker, how many times a week do you use it?

Indonesian: Untuk penanak nasi, berapa kali seminggu anda menggunakannya?

```{.python .input  n=54}
## app_rice_cooker_per_wk
survey['app_rice_cooker_per_wk'].value_counts(dropna=False)
survey['app_rice_cooker_per_wk'].describe()
```

```{.json .output n=54}
[
 {
  "data": {
   "text/plain": "count    169.000000\nmean       6.869822\nstd        2.156298\nmin        1.000000\n25%        7.000000\n50%        7.000000\n75%        7.000000\nmax       24.000000\nName: app_rice_cooker_per_wk, dtype: float64"
  },
  "execution_count": 54,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_rice_cooker_hrs
English: For rice cooker, each time you use it, how many hours do you use it
for?

Indonesian: Untuk penanak nasi, selama berapa jam setiap kali anda
menggunakannya?

```{.python .input  n=55}
## app_rice_cooker_hrs
survey['app_rice_cooker_hrs'].value_counts(dropna=False)
survey['app_rice_cooker_hrs'].describe()
```

```{.json .output n=55}
[
 {
  "data": {
   "text/plain": "count    170.000000\nmean      13.147059\nstd        9.865763\nmin        1.000000\n25%        3.250000\n50%        7.000000\n75%       24.000000\nmax       24.000000\nName: app_rice_cooker_hrs, dtype: float64"
  },
  "execution_count": 55,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_rice_cooker_use_times
English: For rice cooker, what time of the day do you typically use it?

Indonesian: Untuk penanak nasi, pada jam berapa biasanya anda menggunakannya?

```{.python .input  n=56}
## app_rice_cooker_use_times
survey['app_rice_cooker_use_times'].value_counts(dropna=False)
```

```{.json .output n=56}
[
 {
  "data": {
   "text/plain": "NaN                                1014\nmorning mid_day afternoon night     108\nmorning mid_day night                19\nnight                                11\nmorning afternoon                     8\nmorning mid_day                       6\nmid_day                               4\nmorning                               4\nmid_day night                         3\nmorning mid_day afternoon             3\nmorning night                         3\nafternoon night                       1\ndtype: int64"
  },
  "execution_count": 56,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_rice_cooker_use_times/morning

```{.python .input  n=57}
## app_rice_cooker_use_times/morning
survey['app_rice_cooker_use_times/morning'].value_counts(dropna=False)
```

```{.json .output n=57}
[
 {
  "data": {
   "text/plain": "NaN    1014\n 1      151\n 0       19\ndtype: int64"
  },
  "execution_count": 57,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_rice_cooker_use_times/mid_day

```{.python .input  n=58}
## app_rice_cooker_use_times/mid_day
survey['app_rice_cooker_use_times/mid_day'].value_counts(dropna=False)
```

```{.json .output n=58}
[
 {
  "data": {
   "text/plain": "NaN    1014\n 1      143\n 0       27\ndtype: int64"
  },
  "execution_count": 58,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_rice_cooker_use_times/afternoon

```{.python .input  n=59}
## app_rice_cooker_use_times/afternoon
survey['app_rice_cooker_use_times/afternoon'].value_counts(dropna=False)
```

```{.json .output n=59}
[
 {
  "data": {
   "text/plain": "NaN    1014\n 1      120\n 0       50\ndtype: int64"
  },
  "execution_count": 59,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_rice_cooker_use_times/night

```{.python .input  n=60}
## app_rice_cooker_use_times/night
survey['app_rice_cooker_use_times/night'].value_counts(dropna=False)
```

```{.json .output n=60}
[
 {
  "data": {
   "text/plain": "NaN    1014\n 1      145\n 0       25\ndtype: int64"
  },
  "execution_count": 60,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_cooking_per_wk
English: For ${app_other_cooking_desc} ("other cooking"), how many times a week
do you use it?

Indonesian: Untuk ${app_other_cooking_desc} (masakan yang lain), berapakali
seminggu anda menggunakannya?

```{.python .input  n=61}
## app_other_cooking_per_wk
survey['app_other_cooking_per_wk'].value_counts(dropna=False)
survey['app_other_cooking_per_wk'].describe()
```

```{.json .output n=61}
[
 {
  "data": {
   "text/plain": "count    13.000000\nmean      4.692308\nstd       3.038218\nmin       1.000000\n25%       1.000000\n50%       7.000000\n75%       7.000000\nmax       7.000000\nName: app_other_cooking_per_wk, dtype: float64"
  },
  "execution_count": 61,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_cooking_hrs
English:  For ${app_other_cooking_desc} ("other cooking"), each time you use it,
how many hours do you use it for?

Indonesian: Untuk ${app_other_cooking_desc} (masakan yang lain), selama berapa
jam setiap kali anda menggunakannya?

```{.python .input  n=62}
## app_other_cooking_hrs
survey['app_other_cooking_hrs'].value_counts(dropna=False)
survey['app_other_cooking_hrs'].describe()
```

```{.json .output n=62}
[
 {
  "data": {
   "text/plain": "count    13.000000\nmean      9.461538\nstd      10.453192\nmin      -1.000000\n25%       1.000000\n50%       7.000000\n75%      24.000000\nmax      24.000000\nName: app_other_cooking_hrs, dtype: float64"
  },
  "execution_count": 62,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_cooking_use_times
English: For ${app_other_cooking_desc} ("other cooking"), what time of the day
do you typically use it?

Indonesian: Untuk ${app_other_cooking_desc} (masakan yang lain), pada jam berapa
biasanya anda menggunakannya?

```{.python .input  n=63}
## app_other_cooking_use_times
survey['app_other_cooking_use_times'].value_counts(dropna=False)
```

```{.json .output n=63}
[
 {
  "data": {
   "text/plain": "NaN                                1171\nmorning mid_day afternoon night       8\nnight                                 1\nmorning mid_day afternoon             1\nafternoon night                       1\nmid_day                               1\nmorning                               1\ndtype: int64"
  },
  "execution_count": 63,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_cooking_use_times/morning

```{.python .input  n=64}
## app_other_cooking_use_times/morning
survey['app_other_cooking_use_times/morning'].value_counts(dropna=False)
```

```{.json .output n=64}
[
 {
  "data": {
   "text/plain": "NaN    1171\n 1       10\n 0        3\ndtype: int64"
  },
  "execution_count": 64,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_cooking_use_times/mid_day

```{.python .input  n=65}
## app_other_cooking_use_times/mid_day
survey['app_other_cooking_use_times/mid_day'].value_counts(dropna=False)
```

```{.json .output n=65}
[
 {
  "data": {
   "text/plain": "NaN    1171\n 1       10\n 0        3\ndtype: int64"
  },
  "execution_count": 65,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_cooking_use_times/afternoon

```{.python .input  n=66}
## app_other_cooking_use_times/afternoon
survey['app_other_cooking_use_times/afternoon'].value_counts(dropna=False)
```

```{.json .output n=66}
[
 {
  "data": {
   "text/plain": "NaN    1171\n 1       10\n 0        3\ndtype: int64"
  },
  "execution_count": 66,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_cooking_use_times/night

```{.python .input  n=67}
## app_other_cooking_use_times/night
survey['app_other_cooking_use_times/night'].value_counts(dropna=False)
```

```{.json .output n=67}
[
 {
  "data": {
   "text/plain": "NaN    1171\n 1       10\n 0        3\ndtype: int64"
  },
  "execution_count": 67,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_welder_per_wk
English: For welder, how many times a week do you use it?

Indonesian: Untuk mesin las, berapa kali seminggu anda menggunakannya?

```{.python .input  n=68}
## app_welder_per_wk
survey['app_welder_per_wk'].value_counts(dropna=False)
survey['app_welder_per_wk'].describe()
```

```{.json .output n=68}
[
 {
  "data": {
   "text/plain": "count     1\nmean      1\nstd     NaN\nmin       1\n25%       1\n50%       1\n75%       1\nmax       1\nName: app_welder_per_wk, dtype: float64"
  },
  "execution_count": 68,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_welder_hrs
English:  For welder, each time you use it, how many hours do you use it for?

Indonesian: Untuk mesin las, selama berapa jam setiap kali anda menggunakannya?

```{.python .input  n=69}
## app_welder_hrs
survey['app_welder_hrs'].value_counts(dropna=False)
survey['app_welder_hrs'].describe()
```

```{.json .output n=69}
[
 {
  "data": {
   "text/plain": "count     1\nmean      5\nstd     NaN\nmin       5\n25%       5\n50%       5\n75%       5\nmax       5\nName: app_welder_hrs, dtype: float64"
  },
  "execution_count": 69,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_welder_use_times
English: For welder, what time of the day do you typically use it?

Indonesian: Untuk mesin las, pada jam berapa biasanya anda menggunakannya?

```{.python .input  n=70}
## app_welder_use_times
survey['app_welder_use_times'].value_counts(dropna=False)
#survey['app_welder_use_times'].describe()
```

```{.json .output n=70}
[
 {
  "data": {
   "text/plain": "NaN                  1183\nmid_day afternoon       1\ndtype: int64"
  },
  "execution_count": 70,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_welder_use_times/morning

```{.python .input  n=71}
## app_welder_use_times/morning
survey['app_welder_use_times/morning'].value_counts(dropna=False)
```

```{.json .output n=71}
[
 {
  "data": {
   "text/plain": "NaN    1183\n 0        1\ndtype: int64"
  },
  "execution_count": 71,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_welder_use_times/mid_day

```{.python .input  n=72}
## app_welder_use_times/mid_day
survey['app_welder_use_times/mid_day'].value_counts(dropna=False)
```

```{.json .output n=72}
[
 {
  "data": {
   "text/plain": "NaN    1183\n 1        1\ndtype: int64"
  },
  "execution_count": 72,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_welder_use_times/afternoon

```{.python .input  n=73}
## app_welder_use_times/afternoon
survey['app_welder_use_times/afternoon'].value_counts(dropna=False)
```

```{.json .output n=73}
[
 {
  "data": {
   "text/plain": "NaN    1183\n 1        1\ndtype: int64"
  },
  "execution_count": 73,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_welder_use_times/night

```{.python .input  n=74}
## app_welder_use_times/night
survey['app_welder_use_times/night'].value_counts(dropna=False)
```

```{.json .output n=74}
[
 {
  "data": {
   "text/plain": "NaN    1183\n 0        1\ndtype: int64"
  },
  "execution_count": 74,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_grinder_per_wk
English: For grinder, how many times a week do you use it?

Indonesian: Untuk mesin penggiling, berapa kali seminggu anda menggunakannya?

```{.python .input  n=75}
## app_grinder_per_wk
survey['app_grinder_per_wk'].value_counts(dropna=False)
survey['app_grinder_per_wk'].describe()
```

```{.json .output n=75}
[
 {
  "data": {
   "text/plain": "count    2.000000\nmean     2.000000\nstd      1.414214\nmin      1.000000\n25%      1.500000\n50%      2.000000\n75%      2.500000\nmax      3.000000\nName: app_grinder_per_wk, dtype: float64"
  },
  "execution_count": 75,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_grinder_hrs
English: For grinder, each time you use it, how many hours do you use it for?

Indonesian: Untuk mesin penggiling, selama berapa jam setiap kali anda
menggunakannya?

```{.python .input  n=76}
## app_grinder_hrs
survey['app_grinder_hrs'].value_counts(dropna=False)
```

```{.json .output n=76}
[
 {
  "data": {
   "text/plain": "NaN    1182\n 2        1\n 1        1\ndtype: int64"
  },
  "execution_count": 76,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_grinder_use_times
English: For grinder, what time of the day do you typically use it?

Indonesian: Untuk mesin penggiling, pada jam berapa biasanya anda
menggunakannya?

```{.python .input  n=77}
## app_grinder_use_times
survey['app_grinder_use_times'].value_counts(dropna=False)
```

```{.json .output n=77}
[
 {
  "data": {
   "text/plain": "NaN                1182\nmorning mid_day       1\nmid_day night         1\ndtype: int64"
  },
  "execution_count": 77,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_grinder_use_times/morning

```{.python .input  n=78}
## app_grinder_use_times/morning
survey['app_grinder_use_times/morning'].value_counts(dropna=False)
```

```{.json .output n=78}
[
 {
  "data": {
   "text/plain": "NaN    1182\n 1        1\n 0        1\ndtype: int64"
  },
  "execution_count": 78,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_grinder_use_times/mid_day

```{.python .input  n=79}
## app_grinder_use_times/mid_day
survey['app_grinder_use_times/mid_day'].value_counts(dropna=False)
```

```{.json .output n=79}
[
 {
  "data": {
   "text/plain": "NaN    1182\n 1        2\ndtype: int64"
  },
  "execution_count": 79,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_grinder_use_times/afternoon

```{.python .input  n=80}
## app_grinder_use_times/afternoon
survey['app_grinder_use_times/afternoon'].value_counts(dropna=False)
```

```{.json .output n=80}
[
 {
  "data": {
   "text/plain": "NaN    1182\n 0        2\ndtype: int64"
  },
  "execution_count": 80,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_grinder_use_times/night

```{.python .input  n=81}
## app_grinder_use_times/night
survey['app_grinder_use_times/night'].value_counts(dropna=False)
```

```{.json .output n=81}
[
 {
  "data": {
   "text/plain": "NaN    1182\n 1        1\n 0        1\ndtype: int64"
  },
  "execution_count": 81,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_saw_per_wk
English:  For saw, how many times a week do you use it?

Indonesian: Untuk mesin gergaji, berapa kali seminggu anda menggunakannya?

```{.python .input  n=82}
## app_saw_per_wk
survey['app_saw_per_wk'].value_counts(dropna=False)
survey['app_saw_per_wk'].describe()
```

```{.json .output n=82}
[
 {
  "data": {
   "text/plain": "count    7.000000\nmean     1.285714\nstd      0.755929\nmin      0.000000\n25%      1.000000\n50%      1.000000\n75%      2.000000\nmax      2.000000\nName: app_saw_per_wk, dtype: float64"
  },
  "execution_count": 82,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_saw_hrs
English: For saw, each time you use it, how many hours do you use it for?

Indonesian: Untuk mesin gergaji, selama berapa jam setiap kali anda
menggunakannya?

```{.python .input  n=83}
## app_saw_hrs
survey['app_saw_hrs'].value_counts(dropna=False)
survey['app_saw_hrs'].describe()
```

```{.json .output n=83}
[
 {
  "data": {
   "text/plain": "count     6.000000\nmean      5.166667\nstd       4.490731\nmin       1.000000\n25%       1.500000\n50%       4.000000\n75%       8.000000\nmax      12.000000\nName: app_saw_hrs, dtype: float64"
  },
  "execution_count": 83,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_saw_use_times
English: For saw, what time of the day do you typically use it?

Indonesian: Untuk mesin gergaji, pada jam berapa biasanya anda menggunakannya?

```{.python .input  n=84}
## app_saw_use_times
survey['app_saw_use_times'].value_counts(dropna=False)
```

```{.json .output n=84}
[
 {
  "data": {
   "text/plain": "NaN                                1177\nmid_day afternoon                     2\nmorning mid_day afternoon             2\nmorning mid_day                       1\nmorning mid_day afternoon night       1\nmid_day                               1\ndtype: int64"
  },
  "execution_count": 84,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_saw_use_times/morning

```{.python .input  n=85}
## app_saw_use_times/morning
survey['app_saw_use_times/morning'].value_counts(dropna=False)
```

```{.json .output n=85}
[
 {
  "data": {
   "text/plain": "NaN    1177\n 1        4\n 0        3\ndtype: int64"
  },
  "execution_count": 85,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_saw_use_times/mid_day

```{.python .input  n=86}
## app_saw_use_times/mid_day
survey['app_saw_use_times/mid_day'].value_counts(dropna=False)
```

```{.json .output n=86}
[
 {
  "data": {
   "text/plain": "NaN    1177\n 1        7\ndtype: int64"
  },
  "execution_count": 86,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_saw_use_times/afternoon

```{.python .input  n=87}
## app_saw_use_times/afternoon
survey['app_saw_use_times/afternoon'].value_counts(dropna=False)
```

```{.json .output n=87}
[
 {
  "data": {
   "text/plain": "NaN    1177\n 1        5\n 0        2\ndtype: int64"
  },
  "execution_count": 87,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_saw_use_times/night

```{.python .input  n=88}
## app_saw_use_times/night
survey['app_saw_use_times/night'].value_counts(dropna=False)
```

```{.json .output n=88}
[
 {
  "data": {
   "text/plain": "NaN    1177\n 0        6\n 1        1\ndtype: int64"
  },
  "execution_count": 88,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_tools_per_wk
English: For ${app_other_tools_desc} ("other tools") how many times a week do
you use it?

Indonesian: Untuk ${app_other_tools_desc} (alat-alat lain") berapa kali seminggu
anda menggunakannya?

```{.python .input  n=89}
## app_other_tools_per_wk
survey['app_other_tools_per_wk'].value_counts(dropna=False)
survey['app_other_tools_per_wk'].describe()
```

```{.json .output n=89}
[
 {
  "data": {
   "text/plain": "count    59.000000\nmean      4.898305\nstd       3.580093\nmin       1.000000\n25%       2.000000\n50%       6.000000\n75%       7.000000\nmax      24.000000\nName: app_other_tools_per_wk, dtype: float64"
  },
  "execution_count": 89,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_tools_hrs
English: For ${app_other_tools_desc} ("other tools"), each time you use it, how
many hours do you use it for?

Indonesian: Untuk ${app_other_tools_desc} (alat-alat lain"), selama berapa jam
setiap kali anda menggunakannya?

```{.python .input  n=90}
## app_other_tools_hrs
survey['app_other_tools_hrs'].value_counts(dropna=False)
survey['app_other_tools_hrs'].describe()
```

```{.json .output n=90}
[
 {
  "data": {
   "text/plain": "count    59.000000\nmean      4.728814\nstd       5.956250\nmin       1.000000\n25%       2.000000\n50%       3.000000\n75%       4.500000\nmax      24.000000\nName: app_other_tools_hrs, dtype: float64"
  },
  "execution_count": 90,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_tools_use_times
English: For ${app_other_tools_desc} ("other tools"), what time of the day do
you typically use it?

Indonesian: Untuk ${app_other_tools_desc} (alat-alat lain"), jam berapa biasanya
anda menggunakannya?

```{.python .input  n=91}
## app_other_tools_use_times
survey['app_other_tools_use_times'].value_counts(dropna=False)
```

```{.json .output n=91}
[
 {
  "data": {
   "text/plain": "NaN                                1124\nmorning mid_day afternoon night      13\nmorning mid_day afternoon            12\nmorning                               9\nnight                                 7\nmid_day                               6\nmorning afternoon                     3\nmorning mid_day                       3\nafternoon night                       3\nafternoon                             2\nmid_day afternoon                     1\nmorning mid_day night                 1\ndtype: int64"
  },
  "execution_count": 91,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_tools_use_times/morning

```{.python .input  n=92}
## app_other_tools_use_times/morning
survey['app_other_tools_use_times/morning'].value_counts(dropna=False)
```

```{.json .output n=92}
[
 {
  "data": {
   "text/plain": "NaN    1124\n 1       41\n 0       19\ndtype: int64"
  },
  "execution_count": 92,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_tools_use_times/mid_day

```{.python .input  n=93}
## app_other_tools_use_times/mid_day
survey['app_other_tools_use_times/mid_day'].value_counts(dropna=False)
```

```{.json .output n=93}
[
 {
  "data": {
   "text/plain": "NaN    1124\n 1       36\n 0       24\ndtype: int64"
  },
  "execution_count": 93,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_tools_use_times/afternoon

```{.python .input  n=94}
## app_other_tools_use_times/afternoon
survey['app_other_tools_use_times/afternoon'].value_counts(dropna=False)
```

```{.json .output n=94}
[
 {
  "data": {
   "text/plain": "NaN    1124\n 1       34\n 0       26\ndtype: int64"
  },
  "execution_count": 94,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_tools_use_times/night

```{.python .input  n=95}
## app_other_tools_use_times/night
survey['app_other_tools_use_times/night'].value_counts(dropna=False)
```

```{.json .output n=95}
[
 {
  "data": {
   "text/plain": "NaN    1124\n 0       36\n 1       24\ndtype: int64"
  },
  "execution_count": 95,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_per_wk
English: For ${app_other_desc} ("any other"), how many times a week do you use
it?

Indonesian: Untuk ${app_other_desc} ("ada yang lain"), berapa kali seminggu anda
menggunakannya?

```{.python .input  n=96}
## app_other_per_wk
survey['app_other_per_wk'].value_counts(dropna=False)
survey['app_other_per_wk'].describe()
```

```{.json .output n=96}
[
 {
  "data": {
   "text/plain": "count      406.000000\nmean        42.204433\nstd        744.179565\nmin          0.000000\n25%          3.000000\n50%          7.000000\n75%          7.000000\nmax      15000.000000\nName: app_other_per_wk, dtype: float64"
  },
  "execution_count": 96,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_hrs
English:  For ${app_other_desc} ("any other"), each time you use it, how many
hours do you use it for?

Indonesian: Untuk ${app_other_desc} ("ada yang lain"), selama berapa jam setiap
kali anda menggunakannya?

```{.python .input  n=97}
## app_other_hrs
survey['app_other_hrs'].value_counts(dropna=False)
survey['app_other_hrs'].describe()
```

```{.json .output n=97}
[
 {
  "data": {
   "text/plain": "count    405.000000\nmean       5.076543\nstd        5.491809\nmin        0.000000\n25%        2.000000\n50%        3.000000\n75%        6.000000\nmax       24.000000\nName: app_other_hrs, dtype: float64"
  },
  "execution_count": 97,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_use_times
English:  For ${app_other_desc} ("any other"), what time of the day do you
typically use it?

Indonesian: Untuk ${app_other_desc} ("ada yang lain"), jam berapa biasannya anda
menggunakannya?

```{.python .input  n=98}
## app_other_use_times
survey['app_other_use_times'].value_counts(dropna=False)
```

```{.json .output n=98}
[
 {
  "data": {
   "text/plain": "NaN                                780\nnight                              179\nmorning mid_day afternoon night     70\nafternoon night                     27\nmorning mid_day                     22\nmorning                             21\nmorning mid_day afternoon           20\nmid_day night                       18\nmorning night                       15\nmid_day                             14\nmorning afternoon                    7\nmorning mid_day night                4\nmid_day afternoon                    3\nmorning afternoon night              3\nmid_day afternoon night              1\ndtype: int64"
  },
  "execution_count": 98,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_use_times/morning

```{.python .input  n=99}
## app_other_use_times/morning
survey['app_other_use_times/morning'].value_counts(dropna=False)
```

```{.json .output n=99}
[
 {
  "data": {
   "text/plain": "NaN    780\n 0     242\n 1     162\ndtype: int64"
  },
  "execution_count": 99,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_use_times/mid_day

```{.python .input  n=100}
## app_other_use_times/mid_day
survey['app_other_use_times/mid_day'].value_counts(dropna=False)
```

```{.json .output n=100}
[
 {
  "data": {
   "text/plain": "NaN    780\n 0     252\n 1     152\ndtype: int64"
  },
  "execution_count": 100,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_use_times/afternoon

```{.python .input  n=101}
## app_other_use_times/afternoon
survey['app_other_use_times/afternoon'].value_counts(dropna=False)
```

```{.json .output n=101}
[
 {
  "data": {
   "text/plain": "NaN    780\n 0     273\n 1     131\ndtype: int64"
  },
  "execution_count": 101,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

## app_other_use_times/night

```{.python .input  n=102}
## app_other_use_times/night
survey['app_other_use_times/night'].value_counts(dropna=False)
```

```{.json .output n=102}
[
 {
  "data": {
   "text/plain": "NaN    780\n 1     317\n 0      87\ndtype: int64"
  },
  "execution_count": 102,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input}

```
