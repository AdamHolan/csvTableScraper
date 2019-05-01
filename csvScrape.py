import glob
import csv

# last two entries are bad remnants of my logic, too lazy to fix the code itself
unacceptable = ['Bronze', 'Gold', 'Silver', 'Totals', 'Rank', 'NOC', 'Total', 'Totals NOCs)', 'Totals nations)']
countriesList = []
singlesList = []
multiplesList = []

# open every csv file in a folder, works like magic, thanks glob
for file in glob.glob('*.csv'):

    # open the current file im on
    with open(file, 'r') as csvFile:

        # dunno what this line does
        reader = csv.reader(csvFile)

        # for every row apparently
        for row in reader:

            # remnant of lazy code too tired to fix rn
            zipped = zip(row, range(len(row)))

            # not every column, but every entry, too lazy to fix cause i know the syntax
            for column, i in zipped:
                # again, not really a line. its just the entry turned into a list
                line = list(column)
                # if it has a bracket, kill it
                if '(' in line:
                    line = [x for x in column.split()]
                    for element in line:
                        if '(' in list(element):
                            line.remove(element)
                    column = ''
                    for char in line:
                        column += char + ' '

                    # lazy code im removing the space at the end
                    column = column[:-1]

                # i needed to put this in separately otherwise i get spaced words
                else:
                    column = ''
                    for char in line:
                        column += char

                # if its an int, its not a word, so don't add it to the list of countries
                try:
                    int(column)
                except ValueError:
                    countriesList.append(column)

    # close file and move on with my life
    csvFile.close()

# v --- if you're going to fix anything, or change some logic, the problem is probably below --- v

# remove anything that isn't a country
countriesList = [x for x in countriesList if x not in unacceptable]

# if the country appears more than once, add it if it doesn't already exist
for country in countriesList:
    if countriesList.count(country) > 1:
        if country not in multiplesList:
            multiplesList.append(country)
    else:
        singlesList.append(country)

# i sort for clarity
multiplesList.sort()
singlesList.sort()

# add shit to first file
file = open('moreThanOnce.txt', 'w+')
file.write('The countries that are in multiple events: \n')

for entry in multiplesList:
    file.write(entry + '\n')
# add shit to second file
file2 = open('onlyOnce.txt', 'w+')
file2.write('The countries that only participated once are: \n')

for entry in singlesList:
    file2.write(entry + '\n')
