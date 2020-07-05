def build_profile(first,last,**user_info):
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info

my_profile = build_profile('Jason','Heywood',age=22,location='Tian Jin',state='undergraduate')

for key in reversed(list(my_profile.keys())):
    print(f"{key}:\t{my_profile[key]}")