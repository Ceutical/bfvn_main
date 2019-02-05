# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Protagonist")
define o = Character("Octavia1")

######################################

##### TRANSFORM DEFINITIONS #####


transform protagonist:
    xalign 0
    yalign 1.0
transform antagonist:
    xalign 0.95
    yalign 0.05

transform rotation:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 10
    

######################################
label startbattle:
    stop sound fadeout 1.0
    stop music fadeout 1.0
    pause 0.75
    play music poketheme fadein 1.0
    
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
    
    default advantage = [("dog", "paper"), ("stick","bike"), ("street","garbage")]
    default disadvantage = [("dog", "bike"), ("stick","garbage"), ("street","bike")]

    scene bg pokemon
    "Du wirst herausgefordert von [o]"
    
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
        "Dalmatiger" if HP_dog >= 0:
            hide pokstreet with moveoutleft
            hide poksticky with moveoutleft
            $ active_a = "dog"
            show pokdog at protagonist with moveinleft
            p "Los Dalmatiger!"
            $ activeHP_a = HP_dog
        
        "Sticky" if HP_stick >= 0:
            hide pokstreet with moveoutleft
            hide pokdog with moveoutleft
            $ active_a = "stick"
            show poksticky at protagonist with moveinleft
            p "Los Sticky!"
            $ activeHP_a = HP_stick
        
        "Roadeo" if HP_street >= 0:
            hide pokdog with moveoutleft
            hide poksticky with moveoutleft
            $ active_a = "street"
            show pokstreet at protagonist with moveinleft
            p "Los Roadeo!"
            $ activeHP_a = HP_street
        
    
label kampf:
    
    $ defense += 1
    
    if queued == "yes":
        $queued = "no"
        if active_o == "paper":
            "Paperknight läuft an zum Durchstoßen!"
        elif active_o == "garbage":
            "Güllor explodiert in einer Schlammbombe!"
        else:
            "Biclops ist bereit zum Überfahren!"
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
        jump switch
      
    if active_o == "empty":
        show pokpaper at antagonist
        $ activeHP_b = HP_paper
        $ active_o = "paper"
        "[o] sendet Paperknight in den Kampf!"
    elif activeHP_b < 0 and active_o == "paper":
        $ HP_paper = 0
        show pokpaper dead
        "Paperknight wurde besiegt."
        hide pokpaper dead with moveoutright
        show pokgarbage at antagonist with moveinright
        $ activeHP_b = HP_garb
        $ active_o = "garbage"
        o "LOS GÜLLOR!"
    elif activeHP_b < 0 and active_o == "garbage":
        $ HP_garb = 0
        show pokgarbage dead
        "Güllor wurde besiegt."
        hide pokgarbage dead with moveoutright
        show pokbike at antagonist with moveinright
        $ activeHP_b = HP_bike
        $ active_o = "bike"
        o "Los Biclops!"
    elif activeHP_b < 0 and active_o == "bike":
        $ HP_bike = 0
        show pokbike dead
        "Biclops wurde besiegt."
        o "NEEEEEIIIIN!"
        jump switch
    else:
        "Dein Fightemon hat noch [activeHP_a] HP, der Gegner [activeHP_b]."
        "Was wirst du als nächstes tun?"
    
    

    menu:
        "Angriff":

            if active_a == "dog":
                "Dalmatiger wird agressiv mit einen Knochenbiss!"
            elif active_a == "stick":
                "Sticky verwendet sich für seinen Weitwurf!"
            else:
                "Roadeo bolstert sich auf für seinen Bordsteinkantenhieb!"
                
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
                "Paperknight läuft an zum Durchstoßen!"
            elif active_o == "garbage":
                "Güllor explodiert in einer Schlammbombe!"
            else:
                "Biclops ist bereit zum Überfahren!"
                
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
        
        "Starker Angriff":

            if active_a == "dog":
                "Dalmatiger wird wild und will Zerfleischen!!"
            elif active_a == "stick":
                "Sticky verbiegt sich für einen Stockmerang!"
            else:
                "Roadeo stellt eine Falle mit einem Schlagloch!"
                
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
            $ activeHP_a -= 20
            
            
            if active_o == "paper":
                "Paperknight läuft an zum Durchstoßen!"
            elif active_o == "garbage":
                "Güllor explodiert in einer Schlammbombe!"
            else:
                "Biclops ist bereit zum Überfahren!"
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
            
        "Verteidigen":
            $ defense = 0
            
            if active_a == "dog":
                "Dalmatiger rollt sich zu einem Ball zusammen und kreiert ein Schild aus Fell!"
            elif active_a == "stick":
                "Sticky kreiert eine magische Barriere aus seinem Laub!"
            else:
                "Roadeo verwendet ein Teil seines Asphalts, um eine Mauer zu bauen!"
            
            if active_o == "paper":
                "Paperknight läuft an zum Durchstoßen!"
            elif active_o == "garbage":
                "Güllor explodiert in einer Schlammbombe!"
            else:
                "Biclops ist bereit zum Überfahren!"
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
        
        "Wechseln":
            $ queued = "yes"
            jump switch


label win:
    $ win = "yes"
    "Du hast gegen [o] gewonnen!"
    "Gratualtion!"
    jump endbattle

label loss:
    $ win = "no"
    "[o] hat alle deine Monster besiegt!"
    o "Wacker geschlagen, aber noch nicht gut genug!"
    jump endbattle


