# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Start coding here

'''
When was the global search for 'workout' at its peak? Save the year of peak interest as a string named year_str in the format "yyyy".
'''

workout = pd.read_csv("data/workout.csv")


plt.figure(figsize=(12, 6))
plt.plot(workout["month"], workout["workout_worldwide"])
plt.xticks(rotation=90)
plt.title("Workout Popularity")
plt.show()

year_str = "2020"

'''
Of the keywords available, what was the most popular during the covid pandemic, and what is the most popular now? Save your answers as variables called peak_covid and current respectively.
'''

keywords = pd.read_csv("data/three_keywords.csv")

plt.figure(figsize=(12, 6))
plt.plot(keywords["month"], keywords["home_workout_worldwide"])
plt.plot(keywords["month"], keywords["gym_workout_worldwide"])
plt.plot(keywords["month"], keywords["home_gym_worldwide"])
plt.xticks(rotation=90)
plt.legend(["home workout","gym workout","home gym"])
plt.show()

peak_covid = "home workout"
current = "gym workout"

'''
What country has the highest interest for workouts among the following: United States, Australia, or Japan? Save your answer as top_country.
'''

countries = pd.read_csv("data/workout_geo.csv")

clean = countries.dropna(subset = ["workout_2018_2023"]) # verisi olmayanları kaldır, subset

cts = ["United States", "Australia", "Japan"]
country = clean[clean["country"].isin(cts)]

plt.figure(figsize=(12, 6))
plt.bar(clean["country"], clean["workout_2018_2023"])
plt.xticks(rotation=90)
plt.show()

top_country = "United States"

'''
You'd be interested in expanding your virtual home workouts offering to either the Philippines or Malaysia. Which of the two countries has the highest interest in home workouts? Identify the country and save it as home_workout_geo.
'''

malphi_df = pd.read_csv("data/three_keywords_geo.csv", index_col = 0)

print(malphi_df.loc["Philippines", :])
print("\n")
print(malphi_df.loc["Malaysia", :])

home_workout_geo = "Philippines"