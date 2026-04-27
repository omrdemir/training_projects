'''
netflix_data.csv

Column          Description
show_id	        The ID of the show
type	        Type of show
title	        Title of the show
director	    Director of the show
cast	        Cast of the show
country	        Country of origin
date_added	    Date added to Netflix
release_year	Year of Netflix release
duration	    Duration of the show in minutes
description	    Description of the show
genre	        Show genre 
'''

# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

movies = netflix_df[netflix_df["type"] == "Movie"] #filmler

before_mil = movies[movies["release_year"] < 2000] #milenyum öncesi

nineties = before_mil[before_mil["release_year"] >= 1990] #doksanlar
#print(nineties)

plt.hist(nineties["duration"])
plt.show()

duration = 100 #en sık görülen film süresi

action_nineties = nineties[nineties["genre"] == "Action"] #doksanlar aksiyon

short_action = 0

for i, row in action_nineties.iterrows():
    if row["duration"] < 90 :
        short_action += 1


print("90s Short Action Movies Count:", short_action)