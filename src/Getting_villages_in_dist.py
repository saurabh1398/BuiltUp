#This code downloads villages in each district in a state
#There are three input arguments. Ex: python3 Gettingn_villages_in_dist.py Bokaro Jharkhand JH.geojson

import shapely
import geopandas as gpd
from shapely.geometry import Point
from shapely.geometry import Polygon
import sys
import os

#current working directory
cwd = os.getcwd()

dist = sys.argv[1]
dist = dist.replace('_',' ')

state = sys.argv[2]
state = state.replace('_',' ')

state_filename = sys.argv[3]
state_filename = cwd+'/data/State_GeoJSON/' + state_filename

print('Finding villages in: ',dist,state)
print('shapefile: ',state_filename)
print('Please wait...')

#shapefile of the villages in a state
df_vill = gpd.read_file(state_filename)

#the boundaries of a district
dist_filename = cwd + '/data/india_district_boundaries.geojson'
df_dist = gpd.read_file(dist_filename)

df_temp = df_dist[df_dist['Name'] == dist] 
df_temp.head()

#append all the villages in the district
arr = []
for i in range(len(df_vill)):
    try:
        arr.append(df_temp['geometry'].contains(df_vill['geometry'][i]).values[0])
    except:
        arr.append(False)
        print('Error for village: ',i,df_vill['VILL_NAME'][i])

d1 = df_vill[arr]
d1 = d1.reset_index(drop='True')

#save the villages in geojson file
path = cwd+'/data/District_GeoJson/'+state.replace(' ','')
print(path)
if(not(os.path.exists(path))):
    os.makedirs(path)

try:
    path = path + '/'+dist.replace(' ','')+'.geojson'
    d1.to_file(path,driver='GeoJSON')
    print('Done!')
except:
    print('No villages found in: ',dist)



