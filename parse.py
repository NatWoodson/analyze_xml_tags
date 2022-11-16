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

# optional parameter is tag to be searched for to view it within context of xml doc
def main(searched_tag=None):
    for filename in glob.iglob('output_dir/jobs/**', recursive=True):
        if os.path.isfile(filename) and filename.endswith('config.xml'): # filter dirs
    
            parse_xml(filename, searched_tag)

    pprint.pprint(sorted(tags.items(), key=lambda item: item[1], reverse=True))

tags = {}

def parse_xml(xmlfile, searched_tag):
    tree = ET.parse(xmlfile)
    root = tree.getroot()

    # if searched_tag, display files that contain the tag
    if searched_tag:
        for child in list(root.iter()):
            if child.tag == searched_tag:
                print(f'File: {xmlfile}\n')   
                print(ET.tostring(root, encoding='utf8').decode('utf8'))
    else:
        for child in list(root.iter()):
            if child.tag in tags:
                tags[child.tag] += 1 
            else:
                tags[child.tag] = 1
        

if __name__ == "__main__":
    main()

 

