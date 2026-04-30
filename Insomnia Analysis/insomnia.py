# Start coding here
# Use as many cells as you need
import pandas as pd




sleep = pd.read_csv('sleep_health_data.csv')

# Which occupation has the lowest average sleep duration? Save this in a string variable called `lowest_sleep_occ`.

sleep_duration = sleep.groupby('Occupation')['Sleep Duration'].mean()

lowest_sleep_occ = sleep_duration.sort_values().index[0]

print("Lowest average sleep duration: ", lowest_sleep_occ)

# Which occupation had the lowest quality of on average? Did the occupation with the lowest sleep duration also have the worst sleep quality?

sleep_quality = sleep.groupby('Occupation')['Quality of Sleep'].mean()  

lowest_sleep_quality_occ = sleep_quality.sort_values().index[0]

print("Lowest sleep quality: ", lowest_sleep_quality_occ)

if lowest_sleep_occ == lowest_sleep_quality_occ:
  same_occ = True
else:
  same_occ = False

print("Is it same: ", same_occ)
  
# Let's explore how BMI Category can affect sleep disorder rates. Start by finding what ratio of app users in each BMI category have been diagnosed with Insomnia.


normal = sleep[(sleep["BMI Category"] == "Normal") & (sleep["Sleep Disorder"] == "Insomnia")]

all_normal = len(sleep[sleep["BMI Category"] == "Normal"])  

normal_insomnia = round(len(normal) / all_normal, 2)



overweight = sleep[(sleep["BMI Category"] == "Overweight") & (sleep["Sleep Disorder"] == "Insomnia")]  

all_overweight = len(sleep[sleep["BMI Category"] == "Overweight"])  

overweight_insomnia = round(len(overweight) / all_overweight, 2)



obese = sleep[(sleep["BMI Category"] == "Obese") & (sleep["Sleep Disorder"] == "Insomnia")]
       
all_obese = len(sleep[sleep["BMI Category"] == "Obese"])  

obese_insomnia = len(obese) / all_obese



bmi_insomnia_ratios = {
    "Normal": normal_insomnia,  
    "Overweight": overweight_insomnia,
    "Obese": obese_insomnia 
}

print(bmi_insomnia_ratios)