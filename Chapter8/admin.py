from users import User

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