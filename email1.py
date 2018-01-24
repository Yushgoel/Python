import smtplib

sender = 'ayushgoel2004@gmail.com'
receivers = ['goel.monica1@gmail.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <goel.monica1@gmail.com>
Subject: Python email number 1

This is awesome.
"""


smtpObj = smtplib.SMTP('localhost')
smtpObj.sendmail(sender, receivers, message)
print "Successfully sent email"
print "Error: unable to send email"
