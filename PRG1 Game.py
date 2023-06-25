import os, random, time, sys, pygame

#Initial conditions
pygame.init()


run = True
menu = True
play = False
role_select = True
talking = True
fight = False

location = "Start"


#Clear output
def clear():
    os.system("cls")


#Visual defined stuff
def bracket():
    print("+---------+")
def player_bar_top():
    print("<|=/==/==/M\==\==\=|>")
def player_bar_bot():
    print("<|=\==\==\W/==/==/=|>")
def long_bracket():
    print("+" + "-"* 18 + "+")
def bandit_banner():
    print("o-|======-")
def vs_banner():
    print("\n+-----{ VS }----+\n")
def class_banner():
    print("\n-====|-o xXx " + "-"*16 + " xXx o-|====-\n")

def Mage_asci():
    print(
"        ,    _\n"
"       /|   | |\n"
"     _/_\_  >_<\n"
"    .-\-/.   |\n"
"   /  | | \_ |\n"
"   \ \| |\__c|)\n"
"   /(`---')  |\n"
"  / / / || \ |\n"
" /_-_/__|_-_\ ")
    
def Warrior_asci():
    print("""
  ,^.
  |||
  |||       _T_
  |||   .-.[>|<].-.__
  ===__/\ |"'V'"||\  \ 
  E])__\/\/'\-/'\|''''|
   O     \[][][]||C H |
          |[][][]| U J|
         /M[]M[]M'.__.'
         |]"U[]U"[|
         |X|/  \|X|
         | |    | |
       <\X\|    |/X/>
""")

def Rogue_asci():
    print("""
    (
     \ 
      )
##--------> 
      )
     /
    (
""")


#Role
def Warrior():
    global HP, HP_MAX, ATK, AMR, interaction, spec, spec_description, role, chance, spec_count
    HP = 15   # Hitpoints
    HP_MAX = 15   # Hitpoints Max
    ATK = 6   # Attack points
    AMR = 4   # Armor Points
    interaction = 1 # How others will treat this character
    spec = HP_MAX
    spec_count = 2
    spec_description = "Heal up to your \nlife value!"
    role = "Warrior"
    chance = 8
    
def Mage():
    global HP, HP_MAX, ATK, AMR, interaction, spec, spec_description, role, chance, spec_count
    HP = 8   # Hitpoints
    HP_MAX = 8   # Hitpoints
    ATK = 4   # Attack points
    AMR = 2   # Armor Points
    interaction = 2 # How others will treat this character
    spec = 32
    spec_count = 1
    spec_description = f"Cast fireball! \nDeal {spec} dmg!"
    role = "Mage"
    chance = 10
    
def Rogue():
    global HP, HP_MAX, ATK, AMR, interaction, spec, spec_description, role, chance, spec_count
    HP = 10   # Hitpoints
    HP_MAX = 10   # Hitpoints Max
    ATK = 6   # Attack points
    AMR = 6   # Armor Points
    interaction = 3 # How others will treat this character
    spec = 7
    spec_count = 3
    spec_description = f"Throw knives! \nDeal {spec} dmg for each \nthat hits!"
    role = "Rogue"
    chance = 5 # from 1 to 5 a chance on a crit


# Roland
def Stranger():
    global hp_stranger, hp_max_stranger, atk_stranger, amr_stranger
    hp_stranger = 10
    hp_max_stranger = 10
    atk_stranger = 2
    amr_stranger = 2


# Enemies RZ
bandits = {
    "name" : "Bandits",
    "hp" : 15,
    "hp_max"  : 15,
    "atk" : 3,
    "amr" : 1,
}
#not being used
dragon = {
    "name" : "Dragon",
    "hp" : 35,
    "hp_max"  : 35,
    "atk" : 6,
    "amr" : 4,
}


#Dragon JM
def Dragon():
    global hp_dragon, hp_max_dragon, atk_dragon, amr_dragon, attacks
    hp_dragon = 35
    hp_max_dragon = 35
    atk_dragon = 8
    amr_dragon = 5
    attacks = ["Fiery breath", "Razor sharpclaws", "Spiky tail"]
    
def display_dragon_stats():
    player_bar_top()
    print(f"Oirgos the Dragon")
    print(f"Hitpoints: {hp_dragon}/{hp_max_dragon}")
    print(f"Attack: {atk_dragon}")
    print(f"Armor: {amr_dragon}")
    player_bar_bot()


# Display Enemy Stats RZ
def display_enemy_stats(enemy):
    print(f"{enemy['name']}")
    print(f"HP: {enemy['hp']}/{enemy['hp_max']}")
    print(f"Atk: {enemy['atk']}")
    print(f"Def: {enemy['def']}")

# Display Player Stats
def display_stats():
    player_bar_top()
    print(f"{NAME} the {role}")
    print(f"Hitpoints: {HP}/{HP_MAX}")
    print(f"Attack: {ATK}")
    print(f"Armor: {AMR}")
    print(f"Special: {spec_description}")
    player_bar_bot()
    print()
    long_bracket()
    print(f"Special uses left: {spec_count}")
    long_bracket()


# Walls of text    
def introduction():
    input("You walked in to a tavern and ordered your favourite apple juice. \n\n> ")
    clear()    
    input(f"Stranger: Hello there stranger. Are you a {role} by any chance? \n\n> ")
    clear()
    input(f"Stranger: Ha! I knew it. It's been quite some time since I've seen one of you {role}s \n"
    "around here. But it just so happens that I am seeking help and you might be what I need. \n"
    "A vicious dragon has made it's liar in the cave up north from here. He lies on piles \n"
    "of gold that is just waiting to be taken. \n\n>")

def credits():
    print('''
    This is a short text rpg game made by Rafal Zgrzywa & Jack Madsen \n
    as a project for programming course. The idea behind the game is for \n
    the player to select a class "warrior", "wizzard", "rogue" and complete \n
    a quest.
        
    Special thanks to orkslayergamedev whose youtube guide served as an example \n
    on how to make simple games in python.
    ''')

def crossroads():
    print("You arrive at the crossroad.\nOne path is a paved road where merchants travel with their carts \n"
    "and the other one is a more rough forest path. Select where you want to go:")

def boss_monologue():
    print("The Dragon's 'Cave'\n\n")
    print("The cave entrance is large, across it is littered with charred bones and crushed armor..\n")
    print("Inside you hear the deep breaths of the dragon, and you know that it knows you are here.")
    input("\n> ")
    clear()
    print("Inside you follow the sound, and the ever growing amount of dead adventurers...")
    print("Finally, the cave opens up to an enormous open space. From the floor gold piles up several meters")
    print("You start to shout, to gain the dragons attention, and it worked..!")
    input("\n> ")
    clear()
    print("Dragon: FOOLS!!! YOU COME TO STEAL MY GOLD?!! LIKE EVERYONE ELSE, YOU MUST DIIIIEEEE!!!")
    input("\n> ")
    clear()

def the_end(): # JM
    print("With the vicious dragon dead, you realize how tired and worn out you really are")
    print("You find a nice spot to sit down to rest, and ask Roland for his further plans.")
    print("Roland replies: With this wealth all to myself i will start by...")
    print("You interrupt Roland: - To yourself?! I Should at least get half! I Took you all the way here and killed your Dragon")
    print("Roland has gotten up and walks towards you. A sudden swing, followed by a heavy thump sound.")
    input("\n> ")
    clear()
    print("Thats all I remember.. And the pain.. The pain was immense for weeks.. ")
    print("Sometimes when I lie down I still get dizzy...")
    print("'Anyways...', you say to your grandchildren: 'Thats how i lost the biggest fortune in the world! - Now go to bed!'")
    input("\n> ")
    clear()


# Battle RZ
def battle(enemy):
    global fight, play, run, HP, spec_count

    hp = enemy['hp']
    hp_max = hp
    atk = enemy['atk']
    amr = enemy['amr']

    while fight:
        clear()
        bandit_banner()
        print(f"{enemy['name']}")
        print(f"HP: {hp}/{hp_max}")
        print(f"Atk: {atk}")
        print(f"Def: {amr}") 
        bandit_banner()   
        print()
        vs_banner()
        print()
        display_stats()
        print("\n")
        print("1 Attack")
        print("2 Talk")
        if spec_count > 0:  
            print("3 Special")
        print("4 Run")
        fight_choice = input("\n> ")
        print()

        if fight_choice == "1":
            crit = random.randint(1,chance)

            # Critical Strike
            if crit == 1:
                hp -= 2 * ATK
                print(f"{NAME} performed a critical strike! \n{enemy['name']} suffered {str(ATK*2)} damage!")
            # Regular Strike
            else:
                hp -= ATK
                print(f"{NAME} dealt {str(ATK)} dmg to {enemy['name']}.")

            print()

            # Did you win?
            if hp <= 0:
                print(f"Congratulations! You have slain {enemy['name']}")
                fight = False

            # Enemy attacks back
            elif hp > 0:
                HP -= atk
                print(f"{enemy['name']} dealt {atk} dmg to {NAME}")
            
            # Did you die?
            if HP <= 0:
                print("You have died...\n\n")
                again = input("Do you wish to play again?\n\n1 Yes \n2 No\n\n> ")
                if again == "1":
                    restart()
                else:
                    quit()



            input("\n> ")

        elif fight_choice == "2":
            talk = random.randint(1,2)

            # Failed talking attempt
            if talk == 1:
                print("You try reasoning with bandits with no success. \nThey use this chance to strike at you!")
                print()
                HP -= atk
                print(f"{enemy['name']} dealt {atk} dmg to {NAME}")

            # Succesfull talking attempt
            elif talk == 2:
                print("You try reasoning with bandits and they lower their guard \ngiving you chance to strike!")
                print()
                hp -= ATK
                print(f"{NAME} dealt {str(ATK)} dmg to {enemy['name']}")

                            # Did you win?
            if hp <= 0:
                print(f"Congratulations! You have slain {enemy['name']}")
                fight = False
            
            # Did you die?
            if HP <= 0:
                print("You have died...\n\n")
                again = input("Do you wish to play again?\n\n1 Yes \n2 No\n\n> ")
                if again == "1":
                    restart()
                else:
                    quit()
            
            input("\n> ")
            
        elif fight_choice == "3" and spec_count > 0:

            if interaction == 1:
                spec_count -= 1
                print("You scream and boost your life energy healing you to the maximum HP.")
                HP = spec
            elif interaction == 2:
                spec_count -= 1
                print("Mage calls to the fire spirit and casts FIREBALL at the enemies!\n")
                print(f"\n{NAME} dealt {str(spec)} dmg to {enemy['name']}")
                hp -= spec
            elif interaction == 3:
                knives = random.randint(0,3)
                spec_count -= knives
                print("Rogue throws 3 knives!")
                print()
                if knives == 0:
                    print("Knives fly and miss the target... \nDon't worry. It happens even to the best. And since you are the best \nit happens to you all the time.")
                else:
                    print(f"{knives} hits the target dealing {knives*spec} damage!")
                    print()
                    hp -= spec * knives
                    print(f"\n{NAME} dealt {str(spec*knives)} dmg to {enemy['name']}")

            # Did you win?
            if hp <= 0:
                print(f"Congratulations! You have slain {enemy['name']}")
                fight = False

            # Enemy attacks back
            elif hp > 0:
                HP -= atk
                print(f"{enemy['name']} dealt {atk} dmg to {NAME}")
            
            # Did you die?
            if HP <= 0:
                print("You have died...\n\n")
                again = input("Do you wish to play again?\n\n1 Yes \n2 No\n\n> ")
                if again == "1":
                    restart()
                else:
                    quit()

            input("\n> ")
        
        elif fight_choice == "4":
            escape = random.randint(1,chance)
            if escape == 1:
                print(f"{NAME}:What is that! - You scream pointing behind the {enemy['name']}. \nAs they turn around, you make your escape.")
                fight = False
            else:
                print("No luck trying to escape.")
                HP -= atk
                print(f"\n{enemy['name']} dealt {atk} dmg to {NAME}")
            
            # Did you die?
            if HP <= 0:
                print("You have died...\n\n")
                again = input("Do you wish to play again?\n\n1 Yes \n2 No\n\n> ")
                if again == "1":
                    restart()
                else:
                    quit()
            
            input("\n> ")


# Restart
def restart():
    global run, menu, play, role_select, talking, fight, location
    run = True
    menu = True
    play = False
    role_select = True
    talking = True
    fight = False
    location = "Start"

#not working
def reset():
    os.execl(sys.executable, sys.executable, *sys.argv)

def play_again(): # JM
    while True:
        again = input("\nDo you wish to play again? \n1 Yes\n2 No\n> ")
        if again == "1":
            clear()
            restart()
            return False
        elif again == "2":
            clear()
            quit() 
        else:
            clear()
            print("Invalid input.")


# Dragon health status check JM
def check_health(): # JM
    # Dragon died                      
    if hp_dragon <= 0:
        print("Oh Dear! You have Defeated the dragon!")
        input("\n> ")
        clear()
        print("Loading...")
        time.sleep(1)
        clear()   
        the_end()
        play_again()

        # You died
    elif HP <= 0:
        clear()
        print("YOU HAVE DIED")
        play_again()

# Music RZ
pygame.mixer.music.load("x2.mp3")
pygame.mixer.music.set_volume(0.5) # Set's the volume to 50%
pygame.mixer.music.play(loops=-1) # loops the music


#-------------------------------------------------------------------#

#THE GAME   
while run:
    
    # Play music
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # GAME MENU
    while menu:
        clear()
        bracket()
        print("1 NEW GAME")
        print("2 CREDITS")
        print("3 QUIT")
        bracket()
        choice = input("\n> ")

        # 1 NEW GAME
        if choice == "1":
            clear()
            print("What is your name adventurer?")
            NAME = input("\n> ")

            while role_select:
                clear()
                print(f"Select your class {NAME}. \n")
                role = input("1 Warrior \n2 Mage \n3 Rogue \n\n> ")
                print()
                
                if role == "1": #Description of the role
                    clear()
                    Warrior_asci()
                    print()
                    class_banner()
                    print("Strong and sturdy. His special ability \nallows him to heal his HP to the maximum.") 
                    class_banner()
                    
                elif role == "2": #Description of the role
                    clear()
                    Mage_asci()
                    print()
                    class_banner()
                    print("You don't need muscles... \nwhen you can toss flames at your enemies!") 
                    class_banner()
                    
                elif role == "3": #Description of the role
                    clear()
                    Rogue_asci()
                    print()
                    class_banner()
                    print("Cunning and sneaky. \nDo not leave your wallet \nwhen he is around. Also, good with knives.") 
                    class_banner()

                else: # <-- Makes sure if the input is wrong you will have to select again
                    continue 

                decision = input("\nAre you sure? \n\n1 Yes \n2 No \n\n>")

                if decision == "1": #Choice confirmation
                    role_select = False

                    if role == "1":
                        Warrior()

                    elif role == "2":
                        Mage()

                    elif role == "3":
                        Rogue()

            menu = False
            play = True
            clear()
            print("Loading...")
            time.sleep(2)                  
                    
        # 2 CREDITS            
        elif choice == "2": 
            clear()
            credits()
            input("\n> ")
             
        # 3 QUIT
        elif choice == "3":
            clear()
            print("Thank you for playing the game. We hope you enjoyed it")
            input("\n> ")
            menu = False
            run = False
    
    # GAME ON
    while play:  
        clear()
        display_stats()
        input("\n> ")
        
        # 1st Location RZ
        while location == "Start":
            clear()
            introduction()
            
            while talking:
                print(f"Are you up for the quest? \n\n"
                      f"{NAME} the {role}:\n\n"
                      "1 You can count on me strange old man! \n"
                      "2 Thank you but I will have to pass on this one.")
                quest_choice = input("\n> ")

                if quest_choice == "1" and interaction == 1:
                    print("\nStranger: Great! Like my uncle used to say - 'Roland, remember \nif you can't achieve something using your brain, use your muscles.'")

                elif quest_choice == "1" and interaction == 2:
                    print("\nStranger: Marvelous! My name is Roland. I hope you know know some other spells than fireball. \n" 
                          "A wise man once said: A fire can not kill the dragon.")

                elif quest_choice == "1" and interaction == 3:
                    print(f"\nStranger: Excellent! Just make sure not to backstab me later, ha ha! I am Roland by the way")

                elif quest_choice == "2":
                    print(f"\n{NAME}: Mamma said not to trust strangers. Bye.")
                    input("\n> ")
                    clear()
                    quit()

                else:
                    clear()
                    print("[Please select a valid option]\n")
                    continue
                print("Let's go then. There is no time to waste.")
                location = "Road"    
                talking = False
                input("\n> ")
                clear()

        # 2nd Location RZ
        while location == "Road":
            
            talking = True
            while talking:
                crossroads()
                road = input("\n1 Paved road \n2 Forest path \n3 Leave  \n\n> ")
                
                if road == "1": # -> 3rd Location option A
                    location = "Paved road"
                    
                elif road == "2": # -> 3th Location option B
                    location = "Forest path"
                    
                elif road == "3": # Quit
                    print("Maybe it's for the best. Adventuring isn't for everyone...")
                    time.sleep(3)
                    clear()
                    quit()
                    
                else: # Loop
                    clear()
                    continue
                talking = False

        # 3rd Location - A RZ
        while location == "Paved road":
            clear()
            print("As you march on a track you see the sun sets behind the horizon")
            input("\n> ")
            print("\nAlthough it is not so difficult to follow this path you find yourself tripping occasionally. \nRoland notices this and asks you:")
            talking = True
            while talking:
                torch = input("Do you wish to light up the torch? \n\n1 Yes \n2 No \n\n> ")
                print("\n")
                
                if torch == "1":
                    ambush_chance = 1
                elif torch == "2":
                    ambush_chance = random.randint(1,2)
                else:
                    clear()
                    continue

                if torch == "1" and interaction == 1:
                    print("You rip a piece of clothing and wrap it around a stick you picked up from a side of the road \nand set it on fire")
                elif torch == "1" and interaction == 2:
                    print("You reach with your hand and snap your fingers creating a spark that turns into \na flame that you hold seemingly without getting hurt.")
                    input("\n> ")
                    print("Roland: Oh well... Fireball it is.")
                elif torch == "1" and interaction == 3:
                    print("You nod and see as Roland lights up a torch \nRoland: Good choice. I was starting to struggle a bit here.")
                    
                elif torch == "2" and interaction == 1:
                    print("You don't fear darkness. It is darkness that should fear you.")
                elif torch == "2" and interaction == 2:
                    print(f"{NAME}: I am no fool. This road is not safe \nand we don't want to bring unwanted attention.\n")
                    input("\n> ")
                    print("\nRoland: Fair point")
                elif torch == "2" and interaction == 3:
                    print(f"{NAME}: it is not safe to walk around with a torch on these tracks. \nI don't want to get robbed.\n")
                    input("\n> ")
                    print(f"\nRoland to himself: Ironic...")

                talking = False

            input("\n> ")
            clear()
            print("Night")
            input("\n> ")
            
            # Ambush
            if ambush_chance == 1:
                print("Suddenly you hear a noise. \n\nRoland: Who goes there?")
                input("\n> ")
                clear()
                print("3 thugs jump from the bushes nearby holding their knifes pointed at you two")
                input("\n> ")
                clear()
                talking = True
                while talking:
                    print("Bandit: Well, well, well... What do we have here?\n")
                    print(f"1 {NAME}: We are not looking for trouble.")
                    print(f"2 {NAME}: Someone who can kill you faster than you can say 'apple juice'")
                    if interaction == 1:
                        print("3 Jump at them before they can react")
                    elif interaction == 2:
                        print("3 Hit the ground with your staff.")
                    elif interaction == 3:
                        print(f"3 {NAME}: Easy there. Don't you see I am one of you?")
                    bandit_choice = input("\n> ")
                    clear()
                    if bandit_choice == "1": # Escape or Fight
                        gold = True
                        while gold:
                            print("Bandit: You don't mind giving us your gold then, do you?\n")
                            gold_choice = input("1 Give the gold. \n2 Draw your weapon.\n\n> ")

                            if gold_choice == "1": # Escape
                                print("Bandit: There you go, that wasn't so difficult.\n\nThey walk away with your gold")
                                input("\n> ")
                                clear()
                                gold = False
                                talking = False

                            elif gold_choice == "2": # Fight
                                print("\nBandit: Wrong Choice my friend! \nGet them!")
                                fight = True
                                input("\n> ")
                                battle(bandits)
                                gold = False
                                talking = False

                            else: # Loop
                                clear()
                                continue
                            
                    elif bandit_choice == "2": #Fight
                        print("\nBandit: We will see about that!")
                        fight = True
                        input("\n> ")
                        battle(bandits)
                        talking = False
                        
                    elif bandit_choice == "3" and interaction == 1: # Warrior Fight
                        print("Bandit: Aaaagh! You bastard!")
                        fight = True
                        input("\n> ")
                        battle(bandits)
                        talking = False
                    
                    elif bandit_choice == "3" and interaction == 2: # Mage Escape
                        print("You hit the ground and a shockwave sends these thugs flying back into the bushes. \nThat gives you time to escape")
                        talking = False
                        
                    elif bandit_choice == "3" and interaction == 3: # Rogue Escape
                        print("Bandit: Oh! Pardon me. \n\nYou pass by giving them a 'stare'")
                        talking = False                       
                

            print("You continue traveling and soon see your goal from afar...")    
            input("\n> ")
            clear()
            location = 'cave'

        # 3rd Location - B JM
        while location == "Forest path":
            clear()
            print("Forest path\n")
            torch = input("\nAfter following the forest path for a couple of hours, you realize the light is fading as the sun is setting..\n\n" 
                      "1 Find a way to light the path\n"
                      "2 Go through the darkness\n\n> ")
            
            random_value = random.randint(1,3)
            damage = random.randint(1,3)
            
            if torch == "1":
                clear()
                if interaction == 1:
                    print("You fashion a crude torch from a big branch and a ripped piece of your clothing..")
                    print("Roland: Nice work chump, this will guide the way.")
                    input("\n> ")
                    if random_value == 1:
                        HP -= damage
                        print("After a minute Roland realizes that you have been setting the dry withering branches of the trees on fire")
                        print("You throw the torch and both start running, but cant help but stumble a along the narrow winding path")
                        print("After outrunning the raging forestfire, you luckily arrive at the cave")
                        input("\n> ")
                        print("Before entering you assess your bruises and scrapes.")
                        print("You lost-" + str(damage), " Hp.")
                        print("You have " +str(HP), "/ " +str(HP_MAX), "HP left")
                        input("\n> ")
                        clear() 
                        location = "cave"

                    else:
                        print("The crude torch burns brightly and the path soon leads you to the cave") 
                        input("\n> ")
                        clear()
                        location = "cave"
                    
                elif interaction == 2:
                    print("You conjure a flame in your hand and hold it out infront of you to light up the path..")
                    print("Roland: Neat - This must be a handy skill to master")
                    input("\n> ")
                    if random_value == 1:
                        HP -= damage 
                        print("After a long hike, you find a clearing and some decent looking resting spots.\nYou sit down and rest your eyes for a minute")
                        input("\n> ")
                        print("You are awoken to the alarming sound of Roland screaming the word BEEEEAAAR!")
                        print("The bear is sniffing you up and down. You jump up, and almost escape the bears lunging claws!")
                        print("As you run for your lives you arrive at the cave")
                        input("\n> ")
                        print("The bear managed to scratch your upper arm. You assess the damage.")
                        print("You have lost -" + str(damage), " Hp.")
                        print("You have " +str(HP), "/ " +str(HP_MAX), "HP left")
                        input("\n> ")
                        clear()
                        location = "cave"
                        
                else:
                    print("You skillfully craft a torch, using the resources that surrounds you.")
                    print("Roland: Heres the matches boy. Lets get the torch burning before the sun goes all the way down!")
                    input("\n> ")
                    if random_value == 1:
                        HP -= damage 
                        print("The torch burned out much earlier than anticipated and you are left in the darkness surrounded by thorny bushes.")
                        input("\n> ")
                        print("You struggle to make progress, as mud slows you down and the prickly bushes tear at your skin and clothes...")
                        print("Very displeased, Roland scuffs at you, as you finally make it out of the thorny bushes and arrive at the cave")
                        input("\n> ")
                        print("You assess the cuts, and have lost " + str(damage), " hp")
                        print("You have " +str(HP), "/ " +str(HP_MAX), "HP left")
                        input("\n> ")
                        clear() 
                        location = "cave"
                    else:
                        print("The path leads you though dense thorny bushes.. Thank god I have the torch you think to yourself.")
                        input("\n> ")
                        clear()
                        location = "cave"
           
        
        
            elif torch == "2":
                clear()
                
                if interaction == 1:
                    print("You ready yourself with patience and allow your eyes to adapt to the darkness..\n")
                    print("Roland: It will be a loong night")
                    input("\n> ")
                    if random_value == 1:
                        print("The bright moon shines from a cloudless sky, making the path visible in the night..")
                        print("You walk in silence the entire night, but enjoy the company of Roland")
                        input("\n> ")
                        print("After a long night of walking you finally reach the cave")
                        input("\n> ")
                        clear() 
                        location = "cave"
                    else:
                        HP -= damage
                        print("The treacherous pathway with roots, branches and mud kept you both stumbling through the night.") 
                        input("\n> ")
                        print("Upon arriving at the cave you assess your health. You lost " + str(damage), " hp.")
                        print("You have " +str(HP), "/ " +str(HP_MAX), "HP left")
                        input("\n> ")
                        clear()
                        location = "cave"
                    
                elif interaction == 2:
                    print("As dusk turned into night you prepared for the worst...")
                    print("Roland: It will be a loong night")
                    input("\n> ")
                    if random_value == 1:
                        print("Your journey through the forest was accompanied by fireflies which faintly lit up the nearst bits of the path.")
                        print("You walk in silence the entire night, but enjoy the company of Roland and the fireflies")
                        input("\n> ")
                        print("After walking the entire night, you arrive at the cave")
                        input("\n> ")
                        clear() 
                        location = "cave"
                    else:
                        HP -= damage
                        print("You make it to the cave, Roland laughing so much he can barely catch his breath..")
                        print("Somewhere along the way you stepped in a pool of mud and slipped.\nThe landing must have been on a stone because it hurts like hell and now you walk with a limp!")
                        input("\n> ")
                        print("After cleaning your clothing you assess your health. You lost " + str(damage), " hp.")
                        print("You have " +str(HP), "/ " +str(HP_MAX), "HP left")
                        input("\n> ")
                        clear()
                        location = "cave"
                        
                        
                else:
                    print("You put on your hood, becoming one with the night - Your senses sharpen and you breathe lightly..")
                    print("You whisper to Roland: 'walk in my steps'. Roland grunts distrustful..")
                    input("\n> ")
                    if random_value == 1:
                        print("You feel the path with each step, correcting your direction as soon as you step of the path.")
                        input("\n> ")
                        print("The journey took a lot of energy but you made it to the cave")
                        input("\n> ")
                        clear() 
                        location = "cave"
                    else:
                        HP -= damage 
                        print("The path leads you though dense thorny bushes, mud and waist deep waters..")
                        print("Roland, fighting his urge to scream, mutters below his breath: 'So much for following your steps, you incompetent fool!'")
                        input("\n> ")
                        print("You made it to the cave where you stop to clean your clothes, remove leeches, and assess your health. You have lost " + str(damage), " hp")
                        print("You have " +str(HP), "/ " +str(HP_MAX), "HP left")
                        input("\n> ")
                        clear()
                        location = "cave"
                
            else:
                clear()
                continue

        # 4th Location - JM
        while location == "cave":
            Dragon()
            boss_monologue()
            fight = True
            
            #Boss battle            
            while fight:    
                clear()
                display_stats()
                vs_banner()
                display_dragon_stats()
                print("\n\n")
                print("1 Attack")
                print("2 Dodge")
                #if spec_count > 0:    #i commented out the if statement here, and removed indentation in the next line, because i handle the case in the code below.
                print("3 Special")
                print("4 Run")
                fight_choice = input("\n> ")
                
                player_damage = random.randint(ATK/2, ATK)
                dragon_damage = random.randint(atk_dragon/2, atk_dragon)
                player_miss = random.randint(1, chance)

                # Attack                    
                if fight_choice == "1":

                    if player_miss == 1:
                        HP -= dragon_damage
                        print("Oh Dear..! You missed...")

                    elif player_miss == chance:
                        hp_dragon -= player_damage * 2
                        print("You hit your target with a powerful strike, staggering the opponent for a brief period")
                        print("You dealt " + str(player_damage*2), " hp.")
                        print("The dragon has " +str(hp_dragon), "/ " +str(hp_max_dragon), "HP left")
                        input("\n> ")
                        clear()
                        check_health()
                        continue #if we dont like the dragon to be staggered upon crit just remove this continue...

                    else:
                        hp_dragon -= player_damage
                        atk = random.choice(attacks)
                        print("You hit your target")
                        print("You dealt " + str(player_damage), " hp.")
                        print("The dragon has " +str(hp_dragon), "/ " +str(hp_max_dragon), "HP left")
                        input("\n> ")
                        check_health()

                    HP -= dragon_damage
                    atk = random.choice(attacks)    
                    print(f"The dragon attacks you with {atk}!")
                    print("You lost " + str(dragon_damage), " HP.")
                    print("You have " +str(HP), "/ " +str(HP_MAX), "HP left")
                    input("\n> ")
                    clear()
                    check_health()
                    continue

                # Dodge
                elif fight_choice == "2":
                    if player_miss == 1:
                        hp_dragon -= player_damage/2
                        print("You taunt the dragon, awaiting its attack")
                        print("As the dragon attacks, you dodge and manage to land a weak attack")
                        print("You dealt " + str(player_damage/2), " hp.")
                        input("\n> ")
                        clear()
                        check_health()
                        continue
                        
                    else:
                        HP -= dragon_damage
                        attack = random.choice(attacks)
                        print("You taunt the dragon, awaiting its attack")
                        print(f"The dragon attacks you with a strong {attack}!")
                        print("You failed to dodge the attack")
                        print("You lost " + str(dragon_damage), " hp.")
                        print("You have " +str(HP), "/ " +str(HP_MAX), "HP left")
                        input("\n> ")
                        clear()
                        check_health()
                        continue

                # Special                       
                elif fight_choice == "3":
                    if interaction == 1 :
                        if spec_count > 0:
                            spec_count -= 1
                            HP = HP_MAX
                            print("You emptied the entire health potion, and regained full health!")
                            print("With confidence you throw the empty bottle at the floor, shattering it to tiny pieces")
                            print("You have " +str(HP), "/ " +str(HP_MAX), "HP left")
                            input("\n> ")
                            #continue #Dragon will attack after you use heal - i 
                        else:
                            print("The bottles are shattered, you must go on without them!")
                            input("\n> ")
                            clear()
                            check_health()
                            continue
                            
                    if interaction == 2:  
                        if spec_count > 0:
                            spec_count -= 1
                            hp_dragon -= spec
                            print("You focus all your mana into a giant fireball, which you hurl in the face of the dragon.\n It didnt expect it at all!")
                            print(f"You dealt {spec} damage.")
                            print("You wont be able to focus that much mana again, it took a great toll on your powers...")
                            print("The dragon has " +str(hp_dragon), "/ " +str(hp_max_dragon), "HP left")
                            input("\n> ")
                            clear()
                            check_health()
                            #continue #Stagger was removed, dragon will attack after special
                        else:
                            print("You're unable to focus such attack again...")
                            input("\n> ")
                            clear()
                            continue
                            
                    if interaction == 3: 
                        if spec_count > 0:
                            spec_count -= 1
                            knives = random.randint(0, 3)
                            print("Rogue throws 3 knives!\n")
                            if knives == 0:
                                print("Knives fly and miss the target... \nDon't worry. It happens even to the best. And since you are the best \nit happens to you all the time.")
                                input("\n> ")
                                clear()
                                check_health()
                                #continue #dragon will attack after failed special
                            else:
                                hp_dragon -= spec * knives
                                print("You spot a weakness and in a quick elegant move throw your knives as hard as you can directly at it!")
                                print(f"{knives} hit the target dealing {knives*spec} damage!\n")
                                print("The knives are properly stuck in the dragons neck, no chance of getting them back!")
                                print("The dragon has " +str(hp_dragon), "/ " +str(hp_max_dragon), "HP left")
                                input("\n> ")
                                #continue #Stagger was removeed, dragon will attack after special

                        else:
                            print("All your knives are either embedded deep in the dragons neck or lost somewhere far behind it. You wont get them back while its alive!")
                            input("\n> ")
                            clear()
                            check_health()
                            continue

                    HP -= dragon_damage
                    atk = random.choice(attacks)    
                    print(f"The dragon attacks you with {atk}!")
                    print("You lost " + str(dragon_damage), " HP.")
                    print("You have " +str(HP), "/ " +str(HP_MAX), "HP left")
                    input("\n> ")
                    clear()
                    check_health()
                    continue

                # Run                        
                elif fight_choice == "4":
                    print("You try to distract the dragon to make an escape...")
                    escape = random.randint(1, 10)
                    
                    if interaction == 1:
                        print("You make an immense amount of noise with your sword and shield...")
                        if escape == 1:
                            print("You managed to use your sword and shield to create an intense amount of noise that echoed of the walls")
                            print("While the dragon was distracted you managed to sneak into safety!")
                            print("Thanks for playing our game!")
                            credits()
                        else:
                            HP -= (escape - AMR)
                            print("The dragon ignored your pathetic attempt, and smacked you into a pillar")
                            print("You suffered " + str(escape), " damage.")
                            print("You have " +str(HP), "/ " +str(HP_MAX), "HP left")
                            input("\n> ")
                            clear()
                            check_health()
                            continue
                            
                    if interaction == 2:
                        print("You start saying the incantation for a magic spell...")
                        if escape == 1:
                            print("You managed to use your magic to create illusions of yourself")
                            print("While the dragon was distracted you managed to sneak into safety!")
                            print("Thanks for playing our game!")
                            credits()

                        else:
                            HP -= (escape - AMR)
                            print("The dragon ignored your puny magic, and smacked you into the ground.")
                            print("You suffered " + str(escape), " damage.")
                            print("You have " +str(HP), "/ " +str(HP_MAX), "HP left")
                            input("\n> ")
                            clear()
                            check_health()
                            continue
                            
                    if interaction == 3:
                        print("You grab a small object from a pouch attached to you belt...")
                        if escape == 1:
                            print("You used a smoke grenade to distract the dragon as you take cover in the shadows")
                            print("While the dragon was distracted you managed to sneak into safety!")
                            print("Thanks for playing our game!")
                            credits()

                        else:
                            HP -= (escape - AMR )
                            print("The dragon anticipated your little trick, and tossed you across the room before you could move a muscle.")
                            print("You suffered " + str(escape), " damage.")
                            print("You have " +str(HP), "/ " +str(HP_MAX), "HP left")
                            input("\n> ")
                            clear()
                            check_health()
                            continue
                                
            fight = False