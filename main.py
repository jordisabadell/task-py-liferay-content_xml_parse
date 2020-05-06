import argparse
import xml.etree.ElementTree as ET
from functions import loadFile, saveFile, getHeaderRow, xmlParseName

#ARGUMENTS
parser = argparse.ArgumentParser(description='')
parser.add_argument('--inputfile', dest='input_file', 
    help='Input file name.', type=str, required=True)
parser.add_argument('--outputfile', dest='output_file', 
    help='Output file name.', type=str, required=False, default='')
parser.add_argument('--column', dest='column', 
    help='Column number (default value 0: first column).', type=int, required=False, default=0)
parser.add_argument('--locale', dest='locale', 
    help='Locale key (default value \'ca_ES\': catalan).', type=str, required=False, default='ca_ES')
parser.add_argument('--ignoreheaderrow', 
    help='Ignore first row (header).', action="store_true")

args = parser.parse_args()
inputFile = args.input_file
outputFile = args.output_file
columnNumber = args.column
locale = args.locale
ignoreHeaderRow = args.ignoreheaderrow

if not outputFile:
    outputFile = inputFile.replace(".csv", "_parse.csv")

#EXECUTE
items = loadFile(inputFile, ignoreHeaderRow)

#Iterate items
for item in items:
    root  = ET.fromstring(item[columnNumber]) #load xml like <?xml version='1.0' encoding='UTF-8'?><root available-locales="ca_ES,es_ES,en_GB," default-locale="ca_ES"><Name language-id="ca_ES">Visions</Name><Name language-id="es_ES">Visiones</Name><Name language-id="en_GB">Visions</Name></root>
    value = xmlParseName(root, locale)
    if value:
        item[columnNumber] = value

if ignoreHeaderRow:
    #It means that exists first row as Header. Concatenate it.
    header = getHeaderRow(inputFile)
    items = [header] + items

saveFile(outputFile, items)

print("Done.")