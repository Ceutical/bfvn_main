# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Protagonist")
define o = Character("Octavia1")

######################################

##### TRANSFORM DEFINITIONS #####


transform protagonist:
    xalign 0.0
    yalign 1.0
  
transform antagonist:
    xalign 0.95
    yalign 0.05

transform pattack:
    xalign 0.75
    yalign 0.05
    
transform aattack:
    xalign 0.15
    yalign 1.0

transform rotation:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 10
    

######################################
label startbattle:
    play music poketheme fadeout 1.0
    
    $ HP_dog = 100
    $ HP_stick = 100
    $ HP_street = 100
    $ HP_paper = 100
    $ HP_garb = 100
    $ HP_bike = 100
    $ activeHP_a = 100
    $ activeHP_b = 100
    $ active_a = ""
    $ active_o = "empty"
    $ defense = 2
    $ queued = "no"
    $ switchpoints = 0
    
    default advantage = [("dog", "paper"), ("stick","bike"), ("street","garbage")]
    default disadvantage = [("dog", "bike"), ("stick","garbage"), ("street","bike")]

    scene bg pokemon with fade
    "Du wirst herausgefordert von [o]"
    o "Hah, gegen meinen Paperknight hast du keine Chance!"
    
label switch:
    
  
    if active_a == "dog":
        $ HP_dog = activeHP_a
    elif active_a == "stick":
        $ HP_stick = activeHP_a
    elif active_a == "street":
        $ HP_street = activeHP_a

    if HP_dog <= 0 and HP_stick <= 0 and HP_street <= 0:
        jump loss
    elif HP_paper <= 0 and HP_garb <= 0 and HP_bike <= 0:
        jump win      
    else:
        "Welches Monster wirst du wählen?"
        
    
    menu:
        "Dalmatiger" if HP_dog > 0 and active_a != "dog":
            n "Hmm, Dalmatiger ist gut gegen Papiermonster, aber schlecht gegen Fahrradmonster!"
            menu:
                n "Hmm, Dalmatiger ist gut gegen Papiermonster, aber schlecht gegen Fahrradmonster!"
                "Dalmatiger in den Kampf schicken!":
                    if active_a == "stick":
                        play sound pokout
                        hide p1 pokdog
                        with moveoutleft
                    elif active_a == "street":
                        play sound pokout
                        hide p1 pokstreet
                        with moveoutleft
                    $ active_a = "dog"
                    play sound pokin
                    show p1 pokdog at protagonist
                    with moveinleft
                    p "Los Dalmatiger!"
                    $ activeHP_a = HP_dog
                    
                "Doch lieber ein anderes Monster..." if HP_stick >= 0 or HP_street >= 0:
                    jump switch
        
        "Sticky" if HP_stick > 0 and active_a != "stick":
            n "Hmm, Sticky ist gut gegen Fahrradmonster, aber schlecht gegen Müllmonster."
            menu:
                n "Hmm, Sticky ist gut gegen Fahrradmonster, aber schlecht gegen Müllmonster."
                "Sticky in den Kampf schicken!":
                    if active_a == "dog":
                        play sound pokout
                        hide p1 pokdog
                        with moveoutleft
                    elif active_a == "street":
                        play sound pokout
                        hide p1 pokstreet
                        with moveoutleft
                    $ active_a = "stick"
                    play sound pokin
                    show p1 poksticky at protagonist
                    with moveinleft
                    p "Los Sticky!"
                    $ activeHP_a = HP_stick
                    
                "Doch lieber ein anderes Monster..." if HP_dog >= 0 or HP_street >= 0:
                    jump switch
        
        "Roadeo" if HP_street > 0 and active_a != "street":
            n "Hmm, Roadeo ist gut gegen Müllmonster, aber schlecht gegen Fahrradmonster."
            menu:
                n "Hmm, Roadeo ist gut gegen Müllmonster, aber schlecht gegen Fahrradmonster."
                "Roadeo in den Kampf schicken!":
                    if active_a == "dog":
                        play sound pokout
                        hide p1 pokdog
                        with moveoutleft
                    elif active_a == "stick":
                        play sound pokout
                        hide p1 pokstreet
                        with moveoutleft
                    $ active_a = "street"
                    play sound pokin
                    show p1 pokstreet at protagonist
                    with moveinleft
                    p "Los Roadeo!"
                    $ activeHP_a = HP_street
                    
                "Doch lieber ein anderes Monster..." if HP_dog >= 0 or HP_stick >= 0:
                    jump switch
                    
        "Doch nicht wechseln..." if active_a != "":
            $ queued = "no"
            jump kampf
        
    
label kampf:
    
    $ defense += 1
    
    if queued == "yes":
        $queued = "no"
        if active_o == "paper" and HP_paper > 0:
            "Paperknight läuft an zum \"Durchstoßen\"!"
            show p2 pokpaper at aattack with move
            play sound whoosh3
            show p2 pokpaper at antagonist with move
        elif active_o == "garbage" and HP_garb > 0: 
            "Güllor explodiert in einer \"Schlammbombe\"!"
            show p2 pokgarbage at aattack with move
            play sound cardoor1
            show p2 pokgarbage at antagonist with move
        elif active_o == "bike" and HP_bike > 0:
            "Biclops ist bereit zum \"Überfahren\"!"
            show p2 pokbike at aattack with move
            play sound bikebreak
            show p2 pokbike at antagonist with move
        if (active_a, active_o) in disadvantage:
            $ randomnum = renpy.random.randint(50,70)
            "Ein kritischer Treffer!"
        elif(active_a, active_o) in advantage:
            $ randomnum = renpy.random.randint(25,30)
            "Es scheint nicht sehr effektiv zu sein."
        else:
            $ randomnum = renpy.random.randint(35,45)
            "Der Angriff sitzt."

        if defense <= 3:
            $ activeHP_a -= randomnum/2
        else:
            $ activeHP_a -= randomnum  
    
    
    if activeHP_a <=0:
        "Dein Fightemon wurde besiegt!"
        if active_a == "dog":
            play sound pokout
            hide p1 pokdog
            with moveoutleft
            $ switchpoints += 1
            $ active_a = ""
            $ HP_dog = 0
            jump switch
        elif active_a == "street":
            play sound pokout
            hide p1 pokstreet
            with moveoutleft
            $ switchpoints += 1
            $ active_a = ""
            $ HP_street = 0
            jump switch
        elif active_a == "stick":
            play sound pokout
            hide p1 poksticky
            with moveoutleft
            $ switchpoints +=1
            $ active_a = ""
            $ HP_stick = 0
            jump switch
      
    if active_o == "empty":
        play sound pokin
        show p2 pokpaper at antagonist behind p1
        with moveinright
        $ activeHP_b = HP_paper
        $ active_o = "paper"
        "[o] sendet Paperknight in den Kampf!"
    elif activeHP_b < 0 and active_o == "paper":
        $ HP_paper = 0
        show p2 pokpaper dead
        "Paperknight wurde besiegt."
        play sound pokout
        hide p2 pokpaper dead
        with moveoutright
        play sound pokin
        show p2 pokgarbage at antagonist behind p1
        with moveinright
        $ activeHP_b = HP_garb
        $ active_o = "garbage"
        o "LOS GÜLLOR!"
    elif activeHP_b < 0 and active_o == "garbage":
        $ HP_garb = 0
        show p2 pokgarbage dead
        "Güllor wurde besiegt."
        play sound pokout
        hide p2 pokgarbage dead
        with moveoutright
        play sound pokin
        show p2 pokbike at antagonist behind p1
        with moveinright
        $ activeHP_b = HP_bike
        $ active_o = "bike"
        o "Los Biclops!"
    elif activeHP_b < 0 and active_o == "bike":
        $ HP_bike = 0
        show p2 pokbike dead
        "Biclops wurde besiegt."
        hide p2 pokbike dead
        play sound pokout
        with moveoutright
        o "NEEEEEIIIIN!"
        jump switch
    else:
        "Dein Fightemon hat noch [activeHP_a] HP, der Gegner [activeHP_b]."
        "Was wirst du als nächstes tun?"
    
    

    menu:
        "Angriff":
            
            
            if active_a == "dog":
                "Dalmatiger wird agressiv mit einen \"Knochenbiss!\""
                show p1 pokdog at pattack with move
                play sound whoosh1
                show p1 pokdog at protagonist with move
            elif active_a == "stick":
                "Sticky verwendet sich für seinen \"Weitwurf!\""
                show p1 poksticky at pattack with move
                play sound whoosh1
                show p1 poksticky at protagonist with move
            else:
                "Roadeo bolstert sich auf für seinen \"Bordsteinkantenhieb!\""
                show p1 pokstreet at pattack with move
                play sound whoosh1
                show p1 pokstreet at protagonist with move 
            if (active_a, active_o) in advantage:
                $ randomnum = renpy.random.randint(50,70)
                "Ein kritischer Treffer!"
            elif(active_a, active_o) in disadvantage:
                $ randomnum = renpy.random.randint(20,30)
                "Es scheint nicht sehr effektiv zu sein."
            else:
                $ randomnum = renpy.random.randint(30,40)
                "Der Angriff sitzt."
            
            $ activeHP_b -= randomnum
            if active_o == "paper":
                $ HP_paper = activeHP_b
            elif active_o == "garbage":
                $ HP_garb = activeHP_b
            elif active_o == "bike":
                $ HP_bike = activeHP_b
        
            
            if active_o == "paper" and HP_paper > 0:
                "Paperknight läuft an zum \"Durchstoßen\"!"
                show p2 pokpaper at aattack with move
                play sound whoosh3
                show p2 pokpaper at antagonist with move
                jump dmgcalcatk
            elif active_o == "garbage" and HP_garb > 0: 
                "Güllor explodiert in einer \"Schlammbombe\"!"
                show p2 pokgarbage at aattack with move
                play sound cardoor1
                show p2 pokgarbage at antagonist with move
                jump dmgcalcatk
            elif active_o == "bike" and HP_bike > 0:
                "Biclops ist bereit zum \"Überfahren\"!"
                show p2 pokbike at aattack with move
                play sound bikebreak
                show p2 pokbike at antagonist with move
                jump dmgcalcatk
            else:
                jump kampf
        
        "Starker Angriff":

            if active_a == "dog":
                "Dalmatiger wird wild und will \"Zerfleischen!!\""
                show p1 pokdog at pattack with move
                play sound whoosh1
                show p1 pokdog at protagonist with move
            elif active_a == "stick":
                "Sticky verbiegt sich für einen \"Stockmerang\"!"
                show p1 poksticky at pattack with move
                play sound whoosh1
                show p1 poksticky at protagonist with move
            else:
                "Roadeo stellt eine Falle mit einem \"Schlagloch!\""
                show p1 pokstreet at pattack with move
                play sound whoosh1
                show p1 pokstreet at protagonist with move                
            if (active_a, active_o) in advantage:
                $ randomnum = renpy.random.randint(70,90)
                "Ein kritischer Treffer!"
            elif(active_a, active_o) in disadvantage:
                $ randomnum = renpy.random.randint(30,50)
                "Es scheint nicht sehr effektiv zu sein."
            else:
                $ randomnum = renpy.random.randint(40,60)
                "Der Angriff sitzt."
            $ activeHP_b -= randomnum
            if active_o == "paper":
                $ HP_paper = activeHP_b
            elif active_o == "garbage":
                $ HP_garb = activeHP_b
            elif active_o == "bike":
                $ HP_bike = activeHP_b
            $ activeHP_a -= 20
            
            
            if active_o == "paper" and HP_paper > 0:
                "Paperknight läuft an zum \"Durchstoßen\"!"
                show p2 pokpaper at aattack with move
                play sound whoosh3
                show p2 pokpaper at antagonist with move
                jump dmgcalcstratk
            elif active_o == "garbage" and HP_garb > 0: 
                "Güllor explodiert in einer \"Schlammbombe\"!"
                show p2 pokgarbage at aattack with move
                play sound cardoor1
                show p2 pokgarbage at antagonist with move
                jump dmgcalcstratk
            elif active_o == "bike" and HP_bike > 0:
                "Biclops ist bereit zum \"Überfahren\"!"
                show p2 pokbike at aattack with move
                play sound bikebreak
                show p2 pokbike at antagonist with move
                jump dmgcalcstratk
            else:
                jump kampf
            
        "Verteidigen":
            $ defense = 0
            
            if active_a == "dog":
                "Dalmatiger rollt sich zu einem Ball zusammen und kreiert ein Schild aus Fell!"
            elif active_a == "stick":
                "Sticky kreiert eine magische Barriere aus seinem Laub!"
            else:
                "Roadeo verwendet ein Teil seines Asphalts, um eine Mauer zu bauen!"
            
            if active_o == "paper" and HP_paper > 0:
                "Paperknight läuft an zum \"Durchstoßen\"!"
                show p2 pokpaper at aattack with move
                play sound whoosh3
                show p2 pokpaper at antagonist with move
                jump dmgcalcdef
            elif active_o == "garbage" and HP_garb > 0: 
                "Güllor explodiert in einer \"Schlammbombe\"!"
                show p2 pokgarbage at aattack with move
                play sound cardoor1
                show p2 pokgarbage at antagonist with move
                jump dmgcalcdef
            elif active_o == "bike" and HP_bike > 0:
                "Biclops ist bereit zum \"Überfahren\"!"
                show p2 pokbike at aattack with move
                play sound bikebreak
                show p2 pokbike at antagonist with move
                jump dmgcalcdef
            else:
                jump kampf
            
        
        "Wechseln" if switchpoints < 2:
            $ queued = "yes"
            jump switch


label win:
    $ win = "yes"
    "Du hast gegen [o] gewonnen!"
    "Gratulation!"
    jump endbattle

label loss:
    $ win = "no"
    "[o] hat alle deine Monster besiegt!"
    o "Wacker geschlagen, aber noch nicht gut genug!"
    jump endbattle

label dmgcalcdef:
    if (active_a, active_o) in disadvantage:
        $ randomnum = renpy.random.randint(50,70)
        "Ein kritischer Treffer!"
    elif(active_a, active_o) in advantage:
        $ randomnum = renpy.random.randint(25,35)
        "Es scheint nicht sehr effektiv zu sein."
    else:
        $ randomnum = renpy.random.randint(35,45)
        "Der Angriff sitzt."
    if defense <= 3:
        $ activeHP_a -= randomnum/2
    else:
        $ activeHP_a -= ramomnum
        
    jump kampf
    
label dmgcalcatk:
    if (active_a, active_o) in disadvantage:
        $ randomnum = renpy.random.randint(50,70)
        "Ein kritischer Treffer!"
    elif(active_a, active_o) in advantage:
        $ randomnum = renpy.random.randint(25,35)
        "Es scheint nicht sehr effektiv zu sein."
    else:
        $ randomnum = renpy.random.randint(35,45)
        "Der Angriff sitzt."
                
    if defense <= 3:
        $ activeHP_a -= randomnum/2
    else:
        $ activeHP_a -= randomnum
        
    jump kampf

label dmgcalcstratk:
    if (active_a, active_o) in disadvantage:
        $ randomnum = renpy.random.randint(50,70)
        "Ein kritischer Treffer!"
    elif(active_a, active_o) in advantage:
        $ randomnum = renpy.random.randint(25,35)
        "Es scheint nicht sehr effektiv zu sein."
    else:
        $ randomnum = renpy.random.randint(35,45)
        "Der Angriff sitzt."

    if defense <= 3:
        $ activeHP_a -= randomnum/2
    else:
        $ activeHP_a -= randomnum
            
    jump kampf
