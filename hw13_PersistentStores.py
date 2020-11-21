# CSV-to-JSON translator that expects a path to a CSV file as argument, and for each line, prints out a JSON object encapsulating that record
import csv, json, sys
import os

try:
    # retrieve the path from the command line
    path = sys.argv[1]
    # retrieve the extension from the path
    name, extension = os.path.splitext(path)
    # Check that it is a .csv file
    if extension != ".csv":
        raise FileNotFoundError
    csvFilePath = path
    # save the new json file the same name and path of the csv file
    jsonFilePath = path.replace(".csv",".json")

    # Read csv file and add it to data as dictionary
    data = {}
    with open(csvFilePath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for i,rows in enumerate(csvReader):
            id = i
            data[id] = rows

    # create new json file
    with open(jsonFilePath, 'w') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))

except IndexError:
    print("Please enter a file path in the command line")
except FileNotFoundError:
    print("Please enter a correct file path to a .csv file")




