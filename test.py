import folium
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from folium.plugins import MarkerCluster

house = pd.read_csv("C:/Users/USER/Documents/LS빅데이터스쿨/testdashboard/data/houseprice-with-lonlat.csv")

house["Longitude"].mean()
house["Latitude"].mean()

house_map=folium.Map(location=[42.03448223395904,-93.64289689856655],zoom_start=12,
                 tiles="cartodbpositron")

marker_cluster = MarkerCluster().add_to(house_map)

for idx, row in house.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup="집들,,"
    ).add_to(marker_cluster)

house_map.save("map_seoul.html")

---------------------------------------------------------------------------
house_df = pd.read_csv("data/houseprice/houseprice-with-lonlat.csv")

house_df = house_df[["Longitude", "Latitude"]]

center_x=house_df["Longitude"].mean()
center_y=house_df["Latitude"].mean()


map_sig=folium.Map(location = [42.034, -93.642],
                  zoom_start = 12,
                  tiles="cartodbpositron")

marker_cluster = MarkerCluster().add_to(map_sig)

for idx, row in house_df.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup="집들,,"
    ).add_to(marker_cluster)


map_sig.save("map_ames.html")
------------------------------------------------------------------------

house_df = house[["Longitude", "Latitude"]]
house_df


house_df["Longitude"].mean()
house_df["Latitude"].mean()

my_map = folium.Map(location=[42.03, -93.64], 
                    zoom_start=12,
                    tiles= "cartodbpositron") # 확대 단계
my_map.save("map_seoul.html")


for lat, lon in zip(house_df['Latitude'], house_df['Longitude']):
  folium.Marker([lat, lon]).add_to(my_map)
  
my_map.save("map_seoul2.html")
