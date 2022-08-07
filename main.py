from tokyosharehouse import TokyoShareHouse

sharehouse = TokyoShareHouse()
filename = input("Enter the filename output: ");
filename += ".csv";

file = open(filename, "w");
file.close();