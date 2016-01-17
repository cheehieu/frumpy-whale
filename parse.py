import numpy as np
from math import *
from io import StringIO
from numpy import genfromtxt

data = genfromtxt('trv_entry_comb_data_final_uniq.csv', dtype=None, delimiter=',')
col_headings = data[0][:]
MET_time = data[1:, np.where(col_headings == " AFM_MET_time")[0][0]]
latitiude = data[1:, np.where(col_headings == " UPP_ecef_longitude")[0][0]]
longitude = data[1:, np.where(col_headings == " UPP_ecef_gd_latitude")[0][0]]
altitude = data[1:, np.where(col_headings == " UPP_ecef_gd_altitude")[0][0]]

test_lat = 10 * (pi/180)
test_long = 20 * (pi/180)

# Transform lat/long coords to J2000 coords
eps = 23.44 * (pi/180)
right_ascension = 180/pi * atan( (sin(test_long)*cos(eps) - tan(test_lat)*sin(eps)) / cos(test_long) )
declination = 180/pi * asin( sin(test_lat)*cos(eps) + cos(test_lat)*sin(test_long) )

print right_ascension, declination