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
    $ randyname = True
    $ octa_points = 0
    $ eve_points = 0
    $ anja_points = 0
    
    ##### AFFINITY SYSTEM END #####

    
    ##### Szene 1 - Prolog #####
    show bg grura
    
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
    menu narrationoptions:
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
            jump optionsend
            
    ##### WOCHE 1 BEGINN #####
    ##### TAG 1 BEGINN #####
    ##### Szene 2 CHILD #####
label childlike:
    hide bg
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
            "{i}Ich strahle Mama regelrecht an als ich ihr antworte.{/i}"
            m "Das ist schön. Du kommst bestimmt in eine Gruppe mit ganz tollen anderen Kindern."
     
        "Ja...":
            "{i}Ich will Mama nicht traurig machen und versuche sie anzulächeln.{/i}"
            m "Ach Spätzchen... Bist du doch noch so traurig, dass du deine alten Freunde nicht mehr siehst?"
            "{i}Ich schaue traurig auf mein Frühstück runter.{/i}"
            m "Du kommst heute bestimmt ein eine Gruppe mit ganz tollen Kindern, wirst schon sehen!"
            "{i}Als Mama mir durch die Haare wuschelt wird meine Laune wieder besser. Mama ist die Beste!{/i}"
    
        
    "{b}Ende: Kindlicher Erzähler{/b}"
    hide mum
    show bg grura
    jump narrationoptions
    
    ##### Szene 2 - ADULT #####
label retro:
    hide bg
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
            n "Ich wollte endlich wieder mit anderen Kindern spielen. Durch den Umzug und die lange Wartezeit hatte ich viel Zeit allein mit Mama, ohne andere Kinder verbracht."
            m "Das ist schön. Du kommst bestimmt in eine Gruppe mit ganz tollen anderen Kindern."
            
        "Ja...":
            n "Natürlich nicht. Ich wollte zurück zu meinen Freunden. Zu meinen alten Freunden. Heute erinner ich mich kaum noch an sie aber damals war ich sehr traurig."
            n "Ich wollte nur auch Mama nicht traurig machen. Doch Mamas merken alles."
            m "Ach Spätzchen... Bist du doch noch so traurig, dass du deine alten Freunde nicht mehr siehst?"
            m "Hey, schau mich an, nicht dein Essen. Alles wird gut, okay? Komm her, lass dich mal knuddeln."
            m "Siehst du? Alles garnicht mehr so wild."
            m "Du kommst heute bestimmt ein eine Gruppe mit ganz tollen Kindern, wirst schon sehen!"
            n "Mama wusste immer wie man andere aufmuntert."
    
    "{b}Ende: Erwachsener Erzähler{/b}"
    hide mum
    show bg grura
    jump narrationoptions
    
    ##### Szene 2 - NEUTRAL #####
label neutral:
    hide bg
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
    hide mum
    show bg grura
    jump narrationoptions
    ##### Szene 3 #####
label optionsend:
    show bg street
    if seenscene == False:
        menu:
            "Freut sich das Kind auf den Kindergarten?"
            "Ja.":
                $ happytogo = True
                
            "Nein.":
                $ happytogo = False
        
    show mum talk at center
    if happytogo == True:
        n "Ich weiß noch wie aufgeregt ich damals war. Ich hatte mich gefragt wie die anderen Kinder wohl auf mich reagieren würden."
        n "Ich hatte gehofft schnell neue Freunde zu finden und war obwohl ich mich auf den Tag gefreut hatte, froh meine Mama an meiner Seite zu haben."
        m "Das wird ein ganz toller Tag, glaub mir!"
    else:
        n "Ich weiß noch wie viel Angst ich damals hatte. Alles war so neu und ich war unsicher ob ich schnell neue Freunde finden würde."
        n "Ich war nur so froh, dass meine Mama bei mir war."
        m "Gleich sind wir da. Keine Angst, das wird schon! Du wirst bestimmt viele neue Freunde finden."
    n "Mein neuer Kindergarten war ein Gemäuer mit alten Fenstern und Backsteinwänden, welches einen sehr einschüchternden Eindruck auf mich hatte."
    show bg grura with dissolve
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
            h "Ihr Kind ist bei uns bestens aufgehoben. So \"[name]\", deine Gruppe ist die Käfergruppe, die Katrin kümmert sich um dich."
            h "Mitkommen!"
            n "Frau Heidenau hatte mich dann in Richtung des Gruppenraumes gezogen, während meine Mutter besorgt hinterherlief."
            n "Sie schien mich noch nicht mit dieser Frau allein lassen zu wollen."
            h "Hier Katrin. Ein Neuer. Ich muss jetzt weitermachen. Ich erwarte nachher deinen Bericht."
        
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
            h "Ihr Kind ist in der Käfergruppe. Die Gruppenleitung heißt Katrin, das ist die Dicke in dem Raum da hinten."
            h "Wenn es schon nicht reden kann bringen Sie es am Besten selbst. Vielleicht hilft das."
            h "Guten Tag!!"
            hide heide
            show mum at center with move
            n "Nachdem meine Mutter diese Abfertigung verwunden hatte, brachte sie mich zum Gruppenraum. Dort angekommen lernte ich dann auch Katrin kennen."

        
    
    hide heide
    hide mum
    show katrin n
    n "Katrin machte nie den Eindruck als ob sie an ihrer Arbeit Spaß hatte. Vielleicht ist ihr das bei ihrer Chefin aber auch nicht zu verübeln gewesen."
    k "Ahh, hallo sie beide. Danke, dass Sie ihr Kind gebracht habe. Sie können unbesorgt sein, wir kümmern uns ganz wunderprächtig um ihn."
    k "Also willkommen dann, in der Käfergruppe!"
    show katrin go
    k "Kinder, kommt mal alle zusammen, wir haben Neuzugang bekommen!"
    hide katrin
    show anja what at left with moveinleft
    show eve happy2 at right with moveinright
    show octa happy at center
    show louis really at slightright behind octa
    show randy happy at slightleft behind octa
    with moveinbottom
    k "Das sind deine neue Freunde! Stell dich uns allen doch mal vor, wir wissen ja noch garnicht wie du heißt."
    
    menu:
        "Vorstellen.":
            $ menu_choice3 = "yes"
            p "Hallo ich bin [name]! Lasst uns Freunde sein!"
            k "Da hört ihr's Kinder. Ich hoffe ihr freundet euch alle mit [name] an.!"
            
            
        "Schweigen.":
            $ menu_choice3 = "no"
            p "..."
            n "Während ich kein Wort rausbrachte und mich alle anstarrten hörte ich hinter mir Katrin und meine Mutter reden."
            m "Ohh, entschuldigen Sie Frau ..."
            k "Einfach Katrin reicht."
            m "Ohh, in Ordnung. Entschuldigen Sie Katrin, [name] ist noch etwas schüchtern und ..."
            k "Alles gut. Also Kinder, das hier ist [name], ich hoffe ihr alle könnt Freunde werden."
        
        "Stammeln.":
            $ menu_choice3 = "meh"
            p "I.. ich.. also ich b-b-bin..."
            k "Du brauchst keine Angst haben."
            k "Komm, sag mir wie du heißt, dann stell ich dich vor."
            p "...[name]..."
            k "Also Kinder, das hier ist [name], ich hoffe ihr alle könnt Freunde werden."
            
            
    
    ##### Szene 4 #####
    hide octa
    hide anja
    hide eve
    hide louis
    hide randy
    show katrin talk at slightright with moveinright
    show mum talk at slightleft with moveinleft
    k "Sie können Ihr Kind dann jetzt auch bei uns lassen. Wir kümmern uns bis sie zum Abholen vorbeikommen."
    m "Rufen Sie mich einfach sofort an falls irgendwas sein sollte."
    k "Natürlich, natürlich. Überhaupt keine Frage."
    m "Na dann [name]. Viel Spaß an deinem großen Tag. Und jetzt lass dich noch mal knuddeln!"
    p "Tschüss Mama, ich hab dich lieb!"
    hide mum with moveoutleft
    show katrin at center with move
    k "Dann fangen wir doch jetzt auch gleich mal an."
    k "Wir machen jetzt Morgenkreis. Stell dich einfach da hin und warte ab. Brav sein!"
    n "Der Morgenkreis war ein Ritual zu dem Katrin uns jeden Tag zusammenrief. Wir spielten, sangen, musizierten oder lernten zusammen."
    k "Sind alle da?"
    hide katrin
    show anja what at left with moveinleft
    show eve happy2 at right with moveinright
    show octa happy at center
    show louis really at slightright behind octa
    show randy happy at slightleft behind octa
    with moveinbottom
    k "Gut, dann legen wir mal los... Wir spielen wieder das Käfergruppenlied! Holt doch alle schonmal eure Instrumente aus der Kiste."
    n "Natürlich wussten alle was gemeint war. Außer mir. Ich kam mir damals ziemlich hilflos vor, da drückte mir plötzlich ein Mädchen ein paar Klanghölzer in die Hand."
    hide anja
    hide eve
    hide louis
    hide randy
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
    show katrin music at right with moveinright
    k "Also Kinder, alle bereit? Dann 1 und 2 und 3 und ..."
    "Minigame geht los. Takt halten."
    "Minigame steht noch nicht, von daher Choice:"
    menu:
        "Hast du das Minispiel gewonnen oder verloren?"
        
        "Gewonnen.":
            hide katrin
            show octa mine at center with move
            o "Das hat Spaß gemacht! Aber ich war die Einzige die alles richtig gemacht hat."
            if boomstick == True:
                show octa smug
                o "Ich dachte du kannst das? Irgendwie war ich trotzdem viel besser als du."
            else:
                show octa smug
                o "Du hast doch gesagt du kannst das nicht? Egal. Ich war ja auch viel besser als du."
            
        "Verloren...":
            hide katrin
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
    hide octa
    show katrin go at center
    k "Das habt ihr gut gemacht Kinder!"
    k "Aber jetzt ist genug, auf zum Frühstück mit euch. Husch husch, wir haben ja nicht den ganzen Tag Zeit."
    
    ##### Szene 5 #####
    
    hide katrin
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
    e "Das hier."
    show eve paper
    menu:
        n "Wie findest du das Bild?"
        
        "Das sieht toll aus!":
            show eve shy2
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
            show eve mad
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
            show eve mad
            e "Angeber."
            e "Geh weg."
            show eve draw

    
    hide eve
    n "Evelynn sollte mich zukünftig noch häufiger dazu motivieren selbst kreativ zu sein."
    n "Aber an dem Tag ließ ich sie erstmal in Frieden, sie war ohnehin fast sofort wieder in ihrer eigenen Welt versunken."
    n "Und damit war mein erster Tag auch vorbei. Ich hatte so viele neue Kinder kennengelernt und einige von ihnen sollten einen großen Einfluss auf mich haben."
    show mum talk at center with moveinleft
    m "Hallo Püpschen!"
    m "Komm lass dich drücken! Hattest du heute viel Spaß?"
    p "Jaaa! Ich hab gemalt und gesungen und gespielt und Klangholz gespielt und ..."
    m "Haha, so viel also! Komm, erzähl mir den Rest auf dem Weg nach Hause."
    p "Okay Mami."
    hide mum
    show bg street with dissolve
    ##### TAG 1 ENDE #####

    ##### TAG 2 BEGINN #####
    ##### Szene 7 #####
    show bg grura with dissolve
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
    hide eve
    ##### TAG 2 ENDE #####
    
    ##### TAG 3 BEGINN #####
    ##### Szene 9 #####
label choice6_done:
    show bg bedroom
    "???" "{b}KICKERIKI! KICKERIKI! KICKERIKI!{/b}"
    p "Waaah!"
    p "Hilfe! Was ist das?! Mama!!!"
    "???" "{b}KICKERIKI! KICKERIKI! KI...{/b}"
    show mum talk
    m "Guten Morgen Püpschen!"
    m "Ich hab dir was mitgebracht!"
    n "An dieser Stelle sehen Sie einen Wecker der aussieht wie ein Hahn."
    p "Eine Ente!"
    m "Fast! Aber mit diesen Wecker kommst du sicherlich aus den Federn."
    hide mum
    show bg street
    n "Auf dem Weg zum Kindergarten erklärte sie mir dann, dass mein Wecker ein Hahn sei, keine Ente und was die Unterschiede sind."
    n "Ich sollte nun täglich von diesem Hahn geweckt werden, zusammen mit meiner Mutter die sich darüber köstlich amüsieren konnte."
    n "Den Wecker hab ich nie weggeschmissen."
    show bg grura
    show katrin talk
    k "Also Kinder, ich hab euch heute etwas mitgebracht."
    show katrin happy
    k "Das ist ein Radio, mit Mikrofon! Damit können wir singen und uns anhören was wir gesungen haben."
    show katrin shock at slightright with move
    show octa mad at slightleft with moveinleft
    o "Öhhhh!"
    show randy mad at left with moveinleft
    r "Wir haben doch gestern schon gesungen!"
    o "Genau, wir haben keine Lust!"
    n "Und plötzlich verschwor sich der gesamte Raum gegen die arme Katrin. Das passierte recht oft. Und wir haben immer gewonnen."
    show katrin mad
    k "Aber jetzt hab ich doch extra den Recorder für euch mitgebra..."
    r "Aber singen ist blöd."
    show katrin n
    k "In Ordnung ... Und was wollt ihr dann machen?"
    show octa smug
    o "Du bist!"
    show octa vhappy
    o "Los! Rennt!"
    hide randy with moveoutleft
    hide octa with moveoutleft
    show katrin shock at center with move
    k "Aber ... Hey! Halt! Kinder, kommt gefälligst zurück!"
    show katrin mad
    k "Benehmt euch! Ich ... ach was solls."
    show katrin go
    k "Vorsicht, jetzt komm ich!" 
    hide katrin with moveoutleft
    
    ##### Szene 10 #####
    show bg kitchen
    n "Nachdem Katrin uns dann endlich wieder alle eingangen hatte war es Zeit zum Essen."
    n "Ich hatte mich an den nächstbesten Tisch gesetzt und wollte die Apfelstücke essen die meine Mama mir gemacht hatte, als plötzlich ..."
    show louis smug
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
    show louis talk
    L "Ich mag eigentlich einfach keine Erdnüsse aber ich hab hier 3 Snackers."
    L "Du kannst die haben wenn du mir bis Freitags zwei Knappers mitbringst."
    p "Aber das ist doch unfair. Oder?"
    L "Knappers sind wirklich etwas größer. OK. Weil du neu bist, musst du mir nur 1 mitbringen. Ich mag keine Snackers, also hab ich gerade nichts."
    show louis n
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
            hide louis with moveoutbottom
            p "... Was für ein komischer Kerl."
            p "Jetzt zurück zu meinem Apfel... Hey! Da fehlt ja die Hälfte. Louis hat doch nicht ...?"
    

    ##### Szene 11 #####
    show katrin happy at center
    $ gone = False
    k "Kinder, schaut mal an wie schön es draußen ist! Wenn ihr fertig gegessen habt, dann zieht euch an und geht auf den Hof zum spielen."
    show bg court with fade
    hide katrin
    n "Ich weiß noch, dass ich eigentlich vorhatte mich einfach nur ins Gras zu legen, weil ich keine Lust zum spielen hatte."
    n "Aber meine neuen Freunde hatten scheinbar andere Pläne mit mir, denn in der Ferne hörte ich lautes Gezanke und ich war schon als Kind sehr neugierig.."
    n "Ich sah Anja auf einem Baum sitzen, die sich mit einem anderen Kind am Boden lautstark stritt."
    show anja vmadb at right with moveinright
    a "Is doch a völligs Gschmarre wos du dou verzüllst."
    show randy vmad at left with moveinleft
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
            show anja happb
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
                    jump snackend
                    
                "Na gut.":
                    p "Okay aber wenn mir was passiert bist du schuld!"
                    a "Jeder kann klettern, ist nur eine Frage der Technik!"
                    p "Ich hoffe ... "
                    a "Warte ich komm erstmal runter ..."
                    play sound "autotür2.ogg"
                    show anja hihi
                    a "So. Schau erst a mal mir zou."
                    show anja talk
                    a "Nimmst erst as rechte Ba und hebsts an, dann suchst dir mit den Händen nen halt und dann…"
                    show anja happyb
                    a "Bist du auch schon oben. Jetzt du!"
                    p "Wow! Das ging ja schnell. Das sieht so einfach aus."
                    p "Okay also die Hände ..."
                    p "... und die Beine ..."
                    p "... ughh ... dann ... waaahhh!"
                    play sound "autotür2.ogg"
                    p "Aua ..."
                    a "A: Sah doch gut aus, jetzt noch ein bisschen mehr Kraft in den Beinen und du bist oben oder wir machen Räuberleiter."
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
            jump snackend
            
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
                p "Ich hab ein paar Snackers wenn du Schokolade willst, kann ich dir eins abgeben."
                show anja happyb
                a "Bist wohl einer mit Geschmack!"
                p "Ich ... weiß nicht wie ich schmecke ..."
                a "Hahaha!"
                a "Aaahh, Super. Jetzt gehts mir besser."
                
            "Nein":
                jump treetalk
                
label treetalk:
    p "Also das war jetzt .. .Randy? Wie ist der so? Ist der nett?"
    show anja madb
    a "Ganz komischer Kauz."
    show anja happyb
    a "Er ist ein echt netter Kerl und ich bin auf seinen Geburtstag am Freitag eingeladen."
    a "Er ist einer meiner besten Freunde, aber er ist eben so unglaublich Normal, dass treibt mich manchmal echt an die Decke."
    p "Und ihr ... "
    a "Außerdem sind wir sooft anderer Meinung und du hasts ja gesehen."
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
label snackend:
    hide anja with moveoutleft
    show mum at center with move
    show bg bedroom with fade
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
