import xml.sax, zipfile, argparse, csv

def main():
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = Meta()
    parser.setContentHandler( Handler )

    opt = argparse.ArgumentParser()
    opt.add_argument("-f", help='the path to the project', required=True)
    zip = zipfile.ZipFile(opt.parse_args().f, 'r')

    for file in zip.filelist:
        if file.filename.endswith(".bky"):
            Handler.setScreen(file.filename.split('/')[4])
            parser.parse(zip.open(file))

    with open('./results.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(Handler.elements)
    print("Done! You can find files in the results.csv file")

class Meta( xml.sax.ContentHandler):

    stack = []
    elements = []
    name = ""
    depth = 0
    eIndex = 0

    def startElement(self, type, attrs):
        a = [self.eIndex, self.name, type, self.depth]
        for name in attrs.getNames():
            a += [name, attrs.getValue(name)]
        self.stack.append(a)
        self.depth+=1
        self.eIndex+=1
 
    def endElement(self, type):
        t = self.stack.pop()
        self.elements.append(t)
        self.depth-=1

    def setScreen(self, name):
        self.name = name

if (__name__ == "__main__"):
    main()
