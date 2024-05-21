import random

list=[1,2,3,4,5,6]
rolchoice=['batting','bowling']
playerbool=False
computerbool=False
cscore,pscore=0,0
cbat=0
pbat=0

#function for the game//
def game(cbool,pbool,cbat,pbat,cscore,pscore):
   
    if cbool==True and cbat==0:
    
            print('______computer turn______')
            cval=random.choice(list)
            pval=int(input('enter 1-6:'))
            print(f'computer choose {cval}')
            while list[pval-1]!=cval :
                cscore+=cval
                if cscore>pscore and pbat==1:
                    print(f'____computer score:{cscore} ____\n ____player score:{pscore} ______')
                    print(f'computer won the match by {cscore-pscore} runs!!!!!!!')
                    exit() 
                else:
                    cval=random.choice(list)
                    pval=int(input('enter 1-6:'))
                    print(f'computer choose {cval}_')
                
            print(f'computer score:{cscore}, player score:{pscore}')
                
            if  pbat==0 :
                print(f'you took a wicket, now u need to beat computer score by {cscore}')
                cbool=False
                pbool=True
                cbat=1
                game(cbool,pbool,cbat,pbat,cscore,pscore)
            
                
       
        
    elif pbool==True and pbat==0 :
  
            print('______player turn______')
            cval=random.choice(list)
            pval=int(input('enter 1-6:'))
            print(f'computer choose {cval}_')
            while list[pval-1]!=cval:
                pscore+=list[pval-1]
                if pscore>cscore and cbat==1:
                    print(f'____computer score:{cscore} ____\n ____player score:{pscore} ______')
                    print(f'you won the match by {pscore-cscore} runs!!!!!!!!')
                    exit()
                else:
                    cval=random.choice(list)
                    pval=int(input('enter 1-6:'))
                    print(f'computer choose {cval}')
                
            print(f'computer score:{cscore}, player score:{pscore}')
            
            if cbat==0:
                print(f'computer took a wicket, now u need to take down the computer before {pscore}')
                pbat=1
                cbool=True
                pbool=False
                game(cbool,pbool,cbat,pbat,cscore,pscore)
        
            
            
            
#start of program//
pchoice=input("odd/even: ")
player=int(input("enter a number b/w 1-6: "))
computer=random.choice(list)
print(f' computer choose {computer}')
if (list[player-1]+computer)%2!=0 :
    if pchoice=='even':
        print('computer won the toss!!!!!!')
        computerchoice=random.choice(rolchoice)
        print(f'compuer choose {computerchoice}!')
        if(computerchoice=='batting'):
            computerbool=True
        else:
            playerbool=True
    else:
        print('you won the toss!!!!!!')
        uchoice= input('choose batting/bowling:')
        print(f'you choose {uchoice}!')
        if  uchoice=='batting':
            playerbool=True
        else:
            computerbool=True
            
else:
    if pchoice=='odd':
        print('computer won the toss!!')
        computerchoice=random.choice(rolchoice)
        print(f'compuer choose {computerchoice}!')
        if(computerchoice=='batting'):
            computerbool=True
        else:
            playerbool=True
    else:
        print('you won the toss!!')
        uchoice= input('choose batting/bolling:')
        print(f'you choose {uchoice}!')
        if  uchoice=='batting':
            playerbool=True
        else:
            computerbool=True
           
game(computerbool,playerbool,cbat,pbat,cscore,pscore)
            