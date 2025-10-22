import re
import urllib.request
websites=["https://www.jntuh.ac.in/"] 
email_pattern=r"[a-zA-Z0-9+.%_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" 
phone_pattern=r"\b[6-9][0-9]{9}\b" 
for i in websites:
    try:
        print("fetch data from",i)
        print("-"*60) 

        response=urllib.request.urlopen(i)
        html=response.read().decode("utf-8")

        emails=set(re.findall(email_pattern,html))
        phones=set(re.findall(phone_pattern,html)) 

        print("emails found",len(emails))
        
        if emails:
            for email in emails:
                print(" -",email)
        else:
            print("no email found")
        print("phone numbers found",len(phones))
        
        if phones:
            for phone in phones:
                print(" -",phone)
        else:
            print("no phone found")
    except Exception as e:
        print("failed to fetch",i,":",e)