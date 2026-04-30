import pandas as pd

lego_sets = pd.read_csv('data/lego_sets.csv')
lego_sets.head()


parent_themes = pd.read_csv('data/parent_themes.csv')
parent_themes.head()

lego_clean = lego_sets.dropna(subset=['set_num'])
lego_clean.head()


licensed_all = parent_themes[parent_themes['is_licensed']]['name']
licensed_all.head()

licensed_sets = lego_clean['parent_theme'].isin(licensed_all)
licensed = lego_clean[licensed_sets]
licensed.head()

all_sets = len(licensed)

star_wars = len(licensed[licensed['parent_theme'] == 'Star Wars'])

ratio = star_wars / all_sets
the_force = int(ratio * 100)

print("Lisanslı Star Wars setleri oranı: %", the_force)


max_year = licensed.groupby(['year', 'parent_theme']).size().reset_index(name='count')

sw_max = max_year[max_year['parent_theme'] == 'Star Wars']

new_era = int(sw_max.sort_values('count', ascending=False).iloc[0]['year'])

print("Star Wars setlerinin en fazla oldugu yıl: ", new_era)