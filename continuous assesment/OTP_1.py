#sending and generating OTP as a program without Funtional Decomposition


import random;
import smtplib;

server =smtplib.SMTP('smtp.gmail.com',587)
# print(server)
server.starttls()
server.login('mendhenandini910@gmail.com',password= "tvsu gwhh hhcx jrdm")
otp=''.join([str(random.randint(0,9))for i in range(4)])
msg='Hello, your otp is '+str(otp)
server.sendmail('mendhenandini910@gmail.com','mendhenandini44@gmail.com',msg)
server.quit()
print(otp)