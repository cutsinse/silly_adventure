#Exercise 31B:  Make your own game!

def die(why):
    print(why, "Aaaaaaaaaand, you're dead.")

def troll():
    print("Well if you don't want to play I'll just close the game.")

def survive():
    print("Congratulations, you survived!")

def next():
    print("Congratulations, you have another adventure to go on!")

def pet():
    print("Congratulations, you found a new friend for life!")

print("Welcome to the Fairy Forest!")
print(""" In your bag, you have an apple for lunch.
Please type in the number to choose what to do.
1: Follow the forest path to the north.
2: Go east towards a clearing
3: Go south towards the river. """)

path = input(">")

if "1" in path:
    print(""" The air is clean and crisp, the sunlight speckles the ground in gold.
    You see a green fairy in a tree wave to you.  What do you do?
    1: Wave back at the fairy
    2: Throw a rock at the fairy
    3: Offer the fairy an apple.""")
    Green_Fairy = input(">")
    if "1" in Green_Fairy:
        print("""The fairy waves back and flies further north. What do you do?
        1: Follow the Fairy
        2: Climb the tree the fairy was in
        3: Sing a song""")
        Green_Fairy = input(">")
        if "1" in Green_Fairy:
            print("The fairy leads you to a surprise party!\n They hold up a sign that says:\n Congratulations, you're #1!")
        elif "2" in Green_Fairy:
            print("You climb the tree and find the fairy's nest.  Tiny, cute little baby fairy greets you and tell you they love you.")
            pet()
        elif "3" in Green_Fairy:
            print("A green bird appears and perches on your shoulder.")
            pet()
        else:
            troll()
    elif "2" in Green_Fairy:
        print("""The fairy dodges the rock, screams at you and grabs a huge spear! What do you do?
        1: Throw another rock
        2: Grab a stick from the ground
        3: Grab a sword""")
        Green_Fairy = input(">")
        if "1" in Green_Fairy:
            die("The fairy smacks the rock away and stabs you with the spear.")
        elif "2" in Green_Fairy:
            print("The fairy tries to stab you but you smack the spear away and run back into the forest.")
            survive()
        elif "3" in Green_Fairy:
            print("""You reach for your sword only to find you don't have one.
            The fairy starts laughing at you and farts out some pixie dust.
            Now you can fly!  You fly the fuck outta there.""")
            survive()
        else:
            troll()
    elif "3" in Green_Fairy:
        print("The fairy squeels in delight and burrows into the apple in your hand.  It appears to have made a house in the apple.")
        print(""" What do you do now?
        1: Put the apple in your pocket.
        2: Put the apple at the base of the three
        3: Throw the apple as hard as you can. """)
        Green_Fairy = input(">")
        if "1" in Green_Fairy:
            print("The fairy complains and rips a hole in your pocket to get out.  It then smacks you in the face and flies away.")
            survive()
        elif "2" in Green_Fairy:
            print("""The fairy calls out like a bell, and you hear a tiny chime from up above you.\nA tiny, baby fairy flys down, gives you a blue saphire and goes into the house with its parent.""")
            print("Congratulations, you won a  blue saphire!")
        elif "3" in Green_Fairy:
            die("""The apple explodes into a black, toxic dust as it hits a tree.
            The dust has a life of its own, it's coming right at you!!!""")
        else:
            troll()

elif "2" in path:
    print("The sun shines brightly down on you, too brightly actually. \nYou look down and walk forward, and notice a worn looking dagger on the ground.")
    print(""" What do you do?
    1: Walk past it
    2: Pick it up
    3: Poke it""")
    dagger = input(">")
    if "1" in dagger:
        print("""You walk a little ways past the dagger and coil of rope handing off a tree.  What do you do?
        1: Take the rope and climb the tree
        2: Take the rope and go back to the dagger.
        3: Walk past it.""")
        rope = input(">")
        if "1" in rope:
            print("""You climb the tree and look out onto a beautiful sunset.
            You feel a tug and look behind you to see a green cat with blue eyes in the tree with you, playing with the rope.""")
            pet()
        elif "2" in rope:
            print("""You walk back and pick up the dagger, and add them both to your pocket.  Suddenly, the rope and the dagger glow!
            A sign pops up out of the ground with peice of paper nailed to it.  The sign reads:
            I need a smart adventurer, come find me here. -Fugar
            The peice of paper is a map.""")
            next()
        elif "3" in rope:
            print("You continue on a lovely walk through the forest, listening to the birds chirp and the wind blowing through the trees.")
            print("Eventually you wander home to a lovely cottage home, your partner having chicken pot pie ready for dinner.")
            survive()
        else:
            troll()
    elif "2" in dagger:
        print("You pick up the dagger, it looks very old and dull, no special markings, boring wooden handle with lots of dirt on it.")
        print("""Now what?
        1: Use it to slice you palm
        2: Put in your pocket
        3: Lick it """)
        dagger = input(">")
        if "1" in dagger:
            print("Your blood drips onto the ground.  The ground beneith you gives way and you fall into a pit!")
            print("On the wall you see a sign that reads:")
            print('"Only wizards and foolish adventurers fall for that one.  Either way, the world is better off without them"')
            die("The ground above you tumbles down.....")
        elif "2" in dagger:
            print("You now have a worn looking dagger, very useful for your next adventure!")
            next()
        elif "3" in dagger:
            print("You carefully lick the dagger without cutting your tongue.  I glows a bright red, and you hear a pop.")
            print("A chest pops up out of the ground with a note nailed to the top.  It reads:")
            print("Only a skilled adventurer knows to lick the blade.  \n\tI need skilled adventurers, come find me when you're ready for your next adventure. -Baleon")
            print("Inside the chest, you find a map, and a proper sword.")
            next()
        else:
            troll()
    elif "3" in dagger:
        print("""You have poked the dagger.  Nothing happens.
        1: Poke it again.
        2: Kick it.
        3: Poke it with your other hand.""")
        dagger = input(">")
        if "1" in dagger:
            print("You hear a faint pun in the wind.")
            print(">:3")
        elif "2" in dagger:
            print("You cry out in pain, the dagger is somehow stuck to the ground, immoble, and you kick hard.  Nothing happens.")
            survive()
        elif "3" in dagger:
            print("Nothing happens.")
            survive()
    else:
        troll()
elif "3" in path:
    print("The streak flows bright and clean.  You see a cute little otter basking in the sun and lots of shells scattered about. ")
    print("""What do you do?
    1: Offer the otter the apple.
    2: Pick up sea shells and put them in your bag.
    3: Sit down to eat your apple. """)
    river = input(">")
    if "1" in river:
        print("The otter swimms over and gobbles up the apple, happy as can be!")
        print("""What do you do now?
        1: Pet the otter.
        2: Show the otter there is nothing in your bag.
        3: Consider slapping the otter, but then don't.
        """)
        river = input(">")
        if "1" in river:
            print("The otter looks pleased as punch as you pet it.  If decides to follow you home!")
            pet()
        elif "2" in river:
            print("The otter scoffs at you and swims away.  You decide to head home.")
            survive()
        elif "3" in river:
            print("The otter tilts it head at you at first, then decides to swim away.")
            print("Happy that you supressed your darkside today, you decide to head home.")
            survive()
        else:
            troll()
    elif "2" in river:
        print("""You gather up the sea shells until your bag is full.  You hear a faint clicking
         and an annoyed looking hermit crab is scuttling toward you.""")
        print("""What do you do now?
         1: Dump the shells from your bag.
         2: Offer the hermit crab one of the biggest shells from your bag.
         3:Run away""")
        crab = input(">")
        if "1" in crab:
             print("""The crab climbs the pile of shells and it clicks and scuttles at you.
             You get the distint impression it's telling you to get off it's lawn, so you go home.""")
             survive()
        elif "2" in crab:
            print("""The crab takes the shell, but still seems displeased.
            You shrug and decide to go home, leaving the cranky crab to his complaining.""")
            survive()
        elif "3" in crab:
            print("The crab tries to follow you, but you quickly outpace it.  Soon you are home, you can smell chicken pot pie")
            print("You give your partner a beautiful sea shell, they say thank you and give you a hug.")
            survive()
        else:
            troll()
    elif "3" in river:
        print("You bask in the sun as you eat your apple.  After a few minutes, you see a gem shine in the river.  It's a ruby!")
        print("""What do you do?
        1: Take the ruby
        2: Leave the ruby alone
        3: Look around""")
        ruby = input(">")
        if "1" in ruby:
            die("You pick up the shining jewel, and as soon as it is out of the water it bursts into flames!")
        elif "2" in ruby:
            print("You know better then to mess with strange jewels, so you turn around to go.  Behind you, you see a salamander.")
            print("The salamander hops on your shoulder and rides with you all the way home.")
            pet()
        elif "3" in ruby:
            print("""You look around and see a sign that says "Warning, exploding rubies".  Shocked, you pull back and run home as fast as you can!""")
            survive()
        else:
            troll()
else:
    troll()
