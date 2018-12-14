##### SCRIPT START #####

##### CHARACTER DEFINITIONS #####

define m = Character("Mama")
define p = Character("[name]") #Name of Player Character -- P = Protagonist
define n = Character(name=None, what_italic=True) #Narrator
define a = Character("Anja")
define e = Character("Evelynn")
define o = Character("Octavia")
define O = Character("Octa")
define h = Character("Frau Heidenau")
define k = Character("Karin")
define L = Character("Louis")
define r = Character("Randy")
define emum = Character("Evelynn's Mutter")
define edad = Character("Evelynn's Vater")
define omum = Character("Octavia's Mutter")
define odad = Character("Octavia's Vater")
define nvln = Character(name=None, kind=nvl)

######################################

##### MUSIC DEFINITIONS #####

define audio.introtheme = "music/soundtracks/introtheme.mp3"
define audio.anjatheme = "music/soundtracks/anjatheme.mp3"
define audio.evetheme = "music/soundtracks/evetheme.mp3"
define audio.octatheme = "music/soundtracks/octatheme.mp3"
define audio.maintheme = "music/soundtracks/maintheme.mp3"
define audio.treefall = "music/sfx/treefall.ogg"
define audio.cardoor1 = "music/sfx/Autotür1.ogg"
define audio.cardoor2 = "music/sfx/Autotür2.ogg"

######################################

##### TRANSFORM DEFINITIONS #####

transform slightleft:
    xalign .35
    yalign 1.0
transform slightright:
    xalign .68
    yalign 1.0
transform leftish:
    xalign .26
    yalign 1.0
transform rightish:
    xalign .76
    yalign 1.0
transform chicken:
    xalign .68
    yalign .5
    

######################################


label start:
    play music introtheme

    ##### AFFINITY SYSTEM INITIATE #####
    $ randyname = True
    $ octa_points = 0
    $ eve_points = 0
    $ anja_points = 0
    
    ##### AFFINITY SYSTEM END #####

    
    ##### Szene 1 - Prolog #####
label scene1:
    scene bg grura with dissolve    
    
    python:
        name = renpy.input("Gib dem Kind einen Namen.")
        name= name.strip() or "P"
        
        
    menu:
        "Wird das Kind Junge oder als Mädchen gesehen?"
        "Als Junge":
            $ gender = "male"
            
        "Als Mädchen":
            $ gender = "female"
            
            
    
    if gender == "male":
        python:
            pro = "sein"
            pro2 = "er"
            pro3 = "ihm"
            pro4 = "Sohn"
            pro5 = "ihn"
            suf = "en"
    else:
        python:
            pro = "ihr"
            pro2 = "sie"
            pro3 = "ihr"
            pro4 = "Tochter"
            pro5 = "sie"
            suf = "e"
    "{b}ANMERKUNG!{/b}"
    "{b}Wir stellen 3 verschiedene Erzählstile vor.{/b}"
    "{b}Kindlicher Erzähler, Erwachsener Erzähler in Retrospektive, Neutraler Erzähler.{/b}"
    "{b}Es folgt nun eine Szene in dreifacher Ausführung. Jeweils mit einem Erzähler als Beispiel.{/b}"
    "{b}Danach geht das Spiel in einfacher Ausführung mit dem Erzähler weiter, den wir uns ausgesucht haben.{/b}"
    "{b}Wir wollen nur der Vollständigkeit halber die anderen Überlegungen auch einmal gezeigt haben.{/b}"
    $ seenscene = False
label narrationoptions:
    scene bg grura with fade
    menu:
        "Welches Szenenbeispiel möchtest du dir ansehen?"
        
        "Den Kindlichen.":
            $ seenscene = True
            jump childlike
        "Den Retrospektiven.":
            $ seenscene = True
            jump retro
        "Den neutralen Bucherzähler.":
            $ seenscene = True
            jump neutral
        "Ich habe alle gesehen.":
            jump scene3
            
    ##### WOCHE 1 BEGINN #####
    ##### TAG 1 BEGINN #####
    ##### Szene 2 CHILD #####
label childlike:
    scene bg black with fade
    "{b}Start: Kindlicher Erzähler{/b}"
    "???" "Hey Püpschen! Aufwachen! Du willst doch nicht zu spät kommen!"
    "{i}Diese warme Stimme gehört Mama. Jeden Tag weckt sie mich und ist immer für mich da.{/i}"
    "{i}Aber heut is Morgen! Ich komm in den neuen Kindergarten!{/i}"
    "{i}Da treff ich bestimmt...{/i}"
    m "Raus aus den Federn jetzt. Es gibt Frühstück!"
    show bg bedroom with fade
    "{i}Jetzt nimmt sie mir die Decke weg...{/i}"
    "{i}Alles ist furchtbar hell... Aber dann sehe ich auch schon meine Mama.{/i}"
    show mum talk with moveinright
    m "Guten Morgen mein kleiner Spatz!"
    p "Guten Morgen Mama ..."
    p "Ich will aber noch nicht aufstehen!"
    m "Ach jetzt stell dich nicht so an. Na komm. Wir ziehen dich gleich an, jetzt gibt's erstmal Essen."
    m "Ich hab Pfannenkuchen gemacht! Heute ist doch dein großer Tag!"
    "Pfannkuchen! Jaa! Mama ich hab dich lieb!"
    show bg kitchen with dissolve
    "{i}Ich drück Mama ganz doll, kletter aus meinem Bett und lauf mit ihr in die Küche.{/i}"
    m "Freust du dich schon deine neuen Freunde kennenzulernen?"
    menu:
        "Jaaaaaa!":
            $ happytogo = True
            "{i}Ich strahle Mama regelrecht an als ich ihr antworte.{/i}"
            m "Das ist schön. Du kommst bestimmt in eine Gruppe mit ganz tollen anderen Kindern."
     
        "Ja...":
            $ happytogo = False
            "{i}Ich will Mama nicht traurig machen und versuche sie anzulächeln.{/i}"
            m "Ach Spätzchen... Bist du doch noch so traurig, dass du deine alten Freunde nicht mehr siehst?"
            "{i}Ich schaue traurig auf mein Frühstück runter.{/i}"
            m "Du kommst heute bestimmt ein eine Gruppe mit ganz tollen Kindern, wirst schon sehen!"
            "{i}Als Mama mir durch die Haare wuschelt wird meine Laune wieder besser. Mama ist die Beste!{/i}"
    
        
    "{b}Ende: Kindlicher Erzähler{/b}"
    jump narrationoptions
    
    ##### Szene 2 - ADULT #####
label retro:
    scene bg black with fade
    "{b}Start: Erwachsener Erzähler in Retrospektive.{/b}"
    n "Hah. Wo soll ich anfangen?"
    n "Ich bin jetzt 23 Jahre alt."
    n "Und heute bat man mich tatsächlich darum aus meiner Kindergartenzeit zu erzählen."
    n "Wie das eben so ist."
    n "Eins führte zum Anderen und schwupps waren wir beim Thema."
    n "Ehrlich gesagt ... \"meine Kindergartenzeit\" als Ganzes war nichts besonderes."
    n "Nur die Zeit nach meinem ... unserem Umzug."
    n "Mama und ich waren jetzt alleine."
    n "Für mich war alles neu. Und verwirrend. Gott ich war erst 6."
    n "Rückblickend ein absolutes Wunder, dass Mama mich noch irgendwo unterbringen konnte."
    n "Es waren nur wenige Monate bis es in die Schule gehen sollte."
    n "Aber das hat gereicht."
    n "Gereicht für eine ganz besondere Zeit."
    n "Der Weg ist das Ziel, richtig?"
    n "Und mein neuer Weg begann an einem Montag Morgen."    
    "???" "Hey Püpschen! Aufwachen! Du willst doch nicht zu spät kommen!"
    n "Das war meine Mama die mich da weckte. Immer für mich da schmiss sie mich auch jeden Morgen pünktlich aus dem Bett."
    n "Ich hatte damals diese furchtbare Angewohnheit mich dann unter meine Decke zu verstecken und so zu tun als würde ich schlafen."
    show bg bedroom with dissolve
    n "Und sie hatte diese noch viel furchtbarere Angewohnheit mir die Decke einfach wegzureißen..."
    show mum talk with moveinright
    m "Guten Morgen mein kleiner Spatz!"
    p "Guten Morgen Mama ..."
    p "Ich will aber noch nicht aufstehen!"
    m "Ach jetzt stell dich nicht so an. Na komm. Wir ziehen dich gleich an, jetzt gibt's erstmal Essen."
    m "Ich hab Pfannenkuchen gemacht! Heute ist doch dein großer Tag!"
    p "Pfannkuchen! Jaaa! Mama ich hab dich lieb!"
    show bg kitchen with dissolve
    n "Wir gingen dann zusammen in die Küche. Sie war zweckmäßig eingerichtet aber für uns hat es gereicht."
    n "Außerdem war Mamas Essen sowieso das Wichtigste."
    m "Freust du dich schon deine neuen Freunde kennenzulernen?"
    menu:
        "Jaaaaaa!":
            $ happytogo = True
            n "Ich wollte endlich wieder mit anderen Kindern spielen. Durch den Umzug und die lange Wartezeit hatte ich viel Zeit allein mit Mama, ohne andere Kinder verbracht."
            m "Das ist schön. Du kommst bestimmt in eine Gruppe mit ganz tollen anderen Kindern."
            
        "Ja...":
            $ happytogo = False
            n "Natürlich nicht. Ich wollte zurück zu meinen Freunden. Zu meinen alten Freunden. Heute erinner ich mich kaum noch an sie aber damals war ich sehr traurig."
            n "Ich wollte nur auch Mama nicht traurig machen. Doch Mamas merken alles."
            m "Ach Spätzchen... Bist du doch noch so traurig, dass du deine alten Freunde nicht mehr siehst?"
            m "Hey, schau mich an, nicht dein Essen. Alles wird gut, okay? Komm her, lass dich mal knuddeln."
            m "Siehst du? Alles garnicht mehr so wild."
            m "Du kommst heute bestimmt ein eine Gruppe mit ganz tollen Kindern, wirst schon sehen!"
            n "Mama wusste immer wie man andere aufmuntert."
    
    "{b}Ende: Erwachsener Erzähler{/b}"
    jump narrationoptions
    
    ##### Szene 2 - NEUTRAL #####
label neutral:
    scene bg black with fade
    "{b}Start: Neutraler Erzähler{/b}"
    "{b}Der Neutrale Erzähler ist der Grund warum es am Anfang eine Genderabfrage gibt.{/b}"
    "{b}Warum? Weil es allein bei Formulierungen wie \"Das Kind und seine/ihre Mutter leben zusammen.\" schwierig wird wirklich Genderneutral zu schreiben{/b}"
    "{b}Durch die Genderabfrage werden alle Texte des Neutralen Erzählers direkt auf die Wahl des passenden Pronomens angepasst.{/b}"
    n "Dies ist die Geschichte von [name]."
    n "[name] ist ein sechsjähriges Kindergartenkind, dass seit der Scheidung [pro]er Eltern alleine mit [pro]er Mutter zusammen lebt."
    n "Sie sind umgezogen, daher muss [name] jetzt auch auf einen neuen Kindergarten gehen."
    n "Dort kennt [pro2] natürlich noch niemanden."
    n "Jetzt gilt es, neue Freunde zu machen und mit ihnen tolle Abenteuer zu erleben."
    n "[name]'s erster Schritt in die richtige Richtung begann an einem Montag Morgen."    
    "???" "Hey Püpschen! Aufwachen! Du willst doch nicht zu spät kommen!"
    n "[name]'s Mutter schmiss [pro5] jeden Morgen pünktlich aus dem Bett."
    n "Sie arbeitete hart um beide durchzubringen, doch ihr Kind stand immer an erster Stelle."
    n "Und damit dieses den ersten Tag im neuen Kindergarten nicht verpasste, riss sie [pro3] jetzt auch die Decke weg."
    show bg bedroom with dissolve
    show mum talk with moveinright
    m "Guten Morgen mein kleiner Spatz!"
    n "[name] war noch völlig verschlafen."
    p "Guten Morgen Mama ..."
    p "Ich will aber noch nicht aufstehen!"
    m "Ach jetzt stell dich nicht so an. Na komm. Wir ziehen dich gleich an, jetzt gibt's erstmal Essen."
    m "Ich hab Pfannenkuchen gemacht! Heute ist doch dein großer Tag!"
    p "Pfannkuchen! Jaaa! Mama ich hab dich lieb!"
    n "Besänftigt und plötzlich ganz wach, sprang [name] aus [pro]em Bett und folgte [pro]er Mutter in die Küche."
    show bg kitchen with dissolve
    n "Dort angekommen wurde aufgetischt und sich hingesetzt."
    m "Freust du dich schon deine neuen Freunde kennenzulernen?"
    menu:
        "Jaaaaaa!":
            $ happytogo = True
            n "[name] trommelte mit kleinen Fäustchen auf den Tisch, zappelte mit den Beinen und freute sich ganz offensichtlich riesig."
            m "Das ist schön. Du kommst bestimmt in eine Gruppe mit ganz tollen anderen Kindern."
        
        "Ja...":
            $ happytogo = False
            n "[name] sah nur auf [pro]en Teller herunter während [pro2] die Antwort murmelte. Alles war besser als Mama mit der Wahrheit zu verletzen."
            n "Doch Mütter bemerken bekanntlich alles."
            m "Ach Spätzchen... Bist du doch noch so traurig, dass du deine alten Freunde nicht mehr siehst?"
            m "Hey, schau mich an, nicht dein Essen. Alles wird gut, okay? Komm her, lass dich mal knuddeln."
            n "Sie nahm ihr[suf] [pro4] kräftig in den Arm und wuschelte [pro3] durch die Haare."
            n "[name] schien das zu gefallen, denn [pro2] strahlte plötzlich bis zu den Ohren."
            m "Siehst du? Alles garnicht mehr so wild."
            m "Du kommst heute bestimmt in eine Gruppe mit ganz tollen Kindern, wirst schon sehen!"
             
    n "Als sie mit dem Frühstück fertig waren, wurde [name] fertig für den Kindergarten angezogen und beide machten sich auf den Weg."       
    "{b}Ende: Erwachsener Erzähler{/b}"
    jump narrationoptions
    ##### Szene 3 #####
label scene3:
    scene bg street with dissolve
    if seenscene == False:
        menu:
            "Freut sich das Kind auf den Kindergarten?"
            "Ja.":
                $ happytogo = True
                
            "Nein.":
                $ happytogo = False
        
    show mum talk at center
    play music maintheme
    if happytogo == True:
        n "Ich weiß noch wie aufgeregt ich damals war. Ich hatte mich gefragt wie die anderen Kinder wohl auf mich reagieren würden."
        n "Ich hatte gehofft schnell neue Freunde zu finden und war obwohl ich mich auf den Tag gefreut hatte, froh meine Mama an meiner Seite zu haben."
        m "Das wird ein ganz toller Tag, glaub mir!"
    else:
        n "Ich weiß noch wie viel Angst ich damals hatte. Alles war so neu und ich war unsicher ob ich schnell neue Freunde finden würde."
        n "Ich war nur so froh, dass meine Mama bei mir war."
        m "Gleich sind wir da. Keine Angst, das wird schon! Du wirst bestimmt viele neue Freunde finden."
    n "Mein neuer Kindergarten war ein Gemäuer mit alten Fenstern und Backsteinwänden, welches einen sehr einschüchternden Eindruck auf mich hatte."
    scene bg grura with dissolve
    show mum n at slightleft with moveinleft
    show heide n at slightright with moveinright
    n "An meinem ersten Tag wurden Mama und ich dann auch noch von einer verbitterten, alten Frau begrüßt."
    n "Frau Heidenau. Wir allen hatten Angst vor ihr. Und bis heute noch denke ich nicht gerne an sie."
    n "Ich weiß noch wie ich mich während Frau Heidenau und meine Mutter sich unterhielten zwanghaft versuchte unsichtbar zu machen, was auch klappte! Also zumindest bis man mich direkt ansprach."
    hide mum
    show heide talk at center with move
    h "Ah. Der Neuzugang. Ich bin Frau Heidenau. Wie ist dein Name Junge?"
    menu:
        "Selbst vorstellen.":
            p "Ich bin der [name] und schon 6 Jahre alt!"
            h "Hmpf. [name] also. Wieso sollte man sein Kind bitte [name] nennen?"
            show mum mad at left with moveinleft
            m "Na jetzt hören Sie aber mal ..."
            show heide mad
            h "Papperlapapp!"
            hide mum with moveoutleft
            show heide talk
            h "Ihr Kind ist bei uns bestens aufgehoben. So \"[name]\", deine Gruppe ist die Käfergruppe, die Karin kümmert sich um dich."
            h "Mitkommen!"
            n "Frau Heidenau hatte mich dann in Richtung des Gruppenraumes gezogen, während meine Mutter besorgt hinterherlief."
            n "Sie schien mich noch nicht mit dieser Frau allein lassen zu wollen."
            h "Hier Karin. Ein Neuer. Ich muss jetzt weitermachen. Ich erwarte nachher deinen Bericht."
        
        "Mutter hilfesuchend ansehen.":
            show heide n at slightright with move
            show mum talk at slightleft with moveinleft
            p "Äh... I... ich..."
            m "Na komm, sag deinen Namen. Das kannst du doch!"
            p "..."
            m "Na gut, ich mach das für dich. Aber das nächste Mal stellst du dich selbst vor!"
            m "Mein Kind heißt [name] und ist schon 6 Jahre alt. Sie merken ja schon, [name] ist etwas zurückhaltend aber das legt sich mit der Zeit, keine Sorge."
            h "[name]... Wirklich? Was für Namen geben Eltern ihren Kindern bloß heutzutage?"
            show mum mad
            m "Jetzt hören Sie aber mal ..."
            show heide mad
            h "Papperlapapp!"
            show mum n
            show heide talk
            h "Ihr Kind ist in der Käfergruppe. Die Gruppenleitung heißt Karin, das ist die Dicke in dem Raum da hinten."
            h "Wenn es schon nicht reden kann bringen Sie es am Besten selbst. Vielleicht hilft das."
            h "Guten Tag!!"
            hide heide
            show mum at center with move
            n "Nachdem meine Mutter diese Abfertigung verwunden hatte, brachte sie mich zum Gruppenraum. Dort angekommen lernte ich dann auch Karin kennen."

        
    
    hide heide with moveoutleft
    hide mum with moveoutleft
    show karin n with moveinright
    n "Karin machte nie den Eindruck als ob sie an ihrer Arbeit Spaß hatte. Vielleicht ist ihr das bei ihrer Chefin aber auch nicht zu verübeln gewesen."
    k "Ahh, hallo sie beide. Danke, dass Sie ihr Kind gebracht habe. Sie können unbesorgt sein, wir kümmern uns ganz wunderprächtig um ihn."
    k "Also willkommen dann, in der Käfergruppe!"
    show karin go
    k "Kinder, kommt mal alle zusammen, wir haben Neuzugang bekommen!"
    hide karin
    show anja what at left with moveinleft
    show eve happy2 at right with moveinright
    show octa happy at center
    show louis really at slightright behind octa
    show randy happy at slightleft behind octa
    with moveinbottom
    k "Das sind deine neuen Freunde! Stell dich uns allen doch mal vor, wir wissen ja noch garnicht wie du heißt."
    
    menu:
        "Vorstellen.":
            $ menu_choice3 = "yes"
            p "Hallo ich bin [name]! Lasst uns Freunde sein!"
            k "Da hört ihr's Kinder. Ich hoffe ihr freundet euch alle mit [name] an.!"
            
            
        "Schweigen.":
            $ menu_choice3 = "no"
            p "..."
            n "Während ich kein Wort rausbrachte und mich alle anstarrten hörte ich hinter mir Karin und meine Mutter reden."
            m "Ohh, entschuldigen Sie Frau ..."
            k "Einfach Karin reicht."
            m "Ohh, in Ordnung. Entschuldigen Sie Karin, [name] ist noch etwas schüchtern und ..."
            k "Alles gut. Also Kinder, das hier ist [name], ich hoffe ihr alle könnt Freunde werden."
        
        "Stammeln.":
            $ menu_choice3 = "meh"
            p "I.. ich.. also ich b-b-bin..."
            k "Du brauchst keine Angst haben."
            k "Komm, sag mir wie du heißt, dann stell ich dich vor."
            p "...[name]..."
            k "Also Kinder, das hier ist [name], ich hoffe ihr alle könnt Freunde werden."
            
            
    
    ##### Szene 4 #####
label scene4:
    stop music fadeout 1.0
    pause 0.5
    play music octatheme fadein 1.0
    scene bg grura with dissolve
    show karin talk at slightright with moveinright
    show mum talk at slightleft with moveinleft
    k "Sie können Ihr Kind dann jetzt auch bei uns lassen. Wir kümmern uns bis sie zum Abholen vorbeikommen."
    m "Rufen Sie mich einfach sofort an falls irgendwas sein sollte."
    k "Natürlich, natürlich. Überhaupt keine Frage."
    m "Na dann [name]. Viel Spaß an deinem großen Tag. Und jetzt lass dich noch mal knuddeln!"
    p "Tschüss Mama, ich hab dich lieb!"
    hide mum with moveoutleft
    show karin at center with move
    k "Dann fangen wir doch jetzt auch gleich mal an."
    k "Wir machen jetzt Morgenkreis. Stell dich einfach da hin und warte ab. Brav sein!"
    n "Der Morgenkreis war ein Ritual zu dem Karin uns jeden Tag zusammenrief. Wir spielten, sangen, musizierten oder lernten zusammen."
    k "Sind alle da?"
    hide karin
    show anja what at left with moveinleft
    show eve happy2 at right with moveinright
    show octa happy at center
    show louis really at slightright behind octa
    show randy happy at slightleft behind octa
    with moveinbottom
    k "Gut, dann legen wir mal los... Wir spielen wieder das Käfergruppenlied! Holt doch alle schonmal eure Instrumente aus der Kiste."
    n "Natürlich wussten alle was gemeint war. Außer mir. Ich kam mir damals ziemlich hilflos vor, da drückte mir plötzlich ein Mädchen ein paar Klanghölzer in die Hand."
    hide anja
    hide randy
    with moveoutleft
    hide eve
    hide louis
    with moveoutright
    
    show octa music at center
    o "Hallo! Du bist neu, oder? Ich bin Octavia. Das sind Klanghölzer, weißt du oder? Das kannst du doch, oder?"
    menu:
        "Ja! Die sind voll lustig!":
            $ boomstick = True
            o "Find ich auch! Und voll einfach. Ich kann das hier am Besten, sagt meine Mama mir auch immer."
            
        "Ähm, nein ... Noch nie ...":
            $ boomstick = False
            o "Was, du kannst das garnicht?"
            o "Die anderen sagen das ist voll schwer. Find ich nicht. Ich bin die Beste damit!"
    
    n "So war sie immer, so ehrgeizig. Sie musste jederzeit jedem beweisen, dass sie besser war als alle anderen."
    show octa music at left with move
    show karin music at right with moveinright
    k "Also Kinder, alle bereit? Dann 1 und 2 und 3 und ..."
    "Minigame geht los. Takt halten."
    "Minigame steht noch nicht, von daher Choice:"
    menu:
        "Hast du das Minispiel gewonnen oder verloren?"
        
        "Gewonnen.":
            hide karin
            show octa mine at center with move
            o "Das hat Spaß gemacht! Aber ich war die Einzige die alles richtig gemacht hat."
            if boomstick == True:
                show octa smug
                o "Ich dachte du kannst das? Irgendwie war ich trotzdem viel besser als du."
            else:
                show octa smug
                o "Du hast doch gesagt du kannst das nicht? Egal. Ich war ja auch viel besser als du."
            
        "Verloren...":
            hide karin
            show octa mine at center with move
            o "Das hat Spaß gemacht! Aber ich war die Einzige die alles richtig gemacht hat."
            if boomstick == True:
                show octa smug
                o "Du hast alles falsch gemacht! Du hast doch gesagt du kannst das. Ich war viel, viel besser als du."
            else:
                show octa smug
                o "Du warst nicht gut ... Ich hab zugeschaut, weißt du?"
            
    n "Der Morgenkreis ging musikalisch weiter, alle waren voll dabei, ganz egal wie musikalisch oder unmusikalisch sie waren."
    n "Die Zeit damals scheint mir so simpel gewesen zu sein. Uns allen ging es um den Spaß zusammen, nicht ums besser sein."
    n "Naja, uns allen. Außer Octavia."
    hide octa with dissolve
    show karin go at center with dissolve
    
    k "Das habt ihr gut gemacht Kinder!"
    k "Aber jetzt ist genug, auf zum Frühstück mit euch. Husch husch, wir haben ja nicht den ganzen Tag Zeit."
    
    ##### Szene 5 #####
label scene5:
    stop music fadeout 1.0
    pause 0.75
    play music anjatheme fadein 1.0
    scene bg food
    show anja eat at center
    with fade
    n "Damals kannte ich noch niemanden und war mir unsicher wo ich mich hinsetzen sollte, schließlich kannte ich ja noch niemanden."
    n "Als dann sowieso nur noch wenige Plätze frei waren setzte ich mich einfach auf den erstbesten Stuhl, der mir ins Auge fiel."
    n "Neben mir saß ein Mädchen und es entwickelte sich schnell eine recht einseitige Unterhaltung..."
    a "Hey, wie findest du die Frau Heidenau?"
    p "Also, ich-..."
    a "Ich find die blöd… Die anderen Erzieherinnen sind eigentlich echt nett."
    p "Ja, die ist gru-..."
    a "Aber wenn die Frau Heidenau auf uns aufpasst macht es keinen Spaß. Mama sagt das is ne Greiterhex, keiner mag die."
    p "Was ist eine Grei-..."
    a "Und kennst du schon Evelyn? Die sitzt immer nur da und malt, find ich voll langweilig."
    p "Nein die-..."
    a "Boah und die Octavia, die will immer in allem \"die Beste\" sein."
    p "Die kenn ich scho-..."
    
    if menu_choice3 == "yes":
        a "Du heißt [name] oder? Ich bin Anja!"
        
    elif menu_choice3 == "no":
        a "Du bist neu, oder? Wie heißt du überhaupt?"
        p "Ich hei-..."
        a "Ach Karin hat [name] gesagt. Mein Name ist Anja!"
        
    else:
        a "Wieso hast du dich denn beim Morgenkreis so komisch vorgestellt?"
        p "Ich..."
        a "Das fand ich voll lustig wie du so komisch geredet hast. Du bist [name] oder? Ich bin Anja."
        
    a "Kletterst du? Bestimmt."
    a "Wir können auch mal zusammen klettern wenn du willst. Ich kletter immer wenn wir auf den Hof dürfen auf meinen Kletterbaum."
    a "Also du kannst ja klettern. Wenn nicht bring ich's dir bei. Mama und ich gehen auch immer zusammen in den Kletterwald."
    a "Da hat Mama auch mal die Greiterhex gesehen. Ich nicht. Aber Mama."
    a "Naja, einmal wäre ich fast vom Kletterbaum gefallen weil ich nicht aufgepasst hab’, aber dann hab’ ich mich doch noch festgehalten, das war voll knapp!"
    a "Klettern ist nämlich gefährlich, weißt du? Meine Mama sagt mir auch immer, dass ich vorsichtig sein soll, aber ich bin noch nie irgendwo runtergefallen, und du?"
    n "Das war Anja. Man kam eigentlich nie zu Wort. Wäre das Frühstück nicht irgendwann zu Ende gewesen, so hätte ich wohl bald all ihre Klettergeschichten gekannt."
    n "So aber floh ich bei der erstbesten Gelegenheit. Anja war einfach zu viel für mich an meinem ersten Tag."
    
    ##### Szene 6 #####
label scene6:
    scene bg grura with dissolve
    stop music fadeout 1.0
    pause 0.5
    play music evetheme fadein 1.0
    n "Ich floh also in den einzig anderen Raum der mir bekannt vorkam und sah dann am Tisch ein einzelnes Mädchen sitzen, dass in aller Seelenruhe am Malen war.."
    show eve draw at center with moveinbottom
    n "Das war Evelynn. Sie war etwas zurückhalten aber sehr talentiert und dass sie bei unserer ersten Begegnung zeichnete war nur allzu passend für sie."    
    p "Hallo du da. Ich bin [name] und wer bist du?"
    e "Evelynn."
    p "Hallo Evelynn! Wollen wir Freunde sein?"
    e "Okay."
    p "Was machst du da?"
    e "Malen."
    p "Aber was denn?"
    show eve paper
    e "Das hier."
    hide eve
    show dis leuchtturm
    with dissolve
    e "Schau, hier. Das hab ich gemalt."
    
    menu:
        n "Wie findest du das Bild?"
        
        "Das sieht toll aus!":
            hide dis leuchtturm
            show eve shy2
            with dissolve
            e "Dankeschön!"
            show eve happy2
            e "Wir haben zu Hause ein Buch mit ganz vielen Bildern und da ist auch so ein Leuchtturm drin."
            e "Ich mag das Buch. Immer wenn mir was gefällt mal ich das dann hier. Mama sagt ich darf nicht so viel nach draußen also male ich gerne."
            e "Und Leuchttürme haben so tolle rote Streifen! Aber ich fänd viel toller wenn sie goldene und violette Streifen hätten."
            e "Also mach ich meine so, weil die sind ja dann viel schöner."
            p "Ich kann garnicht so toll malen wie du. Zeig mir das!"
            show eve draw
            e "Hmm... Nein."
            p "Doch!"
            e "Ich lerne selbst noch, ich kann dir das nicht beibringen."
            e "Mal doch einfach was, dann lernst du das."
            
        "Was ist das?":
            hide dis leuchtturm
            show eve mad
            with dissolve
            e "Weißt du denn garnicht was ein Leuchtturm ist?"
            menu:
                "Nein...":
                    show eve shy2
                    p "Nein, weiß ich nicht. Aber ich mag dein Bild!"
                    e "Ich hab auch noch nie einen Echten gesehen."
                    show eve happy2
                    e "Aber wir haben zu Hause ein Buch da ist einer drin."
                    e "Das ist der aus dem Buch. Nur anders. Also weil ich ihn male."
                    e "Weil ... ich kann das noch nicht so ... Aber ich übe!"
                    show eve draw
                    p "Aber das sieht doch toll aus!"
                    e "Aber nicht so wie es soll!"
                    e "Aber jetzt weißt du was das ist. Dann kannst du auch einen malen!"
                    
                "Leuchttürme sehen ganz anders aus.":
                    p "Also ich war schonmal mit meinen Eltern bei einem Leuchtturm und der sah ganz anders aus."
                    show eve mad
                    e "War wohl ein blöder Leuchtturm."
                    e "Oder du lügst."
                    show eve draw
                    e "Ich muss jetzt weiter üben."
                    
            
        "Das kann ich aber besser.":
            hide dis leuchtturm
            show eve mad
            with dissolve
            e "Angeber."
            e "Geh weg."
            show eve draw

    
    hide eve
    stop music fadeout 1.0
    pause 0.75
    play music maintheme fadein 1.0
    n "Evelynn sollte mich zukünftig noch häufiger dazu motivieren selbst kreativ zu sein."
    n "Aber an dem Tag ließ ich sie erstmal in Frieden, sie war ohnehin fast sofort wieder in ihrer eigenen Welt versunken."
    n "Und damit war mein erster Tag auch vorbei. Ich hatte so viele neue Kinder kennengelernt und einige von ihnen sollten einen großen Einfluss auf mich haben."
    show mum happy at center with moveinleft
    m "Hallo Püpschen!"
    m "Komm lass dich drücken! Hattest du heute viel Spaß?"
    p "Jaaa! Ich hab gemalt und gespielt und Klangholz gespielt und ..."
    m "Haha, so viel also! Komm, erzähl mir den Rest auf dem Weg nach Hause."
    p "Okay Mami."
    hide mum
    show bg street with dissolve
    p "Also, da waren die Octavia, die Anja und die Evelynn ... ... ..."
    ##### TAG 1 ENDE #####

    ##### TAG 2 BEGINN #####
    ##### Szene 7 #####
label scene7:
    scene bg grura
    show karin music at center
    with dissolve
    n "Der zweite Tag verlief viel weniger chaotisch. Ich hatte mich schnell eingelebt, wie das als Kind nunmal so ist."
    n "Ich weiß noch, dass wir singen mussten ... Karin war sehr übereifrig dabei und wir hatten alle keine Lust."
    
    
    ##### Szene 8 #####
label scene8:
    n "Als dann zum Essen aufgerufen wurde, war ich schneller als sonst. Diesmal wollte ich mir nicht das Ohr abkauen lassen, deshalb setzte ich mich zu Evelynn, welche ganz allein saß..."
    scene bg food
    show eve foodplay at center
    with dissolve
    stop music fadeout 1.0
    pause 0.5
    play music evetheme fadein 1.0
    p "Hallo du!"
    show eve foodask
    e "Hallo..."
    p "Was machst du da?"
    show eve foodplay
    e "Malen..."
    
    menu:
        
        "Interesse zeigen.":
            show eve foodplay
            p "Warte du ..."
            p "Ohh toll! Du malst ja wirklich!"
            p "Das kannst du mit deinem Essen machen?"
            e "Ja natürlich! Man kann mit allem malen, wenn man nur möchte. Mit den Nudeln hier sogar  \"ganz hervorragend\"."
            p "Ganz was?"
            e "Sagt Papa immer so."
            p "Ach so. Ich ess dann jetzt mal."
            show eve foodmad
            e "Warte!"
            p "Was... was ist?"

            
        "Igitt....":
            p "Aber warum denn mit deinem Essen... Das ist doch ekelig."
            show eve foodmad
            e "Garnicht wahr. Das ist schön, guck doch mal."
            p "Jetzt hast du alles an den Fingern kleben."
            p "Malen macht man mit Stiften, nicht mit Essen."
            show eve foodplay
            e "Mir macht das aber Spaß."
            p "Aber das kann man doch nicht mehr essen!"
            show eve foodmad
            e "Darum geht es doch auch garnicht!"
            
        "WAS tust du?!.":
            p "Ihhh! Mama sagt man spielt nicht mit Essen!"
            show eve foodmad
            e "Meine auch. Aber ich spiele ja auch garnicht. Ich male."
            show eve foodplay
            e "Außerdem ist meine Mama gerade nicht hier. Und deine auch nicht."
            p "Hmm... Das sieht eigentlich ganz lustig aus."
            
            
    show eve foodask
    

    menu:
        e "Versuch es doch einfach auch mal."
        
        "Au ja!":
            scene cg foodplay with dissolve
            e "Nicht schlecht. Man kann fast erkennen, dass du ein Haus bauen wolltest."
            p "Das soll doch aber eine Burg sein!"
            e "Ohh! Ja stimmt, wenn man es weiß. Du musst aber wirklich noch üben."
            
        "Nein, sicher nicht.":
            scene cg food with dissolve
            p "Nein ... nein ich esse lieber ganz normal. Ich will mich nicht schmutzig machen."
            e "Dann nicht ..."
    ##### TAG 2 ENDE #####
    
    ##### TAG 3 BEGINN #####
    ##### Szene 9 #####
label scene9:
    stop music fadeout 1.0
    pause 0.75
    play music maintheme fadein 1.0
    scene bg bedroom with dissolve
    "???" "{b}KICKERIKI! KICKERIKI! KICKERIKI!{/b}"
    p "Waaah!"
    p "Hilfe! Was ist das?! Mama!!!"
    "???" "{b}KICKERIKI! KICKERIKI! KI...{/b}"
    show mum talk at center with moveinright
    m "Guten Morgen Püpschen!"
    m "Ich hab dir was mitgebracht!"
    show mum at slightleft with move
    show dis hahn at chicken with dissolve
    p "Eine Ente!"
    m "Fast! Aber mit dem hier kommst du bestimmt leichter aus den Federn."
    scene bg street with dissolve
    n "Auf dem Weg zum Kindergarten erklärte sie mir dann, dass mein Wecker ein Hahn sei, keine Ente und was die Unterschiede sind."
    n "Ich sollte nun täglich von diesem Hahn geweckt werden, zusammen mit meiner Mutter die sich darüber köstlich amüsieren konnte."
    n "Den Wecker hab ich nie weggeschmissen."
    scene bg grura
    show karin talk
    with dissolve
    k "Also Kinder, ich hab euch heute etwas mitgebracht."
    show karin happy
    k "Das ist ein Radio, mit Mikrofon! Damit können wir singen und uns anhören was wir gesungen haben."
    show karin shock at slightright with move
    show octa mad at slightleft with moveinleft
    o "Öhhhh!"
    show randy mad at left with moveinleft
    r "Wir haben doch gestern schon gesungen!"
    o "Genau, wir haben keine Lust!"
    n "Und plötzlich verschwor sich der gesamte Raum gegen die arme Karin. Das passierte recht oft. Und wir haben immer gewonnen."
    show karin mad
    k "Aber jetzt hab ich doch extra den Recorder für euch mitgebra..."
    r "Aber singen ist blöd."
    show karin n
    k "In Ordnung ... Und was wollt ihr dann machen?"
    show octa smug
    o "Du bist!"
    show octa vhappy
    o "Los! Rennt!"
    hide randy with moveoutleft
    hide octa with moveoutleft
    show karin shock at center with move
    k "Aber ... Hey! Halt! Kinder, kommt gefälligst zurück!"
    show karin mad
    k "Benehmt euch! Ich ... ach was solls."
    show karin go
    k "Vorsicht, jetzt komm ich!" 
    hide karin with moveoutleft
    
    ##### Szene 10 #####
label scene10:
    show bg food
    with dissolve
    n "Nachdem Karin uns dann endlich wieder alle einfangen hatte war es Zeit zum Essen."
    n "Ich hatte mich an den nächstbesten Tisch gesetzt und wollte die Apfelstücke essen die meine Mama mir gemacht hatte, als plötzlich ..."
    show louis smug at center with moveinright
    "???" "Hey, was isst du da?"
    n "Vor mir stand ein Junge in Lederjacke mit Sonnenbrille und gegelten Haaren. Das war ein Junge den ich bisher nur beiläufig gesehen hatte."
    n "E musste ein Jahr länger im Kindergarten bleiben, also war er älter als wir anderen und seine Freunde waren fast alle schon in der Schule, daher gab er sich nur mit wenigen von uns ab."
    p "Apfel! Glaub ich ... Hat meine Mama mir gemacht!"
    p "Warte mal, wer bist du eigentlich?"
    show louis talk
    L "Mein Name ist Louis."
    p "Wieso?"
    show louis really
    L "Vielleicht weil ich Louis heiße?"
    p "Nein... Also ... Wegen dem Apfel ..."
    show louis happy
    L "Hahaha, ach so!"
    show louis talk
    L "Hör zu. Mein Papa hat mir Süßigkeiten mitgegeben. Du hast nur Äpfel, also dachte ich du willst sie mir vielleicht ..."
    show louis smug
    L "... abkaufen."
    p "Aber Äpfel sind doch auch süß!"
    show louis really
    L "..."
    p "Außerdem hab ich kein Geld."
    L "Du bist neu hier."
    p "Ja. Wieso?"
    show louis talk at slightleft with move
    show dis snackers3 at chicken with dissolve
    L "Ich mag eigentlich einfach keine Erdnüsse aber ich hab hier 3 Snackers."
    L "Du kannst die haben wenn du mir bis Freitags zwei Knappers mitbringst."
    p "Aber das ist doch unfair. Oder?"
    L "Knappers sind wirklich etwas besser..." 
    L "Okay, weil du neu bist, musst du mir nur ein Knappers mitbringen."
    hide dis snackers3 with dissolve
    show louis n at center with move
    menu:
        L "Also, was sagst du?"
        
        "Ja.":
            $ snackersdeal = True
            n "Gerne!"
            show louis talk
            L "Dann sind diese 3 Snackers für dich."
            show louis n
            L "Und ich nehm mich noch ein Stück Apfel von dir."
            p "Hey!"
            L "Hab dich nicht so. Du hast jetzt alles was ich dabei hatte."
            p "Okay ..."
            show louis happy
            L "Und nicht vergessen! Bis Freitag will ich ein Knappers. Ist nämlich mein Lieblingskeks."
            p "Knappers sind doch keine Kekse."
            show louis really
            L "..."
            show louis mad
            L "NEIN! Deswegen streite ich mich nicht nochmal!"
            show louis smug
            L "Aber egal, falls du mal was zum Naschen brauchst, kannst du mich einfach ansprechen."
            L "Ich habe Freunde in der Schule und über die komme ich an fast alles, außer an Knappers weil es die in meinen Dorf nicht gibt."
            p "Okay...?"
            show louis happy
            L "Und weg bin ich!"
            hide louis with moveoutbottom
            p "Ohh warte Louis ich ... Ohh Mist ... Wir haben doch garkeine Knappers zu Hause. Das muss ich Mama erzählen, sonst ist Louis böse auf mich."
            
        "Nein.":
            $ snackersdeal = False
            p "Meine Mama meint, man soll nicht mit irgendwelchen Leuten sich auf etwas langfristiges einlassen!"
            show louis really
            L "Ääähm, was?"
            p "Ich hab gerade keine Knappers und wenn ich die am Freitag mitbringen soll ist das doch etwas langfristiges."
            L "Ich… Ich glaube ja, aber…"
            p "Also, nein ich will nichts von dir kaufen!"
            show louis smug
            L "T-tauschen!"
            p "Egal!"
            show louis really
            L "Schon gut, schon gut!"
            show louis smug
            L "Aber hey, ich kann dank meinen Freunden in der Schule eigentlich fast alle Süßigkeiten besorgen."
            L "Wenn du es dir mal anders überlegst komm zu mir mit 2 Knappers."
            L "Ich muss jetzt weg. Irgendwer tauscht schon. Dein Pech!"
            hide louis with moveoutright
            p "... Was für ein komischer Kerl."
            p "Jetzt zurück zu meinem Apfel... Hey! Da fehlt ja die Hälfte. Louis hat doch nicht ...?"
    

    ##### Szene 11 #####
label scene11:    
    show karin happy at center with moveinright
    $ gone = False
    k "Kinder, schaut mal an wie schön es draußen ist! Wenn ihr fertig gegessen habt, dann zieht euch an und geht auf den Hof zum spielen."
    scene bg court with fade
    stop music fadeout 1.0
    pause 0.5
    play music anjatheme fadein 1.0
    n "Ich weiß noch, dass ich eigentlich vorhatte mich einfach nur ins Gras zu legen, weil ich keine Lust zum spielen hatte."
    n "Aber meine neuen Freunde hatten scheinbar andere Pläne mit mir."
    n "Bereits aus der Ferne hatte ich lautes Gezanke gehört und ich war schon als Kind sehr neugierig.."
    n "Ich sah Anja auf einem Baum sitzen, die sich mit einem anderen Kind am Boden lautstark stritt."
    show anja vmadb at right with dissolve
    a "Is doch a völligs Gschmarre wos du dou verzüllst."
    show randy vmad at left with dissolve
    "???" "Gibt doch viel besseres was man damit machen kann. Also wieso Eis!?"
    
    menu:
        
        "Stumm abwarten.":
            $ daze = False
            show randy mad
            "???" "Ist doch einfach Geschmackssache und ich will das Eis essen, dass ich essen will."
            show anja madb
            a "Aber das schmeckt doch nur wenn noch was dazugegeben wird."
            "???" "Es schmeckt immer besser!"
            show anja vmadb
            a "UGHHH!"
            show anja madb
            a "Hey. Du! [name]! Schoko oder Vanilleeis!? Du entscheidest das jetzt."
            menu:
                p "Ähm... Ich glaube ..."
                
                "Schoko ist besser!":
                    show anja happyb
                    a "HAH! Da hasts Randy! Jetzt sind wir schon 2."
                    r "Ist doch egal, wenns Geschmackssache ist. Jetzt machts aber eh keinen Sinn mehr da noch zu reden."
                    r "Ich geh jetzt, macht das was ihr wollt ..."
                    hide randy with moveoutleft
                    show anja at center with move
                    p "Warum habt ihr euch denn jetzt eigentlich gezankt?"
                    a "Ich wollte nur etwas sticheln, dann wurde ich wirklich wütend."
                    a "Du, komm mal mit hoch."
                    
                "Vanille ist besser!":
                    show randy vhappy
                    "???" "Ha! Siehst du ist doch nur Geschmackssache! Selbst dein zufälliger Freund stimmt mir zu!"
                    a "Ich mein, ... ja ... also ... [name] fall mir doch nicht einfach in den Rücken!"
                    a "Egal. Dafür kannst du immernoch nicht klettern Randy."
                    show randy mad
                    r "Ach lass mich doch in Ruhe..."
                    hide randy with moveoutleft
                    show anja happyb at center with move
                    p "Hey [name]. Kannst du klettern? Komm mal mit hoch."

            
        "Versuchen den Streit zu stoppen.":
            $ daze = True
            p "Hey! HEY! HÖRT AUF!"
            p "Hört doch auf zu streiten! Das macht doch keinen Sinn"
            show anja vmadb
            show randy vmad
            "{color=#0099ff}???:{/color} Belauscht du uns einfach? Was soll das?\n{color=#0099ff}Anja:{/color} Misch dich nicht ein!"
            p "Aber ich wollte doch nur ..."
            show randy shock
            show anja happyb
            a "Oooh, ähm da haben wir wohl eine gleiche Meinung."
            show randy mad
            "???" "Sieht wohl so aus, ich will aber nicht weitere belauscht werden."
            "???" "Ich gehe. Macht doch was ihr wollt."
            hide randy with moveoutleft
            show anja madb at center with move
            a "Hast du ja toll gemacht [name]."
            p "Warte mal, worum ging es eigentlich?"
            show anja happyb
            a "Hehe, du hast also nicht alles gehört? Dann sag ich auchs nicht."
            p "Komm schon!"
            a "Erst wenn du hier hoch kommst!"


    
    
    menu:
        "Kletterst du zu Anja auf den Baum hoch?"
        
        "Ich kann nicht klettern.":
            p "Also, ähm... Ich kann nicht klettern."
            show anja madb
            a "Probiers doch wenigstens."
            p "Ich trau mich nicht ... Ich kann das nicht!"
            show anja happyb
            a "Komm schon, ich zeigs dir auch wies geht."
            menu:
                "Lieber nicht...":
                    $ gone = True
                    p "Nein! Nein, nein! Ich ... ich guck mal wo dein Freund ist."
                    show anja madb
                    a "NA TOLL! Dann geh doch!"
                    n "Ich wusste damals noch nicht wie sehr ich Anja damit verletzt hatte. Ich wollte nur wirklich einfach nicht mit ihr spielen und hatte riesige Angst auf diesen Baum zu klettern."
                    jump scene12
                    
                "Na gut.":
                    p "Okay aber wenn mir was passiert bist du schuld!"
                    a "Jeder kann klettern, ist nur eine Frage der Technik!"
                    p "Ich hoffe ... "
                    a "Warte ich komm erstmal runter ..."
                    play sound cardoor2
                    show anja hihi
                    a "So. Schau erst a mal mir zou."
                    show anja talk
                    a "Nimmst erst as rechte Ba und hebsts an, dann suchst dir mit den Händen nen halt und dann…"
                    show anja happyb
                    a "Bist du auch schon oben. Jetzt du!"
                    p "Wow! Das ging ja schnell. Das sieht so einfach aus."
                    p "Okay also die Hände ..."
                    p "... und die Beine ..."
                    play sound treefall
                    p "... ughh ... dann ... waaahhh!"
                    p "Aua ..."
                    a "Sah doch gut aus, jetzt noch ein bisschen mehr Kraft in den Beinen und du bist oben oder wir machen Räuberleiter."
                    p "Okay ... ich versuchs ..."
                    p "Also Hände ... Beine und ..."
                    p "ICH BIN OBEN!"
                    a "SAUBER!"
                    p "Ich glaubs nicht! Danke!"
            
            
        "Wortlos gehen.":
            $ gone = True
            show anja madb
            a "Hey! Was soll das? Wo willst du hin?"
            show anja vmadb
            a "NA TOLL! Dann geh doch!"
            n "Ich wusste damals noch nicht wie sehr ich Anja damit verletzt hatte. Ich wollte nur wirklich einfach nicht mit ihr spielen."
            jump scene12
            
        "Ich kann klettern.":
            p "Okay, ich komm zu dir hoch."
            p "Klettern ist einfach. Hände hier, Beine da und schon oben. Hallo du!"
            a "Sauber, kannsts ja so gut wie ich. Respekt."
            p "Ja, ich kletter gern am Gerüst herum."
            a "Bäume sind viel schöner, so groß und massiv. Am besten sind aber Zäune, wie die von meiner Oma!"
                
            
    if daze == True:
        p "Aber worum ging es denn jetzt eigentlich?"
        a "Um Geschmack."
        show anja madb
        a "Schokolade ist das Beste und Randy mag eben Vanilleeis mehr."
        a "Ich wollte ihn einfach nur etwas nerven deswegen."
        show anja vmadb
        a "Aber er ist dann immer so langweilig, dass hat mich wütend gemacht."


    show anja madb
    p "Bist du jetzt noch böse?"
    a "Etwas ..."
    
    if snackersdeal == True:
        menu:
            "Willst du deine Snackers mit Anja teilen um sie zu beruhigen?"
            
            "Ja.":
                p "Ich hab ein paar Snackers. Wenn du Schokolade willst, kann ich dir eins abgeben."
                show anja happyb
                a "Bist wohl einer mit Geschmack!"
                p "Ich ... weiß nicht wie ich schmecke ..."
                a "Hahaha!"
                a "Aaahh, Super. Jetzt gehts mir besser."
                
            "Nein":
                jump treetalk
                
label treetalk:
    p "Also das war jetzt ... Randy? Wie ist der so? Ist der nett?"
    show anja madb
    a "Ganz komischer Kauz."
    show anja happyb
    a "Er ist ein echt netter Kerl und ich bin auf seinen Geburtstag am Freitag eingeladen."
    a "Er ist einer meiner besten Freunde, aber er ist eben so unglaublich Normal, dass treibt mich manchmal echt an die Decke."
    p "Und ihr ... "
    a "Außerdem sind wir so oft anderer Meinung und du hasts ja gesehen."
    show anja madb
    a "Er hat immer den gleichen Standpunkt und wenn er darüber redet ist er sooo laaangweilig, ich weiß nicht was das soll."
    p "Ist das denn so schlecht?"
    a "Eigentlich nicht, aber es nervt mich."
    show anja happyb
    a "Was er aber mag sind Filme mit riesigen Monstern die miteinander kämpfen."
    a "Er hat einen Bruder bei den er die Filme immer anschauen kann."
    a "Sein Bruder ist super nett."
    p "Was für Fil-..."
    a "Die Gozok Reihe, Omegas und so weiter."
    a "Kannst du ja vielleicht kennenlernen, ich kann ja mal mit Randy reden ob du auch am Freitagauch auf seinen Geburtstag kommen kannst…"
    show anja talk at slightleft with move
    n "So verliefen die meisten meiner Gespräche mit Anja. Ich kam nicht zu Wort und sie redete ohne Unterlass."
    show mum talk at right with moveinright
    n "Wenn mich meine Mutter nicht irgendwann abgeholt hätte, säßen wir wohl noch heute in dem Baum und ich wüsste mittlerweile alles über jeden."
    
    ##### Szene 12 #####
label scene12:
    stop music fadeout 1.0
    scene bg bedroom
    show mum happy at center
    with dissolve
    play music maintheme fadein 1.0
    
    m "Und wie hat es dir heute gefallen?"
    p "Gut, wir hatten ganz viel Spaß. "
    
    if gone == False:
        m "Das Mädchen schien ja sehr ... nett zu sein."
        p "Das war die Anja die redet immer viel."
        m "Das ... hab ich gemerkt." 
    
    p "Und ich hab heute Randy getroffen!"
    m "Wer ist denn der Randy?"
    p "Auch ein Kindergartenkind. Mama das ist doch klar."
    m "Haha, ja du hast Recht. Wie ist der denn so?"
    p "Nett. Vielleicht lädt er mich zu seinem Geburtstag ein!"
    p "Darf ich dann Mama? Darf ich?"
    m "Ich freu mich, dass du so viele Freunde machst. Wenn er dich einlädt darfst du auch gehen."
    
    if snackersdeal == True:

        menu:
            "Mama fragen ob wir Knappers kaufen können.":
                $ hasknappers = True
                p "Aber du, haben wir noch Knappers?"
                m "Ohh nein Schatz, davon haben wir keine mehr. Warum denn?"
                p "Ohh ich will... einfach nur mal wieder welche haben."
                m "Ich schlag dir was vor."
                p "Was denn?"
                m "Du hilft mir morgen in der Küche, dann bekommst du ein Knappers."
                p "Mach ich Mama!"
                
            "Mama nichts von den Knappers erzählen.":
                $ hasknappers = False
        ##### TAG 3 ENDE #####
        
        ##### TAG 4 BEGINN #####
        ##### Szene 13 #####
label scene13:
    stop music fadeout 1.0
    scene bg street
    show mum happy at center
    with dissolve
    play music octatheme fadein 1.0
    m "Hey Püpschen, Mama muss heute ganz schnell los. Schaffst du das alleine rein? Ich lass dich gleich am Hof raus."
    p "Mama ich bin doch schon groß!"
    m "Haha, ja mein Schatz, das bist du."
    p "Sag ich doch immer!"
    m "Tust du! So, da sind wir. Wir sehen uns nachher! Benimm dich und ich hab dich lieb!"
    scene bg court with dissolve
    p "Tschüss Mama, hab dich auch lieb!"
    play sound cardoor2
    n "Heute sollte ich Octavia von einer anderen Seite kennenlernen. Ich weiß noch, ich war fast schon im Kindergarten, als hinter mir noch ein Auto auf den Hof fuhr."
    n "Octavia, in volle Schutzmontur gekleidet, stieg aus dem Wagen. Danach ihre Eltern, die ihr Fahrrad aus dem Kofferraum luden. Bisher hatte ich immer gedacht sie würde damit alleine zum Kindergarten fahren."
    show oschutz talk with dissolve
    o "Danke Papi, du bist der Beste!"
    show oschutz happy at slightleft with move
    show odad talk at slightright with moveinright
    odad "Ich bin mir immer noch nicht so sicher."
    odad "Willst du wirklich nicht, dass wir dich abholen?"
    odad "Jetzt wo hier keine Stützräder mehr dran sind kannst du dich wirklich verletzen."
    o "Ihr müsst doch zum Arzt, ich schaff es schon alleine Heim, ihr habt mir ja den Weg gezeigt."
    show odad at right
    show oschutz at center
    with move
    show omum talk at left with moveinleft
    omum "Ja schon, aber sag mir erst wo genau du hinfahren musst."
    show oschutz talk
    o "Von hier bis zu Oma, dann den Berg runter, links zur Kirche, an der Bushaltestelle vorbei, dann kommt der BIDL, die Gartenanlage und dahinter ist doch dann schon unser Haus."
    omum "Gut... Und du bist dir wirklich sicher?"
    o "Bitte, vertraut mir doch ein bisschen."
    o "Ihr seid doch gute Eltern und habt mir alles beigebracht.."
    odad "Hmmmh, na gut Schätzchen. Aber erst zeig ich dir noch einmal wie man das Schloss anschließt."
    o "Danke Papi!"
    o "Ihr könnt jetzt auch wirklich gehen, ich komme zurecht. Bis später! Ich hab euch lieb."
    omum "Wir dich auch Schatz. Bis heute Nachmittag!"
    odad "Und mach das Fahrrad nicht kaputt!"
    o "Ach Papa, ich doch nicht."
    hide omum with moveoutleft
    hide odad with moveoutright
    show oschutz happy at center with move
    play sound cardoor1
    pause 1.0
    play sound cardoor2
    o "Tschüss!"
    o "Und jetzt weg mit dem Zeug."
    hide oschutz
    show octa mine
    with dissolve
    o "Und wiieso musst du mich eigentlich ausspannen?"
    o "Glaub bloß nicht, ich hätte dich nicht gesehen."
    o "Ich hab nämlich auch die besten Augen!"
    p "Auswas?"
    show octa mad
    o "Warum beobachtest du mich?!"
    p "Wegen deinem Fahrrad..."
    show octa smug
    o "Bist du neidisch oder was?"
    p "Ich darf noch kein Fahrrad ohne Stützräder fahren."
    o "Oooh, da kann man aber erst richtig coole Dinge machen. Ich geb dir mal ein Beispiel!"
    hide octa
    show obike n
    with dissolve
    o "Ist ohne die blöde \"Schutzausrüstung\" auch viel leichter."
    show obike wheelie with dissolve
    o "Schau her, so geht das!"
    show obike at right with move
    pause 0.2
    show obike wheelier with dissolve
    pause 0.2
    show obike at center with move
    show obike at left with move
    pause 0.2
    show obike wheelie with dissolve
    pause 0.2
    show obike at center with move
    pause 0.2
    show obike n
    p "Wow!"
    o "Siehste, ganz einfach. Jetzt du!"
    hide obike
    show octa smug at center
    p "Was? Ich darf doch nicht."
    o "Ist doch egal, probiers mal aus, bist doch kein Weichei und wenn du fällst ists ja nicht so schlimm. Hier kannst auch meinen Helm haben."
    
    
    $ bikepoints = 0
    menu:
        o "Bawk, Bawk Bawk! Komm schon, du bist doch kein Angsthase, oder?"
        
        "Auf das Fahrrad steigen.":
            p "Ist ja gut, ich mach ja schon."
            
            
        "Nein.":
            $ bikepoints += 1
            p "Ich... Ich will wirklich nicht!"
            o "Ohh, du bist wohl ein Angsthase."
            show octa mad
            o "Jetzt mach oder ich erzähl allen, dass du mich vom Rad geschubst hast!"
            menu:
                "Doch aufs Rad steigen.":
                    p "Schon gut! Ich fahre ja."
                    
                    
                "Sich weiterhin weigern.":
                    $ bikepoints += 1
                    p "Mama sagt immer lügen tun nur dumme Kinder!"
                    p "Dann macht doch, dann sag ich allen dass du lügst, es hat ja keiner gesehen, dass ich dich geschubst hab!"
                    show octa vmad
                    o "Du Idiot!"
                    p "Selber!"
                    show octa at slightleft with move
                    show heide mad at slightright with moveinright
                    h "WAS ist hier los?"
                    show octa shock
                    o "Also der da..."
                    h "Ihr kommt jetzt beide sofort rein! Aber zack zack! Und hört mit dem GEBRÜLLE auf!"
                    hide heide with moveoutright
                    show octa mad at center with move
                    o "Mit dir rede ich nicht mehr ..."
                    hide octa with moveoutright
                    jump scene15
                 ##### Szene 14 #####   
label scene14:
    scene cg biking with fade
    p "Ooookay und jetzt?"
    o "Und jetzt auf einem Rad! Los! Los!"
    o "Das Hinterrad, komm schon! Komm schon! Komm schon!"
    p "Okay ... also ... SO! Octa guck! Ich kann es! ich kann es!"
    o "[name] pass auf! KATZE!"
    scene cg bikecat with fade
    p "Ohh ... WOAH! Katze vorsicht!"
    scene cg bikefall with fade
    p "Aua ..."
    
    menu:
        p "Das hat weh getan ..."
        
        "Weinen.":
            $ crying = True
            p "Wahhhh! Wahhhh!"
            p "Mein Knie!!"
            p "Waaahhh!"
            o "Ohh Gott ist mit dir alles in Ordnung?"
            p "Ich hab mir mein Knie aufgeschürft!"
            o "Nicht du, die Katze!"
            "Katze" "{i}schnurr{/i}"
            o "Dir geht's gut, dann werd ich mich wohl besser aus dem Staub machen."
            o "Ich will keinen Ärger hörst du?"
            p "WAAAHHHH!"

            
        "Stark bleiben.":
            $ crying = False
            p "Ich brauch ein Pflaster..."
            o "Was ist passiert?"
            p "Hab mir das Knie aufgeschürft. Aber der Katze geht's gut!"
            "Katze" "{i}schnurr{/i}"
            o "Ich hab keine Pflaster. Ich geh rein und hol welche."
            p "Dann hol gleich Karin."
            o "Aber, dann bekommen wir beide doch Ärger!"
            p "Ich blute ganz doll, guck doch mal."
            o "Ja... Ja ist ja gut... Ich... Ich hol einen Erwachsenen."
            
    scene bg court with fade    
    if crying == True:
        show octa shock at center
        show heide mad at right with moveinright
        h "Großer Gott! Was ist denn das hier für ein Tumult!"
        h "Was ist denn hier passiert?"
        h "[name] jetzt hör auf zu weinen. Kannst du laufen?"
        p "Also ich ... {i}schnüff{/i}... ich glaube schon."
        show octa shock at left with move
        h "{b}OCTAVIA SIEGLINDE!{/b}"
        o "J... ja Frau Heidenau!"
        h "Warum liegt [name] hier weinend am Boden?!"
        o "Also ich ..."
        h "Wir reden später. Ihr beiden kommt jetzt mit. [name] wir verarzten dein Bein. Trab trab!"
        p "Aber das tut weh!"
        h "Gleich nicht mehr. Jetzt stell dich nicht so an und komm mit."

    else:
        show octa shock at slightleft with moveinright
        show karin shock at slightright with moveinright
        k "Was ist denn hier passiert?"
        p "Ich hab mir das Knie aufgeschlagen."
        k "Ohh je. Tut es doll weh?"
        p "Es geht so. Mama sagt echte Indianer kennen keinen Schmerz."
        k "Wir lassen trotzdem mal die Frau Heidenau draufschauen."
        p "Frau Heidenau?!"
        k "Ja, sie ist die beste Ersthelferin die wir haben. Schon fast magisch wie sie Wunden versorgt."
        k "Kannst du laufen?"
        p "Ja, ich denke schon."
        k "Ich stütze dich, komm, wir gehen ins Sanitätszimmer."
    
    scene bg health
    show heide talk at slightleft
    show karin n at slightright
    show octa shock at right behind karin
    with fade
    h "So, jetzt zeig mal her dein Knie."
    h "Und Octavia, du kommst auch her. Vielleicht lernst du ja was dazu."
    o "O... okay Frau Heidenau."
    show octa at slightright
    show karin at right behind octa
    with move
    show heide n
    h "Also ich muss das erst reinigen. Das stinkt jetzt etwas und es wird kurz brennen."
    p "Autsch!"
    h "Papperlapapp, so schlimm kann das garnicht sein."
    p "Aber..."
    show heide talk
    h "Shh jetzt!"
    show heide n
    h "Octavia, warum muss ich das machen?"
    show octa smug
    o "Ohh, damit die Wunde sauber ist und richtig heilt, ich bin in Erster Hilfe doch die-..."
    h "Die Beste. Jaja. Wie du meinst. Aber es stimmt. Also halt still [name]."
    show octa happy
    h "Jetzt noch ein Pflaster drauf ... und gut. Besser?"
    p "Ja, besser."
    h "Und jetzt will ich wissen..."
    show heide talk
    show octa shock
    h "Was da draußen passiert ist!"
    o "Also ... ähm ..."
    
    menu:
        "Wie erklärst du die Situation?"
        
        "Die Wahrheit sagen":
            $ octahome = True
            p "Ich bin mit Octavias Fahrrad gefahren."
            show karin shock
            p "Und dann wollte sie, dass ich einen Trick mache und dann bin ich hingefallen."
            show octa mad
            o "STIMMT DOCH GARNICHT!"
            p "Du hast gesagt ich soll fahren oder ich bin ein Angsthase!"
            show octa vmad
            o "Das war doch nur ein Witz. Außerdem bist du nicht wegen den Trick gefallen!"
            o "Sondern weil du fast eine Katze umgefahren hättest, weil du keine Augen im Kopf hast!"
            show heide n
            h "Ich hab genug gehört."
            h "[name], soll ich deine Mama anrufen lassen damit du nach Hause kannst oder soll Karin dich zurück in den Gruppenraum bringen?"
            p "Mama ist unterwegs, ich bleibe hier, das geht schon."
            h "Gut. Karin, bring [name] bitte zurück in den Gruppenraum."
            show karin talk
            k "In Ordnung Frau Heidenau."
            hide karin with moveoutright
            h "Und du Octavia, bleibst bitte nochmal kurz hier."
            show octa shock
            o "Bitte nicht zu Hause anrufen..."
            
        "Lügen.":
            $ octahome = False
            p "Katze!"
            show octa happy
            show heide n
            h "Katze?"
            p "Ich bin wegen einer Katze gestolpert!"
            p "Ich hab Sie nicht gesehen und bin gegen Sie getreten und gestolpert und dann auf die Steinkante gefallen!"
            o "Wieso bist du eigentlich gerannt?"
            show karin mad
            p "Gerannt? Ach, ich bin gerannt ..."
            show heide talk
            h "Du bist also gerannt?"
            show octa smug
            o "Du wolltest dir nur mein Fahrrad ansehen oder?"
            p "Ja! Ja das Fahrrad ansehen."
            show heide n
            h "So ist das also."
            show karin n
            show octa happy
            h "Also ein Unfall. Kann ja mal passieren."
            h "Und es geht dir wieder besser?"
            show heide talk
            o "Ja, uns geht's gut!"
            p "Was? Ohh. Ja. Gut. Uns geht's gut."
            o "Dürfen wir dann jetzt wieder mit Karin in den Gruppenraum?"
            show heide n
            h "[name] ist ja jetzt verarztet. Also ja, ab mit euch."
            h "Bringst du sie Karin?"
            k "In Ordnung Frau Heidenau."
            hide karin
            hide octa
            with moveoutright
            show heide laugh at center with move
            h "Hmm... Gelogen haben sie. Aber wenigstens zusammengehalten. Vielleicht sind ja nicht alle Kinder furchtbar."
            
    if octahome == True:
        scene cg marble with fade
        n "Damit bin ich damals zur Petze geworden. Octavia hatte mir das sehr übel genommen."
        n "Den Blick den sie mir zugeworfen hat als sie von ihren Eltern abgeholt wurde werde ich niemals vergessen."
        n "Bittere Enttäuschung..."
        n "Natürlich hatten die anderen Kinder schnell für Ablenkung gesorgt."
        n "Erst hatten sie alle wissen wollen woher das Pflaster kam und mich dann zum Murmeln spielen aufgefordert."
        n "Da sagt man doch nicht nein."
        
    else:
        scene bg grura
        show octa vhappy
        with dissolve
        o "Danke."
        p "Was? Warum?"
        o "Dass du keine Petze warst, darum."
        p "Jetzt muss ich das nurnoch Mama erklären."
        show octa smug
        o "Ich hab da schon eine Idee..."
            ##### TAG 4 ENDE #####
            
            ##### TAG 5 BEGINN #####
            ##### Szene 15 #####
    n "Hier endet unser Reviewprototyp.."
    n "Es kommen noch ein paar Szenen in skeletaler Form."
    n "Quasi eine reine Techdemo dessen was noch geplant ist."
    n "Allerdings zeigen wir auch einiges an Art die wir bisher nicht gezeigt haben."
    n "Leider hat für die Umsetzung die Zeit gefehlt, da es kurzfristig noch einige Änderungen gab, die eine Gruppenbesprechung erforderlich machen."
    
    menu:
        "Credits anschauen":
            jump credits
            
        "Skeletale Szenen noch ansehen":
            jump scene15
            
    
label scene15:
    stop music fadeout 1.0
    scene bg grura
    show randy happy at center
    with dissolve
    play music maintheme fadein 1.0
    "P wird zu Randy's Gebu eingeladen."
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
label scene16:
    "Mutter holt P ab. P erzählt von der Einladung."
    "Es wird ein Kostüm eingekauft."
    menu:
        "Was für ein Kostüm?"
        
        "Anjakostüm":
            $ costume = "anja"
            "Sie kaufen ein Anjakostüm."
            jump scene17
            
        "Evekostüm":
            $ costume = "eve"
            "Sie kaufen ein Evekostüm."
            jump scene17
            
        "Octakostüm":
            $ costume = "octa"
            "Sie kaufen ein Octakostüm."
            jump scene17
            
##### Szene 17 #####
label scene17:
    scene bg party
    show lparty smug at center
    with dissolve
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
label scene18:
    scene bg party
    show aparty jabber at left
    show eparty vhappy2 at right
    show oparty vhappy at center
    show rparty talk at leftish behind oparty
    show lparty smug at rightish behind oparty
    with fade
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
label scene22:
    "Ende der Party, cooler Ausklang, cooles Gruppenfoto. Nicenstein."    
    "Prototyp Ende"
    
                
label credits:
    scene bg bedroom with dissolve
    nvln "Coding - VN\nKilian Petry"
    nvln "Coding - Minigame\nFrederik Haas"
    nvln "Art - Lead\nNatalie Kuhrt"
    nvln "Art - Support\nFlorian Menzel"
    nvln "Writing\nFrederik Haas, Florian Menzel, Sascha Fuchs\nFabian Pfannmüller, Kilian Petry"
    nvln "Sounddesign\nLuca Pfeiffermann"
    nvl clear
    nvln "Vielen Dank für's Spielen!"
    stop music fadeout 2.0
    nvln "Euer Team von Baby's First Visual Novel"
    "diojasppjdaps"
    "diuashdsaoi"
    "daosijdaos"
    
    
    #"Testtest."
        

    
    
    # This ends the game.

    return
