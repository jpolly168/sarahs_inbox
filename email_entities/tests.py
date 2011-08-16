"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from email_entities.models import *
from mail.models import *
from email_entities import build_entities as b
import httplib2
import urllib
import json
import datetime

class TestEntityMatch(TestCase):
    def setUp(self):
        self.baz = Thread.objects.create(
            name = "Test thread",
            date = datetime.datetime.now()
        )
        self.foo = Email.objects.create(
            text            = 'Sarah Palin Exxon Gap John McCain',
            source_id       = 12345,
            email_thread    = self.baz,
            subject         =  "yo dawg I herd u liek pancakes"
        )
        self.bar = Email.objects.create(
            text            = 'Rick Perry Comcast Rupert Murdoch',
            source_id       = 12345,
            email_thread    = self.baz,
            subject         =  "yo dawg I herd u liek earwigs"
        )
        
    def test_inbox_api(self):
        h = httplib2.Http()
        request = urllib.urlencode({'text':self.foo.text, 'apikey':'sunlight9'})
        r, c = h.request('https://inbox.influenceexplorer.com/contextualize?'+request, body = request)
        context = json.loads(c)
        e = [entity.get("matched_text", False) for entity in context.get('entities', False)]
        self.assertEqual('200', r.get('status', False))
        self.assertIn(['Sarah Palin'], e)
    
    def test_build_table(self):
        b.build_table()
        e = EmailEntity.objects.all()
        palin = EmailEntity.objects.filter(entity_name__icontains="palin")[0]
        comcast = EmailEntity.objects.filter(entity_name__icontains="comcast")[0]
        #murdoch = EmailEntity.objects.filter(entity_name__icontains="murdoch")[0]
        ind = EmailEntityIndustry.objects.filter(thread=self.baz)
        self.assertNotEqual(e, [])
        self.assertNotEqual(ind, [])
        self.assertEquals(palin.entity_type, 'politician')
        self.assertEquals(comcast.entity_type, 'organization')