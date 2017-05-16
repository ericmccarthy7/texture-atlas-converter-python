import xml.etree.ElementTree
import sys, getopt, json

def convertXMLToJSONHash(xml):
    localJson = {
        "frames":{},
        "meta":{}
    }
    counter = 0
    for child in xml:
        counter += 1
        localJson["frames"][child.get('name')] = {}
        localJson["frames"][child.get('name')]["frame"] = {
            "x": child.get('x'),
            "y": child.get('y'),
            "w": child.get('width'),
            "h": child.get('height')
        }
        localJson["frames"][child.get('name')]["spriteSourceSize"] = {
            "x": 0,
            "y": 0,
            "w": child.get('width'),
            "h": child.get('height')
        }
        localJson["frames"][child.get('name')]["sourceSize"] = {
            "w": child.get('width'),
            "h": child.get('height')
        }
        localJson["frames"][child.get('name')]["rotated"] = False
        localJson["frames"][child.get('name')]["trimmed"] = False
        localJson["frames"][child.get('name')]["sourceSize"] = {
            "w": child.get('width'),
            "h": child.get('height')
        }
    localJson["meta"]["sprites"] = counter
    localJson["meta"]["image"] = xml.get('imagePath')
    localJson["meta"]["app"] = "TextureAtlasConverterPython"
    localJson["meta"]["version"] = 0.1
    return localJson
    

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    if inputfile != '':
        e = xml.etree.ElementTree.parse(inputfile).getroot()
        output = convertXMLToJSONHash(e)
        if outputfile == '':
            outputfile = 'out.json'
        with open(outputfile, 'w') as outfile:
            json.dump(output, outfile)

if __name__ == "__main__":
    main(sys.argv[1:])
