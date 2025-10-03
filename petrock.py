hunger = 0
happiness = 0
health = 0
age = 0
name = ""
is_alive = True
anger = 0
cleanliness = 0
boredom = 0
thirst = 0
energy = 0
weight = 0
mood = ""
name = input("What would you like to name your pet rock? ")
partner_name = "lorem ipsum"
def gamestart():
    global name
    if name == "PetRock":
        print("You cannot name your pet rock 'PetRock'. Please choose a different name.")
        name = input("What would you like to name your pet rock? ")
    elif name == "petrock":
        print("You cannot name your pet rock 'petrock'. Please choose a different name.")
        name = input("What would you like to name your pet rock? ")
    elif name == "PETROCK":
        print("You cannot name your pet rock 'PETROCK'. Please choose a different name.")
        name = input("What would you like to name your pet rock? ")
    elif name == "":
        print("You cannot leave the name blank. Please choose a different name.")
        name = input("What would you like to name your pet rock? ")
    elif name == "Sauron":
        print("You have named your pet rock 'Sauron' It has became the Dark Lord.")
        print("Game Over.")
        return
    elif name == "sauron":
        print("You have named your pet rock 'sauron' It has became the Dark Lord.")
        print("Game Over.")
        return
    elif name == "SAURON":
        print("You have named your pet rock 'SAURON' It has became the Dark Lord.")
        print("Game Over.")
        return
    elif name == "Gandalf":
        print("You have named your pet rock 'Gandalf' It has invoked the power of Gandalf!")
        print("Gandalf has declared that your pet rock shall not pass!")
        print("Game Over.")
        return
    elif name == "gandalf":
        print("You have named your pet rock 'gandalf' It has invoked the power of Gandalf!")
        print("Gandalf has declared that your pet rock shall not pass!")
        print("Game Over.")
        return
    elif name == "GANDALF":
        print("You have named your pet rock 'GANDALF' It has invoked the power of Gandalf!")
        print("Gandalf has declared that your pet rock shall not pass!")
        print("Game Over.")
        return
    for is_alive in [True]:
        print(f"{name}'s current stats are:")
        print(f"Hunger: {hunger}")
        print(f"Happiness: {happiness}")
        print(f"Health: {health}")
        print(f"Age: {age}")
        print(f"Anger: {anger}")
        print(f"Cleanliness: {cleanliness}")
        print(f"Boredom: {boredom}")
        print(f"Thirst: {thirst}")
        print(f"Energy: {energy}")
        print(f"Weight: {weight}")
        print(f"Mood: {mood}")
        if mood == "doomed":
            print(f"{name} looks very sad and hopeless.")
        if mood == "happy":
            print(f"{name} looks very happy and content.")
        if mood == "sad":
            print(f"{name} looks very sad and depressed.")
        if mood == "angry":
            print(f"{name} looks very angry and frustrated.")
        if mood == "confused":
            print(f"{name} looks very confused and disoriented.")
        if mood == "mind-boggled":
            print(f"{name} looks very mind-boggled and perplexed.")
        if mood == "romantic":
            print(f"{name} looks very romantic and lovestruck.")
        if mood == "excited":
            print(f"{name} looks very excited and thrilled.")
        if mood == "magical":
            print(f"{name} looks very magical and enchanted.")
        if mood == "epic":
            print(f"{name} looks very epic and heroic.")
        if mood == "GPTed":
            print(f"{name} looks very intelligent and wise.")
        if mood == "mood":
            print(f"{name} looks very {mood}.")
        action = input("What would you like to do? (feed, play, clean, drink, rest, check stats, quit)").lower()
        if action.lower() == "feed":
            feed()
        elif action.lower() == "play":
            play()
        elif action.lower() == "clean":
            clean()
        elif action.lower() == "drink":
            drink()
        elif action.lower() == "rest":
            rest()
        elif action.lower() == "read":
            read()
        elif action.lower() == "punish":
            punish()
        elif action.lower() == "nuke":  
            nuke()
        elif action.lower() == "run doom on rock":
            rundoomonrock()
        elif action.lower() == "github":
            github()
        elif action.lower() == "hvitur":
            hvitur()
        elif action.lower() == "abandon":
            abandon()
        elif action.lower() == "rename":
            rename()
        elif action.lower() == "slap":
            slap()
        elif action.lower() == "hug":
            hug()
        elif action.lower() == "meditate":
            meditate()
        elif action.lower() == "throw":
            throw()
        elif action.lower() == "chisel":
            chisel()
        elif action.lower() == "roll":
            roll()
        elif action.lower() == "reducto":
            reducto()
        elif action.lower() == "accio": 
            accio()
        elif action.lower() == "use to sharpen sword":
            usetosharpensword()
        elif action.lower() == "find partner":
            findpartner()
        elif action.lower() == "teach":
            teach()
        elif action.lower() == "mud bath":
            mudbath()
        elif action.lower() == "sunbathe":
            sunbathe()
        elif action.lower() == "pou":
            pou()
        elif action.lower() == "visit doctor":
            visitdoctor()
        elif action.lower() == "angry birds":
            angrybirds()
        elif action.lower() == "watch movie":
            watchmovie()
        elif action.lower() == "gandalf":
            gandalf()
        elif action.lower() == "voldemort":
            voldemort()
        elif action.lower() == "curse":
            curse()
        elif action.lower() == "gpt":
            gpt()
        elif action.lower() == "secret":
            secret()
        elif action.lower() == "avada kedavra":
            avadakedavra()
        elif action.lower() == "sauron":
            sauron()
        elif action.lower() == "list easter eggs":
            listeastereggs()
        elif action.lower() == "check stats":
            check_stats()
        elif action.lower() == "quit":
            print(f"Goodbye! Thanks for taking care of {name}.")
            break
        else:
            print("Invalid action. Please try again.")
def sauron():
    global is_alive
    is_alive = False
    print("You have summoned Sauron!")
    print("He has taken over your pet rock.")
    print("Game Over.")
    return
def feed():
    global hunger, happiness, health, anger, weight
    hunger += 10
    happiness += 5
    health += 2
    anger -= 1
    weight += 1
    print(f"You fed {name}. Hunger is now {hunger}, Happiness is now {happiness}, Health is now {health}, Anger is now {anger}, Weight is now {weight}.")
def play():
    global happiness, boredom, anger, energy, hunger, thirst
    happiness += 10
    boredom -= 5
    anger -= 2
    energy -= 3
    hunger -= 1
    thirst -= 1
    print(f"You played with {name}. Happiness is now {happiness}, Boredom is now {boredom}, Anger is now {anger}, Energy is now {energy}.")
def clean():
    global cleanliness, health, happiness
    cleanliness += 10
    health += 5
    happiness += 2
    print(f"You cleaned {name}. Cleanliness is now {cleanliness}, Health is now {health}, Happiness is now {happiness}.")
def drink():
    global thirst, health, energy
    thirst += 10
    health += 3
    energy += 2
    print(f"You gave {name} a drink. Thirst is now {thirst}, Health is now {health}, Energy is now {energy}.")
def rest():
    global energy, health, boredom
    energy += 10
    health += 2
    boredom -= 3
    print(f"{name} rested. Energy is now {energy}, Health is now {health}, Boredom is now {boredom}.")
def read():
    global happiness, boredom, anger
    happiness += 5
    boredom -= 2
    anger -= 1
    print(f"You read to {name}. Happiness is now {happiness}, Boredom is now {boredom}, Anger is now {anger}.")
def punish():
        global anger, happiness, health
        anger += 5
        happiness -= 5
        health -= 2
        print(f"You punished {name}. Anger is now {anger}, Happiness is now {happiness}, Health is now {health}.")
def nuke():
    global is_alive
    is_alive = False
    print(f"You have chosen to nuke {name}.")
    print(f"{name} has been destroyed.")
    print("Game Over.")
    return
def rundoomonrock():
    global is_alive
    is_alive = False
    print(f"You have chosen to run Doom on {name}.")
    print(f"{name} has been overwhelmed by the power of Doom.")
    print("Game Over.")
    return
def github():
    global is_alive
    is_alive = False
    print(f"You have chosen to push {name} to GitHub.")
    print(f"{name} has been lost in the vastness of the internet.")
    print("Game Over.")
    return
def hvitur():
    global name
    print(f"You have chosen to hvitur {name}.")
    print(f"{name} has been turned into a white rock. It is now {name} the White.")
    name = name + " the White"
    return
def abandon():
    global is_alive
    is_alive = False
    print(f"You have chosen to abandon {name}.")
    print(f"{name} has been left alone.")
    print("Game Over.")
    return
def rename():
    global name
    if "the white" in name.lower():
        print(f"{name} uses the power of the White Wizard to block your name change.")
    else:
        new_name = input("What would you like to rename your pet rock? ")
        name = new_name
        print(f"Your pet rock has been renamed to {name}.")
def slap():
    global anger, health, happiness
    anger += 5
    health -= 5
    happiness -= 5
    print(f"You slapped {name}. Anger is now {anger}, Health is now {health}, Happiness is now {happiness}.")
def hug():
    global happiness, health, anger
    happiness += 5
    health += 2
    anger -= 2
    print(f"You hugged {name}. Happiness is now {happiness}, Health is now {health}, Anger is now {anger}.")
def meditate():
    global health, anger, happiness
    health += 5
    anger -= 5
    happiness += 2
    print(f"You meditated with {name}. Health is now {health}, Anger is now {anger}, Happiness is now {happiness}.")  
def throw():
    global anger, health, happiness
    anger += 10
    health -= 10
    happiness -= 10
    print(f"You threw {name}. Anger is now {anger}, Health is now {health}, Happiness is now {happiness}.")
def chisel():
    global health, happiness, anger
    health -= 5
    happiness -= 5
    anger += 5
    print(f"You chiseled {name}. Health is now {health}, Happiness is now {happiness}, Anger is now {anger}.")
def roll():
    global happiness, boredom, anger
    happiness += 5
    boredom -= 5
    anger -= 2
    print(f"You rolled {name}. Happiness is now {happiness}, Boredom is now {boredom}, Anger is now {anger}.")
def reducto():
    global health, happiness, anger
    health -= 10
    happiness -= 10
    anger += 10
    print(f"You cast reducto on {name}. Health is now {health}, Happiness is now {happiness}, Anger is now {anger}.")
def accio():
    global happiness, boredom, anger
    happiness += 10
    boredom -= 10
    anger -= 5
    print(f"You cast accio on {name}. Happiness is now {happiness}, Boredom is now {boredom}, Anger is now {anger}.")
def usetosharpensword():
    global health, happiness, anger
    health += 5
    happiness += 5
    anger -= 5
    print(f"You used to sharpen sword on {name}. Health is now {health}, Happiness is now {happiness}, Anger is now {anger}.")
def findpartner():
    global happiness, boredom, anger, partner_name, partnerstats
    if partner_name!= "lorem ipsum":
        print("You already have a partner for your pet rock.")
    else:
        partner_name = input("What is the name of the partner you found for your pet rock? ")
        print(f"You found a partner for {name}. Happiness is now {happiness}, Boredom is now {boredom}, Anger is now {anger}.")
    
    partnerstats={"hunger":0,"happiness":10,"health":5,"age":0,"anger":-5,"cleanliness":5,"boredom":-10,"thirst":0,"energy":5,"weight":0,"mood":"happy"}
    happiness += 20
    boredom -= 10
    anger -= 5
    
def teach():
    global happiness, boredom, anger
    happiness += 5
    boredom -= 5
    anger -= 2
    print(f"You taught {name}. Happiness is now {happiness}, Boredom is now {boredom}, Anger is now {anger}.")
def mudbath():
    global cleanliness, health, happiness
    cleanliness -= 10
    health += 5
    happiness += 2
    print(f"You gave {name} a mud bath. Cleanliness is now {cleanliness}, Health is now {health}, Happiness is now {happiness}.")
def sunbathe():
    global health, happiness, energy
    health += 5
    happiness += 5
    energy += 5
    print(f"You let {name} sunbathe. Health is now {health}, Happiness is now {happiness}, Energy is now {energy}.")
def pou():
    global happiness, boredom, anger
    happiness += 10
    boredom -= 10
    anger -= 5
    print(f"You played Pou with {name}. Happiness is now {happiness}, Boredom is now {boredom}, Anger is now {anger}.")
def visitdoctor():
    global health, happiness, anger
    health += 10
    happiness += 5
    anger -= 5
    print(f"You took {name} to the doctor. Health is now {health}, Happiness is now {happiness}, Anger is now {anger}.")
def angrybirds():
    global happiness, boredom, anger
    happiness += 5
    boredom -= 5
    anger -= 2
    print(f"You played Angry Birds with {name}. Happiness is now {happiness}, Boredom is now {boredom}, Anger is now {anger}.")
def watchmovie():
    global happiness, boredom, anger, mood
    movie = input("What movie would you like to watch with your pet rock? ")
    if movie.lower() == "inception":
        global happiness, boredom, anger
        happiness += 10
        boredom -= 10
        anger -= 5
        mood = "mind-boggled"
        print(f"You watched Inception with {name}. Happiness is now {happiness}, Boredom is now {boredom}, Anger is now {anger}.")
    else:
        if movie.lower() == "the room":
            happiness += 5
            boredom -= 5
            anger -= 2
            mood = "confused"
            print(f"You watched The Room with {name}. Happiness is now {happiness}, Boredom is now {boredom}, Anger is now {anger}.")
        else: 
            if movie.lower() == "titanic":
                happiness += 7
                boredom -= 7
                anger -= 3
                mood = "romantic"
                print(f"You watched Titanic with {name}. Happiness is now {happiness}, Boredom is now {boredom}, Anger is now {anger}.")
            else:
                if movie.lower() == "avengers":
                    happiness += 8
                    boredom -= 8
                    anger -= 4
                    mood = "excited"
                    print(f"You watched Avengers with {name}. Happiness is now {happiness}, Boredom is now {boredom}, Anger is now {anger}.")
                else:
                    if movie.lower() == "harry potter":
                        happiness += 9
                        boredom -= 9
                        anger -= 4
                        mood = "magical"
                        print(f"You watched Harry Potter with {name}. Happiness is now {happiness}, Boredom is now {boredom}, Anger is now {anger}.")
                    else:
                        if movie.lower() == "lord of the rings":
                            happiness += 10
                            boredom -= 10
                            anger -= 5
                            mood = "epic"
                            print(f"You watched Lord of the Rings with {name}. Happiness is now {happiness}, Boredom is now {boredom}, Anger is now {anger}.")
                        else:
                            if movie.lower() == "star wars":
                                happiness += 8
                                boredom -= 8
                                anger -= 4
                                mood = "galactic"
                                print(f"You watched Star Wars with {name}. Happiness is now {happiness}, Boredom is now {boredom}, Anger is now {anger}.")
                            else:
                                if movie.lower() == "the godfather":
                                    happiness += 7
                                    boredom -= 7
                                    anger -= 3
                                    mood = "mafia"
                                    print(f"You watched The Godfather with {name}. Happiness is now {happiness}, Boredom is now {boredom}, Anger is now {anger}.")
                                else:
                                    if movie.lower() == "pulp fiction":
                                        happiness += 6
                                        boredom -= 6
                                        anger -= 2
                                        mood = "cool"
                                        print(f"You watched Pulp Fiction with {name}. Happiness is now {happiness}, Boredom is now {boredom}, Anger is now {anger}.")
                                    else:
                                        if movie.lower() == "forrest gump":
                                            happiness += 9
                                            boredom -= 9
                                            anger -= 4
                                            mood = "inspired"
                                            print(f"You watched Forrest Gump with {name}. Happiness is now {happiness}, Boredom is now {boredom}, Anger is now {anger}.")
                                        else:
                                            print(f"You watched {movie} with {name}. It was an okay movie.")
def gandalf():
    global is_alive
    is_alive = False
    print("You have invoked the power of Gandalf!")
    print("Gandalf has declared that your pet rock shall not pass!")
    print("Game Over.")
    return
def voldemort():
    global is_alive
    is_alive = False
    print("You have summoned Voldemort!")
    print("He has cast avada kedavra on your pet rock.")
    print("Game Over.")
    return
def curse():
    global is_alive
    is_alive = False
    print("You have cursed your pet rock!")
    print("Your pet rock has turned to stone and is no longer alive.")
    print("Game Over.")
    return
def gpt():
    global happiness
    happiness += 10
    print(f"You have activated GPT mode! Happiness is now {happiness}.")
    return
def secret():
    global happiness
    happiness += 100
    print("You have discovered a secret!")
    print("Your pet rock is now extremely happy!")
    print(f"Happiness is now {happiness}.")
    return
def avadakedavra():
    global is_alive
    is_alive = False
    print("You have cast the Avada Kedavra curse!")
    print("Your pet rock has been killed instantly.")
    print("Game Over.")
    return
def check_stats():
    print(f"{name}'s current stats are:")
    print(f"Hunger: {hunger}")
    print(f"Happiness: {happiness}")
    print(f"Health: {health}")
    print(f"Age: {age}")
    print(f"Anger: {anger}")
    print(f"Cleanliness: {cleanliness}")
    print(f"Boredom: {boredom}")
    print(f"Thirst: {thirst}")
    print(f"Energy: {energy}")
    print(f"Weight: {weight}")
    print(f"Mood: {mood}")
    def non_action():
        global hunger, happiness, health, anger, cleanliness, boredom, thirst, energy
        hunger -= 1
        happiness -= 1
        health -= 1
        anger += 1
        cleanliness -= 1
        boredom += 1
        thirst -= 1
        energy -= 1
        print(f"Time passes... {name}'s stats have changed.")
    non_action()
gamestart()
def gamecontinue():
    global is_alive
    while is_alive:
        if health <= -10:
            is_alive = False
            print(f"Sadly, {name} has passed away due to poor health.")
            break
        if hunger <= -10:
            is_alive = False
            print(f"Sadly, {name} has passed away due to starvation.")
            break
        if happiness <= -10:
            is_alive = False
            print(f"Sadly, {name} has passed away due to sadness.")
            break
        if anger >= 10:
            is_alive = False
            print(f"Sadly, {name} has passed away due to anger issues.")
            break
        if cleanliness <= -10:
            is_alive = False
            print(f"Sadly, {name} has passed away due to poor hygiene.")
            break
        if boredom >= 10:
            is_alive = False
            print(f"Sadly, {name} has passed away due to extreme boredom.")
            break
        if thirst <= -10:
            is_alive = False
            print(f"Sadly, {name} has passed away due to dehydration.")
            break
        if energy <= -10:
            is_alive = False
            print(f"Sadly, {name} has passed away due to exhaustion.")
            break
        gamestart()
gamecontinue()

def listeastereggs():
    print("Easter Eggs:")
    print("1. Type 'Sauron' to summon the Dark Lord and end the game.")
    print("2. Type 'Curse' to curse your pet rock and end the game.")
    print("3. Type 'Feed' to feed your pet rock and increase its hunger.")
    print("4. Type 'Play' to play with your pet rock and increase its happiness.")
    print("5. Type 'Clean' to clean your pet rock and increase its cleanliness.")
    print("6. Type 'Drink' to give your pet rock a drink and increase its thirst.")
    print("7. Type 'Rest' to let your pet rock rest and increase its energy.")
    print("8. Type 'Check stats' to check your pet rock's current stats.")
    print("9. Type 'Nuke' to nuke your pet rock and end the game.")
    print("10. Type 'Run Doom on rock' to run Doom on your pet rock and end the game.")
    print("11. Type 'GitHub' to push your pet rock to GitHub and end the game.")
    print("12. Type 'Hvitur' to turn your pet rock into a white rock.")
    print("13. Type 'Abandon' to abandon your pet rock and end the game.")
    print("14. Type 'Rename' to rename your pet rock.")
    print("15. Type 'Slap' to slap your pet rock and increase its anger.")
    print("16. Type 'Hug' to hug your pet rock and increase its happiness.")
    print("17. Type 'Meditate' to meditate with your pet rock and increase its health.")
    print("18. Type 'Throw' to throw your pet rock and increase its anger.")
    print("19. Type 'Chisel' to chisel your pet rock and increase its anger.")
    print("20. Type 'Roll' to roll your pet rock and increase its happiness.")
    print("21. Type 'Reducto' to cast reducto on your pet rock and increase its anger.")
    print("22. Type 'Accio' to cast accio on your pet rock and increase its happiness.")
    print("23. Type 'Use to sharpen sword' to use your pet rock to sharpen a sword and increase its happiness.")
    print("24. Type 'Find partner' to find a partner for your pet rock and increase its happiness.")
    print("25. Type 'Teach' to teach your pet rock and increase its happiness.")
    print("26. Type 'Mud bath' to give your pet rock a mud bath and decrease its cleanliness.")
    print("27. Type 'Sunbathe' to let your pet rock sunbathe and increase its health.")
    print("28. Type 'Pou' to play Pou with your pet rock and increase its happiness.")
    print("29. Type 'Visit doctor' to take your pet rock to the doctor and increase its health.")
    print("30. Type 'Angry Birds' to play Angry Birds with your pet rock and increase its happiness.")
    print("31. Type 'Watch movie' to watch a movie with your pet rock and change its mood.")
    print("32. Type 'Gandalf' to invoke the power of Gandalf and end the game.")
    print("33. Type 'Voldemort' to summon Voldemort and end the game.")
    print("34. Type 'Curse' to curse your pet rock and end the game.")
    print("35. Type 'GPT' to activate GPT mode and increase your pet rock's happiness.")
    print("36. Type 'Secret' to discover a secret and greatly increase your pet rock's happiness.")
    print("37. Type 'Avada Kedavra' to cast the Avada Kedavra curse on your pet rock and end the game.")
    print("38. Type 'List easter eggs' to see this list again.")

    
    

    return
def Youshallnotpass():
    global is_alive
    is_alive = False
    print("You have invoked the power of Gandalf!")
    print("Gandalf has declared that your pet rock shall not pass!")
    print("Game Over.")
    return
