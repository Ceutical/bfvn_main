##### SCRIPT START #####

##### CHARACTER DEFINITIONS #####

define m = Character("Mama")
define v = Character("Papa")

define p = Character("[name]") #Name of Player Character -- P = Protagonist
define pt = Character("[name]", window_ypos=0.27) #ProtaTOP

define n = Character(name=None, what_italic=True) #Narrator
define nt = Character(name=None, window_ypos=0.27, what_italic=True) #NarratorTOP

define a = Character("Anja")

define e = Character("Evelynn")
define et = Character("Evelynn", window_ypos=0.27) #EvelynnTOP

define o = Character("Octavia")
define O = Character("Octa")
define h = Character("Frau Heidenau")
define k = Character("Karin")

define L = Character("Louis")
define Lt = Character("Louis", window_ypos=0.27) #LouisTOP

define r = Character("Randy")
define rt = Character("Randy", window_ypos=0.27) #RandyTOP
define emum = Character("Evelynns Mutter")
define edad = Character("Evelynns Vater")
define omum = Character("Octavias Mutter")
define odad = Character("Octavias Vater")
define rmum = Character("Randys Mutter")
define rdad = Character("Randys Vater")
define nvln = Character(name=None, kind=nvl)

#define test = Character("Test", window_ypos=0.27) #TESTCHAR



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
define audio.decke = "music/sfx/Decke.ogg"
define audio.grassbump = "music/sfx/Aufprall_Rasen.ogg"
define audio.ball = "music/sfx/Ball.ogg"
define audio.ball2 = "music/sfx/Ball1.ogg"
define audio.bal3l = "music/sfx/Ball2.ogg"
define audio.ball4 = "music/sfx/Ball3.ogg"
define audio.ball5 = "music/sfx/Ball4.ogg"
define audio.ballhit1 = "music/sfx/Ball_Getroffen1.ogg"
define audio.ballhit2 = "music/sfx/Ball_Getroffen2.ogg"
define audio.ballhit3 = "music/sfx/Ball_Getroffen3.ogg"
define audio.bell = "music/sfx/bell.ogg"
define audio.child1 = "music/sfx/Kindergeräusche1.ogg"
define audio.child2 = "music/sfx/Kindergeräusche2.ogg"
define audio.kg = "music/sfx/Kinderklasse.ogg"
define audio.pbutton1 = "music/sfx/KnöpfeDrücken1.ogg"
define audio.pbutton2 = "music/sfx/KnöpfeDrücken2.ogg"
define audio.pbutton3 = "music/sfx/KnöpfeDrücken3.ogg"
define audio.draw = "music/sfx/Malgeräusche.ogg"
define audio.foodplay = "music/sfx/Mit Essen Spielen.ogg"
define audio.snackers = "music/sfx/snackers.ogg"
define audio.street = "music/sfx/street.ogg"

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
transform mic:
    xalign .93
    yalign .4
transform topright:
    xalign 1.0
    yalign 0.0
transform topishleft:
    xalign 0.0
    yalign 0.5
transform rotation:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 10
    
######Rennen#####
transform arun1:
    xalign 0.0
    yalign 0.31
transform prun1:
    xalign 0.0
    yalign 0.42
transform lrun1:
    xalign 0.0
    yalign 0.53
transform rrun1:
    xalign 0.0
    yalign 0.64
transform orun1:
    xalign 0.0
    yalign 0.75
    
transform arun2:
    xalign 0.25
    yalign 0.31
transform prun2:
    xalign 0.2
    yalign 0.42
transform lrun2:
    xalign 0.24
    yalign 0.53
transform rrun2:
    xalign 0.27
    yalign 0.64
transform orun2:
    xalign 0.27
    yalign 0.75
    
transform arun3:
    xalign 0.38
    yalign 0.15
transform prun3:
    xalign 0.34
    yalign 0.42
transform lrun3:
    xalign 0.38
    yalign 0.53
transform rrun3:
    xalign 0.41
    yalign 0.64
transform orun3:
    xalign 0.41
    yalign 0.75
    
transform arun4:
    xalign 0.5
    yalign 0.075
transform prun4:
    xalign 0.46
    yalign 0.42
transform lrun4:
    xalign 0.48
    yalign 0.53
transform rrun4:
    xalign 0.5
    yalign 0.64
transform orun4:
    xalign 0.5
    yalign 0.75

transform prun5:
    xalign 0.68
    yalign 0.42
transform lrun5:
    xalign 0.64
    yalign 0.53
transform rrun5:
    xalign 0.66
    yalign 0.64
transform orun5:
    xalign 0.7
    yalign 0.64

transform prun6:
    xalign 0.8
    yalign 0.42
transform lrun6:
    xalign 0.75
    yalign 0.53
transform rrun6:
    xalign 0.73
    yalign 0.64
transform orun6:
    xalign 0.82
    yalign 0.64

transform prun7a:
    xalign 1.0
    yalign 0.42
transform lrun7a:
    xalign 0.92
    yalign 0.53
transform rrun7a:
    xalign 0.88
    yalign 0.64
transform orun7a:
    xalign 0.98
    yalign 0.64

transform prun7b:
    xalign 0.98
    yalign 0.42
transform lrun7b:
    xalign 0.92
    yalign 0.53
transform rrun7b:
    xalign 0.88
    yalign 0.64
transform orun7b:
    xalign 1.0
    yalign 0.64
######################################

##########SANDKASTEN DEFINITIONS###################

transform badsafe:
    xalign -3.0
    yalign 16.0 
    
transform pyhero:
    xalign 35.0
    yalign 5.0
    
transform duckhero:
    xalign 25.0
    yalign 10.0
    
transform riverhero1:
    xalign 18.0
    yalign 2.0
    
transform riverhero2:
    xalign 35.0
    yalign 4.0
    
transform horsehero:
    xalign 16.0
    yalign 23.0
    
transform horserun:
    xalign 0.0
    yalign 4.0

transform dschhero:
    xalign 35.0
    yalign 16.0
    
transform monchero:
    xalign 31.0
    yalign 15.0
    
transform cakehero:
    xalign 31.0
    yalign 26.0
    
transform minehero:
    xalign 23.0
    yalign 23.0
    
transform girlhero:
    xalign 35.0
    yalign 0.0
    
transform kissknight:
    xalign 40.0
    yalign 11.0

transform slap:
    xalign 9.0
    yalign 0.0
    
transform badduck:
    xalign 12.5
    yalign 23.0
    
transform duckfall:
    xalign 11.5
    yalign 14.0
    

######################################


label start:
    play music introtheme
    
    ##### OTHER DEFINITIONS #####
    

    ##### AFFINITY SYSTEM INITIATE #####
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
            pro6 = "Junge"
            suf = "en"
            suf2 = "er"
            suf3 = " "
            suf4 = " "
            ddd = "der"
            pre = "mein"
    else:
        python:
            pro = "ihr"
            pro2 = "sie"
            pro3 = "ihr"
            pro4 = "Tochter"
            pro5 = "sie"
            pro6 = "Mädchen"
            suf = "e"
            suf2 = "e"
            suf3 = "in"
            suf4 = "e"
            ddd = "die"
            pre = "meine"

    ##### Szene 2 CHILD #####
label childlike:
    scene mnd with fade
    pause 1.5
    scene bg black with fade
    "???" "Hey Püpschen! Aufwachen! Du willst doch nicht zu spät kommen!"
    n "Oh man. Ich mag Montage nicht. Ich bin noch so müde."
    n "Aber Moment! Heute geht's in den neuen Kindergarten."
    n "Da treff ich bestimmt..."
    m "Raus aus den Federn jetzt. Es gibt Frühstück!"
    play sound decke
    show bg bedroom2 with fade
    n "Nein… nicht die warme Decke…"
    n "Man, muss alles so hell sein…"
    show bg bedroom with dissolve
    show mum talk with moveinright
    m "Guten Morgen mein kleiner Spatz!"
    p "Morgen Mama ..."
    p "Ich will aber noch nicht aufstehen!"
    m "Ach jetzt stell dich nicht so an. Na komm. Wir ziehen dich gleich an, jetzt gibt's erstmal Essen."
    m "Ich hab Pfannenkuchen gemacht! Heute ist doch dein großer Tag!"
    p "Pfannkuchen! Jaa! Mama ich hab dich lieb!"
    scene bg kitchen with dissolve
    show pancakes with dissolve
    n "Am liebsten würde ich jeden Tag Pfannkuchen essen."
    show mum talk
    hide pancakes with dissolve
    
    m "Freust du dich schon deine neuen Freunde kennenzulernen?"
    menu:
        "Jaaaaaa!":
            $ happytogo = True
            n "Das wird bestimmt super."
            m "Das ist schön. Du kommst bestimmt in eine Gruppe mit ganz tollen anderen Kindern."
     
        "Ja...":
            $ happytogo = False
            n "So wirklich Lust habe ich nicht."
            m "Ach Spätzchen... Bist du doch noch so traurig, dass du deine alten Freunde nicht mehr siehst?"
            n "Ja, das ist echt blöd."
            m "Du kommst heute bestimmt ein eine Gruppe mit ganz tollen Kindern, wirst schon sehen!"
            n "Wenn sie mir so durch die Haare wuschelt fühle ich mich schon wieder besser."
    
        

    ##### Szene 3 #####
label scene3:
    scene bg street with dissolve
    show mum talk at center
    play music maintheme
    if happytogo == True:
        n "Ich bin total aufgeregt. Dabei ist das doch nur ein Kindergartentag wie sonst auch.."
        n "Aber irgendwie auch nicht. Vielleicht finde ich da ja neue noch bessere Freunde als in meinem alten Kindergarten. "
        m "Das wird ein ganz toller Tag, glaub mir!"
    else:
        n "Verdammt ich möchte das nicht. Muss das sein? Mein alter Kindergarten war doch super. Warum muss ich jetzt hier hin?"
        n "Naja, wenigstens ist Mama da."
        m "Gleich sind wir da. Keine Angst, das wird schon! Du wirst bestimmt viele neue Freunde finden."
        n "Mein alter Kindergarten ist definitiv schöner als das hässliche Haus da."
    scene bg flur with dissolve
    play sound child1
    show mum n at slightleft with moveinleft
    show heide n at slightright with moveinright
    n "Was für ne gruselige Frau ist da vorne denn?"
    n "Die sieht überhaupt nicht nett aus."
    show ghost with dissolve
    n "Und warum ist die so weiß? Wie ein Geist..."
    hide mum
    hide ghost with dissolve
    show heide talk at center with move
    h "Ah. Der Neuzugang. Ich bin Frau Heidenau. Wie ist dein Name [pro6]?"
    menu:
        "Selbst vorstellen.":
            p "Ich bin [ddd] [name] und schon 6 Jahre alt!"
            h "Hmpf. [name] also. Wieso sollte man sein Kind bitte [name] nennen?"
            show mum mad at left with moveinleft
            m "Na jetzt hören Sie aber mal ..."
            show heide mad
            h "Papperlapapp!"
            hide mum with moveoutleft
            show heide talk
            h "Ihr Kind ist bei uns bestens aufgehoben. So \"[name]\", deine Gruppe ist die Käfergruppe, die Karin kümmert sich um dich."
            h "Mitkommen!"
            n "Warum zieht sie mich am Ärmel. Ich will das nicht."
            n "Ich wäre auch so mit gekommen. Warum ist diese komische alte Frau so grob. Meine Oma ist auch alt, aber die würde sowas nie machen."
            show bg grura with dissolve
            h "Hier Karin. Ein[suf4] Neu[suf2]. Ich muss jetzt weitermachen. Ich erwarte nachher deinen Bericht."
        
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
            h "Wenn es schon nicht reden kann, bringen Sie es am Besten selbst rum. Vielleicht hilft das."
            h "Guten Tag!!"
            hide heide
            show bg grura with dissolve
            show mum at center with move
            n "Puh, endlich ist diese gruselige Frau weg."

        
    
    hide heide with moveoutleft
    show karin n with moveinright
    hide mum with moveoutleft
    n "Wer ist die Frau? Ist das diese Karin von der die Alte erzählt hat?"
    k "Ahh, hallo sie Beide. Danke, dass Sie ihr Kind gebracht habe. Sie können unbesorgt sein, wir kümmern uns ganz wunderprächtig um [pro5]."
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
    k "Das sind deine neuen Freunde! Stell dich uns Allen doch mal vor, wir wissen ja noch gar nicht wie du heißt."
    
    menu:
        "Vorstellen.":
            $ menu_choice3 = "yes"
            p "Hallo, ich bin [name]! Lasst uns Freunde sein!"
            k "Da hört ihr's Kinder. Ich hoffe ihr freundet euch alle mit [name] an!"
            
            
        "Schweigen.":
            $ menu_choice3 = "no"
            p "..."
            n "Ich will mich nicht vorstellen. Am Ende versprech’ ich mich noch und die Anderen machen sich über mich lustig."
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
    show karin mtalk at center with move
    k "Dann fangen wir doch jetzt auch gleich mal an."
    k "Wir machen jetzt Morgenkreis. Stell dich einfach da hin und warte ab. Brav sein!"
    n "Ah… Morgenkreis. Wie im alten Kindergarten. Ob wir hier auch nur singen?"
    k "Sind alle da?"
    hide karin
    show anja what at left with moveinleft
    show eve happy2 at right with moveinright
    show octa happy at center
    show louis really at slightright behind octa
    show randy happy at slightleft behind octa
    with moveinbottom
    k "Gut, dann legen wir mal los... Wir spielen wieder das Käfergruppenlied! Holt doch alle schonmal eure Instrumente aus der Kiste."
    n "Hä? Was sollen wir machen? Warum gibt mir das Mädchen ein Stück Holz?"
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
    
    n "Sie nimmt das aber Ernst. Ist doch nur der Morgenkreis. Kann man da überhaupt die Beste drin sein?"
    show octa music at left with move
    show karin mhappy at right with moveinright
    k "Also Kinder, alle bereit? Dann 1 und 2 und 3 und ..."
    "Minigame geht los. Takt halten."
    "Minigame steht noch nicht, von daher Choice:"
    menu:
        "Hast du das Minispiel gewonnen oder verloren?"
        
        "Gewonnen.":
            hide karin
            show octa talk at center with move
            o "Das hat Spaß gemacht! Aber ich war die Einzige die alles richtig gemacht hat."
            if boomstick == True:
                show octa smug
                o "Ich dachte du kannst das? Irgendwie war ich trotzdem viel besser als du."
            else:
                show octa smug
                o "Du hast doch gesagt, du kannst das nicht? Egal. Ich war ja auch viel besser als du."
            
        "Verloren...":
            hide karin
            show octa talk at center with move
            o "Das hat Spaß gemacht! Aber ich war die Einzige die alles richtig gemacht hat."
            if boomstick == True:
                show octa smug
                o "Du hast alles falsch gemacht! Du hast doch gesagt, du kannst das. Ich war viel, viel besser als du."
            else:
                show octa smug
                o "Du warst nicht gut ... Ich hab zugeschaut, weißt du?"
            
    n "Der Morgenkreis hier ist auf jeden Fall lustiger als der in meinem alten Kindergarten."
    n "Irgendwie geben sich alle zumindest Mühe."
    n "Aber dieses Mädchen steigert sich da echt rein. Sie heißt Octavia, oder? Was ein komischer Name."
    hide octa with dissolve
    show karin mhappy at center with dissolve
    
    k "Das habt ihr gut gemacht Kinder!"
    k "Aber jetzt ist genug, auf zum Frühstück mit euch. Husch husch, wir haben ja nicht den ganzen Tag Zeit."
    
    ##### Szene 5 #####
label scene5:
    stop sound fadeout 1.0
    stop music fadeout 1.0
    pause 0.75
    play music anjatheme fadein 1.0
    scene bg food
    play sound child2
    show anja eat at center
    with fade
    n "Hmm… Wo soll ich mich bloß hinsetzen. Ich kenn doch noch niemanden."
    n "Ah… da ist noch ein Stuhl frei!"
    n "Vielleicht sollte ich mal hallo sa… "
    a "Hey, wie findest du die Frau Heidenau?"
    p "Also, ich-..."
    a "Ich find die blöd… Die anderen Erzieherinnen sind eigentlich echt nett."
    p "Ja, die ist gru-..."
    a "Aber wenn die Frau Heidenau auf uns aufpasst macht es keinen Spaß. Mama sagt das is ne Greiterhex, keiner mag die."
    p "Was ist eine Grei-..."
    a "Und kennst du schon Evelynn ? Die sitzt immer nur da und malt, find ich voll langweilig."
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
    n "Man sie redet ja ohne Punkt und Komma. Ihre Geschichten sind zwar echt interessant…"
    n "Aber so langsam könnte sie auch mal wieder aufhören."
    a "..."
    n "Ah jetzt hat sie aufgehört."
    p "Du, ich muss mal kurz wo hin..."
    stop sound fadeout 1.0
    
    ##### Szene 6 #####
label scene6:
    scene bg grura with dissolve
    stop music fadeout 1.0
    pause 0.5
    play music evetheme fadein 1.0
    n "Puh… ein Glück dass das Gespräch erstmal vorbei ist."
    n "So viel Labern hält ja keiner aus."
    show eve draw at center with moveinbottom
    play sound draw
    n "Die da sieht ruhiger aus. Was macht sie da am Tisch? Am besten ich stell mich mal vor. Vielleicht will sie ja meine Freundin sein."
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
        e "Wie findest du das Bild?"
        
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
            jump meantoeve

    
    hide eve
    stop music fadeout 1.0
    pause 0.75
    play music maintheme fadein 1.0
    n "Wow… die kann mega toll malen. Ich will das auch können."
    n "Vielleicht kann sie mir ja morgen zeigen wie ich auch so gut werde."
label meantoeve:
    hide eve
    n "Oh… da ist ja Mama? Ist es schon Nachmittag? Aber es war doch gerade noch Morgenkreis und jetzt ist schon wieder Schluss?"
    n "Das ging ja echt schnell."
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
    scene bg black with fade
    show tue with fade
    pause 1.5
    hide tue with fade
    scene bg grura
    play sound child1
    show karin mhappy at center
    with dissolve
    n "Man… heute ist der Morgenkreis echt langweilig."
    n "Singen ist doof. Außerdem singt Karin so laut, da hört man uns eh nicht."
    
    
    ##### Szene 8 #####
label scene8:
    n "Endlich essen!"
    show talking with dissolve
    n "Wenn ich mich wieder zu Anja setze dann labert die mich wieder voll."
    n "Da hab ich echt keinen Bock drauf!"
    hide talking with dissolve
    n "Aber vielleicht kann ich mich ja zu Evelynn setzen."
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
            e "Gar nicht wahr. Das ist schön, guck doch mal."
            p "Jetzt hast du alles an den Fingern kleben."
            p "Malen macht man mit Stiften, nicht mit Essen."
            show eve foodplay
            e "Mir macht das aber Spaß."
            p "Aber das kann man doch nicht mehr essen!"
            show eve foodmad
            e "Darum geht es doch auch gar nicht!"
            
        "WAS tust du?!":
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
            play sound foodplay
            e "Nicht schlecht. Man kann fast erkennen, dass du ein Haus bauen wolltest."
            p "Das soll doch aber eine Burg sein!"
            e "Ohh! Ja stimmt, wenn man es weiß. Du musst aber wirklich noch üben."
            
        "Nein, sicher nicht.":
            scene cg food with dissolve
            p "Nein ... nein ich esse lieber ganz normal. Ich will mich nicht schmutzig machen."
            e "Dann nicht ..."

stop sound fadeout 1.0
    ##### TAG 2 ENDE #####
    
    ##### TAG 3 BEGINN #####
    ##### Szene 9 #####
label scene9:
    stop music fadeout 1.0
    pause 0.75
    play music maintheme fadein 1.0
    scene bg black with fade
    show wed with fade
    pause 1.5
    hide wed with fade
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
    n "Dieser Hahn wie Mama die Ente nennt, ist echt nervig. Wie soll mir das denn beim aufstehen helfen?"
    n "Ich glaube Mama will sich nur über mich lustig machen."
    n "Aber, eigentlich sieht die Ente ja ganz lustig aus. Naja, auf zum Morgenkreis."
    scene bg grura
    show karin talk at slightright
    show dis mikro at mic
    with dissolve
    k "Also Kinder, ich hab euch heute etwas mitgebracht."
    show karin happy
    k "Das ist ein Radio, mit Mikrofon! Damit können wir singen und uns anhören was wir gesungen haben."
    show octa mad at slightleft with moveinleft
    o "Öhhhh!"
    show randy mad at left with moveinleft
    r "Wir haben doch gestern schon gesungen!"
    o "Genau, wir haben keine Lust!"
    p "Schon wieder singen. Mega doof!"
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
    hide dis with dissolve
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
    n "Karin muss echt noch etwas üben, was das Fangen angeht. So lang dauert der Morgenkreis sonst nicht."
    n "Jetzt hab ich Hunger. Fangen macht echt hungrig."
    show louis smug at center with moveinright
    "???" "Hey, was isst du da?"
    n "Wie sieht der denn aus?"
    n "Was ist denn mit seinen Haaren? Die kleben ja."
    n "Und die Jacke… Aus was ist die denn?"
    n "Und warum trägt er ne Sonnenbrille? Wir sind doch drinnen?"
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
            L "Und ich nehm mir noch ein Stück Apfel von dir."
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
            p "Ohh warte Louis ich ... Ohh Mist ... Wir haben doch gar keine Knappers zu Hause."
            n  "Das muss ich Mama erzählen, sonst ist Louis böse auf mich."
            
        "Nein.":
            $ snackersdeal = False
            p "Meine Mama meint, man soll sich nicht mit irgendwelchen Leuten auf etwas langfristiges einlassen!"
            show louis really
            L "Ääähm, was?"
            p "Ich hab gerade keine Knappers und wenn ich die am Freitag mitbringen soll, ist das doch etwas langfristiges."
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
    n "Eigentlich will ich mich nur hinlegen und etwas in der Sonne dösen. Da auf der Wiese siehts gut aus."
    n "Wer schreit denn da?"
    n "Ich guck besser mal nach. Nicht das ich was verpasse."
    n "Sitzt da Anja im Baum? Wer ist den der Junge da?"
    show anja vmadb at topright with dissolve
    a "Is doch a völligs Gschmarre wos du dou verzüllst."
    show randy vmad at left with dissolve
    "???" "Gibt doch viel Besseres, was man damit machen kann. Also wieso Eis!?"
    
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
                    a "HAH! Da hast's, Randy! Jetzt sind wir schon 2."
                    r "Ist doch egal, wenn's Geschmackssache ist. Jetzt macht's aber eh keinen Sinn mehr da noch zu reden."
                    r "Ich geh jetzt, macht doch was ihr wollt ..."
                    hide randy with moveoutleft
                    p "Warum habt ihr euch denn jetzt eigentlich gezankt?"
                    a "Ich wollte nur etwas sticheln, dann wurde ich wirklich wütend."
                    a "Du, komm mal mit hoch."
                    
                "Vanille ist besser!":
                    show randy vhappy
                    "???" "Ha! Siehst du, ist doch nur Geschmackssache! Selbst dein zufälliger Freund stimmt mir zu!"
                    a "Ich mein, ... ja ... also ... [name], fall mir doch nicht einfach in den Rücken!"
                    a "Egal. Dafür kannst du immer noch nicht klettern Randy."
                    show randy mad
                    r "Ach, lass mich doch in Ruhe..."
                    hide randy with moveoutleft
                    show anja happyb at center with move
                    p "Hey, [name]. Kannst du klettern? Komm mal mit hoch!"

            
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
            "???" "Sieht wohl so aus, ich will aber nicht weiter belauscht werden."
            "???" "Ich gehe. Macht doch was ihr wollt."
            hide randy with moveoutleft
            show anja madb
            a "Hast du ja toll gemacht, [name]."
            p "Warte mal, worum ging es eigentlich?"
            show anja happyb
            a "Hehe, du hast also nicht alles gehört? Dann sag ich auch's nicht."
            p "Komm schon!"
            a "Erst wenn du hier hoch kommst!"


    
    
    menu:
        "Kletterst du zu Anja auf den Baum hoch?"
        
        "Ich kann nicht klettern.":
            p "Also, ähm... Ich kann nicht klettern."
            show anja madb
            a "Probier's doch wenigstens."
            p "Ich trau mich nicht ... Ich kann das nicht!"
            show anja happyb
            a "Komm schon, ich zeig's dir auch wie's geht."
            menu:
                "Lieber nicht...":
                    $ gone = True
                    $ anjatreat = False
                    p "Nein! Nein, nein! Ich ... ich guck mal wo dein Freund ist."
                    show anja madb
                    a "NA TOLL! Dann geh doch!"
                    n "Verdammt jetzt ist sie sauer… Ich will doch bloß nicht auf diesen Baum. Da fall ich bestimmt nur runter."
                    jump scene12
                    
                "Na gut.":
                    p "Okay, aber wenn mir was passiert bist du schuld!"
                    a "Jeder kann klettern, ist nur eine Frage der Technik!"
                    p "Ich hoffe ... "
                    a "Warte ich komm erstmal runter ..."
                    play sound cardoor2
                    show anja hihi at right with move
                    a "So. Schau erst a mal mir zou."
                    show anja talk
                    a "Nimmst erst as rechte Ba und hebsts an, dann suchst dir mit den Händen nen halt und dann…"
                    show anja happyb at topright
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
            $ anjatreat = False
            show anja madb
            a "Hey! Was soll das? Wo willst du hin?"
            show anja vmadb
            a "NA TOLL! Dann geh doch!"
            n "Verdammt jetzt ist sie sauer… Ich will doch bloß jetzt grad nicht mit ihr spielen."
            jump scene12
            
        "Ich kann klettern.":
            p "Okay, ich komm zu dir hoch."
            p "Klettern ist einfach. Hände hier, Beine da und schon oben. Hallo du!"
            a "Sauber, kannst's ja so gut wie ich. Respekt."
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
                $ anjatreat = True
                p "Ich hab ein paar Snackers. Wenn du Schokolade willst, kann ich dir eins abgeben."
                show anja happyb
                a "Bist wohl Ein[suf2] mit Geschmack!"
                p "Ich ... weiß nicht wie ich schmecke ..."
                a "Hahaha!"
                play sound snackers
                a "Aaahh, Super. Jetzt gehts mir besser."
                
            "Nein":
                $ anjatreat = False
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
    a "Er hat einen Bruder bei dem er die Filme immer anschauen kann."
    a "Sein Bruder ist super nett."
    p "Was für Fil-..."
    a "Die Gozok Reihe, Omegas und so weiter."
    a "Kannst du ja vielleicht kennenlernen, ich kann ja mal mit Randy reden, ob du auch am Freitag auch auf seinen Geburtstag kommen kannst…"
    show anja happyb
    n "Jetzt redet sie wieder. Irgendwann will ich auch mal so viel am Stück reden können."
    show mum n at left with moveinleft
    n "Oh… Mama ist da! Ist wohl Zeit nach Hause zu gehen."
    
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
        p "Das war die Anja. Die redet immer viel."
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
    scene bg black with fade
    show thr with fade
    pause 1.5
    hide thr with fade
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
    n "Warum fragt sie immer? Sie weiß doch, dass ich schon groß bin. Mit 6 kann man eigentlich alles allein!"
    n "Da drüben. Ist das Octavia? Ja. Die ist aber komisch angezogen."
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
    omum "Ja schon, aber sag mir erst, wo genau du hinfahren musst."
    show oschutz talk
    o "Von hier bis zu Oma, dann den Berg runter, links zur Kirche, an der Bushaltestelle vorbei, dann kommt der BIDL, die Gartenanlage und dahinter ist doch dann schon unser Haus."
    omum "Gut... Und du bist dir wirklich sicher?"
    o "Bitte, vertraut mir doch ein bisschen."
    o "Ihr seid doch gute Eltern und habt mir alles beigebracht."
    odad "Hmmm, na gut Schätzchen. Aber erst zeig ich dir noch einmal, wie man das Schloss richtig zumacht.."
    o "Danke, Papi!"
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
    show octa smug
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
    play sound bell
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
    o "Ist doch egal. Probier's mal aus. Bist doch kein Weichei und wenn du fällst ist's ja nicht so schlimm. Hier, kannst auch meinen Helm haben."
    
    
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
            o "Jetzt mach oder ich erzähl Allen, dass du mich vom Rad geschubst hast!"
            menu:
                "Doch auf's Rad steigen.":
                    p "Schon gut! Ich fahre ja."
                    
                    
                "Sich weiterhin weigern.":
                    $ bikepoints += 1
                    p "Mama sagt, immer lügen tun nur dumme Kinder!"
                    p "Dann macht doch, dann sag ich Allen dass du lügst, es hat ja keiner gesehen, dass ich dich geschubst hab!"
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
    play sound bell
    scene cg bikecat with fade
    p "Ohh ... WOAH! Katze vorsicht!"
    scene cg bikefall with fade
    play sound grassbump
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
        h "Wir reden später. Ihr beiden kommt jetzt mit. [name], wir verarzten dein Bein. Trab trab!"
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
    h "Papperlapapp, so schlimm kann das gar nicht sein."
    p "Aber..."
    show heide talk
    h "Shh jetzt!"
    show heide n
    h "Octavia, warum muss ich das machen?"
    show octa smug
    o "Ohh, damit die Wunde sauber ist und richtig heilt, ich bin in Erster Hilfe doch die-..."
    h "Die Beste. Jaja. Wie du meinst. Aber es stimmt. Also halt still, [name]."
    show octa happy
    h "Jetzt noch ein Pflaster drauf ... und gut. Besser?"
    p "Ja, besser."
    h "Und jetzt will ich wissen..."
    show heide talk
    show octa shock
    h "Was da draußen passiert ist!"
    o "Also ... ähm ..."
    
    menu:
        n "Wie erklär ich das jetzt?"
        
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
            p "Mama ist unterwegs. Ich bleibe hier, das geht schon."
            h "Gut. Karin, bring [name] bitte zurück in den Gruppenraum."
            show karin talk
            k "In Ordnung, Frau Heidenau."
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
            p "Ich hab sie nicht gesehen und bin gegen sie getreten und gestolpert und dann auf die Steinkante gefallen!"
            o "Wieso bist du eigentlich gerannt?"
            show karin mad
            p "Gerannt? Ach, ich bin gerannt ..."
            show heide talk
            h "Du bist also gerannt?"
            show octa smug
            o "Du wolltest dir nur mein Fahrrad ansehen oder?"
            p "Ja! Ja, das Fahrrad ansehen."
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
            k "In Ordnung, Frau Heidenau."
            hide karin
            hide octa
            with moveoutright
            show heide laugh at center with move
            h "Hmm... Gelogen habt ihr. Aber wenigstens zusammengehalten. Vielleicht sind ja nicht alle Kinder furchtbar."
            
    if octahome == True:
        scene cg marble with fade
        n "Na und dann bin ich halt ne Petze. Ist mir doch egal!"
        n "Und bloß weil Octavia mich blöd anschaut muss ich nicht traurig sein."
        n "Ich spiel eh viel lieber mit Murmeln als mit ihrem blöden Fahrrad!"
        
    else:
        scene bg grura
        show octa vhappy
        with dissolve
        o "Danke."
        p "Was? Warum?"
        o "Dass du keine Petze warst, darum."
        p "Jetzt muss ich das nur noch Mama erklären."
        show octa smug
        o "Ich hab da schon eine Idee..."
            ##### TAG 4 ENDE #####
            
            ##### TAG 5 BEGINN #####
            ##### Szene 15 #####

label scene15:
    stop music fadeout 1.0
    scene bg black with fade
    show fri with fade
    pause 1.5
    hide fri with fade
    scene bg grura
    with dissolve
    play music maintheme fadein 1.0
       
    n "Es ist Freitag. Also praktisch Wochenende. Da bin ich immer bei Papa. Vielleicht bekomme ich ja wieder Eis und Schokolade als Abendessen?"
    n "Hoffentlich!"
    n "Außerdem muss ich Papa unbedingt meine Bilder zeigen."
    n "So schön wie die von Evelynn sind sie leider nicht, aber fast!"
    n "Wo ist Evelynn eigentlich?"
    n "Vielleicht weiß Karin ja wo sie ist."
    show karin talk at center
    p "Du... Karin..."
    k "Ja [name]?"
    p "Kann ich dich was fragen?"
    show karin happy
    k "Gerne. Was willst du denn fragen?"
    p "Wo ist denn Evelynn? Ich find die nicht."
    show karin talk
    k "Du musst die Evelynn nicht suchen. Die ist heute zu Hause geblieben."
    k "Ihre Mutter muss angeblich etwas einkaufen und braucht dafür Evelynn. Mehr kann ich dir nicht sagen."
    
    p "Mhhh. Man."
    p "Ist ja voll doof, wollte was mit ihr malen."
    show karin vhappy
    k "Ich kann ja mit dir malen."
    p "Ne, das macht dann keinen Spaß!"
    show karin mad
    k "Also gut..."
    p "Dann halt was anderes."
    hide karin with dissolve

    n "Scheibenkleister!"
    n "Na gut. Dann muss ich eben mit Anja den Tag verbringen."
    n "Die hat sicherlich wieder viel zu erzählen, außerdem muss man die nicht suchen. Anja hört man immer!"
    
    a "Gar nicht wahr!"
    stop music fadeout 1.0
    play music anjatheme fadein 1.0
    n "Ich hör sie sogar jetzt."
    a "Mit den Hula Hoop Reifen bin ich viel besser als du!"
    n "Was is da los? Ich sollte mal nachschauen."
    show bg grura2 with dissolve
    show anja mad at rightish
    show octa mad at leftish
    with moveinbottom
    o "Ich kann ihn bis zu 32 mal drehen bis er runterfällt."
    a "Stimmt doch gar nicht. So schnell kann man nicht mal zählen!"
    show octa smug
    o "Du vielleicht nichtl. Ich kann das schon!"
    a "Lügnerin!"
    show octa vmad
    o "Nenn mich nicht so, wenn ich keine bin!"
    show fight with dissolve
    n "Mama würde jetzt sagen, die Beiden sehen aus wie Zankhähne. Ich selber hab noch nie zankende Hühner gesehen."
    a "Aber du kannst das nicht!"
    o "Kann ich wohl!"
    hide fight with dissolve
    n "Irgendwie blick ich nicht durch, aber Hula Hoop hört sich lustig an"
    p "Darf ich vielleicht den Reifen haben?"
    "{color=#0099ff}Octavia:{/color} Du erst recht nicht! \n{color=#0099ff}Anja:{/color} Gerade nicht!"
    n "Wie es aussieht bin ich hier nicht erwünscht. Ich sollte wohl einfach gehen."
    show bg grura with dissolve
    hide octa with dissolve
    hide anja with dissolve
    stop music fadeout 1.0
    play music maintheme fadein 1.0
    n "Och man, was soll ich dann machen... Murmelbahn vielleicht? Auch langweilig..."
    n "Hmmh..."
    n "Was solls, auf zur Murmelbahn!"
    scene cg marble with fade
    p "Dann kommt das noch hier hin und dann..."
    p "LAAANGWEILIG!"
    
    scene bg grura
    show randy happy at center
    with fade
    r "Da, [name]"
    p "Hmmh?"
    n "Die Stimme kommt von hinten. Ich drehe mich um und sehe Randy."
    n "Er steht mit einer Karte in der Hand vor mir, die er mir entgegenhält."
    r "Du bist zu meiner Monster Party eingeladen!"
    p "Was ist das?"
    show randy vhappy
    r "Wir verkleiden uns als Monster! Das wird voll cool!"
    p "Moment, warum?"
    r "Ich hab dich zu meinem Geburtstag eingeladen und ich möchte, dass wir uns alle verkleiden können."
    show einladung with dissolve
    n "Ich nehme die Einladung an und schaue auf die Karte und versuche vorzulesen. Das kann ich schon ein bisschen."
    p "Ein..laadung zum Kinder... Kindergeb...burtstag!"
    show randy talk
    r "Genau!"
    hide einladung with dissolve
    r "Aber... tut mir leid, dass ich dir das nicht früher gesagt habe."
    p "Wieso?"
    r "Es ist heute, aber wir kannten uns ja nicht und Anja hat gesagt, dass du mitmachen willst."
    show randy happy
    r "Ich hoffe du kannst trotzdem kommen... Wie heißt du eigentlich genau?"
    p "[name]."
    r "Frag einfach deine Mama, die wird bestimmt nichts dagegen haben. Musst du sowieso fragen, sonst sagt meine Mama, du darfst nicht kommen."
    p "Mach ich. Anja hat mir erzählt, dass du Monsterfilme anschauen darfst."
    show randy talk
    r "Stimmt, die sind super. Mein Bruder hat da ganz viele!"
    r "Was hat denn Anja noch so über mich gesagt?"
    p "Schoko ist besser als Vanille."
    show randy mad
    r "Die hört damit auch nie auf, oder?"
    r "Naja, schön dich kennengelernt zu haben."
    p "WARTE!"
    show randy talk
    r "Hmm?"
    p "Mir ist langweilig, willst du was spielen?"
    r "Na gut, danach sind wir dann auch Freunde!"
    scene cg marble with dissolve
    n "Ich hoffe nur, dass meine Mutter mich dann auch zur Feier fährt."

        
label scene16:
    scene bg grura
    n "Nach einiger Zeit spielen tippt mir jemand von hinten auf die Schulter."
    p "Huh?"
    show karin n at rightish
    show mum n at leftish
    k "Hey, [name]. Deine Mutter ist etwas früher gekommen um dich abzuholen."
    m "Hallo Klein[suf2]. Ich muss noch etwas in der Stadt erledigen und wollte, dass du mitkommst."
    p "In Ordnung."
    n "Ich packe also meine Sachen und gehe mit Mama zum Auto."
    scene bg street with dissolve
    n "Auf der Straße fällt mir wieder etwas ein."
    show mum n at rightish
    p "Mama!"
    m "Ja?"
    p "Ich wurde auf einen Geburtstag eingeladen. Darf ich da hingehen? Darf ich? Darf ich?"
    show mum happy at rightish
    m "Schön, dass du schon Freunde gefunden hast. Meinetwegen gerne. Wann genau ist denn der Geburtstag?"
    n "Ich geb ihr meine Einladung."
    p "Da!"
    m "Hmmmh..."
    show mum mad at rightish
    m "15 UHR!"
    m "Wieso bekomme ich das erst jetzt?"
    p "Ich hab die Einladung aber doch grad erst bekommen."
    show mum talk at rightish
    m "Na gut. Ich muss dann aber noch deinem Vater sagen, dass er dich von der Feier abholen soll."
    p "Wir sollen uns außerdem verkleiden!"
    show mum mad at rightish
    m "Mmmmmhhhhh."
    m "Verdaaaaa..."
    show mum happy at rightish
    m "Ähhhm. Klar. Wir sind ja eh in der Stadt. Da können wir ja mal kurz in den Kostümladen schauen."
    p "YAAAY!"
    play sound cardoor1
    play music introtheme
    scene bg shop
    n "Man, hier haben Sie ja wirklich alles! Von typischen Monsterkostümen wie eine Riesenmotte mit bunten Flügeln, bis hin zu... huh"
    n "Ein Tier... Tier... Hasensäbelzahnelchwolf?"
    n "Rehhundkatzenkanninchen?"
    p "Mama! Was ist denn das? Das sieht ja komisch aus."
    show mum talk
    m "Hmmmh..."
    m "Ich glaube ein Wolpertinger!"
    p "Ein Wolterdinger?"
    show mum happy
    m "Wolpertinger. Ein Fabelwesen, welches aus ganz vielen Tieren besteht. Das Wesen kommt aus Bayern."
    p "Cool."
    show mum talk
    m  "Aber schau mal her dieser Orca ist ja nett."
    p "WOAH! EIN KILLERWAL!"
    m "Oder ein Killerwal, wenn dir das besser gefällt."
    m "Wir haben aber leider nicht ewig Zeit. Hast du dich schon für was entschieden?"
    
    menu:
        "Killerwal":
            $ costume = "wal"
            p "KILLERWAL!"
            m "Woah. Also dann, alles klar."
            m "Viel Enthusiasmus hier."
            p "Wieso?"
            m "Weil du dich auf das Kostüm freust. Gefällt dir doch, oder?"
            n "Ich nicke"
            show mum talk
        
        "Motte":
            $ costume = "moth"
            p "Mofpa!"
            m "Die sieht ja scheußlich aus."
            p "Die ist aus‘nem ganz coolen Film! Bitteeeee!"
            m "Wenn du meinst, ich überlass dir heute ja die Entscheidung."
            p "Ja, ich will das Kostüm."
            
        "Wolper...dings":
            $ costume = "wolp"
            p "Wolterdimper. Der ist voll cool!"
            show mum happy 
            m "Gerne kauf ich dir den Wol-Per-Ting-Er, wenn du ihn richtig aussprichst."
            p "Wieso?"
            m "Weil ich‘s süß finde."
            p "Ok... Wol-Per-Ting-Er... Wolperdinger."
            show mum talk
    
    m "Na dann. Ab zur Kasse"
    hide mum talk with dissolve
    show bg black with dissolve
    
    n "Jetzt, wo ich mein tolles Kostüm habe, kann ich auf den Geburtstag gehen!"
    n "Das wird sicher Super!"
    n "Aber erstmal noch mit Mama einkaufen gehen... ob ich wohl trotzdem rechtzeitig komme?"

label scene17:
    
    play sound cardoor1
    stop music fadeout 1.0
    pause 0.75
    play music maintheme fadein 1.0
    scene bg street
    show mum talk at rightish
    m "So, wir sind da."
    n "Ich steige vollkostümiert aus dem Auto aus und bin schon ganz gespannt, was die Anderen an haben werden!"
    n "Mama nimmt mich an die Hand und führt mich zur Tür."
    p "Darf ich klingeln?"
    show mum happy at rightish
    m "Der Knopf da oben ist der Richtige."
    show mum talk at rightish
    n "Kurz darauf geht die Tür auf."
    m "So, geh mal zu deinen Freunden. Ich rede noch kurz mit Randys Mama und bin dann gleich weg. Vergiss nicht, dein Papa holt dich heut Abend ab."
    p "OK. Tschüss Mama."
    hide mum talk with moveoutright
    show bg party with dissolve
    n "Ich komme kaum ins Zimmer, da kommt Louis mir schon entgegen."
    show lparty n 
    L "Hey, [name]."
    p "Hey, Louis."
    
    if snackersdeal == True:
        L "Und, hast du drann gedacht?"
        p "An?"
        L "Ja, ans Knappers!"
        if hasknappers == True:
            menu:
                "Knappers geben":
                    $ trade = True
                    p "Einen Moment... Hier!"
                    show lparty happy
                    L "Gut, dass auf dich Verlass ist."
                    p "Jetzt, sind wir quitt, oder?"
                    L "Ja klar. Wenn du noch einmal was willst, komm wieder zu mir."
                    n "Du bist doch zu mir gekommen..."
                    L "Wollte mich für unser erstes Treffen entschuldigen. War nicht OK."
                    p "Warum?"
                    L "Hab zu dick aufgetragen."
                    p "Wenn... wenn du meinst."

                    p "Sag mal, was bist du für ein Monster?"
                    show lparty smug
                    L "Dr. Acula! Der weltbekannte Arzt."
                    L "Kennst du den wohl nicht?"
                    p "Natürlich!"
                    n "Wenn er weltbekannt ist, dann muss ich ihn ja kennen."

                
                "Kein Knappers geben":
                    $ trade = False
                    p "Ich hab leider keins dabei. Nächste Woche vielleicht?"
                    show lparty mad
                    L "Blödmann!"
                    L "Du hast es mir versprochen, du bekommst nichts mehr von mir!"
                    p "Wieso bist du so wütend?"
                    L "Versprechen werden nicht gebrochen!"
                    n "Irgendwie ist mir das unangenehm..."
                    p "Was bist du denn eigentlich für ein Monster?"
                    L "Sag ich nicht!"
                    n "Wie komm ich aus dieser Situation raus?"

        else:
            menu:
                "Kein Knappers geben":
                    $ trade = False
                    p "Ich hab leider keins dabei. Nächste Woche vielleicht?"
                    show lparty mad
                    L "Blödmann!"
                    L "Du hast es mir versprochen, du bekommst nichts mehr von mir!"
                    p "Wieso bist du so wütend?"
                    L "Versprechen werden nicht gebrochen!"
                    n "Irgendwie ist mir das unangenehm..."
                    p "Was bist du denn eigentlich für ein Monster?"
                    L "Sag ich nicht!"
                    n "Wie komm ich aus dieser Situation raus?"

    else:
        L "Wollte mich für unser erstes Treffen entschuldigen. War nicht OK."
        p "Warum?"
        L "Hab zu dick aufgetragen."
        p "Wenn... wenn du meinst."
        
        p "Sag mal, was bist du für ein Monster?"
        show lparty smug
        L "Dr. Acula! Der weltbekannte Arzt."
        L "Kennst du den wohl nicht?"
        p "Natürlich!"
        n "Wenn er weltbekannt ist, dann muss ich ihn ja kennen."
    
    show lparty really
    "???" "Hallo, Kinder!"
    n "Eine große Frau kommt in den Raum."
    show lparty really at leftish
    show rmum talk at rightish
    "???" "Hallo Louis und du da musst das neue Kind sein, von den mir mein Sohn erzählt hat."
    rmum "Ich bin Erika, also Randys Mama Erika. Schön euch zu sehen."
    rmum "Die Anderen sind grad in Randys Zimmer, kommen aber gleich wieder."
    rmum "Niedliche Kostüme übrigens."
    p "Danke."
    n "Och man. Ich wollte doch gruselig sein, ich bin doch ein Monster!"
    hide lparty really with moveoutleft
    hide rmum talk with moveoutright

label scene18:
    n "Es scheinen schon einige Leute da zu sein. Ich kann sogar schon Anja plappern hören! Und auf dem Fernseher läuft ein Film: Radzilla vs. Mofpa!"
    n "Randy kommt zuerst wieder in das Zimmer gerannt."
    r "Hey [name], konntest ja doch kommen."
    if costume == "moth":
        show rparty happy
        r "MOFPA!"
        n "Randy strahlt mich an und er ist... natürlich Radzilla."
        r "Mein größter Feind... Irgendwie."
        p "Naja, nicht immer."
        r "Toll, dass du gekommen bist."
        
    else:
        show rparty talk
    show geschenk at topishleft with dissolve
    p "Hier Randy, dein Geschenk."
    p "Cooles Kostüm."
    n "Irgendwie ist er wohl von etwas abgelenkt."
    r "Danke, mach ich später auf. Leg es bitte auf den Tisch, OK?"
    hide geschenk with dissolve
    p "Gerne."
    n "Ich lege das Geschenk auf den Tisch und dreh mich um. Ich sehe nichts Besonderes, auf was hat Randy geschaut?"
    hide rparty happy
    if costume == "moth":
        jump scene19
    elif costume == "wolp":
        jump scene20
    else:
        jump scene21
    
label scene19:
    
    n "Na dann, auf zum Tisch und Kuchen essen."
    a "Nimm das Mofpa!"
    n "Jemand sticht mir in meine Seiten."
    stop music fadeout 1.0
    pause 0.75
    play music anjatheme fadein 1.0
    show aparty mad
    p "Hey, lass das!"
    a "Aber du bist doch Böse!"
    p "Tut trotzdem weh."

    if trade == True:
        show aparty n
        a "Hehe, Louis hat gesagt du hast Knappers dabei?"
        p "Hatte ich. Louis gab mir auch drei Snackers dafür und ich hab sie ihm gegeben."
        a "Gut, dass man sich auf dich verlassen kann!"
        
        if anjatreat == True:
            a "Waren das die, die du mir gegeben hast? Ahhhw. Ist ja Süß."
            p "Ja Snackers sind süß."
            show aparty jabber
            a "Oh man. Finde es trotzdem toll, dass du extra Snackers für mich besorgt hast."
            n "Was redet die denn?"
            a "Hmmmh?"
            jump scene19f
        
        else:
            a "Abgeben konntest mir aber nichts?"
            p "Hab nicht daran gedacht."
            a "Na gut Partner..."
            show aparty mad
            a "Hände Hoch, dass ist ein Überfall."
            p "Aber ich hab doch keine mehr dabei!"
            show aparty jabber
            a "War nur ein Jucks."
            a "hmmmh?"
            jump scene19f

    if trade == "false":
        a "Und doof bist du auch!"
        show aparty mad
        p "Was?"
        a "Louis hat‘s mir gesagt. Du versprichst ihm Knappers und bringst sie ihm dann nicht mit!"
        p "Ich konnte noch keine..."
        a "Mach so etwas NIE WIEDER!"
        a "Versprechen bricht man nicht und die Anderen finden das auch dumm."

        if anjatreat == "True":
            p "Aber, du hattest doch auch nichts dagegen, als ich sie mit dir geteilt hab!"
            show aparty shock
            a "Was?"
            show aparty mad
            a "DU VOLLIDIOT HAST EINEM SHERIFF GESTOHLENES ESSEN GEGEBEN?!"
            a "Ich dachte das wäre deins gewesen du Lügner!"
            n "Irgendwie kommt es mir so vor, als würde mich jeder anschauen."
            hide aparty mad
            n "Ich hab es aber auch irgendwie verdient."
            n "Irgendwie fühl ich mich nicht gut, ich versuch aber trotzdem zu feiern."
            "..."
            "..."
            "Einige Zeit vergeht und wie es aussieht nehmen mir die anderen es nicht so übel."
            rmum "Kommt mal alle zusammen ihr kleinen Monsterlein!"
            rmum "Gruppenfoto!"
            "Wenigstens darf ich auch noch auf das Foto."
            rmum "Sagt Käsekuchen"
            scene cg selfiemoth with dissolve
            "Alle" "Käääääseeeekuuuucheeeen!"
        
            scene bg street with dissolve
            jump scene22
        
        else:
            p "Tut mir Leid, ich würde es auch gerne zurückgeben."
            p "Ich traute mich einfach nicht meine Mutter zu Fragen."
            show aparty n
            a "Ist... Verstehe, trotzdem. Nie.."
            p "Nie wieder!"
            a "Nie wieder!"
            jump scene19f

    else:
        show aparty jabber
        a "Hmmmmh?"

label scene19f:
    n "Was ist denn mit Anja los?"
    n "Wieso schaut sie mich so an?"
    a "Ich hab eine Idee!"
    p "?"
    a "Siehst du diese Stadt?"
    p "Die Pappkartons?"
    a "Wenn du schon so angezogen bist, dann mach es wie in den Radzilla Filmen!"
    p "Kämpfen?"
    a "Ja klar. Du bist doch Mofpa. Die Riesenmotte. Und Randy ist Radzilla!"
    p "Ja schon, aber... Ich weiß nicht."
    n "Anja zieht an meinen linken Flügel. Die ist stark."
    a "RANDY!"
    show aparty talk at rightish
    show rparty talk at leftish
    r "Ja."
    a "Radzilla, hier, Mofpa da."
    a "LOS!"
    n "Jetzt wird auch noch Randy herumkommandiert."
    show rparty happy at leftish
    r "Ich verstehe."
    p "Ich nicht!"
    r "Also in Radzilla gegen Prince Ape, kämpft er gegen Prince Ape und in..."
    a "Er kämpft gegen Mofpa."
    r "In einen Film, eigentlich sind sie..."
    a "EGAL! LOS!"
    r "Bereit für einen Monsterkampf in der Stadt?"
    menu:
        "Bereit.":
            n "Es ist sein Geburtstag, muss ja sein..."
            p "Bereit!"
            
        "Bereiterer.":
            n "An seinem Geburtstag doch immer."
            p "Na klar!"
            
        "Am Bereitesten.":
            n "Das müssen sie noch fragen?"
            p "Ich bin bereit! Ich bin bereit! Ich bin bereit!"
    
    a "3"
    a "2"
    a "1"
    a "Los!"
    r "WAAAAH!"
    n "Wir kämpfen eine Weile... ein Tackle hier, etwas ringen, ein Laserstrahl."
    n "Blocken, parrieren."
    n "Es machte wirklich Spaß..."
    n "...Doch nicht für die Stadt, die Pappkartons sind wohl nicht mehr zu gebrauchen."
    n "Natürlich gibt es im Anschluss noch Kuchen!"
    p "Ooof... Fertig"
    hide aparty
    hide rparty
    show rmum talk at center
    with dissolve
    rmum "Keine Müdigkeit vortäuschen."
    rmum "Kommt mal alle zusammen für ein Gruppenfoto."
    "Auch noch so was. Na gut."
    rmum "Los alle. Käsekuchen!"
    scene cg selfiemoth with dissolve
    "Alle" "Käääääseeeekuuuucheeeen!"
    n "... Nett."
    scene bg street with dissolve
    jump scene22
    

label scene20:
    n "Aber da drüben seh ich Evelynn. Ich sollte mal Hallo sagen."
    show eparty talk2
    stop music fadeout 1.0
    pause 0.75
    play music evetheme fadein 1.0
    p "Hi, Evelynn."
    e "Wow! Du siehst ja wild aus [name]."
    e "Komm mal mit mir mit."
    p "Wohin denn?"
    show eparty happy2
    n "Sie packt mich an meinem Arm und zeigt auf jemanden der sich komisch bewegt, während andere..."
    p "Oh nein!" 
    p "Scharade."
    e "Genau."
    show eparty happy2 at rightish with move
    show rparty talk at leftish with dissolve
    "Ich bin doch schlecht in Scharade"
    r "Hey ihr zwei, spielt doch mal was vor."
    e "Gleich zu Anfang an?"
    e "Ich wollte doch erst raten."
    p "Genau! Können wir uns nicht erst hinsetzen?"
    show rparty vhappy
    r "Nein. Ihr seid die Neuen, ihr dürft gleich starten."
    menu:
        "Ich möchte anfangen.":
            p "Gut, dann fang ich eben an. Aber Evelynn, du kommst danach dran."
            e "Danke trotzdem."
            n "Randy gibt mir einen Zettel auf dem steht... natürlich."
            hide rparty vhappy
            n "Radzilla..."
            show eparty happy2 at rightish
            show oparty happy at center
            show aparty n at leftish
            with dissolve
            
            menu:
                "Dinosauriergebrüll":
                    p "Roooaaaar"
                    show oparty mad
                    show eparty mad
                    e "Keine Geräusche. Kein Schummeln."
                    r "Richtig"
                    o "Tss... tss... tsss..."

                "Umherstampfen":
                    show aparty mad
                    show eparty talk2
                    show oparty talk
                    e "Ein Monster!"
                    o "Vielleicht ein Minotaurus?"
                    a "Ich als Cowboy? Nicht lustig."
                
                "Rumstehen":
                    show eparty talk2
                    show oparty mad
                    e "Los, mach was."
                    e "Trau dich."
                    o "Voll lahm."
                    n "Lampenfieber. OK ich schaff das schon..."
            
            n "Ich sollte wohl noch mehr machen."
            menu:
                "Stampf über die Kartonstadt.":
                    show eparty happy2
                    show oparty happy
                    show aparty jabber
                    e "Das Monster das gerade im Fernsehen läuft!"
                    a "Radzilla! Du bist Radzilla!"
                    o "Nicht schlecht."

                "Gib auf!":
                    p "Tut mir Leid, fühl mich unwohl."
                    show oparty buh                    
                    show eparty talk2
                    show aparty n
                    e "Wirklich, du gibst auf?"
                    o "Typisch."
                    p "Entschuldigung."
                    
                "Floppe auf dem Boden herrum.":
                    show oparty happy
                    show eparty mad
                    show aparty shock
                    e "Ähm. Fisch auf dem Trockenen?"
                    a "Trauriger Wal?"
                    r "Radzilla?"
                    p "Richtig!"
                    r "Also, so toll hast du den jetzt nicht gespielt. Aber du wolltest wohl etwas kaputt machen."
                    p "Ääääähhhm... Richtig, das wollte ich."
                    n "Falsch."
            
            hide oparty
            hide aparty
            show eparty talk2 at rightish with move
            show rparty vhappy at leftish with moveinleft
            r "So,jetzt bist du dran Evelynn."
            e "Jetzt schon?"
            r "Ihr seid die Neuen, also ja."
            e "O... OK."
            n "Evelynn will gerade loslegen als Randy's Mama um die Ecke schaut."
            show rmum talk at left with moveinleft
            rmum "Kommt Kinder! Es gibt Kuchen!"
            r "Ohh Junge! Ist der mit Kuchengeschmack?"
            n "Natürlich rennen wir sofort alle an den Esstisch."
            jump foto
            
            
        "Evelynn darf anfangen.":
            p "Komm Evelynn, du fängst an."
            show eparty mad at rightish
            e "Was? Wieso?"
            p "Wir müssen eh beide spielen und du hast mich hier her gebracht."
            show eparty talk2 at rightish
            e "Na gut."
            r "Evelynn, dein Wort ist..."
            "Randy gibt ihr einen Zettel."
            hide rparty talk with dissolve
            show eparty talk2 at center with move
            r "Bereit?"
            e "Ja."
            r "Los."
            hide eparty talk 
            show epanto
            n "Was macht die da?"
            
            menu:
                "Jemand der seitlich steht":
                    p "Ein umfallender Mensch."
                
                "Skateboarder":
                    p "Skateboardfahrer!"
                
                "Keine Ahnung!":
                    p "Ääähm, was bitte?"
            
            r "Radzilla? Der steht auch viel rum."
            a "Sumo-Ringer?"
            a "Ganz sicher."
            o "Der Turm von Pisa!"
            
            show epantobaum
            hide epanto
            n "Evelynn nimmt einen Karton und stellt sich darauf, ich glaube es könnte..."
            menu:
                "...ein Surfer...":
                    "...sein."
                    p "Surfer!"
                    hide epantobaum 
                    hide epanto
                    show eparty happy2 at center
                    e "Richtig!"
                    n "Wieso starren die mich an?"
                    a "Sauber!"
                    a "Hab nicht an so etwas gedacht."
                    show eparty mad at rotation
                    e "Wooosh"
                    "Alle" "Aaaaaah!"
                    r "Jetzt siehst du auch wie eine Surferin aus."
                    "Evelynn schaut mich weiterhin an."
                    menu:
                        "Schauspiel loben.":
                            p "Evelynn ist doch eine gute Schauspielerin. War doch nicht so schwer."
                            show eparty happy2 at center
                            o "Angeber."
                            r "Jetzt bist du dran [name]. Los!"
                            "Randy reicht mir einen Zettel..."
                            n "Ich will gerade loslegen als Randy's Mama um die Ecke schaut."
                            show rmum talk at left with moveinleft
                            rmum "Kommt Kinder! Es gibt Kuchen!"
                            r "Ohh Junge! Ist der mit Kuchengeschmack?"
                            n "Natürlich rennen wir sofort alle an den Esstisch."
                            jump foto
                            
                        "Nichts sagen.":
                            p "..."
                            show eparty mad at center
                            "Evelynn schaut mich einfach weiter an."
                            e "Du bist dran!"
                            r "Stimmt, hier dein Zettel!"
                            n "Ich will gerade loslegen als Randy's Mama um die Ecke schaut."
                            show rmum talk at left with moveinleft
                            rmum "Kommt Kinder! Es gibt Kuchen!"
                            r "Ohh Junge! Ist der mit Kuchengeschmack?"
                            n "Natürlich rennen wir sofort alle an den Esstisch."
                            jump foto

                "...garnichts...":
                    "...sein."
                    r "Prince Ape? Der klettert auf Bäume."
                    a "Ein Affe? Das kann stimmen."
                    o "Ääähm. Breitbeiniger Specht?"
                    e "Wooosh."
                    r "Keine Geräusche!"
                    hide epantobaum
                    hide epanto
                    show eparty mad at center
                    e "Tut mir Leid, ich kann das nicht..."
                    a "Los, was bist du?"
                    e "Surferin."
                    show eparty mad at rotation
                    e "Wooosh"
                    "Alle" "Hmmmmh."
                    "Evelynn schaut mich an."
                    menu:
                        "Schauspiel loben":
                            p "Ist auch kein leichtes Wort, schlecht hast du nicht gespielt."
                            show eparty happy2 at center
                            o "Ähm was?"
                            r "Jetzt bist du dran [name]. Los!"
                            "Randy reicht mir einen Zettel..."
                            n "Ich will gerade loslegen als Randy's Mama um die Ecke schaut."
                            show rmum talk at left with moveinleft
                            rmum "Kommt Kinder! Es gibt Kuchen!"
                            r "Ohh Junge! Ist der mit Kuchengeschmack?"
                            n "Natürlich rennen wir sofort alle an den Esstisch."
                            jump foto

                        "Mit dem Rest schweigen":
                            "..."
                            show eparty talk2 at center
                            e "Du bist dran!"
                            r "Stimmt, hier dein Zettel!"
                            n "Ich will gerade loslegen als Randy's Mama um die Ecke schaut."
                            show rmum talk at left with moveinleft
                            rmum "Kommt Kinder! Es gibt Kuchen!"
                            r "Ohh Junge! Ist der mit Kuchengeschmack?"
                            n "Natürlich rennen wir sofort alle an den Esstisch."
                            jump foto
                            
                    
                "...ein Baumkletterer...":
                    "...sein."
                    p "Kletterer?"
                    r "Prince Ape? Der klettert auf Bäume."
                    a "Ein Affe? Das kann stimmen."
                    o "Ääähm. Breitbeiniger Specht?"
                    e "Wooosh."
                    r "Keine Geräusche!"
                    hide epantobaum
                    hide epanto
                    show eparty mad at center
                    e "Tut mir Leid, ich kann das nicht..."
                    a "Los, was bist du?"
                    e "Surferin."
                    show eparty mad at rotation
                    e "Wooosh"
                    "Alle" "Hmmmmh."
                    "Evelynn schaut mich an."
                    menu:
                        "Schauspiel loben":
                            p "Ist auch kein leichtes Wort, schlecht hast du nicht gespielt."
                            show eparty happy2 at center
                            o "Ähm was?"
                            r "Jetzt bist du dran [name]. Los!"
                            "Randy reicht mir einen Zettel..."
                            n "Ich will gerade loslegen als Randy's Mama um die Ecke schaut."
                            show rmum talk at left with moveinleft
                            rmum "Kommt Kinder! Es gibt Kuchen!"
                            r "Ohh Junge! Ist der mit Kuchengeschmack?"
                            n "Natürlich rennen wir sofort alle an den Esstisch."
                            jump foto

                        "Mit dem Rest schweigen":
                            "..."
                            show eparty talk2 at center
                            e "Du bist dran!"
                            r "Stimmt, hier dein Zettel!"
                            n "Ich will gerade loslegen als Randy's Mama um die Ecke schaut."
                            show rmum talk at left with moveinleft
                            rmum "Kommt Kinder! Es gibt Kuchen!"
                            r "Ohh Junge! Ist der mit Kuchengeschmack?"
                            n "Natürlich rennen wir sofort alle an den Esstisch."
                            jump foto
    
label foto:
    rmum "Kommt mal alle zusammen für ein Gruppenfoto."
    "Auch noch so was. Na gut."
    rmum "Los alle. Käsekuchen!"
    scene cg selfiefriendo
    "Alle" "Käääääseeeekuuuucheeeen!!"
    "... Nett."
    scene bg street with dissolve
    jump scene22
    
    
label scene21:
    n "Na dann, auf zum Tisch."
    show oparty buh at rightish
    play music octatheme
    o "BOOOH"
    o "Haha."
    show oparty happy
    p "Octavia."
    o "Cooles Kostüm, [name]"
    o "Sieht sogar mal gut aus."
    show oparty talk
    p "Danke? Seh ich wohl sonst nicht gut aus?"
    o "Ja, aber du scheinst ja doch was zu können."
    p "Du siehst auch gut aus."
    show oparty happy
    o "Ich bin die Medusa aus der griechischen Antike."
    p "Die Schlangen Haare sehen mega gruselig aus."
    o "Sag mal."
    p "?"
    o "Willst du mir bei was helfen?"
    p "Was willst du denn genau machen?"
    show oparty talk
    o "Anja erschrecken, so wie dich."
    o "Die ist zwar etwas zäh, aber ich glaub ich kann das schaffen."
    o "Es ist eine Monsterparty. Sie wird es uns nicht übel nehmen."
    p "Mmmh... Na gut und wie willst du sie erschrecken?"
    o "Schau mal. Die Bäume da hinten, ich duck mich dahinter und bin dann versteckt."
    o "Du lockst Anja dort hin und dann..."
    p "Und dann?"
    show oparty buh
    n "Die hat echtes Talent für sowas."
    show oparty talk
    o "Ich hoffe Sie erschreckt sich so, das Sie zu Stein erstarrt."
    p "Zu Stein?"
    o "Jeder der die Schlangen der Medusa anschaut wird zu Stein laut Legende, aber ich hab ja nur ein Kostüm."
    o "Bereit?"
    p "In Ordnung."
    n "Zu Stein erstarren? Das will ich sehen!"
    n "Aber Octavia hat auch recht, Anja ist Zäh."
    hide oparty talk
    scene bg partyocta
    n "So, wo ist Anja."
    show aparty n
    p "Hey Anja!"
    show aparty jabber
    a "Hi [name], was bist du denn?"
    p "Ein KILLERwal!"
    p "Und du bist der Sheriff dieser Stadt."
    p "Aber Cowboys sind doch keine Monster?"
    show aparty talk
    a "Mein Papa sagt, sie sind wie riesige Monster gewesen, zumindest gegen die Einheimischen."
    p "Wer sind die Einheimischen?"
    show aparty n
    a "Keine Ahnung."
    a "ABER! Ich kann auch ein MonsterJÄGER sein."
    p "Macht wenig Sinn."
    a "Aber ein Killerwal?"
    n "Guter Punkt!"
    p "Willst du vielleicht bei den Bäumen spielen?"
    a "Aber das sind doch gar keine echten Bäume?"
    p "Ja und? Ist doch egal."
    show aparty mad
    a "Wale können nicht klettern."
    n "Mmmh, irgendwie will sie nicht. Hab ich was Falsches gesagt?"
    n "Egal. Ich kann sie überzeugen."
    menu:
        "WALDKILLERwal":
            n "Dann bin ich eben der erste WALDKILLERwal und du wirst berühmt für deine Entdeckung!"
            show aparty jabber
            a "So richtig glaub ich dir das nicht."
            a "Aber egal, lass uns spielen!"
        
        "In Panama gibt es Dschungel-Wale":
            p "Ich hab mal gehört, in Panama gibt es Wale die im Dschungel sind. Auf so großen Wassern."
            show aparty shock
            a "So etwas kann es geben?"
            a "Wow."
            show aparty talk
            a "Na gut,lass uns klettern."
        
        "Klettern ist klettern":
            p "Klettern ist klettern. Macht doch trotzdem Spaß."
            show aparty mad
            a "Recht haste ja."
            "..."
            show aparty talk
            a "Na gut, wenn du es willst."
            n "Irgendwie hat‘s ja doch geklappt."
            
    show aparty n
    a "Die Bäume sind echt klein, aber eventuell wenn wir..."
    scene bg party
    show oparty buh at rightish
    show aparty shock at leftish
    o "HSSSSSS!"
    "{color=#0099ff}[name]:{/color} AAAAH! \n{color=#0099ff}Anja:{/color} AAAH! HIMMEL HERRGOTT SACKERER!"
    n "Jetzt hab sogar ich mich erschreckt!"
    show oparty vhappy 
    o "Ihr beide hattet ja echt mega Angst."
    o "Ihr seid ja wirklich erstarrt!"
    show aparty mad
    a "Wieso machst du sowas!"
    o "Ruhig, ist doch eine Monsterparty"
    a "Manchmal bist du echt doof!"
    show oparty mad
    o "Aber niemals so doof wie du."
    a "Du hast gerade bewiesen, dass es dümmer geht als ich."
    o "Also gibst du zu, dass du dumm bist?"
    a "AAAAH!"
    n "Oh man, wieder ein Streit. Aber diesmal gibt es einen Ausweg!"
    p "LEUTE! LEUTE! RUHIG!"
    show oparty n
    show aparty n
    "...."
    p "Kuchen!"
    show oparty talk
    o "Wie bitte?"
    a "Ich versteh‘s auch nicht."
    p "Wir sind hier auf einer Party, wollen wir nicht mal etwas Kuchen essen?"
    o "Ich mein... Eigentlich schon."
    show oparty n
    show aparty talk
    a "Kuchen hört sich gut an."
    p "Dann auf zum Kuchen Mampfen." 
    p "Sag mal, was hast du da vorhin eigentlich gesagt Anja." 
    a "Das sagt mein Papa auch immer."
    show oparty talk
    o "Ach sooo! Hab mich das auch schon gefragt."
    p "???"
    o "Mist, versprochen."
    n "Wir reden noch ein bisschen und spielen im Wald, es ist wohl doch wieder alles gut."
    
    p "ooof... Fertig"
    show rmum nerv
    rmum "Keine Müdigkeit vortäuschen."
    show rmum talk
    rmum "Kommt mal alle zusammen für ein Gruppenfoto."
    n "Auch noch so was. Na gut."
    rmum "Los alle. Käsekuchen!"
    scene cg selfieorca
    "alle" "Käääääseeeeekuuuuucheeeeen!"
    n "... Nett."
    scene bg street


    jump scene22
    
label scene22:
    stop music fadeout 1.0
    play music maintheme  
    show car at rightish
    show dad talk at leftish 
    with dissolve
    "Papa:" "Hi, [name]! Lang nicht mehr gesehen."
    p " PAPA!"
    "Papa:" "Na, wie war die Feier? Cool, dass du schon neue Freunde gefunden hast."
    p "Ich weiß nicht."
    "Papa:" "Hmmmh, naja das wird schon. Im Kindergarten gibt es öfters mal was. Ich kann mich noch daran erinnern wie wir immer..."
    n "Papa erzählt gerne Geschichten von früher. Das ist meistens auch ganz spannend. Auf jeden Fall wird das keine langweilige Heimfahrt."
    
  
   ##### TAG 5 ENDE #####
            
  ##### TAG 6 BEGINN #####
    
label scenew2_0:
    scene bg black with fade
    show mnd with fade
    pause 1.5
    hide mnd with fade
    scene bg street
    play sound cardoor2
    show car at rightish
    show dad n at center
    with fade
    n "Man, das Wochenende bei Papa war echt toll."
    n "Irgendwie ist es komisch ihn nur noch am Wochenende zu sehen."
    show bananasplit at center with dissolve
    n "Immerhin machen wir jetzt mehr zusammen. Und das extra große Banana Split bei Waluigi’s war echt lecker."
    hide bananasplit
    show cg gameboy with dissolve
    n "Außerdem hab' ich jetzt ein Vega PlayGear und ich darf es sogar mit in den Kindergarten nehmen."
    hide cg gameboy with dissolve
    n "Oh, ich glaub wir sind schon da. Das ging ja schnell. Mit Mama dauert die Fahrt irgendwie länger." 
    show dad talk
    v "Na? Hat das Wochenende Spaß gemacht?"
    menu:
        "Es war super!":
            p "JA! Das war voll cool! Der Mega Playgear macht voll viel Spaß!"
            v "Na das wusste ich doch dass der dir gefallen wird [pre] Klein[suf2]."
            v "Du hast dir denn doch schon so lange gewünscht. Wenn du mal was anderes möchtest, dann sag’s mir einfach, okay?"
            p "Mach ich!"
            
        "War ganz gut.":
            p "Ja, danke Papa! Eigentlich bin ich lieber bei Mama, aber diesmal war es echt cool!"
            v "Das freut mich, ich weiß ja dass du lieber bei deiner Mama bist. Aber dein alter Herr ist doch auch ganz cool, oder?"            
    
    show dad n
    n "So, wie Papa jetzt ist, mag ich ihn fast lieber als früher. Sein Auto ist auch viel cooler."
    n "Trotzdem wäre es schöner wenn er wieder bei uns einziehen könnte..."
    
    scene bg court
    show dad talk at center
    with fade
    v "Da wären wir, das ist also dein neuer Kindergarten… Du hast bestimmt viel Spaß, oder? Hast du denn schon neue Freunde gefunden?"
    menu:
        "Ja!":
            p  "Ja, ich mag die anderen, wir spielen ganz viel zusammen!"
            v "Das freut mich! Dann mal ab mit dir in den Kindergarten, viel Spaß mein Kleiner!"
            
        "Ein paar.":
            p "Ähm… ein paar schon, ja…"
            v "Das wird schon, keine Sorge. Du bist ja erst eine Woche da."
            
        "Nicht wirklich...":
            p "Bis jetzt noch nicht so viele, nein…"
            v "Naja, du kennst die anderen Kinder ja wahrscheinlich auch noch nich so gut, ihr werdet euch bestimmt bald anfreunden."
            
    n "Papas Bart kratzt in letzter Zeit immer wenn er mir auf die Stirn küsst. Das nervt!"
    n "Und weg ist er auch schon wieder. Ich freue mich irgendwie schon, Mama später wieder zu sehen."
    
    
label scenew2_1:
    stop music fadeout 1.0
    pause 0.75
    play music anjatheme fadein 1.0
    scene bg flur
    show anja hihi at center
    with fade
    a "Sag mal, deine Haare sind ja nass! Hattest du keine Zeit sie zu trocknen?"
    p "Nein, ich…"
    a "Also ich werde gar nicht erst mit nassen Haaren aus dem Haus gelassen. Meine Eltern meinen, ich könnte mich erkälten, dabei ist es ja bloß der Weg zum Auto."
    p "Ich hatte keine Zeit…"
    a "Apropos Auto, dein Papa hat ja voll die coole Karre. Ich habe euch gesehen, als ihr hier angekommen seid. Der scheint ja mega viel zu verdienen!"
    p "Ja, er…"
    a "Mein Papa verdient nicht so viel, aber trotzdem kauft er mir immer wieder schöne Geschenke, wie neulich, da hat er mir…"
    n "Mit Anja zu reden macht manchmal wirklich keinen Spaß. Randy sitzt da drüben so alleine. Vielleicht hat er was Spannenderes zu erzählen."
    hide anja
    scene bg grura
    show karin go at center with dissolve
    n "Heute reden wir im Morgenkreis über Bauernhoftiere, wie z.B. Kühe, Schweine und Schafe."
    show dino at center with dissolve
    n "Nur warum können wir nicht lieber über coole Tiere wie Dinosaurier reden? Wen interessiert denn schon, dass eine Kuh \"muh\" macht"
    n "Ich will wissen was ein T-Rex für ein Geräusch macht: Bestimmt \"rawr\" oder sowas."
    hide dino with dissolve
    
label scenew2_2:
    
    hide karin
    play music maintheme
    n "Der Morgenkreis ist endlich vorbei!"
    n "Ich will endlich Fightë Møn weiter spielen! Ich mach die Arenen heute fertig!"
    n "Eigentlich will ich mir aber auch noch Maltipps von Eveylnn holen."
    n "Ich kann ja auch zu Hause weiter spielen."
    n "Hmmmh"
    menu:
        "Konsole spielen":
            n "Malen kann ich ja immer noch wann anders lernen."
            n "Erst sollte ich alle Arenen erledigen, wenn ich schon damit angefangen habe!"
            n "Außerdem hör ich eh schon die Musik..."
            n "Moment, die ist ja sogar da hinten wo Octavia sitzt."
            play music octatheme
            show octa happy
            n "Sie hat einen Blattsilbernen limitierten PlayGear!"
            n "Ich zeig ihr mal meinen!"
            p "Hey Octavia!"
            show cg gameboy with dissolve
            p "Guck mal was ich auch habe!"
            o "Fightë Møn?"
            p "Ja."
            o "Weißt du..."
            p "Ja?"
            o "Es gibt schon Fightë Møn 2" 
            p "Doch ich möchte [ddd] beste Ausbilder[suf3] der Welt werden! Genau wie im Fernsehen."
            o "Ich brauch nur noch eine handvoll an Monstern, dann bin ich das zuerst!"
            p "Du bist doch nicht deswegen besser!"
            o "Ich beweis es dir! LOS, LASS KÄMPFEN!"
            n "Ich kann es kaum sehen, aber Octavia steckt ein Kabel in mein Gerät und an ihres. Wie es aussieht muss ich wohl kämpfen."
            o "LOS!"
            menu:
                "win":
                    $ mon = "win"
                    "PLACEHOLDER FÜR DEN KAMPF" #####
                    
                "loss":
                    $ mon = "loss"
                    "PLACEHOLDER FÜR DEN KAMPF" #####
            
            if mon == "win":
                show bg grura
                show octa shock
                o "Wie? Ich hab doch fast alle."
                o "Nein!"
                n "Was ist denn jetzt los?"
                show octa mad
                o "Das Spiel ist  eh Mist!"
                o "Bei allem anderen würde ich dich haushoch besiegen!"
                p "Dann schlag doch was vor."
                show octa smug
                o "Na gut. Also wir machen immer so Wettrennen im Hof und da bin ich die Beste. Einige sind gut, sicher. Andere sogar sehr gut, aber niemand hat mich bis jetzt besiegen können und das wirst du auch nicht schaffen! Das kannst du mir aber glauben."
                p "Ich bin auch ziemlich schnell."
                o "Ich warne dich vor. Ich bin viel schneller. Versuchen brauchst du es eigentlich gar nicht!"
                p "Ich hab bereits die Herausforderung angenommen!"
                show octa talk
                o "Alles klar."
                o "Aber erst einmal, wollen wir vielleicht ein paar unserer Fightë Møn tauschen?"
                o " Du hast noch nicht so viel und ich kann eines von dir gebrauchen!"
                n "Irgendwie vertrau ich ihr da nicht so ganz."
                p "Nein, ich muss mich auf unseren Wettkampf vorbereiten!"
                jump scenew2_3
    
    
            else:        
                show bg grura
                show octa smug
                o "Hab ich's dir doch gesagt."
                o "Bin eben viel besser als du. Dachte du hast eigentlich mehr drauf, aber ein echter Gegner bist du wohl nicht."
                o "Lern erst einmal zu spielen!"
                n "Octa ist gerade echt gemein..."
                p "Hey!"
                show octa talk
                o "Was denn Verlierer?"
                p "Ach ich geh!"
                show octa smug
                o "Alles klar, viel Spaß noch!"
                
        "Mit Evelynn malen":
            n "Ich kann ja auch noch Nachmittag daheim spielen, erst einmal zu Evelynn!"
            n "Der Maltisch ist wohl heute wirklich voll. Randy hat sich wohl alle Brettspiele geschnappt."
            scene bg grura2
            show eve draw 
            n "Was malt die denn da?"
            show mantikoreve with fade
            hide mantikoreve with fade
            n "Ich kann gar nichts sehen. Die Anderen standen im Weg!"
            n "Aber es sah interessant aus, vielleicht kann ich es ja nachzeichnen!"
            n "Ich probier es mal."
            n "Erst einmal der Hintergrund!"
            scene memory bg
            play music evetheme
            scene memory bg
            
            n "Sooo, doch welche Farbe hatte das Tier?"
            
            menu:
                "Rot":
                    $ colo = "r"
                    show rot
                    play sound draw
                    n "Es war aggressiv! Also Rot!"
                
                "Orange":
                    $ colo = "o"
                    show orange
                    play sound draw
                    n "Es sah aus wie ein echtes Tier. Viele sind Orange!"
                
                "Lila":
                    $ colo = "l"
                    show lila
                    play sound draw
                    n "Evelynn mag viele Farben, also wohl Lila!"
            
            n "Moment, was war es überhaupt für ein Tier?"
               
            menu:
                "Echse":
                    $ body = "e"
                    show echse
                    play sound draw
                    "Genau, groß und lang wie eine Echse!"
                "Löwe":
                    $ body = "l"
                    show loewe
                    play sound draw
                    "Es war stark, so wie ein Löwe!"
                "Hase":
                    $ body = "h"
                    show hase
                    play sound draw
                    "Es sah irgendwie niedlich aus, wie ein Hase!"
            
            
            n "Hatte es einen Schwanz?"
            n "So einen habe ich glaub ich schon einmal im Fernsehen gesehen, doch nur wo?"
            n "Welcher Schwanz hat das Tier?"
            menu:
                "Skorpion":
                    $ schwanz = "s"
                    show sschwanz
                    play sound draw
                    n "Bei einem Skorpion, die sind super giftig!"
                "Drache":
                    $ schwanz = "d"
                    show dschwanz
                    play sound draw
                    n "Evelynn mag Fantasiebücher, Drachen kommen häufig vor!"
                "Löwe":
                    $ schwanz = "l"
                    show lschwanz
                    play sound draw
                    n "Löwe ist aufjedenfall mit drinnen, so viel weiß ich!"
            
            n "Irgendwas fehlt noch. Doch was?"
            n "Flügel?"
            n "Egal, Flügel!"
            menu:
                "Fledermaus":
                    $ flug = "f"
                    show fwings
                    play sound draw
                    n "Das waren eindeutig Fledermausflügel!"
                "Drache":
                    $ flug = "d"
                    show dwings
                    play sound draw
                    n "Es waren dunkle starke Flügel!"
                "Vogel":
                    $ flug = "v"
                    show bwings
                    play sound draw
                    n "Vögel sind die besten was fliegen an geht, also muss es wohl das sein!"
            
            n "So!"
            n "Meisterwerk vollendet!"
            scene bg grura2
            show eve draw
            p "Schau mal Evelynn!"

            if colo == "o" and body == "l" and schwanz == "s" and flug == "d":
                show edraw talk
                e "Aaa... Also.."
                show edraw mad
                n "Nanu?"
                e "Ein komisches Monster hast du da ja, ich weiß ja nicht."
                show edraw talk
                e "Ich mein ja, woher hast du so eine Idee?"
                e "Was kann es denn? Wieso hast du dich für diese Farben entschieden?"
                hide eve
                show eve draw
                n "Evelynn will echt viel Wissen, dafür dass es so ein komisches Monster ist."
                n "Außerdem wieso verhält Sie sich so komisch?"
                hide eve
                show edraw mad
                n "Ich sollte ihr nicht sagen, dass ich das Bild versucht habe von ihr abzumalen."
                n "Nanu? Wer tippt mich da an?"
                hide eve
                jump scenew2_3
            
            else:
                show edraw mad
                e "Hmmmh!"
                n "Was schaut Sie denn so kritisch?"
                e "Das sieht ja schon mal ganz gut aus, aber du solltest schauen besser auszumalen, außerdem kann man ganz leicht Licht hinzufügen. Farbwahl ist auch..."
                n "Evelynn kann ganz gut meckern, aber es stimmt was sie sagt. Bin ich nicht deswegen hergekommen?"
                n "Moment, bin ich das?"
                show edraw talk
                e "Es ist aber trotzdem hübsch, viele tolle Ideen."
                p "Danke!"
                n "Nanu? Wer tippt mich da an?"
                jump scenew2_3
                hide eve
    
label scenew2_3:
    stop music fadeout 1.0
    pause 0.75
    play music maintheme fadein 1.0
    scene bg grura
    show randy talk at rightish
    r "[name]!"
    n "Was will denn Randy von mir?"
    r "Lust auf eine Runde Oligopoly? Wir brauchen noch jemanden um Zwei gegen Zwei zu spielen!"
    n "Oligopoly ist super."
    p "Auja, da bin ich dabei! Bin nur noch nicht wirklich gut."
    show randy happy
    r "Dann bist du eben in meinen Team, ich kenne die Tricks."
    show bg grura2
    r "Das sind wieder 200!"
    p "Randy und ich sind wohl ein echt gutes Team, noch ein bisschen und wir haben das in der Tasche."
    show mum talk at leftish
    m "Hallo, mein Schatz!"
    p "Och nööö."
    n "Wir haben doch nicht gar nicht so lange gespielt!"
    m "Nööö was?"
    show mum mad
    p "Ich war nur gerade am gewinnen und jetzt bist du da."
    show mum talk
    m "Ach so, aber dann hat's dir doch Spaß gemacht. Und wie war dein Wochenende beim Papa?"
    n "Ich zeig ihr einfach was Papa mir geschenkt hat."
    show cg gameboy with dissolve
    show mum vmad
    m "DAS KANN NICHT SEIN ERNST SEIN!"
    hide cg gameboy with dissolve
    n "Was hat Mama denn?"
    m "Die Dinger kosten doch ein Vermögen. Und das einfach so, der will doch sicherlich nur..."
    m "Schau aber ja nicht zu lange in diese Dinger, sonst werden deine Augen noch rechteckig."
    p "So viele Spiele hab ich auch nicht."
    n "Mama gefällt wohl mein Geschenk nicht. Wenn man so alt wird, spielt man mit so etwas auch nicht mehr hat mir mal jemand gesagt."
    m "Egal, jetzt gehts erst mal Heim!"
    scene bg black with dissolve
    play sound cardoor1
    n "..."
    n "Vielleicht kann ich ja morgen fertig spielen..."
    
    
label scenew2_4:
    stop music fadeout 1.0
    pause 0.75
    play music introtheme fadein 1.0
    scene bg grura
    n "...oder auch nicht. Wieso wurde alles aufgeräumt?"
    show karin go
    k "Kinder! Alle herkommen! Der Morgenkreis fängt an!"
    show karin talk
    k "Diesen Morgen wollen wir uns erst einmal alle ein bisschen aufwärmen."
    k "Ich zeige euch etwas und ihr versucht mir das dann nachzumachen, okay?"
    "Alle" "Ja, machen wir Karin!"
    show karin vhappy
    k "Denn wenn wir heute fertig sind mit unserem Morgenkreis, gehen wir gemeinsam nach draußen."
    k "Dieses tolle Wetter müssen wir ausnutzen!"
    p "Wenn man keine Wolken sieht, dann bleibt das Wetter schön, sagt meine Mama immer."
    k "Genau."
    hide karin with moveoutbottom
    n "Moment..."
    n "Was macht Karin da jetzt auf den Boden?"
    k "Das nennt man Yoga! Puuh."
    show karin go with moveinbottom
    k "Alle gesehen? Da könnt ihr euch richtig austoben!"
    n "Na gut, dann linker Fuß nach hinten..."
    scene bg black with dissolve
    k "So, die dritte Übung ist folgende..."
    k "..."
    k "Genau, so wie bei Octavia!"
    O "ist auch voll leicht."
    k "Nun, weiter..."
    n "..."
    stop music fadeout 1.0
    pause 0.75
    play music maintheme fadein 1.0
    scene bg court with dissolve
    n "Endlich ist das vorbei."
    n "Das wurde ja echt anstregend.."
    n "Und diesen ... Hund? Den hab ich echt nicht mehr verstanden."
    n "Naja, wenigstens darf ich mich jetzt ausruhen."
    show octa vhappy at left with moveinright
    show anja jabber at rightish with moveinright
    a "Dich krieg ich noch."
    o "Vielleicht in 100 Jahren!"
    hide octa with moveoutleft
    hide anja with moveoutleft
    n "Moment. Wieso rennt jeder rum?"
    n "Ich kann ja trotzdem zu..."
    show karin shock at rightish
    show eve talk2 at leftish
    with moveinbottom
    k "Evelynn, tut mir Leid. Das ist die letzte Kreide."
    e "Danke Karin."
    hide karin
    hide eve
    with moveoutbottom
    n "Dann muss ich wohl anderswo mitmachen, aber wo?"

    menu:
        "Sandkasten":
            scene bg sand
            window hide
            nt "Mal sehen, was Louis da so macht!"
            jump scenew2_5

        "Ball spielen":
            scene bg ball
            n "Wenn jeder spielt, dann muss ich wohl auch mitmachen."
            
label scenew2_5:
    scene bg sand
    show burg
    show sandauto
    show sandkuchen
    show sandpyramide
    with dissolve
    $ scastlep = 0
    pt "Hey, Louis!"
    Lt "Oh, hi [name], willst du mitmachen?"
    pt "Hää… wie mitmachen. Bei was denn?"
    Lt "Na, wir spielen Geschichten erzählen."
    pt "Wie spielt man denn etwas zu erzählen?"
    Lt "Wie, das weißt du nicht?"
    Lt "Na gut, okay ich erklärs."
    Lt "Also ich fange einen Satz an und du vervollständigst den dann. Und da wird dann eine Geschichte draus."
    Lt "Schau ich hab hier zum Beispiel ein Schloss gebaut."
    nt "Naja, ob das wie ein Schloss aussieht... Wie hat er es überhaupt geschafft, dass das so schief steht."
    nt "Heißt das, er hat die anderen Sachen gar nicht gebaut? Wer baut denn ein Auto und ne Pyramide und lässt die dann einfach stehen?"
    nt "Und ich glaube auch nicht, dass Randy den Sand essen sollte. Meine Mama sagt zumindest immer, dass man das nicht macht."
    Lt "…und dann könnte man zum Beispiel…"
    Lt "Hey [name], hörst du mir überhaupt zu?"
    pt "Ääääh… was?"
    Lt "Oh man, hör halt mal zu! Und Randy hör auf den Sandkuchen zu essen. Den hab ich gestern gebaut. Der ist nicht zum essen."
    rt "Sorry… er sieht so lecker aus. Und er schmeckt nach Zitrone."
    Lt "Ach, mach, was du willst."
    Lt "Also, hörst du mir jetzt zu [name]?"
    pt "Ja, klar."
    Lt "Gut, dann los!"
    Lt "Heute erzählen wir die Geschichte von einem schrecklichen Ort…"
    nt "Er deutet auf seine Sandburg. Ich glaub er will, dass ich ihr einen Namen gebe…"
    
    menu:
        "Äh...Schloss...äh Sand..gel.":
            $ burgname = "Burgname1"
            $ enemyname = "Enemy1"
            $ scastlep += 1
            Lt "Naja gut. Wenn du meinst..."
            Lt "Wir erzählen also die Geschichte von Schloss Sandgel, in dem der schwarze Ritter wohnt."
            show badboy with dissolve
            Lt "Der schwarze Ritter ist böse und tyra… tyrann… also er ärgert die Bewohner des Landes."
            show badboy at badsafe behind burg
            with MoveTransition(1.0)
            
        "Die Schreckensburg von Zauberer Dunkelbös.":
            $ burgname = "Burgname2"
            $ enemyname = "Enemy2"
            $ scastlep += 2
            Lt "Oh, ja das klingt gut!"
            Lt "Wir erzählen also die Geschichte vom bösen Zauberer Dunkelbös der in seiner Schreckensburg lebt."
            show badboy with dissolve
            Lt "Wie gesagt der Zauberer ist böse und tyra… tyrann… also er ärgert die Bewohner des Landes."
            show badboy at badsafe behind burg
            with MoveTransition(1.0)
            
        "Ich weiß nicht. Mir fällt nichts ein... vielleicht ...Fort Knight.":
            $ burgname = "Burgname3"
            $ enemyname = "Enemy1"
            Lt "Man echt?"
            Lt "Voll der lahme Name. Aber wenn’s sein muss..."
            Lt "Wir erzählen also die Geschichte von Fort Knight in dem der dunkle Ritter wohnt."
            show badboy with dissolve
            Lt "Der schwarze Ritter ist böse und tyra… tyrann… also er ärgert die Bewohner des Landes."
            show badboy at badsafe behind burg
            with MoveTransition(1.0)
            
            
    if burgname == "Burgname1":
        python:
            burg = "Burg Sandgel"
        
    if burgname == "Burgname2":
        python:
            burg = "Schreckensburg" 
        
    if burgname == "Burgname3":
        python:
            burg = "Burg Fort Knight" 
        
    if enemyname == "Enemy1":
        python:
            enemy = "Ritter" 
        
    if enemyname == "Enemy2":
        python:
            enemy = "Zauberer" 
        

            
            
    Lt "Und deswegen haben sich drei mutige Helden zusammengeschlossen um den [enemy] zu besiegen."
    show held
    show knight
    show wizzard
    with dissolve
    pt "Und wie heißen die?"
    Lt "Ähhh... das weiß keiner."
    Lt "Ach ja und um die [burg] betreten zu können müssen die Helden drei Prüfungen bestehen damit ..."
    Lt "Ähh.. sie drei Teile eines magischen Schlüssels erhalten."
    Lt "Ihre Reise beginnt also. Als Erstes müssen sie..."

    menu:
        "...auf die Spitze der Pyramide des Verderbens klettern.":
            show doom with dissolve
            show wizzard at pyhero
            show knight at pyhero
            show held at pyhero
            with MoveTransition(1.5)
            $ scastlep += 2
            Lt "Auf ihrem Weg zum Schloss treffen die Drei auf eine riesige Pyramide."
            Lt "Nach drei harten Tagen haben sie es endlich bis zur Spitze der Pyramide geschafft. In der goldenen Spitze finden sie ein Fach mit einem Teil des Schlüssels."

        "die Ente des Verderbens besiegen.":
            show duck with dissolve
            show wizzard at duckhero
            show knight at duckhero
            show held at duckhero
            with MoveTransition(1.0)
            Lt "Eine Ente? Echt?"
            Lt "Meinst du das Ernst?"
            pt "Also ja..."
            Lt "Ach egal."
            Lt "auf ihrem Weg zur [burg] treffen sie auf eine riesige Ente, die einen Teil des Schlüssels um ihren Hals trägt."
            Lt "Nach einem harten Kampf, schaffen die Helden es der Ente das Halsband mit dem Teil des Schlüssels abzunehmen."

        "den gefährlichen Fluss des Verderbens überqueren.":
            show island behind sandpyramide with dissolve 
            $ scastlep += 1
            show wizzard at riverhero1
            show knight at riverhero1
            show held at riverhero1
            with MoveTransition(1.0)
            Lt "Okay."
            Lt "Auf dem Weg zur [burg] kommen sie an einem gefährlichen Fluss an. In der Mitte des Stroms ist eine Insel mit einer Schatztruhe."
            Lt "Leider ist die Brücke, die eigentlich zur Insel führen soll, zerstört."
            Lt "Die Helden schaffen es aber, ein Floß zu bauen. Sie überwinden den Strom und schnappen sich den ersten Teil des Schlüssels."
            show wizzard at riverhero2
            show knight at riverhero2
            show held at riverhero2
            with MoveTransition(1.5)

    Lt "Nachdem die Helden die erste Prüfung bestanden haben, müssen sie sich nun..."
    
    menu:
        "...mit dem magischen Aut...äh..pferdelosen Wagen gegen das schnellste Pferd des Landes antreten.":
            show horse behind sandauto with dissolve
            show wizzard at horsehero
            show knight at horsehero
            show held at horsehero
            with MoveTransition(1.0)
            $ scastlep += 2
            Lt "Der magische Wagen ohne Pferde steht vor den Helden. Bisher hat es keiner geschafft mit ihm zu fahren."
            pt "Aber die Helden sind mega klug!"
            Lt "Ja genau und weil sie so klug sind bringen sie den Wagen zum laufen."
            show horse at horserun
            with MoveTransition(0.5)
            Lt "Das Rennen gegen das Pferd ist dann fast einfach, denn nichts ist schneller als ihr Wagen. Der zweite Teil des Schlüssels ist jetzt ihrer."
            
        "...durch den Urwald des Verderbens schlagen.":
            show dschungel behind burg with dissolve
            Lt "Wie schon wieder ‘Verderben’?"
            Lt "Ist das nicht etwas langweilig?"
            pt "Nö wieso?"
            Lt "Na gut."
            show wizzard at dschhero
            show knight at dschhero
            show held at dschhero
            with MoveTransition(1.0)
            Lt "Die Helden schlagen sich also durch diesen gefährlichen Urwald. In dem Urwald lauern viele Gefahren wie Krokodile und Schlangen. Trotzdem halten die Helden bis zum Schluss durch und finden den zweiten Teil des Schlüssel auf einem Baumstumpf in einer Lichtung."
    
        "...dem größten Rätselmeister der Welt stellen.":
            show monc behind burg with dissolve
            show wizzard at monchero
            show knight at monchero
            show held at monchero
            with MoveTransition(1.0)
            $ scastlep += 1
            Lt "In einem einsamen Tempel auf dem höchsten Berg des Landes lebt der Rätselmeister."
            Lt "Er stellt den Helden ein Rätsel das bisher niemand gelöst hat."
            Lt "Ein Rätsel so schwierig, dass nicht mal ich die Antwort weiß."
            Lt "Ehrlich gesagt weiß ich nicht mal das Rätsel."
            Lt "Aber egal. Die klugen Helden schaffen es sogar dieses Rätsel zu lösen und erhalten den zweiten Teil des Schlüssels."
            
    Lt "Super! Bis jetzt haben sie alle Prüfungen bestanden. Aber die letzte Prüfung soll auch die härteste sein denn…"
    
    menu:
        "...äh...sie ist mega schwer!":
            Lt "Ja das hab ich ja grade schon gesagt."
            Lt "Aber was ist denn jetzt die letzte Prüfung?"
            Lt "Eigentlich wollte ich ja dass du dir was ausdenkt."
            Lt "Na gut, wie wärs damit."
            show sandpyramide behind sandauto
            show barbie behind burg with dissolve 
            show wizzard at girlhero
            show knight at girlhero
            show held at girlhero
            with MoveTransition(1.0)
            Lt "Die Helden müssen ein ekliges Mädchen küssen, damit sie ihnen das dritte Schlüsselstück gibt."
            Lt "Dörte ist mega hässlich also braucht es sehr viel Mut sich zu überwinden."
            show held at kissknight
            with MoveTransition(1.0)
            show held at girlhero
            with MoveTransition(1.0)
            Lt "Die Helden trinken sich mit Cola Mut an und bekommen den letzten Teil des Schlüssels."
            
        "… der Troll in der alten Mine hat den letzten Teil des Schlüssels.":
            show cave behind sandauto with dissolve 
            show wizzard at minehero
            show knight at minehero
            show held at minehero
            with MoveTransition(1.0)
            $ scastlep += 1
            Lt "Die Helden werden also in die alte Mine geschickt."
            Lt "Dort wohnt ein fieser Troll der das Schlüsselstück unter seinem Kopfkissen versteckt hat."
            Lt "Zum Glück sind die Helden schlau und können den Troll überlisten und ihm den letzten Teil des Schlüssels klauen."
            
        "“… man braucht einen sehr starken Magen um den schrecklich trockenen Kuchen von Fürst Randolph zu verspeisen.":
            $ scastlep += 2
            Lt "Wow… Cool!"
            show wizzard at cakehero
            show knight at cakehero
            show held at cakehero
            Lt "Die Helden suchen Fürst Randolph auf, weil jeder weiß, dass er einen Teil des Schlüssels besitzt."
            Lt "Randolph will aber ihn aber nicht einfach so hergeben. Er stellt ihnen eine Aufgabe. Wenn sie ein Stück seines unglaublich trockenen Kuchen verspeisen können ohne zu Staub zu zerfallen, dann gibt er ihnen sein Schlüsselstück.."
            show sandkuchen2 
            hide sandkuchen with dissolve
            Lt "Die Helden schaffen es nur zu dritt, in dem sie das Stück genau unter sich aufteilen."
            Lt "Fürst Randolph ist beeindruckt und gibt den letzen Teil des Schlüssels frei."
            
    Lt "Okay, jetzt kommt das große Finale!"
    Lt "Nach diesen schweren Prüfungen erreichen die Helden endlich die [burg]."
    Lt "Noch sind die großen schweren Tore verschlossen. Aber mit den drei Schlüsselstücken öffnen sie sich."
    Lt "Im Innenhof der Festung treffen die Helden nun endlich auf den [enemy]. Ein schwerer Kampf steht bevor. Der [enemy] schafft es fast die Helden zu überwältigen, aber am Ende besiegen sie ihn…"
    show burg behind badboy with dissolve
    show badboy at center
    show wizzard at center
    show knight at center
    show held at center
    with MoveTransition(1.5)
    
    menu:
        "...mit einem Stich ins Herz.":
            $ scastlep += 1
            Lt "Uh…voll brutal!"
            Lt "Einer der Helden schafft es sein Schwert direkt durch das Herz des Bösewichts zu stechen."
            show wizzard at slap
            with MoveTransition(0.5)
            hide badboy with dissolve
            show wizzard at center
            with MoveTransition(1.0)
            Lt "Endlich ist der [enemy] besiegt!"
            
        "…mit einer Ente.":
            Lt "Hä? Wie soll das gehen?"
            show badboy at badduck
            with MoveTransition(1.5)
            pt "Naja, er könnte ja auf der Ente ausrutschen und sich alle Knochen brechen."
            Lt "Echt? Wirklich?"
            Lt "Man man man…"
            show badboy at duckfall
            with MoveTransition(0.5)
            Lt "Der Bösewicht rutscht auf einer Quietscheente aus und stirbt."
            hide badboy with dissolve
            Lt "Endlich ist der [enemy] besiegt"
            
        "…mit einem Drachen den sie beschwören.":
            show sanddragon with dissolve
            $ scastlep += 2
            Lt "Yeah, cool ein Drache!"
            Lt "Ich weiß zwar nicht wo der jetzt plötzlich herkommt… aber egal!"
            Lt "Der Drache verschlingt den Bösewicht in einem Haps!"
            Lt "Endlich ist der [enemy] besiegt!"
            hide badboy with dissolve
            
    Lt "Die Welt ist gerettet und die Bewohner des Landes wieder frei."
    Lt "Die Helden werden überall gefeiert und bekommen goldene Medaillen für ihre Hilfe."
    show preis with dissolve
    Lt "Und wenn sie nicht gestorben sind… und so weiter, und so weiter."
    
    if scastlep > 5:
        Lt "Du hast [scastlep] Punkte gesammelt und bekommst viele Affinitypoints!"
        
    else:
        Lt "Du hast [scastlep] Punkte gesammelt und bekommst wenig Affinitypoints ..."
            
            
            
            
            
    window auto
label scenew2_6:
    "Placeholder W2S6"
label scenew2_7:
    "Placeholder W2S7"
label scenew2_8:
    "Placeholder W2S8"
label scenew2_9:
    "Placeholder W2S9"
    
label scenew2_10:
    scene bg grura2
    show karin talk at slightright
    show octa smug at slightleft
    with fade
    n "Heute ist der Morgenkreis sehr lustig. Wir spielen \"Reise nach Jerusalem\". Das macht Spaß."
    n "Aber Octavia gewinnt dauernd. Gegen die hat echt keiner eine Chance!"
    scene bg flur with dissolve
    n "Mh… ich hab mir noch gar nicht überlegt, was ich danach heut eigentlich machen will..."
    scene bg grura
    show randy vhappy at slightleft
    show louis really at slightright
    with fade
    n "Randy spielt schon wieder mit Louis Oligopoly. Das ist langweilig…"
    n "Vielleicht schau ich lieber mal nach, was die Anderen gerade so machen."
    scene bg flur with dissolve
    n "Octavia ist vorhin direkt nach draußen gerannt und Anja ist da wahrscheinlich auch irgendwo Klettern. Nur wo Evelynn ist weiß ich gerade nicht, aber die malt bestimmt wieder."
    ##############################################################
    menu:
        "Ich sollte mal nach Octavia schauen.":
            stop music fadeout 1.0
            pause 0.75
            play music octatheme fadein 1.0
            scene bg court with dissolve
            n "Was ist denn da draußen los im Innenhof?"
            show osport talk at center
            show lsport n at leftish behind osport
            show asport n at rightish behind osport
            with dissolve
            o "Hey, [name]!"
            n "Octavia steht natürlich wieder im Mittelpunkt. Die erzählt wahrscheinlich immer noch, wie oft sie vorhin schon wieder gewonnen hat."
            p "Was macht ihr alle hier?"
            show osport vhappy
            o "Wir machen ein Wettrennen und du machst mit!"
            
            menu:
                "Okay.":
                    "Na gut… Ich hab eh nichts zu tun."
                    label runokay:
                        show asport behind osport
                        show osport happy
                        o "Bereite dich schon mal auf deine Niederlage vor! Ich gehe regelmäßig mit meinem Papa joggen und da machen wir auch immer Sprintübungen."
                        show osport behind asport
                        show asport talk
                        a "Ich geh lieber und kletter auf Bäume. Einmal hab ich da sogar ein Eichhörnchen gesehen. Aber das ist dann ganz schnell wieder-"
                        show asport behind osport
                        o "Und genau deshalb habt ihr überhaupt keine Chance gegen mich"
                        show osport behind asport
                        a "Ist doch eh egal. Solange es Spaß macht."
                        show asport mad behind osport
                        show osport mad
                        o "Ist es eben nicht! Es ist nicht egal, ob man ein Gewinner oder ein Verlierer ist!"
                        n "Nicht das schon wieder..."
                    
                "Moment mal...":
                    p "Gar nicht! Nur weil ich jetzt raus gekommen bin, heißt das noch lange nicht, dass ich alles mache, was du sagst."
                    show osport mad
                    o "Sei kein Lappen! Sogar Randy und Louis machen später auch mit."
                    show osport behind asport
                    show asport happy
                    a "Ey, ich auch!"
                    show asport mad behind osport
                    o "Jaa, und die da auch."
                    n "Nicht das schon wieder..."
                    o "Aber du musst auch nicht mitmachen. Ist mir sowieso pupsegal. Ich gewinne sowieso!"
                    
                    menu:
                        "Okay.":
                            "Na gut… Ich hab eh nichts zu tun."
                            jump runokay
                            
                        "Nö.":
                            p "Ich mach trotzdem nicht mit. Ich kann euch ja zu schauen."
                            o "Kommt gar nicht in die Tüte! Ich brauch doch einen richtigen Mitstreiter. Die da zählt nicht!"
                            show osport behind asport
                            a "Ey! Das hab ich voll gehört!"
                            p "Na gut, ich mach mit!"
                            n "...aber nur damit ihr aufhört zu zanken."
                            jump runokay
            
            show osport behind asport
            show asport n
            a "Jetzt sag doch auch mal was!"
            menu:
                "Spaß ist wichtiger.":
                    $ raceoutcome = "loss"
                    show osport behind asport
                    show asport happy
                    a "Siehste! Ich hab Recht!"
                    show asport behind osport
                    show osport mad
                    o "Pff, der sagt das doch nur, weil er selber ein Verlierer ist."
                    show osport behind asport
                    show asport talk
                    a "Aber ich hab Recht!"
                    
                    
                "Gewinnen ist alles!":
                    $ raceoutcome = "win"
                    show asport behind osport
                    show osport mad
                    o "Siehste!"
                    show osport behind asport
                    show asport mad
                    a "Selber, siehste!"
                    
                    
            p"Wann geht das Rennen denn los?"
            show asport behind osport
            show osport talk
            o "Dann, wenn ich es sage, also jetzt!"
            
            scene bg rennenstart with dissolve
            n "Es machen noch vier Andere mit. Evelynn nicht, die darf ja nicht mit raus."
            show osport happy at center with moveinleft
            n "Ganz vorne an der Startlinie natürlich Octavia, überheblich wie immer."
            hide osport with moveoutright
            show randy happy at center with moveinleft
            n "Dann kommt auch Randy. Der sieht irgendwie aus wie immer. Der ist glaub ich auch nicht soo schnell im Laufen."
            hide randy with moveoutright
            show lsport laugh at center with moveinleft
            n "Daneben steht Louis. Das ist das erste Mal, dass ich ihn ohne seine Lieblingsjacke sehe. Aber die Sonnenbrille hat er natürlich trotzdem auf."
            hide lsport with moveoutright
            show asport happy at center with moveinleft
            n "Und dann hockt Anja da. Die guckt sich aber lieber grad einen Marienkäfer an. Ich glaub, die macht wirklich nur aus Spaß mit."
            hide asport with moveoutright
            show karin vhappy at center with moveinleft
            n "Und Karin ist wohl der Schiedsrichter."
            k "Auf die Plätze…."
            scene bg run
            show arun at arun1
            show prun at prun1
            show lrun at lrun1
            show rrun at rrun1
            show orun at orun1
            with fade
            k "...Fertig…"
            k "Looos!"
            show arun at arun2
            show prun at prun2
            show lrun at lrun2
            show rrun at rrun2
            show orun at orun2
            with MoveTransition(2.5)
            n "Huch, was macht Anja denn da?"
            show arun at arun3
            show prun at prun3
            show lrun at lrun3
            show rrun at rrun3
            show orun at orun3
            with MoveTransition(1.5)
            show asport happy at left with dissolve
            a "Guck mal da! Die Katze!"
            show osport mad at right with dissolve
            o "Ey, keiner streikt während meinem Wettrennen!"
            hide asport
            hide osport
            with dissolve
            show arun at arun4
            show prun at prun4
            show lrun at lrun4
            show rrun at rrun4
            show orun at orun4
            with MoveTransition(1.5)
            show asport happy at left with dissolve
            a "Aber die Katze!"
            scene bg rennen with dissolve
            $ renpy.pause ()
            scene bg run
            show arun at arun4
            show prun at prun4
            show lrun at lrun4
            show rrun at rrun4
            show orun at orun4
            with fade
            show osport mad at right with dissolve
            o "Verlierer!"
            o "Aus dem Weg Randy!"
            show randy shock at rightish behind osport with dissolve
            r "Hey! HEY! Was soll das?!"
            hide osport
            hide randy
            with dissolve
            show prun at prun5
            show lrun at lrun5
            show rrun at rrun5
            show orun at orun5
            with MoveTransition(1.5)
            show prun at prun6
            show lrun at lrun6
            show rrun at rrun6
            show orun at orun6
            with MoveTransition(1)
            n "Puuh, fast geschafft!"
            
            if raceoutcome == "win":
                show prun at prun7a
                show lrun at lrun7a
                show rrun at rrun7a
                show orun at orun7a
                with MoveTransition(1.5)
                k "Und der Gewinner ist ..."
                scene bg rennenende
                show karin vhappy at center
                with fade
                k "[name]!"
                n "Ha! Das war aber wirklich knapp am Ende. Octavia ist echt schnell!"
                show karin at rightish with move
                show osport mad at leftish with moveinleft
                o "Eigentlich wär ich ja schneller gewesen, aber mein Schnürsenkel war nicht ganz zu."
                show asport talk at left behind osport with moveinleft
                a "Du willst doch bloß nicht zugeben, dass du mal was nicht kannst."
                show karin shock
                o "Gar nicht wahr! Nächste Woche gibt es eine Revanche und dann werden wir es ja sehen!"
                n "Octavia ist echt ganz schön wütend."
                
                
            else:
                show prun at prun7b
                show lrun at lrun7b
                show rrun at rrun7b
                show orun at orun7b
                with MoveTransition(1.5)                
                k "Und der Gewinner ist ..."
                scene bg rennenende
                show karin vhappy at slightright
                with fade
                show karin at slightright with move
                show osport mad at slightleft with moveinleft
                k "Octavia!"
                n "Wieso guckt die mich denn so komisch an? Ist sie gar nicht froh, gewonnen zu haben?"
                show karin shock
                o "Ich nehme den Preis nicht an! Ich gehöre nicht in die Reihe der Preisgekrönten, wenn gewisse Personen..." 
                n "Jetzt guckt sie aber wirklich mich an!"
                o"... das Wettrennen nicht ernst nehmen und mich absichtlich gewinnen lassen!"
                n "Häh? Wen meint die denn damit?"
                
            hide karin
            hide asport
            with dissolve
            show osport at center with move
            n "Und jetzt guckt sie mich schon wieder so böse an, dreht sich dann einfach um und geht."
            hide osport with moveoutright
            show asport n at center with dissolve
            a "Wollen wir wieder klettern gehen?"
            scene bg court
            show anja happyb at right
            with fade
            p "Okay."
            show mum n at left with moveinleft
            n "Oh da ist ja auch schon wieder Mama."
            show mum talk
            m "Na, Püpschen, wie war dein Tag so?"
            show mum n
            p "Ich hab Wettrennen gespielt! Jetzt hab ich Hunger… machen wir Pfannkuchen?"
            show mum mad
            m "Die hatten wir doch erst letzte Woche!"
            p "Eben! Das ist schon wieder eine ganze Ewigkeit her!"
            show mum happy
            m "Na gut. Aber nur, wenn du sie diesmal selber brätst."
            show pancakes
            n "Einmal hab ich schon einen Pfannkuchen ganz alleine gewendet. Aber ich brauch auf jeden Fall noch Übung. Irgendwann werde ich ein Pfannkuchen-Wende-Profikoch, dann kann ich sie mir jeden Tag selber machen!"
            jump pnp1done
            
                
                
        "Ich glaub ich geh mal zu Anja.":
            n "Heute ist es echt schön warm draußen!"
            n "Und natürlich hängt Anja wieder im Baum. Wie so einer dieser orangenen Affen. Die hab ich mal im Zoo gesehen."
            a "[name]! Draußen ist es doch echt am coolsten, oder?"
            a "Außerdem sagt meine Mama immer, dass frische Luft gesund ist. Nur die Luft auf dem Land soll noch besser sein. Meine Oma und mein Opa zum Beispiel wohnen auf dem Land. Die haben einen ganz eigenen Bauernhof!"
            
            menu:
                "Das ist ja echt cool!":
                    p "Ich fin-"
                
                "Ich finde es in der Stadt besser als auf dem Land.":
                    p "Ich fin-"
            
            a "Aber die Luft finde ich da eigentlich nicht so toll. Vor allem im Schweinestall stinkt es immer voll. Aber das Stroh riecht gut!"
            p "Das ist natürlich-"
            a "Meine Oma und mein Opa haben aber auch ganz viele anderen Tiere. Mit denen darf ich auch immer spielen. Aber manchmal ist es alleine trotzdem..."
            n "Ich finde es immer noch lustig, wie Anja ohne Pause reden kann. Mama würde sagen, sie labert wie ein Wasserfall. Auch wenn Wasserfälle doch eigentlich gar nich reden können."
            n "Manchmal sagen Erwachsene schon echt komische Sachen..."
            n "Oh... Anja guckt mich plötzlich so komisch an."
            p "Was hast du gesagt?"
            a "Na, ob du mal mitkommen möchtest? Auf den Bauernhof? Dann kann ich dir unsere Hühnerbabies zeigen, die sind erst zwei Wochen alt und voll flauschig. Und eine Katze haben wir auch! Mama kann die bestimmt heut mitnehmen!"
            p "Äh...ich-"
            a "Meine Oma und mein Opa wohnen auch schon länger hier als wir. Wir sind deswegen dann auch hierher gezogen, damit wir sie ganz oft besuchen können. Und meine Oma backt dann immer Kirschkuchen mit Sahne."
            
            menu:
                "Lecker! Kirschkuchen!":
                    p "Das klingt-"
                    
                "Nichts schmeckt besser als Mamas Kekse!":
                    p "Das klingt-"
                    
            a "Aber die Tiere sind trotzdem das Coolste! Ich will später auch mal irgendwas mit ganz viel Tieren machen. Aber nicht Bauer."
            a "Lieber Tierarzt oder so. Dann kann ich den ganzen Tieren helfen und dann werden die alle meine Freunde. Aber niemand wird ein besserer Freund als unsere Kuh Elsa. Die ist die Allerbesteste!"
            a "Was ist denn- Komm auch hoch! Das musst du sehen! Schnell!"
            menu:
                "Ich kann da nicht hochklettern.":
                    a "Jetzt komm schon! Du verpasst es!"
                
                "Ich beeil mich.":
                    a "Jetzt komm schon! Du verpasst es!"
                    
            n "Was macht die denn für einen Wirbel? Die tut ja fast schon so, als wäre da oben ein Alien"
            a "Schneller!"
            p "Jaa doch..."
            n "Wie war das nochmal? Erst hier hoch und dann..."
            n "Uff… das war knapp."
            a "Siehst du das? Da oben? Die alte Greiterhex!"
            p "Wo? Meinst du da am Fenster? Da dürfen wir doch eigentlich gar nicht hochgehen. Ich weiß nich ob wir-"
            a "Du kannst ja auch gerne wieder runterklettern, du Spielverderber! Aber ich sag dir, mit der stimmt was nicht!"
            
            menu:
                "Oben bleiben":
                    n "Der Schatten hinter dem Vorhang sieht wirklich aus wie der von Heidenau. Nur irgendwie gruseliger… Das ist echt unheimlich."
                    p "Was macht die denn da?"
                    a "Keine Ahnung! Aber die läuft da schon die ganze Zeit im Kreis und siehst du da den Rauch aus dem Fenster kommen? Die kocht da jetzt bestimmt irgendeinen Zaubertrank!"
                    n "Das vielleicht nicht unbedingt, aber auf jeden Fall ist das komisch. Und da kommen auch ganz komische Geräusche aus dem Zimmer."
                    n " Das klingt fast so, als würde jemand einer Eule am Schwanz ziehen. Und dann ist da noch irgendein seltsames Musik-Dingsbums oder so… so was ganz tiefes. Und die Bewegungen der Schatten werden auch immer komischer."
                    a "Die läuft rum, als wäre sie von einem Dämon besessen, wie in diesen Filmen!"
                    a "Achtung, sie kommt wieder zum Fenster!"
                    n "Anja springt schnell runter vom Baum und eh ich mich versehe ist sie um den nächsten Busch geflitzt."
                    n "Plötzlich starrt mich Heidenau direkt an. Ihre Augen leuchten schon fast rot im dunklen Zimmer."
                    h "Das ist doch… [name]! Was machen sie da oben auf dem Baum?! Sofort runter da! Und wo ist denn schon wieder diese unzuverlässige..."
                    n "Heidenau schließt das Fenster wieder. Ich kletter auch lieber schnell runter. Und dann versteck ich mich mit bei Anja, bevor ich noch mehr Ärger bekomme."
                    
                "Runter klettern":
                    p "Lass uns was anderes Spielen. Das ist doof!"
                    a "Ist ja schon gut, aber ich sag‘s dir! Irgendwann wird sie dich fressen und dann bist du froh, wenn du mich hast!"
                    p "Das werden wir dann sehen!"
                    n "Anja kommt jetzt auch runter und schaut mich kurz fragend an. Ich hab mir noch gar nichts überlegt, was wir stattdessen machen können..."
                    
            p "Lass uns doch lieber schnell wippen gehen."
            n "Die Schlangenwippe ist echt lustig. Aber irgendwie ist Anja nicht bei der Sache."
            a "Weißt du, das da oben war schon echt seltsam. Und meine Mama sagt ja auch immer, dass Heidenau eine Greiterhex ist. Meinst du, die ist wirklich eine echte Hexe? Mit Besen und Allem?"
            
            menu:
                "Ja, das glaube ich auch!":
                    a "Wir sollten sie auf jeden Fall weiter beobachten!"
                    
                "Hexen gibt es doch nicht in echt!":
                    a "Mmh… ich denke es gibt viel mehr als Erwachsene immer sagen. Auch Dinge wie Geister, die man vielleicht sogar gar nicht sehen kann. Und die klauen dann immer die Socken aus der Maschine!"
                    

            m "[name]! Na, hattest du einen schönen Vormittag?"
            n "Oh...schon wieder vorbei? Das ging ja schnell. Aber von Anjas Verdacht erzähl ich Mama lieber nichts. Die lacht mich sonst nur aus."
            
            menu:
                "Nichts sagen.":
                    m "Na, und freust du dich schon auf morgen? Da ist doch euer Wandertag!"
                    p "Oh jaa! Das wird bestimmt lustig!"
                    p "Gibt‘s heut eigentlich wieder Pfannkuchen?"
                    m "Die hatten wir doch erst letzte Woche!"
                    p "Eben! Das ist schon wieder eine ganze Ewigkeit her!"
                    m "Na gut. Aber nur, wenn du sie diesmal selber brätst."
                    n "Einmal hab ich schon einen Pfannkuchen ganz alleine gewendet. Aber ich brauch auf jeden Fall noch Übung. Irgendwann werde ich ein Pfannkuchen-Wende-Profikoch, dann kann ich sie mir jeden Tag selber machen!"
                    jump pnp1done
                    
                "Mama fragen, ob ich mit auf den Bauernhof darf.":
                    m "Heute noch? Das muss ich dann aber erst mal mit Anjas Eltern besprechen, ob das denn wirklich in Ordnung ist."
                    a "Meine Oma hat gesagt, ich und meine Freunde sind immer willkommen."
                    p "Bitteee!"
                    m "Ist ja schon gut. Aber ich würde trotzdem gerne mit Anjas Eltern sprechen."
                    n "Erwachsene… immer wollen die nur Reden..."
                    n "Aber dann darf ich wirklich auf den Bauernhof! Und Anjas Oma und Opa sind echt nett."
                    n "Und Anja ist total aufgeregt und zeigt mir den ganzen Bauernhof. Elsa ist wirklich eine tolle Kuh! Und die Küken sind auch niedlich."
                    n "Sogar einen Hahn haben sie, aber der ist ziemlich eingebildet und stolziert immer über den Hof, wie diese Frauen in hohen Schuhen im Fernsehen."
                    a "Und hier, das Heulager, das ist mein Lieblingsort. Da spiele ich immer verstecken. Nur der Hahn stört manchmal. Der krächzt dann Ewigkeiten als würde er bei einem Gesangswettbewerb mitmachen."
                    p "Dann ist er ja fast so schlimm wie du!"
                    a "Na warte! Das wirst du noch bereuen!"
                    n "Anja schnappt sich jetzt doch tatsächlich ein Büschel Stroh und stopft es mir hinten ins T-Shirt rein."
                    p "Ahhh, unfair! Du hattest Vorsprung!"
                    n "Schnell schnappe ich mir auch ein bisschen Stroh und werfe es in Anjas Richtung."
                    n "Fast alles davon bleibt in Anjas Haaren hängen. Sie sieht fast so aus, wie ein Spaghettimonster."
                    a "Ey, ich kann gar nicht mehr sehen. Ich bin bliiind!"
                    n "Ich glaub Anja kann wirklich nichts mehr sehen. So langsam wankt sie Richtung Treppe. Aber sie ist auch schon wieder ordentlich mit Heu bewaffnet."
                    
                    menu:
                        "Anja umlenken.":
                            p "Vorsicht, da ist eine-"
                            a "Raaaaacheeee!"
                            p "Bah, voll ins Gesicht!"
                            n "Stroh schmeckt echt nicht gut."
                            n "Wie Tiere das nur den ganzen Tag essen können?"
                            a "Ahahaa...wie du aussiehst!"
                            p "Du siehst nicht besser aus!"
                            a "Ich bin ja auch eine Hexe, wie die Heidenau! Die sollen auch nicht gut aussehen!"
                            p "Da sieht Heidenau aber noch wesentlich besser aus!"
                            a "Pass auf, gleich fress ich dich! Hexen lieben Kinder zum Nachtisch!"
                            n "Ich glaub Anja mag Hexen. In letzter Zeit redet sie echt oft darüber. Aber das Spielen mit ihr macht trotzdem sehr viel Spaß!"
                            jump pnp1done
                            
                        "Dem Heu ausweichen.":
                            p "Ha, nicht erwischt!"
                            a "Irgendwann er-WOAH!"
                            n "Ohjeh! Jetzt fällt Anja doch noch die Stufe runter! Zum Glück ist ja alles gut mit Heu abgepolstert."
                            p "Hast du dir weh getan?"
                            a "Du Blödian! Hättest du mir nicht was sagen können?! Du weißt genau, dass ich nix sehe!"
                            p "Tut mir Lei-"
                            a "Ist das das Danke dafür, dass ich dich eingeladen hab?! Ich hätte auch Randy mitnehmen können, der ist sowieso viel coolerer als du! Und der hätte mich bestimmt nicht verraten!"
                            p "Tut mir wirkl-"
                            a "Mit dir spiel ich nicht mehr! Und das Stroh ist auch voll doof in den Haaren. Das pikst voll!"
                            n "Wieso muss die immer gleich so sauer sein? Es tut mir doch leid, aber ich kann mich ja nicht mal entschuldigen, wenn die soviel redet!"
                            n "Und jetzt steht die auch noch einfach auf und geht. Na super! So hab ich mir das ja nicht vorgestellt..."
                            jump pnp1done
            
                            
        "Ich schau lieber mal, wo Evelynn ist.":
             n "Oh, Evelynn ist doch nicht am Maltisch. Komisch!"
             p "Karin! Hast du die Evelynn gesehen?"
             k "Ich glaub, die war zuletzt vorne in der Kuschelecke!"
             p "Oh danke!"
             n "Da ist sie ja wirklich! Warum ist sie denn so aufgeregt?"
             e "[name]!"
             n "Jetzt springt sie sogar auf. So fröhlich hab ich sie noch nie gesehen."
             p "Hi!"
             p "Was machst du denn hier?"
             e "Mama und Papa haben mir heut ausnahmsweise mal erlaubt mein Spielbuch mitzunehmen. Das heißt \"Das blaue Auge\" und ist voll toll! Da kann man sich eigene Geschichten ausdenken!"
             p "Ah… ach so…"
             e "Außerdem hat mein Papa jetzt Urlaub, da sind beide dann Zuhause und dann dürfen auch mal Leute mit zu mir zum Spielen kommen."
             n "Ich war noch nie mit bei Evelynn. Ich frag mich, wie ihr Zimmer aussieht. Bestimmt hat sie ganz viele Zeichnungen rumhängen."
             p "Darf ich auch kommen?"
             e "Klar! Ich wollte dich eh grade fragen. Dann können wir das Buch ausprobieren. Du musst dir nur noch vorher ausdenken, wen du spielen willst."
             p "Hä, was meinst du?"
             e "Na also guck das ist ganz einfach. Erst suchst du dir aus was für ein Wesen du sein willst."
             p "Hm…mal sehen was zur Auswahl steht…"
             $ berry = False
             $ powder = False
             $ pnp1winpoints = 0
             
            
             menu:
                "Zwerg":
                    $ race = "Zwergen"
                    n "Zwergen sind bestimmt am Stärksten!"
                    
                "Elfe":
                    $ race = "Elfen"
                    n "Elfen sehen total cool aus!"
                    
                "Mensch":
                    $ race = "Menschen"
                    n "Ich glaub ich bleibe einfach ein Mensch."
                    
             e "…und dann wählst du deine Rolle. Das ist was du gut kannst."
             n "Was für eine Rolle habe ich?"
            
             menu:
                 "Zauberer":
                     $ role = "Zauberer"
                     n "Niemand besiegt mich, wenn ich zaubern kann!"
                    
                 "Bogenschießer":
                     $ role = "Bogenschießer"
                     n "Ich bin der besteste Pfeilbogenschießer der Welt!"
                
                 "Kämpfer":
                     $ role = "Kämpfer"
                     n "Mit meinem großen Schwert, hau ich alle um!"
                    
             e "Ich hab mir auch schon was ausgedacht. Aber das verrate ich dir noch nicht!"
             p "Wieso nicht? Du weißt doch auch, was ich bin, also sag schon!"
             e "Ätschi-Bätsch! Das wirst du sehen, wenn wir spielen!"
             n "Wenn Evelynn mir nichts verrät dann macht es nur noch spannender."
             e "Also, los geht's!"
             e "Es war einmal, vor langer Zeit..."
             n "Evelynn ist sofort drin im Spiel. Was muss ich eigentlich machen?"
             e "... in einem Land namens Müramoor."
             e "Da lebten zwei Helden, die waren auf der Durchreise durch das Land, auf der Suche nach Abenteuern."
             e "Sie waren gerade gemütlich unterwegs im Wald auf dem Weg in das nächste Dorf, als sie auf dem Weg eine zwieli...zw... eine komische Person mit einem langen Mantel bemerkten."
             e "Da sagte die mutige Bardin zu ihre[r/m] Freund[in] dem:"
             e "Was willst du tun? Das könnte ein Bandit sein. Sollen wir uns verstecken?"
             n "Oh..."
             n "Ich glaub, ich soll jetzt was sagen."
            
             menu:
                 "Äh...worum geht's?":
                     n "Ich glaub, das war falsch. Evelynn rollt mit den Augen."
                     e "\"Dann halt nicht\", sagt die Bardin. Aber lass uns schnell weitergehen, ich hab Hunger."
                    
                 "Ja, das wäre das Beste!":
                     e "Die beiden Helden verstecken sich hinter einem Baum. Leise warten sie da und beobachten die Person."
                     e " \"Vielleicht war es doch nur ein Händler\", sagte die Bardin. \"Aber sicher ist sicher.\" "
                     p "Woran erkennst du das?"
                     e "Sie trägt ganz viele Taschen mit Stoffen drin. Die will sie bestimmt verkaufen."
                     e "Aber sieh nur, hier in dem Strauch neben den Baum sind lauter Beeren! Sollen wir welche mitnehmen?"
                    
                     menu:
                         "Vielleicht sind die giftig...":
                             p "Wir sollten sie lieber hier lassen. Mama sagt, man soll nix aus dem Wald in den Mund stecken."
                             e "Eure Frau Mutter scheint ein schlauer Mensch zu sein."
                             n "Was will Evelynn denn nur damit sagen?"
                             e "Die Helden lassen die Beeren also da."
                            
                         "Okay.":
                             $ berry = True
                             p "Ich hab noch Platz hier in meiner Tasche."
                             e "Beide Helden stecken sich ein paar der Beeren in die Beutel, essen sie aber nicht, weil sie nicht wissen, ob man das darf."
                             e "Dann bemerken sie, dass die komische Person nicht mehr zu sehen ist und kriechen wieder aus dem Gebüsch."    
                            
                         "Wieso mitnehmen und nicht gleich essen?":
                             n "Evelynn schaut mich komisch an."
                             e "Die Bardin sagte ihrem Heldenfreund, dass sie das für keine gute Idee hält."
                             p "Und der Heldenfreund sagt der Bardin, dass er ein Held ist und vor gar nix Angst hat. Schon gar nicht vor Beeren."
                             p "Und ich hab Hunger."
                             e "Der Held hat Bauchschmerzen und kann nicht mehr kämpfen."
                             p "Hö...was?"
                             e "Tja, der Held hätte lieber erstmal der Bardin zuhören sollen."
                             jump pnp1end
                            
                 "Vielleicht sollten wir ihr \"Hallo\" sagen?":
                     e "Du gehst voran!"
                     p "Äh...hallo?!"
                     e "Die Person dreht sich um. Nun könnt ihr sie besser sehen."
                     e "Ihr erkennt, dass sie aussieht, wie ein riesiger Panther. Er trägt viele Taschen mit Tüchern bei sich, die er wahrscheinlich verkaufen will."
                     e "(mit verstellter Stimme)\"Grüß Somonoa, ihr Reisenden. Kann ich euch helfen?\" "
                    
                     menu:
                         "Wir sind Helden auf der Suche nach Abenteuern!":
                             e "Der Händler lachte. \"Somonoa, davon gibt es wirklich schon mehr als genug. Wollt ihr euch nicht noch kurz meine Tücher anschauen?\" "
                             e "\"Das ist sehr nett\", sagte die Bardin.\"Aber wir besitzen momentan kein Geld.\" "
                             e "\"Zu schade! Dann will ich euch nicht länger stören.\" "
                             p "Kann er uns nicht einfach was schenken?"
                             e "\"Der Händler lacht nur und geht weiter."
                            
                         "Wir sind eigentlich nur auf dem Weg ins nächste Dorf.":
                             e "\"Oh...\" Der Händler schaut kurz komisch. \"Dann hab ich vielleicht was, was ihr gebrauchen könntet.\""
                             e "Er kramt in seiner Tasche und zieht anschließend ein Glas mit einem schwarzen Pulver raus."
                             e "\"Vertraut mir, ihr werdet es brauchen!\" "
                             
                             menu:
                                 "Oh...danke!":
                                     $ powder = True
                                     e "\"Aber wir können das gar nicht bezahlen\", sagte die Bardin."
                                     e "\"Keine Sorge!\", sagte der Händler. \"Das ist ein Geschenk. Wir Eeisenden müssen zusammen halten.\" Er lächelte noch kurz komisch, drehte sich um und ging wieder weiter."
                                    
                                 "Nein, danke!":
                                     p "Mama sagt, man nimmt nichts von Fremden an."
                                     e "\"Was mein Freund eigentlich sagen will\", sagte die Bardin,\"ist, dass wir kein Geld haben. Und wir können keine Geschenke annehmen.\""
                                     e "\"Das ist schade\", sagte der Händler, lächelte noch kurz komisch, drehte sich um und ging wieder weiter."
                                    
                         "Wie soll ein Händler Helden helfen?":
                             n "Evelynn schaut mich böse an."
                             e "Der Händler ist beleidigt, dreht sich um und geht ohne auch nur ein Wort zu sagen."
                             e "Die Bardin guckt ihren Freund böse an."
                             e "Das hätte man besser machen können!"
                            
                 "Keine Sorge, mein Fräullein! Ich werde Euch beschützen!":
                     p "Ich bin ein mutiger Krieger und hab vor niemandem Angst! Kein Bandit kann mich besiegen!"
                     n "Irgendwie schaut Evelynn mich komisch an."
                     e "Der Held hat etwas zu laut gesprochen. Die komische Person hat das gehört und ist jetzt beleidigt."
                     e " \"Ihr wollt es mit mir aufnehmen?\", fragte der Panthermensch wütend. \"Ich bin Händler. Ich begegne oft Leuten wie dir und hab Übung im Kämpfen. Du bist keine Gefahr für mich.\""
                     p "Der Held hatte es nicht so gemei-"
                     e "Der Händler zieht sein Schwert, entschlossen seine Sachen vor den beiden Fremden zu schützen."
                     e "\"Also, das darfst du jetzt alleine auslöffeln\", sagte die Bardin zu ihrem Heldenfreund."
                    
                     menu:
                         "Ich greife an!":
                             e "Das wird schwer..."
                             p "Ach ja? Ich nehm einfach mein-"
                             e "Du musst würfeln!"
                             n "Das ist ja ein komischer Würfel...fast schon rund. Und ganz viele Zahlen stehen da drauf."
                             p "Ha! 19! Das ist fast das höchste!"
                             n "Warum schaut sie mich denn so komisch an?"
                             p "Tjaa...das hättste nicht gedacht, was?"
                             e "Der Held stolpert beim Ziehen seiner Waffe über seine eigenen Füße und fällt in eine Sumpfgrube neben dem Weg. Dabei geht auch noch seine Waffe kaputt und er kann nicht mehr kämpfen."  
                             p "Was? Wiesooo?! Das ist unfair!"
                             e "Es ist schlecht Hohe Zahlen zu würfeln."
                             jump pnp1bad
                            
                         "Ich renne weg!":
                             n "Warum schaut sie mich denn so komisch an?"
                             e "Der Held rennt panisch davon. Die Bardin schaut ihm hinterher. \"Man, bist du peinlich...\", sagte sie und ging ihrem Freund dann schnell hinterher."
                            
             e "Die Beiden liefen weiter und sahen bald ein Dorf."
             e "Aber auch das Dorf war komisch. Die Häuser waren alle schwarz und hatten große Löcher."
             e "Die Bardin sah einen Bauer und sprach ihn darauf an."
             e "Er erzählte ihr, dass die Leute hier in letzter Zeit oft Besuch von einem bösen Drachen bekommen, der aus Spaß ihre Häuser verbrennt und all ihr Essen wegisst; Vor allem die leckeren Kuchen, die eigentlich für den Geburtstag des Bürgermeisters gedacht waren."
             e "\"Keine Sorge, mein Freund!\", sagte die Bardin zu ihm. \"Wir werden euch helfen!\" "
             p "Ach ja?"
             e "Wir werden mit ihm reden und mit ihm schimpfen! Dann werdet ihr keine Angst mehr vor ihm haben müssen."
             e "Der Bauer schaut euch dankbar an."
             p "Und wo sollen wir den Drachen finden?"
             e "\"Ganz einfach\", sagte die Bardin. \"Wir folgen einfach den großen Füßabdrücken!\""
             e "Nach gar nicht langer Zeit sahen sie den Drachen. Er lag unter einem Baum und hielt ein Mittagsschlaf, weil er so viel Kuchen gegessen hatte."
             e "Was sollen wir tun?"
             
            
            
             menu:
                 
                 "Lass uns einfach angreifen!":
                     e "Der Held rennt natürlich mal wieder einfach ohne nachzudenken auf den Drachen zu."
                     e "Der wird von dem Gebrüll natürlich wach und ist gar nicht glücklich, dass ihn jemand beim Schlafen stört."
                     e "Er steht auf und funkelt den Helden wütend an."
                     e "Du musst würfeln. Je niedriger, desto besser."
                     n "Okay, das muss doch..."
                     p "8!"
                     e "Glück gehabt!"
                     e "Der Drache will Feuer nach dir spucken, aber spuckt aus Versehen vorbei."
                     e "Du tust ihm aber mit deinem Angriff etwas weh."
                     e "\"Aua!\", sagt der Drache. \"Das ist unfair!\""
                     e "Aber noch ist der Drache nicht besiegt!"
                    
                     if powder = True:
                         $ pnp1winpoints += 1
                         jump pnp1powdered
                        
                     else:
                         jump pnp1gethit
                        
                 "Wir können ihn austricksen!":
                     e "Das ist eine gute Idee! Und wie?"
                     if berry == True:
                         $ pnp1winpoints += 1
                         p "Wir könnten ihm heimlich die Beeren geben, die wir gefunden haben. Vielleicht wird ihm dann schlecht."
                         e "Das können wir probieren."
                         e "Du musst würfeln!"
                         e "Du musst würfeln. Je niedriger, desto besser."
                         n "Okay, das muss doch..."
                         p "8!"
                         e "Das ist gut!"
                         e "Der Held schafft es dem Drachen die Beeren heimlich ins Maul zu stecken."
                         e "Der Drache wird davon wach, schluckt die Beeren aber trotzdem aus Versehen runter."
                         e "\"Aua!\", sagt der Drache. \"Mein Bauch! Das ist unfair!\""
                         e "Aber noch ist der Drache nicht besiegt!"
                        
                         if powder == True:
                             $ pnp1winpoints +=1
                             jump pnp1powdered
                            
                         else:
                             jump pnp1gethit
                            
                     else:
                         p "Wir könnten uns leise anschleichen! Und dann überraschen wir ihn, mit unserem Angriff!"
                         e "Das ist eine gute Idee!"
                         e "Die Helden schleichen sich an. Ganz langsam, um den Drachen nicht zu wecken."
                         e "Dann holt der Held aus und-"
                         p "..."
                         e "..."
                         e "Du musst würfeln! Je niedriger, desto besser."
                         n "Okay, das muss doch..."
                         p "8!"
                         e "Glück gehabt!"
                         e "Der Drache wacht auf und will Feuer nach dir spucken, aber spuckt aus Versehen vorbei."
                         e "Du tust ihm aber mit deinem Angriff etwas weh."
                         e "\"Aua!\", sagt der Drache. \"Das ist unfair!\""
                         e "Aber noch ist der Drache nicht besiegt!"
                        
                         if powder == True:
                             $ pnp1winpoints +=1
                             jump pnp1powdered
                            
                         else:
                             jump pnp1gethit
                            
label pnp1gethit:
    e "\"Wir müssen schnell nochmal angreifen!\" rief die Bardin. \"Wir haben gar keine andere Wahl!\" "
    e "Du musst würfeln."
    n "Nur einmal noch..."
    p "..."
    e "Eine 15? Oh jeh..."
    e "Der Drache wird langsam wütend und er kratzt dich einmal mit seiner Kralle am Arm."
    if pnp1winpoints == 0:
        jump pnp1lost
        
    elif pnp1winpoints == 1:
        jump pnp1patt
        
    else:
        jump pnp1win
        
label pnp1powdered:
    p "Vielleicht sollte ich mal das komische Pulver ausprobieren. Vielleicht bringt das was."
    e "Das ist eine gute Idee!"
    e "Du holst das Glas raus und schüttest alles aus, so dass sich eine große Wolke bildet in die der Drache reintaumelt."
    e "Ein bisschen was von dem Pulver weht auch zu dir und es fällt dir auf, dass es Pfeffer ist. Du musst sofort niesen."
    e "Und auch dem Drachen geht es so. Er niest und niest. Ganz knapp nur kannst du seinen Feuerstrahlen ausweichen."
    e "Aber als er endlich fertig war, konnte er gar kein Feuer mehr benutzen, weil er sich erst mal wieder erholen musste."
    if pnp1winpoints == 0:
        jump pnp1lost
        
    elif pnp1winpoints == 1:
        jump pnp1patt
        
    else:
        jump pnp1win
    
    
label pnp1win:
    e "Der Drache schnaubt vor Wut, aber er sieht ein, dass ihr besser seid."
    e "Er schnappt sich noch schnell einen Apfel vom Baum und läuft dann schnell nach Hause zu seiner Höhle, wo seine Mami auf ihn wartet."
    e "Die Dorfbewohner haben alles gesehen und feiern ihre beiden Helden."
    e "Dafür veranstalten sie ein großes Fest mit viel Musik."
    e "Aber die Helden können sich nicht lange ausruhen, denn direkt dort auf dem Fest, kommt plötzlich-"
    jump pnp1good
    
label pnp1patt:
    e "\"Das hat keinen Sinn!\" rief die Bardin. \"Er ist einfach zu mächtig.\""
    p "Och manno."
    e "Du hast dir Mühe gegeben, aber wenn du ihn besiegen willst, sollten wir noch etwas trainieren."
    e "Wir sollten uns besser erstmal verstecken und später wieder kommen."
    p "Okay."
    e "Aber das ist nicht schlimm. Bis dahin gibt es auch noch andere Abenteuer. Im anderen Dorf gibt es zum Beispiel-"
    jump pnp1good
    
label pnp1lost:
    e "Du hast alles versucht, aber der Drache ist einfach zu stark."
    e "Und jetzt ist er erst recht wütend."
    e "Er packt dich am Kragen und schnippst dich bis rüber ins Nachbardorf, wo du in einem Misthaufen landest."
    e "Die Leute da haben alles gesehen und lachen dich aus."
    p "Ich glaub, mehr muss ich gar nicht wissen..."
    jump pnp1bad
    
label pnp1good:
    m "Ach, da bist du!"
    p "Och nö, kann ich nicht noch weiter spielen? Nur noch ein ganz klein bisschen?"
    m "Wir haben es leider etwas eilig. Wir müssen noch einkaufen gehen. Aber du kannst doch morgen weiterspielen. Das läuft dir schon nicht weg."
    p "Okaaaay..."
    n "Immer dann, wenn es am lustigsten wird, muss man aufhören. Das ist unfair. Wenn ich erst einmal groß bin, hör ich erst dann auf, wenn ich will."
    jump pnp1done
    
label pnp1bad:
    n "Evelynn knallt das Buch zu."
    e "Du hast verloren."
    n "Sie sagt das so, wie jemand sagen würde \"Es regnet heute\". Ich bin mir nur nicht sicher, ob sie sauer oder enttäuscht ist."
    p "Können wir nicht noch weiterspielen?"
    e "Nein."
    e "Dafür musst du erst wieder eine neue Figur basteln und darauf hab ich jetzt keine Lust. Ich geh malen."
    n "Was hat die denn auf einmal? Jetzt stampft sie einfach mit dem Buch davon..."
    m "Na, mein Püpschen!"
    m "Wie war der Tag heut so?"
    p "Mhh..."
    m "Das klingt ja sehr begeistert. Freust du dich gar nicht auf den Wandertag?"
    p "Doch."
    n "Nicht so wirklich. Ich mag es nicht, wenn Evelynn auf mich sauer ist."
    jump pnp1done
    
    
    
label pnp1done:
    
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
