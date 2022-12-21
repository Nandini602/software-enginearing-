# Sending nd generating OTP assingnment with funtional decomposition after code review

import math
import random 
import Sender_data
import smtplib  #simple massage transfer protocol library to send email to user 
 

#function to generate otp 
def generateOTP(n): 
    OTP =""     

    for i in range(0,n):
        OTP+= str(random.randint(0,9))#otp will take any random digitd from(0,9)
    return (OTP) 



#get senders email from another file
Email_id = Sender_data.email
password = Sender_data.password 




#function to send email
def send_email(r_name,r_email,otp):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls() #transfered layer security
    server.login('mendhenandini910@gmail.com',password= "tvsu gwhh hhcx jrdm")
    
    msg =("HI"+ r_name+"\n" + str(otp)+"is your otp")
    print(msg)
    server.sendmail(Email_id,r_email,msg)
    server.quit() #to quit the server 
    print("opt is verified") 

if __name__=='__main__':
#function calling 
    r_name = input("Enter the receiver name")
    r_email = input("Enter the receivers email") 

    n = (int(input("enter the range of otp "))) #taking the input for length of opt 
    
    otp = generateOTP(n)
    
    send_email(r_name,r_email,otp)
 