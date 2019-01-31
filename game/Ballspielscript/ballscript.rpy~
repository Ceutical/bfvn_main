# The script of the game goes in this file.

###### SCRIPT START #####

##### CHARACTER DEFINITIONS #####

define p = Character("Prot") 

define n = Character(name=None, what_italic=True) #Narrator

define a = Character("Anja")

define o = Character("Octavia")
define O = Character("Octa")
define k = Character("Karin")

define L = Character("Louis")
define nvln = Character(name=None, kind=nvl)

#define test = Character("Test", window_ypos=0.27) #TESTCHAR



######################################

##### MUSIC DEFINITIONS #####

define audio.octatheme = "music/soundtracks/octatheme.mp3"

######################################

##### TRANSFORM DEFINITIONS #####


transform leftish:
    xalign .26
    yalign 1.0
transform rightish:
    xalign .76
    yalign 1.0
    
############################################################


transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.
    
    
init:
    $ timer_range = 0
    $ timer_jump = 0
    
###########################################################    


label startballgame:
    play music octatheme

    

##### Szene Ballspiel #####
label scenetutorial:
    
    
        
    scene bg ball with dissolve
    show osport talk with moveinright
    o "Und du willst wirklich mitspielen? Kannst du das überhaupt."
    o "Bei dem Spiel muss man gute Reflexe haben!"
    menu:
        "Ich kann das!":
            o "Das will ich sehen:"
        
        "Ich geb mir Mühe...":
            o "Das können wir gleich mal testen"
            
    o "Fang!"
    
label timedmenu1:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'menu1_slow'
    show screen countdown
    menu:
        "Fang den Ball":
            hide screen countdown
            jump menu1_end

   
label menu1_slow:
    o "Das muss aber noch besser werden! Wir sehen uns auf dem Feld!"
    jump sceneball
    
label menu1_end:
    o "Gar nicht mal so schlecht. Jetzt bloß nicht nachlassen beim Spiel!"
    
    
label sceneball:
    scene bg ball with dissolve
    show karin go at leftish
    show osport vhappy at rightish
    k "Soo, alle bereit? Dann kann es ja gleich los gehen, auf 3..."
    o "Wir machen euch fertig!"
    hide osport vhappy with moveoutright
    k "...2"
    scene bg bexperiment
    show oball n
    show plinks n
    show lrechts n
    with fade
    k " ...1"
    a "Du hast zuerst den Ball!"
    show prot gefangen with dissolve
    k "Los!"
    $ spielpunkte = 0

label timedmenu2:
    $ time = 2
    $ timer_range = 2
    $ timer_jump = 'menu2_slow'
    show oball links
    show lrechts links
    with dissolve
    pause 0.5
    show screen countdown
    menu:
        
        "Nach links werfen":
            hide screen countdown
            $ enemyname = "lrechtsdrin"
            show oball linksausg
            show plinks n
            show lrechts ausg
            show prot geworfen
            with dissolve
            show ball links with zoomin
            a "Haha! Person 1, du bist raus!"
            $ spielpunkte += 1
            o "Anfängerglück!"
            hide prot
            hide ball
            hide plinks
            show oball mittelzielen
            show lrechts n
            with dissolve
            o "Na warte, jetzt bin ich dran!"
            show oball hochzielen with dissolve
            
        
        "In die Mitte werfen":
            hide screen countdown
            $ enemyname = "plinksdrin"
            show oball linksausg
            show lrechts ausg
            show plinks n
            show prot geworfen
            with dissolve
            show ball mittelrechts with zoomin
            a "Haha! Louis, du bist raus!"
            $ spielpunkte += 1
            o "Anfängerglück!"
            hide prot
            hide ball
            hide lrechts ausg
            show oball mittelzielen
            with dissolve
            o "Na warte, jetzt bin ich dran!"
            show oball hochzielen with dissolve
            
        
        
        "Nach rechts werfen":
            label menu2_slow:
                hide screen countdown
                $ enemyname = "lrechtsdrin"
                $ enemyname = "plinksdrin"
                show oball linksausg
                show lrechts ausg
                show plinks n
                show prot geworfen
                with dissolve
                show ball rechts with zoomin
                o "Was war denn das?"
                hide prot
                hide ball
                show oball mittelzielen
                show lrechts n
                with dissolve
                o "Also, wenn ihr noch gewinnen wollt, müsst ihr noch sehr viel besser werden!"
                a "Protagonist wärmt sich nur noch auf, du wirst schon sehen!"
                show oball hochzielen with dissolve
        
                
label timedmenu3:
    $ time = 1.8
    $ timer_range = 1.8
    $ timer_jump = 'menu3_slow'
    pause 0.5
    show screen countdown
    menu:
        "Ducken":
            hide screen countdown
            $ ballname = "agefangen1"
            show oball n with dissolve
            p "Hui, das war knapp!"
            o "Dafür hab ich Randy erwischt! Du bist draußen!"
            $ spielpunkte -= 1
            show amate gefangen with dissolve
            a "Ich hab den Ball!"
            a "Wohin soll ich werfen?"
            
        
        "Versuchen zu fangen":
            hide screen countdown
            $ ballname = "gefangen1"
            show oball n
            show prot gefangen
            with dissolve
            p "Ha!"
            a "Gut gemacht! Du darfst wieder werfen!"
            
        
        "Hoch springen":
            label menu3_slow:
                hide screen countdown
                show ball iyf
                o "Ha! Voll erwischt!"
                o "Du bist draußen!"
                n "Danach hat Octavia einen nach dem Anderen wie Federn vom Spielfeld gepustet."
                jump sceneverloren
                

                
label timedmenu4:
    show oball rechts with dissolve
    pause 0.5
    $ time = 1.6
    $ timer_range = 1.6
    $ timer_jump = 'menu4_slow'
    show screen countdown
    
    
    if enemyname == "plinksdrin":
        show plinks rechts with dissolve
        
        
    menu:
        "Nach links zielen":
            label menu4_slow:
                hide screen countdown
                show oball rechtsausg with dissolve
                
                if enemyname == "plinksdrin":
                    $ enemyname = "plinksdrin2"
                    show plinks ausg with dissolve
                    
                elif enemyname == "lrechtsdrin":
                    $ enemyname = "lrechtsdrin2"
                    
                if ballname == "gefangen1":
                    show prot geworfen with dissolve
                    
                elif ballname == "agefangen1":
                    show amate geworfen with dissolve
                
                show ball links with zoomin
                hide prot geworfen
                hide amate geworfen
                with dissolve
                o "Ha! Daneben!"
                
                if enemyname == "plinksdrin":
                    show plinks n with dissolve
                    hide ball links with dissolve
                    show oball mittelzielen
                    o "Jetzt mach ich dich fertig!"
                    
                    
        "In die Mitte zielen":
            hide screen countdown
            show oball rechtsausg with dissolve
            
            if enemyname == "lrechtsdrin":
                $ enemyname = "lrechtsdrin2"
            
            if enemyname == "plinksdrin":
                show plinks ausg with dissolve
            
            if ballname == "gefangen1":
                show prot geworfen with dissolve
                
            if ballname == "agefangen1":
                show amate geworfen with dissolve
                
            show ball mittellinks with zoomin
            
            if enemyname == "plinksdrin":
                k "Person 1, du bist draußen!"
                o "So ein Mist aber auch!"
                $ spielpunkte += 1
                
            else:
                o "Haha! Schon wieder daneben!"
               
            hide prot
            hide plinks
            hide amate
            hide ball
            with dissolve
            show oball mittelzielen with dissolve
            o "Jetzt mach ich dich fertig!"
            
                
        
        "Nach rechts zielen":
            hide screen countdown
            show oball rechtsausg with dissolve
            
            if enemyname == "lrechtsdrin":
                show lrechts n with dissolve
            
            if enemyname == "plinksdrin":
                show plinks ausg with dissolve
                $ enemyname = "plinksdrin2"
            
            if ballname == "gefangen1":
                show prot geworfen with dissolve
                
            if ballname == "agefangen1":
                show amate geworfen with dissolve
                
            show ball rechts with zoomin
            hide prot geworfen
            hide amate geworfen
            with dissolve
            
            if enemyname == "plinksdrin":
                show plinks n with dissolve
            
            elif enemyname  == "lrechtsdrin":
                k "Louis du bist raus!"
                L "Menno!"
                $ spielpunkte += 1
                hide lrechts n
                hide ball
                show oball mittelzielen
                with dissolve
                o "Jetzt geht es um alles!"
                
        
            else: 
                k "Octavia, du bist raus!"
                o "Das ist doch blöd!"
                n "Nachdem Octavia einmal draußen war, war Gewinnen ganz einfach."
                jump scenegewonnen
                
                
                
    
label timedmenu5:
    show oball tiefzielen with dissolve
    pause 0.5
    $ time = 1.4
    $ timer_range = 1.4
    $ timer_jump = 'menu5_slow'
    show screen countdown
    
    
    menu:
        "Ducken":
            hide screen countdown
            show oball n with dissolve
            show prot gefangen
            p "Ha!"
            o "Der schummelt doch!"
        
        "Versuchen zu fangen":
            label menu5_slow:
                hide screen countdown
                show oball n with dissolve
                o "Ha! Voll auf die Beine!"
                k "Prot! Du bist raus!"
                n "Danach hat Octavia Einen nach dem Anderen wie Federn vom Spielfeld gepustet."
                jump sceneverloren
        
        "Hoch springen":
            hide screen countdown
            show oball n with dissolve
            a "Huch! Was machst du denn?"
            o "Ha! Ich hab Anja erwischt!"
            k "Anja du bist draußen!"
            $ spielpunkte -= 1
            a "Och manno..."
            $ enemyname = "adraußen"
            
            
    if spielpunkte >0:
        jump scenegewonnen
        
    elif spielpunkte <0:
        jump sceneverloren
        
    else:
        jump sceneunentschieden
        
    
label sceneverloren:
    scene bg ball with dissolve
    show karin go at left
    k "Oh...leider müssen wir jetzt Schluss machen!"
    k "Es fängt gleich an zu Regnen."
    k "Da bei Team Octa noch mehr Spieler im Feld stehen, habt ihr gewonnen!"
    show osport happy at center with moveinright
    show asport mad at rightish with moveinright
    k "Damit hat Team Octa gewonnen!"
    a "Menno!"
    o "Das war von vornherein klar!"
    jump scenew2_6
    
label scenegewonnen:
    scene bg ball with dissolve
    show karin go at left
    k "Oh...leider müssen wir jetzt Schluss machen!"
    k "Es fängt gleich an zu Regnen."
    k "Da bei Team Prota noch mehr Spieler im Feld stehen, habt ihr gewonnen!"
    show osport mad at center with moveinright
    show asport happy at rightish with moveinright
    o "Menno!"
    a "Yuhuuuu!"
    jump scenew2_6
    
label sceneunentschieden:
    scene bg ball with dissolve
    show karin go at left
    k "Oh...leider müssen wir jetzt Schluss machen!"
    k "Es fängt gleich an zu Regnen."
    k "Da bei beiden noch gleich viele Spieler im Spielfeld stehen, ist unentschieden!"
    show osport mad at center with moveinright
    show asport mad at rightish with moveinright
    o "Na warte! So leicht kommst du mir nicht davon."
    o "Das gibt noch eine Revanche!"
    a "Worauf du dich verlassen kannst!"
    jump scenew2_6
