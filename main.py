x = int(input("Give me a four digit number that does not end with 0 and is even."))

####### The nice way to do it ####### EASY TO READ!!!
if x >= 1000 and x <= 9999 and x%2 == 0:
    print("Good job!")
else:
    print("Nope, that's not right!")

####### The nested way to do it #### SAME RESULT!!!
if x >= 1000:
    if x <= 9999:
        if x%2 == 0:
            print("Good job!")
        else:
            print("Nope, that's not right!")
    else:
        print("Nope, that's not right!")
else:
    print("Nope, that's not right!")

#quit
quit()