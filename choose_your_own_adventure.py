name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You are on a dirt road. It has come to an end, and you can go left or right. Which way to go? ").lower()

if answer == "left":
    answer = input("You come to a rive, you can walk around it or swim accros? Type walk to walk around and swim to swim accross: ").lower()
    
    if answer == "swim":
        print('You swam accross and were eaten by an alligator.')
    elif answer == "walk":
        print("You worked for many miles, ran out of water and lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bride, it looks wobbly, do you want to cross it or head back? (cross/back)").lower()
    if answer == "back":
        print('You go back and lose.')
    elif answer == "cross":
        answer = input("You cross the bridge and meet the stranger. Do you talk to them? Yes/No: ").lower()
        if answer == "Yes":
            print('Stranger gives gold and you win.')
        elif answer == "No":
            print("You ignore stranger and you lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
        
else:
    print("Not a valid option. You lose.")
    

print("Thank you for trying this game.")