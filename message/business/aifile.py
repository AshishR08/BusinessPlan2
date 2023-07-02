import os
import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY


def companyDescriptionProgress(business_name, business_type, country, product_service, short_description, years, progress):
    response = openai.Completion.create(
            model="text-davinci-002",
            prompt= "Generate Company Description section for a Business Plan for the following business, using the guideline provided:\nBusiness Name: {}\nBusiness Type: {}\nCountry: {}\nProduct or Service: {}\nShort Business Description: {}\nYears in operation: {}\nBusiness progress to date: {}\n\nGuidelines: Start the company description by listing the business name and company structure, if one is provided. Write a detailed business description fofr the short description provided, in a professional business tone. Describe the industry the business will be operating in and re-write the business progress to date. Finally, provide a numbered list of three suitable business objectives for this business and for each objective, describe how the obective fits the business and how it will benefite the stakeholders in the long run. \n\nCompany Description\n{}".format(business_name, business_type, country, product_service, short_description, years, progress, business_name),
            temperature=0.7,
            max_tokens=2000,
            top_p=1,
            best_of=2,
            frequency_penalty=0,
            presence_penalty=0
            )
    
    if 'choices' in response:
        if len(response['choices'])>0:
            answer = response['choices'][0]['text']
            #answer = response['choices'][0]['text'].replace('\n','<br/>')

            return business_name + answer
        else:
            return ''
    else:
        return ''
    



def companyDescription(business_name, business_type, country, product_service, short_description, years):
    response = openai.Completion.create(
            model="text-davinci-002",
            prompt= "Generate Company Description section for a Business Plan for the following business, using the guideline provided:\nBusiness Name: {}\nBusiness Type: {}\nCountry: {}\nProduct or Service: {}\nShort Business Description: {}\nYears in operation: {}\n\nGuidelines: Start the company description by listing the business name and company structure, if one is provided. Write a detailed business description fofr the short description provided, in a professional business tone. Describe the industry the business will be operating in and re-write the business progress to date. Finally, provide a numbered list of three suitable business objectives for this business and for each objective, describe how the obective fits the business and how it will benefite the stakeholders in the long run. \n\nCompany Description\n{}".format(business_name, business_type, country, product_service, short_description, years, business_name),
            temperature=0.7,
            max_tokens=2000,
            top_p=1,
            best_of=2,
            frequency_penalty=0,
            presence_penalty=0
            )
    
    if 'choices' in response:
        if len(response['choices'])>0:
            answer = response['choices'][0]['text'].replace('\n','<br/>')
            return business_name + answer
        else:
            return ''
    else:
        return ''