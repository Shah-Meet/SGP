import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def emailAttach():
    '''Attach a file with email than send'''

    user = '18it122@charusat.edu.in'

    f = open('E:\\Project\\Assistant - Copy\\Emailpass.txt','r')
    passwd = f.readline()
    f.seek(0)
    f.close()
    reciver  = '18it122@charusat.edu.in'

    subject = 'sending a attachment'

    msg = MIMEMultipart()
    # part the msg into diffrent elemnt like To ,Subject ,From
    msg['From'] = '18it122@charusat.edu.in'
    msg['To']  = '18it122@charusat.edu.in'
    msg['Subject'] = 'sending an attachment using python'

    body = 'attachment is here....!! '
    msg.attach(MIMEText(body,'plain'))#attach a body part in msg

    fileName = 'Textdoc.txt'
    attachFile = open('Textdoc.txt','rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachFile).read())
    encoders.encode_base64(part)# Encode data using base64
    part.add_header('Content-Disposition',"attachment; filename= "+fileName)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('18it122@charusat.edu.in' ,passwd)

    server.sendmail('18it122@charusat.edu.in','18it122@charusat.edu.in',text)
    server.quit()

if __name__ == "__main__":
    emailAttach()
