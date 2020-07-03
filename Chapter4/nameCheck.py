current_users=['admin','Jason','Heywood','Jack','Bob']

for i in range(0,len(current_users)):
    current_users[i]=current_users[i].lower()

new_users=['admin','Jason','James','Durant','Kobe']

for new_user in  new_users:
    if new_user.lower() in current_users:
        print("This username has already been used.")
    else:
        print('This username is available.')