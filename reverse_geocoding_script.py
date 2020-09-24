from geopy.geocoders import Nominatim
import utm

while True:

    #input as terminal tool
    print("X:")
    # input latitude (x) UTM33
    input_x = float(input())
    print("Y:")
    # input longtude (y) UTM33
    input_y = float(input())
    # utm (UTM33) to DG
    long_lat = utm.to_latlon(input_x, input_y, 33, 'U')
    print(long_lat)
    # reverse geo engineer with DG
    geolocator = geolocator = Nominatim(user_agent="cfs_geo_reverse")
    location = geolocator.reverse(long_lat)
    
    print(location.address)
    print("-----------------------------------")
