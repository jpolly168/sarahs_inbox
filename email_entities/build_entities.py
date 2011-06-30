# Create your views here.
from dcentity.models import *
from oxtail.matching import *
from mail.models import *
from email_entities.models import *
try:
    import json
except:
    import simplejson as json
from django.template.defaultfilters import slugify

def build_industries(entity):
    industry = None

    if entity.entity_type == u'organization':
        industry = Entity.objects.filter( industry_entity__entity__organization_metadata__entity__id=entity.entity)
    elif entity.entity_type == u'individual':
        industry = Entity.objects.raw("select id, name from matchbox_entity where matchbox_entity.id in (select distinct industry_entity_id from matchbox_indivorgaffiliations indiv inner join matchbox_organizationmetadata org on indiv.organization_entity_id = org.entity_id where indiv.individual_entity_id = %s)", [entity.entity])

    if industry is not None:
        for i in industry:
            EmailEntityIndustry.objects.create(
                industry    = i.name, 
                entity      = entity,
                email       = entity.mail,
                thread      = entity.mail.email_thread,
                slug        = slugify(i.name)
            )

def build_table():
    #this only needs to run once
    emails_to_search = Email.objects.only('to','cc','text','id')
    
    for email in emails_to_search:
        print "doing "+email.subject
        meta = str(email.to.all())+str(email.cc.all())
        m = match(meta+email.text)
        for key, value in m.items():
            try:
                e = Entity.objects.get(pk = key)
            except:
                continue
            
            #since match() returns a list of references, store it as a JSON-formatted string
            r = json.dumps(map(unicode, value))
        
            party = ""

            if e.type == u'politician':
                party = PoliticianMetadataLatest.objects.get(entity = e).party
            
            ee = EmailEntity.objects.create(
                mail            = email,
                entity          = e.id,
                entity_name     = e.name,
                entity_type     = e.type,
                references      = r,
                party           = party
            )
            
            build_industries(ee)
    
    print('\a')*3
    print 'all done'