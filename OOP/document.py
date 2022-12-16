class Document:
    def __init__(self,text=""):
        self.text = text

    def to_string(self):
        return self.text
    
    def set_text(self, text_string):
        self.text = text_string


class Email(Document):
    def __init__(self, sender="", recipient="", title=""):
        self.sender = sender
        self.recipient = recipient
        self.title = title
    
    def set_sender(self, sender):
        self.sender = sender

    def set_recipient(self, recipient):
        self.recipient = recipient

    def set_title(self, title):
        self.title = title

    def get_sender(self):
        return self.sender

    def get_recipient(self):
        return self.recipient

    def get_title(self):
        return self.title

    def send(self):
        print ("sending mail...")
        print("Sent succesfuly.")


class File(Document):
    def __init__(self, pathname=""):
        self.pathname = pathname
        


mail_doc = Email()
print("My Mailer")

sender = input("From: ")
recipient = input("To: ")
title = input("Title: ")
body = input("Body: ")

mail_doc.set_recipient(recipient)
mail_doc.set_sender(sender)
mail_doc.set_title(title)
mail_doc.set_text(body)

print(
    f'''
    From: {mail_doc.sender}
    To: {mail_doc.recipient}
    Title: {mail_doc.title}
    Body: {mail_doc.text}
    '''
)
mail_doc.send()




# my_doc = Document()

# my_doc.set_text("Hello, I am  faraji")
# print(my_doc.to_string())

# print(my_doc.my_text)