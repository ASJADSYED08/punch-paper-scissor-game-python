import random
i=1
n=0
l=0
d=0
name=input("ENTER YOUR NAME->")
while(i<=5):
    print("----paper,scissor,punch----")
    inp=input(name)
    lst=["paper","scissor","punch"]
    choice=random.choice(lst)
    print("PC->",choice)
    i=i+1
    if inp=="paper":
        if choice=="paper":           
            print("draw")
            d=d+1
        elif choice=="scissor":
            print("PC Won")
            l=l+1
        elif choice=="punch":
            print(name," won")
            n=n+1
    if inp=="punch":
        if choice=="punch":           
            print("draw")
            d=d+1
        elif choice=="scissor":
            print(name," won")
            n=n+1
        elif choice=="paper":
            print("PC won")
            l=l+1
    if inp=="scissor":
        if choice=="scissor":           
            print("draw")
            d=d+1
        elif choice=="paper":
            print(name," won")
            n=n+1
        elif choice=="punch":
            print("PC won")     
            l=l+1
    if i==6:  
        print("-------RESULT-------")              
        print(name," won",n,"matches")
        print("PC won",l,"matches")  
        print("Matches Draw->",d)                         

                    

