'''
Created on May 25, 2013

@author: Deja-Vu
'''
#!/u    sr/bin/python
# -*- coding: iso-8859-1 -*-
import os, sys
import xml.etree.ElementTree as xml

class XML:
    def __init__(self):
        self.tree = ""

    
    def get_attributes(self,path):
        self.path = path
        tree = xml.parse(path)
        root = tree.getroot()
        group_list = []
        matrix_list = []
        normal_list = []
        final_list = []
        
        for element in root.iter():
            if element.tag.startswith("module"):
                root0=element
                for element in root0.iter():
                    if element.tag.startswith("controls"):
                        root1=element
                        for element in root1.iter():
                            for name, value in element.items():
                                if value.startswith("QN"):
                                    if element.tag.startswith("group"):
                                        group_list.append(value+"group")
                                        root2=element
                                        for element in root2.iter():
                                            if element.tag.startswith("sub"):
                                                root3 = element
                                                for element in root3.iter():
                                                    for name,value in element.items():
                                                        if value.startswith("QN"):
                                                            group_list.append(value+"subgroup")
                                    elif element.tag.startswith("matrix"):
                                        matrix_list.append(value+"matrix")
                                        root2=element
                                        for element in root2.iter():
                                            if element.tag.startswith("matrixrow"):
                                                root3 = element
                                                for element in root3.iter():
                                                    for name,value in element.items():
                                                        if value.startswith("QN"):
                                                            matrix_list.append(value+"matrixrow")                        
                                    else:
                                        if len(value) > 9:
                                            continue
                                        else:
                                            normal_list.append(value)
        
        if (normal_list[0]<group_list[0] and normal_list[0]<matrix_list[0]):
            normal_list.reverse()
            final_list = normal_list
            if (group_list[0]<matrix_list[0]):
                final_list.append(group_list.pop(0))
                group_list.reverse()
                final_list = final_list + group_list+matrix_list
            elif (matrix_list[0]<group_list[0]):
                final_list = final_list + matrix_list
                final_list.append(group_list.pop(0))
                group_list.reverse()
                final_list = final_list + group_list
        elif (normal_list[0]>group_list[0] and normal_list[0]>matrix_list[0]):
            if (group_list[0]<matrix_list[0]):
                final_list.append(group_list.pop(0))
                group_list.reverse()
                final_list = final_list + group_list+matrix_list
            elif (matrix_list[0]<group_list[0]):
                final_list = final_list + matrix_list
                final_list.append(group_list.pop(0))
                group_list.reverse()
                final_list = final_list + group_list
            normal_list.reverse()
            final_list = final_list + normal_list
        elif (normal_list[0]<group_list[0] and normal_list[0]>matrix_list[0]):
            final_list = final_list + matrix_list
            normal_list.reverse()
            final_list = final_list + normal_list
            final_list.append(group_list.pop(0))
            group_list.reverse()
            final_list = final_list+ group_list
        elif (normal_list[0]>group_list[0] and normal_list[0]<matrix_list[0]):
            final_list.append(group_list.pop(0))
            group_list.reverse()
            final_list = final_list+ group_list
            normal_list.reverse()
            final_list = final_list + normal_list
            final_list = final_list + matrix_list
        
        return final_list
#tree = xml.parse("E:/hawa Backup/python test code/Question_XML.xml")
#root = tree.getroot()

#list = []
#for element in root.iter():
#    for name,value in (element.items()):
#        check = value.startswith("QN")
#        if value.startswith("QN"):
#            print ("%s = %r" % (name,value))
#            list.append(value)
#print list[0]
