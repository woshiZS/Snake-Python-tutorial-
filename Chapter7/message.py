def display_message(messages):
    for message in messages:
        print(message)

def send_message(messages,sent_messages):
    while messages:
        mess=messages.pop()
        print(mess)
        sent_messages.append(mess)

infos=['I love you','But I have to leave you alone','Our love is accidential']
sent_ones=[]
send_message(infos[:],sent_ones)
print(infos)
print(sent_ones)