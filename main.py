import argparse
from functions import loadFile, saveFile, getHeaderRow

#ARGUMENTS
#example: py main.py --inputfile c:/tmp/pages_sorted.csv --column 3 --ignoreheaderrow
parser = argparse.ArgumentParser(description='Given a CSV file with parent-child relationship column, this task sort the rows. Optional it creates a new column with tree format.')
parser.add_argument('--inputfile', dest='input_file', 
    help='Input file name.', type=str, required=True)
parser.add_argument('--outputfile', dest='output_file', 
    help='Output file name.', type=str, required=False, default='')
parser.add_argument('--column', dest='column', 
    help='Column number (default value 0: first column).', type=int, required=True, default=0)
parser.add_argument('--ignoreheaderrow', 
    help='Ignore first row (header).', action="store_true")

args = parser.parse_args()
inputFile = args.input_file
outputFile = args.output_file
columnNumber = args.column
ignoreHeaderRow = args.ignoreheaderrow

if not outputFile:
    outputFile = inputFile.replace(".csv", "_parse.csv")

#EXECUTE
items = loadFile(inputFile, ignoreHeaderRow)

if ignoreHeaderRow:
    #It means that exists first row as Header. Concatenate it.
    header = getHeaderRow(inputFile)
    items = [header] + items

saveFile(outputFile, items)

print("Done.")