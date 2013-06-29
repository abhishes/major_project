from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
import xml.etree.ElementTree as xml
import question_XML_read
import questionXML_query
import answerXML_query
import receive_SMS
import write_answer_XML
from django.core.context_processors import request

def index(request):
    #t = get_template("template1.html")
    #html = t.render(Context({'aalu_mula': 'khoi aalu ho ki mula ho :P'}))
    return render(request, 'template1.html', {'aalu_mula': "heheheheheheheheheheeheh"})

def hello(request):
    return HttpResponse("Hello world")

def process_xml(request):
   process123 = question_XML_read.XML() 
   attributes_list = process123.get_attributes("E:/aptana workspace/test_server/XML_files/Question_XML.xml")
   
   att_send = questionXML_query.questionXML()
   att_send.clear_question_table()
   att_send.insert_attributes(attributes_list)
   
   fill_answer = answerXML_query.answerXML()
   fill_answer.clear_answer_table()
   fill_answer.fill_attributes(attributes_list)
   
   return render(request, 'template1.html', {'qncode_list': attributes_list})
def process_SMS(request):
    SMS1 = receive_SMS.SMS()
    received_SMS_member_list = SMS1.return_SMS()
    
    get_id_list = answerXML_query.answerXML()
    id_list = get_id_list.get_id()
    fill_answer = answerXML_query.answerXML()
    fill_answer.fill_data(received_SMS_member_list,id_list)
    
    return render(request, 'template2.html', {'SMS': received_SMS_member_list})

def write_XML(request):
    get_data_list = answerXML_query.answerXML()
    data_list = get_data_list.get_all_data()
    
    write1 = write_answer_XML.XML()
    write1.write_XML(data_list)
    return render(request, 'template3.html', {'message': "done"})
        
