import smtplib
import connector
import random
def smtp(uid):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("group1@apsjorhat.org", "apsj#12345678")
    otp=random.randint(100000,999999)
    otp=str(otp)
    message = "Hello your login code is "+otp
    s.sendmail("group1@apsjorhat.org", uid, message)
    s.quit()


def auth_user(uid):
    count=0
    query = "select * from reg_users;"
    connector.cursor.execute(query)
    for i in connector.cursor:
        if i[0]==uid:
            smtp(uid)
            count=1
            print("MAIL HAS BEEN SENT")
    if count==0:
        print("USER ID NOT FOUND")