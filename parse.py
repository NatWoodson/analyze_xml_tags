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
        if child.tag == "canRoam":
            print(xmlfile)
        if child.tag in tags:
            tags[child.tag] += 1 
        else:
            tags[child.tag] = 1


count = 0
for filename in glob.iglob('output_dir/jobs/**', recursive=True):
    if os.path.isfile(filename) and filename.endswith('config.xml'): # filter dirs
        count += 1
    
        parse_xml(filename)




print(f"Total num of config.xml files is: {count}")
# pprint.pprint(tags)
pprint.pprint(sorted(tags.items(), key=lambda item: item[1], reverse=True))

 



