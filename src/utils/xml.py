# https://stackoverflow.com/questions/2148119/how-to-convert-an-xml-string-to-a-dictionary
from typing import Any
from xml.etree import cElementTree as ET


class XmlListConfig(list):
    def __init__(self, aList):
        for element in aList:
            if element:
                # treat like dict
                if len(element) == 1 or element[0].tag != element[1].tag:
                    self.append(XmlDictConfig(element))
                # treat like list
                elif element[0].tag == element[1].tag:
                    self.append(XmlListConfig(element))
            elif element.text:
                text = element.text.strip()
                if text:
                    self.append(text)


class XmlDictConfig(dict):
    '''
    Example usage:

    >>> tree = ElementTree.parse('your_file.xml')
    >>> root = tree.getroot()
    >>> xmldict = XmlDictConfig(root)

    Or, if you want to use an XML string:

    >>> root = ElementTree.XML(xml_string)
    >>> xmldict = XmlDictConfig(root)

    And then use xmldict for what it is... a dict.
    '''
    def __init__(self, parent_element):
        if parent_element.items():
            self.update(dict(parent_element.items()))
        for element in parent_element:
            if element:
                # treat like dict - we assume that if the first two tags
                # in a series are different, then they are all different.
                if len(element) == 1 or element[0].tag != element[1].tag:
                    aDict = XmlDictConfig(element)
                # treat like list - we assume that if the first two tags
                # in a series are the same, then the rest are the same.
                else:
                    # here, we put the list in dictionary; the key is the
                    # tag name the list elements all share in common, and
                    # the value is the list itself 
                    aDict = {element[0].tag: XmlListConfig(element)}
                # if the tag has attributes, add those to the dict
                if element.items():
                    aDict.update(dict(element.items()))
                self.update({element.tag: aDict})
            # this assumes that if you've got an attribute in a tag,
            # you won't be having any text. This may or may not be a 
            # good idea -- time will tell. It works for the way we are
            # currently doing XML configuration files...
            elif element.items():
                self.update({element.tag: dict(element.items())})
            # finally, if there are no child tags and no attributes, extract
            # the text
            else:
                self.update({element.tag: element.text})
                
                

def xml_to_dict(xml_string: str):
    """Converts an XML string into a python dict"""
    root = ET.XML(xml_string)
    xml_dict = XmlDictConfig(root)
    return xml_dict


def dict_to_xml(dictionary: dict[str, Any], root_tag: str = 'root'):
    """
    Converts a dictionary to XML using the lxml module.

    Args:
    dictionary (dict): The dictionary to convert to XML.
    root_tag (str): The root tag of the XML document. Default is 'root'.

    Returns:
    etree: The XML document as an lxml etree object.
    """
    root = ET.Element(root_tag)
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        if isinstance(value, dict):
            child.text = '\n' + dict_to_xml(value, key).decode() + '  '
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    child.append(dict_to_xml(item))
                else:
                    subchild = ET.SubElement(child, key)
                    subchild.text = str(item)
        else:
            child.text = str(value)
    return ET.tostring(root, encoding='unicode')