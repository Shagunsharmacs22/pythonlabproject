#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     30-04-2023
# Copyright:   (c) HP 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
import string

def generate_otp(length):
    # define all possible characters for the OTP
    characters = "12345"+string.ascii_letters + string.digits

    # generate random OTP by choosing characters randomly
    otp = ''
    for i in range(length):
        otp += random.choice(characters)

    return otp

# generate a 6-digit alphanumeric OTP
otp_6 = generate_otp(6)
print('6-digit OTP:', otp_6)

# generate a 4-digit alphanumeric OTP
otp_4 = generate_otp(4)
print('4-digit OTP:',otp_4)