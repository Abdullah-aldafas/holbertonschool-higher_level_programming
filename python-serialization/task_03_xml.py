#!/usr/bin/env python3


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value) if value is not None else ""
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    result: Dict[str, str] = {}
    for child in root:
        result[child.tag] = "" if child.text is None else child.text
    return result
