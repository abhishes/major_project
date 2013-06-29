'''
Created on May 29, 2013

@author: Deja-Vu
'''
import xml.etree.ElementTree as xml
from xml import etree
from lxml import etree
import shutil
from pprint import PrettyPrinter

class XML:
    def __init__(self):
        self.tree = ""
        
    def write_XML(self, data_list):
        id_list=[]
        question_number_list=[]
        received_answer_list=[]
        
        for item in data_list:
            id_list.append(item.id)
        print "======================="
        print id_list
        print "======================="
            
        for item in data_list:
            question_number_list.append(item.question_number)
        print "======================="
        print question_number_list
        print "======================="
        
        for item in data_list:
            received_answer_list.append(item.received_answer)
        print "======================="
        print received_answer_list
        print "======================="
        
        shutil.copy2("e:/aptana workspace/test_server/XML_files/Answer_XML_skeleton.xml", "e:/aptana workspace/test_server/XML_files/XML%s.xml"%id_list[0])
        
        path = "E:/aptana workspace/test_server/XML_files/XML%s.xml"%id_list[0]
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(path,parser)
        root = tree.getroot()
        for element in root.iter():
            att = element.attrib
            for item in att:
                for item1 in data_list:
                        print "tinta"
                        print item, str(item1.question_number)
                        if item == "id" and item1.question_number == "dataID":
                            element.attrib[item] = item1.received_answer
                        if item == str(item1.question_number):
                            print "charta"
                            if item1.received_answer == "X":
                                continue
                            element.attrib[item] = item1.received_answer 
    
        for element in root:
            root1 = element
            count = 0
            for item in data_list:
                if item.question_number.startswith("QN"):
                    if item.received_answer == "-":
                        continue
                    elem = etree.Element(str(item.question_number))
                    elem.text = str(item.received_answer)
                    root1.insert(count,elem)
                    count=count+1
        
                            
        tree.write(path,pretty_print=True)
                        