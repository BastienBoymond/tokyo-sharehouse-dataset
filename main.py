#!/usr/bin/env python3

from tokyosharehouse import TokyoShareHouse
from university import getAllUniversity, getUniCoord

university_to_get = input("Enter list of universities you want distance to sharehouse (ex: Shibaura Institute of Technology,...,...) if you want all university press Enter : ").split(',')
onlyAvailable = input("Do you want only available sharehouse? (y/n) : ")
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

filename = input("Enter the filename output: ");
filename += ".csv";
sharehouse = TokyoShareHouse(university, onlyAvailable);

sharehouse.writeToFile(filename);
print("CSV Created with filename:" + filename);
