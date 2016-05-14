from django.shortcuts import render_to_response
from django.http import HttpResponse,JsonResponse
import subprocess

# Create your views here.
def HomeView(request):
    dictValues = {}
    addresses = [ 'google.com','sugeek.net','eskxdjfl.com/'] #Change IP Addresses accordingly
    statuses = {} #Active or not
    for ping in addresses:
        address = (ping)
        res = subprocess.call(['ping', '-c', '3', address]) #Ping 3 times
        if res == 0:
            print "ping to", address, "OK"
            statuses[ping] = 'OK'
        elif res == 2:
            print "no response from", address
            statuses[ping] = 'NO RESPONSE'
        else:
            print "ping to", address, "failed!"
            statuses[ping] = 'FAILED'
    dictValues['statuses'] = statuses
    return render_to_response('Home.html',dictValues)

def UpdateView(request):
    dictValues = {}
    addresses = [ 'google.com','sugeek.net','eskxdjfl.com/']
    statuses = {} #Active or not
    for ping in addresses:
        address = (ping)
        res = subprocess.call(['ping', '-c', '3', address]) #Ping 3 times
        if res == 0:
            print "ping to", address, "OK"
            statuses[ping] = 'OK'
        elif res == 2:
            print "no response from", address
            statuses[ping] = 'NO RESPONSE'
        else:
            print "ping to", address, "failed!"
            statuses[ping] = 'FAILED'
    return JsonResponse(statuses)
