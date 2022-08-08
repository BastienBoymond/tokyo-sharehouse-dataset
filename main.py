#!/usr/bin/env python3

from tokyosharehouse import TokyoShareHouse
from university import getAllUniversity

university = input("Enter list of universities you want distance to sharehouse (ex: Shibaura Institute of Technology,...,...) if you want all university press Enter : ").split(',')

if len(university) == 1 and university[0] == "":
    university = getAllUniversity();

sharehouse = TokyoShareHouse(university)
filename = input("Enter the filename output: ");
filename += ".csv";

file = open(filename, "w");
file.close();
