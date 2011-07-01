from django.db import connection
from mail.models import *

def migrate_recipient_html():
    #couldn't get this to run through django, do it manually
    #cursor = connection.cursor()
    #cursor.execute('alter table mail_thread add column "all_recipient_html" text',[])
    #transaction.commit_unless_managed()
    t = Thread.objects.all()
    for thread in t:
        thread.save()
    
    print("\a"*3)