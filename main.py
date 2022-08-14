#!/usr/bin/env python3

from tokyosharehouse import TokyoShareHouse
from university import getAllUniversity, getUniCoord

university_to_get = input("\33[34m" + "Enter list of universities you want distance to sharehouse (ex: Shibaura Institute of Technology,...,...) if you want all university press Enter : " + "\33[0m").split(',')
onlyAvailable = input("\33[34m" +"Do you want only available sharehouse? (y/n) : " + "\33[0m")
university = []

if len(university_to_get) == 1 and university_to_get[0] == "":
    university = getAllUniversity();
else:
    for uni in university_to_get:
        uni = getUniCoord(uni);
        university.append(uni)

if (onlyAvailable == 'y' or onlyAvailable == 'Y' or onlyAvailable == ''):
    onlyAvailable = True
else:
    onlyAvailable = False

filename = input("\33[92m" + "Enter the filename output: " + "\33[0m");
filename += ".csv";
sharehouse = TokyoShareHouse(university, onlyAvailable);

sharehouse.writeToFile(filename);
print("\33[92m" + "\33[4m" + "CSV Created with filename:" + filename + "\33[0m");
