from django.shortcuts import render
from django.http import HttpResponse
# from rest_framework import viewsets
# import requests

from skyfield.api import load, wgs84
from skyfield.api import EarthSatellite
import json

stations_url = 'https://celestrak.com/NORAD/elements/1999-025.txt'
# textfile = requests.get(stations_url)
satellites = load.tle_file(stations_url)
# print('Loaded', len(satellites), 'debris')

# response_data = {}
# i = 0
# ts = load.timescale()
# t = ts.now()
# for sat in satellites:
#     response_data[i] = f"{str(sat)}" + " " + f"{str(sat.at(t).position.km)}"
#     i = i+1
#     print(str(sat) + " " + str(sat.at(t).position.km))


ts = load.timescale()
t = ts.now()

# i = 0
sat_data = {}
longitude = []
latitude = []
name = []
epoch = []
for sat in satellites:
    geocentric = sat.at(t)
    # print(sat.name)
    subpoint = wgs84.subpoint(geocentric)
    # print(sat.epoch)
    latitude.append(subpoint.latitude.degrees)
    longitude.append(subpoint.longitude.degrees)
    name.append(sat.name)
    temp = str(sat).split(' ')
    epoch.append(str(temp[6] + " " + temp[7]))
    # this_latitude = subpoint.latitude.degrees
    # this_longitude = subpoint.longitude.degrees
    # print('Latitude:', this_latitude)
    # print('Longitude:', this_longitude)
    # print('Height: {:.1f} km'.format(subpoint.elevation.km))
    # sat_data[i] = {
    #         'Latitude': subpoint.latitude.degrees,
    #         'Longitude': subpoint.longitude.degrees,
    #         'epoch': str(sat.epoch),
    #         'name': str(sat.name)
    # }
    # i+=1

# sat_data_json = json.dumps(sat_data)
sat_data["latitude"] = latitude
sat_data["longitude"] = longitude
sat_data["name"] = name
sat_data["epoch"] = epoch

# Create your views here.

def index(request):
    return HttpResponse(json.dumps(sat_data))

