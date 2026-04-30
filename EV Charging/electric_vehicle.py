import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

private_ev = pd.read_csv("private_ev_charging.csv")
public_ev = pd.read_csv("public_ev_charging.csv")
ev_sales = pd.read_csv("ev_sales.csv")

ev_total_sales = ev_sales.groupby('year')['sales'].sum().reset_index()

sales_2018_row = ev_total_sales[ev_total_sales['year'] == 2018]
ev_sales_2018 = int(sales_2018_row['sales'].iloc[0])


charging_merged = private_ev.merge(public_ev, on='year')

df_final = charging_merged.merge(ev_total_sales, on='year')


fig, ax = plt.subplots(figsize=(10, 6))


sns.lineplot(data=df_final, x='year', y='private_ports', label='Private Ports', ax=ax)
sns.lineplot(data=df_final, x='year', y='public_ports', label='Public Ports', ax=ax)
sns.lineplot(data=df_final, x='year', y='sales', label='Total Sales', linestyle=':', ax=ax)


ax.set_title('Electric Vehicle Trends (2015-2018)')
ax.set_xlabel('Year')
ax.set_ylabel('Count')
ax.legend()

plt.show()


trend = "same"