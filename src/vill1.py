import sys
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import csv
import os

#this function scales the values of the input image
#so that the values of pixels are: 0,1,2,3,4
#0 - backgroung
#1 - green
#2 - water
#3 - built-up
#4 - barren
def adjust_range(img):
  img1 = np.copy(img)
  factor = (4/np.max(img1))

  for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
      img1[i,j] = int(np.round(factor*img1[i,j]))
  
  img1 = img1.astype('int')

  return img1.astype('int')


#compress the other classes to only BU(1) and NBU(2) and Background (0)
def compress_classes(img):
  img1 = np.copy(img)
  img1[img1 == 1] = 2 #green
  img1[img1 == 4] = 2 #barren
  img1[img1 == 3] = 1 #BU

  return img1.astype('uint8')


cwd = os.getcwd()

state = str(sys.argv[1])
state = state.replace('_',' ')

dist_name = str(sys.argv[2])


#take then png image as input
village_name = str(sys.argv[3])
print(state,dist_name,village_name)
vill_code = int(village_name[village_name.find('_')+1:])
#print(village_name)
#print(pc11_vill_code)

vill_name = village_name[:village_name.find('_')]
print(vill_name)
#print('_________')

path2013 = cwd+"/data/IndiaSat/Results/"+dist_name+"/"+village_name+"/results/combined_yearly_prediction_temp_corrected/"+village_name+"_prediction_2013.png"
im2013 = compress_classes(adjust_range(plt.imread(path2013)))

path2019 = cwd+"/data/IndiaSat/Results/"+dist_name+"/"+village_name+"/results/combined_yearly_prediction_temp_corrected/"+village_name+"_prediction_2019.png"
im2019 = compress_classes(adjust_range(plt.imread(path2019)))

bu_pixels2013 = im2013[im2013 == 1].shape[0]
bu_pixels2019 = im2019[im2019 == 1].shape[0]
#print(bu_pixels2014)
#print(bu_pixels2019)

percent_change_bu = 0
if(bu_pixels2013) == 0:
    percent_change_bu = bu_pixels2019
else:
    percent_change_bu = (100 * (bu_pixels2019 - bu_pixels2013))/bu_pixels2013

fname = cwd+'/results/'+state.replace(' ','').lower()+'_villages.csv'
with open(fname,'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([str(vill_code),str(vill_name),str(dist_name),str(bu_pixels2013),str(bu_pixels2019),str(percent_change_bu)])

print('Done!')