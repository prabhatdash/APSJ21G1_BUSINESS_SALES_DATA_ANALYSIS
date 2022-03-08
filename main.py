
import GitHub.auth as auth
import GitHub.otp_sender as otp
import GitHub.dashboard as dash
print("ENTER USER ID")
email=str(str.lower((input())))
if auth.auth_user(email)==1:
    rcv_otp=otp.otp_sender(email)
    print("AN OTP HAS BEEN SENT TO THE REG. MAIL ID. PLEASE ENTER THE OTP TO LOGIN !")
    inp_otp=input()
    if rcv_otp == inp_otp:
        print("VALIDATION SUCCESSFUL")
        dash.dashboard()
    else:
        print("INVALID OTP")
        exit()
else:
    print("USER NOT REGISTERED!")
    print("Please send an email to group1@apsjorhat.org to register")
    exit()