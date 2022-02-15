import sys
from rainlibs.datasources import load_csv
from rainlibs.geo import find_city_lat_lon_in_us

def main(city):

    data_source = '/home/ali/Downloads/chirps20GlobalPentadP05_233e_7ccc_b137.csv'
    rain_data = load_csv(data_source)

    c_lat, c_lon = find_city_lat_lon_in_us(city)

    dist_thresh=0.05
    rain_thresh=8.0
    dates=list()
    for row in rain_data:
        t,lat,lon,rain=row
        t=t[:10]
        lat_diff=abs(float(lat)-float(c_lat))
        lon_diff=abs(float(lon)-float(c_lon))
        if rain != "NaN":
            if float(rain) >= rain_thresh:
                if lat_diff<dist_thresh:
                    if lon_diff<dist_thresh:
                        dates.append((t,rain))

    # dates=sorted(list(set(dates)))
    for item in dates:
        print(item)
    print("number of rainy 5-days: "+str(len(dates)))

if __name__ == "__main__":
    # is there any city name on command line ?
    if len(sys.argv) > 1:
        city = sys.argv[1]
    else:
        city = str(input("Enter city name:[San Jose]") or "San Jose")
    main(city)


