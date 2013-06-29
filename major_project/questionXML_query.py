'''
Created on May 27, 2013

@author: Deja-Vu
'''

from database.models import questionnaire

class questionXML:
    def clear_question_table(self):
        questionnaire.objects.all().delete()
        
    def insert_attributes(self,attributes_list):
        for item in attributes_list:
            if 'group' in item :
                if 'subgroup' in item:
                    q1 = questionnaire(type="subgroup",question_number=item.rstrip('subgroup'))
                else:
                    q1 = questionnaire(type="group",question_number=item.rstrip('group'))
            elif 'matrix' in item:
                if 'matrixrow' in item:
                    q1 = questionnaire(type="matrixrow",question_number=item.rstrip('matrixrow'))
                else:
                    q1 = questionnaire(type="matrix",question_number=item.rstrip('matrix'))
            else:
                q1 = questionnaire(type="xx",question_number=item)
            q1.save()
    
                
        