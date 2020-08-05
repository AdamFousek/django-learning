import gpxpy.gpx
import gpxpy
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")


def city_state_country(coord):
    location = geolocator.reverse(coord, exactly_one=True)
    address = location.raw['address']
    suburb = address.get('suburb', '')
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    return suburb, city, state, country


print(city_state_country("49.8633381, 18.0931958"))

"""
# Parsing an existing file:
# -------------------------
gpx_file = open('export.gpx', 'r')

gpx = gpxpy.parse(gpx_file)
print(gpx)

for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            print()
            print(city_state_country("{0}, {1}".format(point.latitude,
                                                       point.longitude)))
            # print('Point at ({0},{1}) -> {2}'.format(point.latitude,point.longitude, point.elevation))

for waypoint in gpx.waypoints:
    print('waypoint {0} -> ({1},{2})'.format(waypoint.name,
                                             waypoint.latitude, waypoint.longitude))

for route in gpx.routes:
    print('Route:')
    for point in route.points:
        print('Point at ({0},{1}) -> {2}'.format(point.latitude,
                                                 point.longitude, point.elevation))

# There are many more utility methods and functions:
# You can manipulate/add/remove tracks, segments, points, waypoints and routes and
# get the GPX XML file from the resulting object:

# print('GPX:', gpx.to_xml())
"""
