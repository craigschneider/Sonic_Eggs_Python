def Start():
    print("War In Paradise Python")
    print("Credits:")
    Credits = ["Sonic Egg - Maker of game, Ree Studios - Original game, Scratch - Project maker, Pthon - Program maker"]
    for x in Credits:
        print(x)
#Starting up the game
Start()
Answer = ""
Gold = 0
GuySad = "true"
GuyHungry = "true"
Got15Gold = "false"
Inventory = [""]
TalkedLordLeft = 0
#Frist ZoneQuestion
def Zone_Town():
    print("You go to the town")
    Answer = ""
    while not Answer == "4":
        Answer = input("Buy something at the shop - 1 Walk over to cube without hat - 2 Walk over to hungry guy - 3 Go to city - 4")
#Ans 1
        if Answer == "1":
            Answer = input("Shopkeeper: What would you like to buy? Wodden Sword (Cost: 5g) Hotdog (Cost: 5g) Healing Shard (Cost: 10g)")
            if Answer == "Wodden Sword":
                if Gold > 4:
                    Gold = (Gold - 5)
                    Inventory = Iventory, "Wodden Sword"
            if Answer == "Hotdog":
                if Gold > 4:
                    Gold = (Gold - 5)
                    Inventory = Iventory, "Hotdog"
            if Answer == "Healing Shard":
                if Gold > 9:
                    Gold = (Gold - 10)
                    Inventory = Iventory, "Healing Shard"
            
#Ans 2
        if Answer == "2" and GuySad == "true":
            print("Sad Guy: Can you please find my hat? I can't find it.")
            Answer = input("Get hat? Yes / No")
            if Answer == "Yes":
                print("Happy Guy: Thank you for finding my hat.")
                GuySad = "false"
                Gold = Gold + 5
            else:
                print("Sad Guy: Why Not?")

#Ans 3
        if Answer == "3" and GuyHungry == "true":
            print("Jerry: Hello!")
            print("Jerry: Can you buy an apple for me?")
            print("Jerry: I have not eaten in days.")
            print("Jerry: And I have no money.")
            print("Jerry: So please buy an apple for me.")
            Answer = input("Get apple? Yes / No")
            if Answer == "Yes":
                print("Jerry: Thank you!")
                GuyHungry = "false"
                Gold = Gold + 5
            else:
                print("Jerry: Why Not?")
def Zone_Cave():
    Answer = ""
    print("You go in the cave")
    while not Answer == "3":
#Second ZoneQuestion
        Answer = input("Get Jatty's Beachball - 1 Talk to trainer 1 - 2 Go to city - 3")
#Ans 1
        if Answer == "1":
            print("Jatty: Thank you for finding my ball!")
            print("Jatty: Here is 10 gold!")
            Gold = Gold + 10
#Ans 2
        if Answer == "2":
            print("Trainer 1: Hello.")
            print("Trainer 1: I was supposed to be with the others at shore")
            print("Trainer 1: But I didn't want to go...")
            print("Trainer 1: So I took the day off")
            print("Fight not added yet")
def Zone_Castle ():
    Answer = ""
    print("You went outside the castle")
    while not Answer == "3":
#Third ZoneQuestion
        Answer = input("Talk to long lost brother - 1 Go to floor 1 (Castle) - 2 Go to city - 3")
#Ans 1
        if Answer == "1":
            print("???: Hello.")
            print("Long Lost Brother: I am your long lost brother")
            print("Long Lost Brother: I have not seen you for 2 years.")
            print("Long Lost Brother: Finally, we meet again.")
            Answer = input("Long Lost Brother: Say, Wanna battle?")
            if Answer == "Yes":
                print("Battle not added yet")
            else:
                print("Long Lost Brother: Okay, maybe next time.")
#Ans 2
        if Answer == "2":
            Answer = input("Do you want to go to floor 2? Yes / No")
            if Answer == "Yes":
                Answer = input("Do you want to go to the top?")
                if Answer == "Yes":
                    print("There is nothing at the top other than wind.")
                    print("You decide to go back to the bottom")
        
def Zone_City():
    Answer = ""
    print("You go to the city")
#Fourth ZoneQuestion
    while not Answer == "5" or not Answer == "6" or not Answer == "2":
        Answer = input("Get 15 Gold - 1 Go in cave - 2 Talk to guard - 3 Talk to lord left - 4 Go to castle - 5 Go to town - 6")

#Ans 1
        if Answer == "1" and Got15Gold == "false":
            Gold = Gold + 15
            Got15Gold = "true"
#Ans 3
        if Answer == "3":
            Answer = input("Guard 1: Do you want to help destroy the left island? Yes / No")
            if Answer == "Yes":
                Laps = 0
                while not Answer == "2":
                    Answer = input("Do another lap to train - 1 Talk to the guard and go back to the city")
                    if Answer == "1":
                        Laps = Laps + 1
#Ans 4
        if Answer == "4":
            if TalkedLordLeft == 3:
                print("(Boss Not Added Yet")
            else:
                print("Lord Left: WHY DID YOU TALK TO ME?!?!?")
                print("Lord Left: DO NOT THIS AGAIN")
                #print("Lord Left: DO THIS " 3 - TalkedLordLeft " MORE TIMES AND I, THE GREAT PAPUYRUS WILL CAPTURE YOU!")
                print("Lord Left: DO THIS ", 3 - TalkedLordLeft," MORE TIMES AND I WILL FIGHT YOU!")
    if Answer == "2":
        Zone_Cave()
    else:
        if Answer == "5":
            Zone_Castle()
        else:
            Zone_Town()
while "1" == "1":
    Zone_City()
