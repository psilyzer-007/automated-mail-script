import pandas as pd
import smtplib
import time
from email.message import EmailMessage
from email.mime.text import MIMEText

# change here
email = "yourname@domainaddress.com"
pwd = "yourpasswordhere"

#change column names and file name according to your data

data = pd.read_csv("Mailing.csv") #replace file name
rows = data.shape[0]
names = data['Name']#["Sai",  "Sreyas"]
mails = data['Email']#["s.sai@iitg.ac.in"]
file_name = data['File_Name']
str =  ['0', '0','0']



    



for i in range(0, rows):
    msg = EmailMessage()
    msg['Subject'] = 'Problem Statement | ProduScope'
    msg['From'] = email
    msg['To'] = mails[i]
    
    body = """
Hello {},<br><br>

Please find attached your certificate.<br><br>

Best wishes,<br>
Yourname""".format(names[i],names[i])

    msg.add_alternative(body, subtype='html')
    #string addition
    carry = 1
    for it in range(3):
        tmp = str
        digit = (ord(tmp[2-it]))
        if(digit == 57):
            carry = 1
            str[2-it] = '0'     
        else:
            str[2-it] = chr(digit+carry)
            carry = 0

FileName = ""
    for ch in str:
        FileName += ch
    FileName += ".pdf"
    #files = [file_name[i]]
    files = [FileName]
    
    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=names[i]+".pdf")
        
        

    #outlook may be replaced by gmail/zoho/anything else according to your mail id
    with smtplib.SMTP('smtp.outlook.com', 587) as smtp:
        smtp.starttls()
        smtp.login(email, pwd)
        smtp.send_message(msg)
        smtp.quit()
        

    """with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email, pwd)
        smtp.send_message(msg)"""

    print("Sent to no. {} name {}".format(i,names[i]))

###### Note #####
# the code may stop after sending some particular number of mails there could be two reason - 
# 1. login timeout - run the code again after changing the range of for loop appropriately 
# 2. mail limit exceeded (depends on your mail provider) - ooooops!!! lets call it a day you cant send more mails today not even directly from the app/site


#Made By Sai Sreyas Ray
