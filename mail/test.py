from mail.models import *
import timeit

def buh_test():
    palin = Person.objects.sarah_palin()
    emails = Email.objects.select_related().exclude(email_thread__creator__in=palin).filter(email_thread__isnull=False).order_by('-email_thread__date')
    len(emails) #force evaluate to avoid like a million queries
    return emails

#stole this from http://www.peterbe.com/plog/uniqifiers-benchmark

def f1(emails = buh_test()):
    seen = set()
    threads = [x.email_thread for x in emails if x.email_thread.id not in seen and not seen.add(x.email_thread.id)]
    return threads
    
def f2(emails = buh_test()):
    seen = 0
    a = []
    for x in emails:
        if x.email_thread.id == seen:
            continue
        else:
            seen = x.email_thread.id

def doTheShit():
    t = timeit.Timer("f2()", "from mail.test import f2")
    return t.timeit()