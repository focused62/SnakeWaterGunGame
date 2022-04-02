
import random

def gamewin(comp,Player2):
    if comp==Player2 :
        return None
    elif comp==1:
        if Player2==2:
            print('Player 2 wins')
        elif Player2==3:
            print('Player 2 wins')
    elif comp==2:  
        if Player2==3:
            print('Player 1 wins')
        elif Player2==1:
            print('Player 1 wins')
    elif comp==3:
        if Player2==1:
            print('Player 1    wins')
        elif Player2==2:
            print('Player 2 wins')
PlayerN=input("Enter Player 2's name:" )
print('Player 1-Computer''s Turn: Snake(s)->1  water(w)-> 2 or Gun(g)-> 3:')   
rand=random.randint(1,2) 
print(rand)   
if rand==1:   
    comp='s'  
elif rand==2:
    comp='w'
elif rand==3:
    comp='g'


Player2=int(input('Player 2 Turn: Snake(s) water(w) or Gun(g):'))
a=gamewin(comp,Player2)


#a=gamewin(comp,Player2)

if Player2==1:   
    print(f'Player 2 {PlayerN} chooses- s') 
elif Player2==2:
    print(f'Player 2 {PlayerN} chooses- w ')
elif Player2==3:
    print(f'Player 2 {PlayerN} chooses- g')


print(f'Player 1 Computer chooses- {comp}')
#print(f'Player 2 {PlayerN} chooses- {Player}')
if a==None:
    print('THE GAME IS A TIE')
elif a:
    print(f'{PlayerN} wins')
else:
    print(f'{PlayerN} looses')
    '''
    snake water-snake
    water gun- water
    gun snake-gun
    swg=123
    1 2-2
    2 3-2
    3 1-3
    '''
'''import random
def gameWin(comp,you):
  
  if comp==you:
    return None
  elif comp=="s":
    if you=="w":
     return False
    elif you=="g":
     return True
      
  elif comp=="w":
    if you=="g":
     return False
    elif you=="s":
     return True
      
  elif comp=="g":
    if you=="s":
     return False
    elif you=="w":
     return True
    
Player=input('Enter the name of the player- ')   
''' 
print("comp turn:Snake(s) Water(w) or Gun(g)")

randNo=random.randint(1,3)

if randNo==1:
  comp="s"
elif randNo==2:
  comp="w"
elif randNo==3:
  comp="g"
print(f"computer choose\t {comp}\n")
'''
you=input("Your turn:Snake(s)Water(w)orGun(g)?\n")
print(f"You choose\t {you}\n")
#a=gameWin(comp,you)

#print(f"computer choose\t {comp}\n")
#print(f"You choose\t {you}\n")
print("comp turn:Snake(s) Water(w) or Gun(g)")

randNo=random.randint(1,3)

if randNo==1:
  comp="s"
elif randNo==2:
  comp="w"
elif randNo==3:
  comp="g"
print(f"computer choose\t {comp}\n")
a=gameWin(comp,you)
if a==None:
  print("the game is tie!")
elif a:
  print(f"{Player} win!")
else:
  print(f"{Player} lose!")
'''