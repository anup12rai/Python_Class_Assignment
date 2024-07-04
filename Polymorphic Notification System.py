# Create a base class Notification with a method send().
# Then, create two derived classes EmailNotification and
# SMSNotification that override the send() method to simulate sending an email 
# and an SMS, respectively. Demonstrate polymorphism by creating a list of notifications and sending them.
class Notification:
    def send(self):
        pass
class SMSNotification(Notification):
    def send(self):
        return "Sending SMS..."
class EmailNotification(Notification):
    def send(self):
        
        return "Sending Email..."

wer = [SMSNotification(),EmailNotification()]
for i in wer:
    print(i.send())            