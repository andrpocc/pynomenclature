letters_list_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                   'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v']

letters_list_ru = [['а', 'б'],
                   ['в', 'г']]

letters_list_ru_up = [['А', 'Б'],
                      ['В', 'Г']]


def to_degrees(degrees: int, minutes: float, seconds: float = 0):
    return degrees + minutes / 60 + seconds / 3600


def map_1000000(longitude, latitude):
    latitude_boundaries = list()
    longitude_boundaries = list()
    map_longitude = 0
    n = 0
    while map_longitude < longitude:
        if map_longitude < longitude:
            map_longitude += 6
            n += 1
            longitude_boundaries = [map_longitude - 6, map_longitude]
    n += 30
    if n > 60:
        n -= 60

    map_latitude = 0
    f = 0
    while map_latitude < latitude:
        if map_latitude < latitude:
            map_latitude += 4
            f += 1
            latitude_boundaries = [map_latitude - 4, map_latitude]
    col = n
    line = letters_list_en[f-1]
    return str(col), line.upper(), longitude_boundaries, latitude_boundaries


def map_100000(longitude_boundaries_1000000: list, latitude_boundaries_1000000: list, longitude, latitude):
    start_longitude = longitude_boundaries_1000000[0]
    end_longitude = longitude_boundaries_1000000[1]
    start_latitude = latitude_boundaries_1000000[0]
    end_latitude = latitude_boundaries_1000000[1]
    i, j = 0, 0
    longitude_boundaries = list()
    latitude_boundaries = list()
    while start_longitude < longitude:
        if start_longitude < longitude:
            start_longitude += 30/60
            i += 1
    longitude_boundaries = [start_longitude - 30/60, start_longitude]
    while end_latitude > latitude:
        if end_latitude > latitude:
            end_latitude -= 20/60
            j += 1
    latitude_boundaries = [end_latitude, end_latitude + 20/60]
    position = (j-1) * 12 + i
    return str(position), longitude_boundaries, latitude_boundaries


def map_5000(longitude_boundaries_5000: list, latitude_boundaries_5000: list, longitude, latitude):
    start_longitude = longitude_boundaries_5000[0]
    end_longitude = longitude_boundaries_5000[1]
    start_latitude = latitude_boundaries_5000[0]
    end_latitude = latitude_boundaries_5000[1]
    i, j = 0, 0
    longitude_boundaries = list()
    latitude_boundaries = list()
    while start_longitude < longitude:
        if start_longitude < longitude:
            start_longitude += to_degrees(0,1,52.5)
            i += 1
    longitude_boundaries = [start_longitude - to_degrees(0,1,52.5), start_longitude]
    while end_latitude > latitude:
        if end_latitude > latitude:
            end_latitude -= to_degrees(0,1,15)
            j += 1
    latitude_boundaries = [end_latitude, end_latitude + to_degrees(0,1,15)]
    position = (j-1) * 16 + i
    return str(position), longitude_boundaries, latitude_boundaries


def map_50000(longitude_boundaries_100000: list, latitude_boundaries_100000: list, longitude, latitude):
    start_longitude = longitude_boundaries_100000[0]
    end_longitude = longitude_boundaries_100000[1]
    start_latitude = latitude_boundaries_100000[0]
    end_latitude = latitude_boundaries_100000[1]
    i, j = 0, 0
    longitude_boundaries = list()
    latitude_boundaries = list()
    while start_longitude < longitude:
        if start_longitude < longitude:
            start_longitude += 15 / 60
            i += 1
    longitude_boundaries = [start_longitude - 15 / 60, start_longitude]
    while end_latitude > latitude:
        if end_latitude > latitude:
            end_latitude -= 10 / 60
            j += 1
    latitude_boundaries = [end_latitude, end_latitude + 10/60]
    position = letters_list_ru_up[j-1][i-1]
    return position, longitude_boundaries, latitude_boundaries


def map_25000(longitude_boundaries_50000: list, latitude_boundaries_50000: list, longitude, latitude):
    start_longitude = longitude_boundaries_50000[0]
    end_longitude = longitude_boundaries_50000[1]
    start_latitude = latitude_boundaries_50000[0]
    end_latitude = latitude_boundaries_50000[1]
    i, j = 0, 0
    longitude_boundaries = list()
    latitude_boundaries = list()
    while start_longitude < longitude:
        if start_longitude < longitude:
            start_longitude += 7.5 / 60
            i += 1
    longitude_boundaries = [start_longitude - 7.5 / 60, start_longitude]
    while end_latitude > latitude:
        if end_latitude > latitude:
            end_latitude -= 5 / 60
            j += 1
    latitude_boundaries = [end_latitude, end_latitude + 5 / 60]
    position = letters_list_ru[j - 1][i - 1]
    return position, longitude_boundaries, latitude_boundaries
