digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"






def to_decimal(inp, base):
    if type(inp) != str:
        return "input type error"
    base = int(base)
    if type(base) != int or base > 36:
        return "bass type error"
    out = int(0)
    exp = int(0)
    char_val = int(0)
    for x in reversed(inp):
        char_val = digits.index(x.upper())
        out += (char_val * (base ** exp))
        exp += 1
    return out

def from_decimal(input_str,base):
    base = int(base)
    input_str = int(input_str)
    if type(input_str) != str:
        return "input type error"

    if type(base) != int or base > 36:
        return "bass type error"
    out = ''
    remainder = 0
    char = ''
    if int(input_str) == 0:
        return 0
    while input_str > 0:
        remainder = input_str % base
        input_str = input_str // base
        char = digits[remainder]
        out = char + out
    return out

def main():
    while True:
        option = input('For what purpose do you come to ME, the HEXORCIST‽ \n 1. I need to convert between 2 bases \n 2. I uh- was actually just leaving now that you mention it... \n >')
        if option == '2':
            quit()
        elif option == '1':
            val = input("Value > ")
            base1 = input("What base was that? >")
            base2 = input("What base should it be? >")
            print(f'that would be... \n about {from_decimal(to_decimal(val,base1),base2)}')
        else:
            print("I'm not dealing with your crap today. Get out.")
            quit()
main()
