import random
import python
def choose():
    words=['rainbow','compare','light','dark','horses','player','dusky','knighthood','hendricks']
    pick=random.choice(words)
    return pick
def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
def thank(p1n,p2n,pp1,pp2):
    print(p1n,' Your score is: ',pp1)
    print(p2n,' Your score is: ',pp2)
def play():
    p1n=input('Enter name player 1: ')
    p2n=input('Enter name player 2: ')
    pp1=0
    pp2=0
    turn=0
    while(1):
        word=choose()
        qn=jumble(word)
        print(qn)
        if turn%2==0:
            print('Its your turn ',p1n)
            ans=input('Ener the correct word: ')
            if ans==word:
                print("CORRRECT WORD")
                pp1=pp1+1
            else:
                print("WRONG ANSWER")
                print("The correct word is: ",word)
            c=input("Press 1 to continue and 0 to quit: ")
            if c==0:
                print("C=0")
                thank(p1n,p2n,pp1,pp2)
                break
        else:
            print(p2n,'Its your turn ',p2n)
            ans=input('Enter the correct word: ')
            if ans==word:
                print("CORRECT WORD")
                pp2=pp2+1
            else:
                print("INCORRECT WORD")
                print("The correct word is: ",word)
            c=input("Press 1 to continue and 0 to quit: ")
            if c==0:
                print("C=0")
                thank(p1n,p2n,pp1,pp2)
                break
        turn=turn+1

play()          
#TEST LINE 1
# Test line 2   
    
