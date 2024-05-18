import random

def game():
    number=random.randint(1,10)
    print(number)
    i=1
    while i<=3:
     user_num=int(input("gase a number 1 to 10 "))
     if number == user_num:
        print("wine the game")
        print("....................................")
        start()
        break
     elif i<3:
      print("try agin")
     i+=1

    if i>3:
        masg="loss the game number are \n "
        print( masg + str(number))
        print("......................................")
        start()
     

def start():
    user_opt=int(input("1.play game \t\t 2.game info \t\t 3.exit game\n..............................\n enter option "))
    
    match user_opt:
       case 1:
         game()
       case 2:
         print("gessing number in 1 to 10 and \nyou are three time enter your number")
         print("....................................")
         start()
       
          
         
start()



 






    
