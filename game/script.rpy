##### SCRIPT START #####

##### CHARACTER DEFINITIONS #####

define m = Character("Mama")
define p = Character("[name]") #Name of Player Character -- P = Protagonist
define a = Character("Anja")
define e = Character("Evelynn")
define o = Character("Octavia")
define O = Character("Octa")
define h = Character("Frau Heidenau")
define k = Character("Katrin")
define L = Character("Louis")
define r = Character("Randy")
define emum = Character("Evelynn's Mutter")
define edad = Character("Evelynn's Vater")

##### CHARACTER DEFINITIONS END #####

######################################

##### TRANSFORM DEFINITIONS #####

transform slightleft:
    xalign .35
    yalign 1.0
transform slightright:
    xalign .68
    yalign 1.0
    
##### TRANSFORM DEFINITIONS END #####

######################################


label start:

    ##### AFFINITY SYSTEM INITIATE #####
    
    $ octa_points = 0
    $ eve_points = 0
    $ anja_points = 0
    
    ##### AFFINITY SYSTEM END #####

    
    ##### Szene 1 - Prolog #####
    
    ##### WOCHE 1 BEGINN #####
    ##### TAG 1 BEGINN #####
    ##### Szene 2 #####
    "???" "Hey Kleiner! Aufwachen! Du willst doch nicht zu spät kommen!"
    "{i}Diese warme Stimme gehört Mama. Jeden Tag weckt sie mich und ist immer für mich da.{/i}"
    "{i}Aber heut is Morgen! Ich komm in den neuen Kindergarten!{/i}"
    "{i}Da treff ich bestimmt...{/i}"
    m "Raus aus den Federn jetzt. Es gibt Frühstück!"
    show bg bedroom with fade
    "{i}Jetzt nimmt sie mir die Decke weg...{/i}"
    "{i}Alles ist furchtbar hell... Aber dann sehe ich auch schon meine Mama.{/i}"
    show mum talk with moveinright
    m "Guten Morgen mein kleiner Spatz!"
    m "Na komm. Wir ziehen dich gleich an, jetzt gibt's erstmal Essen."
    m "Ich hab Pfannenkuchen gemacht! Heute ist doch dein großer Tag!"
    "Pfannenkuchen! Ohh Mama ich hab dich lieb!"
    show bg kitchen with dissolve
    "{i}Ich drück Mama ganz doll, kletter aus meinem Bett und lauf mit ihr in die Küche.{/i}"
    m "Freust du dich schon deine neuen Freunde kennenzulernen?"
    menu:
        "Jaaaaaa!":
            "{i}Ich strahle Mama regelrecht an als ich ihr antworte.{/i}"
            m "Das ist schön. Du kommst bestimmt in eine Gruppe mit ganz tollen anderen Kindern."
            jump choice1_done
     
        "Ja...":
            "{i}Ich will Mama nicht traurig machen und versuche sie anzulächeln.{/i}"
            m "Ach Spätzchen... Bist du doch noch so traurig, dass du deine alten Freunde nicht mehr siehst?"
            "{i}Ich schaue traurig auf mein Frühstück runter.{/i}"
            m "Kopf hoch, das wird ganz toll. Du kommst in eine Gruppe mit ganz tollen anderen Kindern!"
            "{i}Als Mama mir durch die Haare wuschelt wird meine Laune wieder besser. Mama ist die Beste!{/i}"
            jump choice1_done
    
        
label choice1_done:
    hide mum
    
    ##### Szene 3 #####
    m "Blabla auf zum KiGa bla."
    "{i}Blabla deepe Kindergedanken auf dem Weg zum KiGa bla.{/i}"
    "Ankunft Kindergarten. Beschreibung Hof / Gebäude."
    show bg grura with dissolve
    show mum n at slightleft with moveinleft
    show heide n at slightright with moveinright
    "Gespräch zwischen Mutter und Heidenau"
    "Vorstellungsmöglichkeit für den Spieler"
    menu:
        "Selbst vorstellen.":
            python:
                name = renpy.input("Wie lautet dein Name?")
                name = name.strip() or "P"
            "{i}Ich heiße [name].{/i}"
            "Mutter+Heide reden weiter, Karin kommt und bringt ihr Kind zum Gruppenraum."
            jump choice2_done
        
        "Mutter hilfesuchend ansehen.":
            python:
                name = renpy.input("Wie lautet dein Name?")
                name = name.strip() or "P"
            m "Er heißt [name]."
            "Mutter ist besorgt, lässt sich von Heide sagen wo sie hin muss und bringt ihr Kind zum Gruppenraum."
            jump choice2_done
        
    
label choice2_done:
    hide heide
    hide mum
    show octa happy at center with moveintop
    show anja what at left with moveinleft
    show eve happy2 at right with moveinright
    show louis really at slightright behind octa with moveinbottom
    show randy happy at slightleft behind octa with moveinbottom
    "Im Gruppenraum werden die Kinder versammelt und man muss sich vorstellen."
    menu:
        "Vorstellen.":
            $ menu_choice3 = "yes"
            p "Hallo ich bin [name]! Lasst uns Freunde sein!"
            jump choice3_done
            
        "Schweigen.":
            $ menu_choice3 = "no"
            p "{i}...{/i}"
            jump choice3_done
        
        "Stammeln.":
            $ menu_choice3 = "meh"
            p "Asduijsahdpiojan"
            jump choice3_done
            
    
    ##### Szene 4 #####
label choice3_done:
    hide octa
    hide anja
    hide eve
    hide louis
    hide randy
    show katrin n
    "Katrin stellt sich vor und beginnt den Morgenkreis."
    show katrin music at right with move
    show octa music at left with moveinleft
    "Minigame geht los. Takt halten."
    "Minigame steht noch nicht, von daher Choice:"
    menu:
        "Hast du das Minispiel gewonnen oder verloren?"
        
        "Gewonnen.":
            hide katrin
            show octa mine at center with move
            "Octa beleidigt dich zwar, findet es aber gut."
            jump choicemini_done
            
        "Verloren...":
            hide katrin
            show octa mine at center with move
            "Octa macht sich über dich lustig."
            jump choicemini_done
            
    
    ##### Szene 5 #####
label choicemini_done:
    hide octa
    show bg kitchen with fade
    "Frühstück. Da [name] sonst keinen kennt setzt er sich neben Anja."
    show anja eat at center with moveinbottom
    "Anja labert ihn zu, lästert vor allem über andere."
    "Anja spricht dich auf deine Vorstellung an."
    if menu_choice3 == "yes":
        "Anja fragt ob man gerne klettert und erzählt."
        
    elif menu_choice3 == "no":
        "Anja fragt dich wer du bist und stellt sich vor. Sie redet aber sofort selbst weiter."
        
    else:
        "Anja macht sich über dich lustig."
        
    "[name] fühlt sich unwohl und flieht zum Frühstücksende vor Anja."
    hide anja
    
    ##### Szene 6 #####
    show bg grura
    "Im Gruppenraum trifft man Evelynn."
    show eve draw at center with moveinbottom
    "Man setzt sich zu ihr, sieht dass sie zeichnet, stellt sich vor und fragt sie wie sie heißt."
    "Evelynn antwortet knapp."
    "Als man sie fragt was sie malt, zeigt sie einem ihr Bild von einem Leuchtturm."
    show eve paper
    menu:
        "Wie findest du das Bild?"
        
        "Das sieht toll aus!":
            show eve shy2
            "Evelynn bedankt sich bei dir."
            jump choice4_done
            
        "Was ist das?":
            "Evelynn erklärt, dass es ein Leuchtturm ist und fragt ob man garnicht wissen was ein Leuchtturm sei."
            menu:
                
                "Nein...":
                    show eve talk2
                    "Evelynn erklärt was ein Leuchtturm ist und erzählt eine Geschichte dazu."
                    jump choice4_done
                    
                "Leuchttürme sehen doch ganz anders aus...":
                    show eve mad
                    "Evelynn schaut dich böse an und nimmt ihre Zeichnung zurück."
                    jump choice4_done
            
        "Das kann ich aber besser.":
            show eve mad
            "Evelynn schaut dich böse an und nimmt ihre Zeichnung zurück."
            jump choice4_done
    

    
label choice4_done:
    hide eve
    "Man entscheidet sich auch irgendwann mal was zu malen."
    show mum talk at center with moveinleft
    "Mutter holt einen ab."
    hide mum
    ##### TAG 1 ENDE #####

    ##### TAG 2 BEGINN #####
    ##### Szene 7 #####
    show katrin music at center
    "Beim Morgenkreis wurde gesungen."
    hide katrin
    
    ##### Szene 8 #####
    show eve foodplay at center with fade
    "P sieht E allein am Tisch und setzt sich dazu. E spielt mit ihrem Essen, sie scheint damit zu malen."
    menu:
        
        "Interesse zeigen.":
            show eve shy2
            "Evelynn freut sich."
            jump choice5_done
            
        "Geekelt sein.":
            "Du zeigst Evelynn wie sehr du dich ekelst."
            show eve mad
            "E erklärt dir, dass man mit Essen ganz toll malen kann und das auch Spaß macht."
            jump choice5_done
            
        "Geschockt reagieren.":
            "Mama sagt, dass man nicht mit Essen spielt!"
            show eve talk2
            "E meine auch. Aber die ist jetzt auch nicht hier."
            jump choice5_done
            
    
    
label choice5_done:
    menu:
        "Evelynn fragt, ob du nicht auch Lust hättest mit dem Essen zu spielen."
        
        "Au ja!":
            "P entscheided sich zusammen mit Evelynn zu spielen."
            "Er baut mit ihrer Hilfe einen Leuchtturm aus seinem Essen."
            jump choice6_done
            
        "Nein, sicher nicht.":
            "P wehrt sich gegen die Vorstellung in seinem Essen rumzumatschen."
            "E findet das blöd."
            jump choice6_done
    ##### TAG 2 ENDE #####
    
    ##### TAG 3 BEGINN #####
    ##### Szene 9 #####
label choice6_done:
    hide eve
    show katrin music
    "Anstelle des Morgenkreises haben heute alle fangen gespielt."
    hide katrin
    
    ##### Szene 10 #####
    "P sitzt allein beim Essen, als sich Louis dazugesellt."
    "Louis bietet P den Snackersdeal an."
    menu:
        "Snackers dealen?"
        
        "Ja.":
            $ snackersdeal = True
            e "Deal!"
            jump choice7_done
            
        "Nein.":
            $ snackersdeal = False
            e "No Deal!"
            jump choice7_done
    
label choice7_done:
    "Louis geht."
    ##### Szene 11 #####
    "Katrin scheucht alle Kinder raus."
    "Auf dem Hof hört P 2 Kinder streiten."
    "1. Auftritt Randy. Randy ist P noch unbekannt"
    menu:
        "Wie reagieren?"
        
        "Stumm abwarten.":
            $ daze = False
            "Streit geht weiter. Streitgrund wird erfahren. Name von Randy wird erfahren."
            $ randyname = True
            "A mag lieber Schoko, R lieber Vanille."
            "Streithähne trennen sich."
            jump choice8_done
            
        "Dazwischengehen.":
            $ daze = True
            $ randyname = False
            "HÖRT AUF!"
            "MISCH DICH NET EIN!"
            "Streithähne trennen sich, da sie dieselbe Meinung haben."
            jump choice8_done

    
label choice8_done:
    "Anja ist sauer, sieht P, wird fröhlich, bittet ihn hochzuklettern."
    menu:
        "Klettern?"
        
        "Ich kann nicht klettern.":
            "A hilft P."
            jump choice9_done
            
        "Einfach gehen.":
            "P geht einfach, A ist wütend."
            jump snackend
            
        "Hochklettern.":
            "P klettert einfach hoch."
            jump choice9_done

    
label choice9_done:
    if daze == True:
        menu:
            
            "Nachfragen worum der Streit ging.":
                "A schiebt die Frage beiseite."
                jump treetalk
                
            "Nicht nachfragen.":
                jump treetalk
                
    else:
        jump treetalk
    
    menu treetalk:
        a "Findest du Schokolade oder Vanille besser?"
        
        "Schokolade.":
            "Endlich mal jemand mit Geschmack."
            jump choice10_done
            
        "Vanille.":
            "BAH! BANAUSE!"
            jump choice10_done
            
    
label choice10_done:
    if snackersdeal == True:
        menu:
            "Anja zur Beruhigung ein Snackers geben?"
            
            "Ja.":
                a "Ohh Junge, ein Snackers!"
                jump treetalk2
                
            "Nein.":
                jump treetalk2
                
    else:
        jump treetalk2
        
    
label treetalk2:
    "A und P unterhalten sich. A lästert über Randy."
    "A erzählt viele interessante Details über alle möglichen Leute."
    jump snackend
    
    ##### Szene 12 #####
label snackend:
    if snackersdeal == True:
        "Mama holt P ab."
        menu:
            
            "Mama fragen ob wir Knappers kaufen können.":
                $ hasknappers = True
                "Mama und P gehen Knappers kaufen."
                jump day4
                
            "Mama nichts von den Knappers erzählen.":
                $ hasknappers = False
                jump day4
    else:
        jump day4
        ##### TAG 3 ENDE #####
        
        ##### TAG 4 BEGINN #####
        ##### Szene 13 #####
label day4:
    "Ankunft am KiGa."
    "P sieht wie O von Eltern zum KiGa gebracht wird."
    "Eltern weg --> O wirft Schutzmontur weg und fährt irrsinning auf dem Fahrrad."
    "O will P überzeugen auch zu zeigen was er kann."
    $ bikepoints = 0
    menu:
        "Aufs Fahrrad steigen?"
        
        "Ja.":
            jump bikescene
            
        "Nein.":
            $ bikepoints += 1
            o "Ohh, du bist wohl ein Angsthase."
            o "Gib doch zu, dass du es einfach nicht kannst."
            menu:
                "Doch aufs Rad steigen.":
                    jump bikescene
                    
                "Sich weiterhin weigern.":
                    $ bikepoints += 1
                    "O droht P"
                    "P steigt jetzt doch lieber auf's Fahrrad."
                    jump bikescene
                 ##### Szene 14 #####   
label bikescene:
    "O drängt P zu einem Trick."
    "Er gelingt."
    "E's Eltern tauchen um die Ecke auf. P erschrickt, fällt und verletzt sich"
    menu:
        "Wie reagiert P?"
        
        "Weinen.":
            $ crying = True
            jump bikescene2
            
        "Stark bleiben.":
            $ crying = False
            jump bikescene2
            
label bikescene2:
    "E will helfen, darf aber nicht."
    emum "NEIN! Evelynn, was am Boden liegt, darf man nicht aufheben!"
    "E wird in den KiGa geschleppt."
    "O rennt zu P and macht sich Sorgen."
    o "Ist dir was passiert?"
    if crying == True:
        "P heult rum."
        o "Ich rede nicht mit dir, sondern mit meinem Fahrrad!"
        "O rennt los, holt Erzieherin und wirkt besorgt."
        "O kommt mit Karin zurück. Karin klebt P ein Pflaster auf."
        "O steht Schuldbewusst daneben."
    else:
        "P sagt er braucht ein Pflaster."
        o "Ich rede nicht mit dir, sondern mit meinem Fahrrad!"
        "O schaut sich die Situation an, stellt ihr Rad an die Seite und geht Hilfe holen."
        "O kommt mit Karin zurück."
        "P will Pflaster haben aber O weist ihn ab und klebt ihm das Pflaster selbst auf."
    
    "Karin will wissen was passiert ist."
    menu:
        "Was wirst du Karin sagen?"
        
        "Karin alles erzählen.":
            "P erzählt alles."
            $ octahome = True
            if bikepoints == 2:
                "Octa verabscheut dich."
            elif bikepoints == 1:
                "Octa hasst dich."
            else:
                "Octa mag dich nicht."
                
            "Karin schimpft mit O, ruft ihre Eltern an und lässt sie abholen."
            jump gohom
            
        "Karin nichts sagen.":
            $ octahome = False
            "P deckt O, erzählt von einem Unfall und O's Mithilfe."
            if bikepoints == 2:
                "Octa vergöttert dich."
            elif bikepoints == 1:
                "Octa bewundert dich."
            else:
                "Octa ist dir dankbar."
                
            "Karin lobt Octa."
            jump gohom
            
    menu gohom:
        k "Möchtest du lieber nach Hause oder im KiGa bleiben?"
        
        "Bleiben.":
            if octahome == True:
                "P bleibt und verbringt den Tag mit anderen Kindern."
                
            else:
                "P bleibt und spielt den Rest des Tages mit O."
            jump day5 
                
        "Gehen.":
            "P's Mutter wird angerufen, P wird abgeholt und bleibt den Rest des Tages zu Hause."
            jump day5
            ##### TAG 4 ENDE #####
            
            ##### TAG 5 BEGINN #####
            ##### Szene 15 #####
label day5:
    "P wird überraschend zum Gebu eingeladen."
    if randyname == True:
        "P erkennt Randy."
        "Randy wundert sich. P erklärt, dass er den Namen beim Streit gehört hat."
        "Randy geht zurück zum Thema."
        
    else:
        "Randy stellt sich vor."
    

    "P fragt wann."
    "R sagt heute und es ist eine Kostümparty."
    "P sagt zu."
    
    ##### Szene 16 #####
    "Mutter holt P ab. P erzählt von der Einladung."
    "Es wird ein Kostüm eingekauft."
    menu:
        "Was für ein Kostüm?"
        
        "Anjakostüm":
            $ costume = "anja"
            "Sie kaufen ein Anjakostüm."
            jump partyday
            
        "Evekostüm":
            $ costume = "eve"
            "Sie kaufen ein Evekostüm."
            jump partyday
            
        "Octakostüm":
            $ costume = "octa"
            "Sie kaufen ein Octakostüm."
            jump partyday
            
label partyday:
    ##### Szene 17 #####
    if snackersdeal == True:
        "P wird von Louis aufgehalten."
        L "Du schuldest mir noch was."
        if hasknappers == True:
            menu:
                "Louis das Knappers geben?"
                
                "Ja.":
                    $ dealcomplete = True
                    "Louis ist zufrieden und erzählt nurnoch gutes über dich."
                    
                "Nein.":
                    $ dealcomplete = False
                    "Louis ist sauer und erzählt allen was für ein schlechter Mensch du bist."
        else:
            menu:
                "Louis das Knappers geben?"
                
                "{s}Louis das Knappers geben.{/s} (disabled)":
                    "This should not be visible. Like ever."
                    
                "Ich habe kein Knappers dabei.":
                    $ dealcomplete = False
                    "Louis ist sauer und erzählt allen was für ein schlechter Mensch du bist."
                    
                    ##### Szene 18 #####
    "Die Party beginnt. Kurze Beschreibung."
    "Blabla mit Randy."
    ##### Szene 19 #####
    if costume == "anja":
        "Cooler Anja Storypfad."
        
        ##### Szene 20 #####
    elif costume == "eve":
        "Cooler Evelynn Storypfad."
        
        ##### Szene 21 #####
    else:
        "Cooler Octavia Storypfad."
        
        ##### Szene 22 #####
    "Ende der Party, cooler Ausklang, cooles Gruppenfoto. Nicenstein."    
    "Prototyp Ende"
    
                

    
    #"Testtest."
        

    
    
    # This ends the game.

    return
