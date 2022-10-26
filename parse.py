from typing import Type
import zipfile
import glob, os
import pprint
import xml.etree.ElementTree as ET


try:
    with zipfile.ZipFile("jobs.zip", mode="r") as archive:
        for folder in archive.namelist():
                archive.extract(folder, path="output_dir/")     
except zipfile.BadZipFile as error:
    print(error)


tags = {}

def parse_xml(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()

    for child in list(root.iter()):
        try:
            if child.tag in tags:
                tags[child.tag] += 1 
            else:
                tags[child.tag] = 1
        except SyntaxError as e:
            print(filename, e)

        except TypeError as e:
            print(filename, e)

    
    pprint.pprint(tags)

for filename in glob.iglob('output_dir/jobs/**', recursive=True):
    if os.path.isfile(filename) and filename.endswith('.xml'): # filter dirs
        parse_xml(filename)



