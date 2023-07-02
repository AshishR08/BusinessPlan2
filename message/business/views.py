from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse

from .functions import *

import json

# Create your views here.

def home(request):
    return render(request,'business/index.html',{})


@csrf_exempt
def whatsAppWebhook(request):
    if request.method == 'GET':
        VERIFY_TOKEN = '1234'
        mode = request.GET['hub.mode']
        token = request.GET['hub.verify_token']
        challenge = request.GET['hub.challenge']

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)
        else:
            return HttpResponse('error',status=404)
        
    if request.method == 'POST':
        data = json.loads(request.body)
        print(request.body)
        if 'object' in data and 'entry' in data:
            if data['object'] == 'whatsapp_business_account':
                    for entry in data['entry']:
                        #phoneNumber = entry['changes'][0]['value']['metadata']['display_phone_number']
                        phoneId = entry['changes'][0]['value']['metadata']['phone_number_id']

                        try:
                            profileName = entry['changes'][0]['value']['contacts'][0]['profile']['name']
                        except:
                            profileName = "Unknown"

                        #whatsAppId = entry['changes'][0]['value']['contacts'][0]['wa_id']
                        fromId = entry['changes'][0]['value']['messages'][0]['from']
                        #messageId = entry['changes'][0]['value']['messages'][0]['id']
                        #timestamp = entry['changes'][0]['value']['messages'][0]['timestamp']
                        text = entry['changes'][0]['value']['messages'][0]['text']['body']

                        handleWhatsAppChat(fromId,profileName,phoneId,text)
            else:
                pass
        else:
            pass

        return HttpResponse('success',status = 200)
    

# try:
#     profileName = entry['changes'][0]['value']['contacts'][0]['profile']['name']
#     # Continue with the rest of your code that uses profileName
# except KeyError:
#     # Handle the case when the 'contacts' key is not present
#     profileName = "Unknown"
#     # Or you can raise an exception or perform any other appropriate action