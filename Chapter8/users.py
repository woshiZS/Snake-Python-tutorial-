class User:
    '''Describing a user.'''

    def __init__(self,first_name,last_name,**user_info):
        self.user_info={}
        self.user_info=user_info
        self.login_attempts=0
        self.user_info['first_name']=first_name
        self.user_info['last_name']=last_name

    def describe_user(self):
        print("The basic information of this user is below :")
        for k,v in self.user_info.items():
            print(f"{k}:\t{v}")

    def greet_user(self):
        print(f"Hello,{self.user_info['first_name']}{self.user_info['last_name']}")

    def increment_login_attempts(self):
        self.login_attempts+=1
    
    def reset_login(self):
        self.login_attempts=0

if __name__=="__main__":
    me = User('Jason','Heywood',age=18,hobby='play basketball')

    me.greet_user()
    me.describe_user()

    for i in range(5):
        me.increment_login_attempts()

    print(me.login_attempts)
    me.reset_login()
    print(me.login_attempts)

class Privilege:
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

class Admin(User):

    def __init__(self, first_name, last_name, **user_info):
        super().__init__(first_name, last_name, **user_info)
        self.privileges=Privilege()


if __name__=="__main__":
    adm_0=Admin('Jason','Heywood',age=18,hobby='play basketball')
    adm_0.privileges.show_privileges()