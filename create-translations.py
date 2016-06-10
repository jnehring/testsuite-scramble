infile = open("output/scramble-2016-06-07---10-09-00.txt", "r")
outfile = open("output/translation-2016-06-07---10-09-00.txt", "w")

for line in infile:
    outfile.write(line.upper())

infile.close()
outfile.close()