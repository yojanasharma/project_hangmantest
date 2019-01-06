import time
import random
secret_word=["hang","man","juju","thapadi"]
x=random.randint(0,3)
real_word=list(secret_word[x])
y_or_no=input("do you want to play:\n Enter Y for yes and N for no")
time.sleep(5)
if y_or_no=='Y':
    guess=['_']*len(real_word)
    print(guess)
    try1=len(real_word)+1
    while try1>0:
        char=input("")
        for i in range (0,len(real_word)):
            if (real_word[i]==char):
                guess[i]=char

        if char not in real_word:
            try1=try1-1
        if char in real_word:
          print (guess)
        check="_"
        if check not in guess:
            print("You won")
    if try1 == 0:
        print("dead baby")
else:
    print("thanks only")
