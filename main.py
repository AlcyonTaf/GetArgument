# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import os
import xml.etree.cElementTree as ET



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print('test')
    #print(sys.argv)
    filepath = sys.argv[1]

    dir = os.path.dirname(filepath)

    root = ET.Element("Output")
    ET.SubElement(root, "Status").text = "OK"
    ET.SubElement(root, "OutputFilePath").text = filepath

    tree = ET.ElementTree(root)
    ET.indent(tree, space="\t", level=0)
    tree.write(dir+"\main.xml", encoding="utf-8", xml_declaration=True)



