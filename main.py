from nomenclature import *
print('Введите широту:')
lat = input().split(' ')
lat = to_degrees(int(lat[0]), float(lat[1]), float(lat[2]))
print('Введите долготу:')
long = input().split()
long = to_degrees(int(long[0]), float(long[1]), float(long[2]))

col, line, long_list, lat_list = map_1000000(long, lat)
pos1, long_list100, lat_list100 = map_100000(long_list, lat_list, long, lat)
pos2, long_list50, lat_list50 = map_50000(long_list100, lat_list100, long, lat)
pos3, long_list25, lat_list25 = map_25000(long_list50, lat_list50, long, lat)
pos4, long_list, lat_list = map_5000(long_list100, lat_list100, long, lat)

print('\n' * 2)
print('Номенклатура карты 1:25000')
print('{}-{}-{}-{}-{}'.format(line, col, pos1, pos2, pos3))
print('\n')
print('Номенклатура карты 1:5000')
print('{}-{}-{}({})'.format(line, col, pos1, pos4))

input()