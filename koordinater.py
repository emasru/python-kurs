from geopy import Nominatim


def koordinater(sted):
    locator = Nominatim(user_agent="vsenter")
    location = locator.geocode(sted)
    return location.latitude, location.longitude


