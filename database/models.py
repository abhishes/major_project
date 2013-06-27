'''
Created on May 25, 2013

@author: Deja-Vu
'''
from django.db import models

class questionnaire(models.Model):
        type = models.CharField(max_length=10)
        question_number = models.CharField(max_length=20)
        def __unicode__(self):
            return self.question_number
            
        
class answer(models.Model):
        question_number = models.CharField(max_length=20)
        received_answer = models.CharField(max_length=999)
        def __unicode__(self):
            return u'%s %s' % (self.question_number, self.received_answer)