# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Start your code here!


flights = pd.read_csv("flights2022.csv")
weather = pd.read_csv("flights_weather2022.csv")

flights["route"] = flights["origin"] + "-" + flights["dest"]

flights["is_cancelled"] = flights["dep_time"].isna()

routes_delays_cancels = flights.groupby("route").agg(
    avg_dep_delay=("dep_delay", "mean"), # ortalama gec kalma suresi
    max_cancellation=("is_cancelled", "sum") # cancellation sayisi
).reset_index()

airlines_delays_cancels = flights.groupby("airline").agg(
    avg_dep_delay=("dep_delay", "mean"),
    max_cancellation=("is_cancelled", "sum")
).reset_index()

# En çok iptal edilen 9 rota

top9_route_cancels_bar, ax1 = plt.subplots(figsize=(12, 6))
top9_route_cancels = routes_delays_cancels.sort_values("max_cancellation", ascending=False).head(9)
ax1.bar(top9_route_cancels["route"], top9_route_cancels["max_cancellation"])
ax1.set_title("En Çok İptal Olan 9 Rota")
plt.show()

# En çok geciken 9 havayolu

top9_airline_delays_bar, ax2 = plt.subplots(figsize=(12, 6))
top9_airline_delays = airlines_delays_cancels.sort_values("avg_dep_delay", ascending=False).head(9)
ax2.bar(top9_airline_delays["airline"], top9_airline_delays["avg_dep_delay"])
ax2.set_title("En Çok Geciken 9 Havayolu")
ax2.tick_params(rotation = 90)
plt.show()

flights["wind"] = weather["wind_gust"].apply(lambda x: "10<" if x >= 10 else "10>" )


wind_origin_delay = flights.groupby(["wind","origin"]).agg(
    wind_dep_delay = ("dep_delay", "mean")
)


wind_fast = weather[weather["wind_gust"] >= 10]["dep_delay"].mean()
wind_slow = weather[weather["wind_gust"] < 10]["dep_delay"].mean()

wind_response = wind_fast > wind_slow

print(wind_origin_delay)
print(wind_response)
