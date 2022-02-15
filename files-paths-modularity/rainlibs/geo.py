import requests

def find_city_lat_lon_in_us(city_name):
    """
    specific function
    :param city_name:
    :return:
    """
    base_url = "https://nominatim.openstreetmap.org/"
    query = "search.php?city=" + city_name + "&format=jsonv2&namedetails=0&addressdetails=0&limit=1"
    full_url = base_url + query
    response = requests.get(full_url)
    city_data = response.json()
    lat = city_data[0]['lat']
    lon = city_data[0]['lon']
    return lat, lon

if __name__ == "__main__":
    city = str(input("Enter city name:[San Jose]") or "San Jose")
    print(find_city_lat_lon_in_us(city))





