import pandas as pd
import matplotlib.pyplot as plt

flights = pd.read_csv("flights2022.csv")
weather = pd.read_csv("flights_weather2022.csv")
sleep = pd.read_csv("sleep_health_data.csv")
soil = pd.read_csv("soil_measures.csv")
lego = pd.read_csv("lego_sets.csv")

'''
Soru 1: 
Her havayolu şirketinin (airline) hangi havaalanından (origin) 
kaçar tane uçuş gerçekleştirdiğini gösteren bir özet tablo oluştur.
'''
flight_pivot = flights.pivot_table(index='airline', columns='origin', values='dep_time', aggfunc='count').fillna(0)
print("\nSoru 1")
print(flight_pivot.head())


'''
Soru 2: 
Quality of Sleep puanı 8 ve üzeri olanlara "Good", 
6-7 arasındakilere "Normal", 6'dan küçük olanlara "Bad" yazan Sleep_Status adlı yeni bir sütun ekle.
'''
def sleep_score(score):
    if score >= 8: return "Good"
    elif score >= 6: return "Normal"
    else: return "Bad"

sleep['Sleep_Status'] = sleep['Quality of Sleep'].apply(lambda x: sleep_score(x))
print("\nSoru 2")
print(sleep[['Occupation', 'Quality of Sleep', 'Sleep_Status']].head())


'''
Soru 3: 
LEGO setleri için yıllara (year) göre ana temaların (parent_theme) 
set sayılarını gösteren bir özet tablo oluştur.
'''
lego_pivot = lego.pivot_table(index='year', columns='parent_theme', values='set_num', aggfunc='count').fillna(0)
print("\nSoru 3")
print(lego_pivot.head())


'''
Soru 4: 
Toprak ölçümlerinde Potasyum (K) değeri 200'den büyükse "Rich", 
değilse "Standard" yazan K_Level adlı yeni bir sütun ekle.
'''

soil['K_Level'] = soil['K'].apply(lambda x: "Rich" if x > 200 else "Standard")
print("\nSoru 4")
print(soil[['crop', 'K', 'K_Level']].head())


'''
Soru 5: 
Hava durumu verisinde rüzgar hamlesi (wind_gust) 15 mph ve üzeriyse "Stormy", 
altındaysa "Calm" yazan Wind_Condition sütunu ekle.
'''
weather['Wind_Condition'] = weather['wind_gust'].apply(lambda x: "Stormy" if x >= 15 else "Calm")
print("\nSoru 5")
print(weather[['year', 'month', 'day', 'wind_gust', 'Wind_Condition']].head())


'''
Soru 6: 
Uçuş verilerinde kalkış gecikmesi (dep_delay) 15 dakikadan fazlaysa "Late", 
0 ile 15 arasındaysa "On Time", 0'dan küçükse "Early" yazan Delay_Status sütunu ekle.
'''
def check_delay(delay):
    if delay > 15: return "Late"
    elif delay >= 0: return "On Time"
    else: return "Early"

flights['Delay_Status'] = flights['dep_delay'].apply(check_delay)
print("\nSoru 6")
print(flights[['airline', 'dep_delay', 'Delay_Status']].head())


'''
Soru 7: 
Toprak verisinde her ürün (crop) için ortalama pH ve Fosfor (P) 
değerlerini gösteren bir özet tablo oluştur.
'''
soil_pivot = soil.pivot_table(index='crop', values=['ph', 'P'], aggfunc='mean')
print("\nSoru 7")
print(soil_pivot.head())


'''
Soru 8: 
LEGO setlerinde parça sayısı (num_parts) 1000'den fazlaysa "Expert", 
100-1000 arasındaysa "Intermediate", 100'den azsa "Beginner" kategorisi ekle.
'''
def lego_difficulty(parts):
    if parts >= 1000: return "Expert"
    elif parts >= 100: return "Intermediate"
    else: return "Beginner"

lego['Difficulty'] = lego['num_parts'].apply(lego_difficulty)
print("\nSoru 8")
print(lego[['name', 'num_parts', 'Difficulty']].head())


'''
Soru 9: 
Havayolu şirketlerinin her havaalanındaki (origin) 
ortalama kalkış gecikmelerini (dep_delay) gösteren bir özet tablo oluştur.
'''
airline_delay_pivot = flights.pivot_table(index='airline', columns='origin', values='dep_delay', aggfunc='mean')
print("\nSoru 9")
print(airline_delay_pivot.head())


'''
Soru 10: 
Uyku verisinde günlük adım sayısı (Daily Steps) 8000'den fazlaysa "Active", 
5000-8000 arasındaysa "Moderate", 5000'den azsa "Sedentary" etiketi ekle.
'''
sleep['Activity_Level'] = sleep['Daily Steps'].apply(lambda x: "Active" if x > 8000 else ("Moderate" if x >= 5000 else "Sedentary"))
print("\nSoru 10")
print(sleep[['Occupation', 'Daily Steps', 'Activity_Level']].head())


'''
Soru 11: 
Uyku verisindeki stres seviyesini (Stress Level) şu şekilde grupla:
1-3 arası "Low", 4-7 arası "Medium", 8-10 arası "High". 
Sonucu 'Stress_Category' sütununa kaydet.
'''
def categorize_stress(level):
    if level <= 3: return "Low"
    elif level <= 7: return "Medium"
    else: return "High"

sleep['Stress_Category'] = sleep['Stress Level'].apply(categorize_stress)
print("\nSoru 11")
print(sleep[['Occupation', 'Stress Level', 'Stress_Category']].head())


'''
Soru 12: 
Toprak verisinde her ürün (crop) tipi için ölçülen 
maksimum Azot (N) miktarını gösteren bir özet tablo oluştur.
'''
soil_max_n = soil.pivot_table(index='crop', values='N', aggfunc='max')
print("\nSoru 12")
print(soil_max_n)


'''
Soru 13: 
LEGO setlerini üretim yıllarına göre kategorize et:
1990 öncesi "Retro", 1990-2010 arası "Classic", 2010 sonrası "Modern".
Sonucu 'Era' sütununa kaydet.
'''
def get_era(year):
    if year < 1990: return "Retro"
    elif year <= 2010: return "Classic"
    else: return "Modern"

lego['Era'] = lego['year'].apply(get_era)
print("\nSoru 13")
print(lego[['name', 'year', 'Era']].head())


'''
Soru 14: 
Havayolu şirketlerinin kalkış yaptıkları her havaalanındaki (origin) 
en düşük (minimum) gecikme süresini gösteren bir özet tablo oluştur.
'''
min_delay_pivot = flights.pivot_table(index='airline', columns='origin', values='dep_delay', aggfunc='min')
print("\nSoru 14")
print(min_delay_pivot.head())


'''
Soru 15: 
Hava durumu verisindeki görüş mesafesini (visib) şu şekilde sınıflandır:
10 mil "Perfect", 7-9.9 mil "Clear", 7 milden azsa "Hazy".
Sonucu 'Visibility_Status' sütununa kaydet.
'''
def check_visib(v):
    if v >= 10: return "Perfect"
    elif v >= 7: return "Clear"
    else: return "Hazy"

weather['Visibility_Status'] = weather['visib'].apply(check_visib)
print("\nSoru 15")
print(weather[['visib', 'Visibility_Status']].head())


'''
Soru 16: 
Uçuş ve Hava Durumu verilerini birleştir. Hem rüzgar (wind_gust) hem de 
görüş mesafesini (visib) kontrol ederek bir "Risk_Level" sütunu oluştur:
- Rüzgar > 20 VEYA Görüş < 5 ise "High Risk"
- Rüzgar 10-20 arası VEYA Görüş 5-9 arası ise "Medium Risk"
- Diğer durumlar "Low Risk"
Ardından, her havayolunun bu risk seviyelerindeki ortalama gecikmesini 
pivot tablo ile göster ve sonuçları çubuk grafik (bar plot) olarak çiz.
'''
merged = flights.merge(weather, on=['year', 'month', 'day', 'hour', 'origin', 'dest', 'airline'])

def determine_risk(row):
    if row['wind_gust'] > 20 or row['visib'] < 5:
        return "High Risk"
    elif (10 <= row['wind_gust'] <= 20) or (5 <= row['visib'] <= 9):
        return "Medium Risk"
    else:
        return "Low Risk"

merged['Risk_Level'] = merged.apply(determine_risk, axis=1) #axis 1 satırdaki tüm sütunları göndermek için kullanılır

risk_pivot = merged.pivot_table(index='airline', columns='Risk_Level', values='dep_delay_x', aggfunc='mean')

risk_pivot.plot(kind='bar')
plt.title("Havayollarının Risk Seviyesine Göre Ortalama Gecikmesi")
plt.ylabel("Ortalama Gecikme")
plt.xticks(rotation=90)
plt.show()

print("\nSoru 16")
print(risk_pivot.head())


'''
Soru 17: 
Uyku verisinde "Wellness_Score" adında gelişmiş bir puanlama sistemi kur:
Puan = (Sleep Duration * 10) + (Quality of Sleep * 5) - (Stress Level * 3)
Bu puanı hesapladıktan sonra, mesleklere (Occupation) göre puan ortalamalarını 
pivot tablo ile çıkar. En yüksek puana sahip ilk 5 mesleği yatay bar grafikte göster.
'''

def wellness(row):
    score = (row['Sleep Duration'] * 10) + (row['Quality of Sleep'] * 5) - (row['Stress Level'] * 3)
    return score

sleep['Wellness_Score'] = sleep.apply(wellness, axis=1)


wellness_pivot = sleep.pivot_table(index='Occupation', values='Wellness_Score', aggfunc='mean')


top_5 = wellness_pivot.sort_values(by='Wellness_Score').head(5)


top_5.plot(kind='barh')
plt.title("En Yüksek Wellness Skoruna Sahip İlk 5 Meslek")
plt.xlabel("Ortalama Wellness Puanı")
plt.show()

print("\nSoru 17")
print(top_5)
