import random as r
def winOrLose(com,user):
    if(com == 0 and user == 1 or
       com == 1 and user == 2 or
       com == 2 and user == 0):
       print("Congratulations! You Win")
       
    elif(com == 0 and user == 2 or
         com == 1 and user == 0 or
         com == 2 and user == 1):
         print("Computer Win")
         
    else:   
        print("Match Draw")       
    
com_choice = r.randint(0,2)
'''0 as ston
   1 as paper
   2 as scissor'''
 
print('''Enter 0 for ston,
Enter 1 for paper,
Enter 2 for scissor''') 
print()

while(1):
    user_choice = int(input("Enter your choice:-")) 
    print("computer choice =",com_choice)
    print()
    if(user_choice <= 2 and user_choice >= 0):
        winOrLose(com_choice,user_choice) 
        break
    else:
        print("""You entered wrong choice
        Try again""")
        continue                 
                            

   