import smtplib

def sendMessageEmail(to, content):
    '''send a mesage by email'''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()  # TLS = Transpoort Layer security
    #f = open('Emailpass.txt', 'r')
    f = open('E:\\Project\\Assistant - Copy\\Emailpass.txt', 'r')
    str = f.readline()
    f.seek(0)
    f.close()
    server.login('18it122@charusat.edu.in', str)
    server.sendmail('18it122@charusat.edu.in', to, content)
    server.quit()

if __name__ == '__main__':
    sendMessageEmail()