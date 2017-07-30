# import smtplib
# from email.mime.text import MIMEText

# SMTP_host = 'smtp.gmail.com'
# SMTP_email = 'zlsLandMeter@gmail.com'
# SMTP_pass = 'zlsBBB2017'


# def send_email(to, subject, body):
# 	msg = MIMEText(body)
# 	msg['Subject'] = subject
# 	msg['From'] = SMTP_email
# 	msg['To'] = to
# 	server = smtplib.SMTP_SSL(SMTP_host)
# 	#print(msg.as_string())
# 	server.login(SMTP_email,SMTP_pass)
# 	server.send_email(SMTP_email, to, msg.as_string())
	
# subject = 'test'
# to = 'mba_jack@hotmail.com'
# body = 'This is a test email from BBB 1'

# send_email(to, subject, body)



import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
fromaddr = "zlsLandMeter@gmail.com"
toaddr = "james.zlscorp@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test email from ZLS Beaglebone Black"
 
body = "This is a test of the ZLS Beaglebone Black Wireless warning system. This is only a test.  If this were a real warning it would include date, time and system information as well as what caused the alarm condition."
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "zlsBBB2017")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
