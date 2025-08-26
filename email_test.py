import gmail
email_id="use own email id here"
app_pass="use own app password gmail here"

def send_openacn_ack(uemail,uname,uacn,upass):
    con=gmail.GMail(email_id,app_pass)
    sub="Congrats😊,Account opened successfully"
    
    utext=f"""Hello,{uname}
Welcome to ABC Bank
Your Acc No is {uacn}
Your Pass is {upass}
Kindly change your password when you login first

Thanks
ABC Bank
Noida
    """
    msg=gmail.Message(to=uemail,subject=sub,text=utext)
    con.send(msg)

def send_otp(uemail,otp,amt):
    con=gmail.GMail(email_id,app_pass)
    sub="otp for fund transfer"
    
    utext=f"""Your otp is {otp} to transfer amount {amt}

Kindly use this otp to complete transfer
Please don't share to anyone else

Thanks
ABC Bank
Noida
    """
    msg=gmail.Message(to=uemail,subject=sub,text=utext)
    con.send(msg)

def send_otp_4_pass(uemail,otp):
    con=gmail.GMail(email_id,app_pass)
    sub="otp for password recovery"
    
    utext=f"""Your otp is {otp} to recover password
Please don't share to anyone else

Thanks
ABC Bank
Noida
    """
    msg=gmail.Message(to=uemail,subject=sub,text=utext)
    con.send(msg)


def send_otp_4_close(uemail,otp):
    con=gmail.GMail(email_id,app_pass)
    sub="otp for account closed"
    
    utext=f"""Your otp is {otp} to close account
Please don't share to anyone else

Thanks
ABC Bank
Noida
    """
    msg=gmail.Message(to=uemail,subject=sub,text=utext)
    con.send(msg)