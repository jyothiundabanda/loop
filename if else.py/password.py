from builtins import input


password=input("enter the password")
if len(password)>6:
    if "@" or "#" or "&" in password:
        if "a" or "b" or "c" or "d"  or "e" or "f" or "g" or "h" or "i"  or "j" or "k" or "l" or "m" or "n" or "o" or "p" or "q" or "r" or "s" or "t" or "u" or "v" or "w" or "x"or "y" or "z"in password:
            if "A" or "B" or "C" or "D" or "E" or "F" or "G" or "H" or "I" or "J" or "K" or "L" or "M" or "N" or "O"  or "P"  "Q" or "R" or "S" or "T" or "U" or "V" or "W" or "X" or "Y" or "Z"in password: 
                if "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" in password:
                    print("strong password")
                else:
                    print("week password")
            else:
                print("valid upper case")
        else:
            print("lower case")
    else:
        print("valid special character")
else:
    print("invalid values")