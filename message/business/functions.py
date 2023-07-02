from django.conf import settings
from .models import *
from django.contrib.auth.models import User

import requests

def sendWhatsAppMessage(phoneNumber, message):
    headers = {"Authorization": settings.WHATSAPP_TOKEN}
    payload = {"messaging_product": "whatsapp",
               "recipient_type": "individual",
               "to": phoneNumber,
               "type":"text",
               "text":{"body":message}
               }
    
    response = requests.post(settings.WHATSAPP_URL,headers=headers,json=payload)
    ans = response.json()
    return ans

#phoneNumber = "+23057545423"
#message = "Hello there"
#ans = sendwhatsAppMessage(phoneNumber, message)
#ans

def handleWhatsAppChat(fromId,profileName, phoneId, text):
    ##check if there is a chat session

    try:
        chat = ChatSession.objects.get(profile__phoneNumber=fromId)

    except:
        
        if User.objects.filter(username=phoneId).exists():
            user = User.objects.get(username=phoneId)
            user_profile = user.profile
        else:
            ##Create a User
            user = User.objects.create_user(
            username =phoneId,
            email= 'tester1@skhokho.tech',
            password='password',
            first_name=profileName,
            )    

            ##creating a profile
            user_profile = Profile.objects.create(
                user=user,
                phoneNumber = fromId,
                phoneId = phoneId
            )

        
    
        ##Create a chat session
        chat = ChatSession.objects.create(profile=user_profile)
        ##send a message
        message = "Welcome to the AI Business Plan creater \n I am going to take you through the process of creating your business plan, right here on whatsApp. To get started, enter your Business Name:"
        sendWhatsAppMessage(fromId, message)
    
    ##When you return
    ####Continue with function
    if chat.business_name:
        if chat.business_type:
            if chat.country:
                if chat.product_service:
                    if chat.short_description:
                        if chat.years:
                            if chat.progress:
                                # Do something
                                message("Our AI is working on it. Give us a moment, we will message you when your business plan is ready")
                                sendWhatsAppMessage(fromId,message)

                            else:
                                chat.progress = text
                                chat.save()

                                message = "Great we have everything we need to build your Business Plan"
                                sendWhatsAppMessage(fromId,message)

                    #continue
                        else:
                            try:
                                years = int(text.replace(' ',''))
                                chat.years = years
                                chat.save()

                                message = "How much traction have you made in your business?"
                                sendWhatsAppMessage(fromId,message)

                            except:
                                message = "Please try again, enter only a number like 1 or 2"
                                sendWhatsAppMessage(fromId,message)

                    else:
                        chat.product_service = text
                        chat.save()

                        message = "How many years have you been in business for? Enter a number like 1 or 2."
                        sendWhatsAppMessage(fromId,message)

                else:
                    chat.product_service = text
                    chat.save()

                    message = "Describe your business in one or two sentences."
                    sendWhatsAppMessage(fromId,message)

            else:
                chat.country = text
                chat.save()

                message = "What product or service will your business be providing?"
                sendWhatsAppMessage(fromId,message)
        else:
            #Test for the number
            try:
                type = int(text.replace(' ', ''))
                if type == 1:
                    chat.business_type = '(Pty) Ltd'
                    chat.save()

                    message = "Which country are you from?"
                    sendWhatsAppMessage(fromId,message)
                elif type == 2:
                    chat.business_type = 'Not Profit'
                    chat.save()

                    message = "Which country are you from?"
                    sendWhatsAppMessage(fromId,message)
                elif type == 3:
                    chat.business_type = 'Partnership'
                    chat.save()

                    message = "Which country are you from?"
                    sendWhatsAppMessage(fromId,message)
                else:
                    message = "Please try again. Enter the number corresponding to the Business Type: \n 1.(Pty) Ltd \n 2.Non Profit \n 3. Partnership \n \n Enter just the number. "
                    sendWhatsAppMessage(fromId,message)
            except:
                message = "Please try again. Enter the number corresponding to the Business Type: \n 1.(Pty) Ltd \n 2.Non Profit \n 3. Partnership \n \n Enter just the number. "
                sendWhatsAppMessage(fromId,message)
    else:
        chat.business_name = text
        chat.save()

        ##Send next message
        message = "Please select the type of business. Enter the number corresponding to the Business Type: \n 1.(Pty) Ltd \n 2.Non Profit \n 3. Partnership \n \n Enter just the number."
        sendWhatsAppMessage(fromId,message)