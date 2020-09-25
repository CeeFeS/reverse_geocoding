from geopy.geocoders import Nominatim
import utm
import getpass
# import only system from os
from os import system, name

# source(https://www.geeksforgeeks.org/clear-screen-python/)
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

print("UTM ZONE (https://mangomap.com/robertyoung/maps/69585/what-utm-zone-am-i-in-#): ")
input_utm_zone = int(input())
clear()

while True:

    #input as terminal tool
    print("X:")
    # input latitude (x) UTM33
    input_x = float(input())
    print("Y:")
    # input longtude (y) UTM33
    input_y = float(input())
    # utm (UTM33) to DG
    long_lat = utm.to_latlon(input_x, input_y, input_utm_zone, 'U')
    #useragent is current username
    username = getpass.getuser()
    # reverse geo engineer with DG
    geolocator = geolocator = Nominatim(user_agent=username)
    location = geolocator.reverse(long_lat)
    #print results
    print("\n------results------\n")
    print(long_lat)
    print(location.address)
    print("\n-------------------\n\n")
