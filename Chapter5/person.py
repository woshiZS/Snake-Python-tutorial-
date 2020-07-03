person_0={'first_name':'Jason','last_name':'Heywood','age':'22','city':'Tian Jin'}
person_1={'first_name':'Bob','last_name':'Allen','age':'34','city':'Los Angels'}
person_2={'first_name':'Kobe','last_name':'Bryant','age':'43','city':'Phila'}

persons=[person_0,person_1,person_2]

for person in persons:
    print(" ")
    for key in person:
        print(key+" : "+person[key])

