import win32console
from colorama import Fore, init, Style
from pyfiglet import Figlet

from nomenclature import *


def main():
    print(f'{Fore.CYAN}Введите широту (пример: 55 44 33):')
    lat = input().split()
    lat = to_degrees(int(lat[0]), float(lat[1]), float(lat[2]))
    print('Введите долготу (пример: 35 45 55):')
    long = input().split()
    long = to_degrees(int(long[0]), float(long[1]), float(long[2]))

    col, line, long_list, lat_list = map_1000000(long, lat)
    pos1, long_list100, lat_list100 = map_100000(long_list, lat_list, long, lat)
    pos2, long_list50, lat_list50 = map_50000(long_list100, lat_list100, long, lat)
    pos3, long_list25, lat_list25 = map_25000(long_list50, lat_list50, long, lat)
    pos4, long_list, lat_list = map_5000(long_list100, lat_list100, long, lat)

    print(Fore.RED)
    print('Номенклатура листа карты 1:25000')
    print('{}-{}-{}-{}-{}'.format(line, col, pos1, pos2, pos3))
    print()
    print('Номенклатура листа плана 1:5000')
    print('{}-{}-{}({})'.format(line, col, pos1, pos4))
    print()
    print('===================================')
    print()


def run():
    win32console.SetConsoleTitle('PyNomenclature')
    init()
    f = Figlet()
    banner = f.renderText('PyNom')
    print(Style.BRIGHT, end='', sep='')
    print(Fore.RED, banner, sep='', end='')
    print('by Pochatkov A. R.')
    print()
    while True:
        main()


if __name__ == '__main__':
    run()
