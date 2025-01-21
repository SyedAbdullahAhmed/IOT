import os
import resend

resend.api_key = ""


def sendMail():
    print("Mail sent")
    params: resend.Emails.SendParams = {
        "from": "Acme <onboarding@resend.dev>",
        "to": ["abdullahahmedsyed65@gmail.com"],
        "subject": "Temperatrure Alert!",
        "html": '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Temperature Rise Alert</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 20px; background-color: #f9f9f9;">
    <h1 style="color: #d9534f;">⚠️ Temperature Rise Alert</h1>
    <p><strong>It works!</strong></p>
    <p>The temperature has exceeded the safe threshold. Immediate action is required to mitigate potential risks. Please check the system and ensure safety protocols are in place.</p>
</body>
</html>"
'''
    }

    email = resend.Emails.send(params)
    print(email)
    
