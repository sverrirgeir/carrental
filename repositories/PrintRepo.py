import smtplib

class PrintRepo():    
    def send_email(self, name, inday, outday):
            our_email = 'bilaleigaehf@gmail.com'
            password = 'Verklegt1'
            send_to_email = input("\n\tEmail: ")
            message = name + "\n" + " \nPontun Stadfest " + "\nFra: " + str(inday) + " Til: " + str(outday)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(our_email, password)
            server.sendmail(our_email, send_to_email , message)
            server.quit()
            return