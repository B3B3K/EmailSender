import smtplib
print("username giriniz")
print("örnek: osmancelikpasa1@gmail.com")
user = input("-> :") 
print("şifrenizi giriniz ")
print("örnek: abc123")
passw = input("-> :")
kim = input("göndermek istediğin mail adresi :")
bas = input("başlık giriniz :")
txt = input("içeriğinizi giriniz :")
ism = input("isminiz ve soyisminiz ( eposta başlığında gözükecektir ) :")
TO = kim
SUBJECT = bas
TEXT = txt
send_from = ism
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(user, passw)
BODY = '\r\n'.join(['To: %s' % TO,
        'From: %s' % ism,
        'Subject: %s' % SUBJECT,
        '', TEXT])

server.sendmail(user, [TO], BODY)
print ('e posta gönderildi')