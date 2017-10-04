import smtplib, time
shopping_list = []
print("What should we get from the store today?")
print("Enter DONE to end list..")

while True:
    new_item = input("> ")

    if new_item == 'DONE':
        break

    shopping_list.append(new_item)
print("Here's your list for today: ")

for item in shopping_list:
    print(item)

print("Do you want me to email it to you?")
send = input("")
if send == "YES":
    print("OKAY!!")

    def email():
        print('Who are you sending to?')
        recipient_email = input()
        #print(shopping_list)
        subject = str(shopping_list) ## THIS IS WHERE IM STUCK..
        #print(subject)
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login('shoppinglist.bot1@gmail.com', 'shoppinglistpassword')
        # Need advice making this secure..
        smtpObj.sendmail('shoppinglist.bot1@gmail.com', recipient_email, subject + " Don't forget the reusable bags!")
        smtpObj.quit()

        print("Your mail is on it's way...")
        #wait 2 seconds
        time.sleep(2)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("Sent!")

    email()
else:
    print("FAIL")
