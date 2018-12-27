
while True:
    import random
    a = random.randint(0,9)
    b = input("Guess the number \n")
    if a == b:
        print "You guessed it! \n"
    elif a < b:
        print "Thats too high!"
        print "The number was " + str(a) + "!"
    elif a > b:
        print "Thats too low! "
        print "The number was " + str(a) +"!"
    c = raw_input("Want to play again \n")
    if c == "yes":
        continue
    if c == "no":
        break
    if c != "yes" or "no":
        print "You typed this " +c
        break




