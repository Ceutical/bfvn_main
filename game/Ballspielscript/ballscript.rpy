# The script of the game goes in this file.

###### SCRIPT START #####

##### CHARACTER DEFINITIONS #####

define p = Character("[name]") #Name of Player Character -- P = Protagonist) 

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
    p "Hey, Leute, kann ich noch mitspielen?"
    o "Wirklich? Kannst du das überhaupt?"
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
    o "Das muss aber noch besser werden. In mein Team kommen nur die Besten. Wir sehen uns dann auf dem Feld!"
    jump sceneball
    
label menu1_end:
    o "Gar nicht mal so schlecht. Aber in mein Team kommen nur die Besten. Wir sehen uns auf dem Feld!!"
    
    
label sceneball:
    show karin go at leftish with moveinleft
    show osport vhappy at rightish with dissolve
    show asport mad at center with moveinleft
    a "Ist doch egal, ob er gut spielt."
    o "Ne, ist es nicht. Wenn er schlecht spielt, zieht er nur mein Team runter. Er muss mindestens so gut sein wie die aus der Axolotl-Gruppe."
    show asport n
    p "Also, ich-"
    o "Dann nimm du ihn doch, wenn es dich nicht stört, Anja!"
    show asport happy
    a "Mach ich auch!"
    o "Weil wir sowieso besser sind, dürft ihr Ausnahmsweise den Ball zuerst haben. Sonst wäre es zu einfach für mich."
    hide asport n with dissolve
    n "Octavia tut zwar auf cool, ist aber wieder total angespannt. Warum nimmt die das alles immer so furchtbar ernst?"
    k "Soo, alle bereit?" 
    p "Ja!"
    k "Dann kann es ja gleich los gehen, auf 3..."
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
    p "Okay, jetzt darf ich bloß nicht zu langsam sein..."
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
            a "Haha! Und schon ist die aus der anderen Gruppe draußen!"
            $ spielpunkte += 1
            o "Anfängerglück!"
            hide prot
            hide ball
            hide plinks
            show oball mittelzielen
            show lrechts n
            with dissolve
            o "Na warte, jetzt bin ich dran!"
            o "Pow!"
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
            o "Pow!"
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
                a "[name] wärmt sich nur noch auf, du wirst schon sehen!"
                o "Na warte, jetzt bin ich dran. Pow!"
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
                show oball n
                show ball iyf
                with dissolve
                o "Ha! Voll erwischt!"
                o "Du bist draußen!"
                hide ball iyf
                p "Hey, das gildet nicht, ich war ja noch gar nicht richtig drinnen und..."
                o "Nix da! Getroffen ist getroffen, also raus mit dir!"
                p "Jaja, ich geh ja schon!"
                o "So, wer ist als nächstes dran?"
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
                    p "SUPER-SPEZIAL-WURF!"
                    show prot geworfen with dissolve
                    
                elif ballname == "agefangen1":
                    a "Und Spezialwurf!"
                    show amate geworfen with dissolve
                
                show ball links with zoomin
                hide prot geworfen
                hide amate geworfen
                with dissolve
                o "Ha! Daneben!"
                hide ball links with dissolve
                
                if enemyname == "plinksdrin2":
                    show plinks n with dissolve
                    
                hide ball links  
                show oball mittelzielen
                with dissolve
                o "Jetzt mach ich dich fertig!"
                n "Immer wenn Octavia den Ball in der Hand hat, ist das andere Team wie erstarrt. Nichtmal Anja bewegt sich."
                    
                    
        "In die Mitte zielen":
            hide screen countdown
            show oball rechtsausg with dissolve
            
            if enemyname == "lrechtsdrin":
                $ enemyname = "lrechtsdrin2"
            
            if enemyname == "plinksdrin":
                show plinks ausg with dissolve
            
            if ballname == "gefangen1":
                p "SUPER-SPEZIAL-WURF!"
                show prot geworfen with dissolve
                
            if ballname == "agefangen1":
                a "Und Spezialwurf!"
                show amate geworfen with dissolve
                
            show ball mittellinks with zoomin
            
            if enemyname == "plinksdrin":
                a "Haha! Und schon ist die aus der anderen Gruppe draußen!"
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
            n "Immer wenn Octavia den Ball in der Hand hat, ist das andere Team wie erstarrt. Nichtmal Anja bewegt sich."
            
                
        
        "Nach rechts zielen":
            hide screen countdown
            show oball rechtsausg with dissolve
            
            if enemyname == "lrechtsdrin":
                show lrechts n with dissolve
            
            if enemyname == "plinksdrin":
                show plinks ausg with dissolve
                $ enemyname = "plinksdrin2"
            
            if ballname == "gefangen1":
                p "SUPER-SPEZIAL-WURF!"
                show prot geworfen with dissolve
                
            if ballname == "agefangen1":
                a "Und Spezialwurf!"
                show amate geworfen with dissolve
                
            show ball rechts with zoomin
            hide prot geworfen
            hide amate geworfen
            with dissolve
            
            if enemyname == "plinksdrin":
                show plinks n with dissolve
            
            elif enemyname  == "lrechtsdrin":
                L "Uff!"
                k "Louis du bist raus!"
                o "Hättest echt mal besser ausweichen können!"
                o "Alles muss man alleine machen!"
                $ spielpunkte += 1
                hide lrechts n
                hide ball
                show oball mittelzielen
                with dissolve
                o "Jetzt geht es um alles!"
                n "Immer wenn Octavia den Ball in der Hand hat, ist das andere Team wie erstarrt. Nichtmal Anja bewegt sich."
                
        
            else: 
                k "Octavia, du bist raus!"
                o "Das ist doch blöd! Das war nur ein Streifer..."
                a "Runter vom Feld! Du wurdest getroffen. Das zählt!"
                n "Nachdem Octavia einmal draußen war, war Gewinnen ganz einfach. Vor allem Anja hat alle mit ihrem SUPER-MEGA-ULTRA-SPEZIALWURF aus dem Feld gehauen."
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
                r "Ich dachte auf die Beine ist verboten!"
                o "Quatsch, gar nix ist verboten!"
                k "[name] ! Du bist raus!"
                p "Jaja, ich geh ja schon!"
                o "So, wer ist als nächstes dran?"
                n "Danach hat Octavia Einen nach dem Anderen wie Federn vom Spielfeld gepustet."
                jump sceneverloren
        
        "Hoch springen":
            hide screen countdown
            show oball n with dissolve
            a "Huch! Was machst du denn?"
            o "Ha! Ich hab Anja erwischt!"
            a "Aua!"
            a "Musst du so hart werfen?"
            o "Sei mal nicht so eine Memme! Das ist ein Schaumball, der kann gar nicht wehtun."
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
    $ anja_points -= 1
    $ octa_points -= 2
    scene bg ball with dissolve
    show karin go at left
    k "Oh...leider müssen wir jetzt Schluss machen!"
    k "Bald ist schon wieder Abholzeit."
    k "Da bei Team Octa noch mehr Spieler im Feld stehen, habt ihr gewonnen!"
    show osport happy at center with moveinright
    show asport mad at rightish with moveinright
    o "Ja, ich hab gewonnen! Ich bin die Beste!"
    a "Du hast meinen Spezialwurf geklaut! Das darfst du nicht!"
    o "Hah, nix geklaut! Das war mein eigener Spezialwurf. Ihr habt verloren, voll traurig für euch!"
    n "Man, die hören ja wirklich nie auf."
    hide karin with dissolve
    jump scenenachball
    
label scenegewonnen:
    $ anja_points += 2
    $ octa_points += 3
    scene bg ball with dissolve
    show karin go at left
    k "Oh...leider müssen wir jetzt Schluss machen!"
    k "Bald ist schon wieder Abholzeit."
    k "Da bei Team Prota noch mehr Spieler im Feld stehen, habt ihr gewonnen!"
    show osport mad at center with moveinright
    show asport happy at rightish with moveinright
    a "Yuhuuuu!"
    o "Ich hab voll mit Absicht nicht so hart gespielt. Schließlich ist [name] neu hier!"
    a "Von wegen! Du hast sogar meinen Spezialwurf geklaut!"
    o "Hah, nix geklaut! Das war mein eigener Spezialwurf. Ich hätte auch locker gewinnen können!"
    n "Man, die hören ja wirklich nie auf."
    hide karin with dissolve
    jump scenenachball
    
label sceneunentschieden:
    $ anja_points += 1
    $ octa_points -= 1
    scene bg ball with dissolve
    show karin go at left
    k "Oh...leider müssen wir jetzt Schluss machen!"
    k "Bald ist schon wieder Abholzeit."
    k "Da bei beiden noch gleich viele Spieler im Spielfeld stehen, ist unentschieden!"
    show osport mad at center with moveinright
    show asport mad at rightish with moveinright
    o "Na warte! So leicht kommst du mir nicht davon."
    o "Das gibt noch eine Revanche!"
    a "Worauf du dich verlassen kannst!"
    hide karin with dissolve
    jump scenenachball
    
    
    
    
label scenenachball:
    show osport mad at leftish with dissolve
    show asport mad at rightish with dissolve
    o "Man, du bist so schlecht Anja!"
    a "Ich bin überhaupt nicht schlecht!"
    "{color=#0099ff}Octavia:{/color} Doch bist du! Außerdem strengst du dich gar nicht an. \n{color=#0099ff}Anja:{/color} Na und?! Dafür kannst du nicht klettern!"
    "{color=#0099ff}Octavia:{/color} Das stimmt doch gar nicht! \n{color=#0099ff}Anja:{/color} Stimmt wohl! Ich wette du kommst nicht mal den Baum hoch."
    o "D…doch das ist su..per einfach."
    n "Warum stottert sie denn jetzt. Kann Octa nicht klettern?"
    a "Dann komm mit hoch. Ich Kletter schon mal vor."
    o "Ah...klar."
    
    menu:
        n "Was mach ich jetzt nur?"
        
        "Ich halt mich besser zurück...":
            
            a "Worauf wartest du dann? Los!"
            o "Ja, ja ich mach ja gleich."
            n "Man das sieht nicht gut aus."
            o "So…erstmal…"
            n "Verdammt hoffentlich hat sie sich nicht weh getan."
            o "Au…"
            k "Was ist denn hier los?"
            k "Oh man Octa, was machst du denn?"
            o "Ich wollte doch nur…"
            k "Jetzt komm mal mit wir müssen das verarzten."
            k "Und du Anja kommst auch mal mit."
            a "Aber…"
            k "Nix aber! Du kommst jetzt mit."
            n "Vielleicht hätte ich doch lieber im Sandkasten gespielt…"
            jump scenew2_6
            
        "Ich will auch klettern!":
            p "Hey, lass mich mal. Ich will auch auf den Baum!"
            $ octa_points += 1
            
            if climber == True:
                n "Jetzt beim zweiten mal ist es echt nicht mehr so schwer."
                a "Schau sogar [name] kann das."
                o "Ja, aber jetzt wo ihr da oben seid kann ich ja nicht mehr hoch. Da ist nämlich überhaupt kein Platz für 3."
                o "Sonst würde ich das natürlich machen."
                a "Ja ja was auch immer! Feigling!"
                a "Verzieh dich!"
                o "Pah!"
                n "Und weg ist sie…"
                a "Man die nervt! Bin ich froh, dass sie abgehauen ist."
                a "Und du… sag mal was sollte das?"
                
                menu:
                    a "Warum hast du dich denn vorgedrängelt?"
                    
                    "Na ich wollte halt hoch auf den Baum.":
                        $ anja_points -= 1
                        a "Ach lüg doch nicht!"
                        p "Was wieso?"
                        a "Du hast das doch nur gemacht damit sie sich nicht schlecht fühlt."
                        a "Weiß doch jeder, dass sie nicht klettert. Ich glaub sie hat Angst davor."
                        p "Na gut, vielleicht."
                        a "Sag mal magst du die Octavia. Kann ich ja nicht wirklich verstehen."
                        a"Die nervt doch immer nur."
                        p"Ja aber…"
                        jump axolotl
                        
                    "Octavia hat mir leid getan...":
                        $ anja_points += 2
                        a "Ach so! Das hatte ich mir irgendwie schon gedacht."
                        a "Gut dass du nicht gelogen hast."
                        a "So richtig versteh ich das ja nicht. Octavia nervt doch immer nur."
                        p"Ja aber…"
                        jump axolotl
                        
                        
            else:
                n "So, ich  brauch nur ordentlich Schwung."
                p "Au! Verdammt! Blöder Baum!"
                o "Hahaha… was machst du denn für einen Blödsinn?"
                a "[name]? Ist alles okay?"
                p "Ja, ich glaub schon."
                a "Gut. Das hat ganz schön gekracht. Dachte schon du hättest dir was gebrochen."
                a "Aber egal. Dann kann ja jetzt Oc…"
                a "Hey, Moment! Wo ist sie denn?"
                a "Ist die einfach abgehauen?"
                p "Hm…sieht so aus."
                a "Typisch."
                a "Und du… sag mal was soll das eigentlich?"
                
                menu:
                    a "Warum hast du dich denn vorgedrängelt?"
                    
                    "Na ich wollte halt hoch auf den Baum.":
                        $ anja_points -= 3
                        a "Ach lüg doch nicht!"
                        p "Was wieso?"
                        a "Letzte Woche wolltest du auch nicht klettern. Und jetzt plötzlich…"
                        a "Das glaub ich nicht."
                        p "Aber…"
                        a "Nix aber lügen ist blöd!"
                        a "Weiß doch jeder, dass sie nicht klettert. Ich glaub sie hat Angst davor."
                        p "Na gut, vielleicht."
                        a "Ja und deswegen hast du dich vorgedrängelt, damit sie nicht klettern muss."
                        a "Und weißt du was?"
                        a "Wenn du die blöde Octavia so magst, dann geh doch zu der statt rumzulügen!"
                        n "Ich geh besser. Sie ist echt sauer. Vielleicht hätte ich nicht lügen sollen, aber ich wollte doch nur dass sich Octa nicht weh tut…"
                        jump scenew2_6
                        
                    "Octavia hat mir leid getan...":
                        $ anja_points += 2
                        a "Ach so! Das hatte ich mir irgendwie schon gedacht."
                        a "Gut dass du nicht gelogen hast."
                        a "So richtig versteh ich das ja nicht. Octavia nervt doch immer nur."
                        p"Ja aber…"
                        jump axolotl
                        
                        
label axolotl:
    a "Weißt du eigentlich, dass der Lucas aus der Axolotl-Gruppe ein Handy bekommen hat?"
    p "Nö, wer ist Lu…"
    a "Ich meine so eins von diesen wo man Spiele drauf spielen kann. Voll krass!"
    p "Ist das d…"
    a "Zum Beispiel gibt es da so ein Spiel mit ‘ner Schlange und man muss irgendwie machen, dass die Schlange länger wird."
    p "Aha, und wi…"
    a "Und man muss irgendwie auch seinem eigenen Schwanz ausweichen."
    n "Ob ich heute noch mal zu Wort komme…"
    jump scenew2_6
