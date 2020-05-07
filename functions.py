import os
import codecs
import xml.etree.ElementTree as ET

def loadFile(fileName, ignoreHeaderRow):
    '''
    '''

    #read file
    file = open(fileName, "r", encoding="utf8")

    #iterate lines
    items = []
    for i, line in enumerate(file):
        if (ignoreHeaderRow and i>0) or (not ignoreHeaderRow):
            if line:
                #convert line to array of elements
                item = []
                values = line.replace("\n", "").split("\t")
                for value in values:
                    item.append(value.strip())

                items.append(item)
    
    return items


def saveFile(fileName, items):
    '''
    '''

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
    '''
    '''

    file = open(fileName, "r", encoding="utf8")
    return file.readline().replace("\n", "").split("\t")


def xmlParseName(root, locale):
    '''
    '''
    
    value = ''

    if root:
        #check if exist locale
        locales = root.get('available-locales')
        if not locale in locales:
            locale = root.get("default-locale") #otherwise, get default local
        
        nodes = root.findall(".//Name/[@language-id='" + locale +"']")
        if nodes and len(nodes)>=1:
            value = nodes[0].text #first node
        
    return value    