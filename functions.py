import os
import codecs

def loadFile(fileName, ignoreHeaderRow):

    #read file
    file = open(fileName, "r", encoding="utf8")

    if ignoreHeaderRow:
        file.readline()

    #iterate lines
    items = []
    for i, line in enumerate(file):
        if i>0:
            if line:
                #convert line to array of elements
                item = []
                values = line.replace("\n", "").split("\t")
                for value in values:
                    item.append(value.strip())

                items.append(item)
    
    return items

def saveFile(fileName, items):

    #remove file if exists
    if os.path.exists(fileName):
        os.remove(fileName)

    #wirte output file
    f = codecs.open(fileName, "a", "utf-8")
    for item in items:
        f.write('\t'.join(map(str, item))+"\n")
    f.close()

    return True

def getHeaderRow(fileName):
    file = open(fileName, "r", encoding="utf8")
    return file.readline().replace("\n", "").split("\t")