import math

while True:
    try:
        text = input('> ')
        if text[0] == 'q':
            break
        x  = float(text)
        y = math.log10(x)
        print(f"log10{x} = {y}\n")
    except ValueError:
        print("The value must be greater than 0")