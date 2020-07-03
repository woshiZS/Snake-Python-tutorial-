favorite_language={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

candidates = ['jen','Bob','jason','Durant']

for candidate in candidates:
    if candidate.lower() in favorite_language.keys():
        print(f"{candidate.capitalize()}, thank you for your respoding!")
    else:
        print(f"{candidate.capitalize()},could you please take the poll?")