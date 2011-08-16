# Create your views here.
#from dcentity.models import *
#from oxtail.matching import *
from mail.models import *
from email_entities.models import *
from django.db.models import Q
from django.template.defaultfilters import slugify
import httplib2
import json
import urllib
import settings

h = httplib2.Http()

def _match(text):
    text = urllib.quote(text)
    req_url = 'https://inbox.influenceexplorer.com/contextualize?text="%s"&apikey=%s'%(text, settings.APIKEY)
    r, c = h.request(req_url)
    if r.get('status') == '200':
        return json.loads(c)
    else:
        print r.get('status')
        print req_url

def _entity(id):
    req_url = 'http://transparencydata.com/api/1.0/entities/%s.json?apikey=%s'%(id, settings.APIKEY)
    r, c = h.request(req_url)
    if r.get('status') == '200':
        return json.loads(c)
    else:
        print r.get('status')
        print req_url

def build_industries(entity): #adding an arbitrary comment to trigger file change
    industry = []

    if entity.entity_type == u'organization':
        try:
            industry_id = _entity(entity.entity).get('metadata').get('industry_entity')
            industry.append(_entity(industry_id))
        except:
            pass
    elif entity.entity_type == u'individual':
        org_ids = []
        try:
            orgs = _entity(entity.entity).get('metadata').get('affiliated_organizations')
            for org in orgs:
                industry.append(_entity(org.get("id")))
        except:
            pass
    elif entity.entity_type == u'politician':
        try:
            industry = _entity(entity.entity).get('metadata').get('party')
        except:
            pass

    if industry is not [] and industry != "UNKNOWN":
        for i in industry:
            try:
                str = i.get('name')
            except:
                str = i
            EmailEntityIndustry.objects.create(
                industry    = str, 
                entity      = entity,
                email       = entity.mail,
                thread      = entity.mail.email_thread,
                slug        = slugify(str)
            )

def build_table():
    #this only needs to run once
    emails_to_search = Email.objects.only('to','cc','text','id')
    for email in emails_to_search:
        print "doing "+email.subject
        entity_matches = _match(email.text)
        for entity in entity_matches.get('entities'):
            
            e = entity.get('entity_data')      
            r = json.dumps(map(unicode, entity.get('matched_text')))
        
            ee = EmailEntity.objects.create(
                mail            = email,
                entity          = e.get('id'),
                entity_name     = e.get('name'),
                entity_type     = e.get('type'),
                references      = r,
            )
            build_industries(ee)
    
    print('\a')*3
    print 'all done'