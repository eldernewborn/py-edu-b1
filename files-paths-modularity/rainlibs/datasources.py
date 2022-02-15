import csv

# rain data from .
# https://coastwatch.pfeg.noaa.gov/erddap/griddap/chirps20GlobalPentadP05.html
# used dataset:
# https://coastwatch.pfeg.noaa.gov/erddap/griddap/chirps20GlobalPentadP05.csv?precip%5B(2021-8-01T00:00:00Z):1:(2021-11-26T00:00:00Z)%5D%5B(30.0):.25:(42.0)%5D%5B(-123.0):.25:(-113.0)%5D

def load_csv(csv_path):
    csv_file = open(csv_path)
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    rain_data = list()
    for row in csv_reader:
        line_count += 1
        if line_count <=2:
            # print(f'Column names are {", ".join(row)}')
            continue
        elif line_count >=10e10:
            break
        rain_data.append(row)
    csv_file.close()
    return rain_data
