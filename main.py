x = int(input("Give me a four digit number that is even but does not end with 0"))

####### The nice way to do it ####### EASY TO READ!!!
if x >= 1000 and x <= 9999 and x%2 == 0 and not x%10 == 0:
    print("Good job!")
else:
    print("Nope, that's not right!")

####### The nested way to do it #### SAME RESULT!!!
if x >= 1000:
    if x <= 9999:
        if x%2 == 0:
            if not x%10 == 0:
                print("Good job!")
            else:
                print("Nope, that's not right! It ends with 0")
        else:
            print("Nope, that's not right! It is not even")
    else:
        print("Nope, that's not right! It is too big")
else:
    print("Nope, that's not right! IT is too small")

#quit
quit()