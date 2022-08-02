
name = input("Type your Name: ")
print("Welcome",name,"to this adventure!")


while True:

    ans = input("You have two options. You can choose either Mountain or Sea-beach. Choose your answer ")

    if ans.lower() == "mountain":
        ans = input("Where do you want to go peak or underneath of hills? ").lower()
        if ans == "peak":
            ans = input("Do you have energy yes or no? ").lower()
            if ans == "yes":
                print("You will be able to reach to the peak of hill and You will win!")
                print("Thanks for trying this adventure", name)
                break
            else:
                print("You have fallen down and You will lose!")
                print("Thanks for trying this adventure", name)
                break
        elif ans == "underneath":
            ans = input("Do you want to go to cave or back? ").lower()
            if ans == "cave":
                print("You will find a gold and You will win!")
                print("Thanks for trying this adventure", name)
                break
            else:
                print("You will lose!")
                print("Thanks for trying this adventure", name)
                break
        else:
            print("You gave up so You are a looser!")
    elif ans.lower() == "sea-beach":
        ans = input("Can you Swim yes or no? ").lower()
        if ans == "yes":
            ans = input("Do you want to go to in the middle of sea yes or no? ").lower()
            if ans == "yes":
                print("Shark will eat you then You will die and lose!")
                print("Thanks for trying this adventure", name)
                break
            else:
                print("You will survive and win!")
                print("Thanks for trying this adventure", name)
                break
        elif ans == "no":
            ans = input("Do you have life jacket yes or no ").lower()
            if ans == "yes":
                print("You will win!")
                print("Thanks for trying this adventure", name)
                break
            else:
                print("You will lose!")
                print("Thanks for trying this adventure", name)
                break
        else:
            print("You gave up so You are a looser!")
            print("Thanks for trying this adventure", name)
            break

    else:
        print("There is no options like that, please choose the right option :)")
        continue
