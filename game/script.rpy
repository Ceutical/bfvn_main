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
define emum = Character("Evelynns Mama")
define edad = Character("Evelynns Papa")
define omum = Character("Octavias Mama")
define odad = Character("Octavias Papa")
define rmum = Character("Randys Mama")
define rdad = Character("Randys Papa")
define nvln = Character(name=None, kind=nvl)
define kg = Character("Kinder", what_italic=True) #Kindergartengruppe

#define test = Character("Test", window_ypos=0.27) #TESTCHAR



######################################

##### MUSIC CHANNEL DEFINITIONS #####

init python:
    renpy.music.register_channel("music1", mixer=None, loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    renpy.music.register_channel("music2", mixer=None, loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    renpy.music.register_channel("music3", mixer=None, loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    renpy.music.register_channel("sound1", mixer=None, loop=False, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    renpy.music.register_channel("sound2", mixer=None, loop=False, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    renpy.music.register_channel("sound3", mixer=None, loop=False, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    renpy.music.register_channel("sound4", mixer=None, loop=False, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)

##### MUSIC DEFINITIONS #####

define audio.introtheme = "music/soundtracks/introtheme.mp3"
define audio.anjatheme = "music/soundtracks/anjatheme.mp3"
define audio.evetheme = "music/soundtracks/evetheme.mp3"
define audio.octatheme = "music/soundtracks/octatheme.mp3"
define audio.maintheme = "music/soundtracks/maintheme.mp3"
define audio.poketheme = "music/soundtracks/Pokemon_Minigame.ogg"
define audio.dueltheme = "music/soundtracks/Dramatische_Duellmusik.ogg"
define audio.bosstheme1 = "music/soundtracks/Fantasy_Boss1.ogg"
define audio.bosstheme2 = "music/soundtracks/Fantasy_Boss2.ogg"
define audio.fantheme1 = "music/soundtracks/Fantasy1.ogg"
define audio.fantheme2 = "music/soundtracks/Fantasy2.ogg"
define audio.happytheme1 = "music/soundtracks/Happy_Theme1.ogg"
define audio.happytheme2 = "music/soundtracks/Happy_Theme2.ogg"
define audio.playtheme1 = "music/soundtracks/Kinder_Beim_Spielen1.ogg"
define audio.playtheme2 = "music/soundtracks/Kinder_Beim_Spielen2.ogg"
define audio.opartytheme = "music/soundtracks/Kinder_Party_Theme1.ogg"
define audio.apartytheme = "music/soundtracks/Kinder_Party_Theme2.ogg"
define audio.epartytheme = "music/soundtracks/Kinder_Party_Theme3.ogg"

#JUMPER
##### SFX DEFINITIONS #####

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
define audio.whoosh3 = "music/sfx/whoosh3.ogg"
define audio.Chicken = "music/sfx/Hahnwecker.ogg"
define audio.antiarmor = "music/sfx/Schutzausrüstung_ausziehen.ogg"
define audio.bike = "music/sfx/Fahrrad.ogg"
define audio.chain = "music/sfx/Fahrrad_alteKette.ogg"
define audio.bikebreak = "music/sfx/Fahrradbremse.ogg"
define audio.scream = "music/sfx/Kinderschrei3.ogg"
define audio.scream2 = "music/sfx/Kinderschrei1.ogg"
define audio.whoosh1 = "music/sfx/Whoosh1.ogg"
define audio.boing = "music/sfx/Boing.ogg"
define audio.pokin = "music/sfx/PKMN-Einwurf.ogg"
define audio.pokout = "music/sfx/PKMN-Tot.ogg"
define audio.purr = "music/sfx/Katzenschnurren.ogg"
define audio.rain = "music/sfx/Regen.ogg"


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
transform topleft:
    xalign 0.0
    yalign 0.0    
transform topishleft:
    xalign 0.0
    yalign 0.5
transform rotation:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 10
transform rotationreset:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
transform flight:
    xalign .5
    yalign .4
transform flightright:
    xalign .8
    yalign .4
    
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
    stop music
    play music1 introtheme
    python:
        if not persistent.set_volumes:
            persistent.set_volumes = True
            _preferences.volumes['music'] *= .80 
        renpy.music.set_volume(volume=0.5, channel='music1')
    
    ##### OTHER DEFINITIONS #####
    $ seekwin = True
    $ seekloss = True
    $ grura = True
    $ flur = True
    $ court = True
    $ kz = True
    $ food = True
    $ catch = 0
    $ seekattempts = 0
    $ climber = False
    $ tookrandy = False
    $ boomstickpoints = 0
    $ dynamik = False
    $ trade = False
    $ tip = False
    $ farbflug = False
    $ chaos = False
    $ octaannoyed = 0
    $ pnpstr = 0
    $ pnpdex = 0
    $ pnpint = 0
    
    
    init:
        image odance:
            "images/Characters/octavia/omusic clap.png"
            pause 0.20
            "images/Characters/octavia/omusic pause.png"
            pause 0.17
            "images/Characters/octavia/octa music.png"
            pause 0.17
            repeat
            
        image kdance:
            "images/Characters/karin/kmusic left.png"
            pause 0.269
            "images/Characters/karin/kmusic happy.png"
            pause 0.269
            "images/Characters/karin/kmusic right.png"
            pause 0.269
            "images/Characters/karin/kmusic happy.png"
            pause 0.269
            repeat
            
        image oadance:
            "images/Characters/octavia/oparty vhappy.png"
            xalign 1.0 yalign 1.0
            linear 1.0 xalign 0.5
            "images/Characters/octavia/oparty vhappy.png"
            xalign 0.5 yalign 1.0
            linear 1.0 xalign 1.0
            repeat
            
        image aodance:
            "images/Characters/anja/AParty/aparty jabber.png"
            xalign 0.5 yalign 1.0
            linear 1.0 xalign 1.0
            "images/Characters/anja/AParty/aparty jabber.png"
            xalign 1.0 yalign 1.0
            linear 1.0 xalign 0.5
            repeat
            
        image raindrops:
            "images/Displayables/regen/drop1.png"
            pause 0.1
            "images/Displayables/regen/drop2.png"
            pause 0.1
            "images/Displayables/regen/drop3.png"
            pause 0.1
            repeat
            
        image rainsplash:
            "images/Displayables/regen/splash1.png"
            pause 0.1
            "images/Displayables/regen/splash2.png"
            pause 0.1
            "images/Displayables/regen/splash3.png"
            pause 0.1
            repeat
            
            

    ##### AFFINITY SYSTEM INITIATE #####
    $ octa_points = 0
    $ eve_points = 0
    $ anja_points = 0
    $ mapa = "Bumpy" #Marschpartner
    
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
            suf3 = ""
            suf4 = ""
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
            pre = "meine"
            suf4 = "e"
            ddd = "die"

    ##### Szene 2 CHILD #####
    menu:
        "Was spielen?"
        "Anjas Ende.":
            stop music1
            jump anjas_ending

        "Eves Ende.":
            stop music1
            jump eves_ending
            
        "Normal.":
            jump childlike
label childlike:
    scene mnd with fade
    $ renpy.pause(0.6, hard = True)
    scene bg black with fade
    "???" "Hey Püpschen! Aufwachen! Du willst doch nicht zu spät kommen!"
    n "Oh man. Ich mag Montage nicht. Ich bin noch so müde."
    n "Aber Moment! Heute geht's in den neuen Kindergarten."
    m "Raus aus den Federn jetzt. Es gibt Frühstück!"
    play sound decke
    show bg bedroom2 with fade
    n "Nein… nicht die warme Decke…"
    n "Mann, muss alles so hell sein…"
    show bg bedroom with dissolve
    show mum talk with moveinright
    m "Guten Morgen mein kleiner Spatz!"
    p "Morgen Mama ..."
    p "Ich will aber noch nicht aufstehen!"
    m "Ach jetzt stell dich nicht so an. Na komm. Wir ziehen dich gleich an, jetzt gibt's erstmal Essen."
    m "Ich hab Pfannenkuchen gemacht! Heute ist doch dein großer Tag!"
    p "Pfannkuchen! Jaa! Mama ich hab dich lieb!"
    scene bg kitchen
    show pancakes
    with dissolve
    n "Am liebsten würde ich jeden Tag Pfannkuchen essen."
    show mum talk
    hide pancakes
    with dissolve
    m "Freust du dich schon deine neuen Freunde kennenzulernen?"
    
    
    menu:
        m "Freust du dich schon deine neuen Freunde kennenzulernen?"
        
        "Jaaaaaa!":
            $ octa_points += 1
            $ eve_points -= 1
            $ anja_points += 1
            $ happytogo = True
            n "Das wird bestimmt super."
            m "Das ist schön. Du kommst bestimmt in eine Gruppe mit ganz tollen anderen Kindern."
     
        "Ja...":
            $ eve_points += 1
            $ happytogo = False
            n "So wirklich Lust hab ich ja nicht."
            m "Ach Spätzchen... Bist du doch noch so traurig, dass du deine alten Freunde nicht mehr siehst?"
            n "Ja, das ist echt blöd."
            m "Du kommst heute bestimmt ein eine Gruppe mit ganz tollen Kindern, wirst schon sehen!"
            n "Wenn sie mir so durch die Haare wuschelt fühle ich mich schon wieder besser."
    
        

    ##### Szene 3 #####
label scene3:
    scene bg street
    show mum talk at center
    with fade
    stop music1 fadeout 2.0
    play music maintheme fadein 3.0
    python:
        renpy.music.set_volume(volume=1.0, delay=1.2, channel='music')
    if happytogo == True:
        n "Ich bin total aufgeregt. Dabei ist das doch nur ein Kindergartentag wie sonst auch.."
        n "Aber irgendwie auch nicht. Vielleicht finde ich da ja neue noch bessere Freunde als in meinem alten Kindergarten. "
        m "Das wird ein ganz toller Tag, glaub mir!"
    else:
        n "Mann, ich will nicht. Muss das sein? Mein alter Kindergarten war doch super. Warum muss ich jetzt hier hin?"
        n "Naja, wenigstens ist Mama da."
        m "Gleich sind wir da. Keine Angst, das wird schon! Du wirst bestimmt viele neue Freunde finden."
        n "Mein alter Kindergarten ist definitiv schöner als das hässliche Haus da."
    scene bg flur
    show heide n at center
    with fade
    play music2 child1
    n "Was für ne gruselige Frau ist da vorne denn?"
    n "Die sieht überhaupt nicht nett aus."
    show ghost with dissolve
    n "Und warum ist die so weiß? Wie ein Geist..."
    hide ghost with dissolve
    show heide talk at center
    h "Ah. Der Neuzugang. Ich bin Frau Heidenau. Wie ist dein Name [pro6]?"
    menu:
        h "Ah. Der Neuzugang. Ich bin Frau Heidenau. Wie ist dein Name [pro6]?"
        "Selbst vorstellen.":
            $ octa_points += 1

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
            scene bg grura
            show karin n at slightleft
            with fade
            show heide mad at slightright with moveinright
            h "Hier Karin. Ein[suf4] Neu[suf2]. Ich muss jetzt weitermachen. Ich erwarte nachher deinen Bericht."
            hide heide with moveoutright
            show karin n at center with move
        
        "Mama hilfesuchend ansehen.":
            $ octa_points -= 1
            $ anja_points += 1

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
            hide heide with moveoutright
            n "Puh, endlich ist diese gruselige Frau weg."
            scene bg grura
            show karin n at center
            with fade

        

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
        k "Das sind deine neuen Freunde! Stell dich uns Allen doch mal vor, wir wissen ja noch gar nicht wie du heißt."
        "Vorstellen.":
            $ octa_points += 1
            $ anja_points += 1

            $ menu_choice3 = "yes"
            p "Hallo, ich bin [name]! Lasst uns Freunde sein!"
            k "Da hört ihr's Kinder. Ich hoffe ihr freundet euch alle mit [name] an!"
            
            
        "Schweigen.":
            $ octa_points -= 1
            $ eve_points += 2
            $ anja_points -= 1

            $ menu_choice3 = "no"
            p "..."
            n "Ich will mich nicht vorstellen. Am Ende versprech’ ich mich noch und die Anderen machen sich über mich lustig."
            m "Ohh, entschuldigen Sie Frau ..."
            k "Einfach Karin reicht."
            m "Ohh, in Ordnung. Entschuldigen Sie Karin, [name] ist noch etwas schüchtern und ..."
            k "Alles gut. Also Kinder, das hier ist [name], ich hoffe ihr alle könnt Freunde werden."
        
        "Stammeln.":
            $ octa_points -= 1
            $ anja_points += 1

            $ menu_choice3 = "meh"
            p "I.. ich.. also ich b-b-bin..."
            k "Du brauchst keine Angst haben."
            k "Komm, sag mir wie du heißt, dann stell ich dich vor."
            p "...[name]..."
            k "Also Kinder, das hier ist [name], ich hoffe ihr alle könnt Freunde werden."
            
            
    
    ##### Szene 4 #####
label scene4:
    play music octatheme fadeout 1.0
    scene bg grura
    show karin talk at slightright
    show mum talk at slightleft
    with fade
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
    hide karin with dissolve
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
    hide eve
    hide louis
    show octa music
    with dissolve
    o "Hallo!"
    o "Ich bin Octavia. Das sind Klanghölzer, weißt du oder?"
    o "Damit kannst du umgehen, oder?"
    menu:
        o "Damit kannst du umgehen, oder?"
        "Ja! Die sind voll lustig!":
            $ boomstickpoints += 1
            o "Find ich auch! Und voll einfach. Ich kann das hier am Besten, sagt meine Mama mir auch immer."
            
        "Ähm, nein ... Nicht wirklich ...":
            o "Was, du kannst das garnicht?"
            o "Die anderen sagen das ist voll schwer. Find ich nicht. Ich bin die Beste damit!"
    
    n "Sie nimmt das aber Ernst. Ist doch nur der Morgenkreis. Kann man da überhaupt die Beste drin sein?"
    o "Und du weißt auch wozu die Klanghölzer gut sind?"
    menu:
        o "Und du weißt auch wozu die Klanghölzer gut sind?"
        
        "Für den Rhythmus!":
            $ boomstickpoints += 1
            p "Na um damit den Rhythmus zu halten, ist doch ganz einfach."
            o "Puh, na dann weißt du ja wenigstens etwas."
        
        "Zum Krach machen!":
            p "Um sie volle Kanne gegeneinander zu hauen! Juhu!"
            o "..."
            o "Schon. Aber mit Gefühl. Im richtigen Takt."
            
    o "Wie willst du überhaupt vernünftig mitmachen?"
    o "Du kennst doch unser Käfergruppenlied noch garnicht."
    o "Am Ende versaust du noch alles ..."
    o "Und dann muss ich, als die Beste natürlich, alles wieder gutmachen!"
    
    menu:
        o "Und dann muss ich, als die Beste natürlich, alles wieder gutmachen!"
        
        "Ich lerne schnell!":
            $ boomstickpoints += 1
            p "Das ist garkein Problem! Ich lerne ganz schnell, sagt Mama immer."
            o "Dann klingt es am Anfang immernoch furchtbar."
            p "Na dann hör ich dir zu und dann mach ich das was du machst."
            o "Willst du mich etwa nachmachen?"
            p "Du hast doch gesagt du bist die Beste!"
            o "Natürlich bin ich die Beste!"
        
        "Wird schon schiefgehen ...":
            p "Ach das klappt schon. Irgendwie."
            o "Wir machen das hier doch nicht zum Spaß."
            p "Aber ich dachte ..."
            o "Streng dich gefälligst an!"
            
    show octa music at leftish with move
    show karin mhappy at rightish with moveinright
    k "Also Kinder, alle bereit?"
    stop music fadeout 2.0
    k "Dann 1 und 2 und 3 und ..."
    hide karin
    hide octa
    show odance at leftish
    show kdance at rightish
    play music happytheme1
    n "Das ist also das Käfergruppenlied?"
    n "Klingt total toll ..."
    n "Und die Klanghölzer machen voll Spaß!"
    n "..."
    n "Ohh, sieht so aus als wären wir gleich fertig..."
    n "Schade..."
    window hide
    $ renpy.pause ()
    window auto
    play music octatheme fadeout 1.5
    if boomstickpoints == 3:
        scene bg grura
        show octa talk at center
        with fade
        $ octa_points += 3
        o "Das hat Spaß gemacht! Aber ich war die Einzige die alles richtig gemacht hat."
        o "Aber ... du warst auch garnicht schlecht!"
        p "Ohh dankesch..."
        show octa smug
        o "Hast ja auch von der Besten gelernt."
        n "Ja genau ... Von der Besten ..."
        
    else:
        scene bg grura
        show octa talk at center
        with fade
        $ octa_points -= 3
        o "Das hat Spaß gemacht! Aber ich war die Einzige die alles richtig gemacht hat."
        if boomstickpoints == 1 or boomstickpoints == 2:
            $ octa_points += 1
            show octa smug
            o "Du hast doch gesagt, du kannst das. Ich war viel, viel besser als du."
            p "Tut mir leid..."
            o "Jetzt ist zu spät. Ich hatte viel mehr von dir erwartet..."
            o "Naja. Nächstes Mal dann."
            
        elif boomstickpoints == 0:
            show octa smug
            o "Du warst nicht gut ... Ich hab zugeschaut, weißt du?"
            p "Aber ich hatte Spaß!"
            show octa mad
            o "Aber du warst nicht gut. Hier geht es nicht um Spaß, hab ich das nicht schonmal gesagt?!"
            p "Ist ja gut ..."
            n "Warum ist die denn so sauer?"
    
    hide octa with moveoutleft
    n "Der Morgenkreis hier ist auf jeden Fall lustiger als der in meinem alten Kindergarten."
    n "Irgendwie geben sich alle zumindest Mühe."
    n "Aber dieses Mädchen steigert sich da echt rein. Sie heißt Octavia, oder? Was ein komischer Name."
    show karin mhappy at center with moveinright
    
    k "Das habt ihr gut gemacht Kinder!"
    k "Aber jetzt ist genug, auf zum Frühstück mit euch. Husch husch, wir haben ja nicht den ganzen Tag Zeit."
    
    ##### Szene 5 #####
label scene5:
    stop sound fadeout 1.0
    play music anjatheme fadeout 1.0
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
    play music evetheme fadeout 1.5
    n "Puh… ein Glück, dass das Gespräch erstmal vorbei ist."
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
            $ eve_points += 2

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
                e "Weißt du denn garnicht was ein Leuchtturm ist?"
                "Nein...":
                    $ eve_points += 1
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
                    $ eve_points -= 2
                    p "Also ich war schonmal mit meinen Eltern bei einem Leuchtturm und der sah ganz anders aus."
                    show eve mad
                    e "War wohl ein blöder Leuchtturm."
                    e "Oder du lügst."
                    show eve draw
                    e "Ich muss jetzt weiter üben."
                    
            
        "Das kann ich aber besser.":
            $ eve_points -= 3
            hide dis leuchtturm
            show eve mad
            with dissolve
            e "Angeber."
            e "Geh weg."
            show eve draw
            jump meantoeve

    
    hide eve with dissolve
    n "Wow… die kann mega toll malen. Ich will das auch können."
    n "Wenn ich öfter mit ihr zusammen male bin ich vielleicht auch irgendwann mal so gut."
label meantoeve:
    hide eve with dissolve
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
    show tue with dissolve
    $ renpy.pause(0.6, hard = True)
    scene bg grura
    play music happytheme2 fadeout 1.0
    play sound child1
    show karin mhappy at center
    with fade
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
        n "Sie malt ... mit ihrem Essen?"
        "Cool!":
            $ eve_points += 1
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
            $ eve_points -= 2
            p "Aber warum denn mit deinem Essen... Das ist doch ekelig."
            show eve foodmad
            e "Gar nicht wahr. Das ist schön, guck doch mal."
            p "Jetzt hast du Alles an den Fingern kleben."
            p "Malen macht man mit Stiften, nicht mit Essen."
            show eve foodplay
            e "Mir macht das aber Spaß."
            p "Aber das kann man doch nicht mehr essen!"
            show eve foodmad
            e "Darum geht es doch auch gar nicht!"
            
        "WAS tust du?!":
            $ eve_points -= 1
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
            $ eve_points += 1
            window hide
            scene cg foodplay with dissolve
            play sound foodplay
            $ renpy.pause ()
            window auto
            e "Nicht schlecht. Man kann fast erkennen, dass du ein Haus bauen wolltest."
            p "Das soll doch aber eine Burg sein!"
            e "Ohh! Ja stimmt, wenn man es weiß. Du musst aber wirklich noch üben."
            
        "Nein, sicher nicht.":
            $ eve_points -= 1
            window hide
            scene cg food with dissolve
            $ renpy.pause ()
            window auto
            p "Nein ... nein ich esse lieber ganz normal. Ich will mich nicht schmutzig machen."
            e "Dann nicht ..."

stop sound fadeout 1.0
    ##### TAG 2 ENDE #####
    
    ##### TAG 3 BEGINN #####
    ##### Szene 9 #####
label scene9:
    play music maintheme fadeout 1.0
    scene bg black with fade
    show wed with dissolve
    $ renpy.pause(0.6, hard = True)
    scene bg bedroom with fade
    play sound Chicken loop
    "???" "{b}KICKERIKI! KICKERIKI! KICKERIKI!{/b}"
    p "Waaah!"
    p "Hilfe! Was ist das?! Mama!!!"
    "???" "{b}KICKERIKI! KICKERIKI! KI...{/b}"
    stop sound
    show mum talk at center with moveinright
    m "Guten Morgen Püpschen!"
    m "Ich hab dir was mitgebracht!"
    show mum at slightleft with move
    show dis hahn at chicken with dissolve
    p "Eine Ente!"
    m "Fast! Aber mit dem hier kommst du bestimmt leichter aus den Federn."
    scene bg street with dissolve
    n "Dieser Hahn wie Mama die Ente nennt, ist echt nervig. Wie soll mir das denn beim Aufstehen helfen?"
    n "Ich glaube Mama will sich nur über mich lustig machen."
    n "Aber, eigentlich sieht die Ente ja ganz lustig aus. Naja, auf zum Morgenkreis."
    scene bg grura
    show karin talk at slightright
    show dis mikro at mic
    with fade
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
    play music happytheme2 fadeout 1.0
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
    play music anjatheme fadeout 1.0
    scene bg court with fade    
    n "Eigentlich will ich mich nur hinlegen und etwas in der Sonne dösen. Da auf der Wiese siehts gut aus."
    n "Wer schreit denn da?"
    n "Ich guck besser mal nach. Nicht das ich was verpasse."
    n "Sitzt da Anja im Baum? Wer ist den der Junge da?"
    show anja vmadb2 at topleft with dissolve
    a "Is doch a völligs Gschmarre wos du dou verzüllst."
    show randy vmad at right with dissolve
    "???" "Gibt doch viel Besseres, was man damit machen kann. Also wieso Eis!?"
    
    menu:
        
        "Stumm abwarten.":
            $ daze = False
            show randy mad
            "???" "Ist doch einfach Geschmackssache und ich will das Eis essen, dass ich essen will."
            show anja madb2
            a "Aber das schmeckt doch nur wenn noch was dazugegeben wird."
            "???" "Es schmeckt immer besser!"
            show anja vmadb2
            a "UGHHH!"
            show anja madb2
            a "Hey. Du! [name]! Schoko oder Vanilleeis!? Du entscheidest das jetzt."
            menu:
                p "Ähm... Ich glaube ..."
                
                "Schoko ist besser!":
                    $ anja_points += 1
                    show anja happyb2
                    a "HAH! Da hast's, Randy! Jetzt sind wir schon 2."
                    r "Ist doch egal, wenn's Geschmackssache ist. Jetzt macht's aber eh keinen Sinn mehr da noch zu reden."
                    r "Ich geh jetzt, macht doch was ihr wollt ..."
                    hide randy with moveoutright
                    p "Warum habt ihr euch denn jetzt eigentlich gezankt?"
                    a "Ich wollte nur etwas sticheln, dann wurde ich wirklich wütend."
                    a "Du, komm mal mit hoch."
                    
                "Vanille ist besser!":
                    $ anja_points -= 1
                    show randy vhappy
                    "???" "Ha! Siehst du, ist doch nur Geschmackssache! Selbst dein neuer Freund stimmt mir zu!"
                    a "Ich mein, ... ja ... also ... [name], fall mir doch nicht einfach in den Rücken!"
                    a "Egal. Dafür kannst du immer noch nicht klettern Randy."
                    show randy mad
                    r "Ach, lass mich doch in Ruhe..."
                    hide randy with moveoutright
                    show anja happyb2
                    p "Hey, [name]. Kannst du klettern? Komm mal mit hoch!"

            
        "Versuchen den Streit zu stoppen.":
            $ anja_points -= 1
            $ daze = True
            p "Hey! HEY! HÖRT AUF!"
            p "Hört doch auf zu streiten! Das macht doch keinen Sinn"
            show anja vmadb2
            show randy vmad
            "{color=#0099ff}???:{/color} Belauscht du uns einfach? Was soll das?\n{color=#0099ff}Anja:{/color} Misch dich nicht ein!"
            p "Aber ich wollte doch nur ..."
            show randy shock
            show anja happyb2
            a "Oooh, ähm da haben wir wohl eine gleiche Meinung."
            show randy mad
            "???" "Sieht wohl so aus, ich will aber nicht weiter belauscht werden."
            "???" "Ich gehe. Macht doch was ihr wollt."
            hide randy with moveoutright
            show anja madb2
            a "Hast du ja toll gemacht, [name]."
            p "Warte mal, worum ging es eigentlich?"
            show anja happyb2
            a "Hehe, du hast also nicht alles gehört? Dann sag ich auch's nicht."
            p "Komm schon!"
            a "Erst wenn du hier hoch kommst!"


    
    
    menu:
        "Kletterst du zu Anja auf den Baum hoch?"
        
        "Ich kann nicht klettern.":
            p "Also, ähm... Ich kann nicht klettern."
            show anja madb2
            a "Probier's doch wenigstens."
            p "Ich trau mich nicht ... Ich kann das nicht!"
            show anja happyb2
            a "Komm schon, ich zeig's dir auch wie's geht."
            menu:
                "Lieber nicht...":
                    $ anja_points -= 2
                    $ gone = True
                    $ anjatreat = False
                    $ climber = False
                    p "Nein! Nein, nein! Ich ... ich guck mal wo dein Freund ist."
                    show anja madb2
                    a "NA TOLL! Dann geh doch!"
                    n "Verdammt jetzt ist sie sauer… Ich will doch bloß nicht auf diesen Baum. Da fall ich bestimmt nur runter."
                    jump scene12
                    
                "Na gut.":
                    $ climber = True
                    $ anja_points += 3
                    p "Okay, aber wenn mir was passiert bist du Schuld!"
                    a "Jeder kann klettern, ist nur eine Frage der Technik!"
                    p "Ich hoffe ... "
                    a "Warte ich komm erstmal runter ..."
                    play sound grassbump
                    show anja hihi at left with dissolve
                    a "So. Schau erst a mal mir zou."
                    show anja talk
                    a "Nimmst erst as rechte Ba und hebsts an, dann suchst dir mit den Händen nen Halt und dann…"
                    show anja happyb2 at topleft with dissolve
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
            $ climber = False
            $ anja_points -= 3
            $ gone = True
            $ anjatreat = False
            show anja madb2
            a "Hey! Was soll das? Wo willst du hin?"
            show anja vmadb2
            a "NA TOLL! Dann geh doch!"
            n "Verdammt jetzt ist sie sauer… Ich will doch bloß jetzt grad nicht mit ihr spielen."
            jump scene12
            
        "Ich kann klettern.":
            $ climber = True
            $ anja_points += 2
            p "Okay, ich komm zu dir hoch."
            p "Klettern ist einfach. Hände hier, Beine da und schon oben. Hallo du!"
            a "Sauber, kannst's ja so gut wie ich. Respekt."
            p "Ja, ich kletter gern am Gerüst herum."
            a "Bäume sind viel schöner, so groß und massiv. Am besten sind aber Zäune, wie die von meiner Oma!"
                
            
    if daze == True:
        p "Aber worum ging es denn jetzt eigentlich?"
        a "Um Geschmack."
        show anja madb2
        a "Schokolade ist das Beste und Randy mag eben Vanilleeis mehr."
        a "Ich wollte ihn einfach nur etwas nerven deswegen."
        show anja vmadb2
        a "Aber er ist dann immer so langweilig, dass hat mich wütend gemacht."


    show anja madb2
    p "Bist du jetzt noch böse?"
    a "Etwas ..."
    
    if snackersdeal == True:
        menu:
            n "Vielleicht beruhigt sie ja etwas Schokolade?"
            
            "Snackers mit Anja teilen.":
                $ anja_points += 2
                $ anjatreat = True
                p "Ich hab ein paar Snackers. Wenn du Schokolade willst, kann ich dir eins abgeben."
                show anja happyb2
                a "Bist wohl Ein[suf2] mit Geschmack!"
                p "Ich ... weiß nicht wie ich schmecke ..."
                a "Hahaha!"
                play sound snackers
                a "Aaahh, Super. Jetzt gehts mir besser."
                
            "Snackers für mich behalten.":
                $ anjatreat = False
                jump treetalk
                
label treetalk:
    p "Also das war jetzt ... Randy? Wie ist der so? Ist der nett?"
    show anja madb2
    a "Ganz komischer Kauz."
    show anja happyb2
    a "Er ist ein echt netter Kerl und ich bin auf seinen Geburtstag am Freitag eingeladen."
    a "Er ist einer meiner besten Freunde, aber er ist eben so unglaublich normal, dass treibt mich manchmal echt an die Decke."
    p "Und ihr ... "
    a "Außerdem sind wir so oft anderer Meinung und du hasts ja gesehen."
    show anja madb2
    a "Er hat immer den gleichen Standpunkt und wenn er darüber redet ist er sooo laaangweilig, ich weiß nicht was das soll."
    p "Ist das denn so schlecht?"
    a "Eigentlich nicht, aber es nervt mich."
    show anja happyb2
    a "Was er aber mag sind Filme mit riesigen Monstern die miteinander kämpfen."
    a "Er hat einen Bruder bei dem er die Filme immer anschauen kann."
    a "Sein Bruder ist super nett."
    p "Was für Fil-..."
    a "Die Gozok Reihe, Omegas und so weiter."
    a "Kannst du ja vielleicht kennenlernen, ich kann ja mal mit Randy reden, ob du auch am Freitag auch auf seinen Geburtstag kommen kannst…"
    show anja happyb2
    n "Jetzt redet sie wieder. Irgendwann will ich auch mal so viel am Stück reden können."
    show mum n at right with moveinright
    n "Oh… Mama ist da! Ist wohl Zeit nach Hause zu gehen."
    
    ##### Szene 12 #####
label scene12:
    play music maintheme fadeout 1.0
    scene bg bedroom
    show mum happy at center
    with fade
    
    
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
                m "Du hilfst mir morgen in der Küche, dann bekommst du ein Knappers."
                p "Mach ich Mama!"
                
            "Mama nichts von den Knappers erzählen.":
                $ hasknappers = False
        ##### TAG 3 ENDE #####
        
        ##### TAG 4 BEGINN #####
        ##### Szene 13 #####
label scene13:
    play music octatheme fadeout 1.0
    scene bg black with fade
    show thr with dissolve
    $ renpy.pause(0.6, hard = True)
    scene bg street
    show mum happy at center
    with fade
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
    o "Ihr seid doch gute Eltern und habt mir Alles beigebracht."
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
    play sound antiarmor
    o "Und jetzt weg mit dem Zeug."
    hide oschutz
    show octa smug
    with dissolve
    o "Und wieso musst du mich eigentlich ausspannen?"
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
    play sound1 bike
    play sound2 chain
    show obike at right with move
    pause 0.2
    show obike wheelier with dissolve
    pause 0.2
    show obike at center with move
    show obike at left with move
    pause 0.2
    show obike wheelie with dissolve
    pause 0.2
    play sound3 bikebreak
    show obike at center with move
    pause 0.2
    stop sound1 fadeout 1.0
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    show obike n
    p "Wow!"
    o "Siehste, ganz einfach. Jetzt du!"
    hide obike
    show octa smug at center
    p "Was? Ich darf doch nicht."
    o "Ist doch egal. Probier's mal aus. Bist doch kein Weichei und wenn du fällst ist's ja nicht so schlimm. Hier, kannst auch meinen Helm haben."
    
    
    
    menu:
        o "Bawk, Bawk Bawk! Komm schon, du bist doch kein Angsthase, oder?"
        
        "Auf das Fahrrad steigen.":
            $ octa_points += 2
            p "Ist ja gut, ich mach ja schon."
            
            
        "Nein.":
            $ octa_points -= 1
            p "Ich... Ich will wirklich nicht!"
            o "Ohh, du bist wohl ein Angsthase."
            show octa mad
            o "Jetzt mach oder ich erzähl Allen, dass du mich vom Rad geschubst hast!"
            menu:
                "Doch auf's Rad steigen.":
                    $ octa_points += 1
                    p "Schon gut! Ich fahre ja."
                    
                    
                "Sich weiterhin weigern.":
                    $ octa_points -= 2
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
    window hide
    scene cg biking with fade
    $ renpy.pause ()
    window auto
    play sound1 bike loop
    play sound2 chain loop
    p "Ooookay und jetzt?"
    o "Und jetzt auf einem Rad! Los! Los!"
    o "Das Hinterrad, komm schon! Komm schon! Komm schon!"
    p "Okay ... also ... SO! Octa guck! Ich kann es! ich kann es!"
    o "[name] pass auf! KATZE!"
    window hide
    scene cg bikecat with dissolve
    play sound3 bikebreak
    play sound bell
    stop sound1 fadeout 1.0
    stop sound2 fadeout 1.0
    $ renpy.pause ()
    window auto
    p "Ohh ... WOAH! Katze vorsicht!"
    window hide
    scene cg bikefall with fade
    play sound grassbump
    $ renpy.pause ()
    window auto
    p "Aua ..."
    
    menu:
        p "Das hat weh getan ..."
        
        "Weinen.":
            $ octa_points -= 1
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
            $ octa_points += 1
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
            
      
    if crying == True:
        scene bg court with fade
        show octa shock at center with moveinright
        show heide mad at right with moveinright
        h "Großer Gott! Was ist denn das hier für ein Tumult!"
        h "Was ist denn hier passiert?"
        h "[name] jetzt hör auf zu weinen. Kannst du laufen?"
        p "Also ich ... {i}schnüff{/i}... ich glaube schon."
        o "D...dann kann ich ja jetzt gehen."
        show octa shock at left with move
        h "{b}OCTAVIA SIEGLINDE!{/b}"
        o "J... ja Frau Heidenau!"
        h "Warum liegt [name] hier weinend am Boden?!"
        o "Also ich ..."
        h "Wir reden später. Ihr beiden kommt jetzt mit. [name], wir verarzten dein Bein. Trab trab!"
        p "Aber das tut weh!"
        h "Gleich nicht mehr. Jetzt stell dich nicht so an und komm mit."

    else:
        scene bg court with fade  
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
    h "Die Beste. Jaja. Wie du meinst."
    show octa happy
    h "Aber das war richtig. Also halt still, [name]."
    h "Jetzt noch ein Pflaster drauf ... und gut. Besser?"
    p "Ja, besser."
    h "Und jetzt will ich wissen..."
    show heide mad
    show octa shock
    h "Was da draußen passiert ist!"
    o "Also ... ähm ..."
    
    menu:
        n "Wie erklär ich das jetzt?"
        
        "Die Wahrheit":
            $ octa_points -= 3
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
            
        "Notlüge":
            $ octa_points += 2
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
            show heide talk
            h "So ist das also."
            show karin n
            show octa happy
            h "Also ein Unfall. Kann ja mal passieren."
            h "Und es geht dir wieder besser?"
            show heide n
            o "Ja, uns geht's gut!"
            p "Was? Ohh. Ja. Gut. Uns geht's gut."
            o "Dürfen wir dann jetzt wieder mit Karin in den Gruppenraum?"
            show heide talk
            h "[name] ist ja jetzt verarztet. Also ja, ab mit euch."
            h "Bringst du sie Karin?"
            k "In Ordnung, Frau Heidenau."
            hide karin
            hide octa
            with moveoutright
            show heide laugh at center with move
            h "Hmm... Gelogen habt ihr. Aber wenigstens zusammengehalten. Vielleicht sind ja nicht alle Kinder furchtbar."
            
    if octahome == True:
        window hide
        scene cg marble with fade
        $ renpy.pause ()
        window auto
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
    play music maintheme fadeout 1.0
    scene bg black with fade
    show fri with dissolve
    $ renpy.pause(0.6, hard = True)
    scene bg flur with fade

       
    n "Es ist Freitag. Also praktisch Wochenende. Da bin ich immer bei Papa. Vielleicht bekomme ich ja wieder Eis und Schokolade als Abendessen?"
    n "Hoffentlich!"
    n "Außerdem muss ich Papa unbedingt meine Bilder zeigen."
    n "So schön wie die von Evelynn sind sie leider nicht, aber fast!"
    n "Wo ist Evelynn eigentlich?"
    n "Vielleicht weiß Karin ja wo sie ist."
    scene bg grura
    show karin talk at center
    with fade
    p "Du... Karin..."
    k "Ja [name]?"
    p "Kann ich dich was fragen?"
    show karin happy
    k "Gerne. Was willst du denn fragen?"
    p "Wo ist denn Evelynn? Ich find die nicht."
    show karin talk
    k "Du musst die Evelynn nicht suchen. Die ist heute zu Hause geblieben."
    k "Ihre Mutter muss angeblich etwas einkaufen und braucht dafür Evelynn. Mehr kann ich dir nicht sagen."
    
    p "Mhhh. Mann."
    p "Ist ja voll doof, wollte was mit ihr malen."
    show karin vhappy
    k "Ich kann ja mit dir malen."
    p "Ne, das macht dann keinen Spaß!"
    show karin mad
    k "Also gut..."
    p "Dann halt was Anderes."
    hide karin with dissolve

    n "Scheibenkleister!"
    n "Na gut. Dann muss ich eben mit Anja den Tag verbringen."
    n "Die hat sicherlich wieder viel zu erzählen, außerdem muss man die nicht suchen. Anja hört man immer!"
    
    a "Gar nicht wahr!"
    n "Ich hör sie sogar jetzt."
    a "Mit den Hula Hoop Reifen bin ich viel besser als du!"
    n "Was is da los? Ich sollte mal nachschauen."
    scene bg court
    show anja mad at rightish
    show octa mad at leftish
    with fade
    o "Ich kann ihn 32 mal drehen bis er runterfällt."
    a "Stimmt doch gar nicht. So schnell kann man nicht mal zählen!"
    show octa smug
    o "Du vielleicht nicht. Ich kann das schon!"
    a "Lügnerin!"
    show octa vmad
    o "Nenn mich nicht so, wenn ich Keine bin!"
    show fight with dissolve
    n "Mama würde jetzt sagen, die Beiden sehen aus wie Zankhähne. Ich selber hab noch nie zankende Hühner gesehen."
    a "Aber du kannst das nicht!"
    o "Kann ich wohl!"
    hide fight with dissolve
    n "Irgendwie blick ich nicht durch, aber Hula Hoop hört sich lustig an"
    p "Darf ich vielleicht den Reifen haben?"
    "{color=#0099ff}Octavia:{/color} Du erst recht nicht! \n{color=#0099ff}Anja:{/color} Gerade nicht!"
    n "Wie es aussieht bin ich hier nicht erwünscht. Ich sollte wohl einfach gehen."
    scene bg grura2 with fade
    n "Och man, was soll ich dann machen... Murmelbahn vielleicht? Auch langweilig..."
    n "Hmmh..."
    n "Was solls, auf zur Murmelbahn!"
    window hide
    scene cg marble with fade
    $ renpy.pause ()
    window auto
    p "Dann kommt das noch hier hin und dann..."
    p "LAAANGWEILIG!"
    
    scene bg flur
    with fade
    r "Da, [name]"
    p "Hmmh?"
    n "Die Stimme kommt von hinten. Ich drehe mich um und sehe Randy."
    show randy happy at center
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
    window hide
    scene cg marble with dissolve
    $ renpy.pause ()
    window auto
    n "Ich hoffe nur, dass Mama mich dann auch zur Feier fährt."
    n "Nach einer Weile tippt mir jemand von hinten auf die Schulter."
    p "Huh?"

        
label scene16:
    scene bg grura
    show karin n at rightish
    show mum n at leftish
    with fade
    k "Hey, [name]. Deine Mutter ist etwas früher gekommen um dich abzuholen."
    m "Hallo Klein[suf2]. Ich muss noch etwas in der Stadt erledigen und wollte, dass du mitkommst."
    p "In Ordnung."
    n "Ich packe also meine Sachen und gehe mit Mama zum Auto."
    scene bg street
    show mum n at rightish
    with fade
    n "Auf der Straße fällt mir wieder etwas ein."
    
    p "Mama!"
    m "Ja?"
    p "Ich wurde auf Randys Geburtstag eingeladen! Darf ich da hingehen? Darf ich? Darf ich?"
    show mum happy
    m "Schön, dass du schon Freunde gefunden hast. Meinetwegen gerne. Wann genau ist denn der Geburtstag?"
    n "Ich geb ihr meine Einladung."
    p "Da!"
    m "Hmmmh..."
    show mum mad
    m "15 UHR!"
    m "Wieso bekomme ich das erst jetzt?"
    p "Ich hab die Einladung aber doch grad erst bekommen."
    show mum talk
    m "Na gut. Ich muss dann aber noch deinem Vater sagen, dass er dich von der Feier abholen soll."
    p "Wir sollen uns außerdem verkleiden!"
    show mum mad
    m "Mmmmmhhhhh."
    m "Verdaaaaa..."
    show mum happy
    m "Ähhhm. Klar. Wir sind ja eh in der Stadt. Da können wir ja mal kurz in den Kostümladen schauen."
    p "YAAAY!"
    play sound cardoor1
    play music playtheme1 fadeout 1.0
    scene bg shop with fade
    n "Man, hier haben Sie ja wirklich alles! Von typischen Monsterkostümen wie eine Riesenmotte mit bunten Flügeln, bis hin zu... huh"
    n "Ein Tier... Tier... Hasensäbelzahnelchwolf?"
    n "Rehhundkatzenkanninchen?"
    p "Mama! Was ist denn das? Das sieht ja komisch aus."
    show mum talk at left with moveinleft
    m "Hmmmh..."
    m "Ich weiß nicht genau... Vielleicht ein Wolpertinger?"
    p "Ein Wolterdinger?"
    show mum happy
    m "Wolpertinger. Ein Fabelwesen, welches aus ganz vielen Tieren besteht. Das Wesen kommt aus Bayern."
    p "Cool."
    show mum n
    m  "Aber schau mal her dieser Orca ist ja nett."
    p "WOAH! EIN KILLERWAL!"
    show mum talk
    m "Oder ein Killerwal, wenn dir das besser gefällt."
    show mum happy
    m "Wir haben aber leider nicht ewig Zeit. Hast du dich schon für was entschieden?"
    hide mum with dissolve
    
    menu:
        m "Wir haben aber leider nicht ewig Zeit. Hast du dich schon für was entschieden?"
        "Killerwal":
            $ octa_points += 2
            $ costume = "wal"
            p "KILLERWAL!"
            m "Woah. Also dann, alles klar."
            m "Viel Enthusiasmus hier."
            p "Wieso?"
            m "Weil du dich auf das Kostüm freust. Gefällt dir doch, oder?"
            n "Ich nicke"
        
        "Motte":
            $ anja_points += 2
            $ costume = "moth"
            p "Mofpa!"
            m "Die sieht ja scheußlich aus."
            p "Die ist aus‘nem ganz coolen Film! Bitteeeee!"
            m "Wenn du meinst, ich überlass dir heute ja die Entscheidung."
            p "Ja, ich will das Kostüm."
            
        "Wolper...dings":
            $ eve_points += 2
            $ costume = "wolp"
            p "Wolterdimper. Der ist voll cool!"
            m "Gerne kauf ich dir den Wol-Per-Ting-Er, wenn du ihn richtig aussprichst."
            p "Wieso?"
            m "Weil ich‘s süß finde."
            p "Ok... Wol-Per-Ting-Er... Wolperdinger."
    
    show mum talk at center with dissolve
    m "Na dann. Ab zur Kasse"
    scene bg black with dissolve
    
    n "Jetzt, wo ich mein tolles Kostüm habe, kann ich auf den Geburtstag gehen!"
    n "Das wird sicher super!"
    n "Jetzt sind wir auch mit Einkaufen fertig, ich hoffe ich komme noch rechtzeitig zum Randys Geburtstag!"

label scene17:
    
    play sound cardoor1
    play music happytheme1 fadeout 1.0
    scene bg street
    show mum talk at rightish
    with fade
    m "So, wir sind da."
    n "Ich steige vollkostümiert aus dem Auto aus und bin schon ganz gespannt, was die Anderen an haben werden!"
    n "Mama nimmt mich an die Hand und führt mich zur Tür."
    p "Darf ich klingeln?"
    show mum happy
    m "Der Knopf da oben ist der Richtige."
    show mum talk
    n "Kurz darauf geht die Tür auf."
    m "So, geh mal zu deinen Freunden. Ich rede noch kurz mit Randys Mama und bin dann gleich weg. Vergiss nicht, dein Papa holt dich heut Abend ab."
    p "OK. Tschüss Mama."
    hide mum talk with moveoutright
    scene bg party with dissolve
    n "Ich komme kaum ins Zimmer, da kommt Louis mir schon entgegen."
    show lparty n with moveinright
    L "Hey, [name]."
    p "Hey, Louis."
    
    if snackersdeal == True:
        L "Und, hast du dran gedacht?"
        p "An?"
        L "Na ans Knappers!"
        if hasknappers == True:
            menu:
                "Versprechen erfüllen.":
                    $ eve_points += 1
                    $ anja_points += 2
                    $ trade = True
                    p "Einen Moment... Hier!"
                    show lparty happy
                    L "Gut, dass auf dich Verlass ist."
                    p "Jetzt sind wir quitt, oder?"
                    L "Ja klar. Wenn du noch mal was willst, komm wieder zu mir."
                    n "Du bist doch zu mir gekommen..."
                    show lparty really
                    L "Wollte mich außerdem für das im Kindergarten entschuldigen..."
                    p "Warum?"
                    L "War vielleicht ein bisschen zu gemein."
                    p "Was ... ach Louis. Alles gut.."
                    p "Wir sind doch Freunde, oder?"
                    show lparty happy
                    L "Na klar sind wir Freunde!"
                    p "Sag mal, was bist du für ein Monster?"
                    show lparty smug
                    L "Dr. Acula! Der weltbekannte Arzt."
                    L "Kennst du den wohl nicht?"
                    p "Natürlich!"
                    n "Wenn er weltbekannt ist, dann muss ich ihn ja kennen."

                
                "Alle aufgegessen...":
                    $ octa_points -= 2
                    $ eve_points -= 1
                    $ anja_points -= 3
                    $ trade = False
                    p "Ohh..."
                    p "Ich hab garnicht dran gedacht, dass du ja auch welche von mir bekommst."
                    p "Ich hab die schon alle aufgegessen..."
                    p "Ich bring dir nächste Woche auch zwei Knappers mit!"
                    show lparty mad
                    L "Blödian!"
                    L "Du hast es mir versprochen, du bekommst nichts mehr von mir!"
                    p "Ich bring dir doch nächste Woche zwei Knappers mit, ganz ehrlich!"
                    L "Versprechen werden nicht gebrochen!"
                    n "Louis ist wohl echt böse auf mich ..."
                    n "Vielleicht lässt er sich ja ablenken?"
                    p "Was bist du denn eigentlich für ein Monster?"
                    L "Sag ich nicht!"
                    n "Ohh je, wie mach ich das wieder gut?"

        else:
            menu:
                "Das hab ich total vergessen!":
                    $ octa_points -= 2
                    $ eve_points -= 1
                    $ anja_points -= 2
                    $ trade = False
                    p "Ohh nein ... Ich hab vergessen Mama zu sagen, dass wir welche kaufen müssen!"
                    p "Ich bring dir nächste Woche auch zwei Knappers mit!"
                    show lparty mad
                    L "Blödian!"
                    L "Du hast es mir versprochen, du bekommst nichts mehr von mir!"
                    p "Wieso bist du denn so wütend?"
                    p "Ich bring dir doch nächste Woche zwei Knappers mit, ehrlich!"
                    L "Versprechen werden nicht gebrochen!"
                    n "Louis ist wohl echt böse auf mich ..."
                    n "Vielleicht lässt er sich ja ablenken?"
                    p "Was bist du denn eigentlich für ein Monster?"
                    L "Sag ich nicht!"
                    n "Ohh je, wie mach ich das wieder gut?"

    else:
        L "Also... ich wollte mich für das im Kindergarten entschuldigen..."
        p "Warum?"
        L "War vielleicht ein bisschen zu gemein."
        p "Was ... ach Louis. Alles gut.."
        p "Wir sind doch Freunde, oder?"
        show lparty happy
        L "Na klar sind wir Freunde!"
        p "Sag mal, was bist du für ein Monster?"
        show lparty smug
        L "Dr. Acula! Der weltbekannte Arzt."
        L "Kennst du den wohl nicht?"
        p "Natürlich!"
        n "Wenn er weltbekannt ist, dann muss ich ihn ja kennen."
    
    show lparty really
    "???" "Hallo, Kinder!"
    n "Eine große Frau kommt in den Raum."
    show lparty really at leftish with move
    show rmum talk at rightish with moveinright
    "???" "Hallo Louis und du da musst das neue Kind sein, von den mir mein Sohn erzählt hat."
    rmum "Ich bin Erika, also Randys Mama Erika. Schön euch zu sehen."
    rmum "Die Anderen sind grad in Randys Zimmer, kommen aber gleich wieder."
    rmum "Niedliche Kostüme übrigens."
    p "Danke."
    n "Och man. Ich wollte doch gruselig sein, ich bin doch ein Monster!"
    hide lparty really with dissolve
    hide rmum talk with moveoutright

label scene18:
    n "Es scheinen schon einige Leute da zu sein. Ich kann sogar schon Anja plappern hören! Und auf dem Fernseher läuft ein Film: Radzilla vs. Mofpa!"
    n "Randy kommt zuerst wieder in das Zimmer gerannt."
    show rparty happy at center with moveinright
    r "Hey [name], konntest ja doch kommen."
    if costume == "moth":
        show rparty vhappy
        r "MOFPA!"
        n "Randy strahlt mich an."
        n "Er ist natürlich als Radzilla verkleidet."
        show rparty talk
        r "Mein größter Feind... Irgendwie."
        p "Aber heute sind sie Freunde!"
        r "Toll, dass du gekommen bist."
        
    else:
        show rparty talk
    show geschenk at topishleft with dissolve
    p "Hier Randy, dein Geschenk."
    p "Cooles Kostüm."
    n "Irgendwie ist er wohl von etwas abgelenkt."
    r "Danke, mach ich später auf. Leg es da auf den Tisch, OK?"
    hide geschenk with dissolve
    p "Mach ich!"
    n "Ich lege das Geschenk auf den Tisch und dreh mich um. Ich sehe nichts Besonderes, auf was hat Randy geschaut?"
    hide rparty happy
    if costume == "moth":
        jump scene19
    elif costume == "wolp":
        jump scene20
    else:
        jump scene21
    
label scene19:
    
    n "Naja egal, erstmal Kuchen essen."
    a "Nimm das Mofpa!"
    n "Jemand sticht mir in meine Seiten."
    play music apartytheme fadeout 1.0
    show aparty mad with dissolve
    p "Hey, lass das!"
    a "Aber du bist doch Böse!"
    p "Aber das tut trotzdem weh."
    if snackersdeal == True:
        if trade == True:
            show aparty n
            a "Hehe, Louis hat gesagt du hast Knappers dabei?"
            p "Hatte ich! Aber nur eins ..."
            p "Und das hab ich Louis gegeben."
            p "Der hat mir dafür drei Snackers getauscht!"
            a "Aha! Ein ehrlicher Tauschhandel. Das macht den Sherrif aber glücklich."
            a "Gut, dass man sich auf dich verlassen kann!"
            show aparty jabber        
            a "Bist wohl ein ehrbares Monster!"
            
            if anjatreat == True:
                show aparty n
                a "Aber, waren das die, die du mir gegeben hast? Ahhhw. Ist ja Süß."
                p "Ja Snackers sind süß."
                show aparty talk
                a "Oh Mann. Finde es trotzdem toll, dass du extra Snackers für mich besorgt hast."
                n "Extra für sie?"
                n "Häh, ich hab doch nur mit Louis getauscht."
                n "Dieses Mädchen ist echt komisch."
                show aparty jabber
                a "Hmmmh?"
                jump scene19f
                
            else:
                show aparty shock
                a "Und du hast mir keins abgegeben?"
                p "Hab nicht daran gedacht."
                show aparty n
                a "Na gut Partner..."
                show aparty mad
                a "Hände Hoch, dass ist ein Überfall."
                p "Aber ich hab doch keine mehr dabei!"
                show aparty jabber
                a "War nur ein Jucks."
                a "Hmmmh?"
                jump scene19f

        else:
            a "Und doof bist du auch!"
            show aparty mad
            p "Was?"
            a "Louis hat‘s mir gesagt. Du versprichst ihm Knappers und bringst sie ihm dann nicht mit!"
            p "Ich konnte noch keine..."
            a "Mach so etwas NIE WIEDER!"
            a "Versprechen bricht man nicht und die Anderen finden das auch dumm."

            if anjatreat == True:
                p "Aber, du hattest doch auch nichts dagegen, als ich sie mit dir geteilt hab!"
                show aparty shock
                a "Was?"
                show aparty mad
                a "DU VOLLIDIOT HAST EINEM SHERIFF GESTOHLENES ESSEN GEGEBEN?!"
                a "Ich dachte das wäre deins gewesen du Lügner!"
                hide aparty mad with moveoutright
                n "Irgendwie kommt es mir so vor, als würde mich jeder anschauen."
                n "Vielleicht hab ich das auch verdient ..."
                n "Hoffentlich hab ich jetzt Randy nicht den Geburtstag verdorben."
                "..."
                n "Hmm... wie es aussieht nehmen es mir die Anderen gar nicht so übel."
                show rmum n at center with moveinright
                rmum "Kommt mal alle zusammen ihr kleinen Monsterlein!"
                rmum "Gruppenfoto!"
                n "Wenigstens darf ich auch noch auf das Foto."
                rmum "Sagt Käsekuchen"
                scene cg selfiemoth with dissolve
                "Alle" "Käääääseeeekuuuucheeeen!"
                window hide
                $ renpy.pause ()
                window auto
                scene bg black with fade
                jump scene22
                
            else:
                p "Es tut mir ja leid ..."
                p "Ich hab mich doch schon entschuldigt ..."
                p "Ich würde es auch gerne zurückgeben aber ich hab heute keins dabei."
                p "Ich hab Louis gesagt er bekommt nächste Woche zwei Knappers ..."
                show aparty n
                a "Ist... Verstehe, trotzdem. Nie.."
                p "Nie wieder!"
                a "Nie wieder!"
                show aparty jabber
                a "Hmmmh?"
                jump scene19f

label scene19f:
    n "Wieso schaut sie mich denn jetzt so an?"
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
    show aparty talk at leftish with move
    show rparty happy at rightish with moveinright
    r "Ja?"
    a "Radzilla, hier, Mofpa da."
    a "LOS!"
    n "Jetzt wird auch noch Randy herumkommandiert."
    hide aparty with dissolve
    show rparty vhappy at center with move
    r "Ich verstehe."
    p "Ich nicht!"
    show rparty talk
    r "Also in Radzilla gegen Prince Ape, kämpft er gegen Prince Ape und in..."
    show aparty talk at right with moveinright
    a "Er kämpft gegen Mofpa."
    hide aparty with moveoutright
    r "In einem Film, eigentlich sind sie..."
    show aparty mad at right with moveinright
    a "EGAL! LOS!"
    hide aparty with moveoutright
    r "Bereit für einen Monsterkampf in der Stadt?"
    menu:
        "Bereit.":
            n "Es ist sein Geburtstag, muss ja sein..."
            p "Bereit!"
            
        "Bereiterer.":
            $ anja_points += 1
            n "An seinem Geburtstag doch immer."
            p "Na klar!"
            
        "Am Bereitesten.":
            $ anja_points += 2
            n "Das müssen sie noch fragen?"
            p "Ich bin bereit! Ich bin bereit! Ich bin bereit!"
    
    a "3"
    a "2"
    a "1"
    a "Los!"
    show rparty vmad
    r "WAAAAH!"
    scene bg party
    show rparty vhappy at leftish
    show aparty jabber at rightish 
    with fade
    n "Als wir fertig gekämpt hatten waren wir erschöpft und glücklich."
    n "Und die Kartonstadt völlig zerstört."
    n "Und natürlich gab es im Anschluss noch Kuchen!"
    p "Ooof... Fertig"
    show aparty at slightright with move
    show rmum talk at right with moveinright
    with dissolve
    rmum "Keine Müdigkeit vortäuschen."
    rmum "Kommt mal alle zusammen für ein Gruppenfoto."
    rmum "Los alle! Käsekuchen!"
    scene cg selfiemoth with dissolve
    "Alle" "Käääääseeeekuuuucheeeen!"
    window hide
    $ renpy.pause ()
    window auto
    scene bg black with fade
    jump scene22
    

label scene20:
    n "Aber da drüben seh ich Evelynn. Ich sollte mal Hallo sagen."
    show eparty talk2 at center with moveinright
    play music epartytheme fadeout 1.0
    p "Hi, Evelynn."
    e "Wow! Du siehst ja wild aus [name]."
    e "Komm mal mit mir mit."
    p "Wohin denn?"
    show eparty happy2
    n "Sie packt mich an meinem Arm und zeigt auf jemanden der sich komisch bewegt, während andere..."
    p "Oh nein!" 
    p "Scharade."
    show eparty vhappy2
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
            $ eve_points += 2
            p "Gut, dann fang ich eben an. Aber Evelynn, du kommst danach dran."
            e "Na gut."
            n "Randy gibt mir einen Zettel auf dem steht... natürlich."
            show rparty happy at rightish
            show eparty happy2 at right
            with move
            show oparty happy at center
            show lparty n at leftish behind oparty
            show aparty n at left behind lparty
            with moveinleft
            n "Radzilla..."
            
            menu:
                "Dinosauriergebrüll":
                    $ eve_points -= 2
                    p "Roooaaaar"
                    show oparty mad
                    show eparty mad
                    show aparty shock
                    show rparty vhappy
                    show lparty mad
                    e "Keine Geräusche. Kein Schummeln."
                    r "Jaaa! Richtig!"
                    o "Tss... tss... tsss..."

                "Umherstampfen":
                    $ eve_points += 2
                    show aparty mad
                    show eparty talk2
                    show oparty talk
                    show rparty vhappy
                    show lparty happy
                    e "Ein Monster!"
                    o "Vielleicht ein Minotaurus?"
                    a "Ich als Cowboy? Nicht lustig."
                
                "Rumstehen":
                    $ eve_points -= 1
                    show eparty talk2
                    show oparty mad
                    show rparty vmad
                    show aparty mad
                    show lparty really
                    e "Los, mach was."
                    e "Trau dich."
                    o "Voll lahm."
                    n "Lampenfieber. OK ich schaff das schon..."
            
            n "Ich sollte wohl noch mehr machen."
            menu:
                "Stampf über die Kartonstadt.":
                    $ eve_points += 2
                    show eparty vhappy2
                    show oparty vhappy
                    show aparty jabber
                    show rparty vhappy
                    show lparty happy
                    e "Das Monster das gerade im Fernsehen läuft!"
                    a "Radzilla! Du bist Radzilla!"
                    o "Nicht schlecht."

                "Gib auf!":
                    $ eve_points -= 2
                    p "Tut mir Leid, fühl mich nicht gut."
                    show oparty buh                    
                    show eparty mad
                    show aparty mad
                    show rparty vmad
                    show lparty really
                    e "Wirklich, du gibst auf?"
                    o "Typisch."
                    p "Entschuldigung."
                    
                "Floppe auf dem Boden herrum.":
                    show oparty happy
                    show eparty talk2
                    show aparty shock
                    show rparty vhappy
                    show lparty really
                    e "Ähm. Fisch auf dem Trockenen?"
                    a "Trauriger Wal?"
                    r "Radzilla?"
                    p "Richtig!"
                    r "Also, so toll hast du den jetzt nicht gespielt. Aber du wolltest wohl etwas kaputt machen."
                    p "Ääääähhhm... Richtig, das wollte ich."
            
            show oparty happy
            show aparty n
            show eparty talk2
            show rparty vhappy
            show lparty n
            r "So, jetzt bist du dran Evelynn."
            show eparty mad
            e "Jetzt schon?"
            show rparty talk
            r "Ihr seid die Neuen, also ja."
            show eparty happy2
            e "O... OK."
            hide oparty
            hide aparty
            hide rparty
            hide lparty
            with dissolve
            show eparty at center with move
            n "Evelynn will gerade loslegen als Randy's Mama um die Ecke schaut."
            jump foto
            
            
        "Evelynn darf anfangen.":
            $ eve_points += 1
            p "Komm Evelynn, du fängst an."
            show eparty mad at rightish
            e "Was? Wieso?"
            p "Wir müssen eh beide spielen und du hast mich hier her gebracht."
            show eparty talk2 at rightish
            e "Na gut."
            r "Evelynn, dein Wort ist..."
            "Randy gibt ihr einen Zettel."
            hide rparty talk with moveoutleft
            show eparty talk2 at center with move
            r "Bereit?"
            e "Ja."
            r "Los."
            hide eparty talk 
            show epanto
            n "Was macht die da?"
            
            menu:
                "Jemand der seitlich steht":
                    $ eve_points -= 1
                    p "Ein umfallender Mensch."
                
                "Skateboarder":
                    $ eve_points += 1
                    p "Skateboardfahrer!"
                
                "Keine Ahnung!":
                    $ eve_points -= 2
                    p "Ääähm, was bitte?"
            
            r "Radzilla? Der steht auch viel rum."
            a "Sumo-Ringer?"
            a "Ganz sicher."
            o "Der Turm von Pisa!"
            
            show epantobaum
            hide epanto
            n "Evelynn nimmt sich einen Ast der zur Deko gehört und stellt sich darauf, ich glaube es könnte..."
            menu:
                "...ein Surfer...":
                    $ eve_points += 2
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
                            $ eve_points += 2
                            p "Evelynn ist doch eine gute Schauspielerin. War doch nicht so schwer."
                            show eparty happy2 at rotationreset
                            o "Angeber."
                            r "Jetzt bist du dran [name]. Los!"
                            "Randy reicht mir einen Zettel..."
                            n "Ich will gerade loslegen als Randys Mama um die Ecke schaut."
                            jump foto
                            
                        "Nichts sagen.":
                            $ eve_points -=1 
                            p "..."
                            show eparty mad at rotationreset
                            "Evelynn schaut mich einfach weiter an."
                            e "Du bist dran!"
                            r "Stimmt, hier dein Zettel!"
                            n "Ich will gerade loslegen als Randys Mama um die Ecke schaut."
                            jump foto

                "...garnichts...":
                    $ eve_points -= 1
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
                            $ eve_points += 2
                            p "Ist auch kein leichtes Wort, schlecht hast du nicht gespielt."
                            show eparty happy2 at rotationreset
                            o "Ähm was?"
                            r "Jetzt bist du dran [name]. Los!"
                            "Randy reicht mir einen Zettel..."
                            n "Ich will gerade loslegen als Randys Mama um die Ecke schaut."
                            jump foto

                        "Mit dem Rest schweigen":
                            $ eve_points -=1 
                            "..."
                            show eparty talk2 at rotationreset
                            e "Du bist dran!"
                            r "Stimmt, hier dein Zettel!"
                            n "Ich will gerade loslegen als Randys Mama um die Ecke schaut."
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
                            $ eve_points += 2
                            p "Ist auch kein leichtes Wort, schlecht hast du nicht gespielt."
                            show eparty talk2 at rotationreset
                            o "Ähm was?"
                            r "Jetzt bist du dran [name]. Los!"
                            "Randy reicht mir einen Zettel..."
                            n "Ich will gerade loslegen als Randys Mama um die Ecke schaut."
                            jump foto

                        "Mit dem Rest schweigen":
                            $ eve_points -=1 
                            "..."
                            show eparty talk2 at rotationreset
                            e "Du bist dran!"
                            r "Stimmt, hier dein Zettel!"
                            n "Ich will gerade loslegen als Randys Mama um die Ecke schaut."
                            jump foto
    
label foto:
    show rmum talk at left with moveinleft
    rmum "Kommt Kinder! Es gibt Kuchen!"
    show rparty vhappy at right with moveinright
    r "Ohh Junge! Ist der mit Kuchengeschmack?"
    n "Natürlich rennen wir sofort alle an den Esstisch."
    scene bg party
    show rmum talk at center
    with fade
    rmum "Kommt mal alle zusammen für ein Gruppenfoto."
    "Auch noch so was. Na gut."
    rmum "Los alle! Käsekuchen!"
    scene cg selfiefriendo with dissolve
    "Alle" "Käääääseeeekuuuucheeeen!!"
    window hide
    $ renpy.pause ()
    window auto
    scene bg black with fade
    jump scene22
    
    
label scene21:
    n "Naja egal, erstmal Kuchen essen."
    show oparty buh at center with dissolve
    play music opartytheme
    o "BOOOH"
    p "Ahh!"
    show oparty vhappy    
    o "Haha."
    show oparty happy
    p "Octavia! Erschreck mich doch nicht so ..."
    o "Cooles Kostüm, [name]"
    o "Sieht sogar mal gut aus."
    show oparty talk
    p "Danke!"
    p "Seh ich sonst nicht gut aus?"
    o "Doch schon... Ich meine..."
    o "Du scheinst ja doch was zu können."
    p "Danke. Aber du siehst auch gut aus."
    p "Wenn ich jetzt noch wüsste was du bist ..."
    show oparty happy
    o "Ich bin die Medusa aus der griechischen Antike."
    p "Die Schlangenhaare sehen mega gruselig aus."
    show oparty talk
    o "Sag mal ..."
    p "Ja?"
    o "Willst du mir bei was helfen?"
    p "Was willst du denn genau machen?"
    show oparty buh
    o "Anja erschrecken, so wie dich."
    show oparty talk
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
    show oparty happy
    n "Zu Stein erstarren? Das will ich sehen!"
    n "Aber Anja ist zäh, mal schauen ob das was wird!"
    scene bg partyocta with dissolve
    n "So, wo ist Anja?"
    n "Ach da drüben steht sie ja."
    p "Hey Anja!"
    show aparty jabber at center with dissolve
    a "Hi [name], was bist du denn?"
    p "Ein KILLERwal!"
    p "Und du bist der Sheriff dieser Stadt?"
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
        n "Egal. Ich kann sie überzeugen."
        "WALDkillerwal":
            $ octa_points += 1
            n "Dann bin ich eben der erste WALDKILLERwal und du wirst berühmt für deine Entdeckung!"
            show aparty jabber
            a "So richtig glaub ich dir das nicht."
            a "Aber egal, lass uns spielen!"
        
        "In Panama gibt es Dschungel-Wale":
            $ octa_points += 2
            p "Ich hab mal gehört, in Panama gibt es Wale die im Dschungel sind. Auf so großen Wassern."
            show aparty shock
            a "So etwas kann es geben?"
            a "Wow."
            show aparty talk
            a "Na gut, lass uns klettern."
        
        "Klettern ist klettern":
            $ octa_points -= 1
            p "Klettern ist klettern. Macht doch trotzdem Spaß."
            show aparty mad
            a "Recht haste ja."
            "..."
            show aparty talk
            a "Na gut, wenn du es willst."
            n "Irgendwie hat‘s ja doch geklappt."
            
    show aparty n
    a "Die Bäume sind echt klein, aber eventuell wenn wir..."
    show bg party
    show oparty buh at slightright behind aparty with dissolve
    o "HSSSSSS!"
    play sound1 scream
    show aparty shock at center
    "{color=#0099ff}[name]:{/color} AAAAH! \n{color=#0099ff}Anja:{/color} AAAH! HIMMEL HERRGOTT SACKERER!"
    n "Wo kam die denn her?!"
    show oparty vhappy at rightish with move
    o "Ihr beide hattet ja echt mega Angst."
    o "Ihr seid ja wirklich erstarrt!"
    show aparty mad at slightleft with move
    a "Wieso machst du sowas!"
    o "Ruhig, ist doch eine Monsterparty"
    a "Manchmal bist du echt doof!"
    show oparty mad
    o "Aber niemals so doof wie du."
    a "Du hast gerade bewiesen, dass es... noch doofer geht als ich."
    o "Also gibst du zu, dass du doof bist?"
    show aparty at center with MoveTransition(0.2)
    a "AAAAH!"
    show fight with dissolve
    n "Oh man, wieder ein Streit. Aber diesmal gibt es einen Ausweg!"
    hide fight with dissolve
    p "LEUTE! LEUTE! RUHIG!"
    "{color=#0099ff}Octavia::{/color} WAS IST?! \n{color=#0099ff}Anja:{/color} WAS WILLST DU?!"
    "...."
    p "Kuchen!"
    show oparty talk
    o "Wie bitte?"
    a "Versteh ich nicht."
    p "Wir sind hier auf einer Party, wollen wir nicht mal etwas Kuchen essen?"
    o "Ich mein... Eigentlich schon."
    show oparty happy
    show aparty talk
    a "Kuchen hört sich gut an."
    p "Dann auf zum Kuchen mampfen." 
    p "Und du... Anja?"
    show aparty n
    a "Hmm?"
    p "Wer ist denn Herr Gottsackerer?"
    show aparty jabber
    a "Hahaha."
    a "Herrgott Sackerer!"
    a "Weiß nich. Sagt mein Papa immer so."
    show aparty n
    show oparty talk
    o "Ach sooo! Hab mich das auch schon gefragt."
    show aparty shock
    p "Warte, was?"
    show oparty vhappy at right with move
    show aparty jabber
    o "Ähh.. Ach so, hättest du das mal mich gefragt. Ich hätte das gewusst."
    hide oparty
    hide aparty
    show aodance
    show oadance
    n "Nachdem der Kuchen alle versöhnt hatte, haben wir noch ein wenig miteinander gespielt."
    n "Anja und Octavia haben sich sogar ausnahmsweise mal vertragen!"
    window hide
    $ renpy.pause()
    hide aodance
    hide oadance
    with dissolve
    window auto
    show rmum talk at center with moveinright
    rmum "Kommt mal alle zusammen für ein Gruppenfoto."
    n "Auch das noch! Na gut."
    rmum "Los alle. Käsekuchen!"
    scene cg selfieorca with dissolve
    "Alle" "Käääääseeeeekuuuuucheeeeen!"
    window hide
    $ renpy.pause ()
    window auto
    scene bg black with fade
    jump scene22
    
label scene22:
    scene bg street
    play music maintheme fadeout 1.0
    show car at rightish
    show dad talk at leftish 
    with dissolve
    v "Hi, [name]! Lang nicht mehr gesehen."
    p " PAPA!"
    v "Na, wie war die Feier? Cool, dass du schon neue Freunde gefunden hast."
    p "Nur ein paar Freunde! Ich bin ja noch neu!"
    p "Aber wir haben ein Gruppenfoto gemacht!"
    v "Hmmmh, ach das wird schon. Ach ich erinner mich noch an meine Zeit im Kindergarten."
    v "Damals, da haben wir immer ..."
    n "Papa erzählt gerne Geschichten von früher. Das ist meistens auch ganz spannend. Auf jeden Fall wird das keine langweilige Heimfahrt."
    
  
   ##### TAG 5 ENDE #####
            #JUMPER
  ##### TAG 6 BEGINN #####
    
label scenew2_0:
    scene bg black with fade
    show mnd with dissolve
    $ renpy.pause(0.6, hard = True)
    scene bg court
    play sound1 rain loop
    show pfütze
    show rainsplash
    show dad n at center
    show raindrops
    play sound cardoor2
    with fade
    p "Ihh! Regen!"
    v "Na nun hab dich nicht so, komm wir beeilen uns, dann bist du schneller im Trockenen!"
    n "Irgendwie ist es komisch Papa nur noch am Wochenende zu sehen."
    n "So, wie Papa jetzt ist, mag ich ihn fast lieber als früher."
    n "Er hat jetzt viel mehr Zeit für mich."
    n "Und ich seh ihn viel öfter... Auch wenn's nur am Wochenende ist."
    n "Und sein Auto ist auch viel cooler!"
    n "Trotzdem wäre es schön wenn er wieder bei uns einziehen könnte..."
    n "Immerhin machen wir jetzt mehr zusammen."
    show bananasplit at center with dissolve
    n "Und das extra große Eis bei Maluigi’s war echt lecker."
    hide bananasplit
    show dis gameboy 
    with dissolve
    n "Und ich hab' jetzt ein Vega PlayGear und ich darf es sogar mit in den Kindergarten nehmen."
    hide dis gameboy with dissolve
    n "Damit kam mir die Fahrt auch ganz kurz vor."
    n "Mit Mama dauert das irgendwie länger." 
    show dad talk
    v "Hat dir denn das Wochenende bei mir Spaß gemacht?"
    menu:
        v "Hat dir denn das Wochenende bei mir Spaß gemacht?"
        "Es war super!":
            p "Ja! Das war voll cool! Der Mega Playgear macht voll viel Spaß!"
            v "Na das wusste ich doch dass der dir gefallen wird [pre] Klein[suf2]."
            v "Du hast dir den doch schon so lange gewünscht. Wenn du mal was anderes möchtest, dann sag’s mir einfach, okay?"
            p "Mach ich! Danke Papa!"
            
        "War ganz gut.":
            p "Ja, danke Papa! Eigentlich bin ich ja lieber bei Mama, aber diesmal war es echt cool!"
            v "Das freut mich, ich weiß ja dass du lieber bei deiner Mama bist. Aber dein alter Herr ist doch auch ganz cool, oder?"
    
    
    scene bg flur
    stop sound1 fadeout 3
    show dad talk at center
    with fade
    v "Da wären wir, das ist also dein neuer Kindergarten… Du hast bestimmt viel Spaß, oder?"
    v "Hast du denn schon neue Freunde gefunden?"
    menu:
        v "Hast du denn schon neue Freunde gefunden?"
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
    v "Mach's gut mein Kleiner. Bis nächstes Mal!"
    hide dad with moveoutleft
    n "Und weg ist er auch schon wieder. Ich freue mich irgendwie schon, Mama später wieder zu sehen."
    
    
label scenew2_1:
    play music playtheme1 fadeout 1.0
    show anja hihi at center with moveinright
    a "Hallo [name]!"
    a "Sag mal, deine Haare sind ja nass! Hattest du keine Zeit sie zu trocknen?"
    p "Nein, es regnet do…"
    a "Also ich werde gar nicht erst mit nassen Haaren aus dem Haus gelassen. Meine Eltern meinen, ich könnte mich erkälten, dabei ist es ja bloß der Weg zum Auto."
    p "Aber ich komme vom Au…"
    a "Apropos Auto, dein Papa hat ja voll die coole Karre. Ich habe euch gesehen, als ihr hier angekommen seid. Der scheint ja mega viel zu verdienen!"
    p "Ja, er…"
    a "Mein Papa verdient nicht so viel, aber trotzdem kauft er mir immer wieder schöne Geschenke, wie neulich, da hat er mir…"
    n "Mit Anja zu reden macht manchmal wirklich keinen Spaß. Randy sitzt da drüben so alleine. Vielleicht hat er was Spannenderes zu erzählen."
    scene bg grura
    show karin go at center
    with fade
    n "Heute reden wir im Morgenkreis über Bauernhoftiere, wie z.B. Kühe, Schweine und Schafe."
    show dino at center with dissolve
    n "Nur warum können wir nicht lieber über coole Tiere wie Dinosaurier reden? Wen interessiert denn schon, dass eine Kuh \"muh\" macht?"
    n "Ich will wissen was ein T-Rex für ein Geräusch macht: Bestimmt \"rawr\" oder sowas..."
    
label scenew2_2:
    
    scene bg black with fade
    scene bg grura with dissolve
    n "Der Morgenkreis ist endlich vorbei!"
    n "Ich will endlich Fightë Møn weiter spielen! Ich mach die Arenen heute fertig!"
    n "Eigentlich will ich mir aber auch noch Maltipps von Eveylnn holen."
    n "Ich kann ja auch zu Hause weiter spielen."
    n "Hmmmh"
    menu:
        n "Also, was tun?"
        "Fightë Møn!":
            $ octa_points += 2
            play music octatheme fadeout 2.0
            n "Malen kann ich ja immer noch wann anders lernen."
            n "Erst sollte ich alle Arenen erledigen, wenn ich schon damit angefangen habe!"
            n "Außerdem hör ich eh schon die Musik..."
            n "Moment, die ist ja sogar da hinten wo Octavia sitzt."
            show octa happy with dissolve
            n "Sie hat einen blattsilbernen, limitierten PlayGear!"
            n "Ich zeig ihr mal meinen!"
            p "Hey Octavia!"
            show dis gameboy with dissolve
            p "Guck mal was ich auch habe!"
            o "Fightë Møn?"
            p "Ja."
            o "Weißt du..."
            p "Ja?"
            o "Das hab ich schon viel länger als du. Also bin ich auch besser." 
            p "Doch ich möchte [ddd] beste Ausbilder[suf3] der Welt werden! Genau wie im Fernsehen."
            o "Ich brauch nur noch eine handvoll an Monstern, dann bin ich das zuerst!"
            p "Du bist doch nicht besser nur weil du mehr Monster hast!"
            o "Ich beweis es dir! LOS, LASS KÄMPFEN!"
            n "Und schon hat Octavia ein Kabel in unsere PlayGears gesteckt. Um den Kampf komm ich wohl nicht drumrum."
            o "Warte."
            o "Wie lange hast du das Spiel schon?"
            p "Erst seit Randys Geburtstag..."
            o "Dann weißt du doch noch garnicht wie man gegen andere Spieler kämpft!"
            menu:
                o "Dann weißt du doch noch garnicht wie man gegen andere Spieler kämpft!"
                
                "Doch das weiß ich!":
                    o "Ach na dann..."
                    
                "Ähh...":
                    label monstererklärung:
                        if octaannoyed < 2:
                            o "..."
                            o "Dann lass es dir nochmal von der besten Ausbilderin erklären."
                            o "Das läuft ein bisschen anders als wenn du alleine spielst."
                            o "Zuerst musst du natürlich ein Monster zum Kampf aussuchen."
                            o "Und dann sagst du ihm was es tun soll."
                            o "\"Angriff\" ist angreifen. Nicht so stark aber zuverlässig."
                            o "\"Starker Angriff\" ist ein rücksichtloser Angriff. Der macht zwar mehr Schaden aber tut auch deinem Monster weh."
                            o "\"Verteidigen\" heißt du bekommst von meinem nächsten Angriff weniger Schaden. Aber du greifst auch nicht an."
                            o "Und mit \"Wechseln\" wechselst du dein Monster aus."
                            o "Alles klar soweit?"
                            menu:
                                o "Alles klar soweit?"
                                "Na klar!":
                                    o "Na dann..."
                                    
                                "Nochmal von vorn...":
                                    $ octaannoyed += 1
                                    jump monstererklärung
                        else:
                            $ octa_points -= 1
                            show octa mad
                            o "Sag mal versuchst du hier eigentlich nur Zeit zu schinden?"
                            o "Jetzt reicht es mir aber!"
            o "LOS!"
            jump startbattle
            
            
            label endbattle:
                play music octatheme fadeout 2.0
                if win == "yes":
                    $ octa_points += 2
                    scene bg grura
                    show octa shock
                    with fade
                    o "Wie? Ich hab doch fast alle."
                    o "Nein!"
                    n "Was ist denn jetzt los?"
                    show octa mad
                    o "Das Spiel ist eh Mist!"
                    o "Bei allem anderen würde ich dich haushoch besiegen!"
                    p "Dann schlag doch was vor."
                    show octa smug
                    o "Na gut."
                    o "Also wir machen immer so Wettrennen im Hof und da bin ich die Beste."
                    o "Einige sind gut, sicher. Andere sogar sehr gut, aber niemand hat mich bis jetzt besiegen können."
                    o "Und das wirst du auch nicht schaffen! Das kannst du mir aber glauben."
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
                    $ octa_points -= 2
                    scene bg grura
                    show octa smug
                    with fade
                    o "Hab ich's dir doch gesagt."
                    o "Bin eben viel besser als du. Dachte du hast eigentlich mehr drauf, aber ein echter Gegner bist du wohl nicht."
                    o "Lern erst einmal zu spielen!"
                    n "Octa ist gerade echt gemein..."
                    p "Hey!"
                    show octa talk
                    o "Was denn, Verlierer?"
                    p "Ach ich geh!"
                    show octa smug
                    o "Alles klar, viel Spaß noch!"
                    
        "Mit Evelynn malen.":
            play music evetheme fadeout 1.0
            $ eve_points += 2
            n "Ich kann ja auch noch Nachmittag daheim spielen, erst einmal zu Evelynn!"
            n "Der Maltisch ist wohl heute wirklich voll. Randy hat sich wohl alle Brettspiele geschnappt."
            scene bg grura2
            show eve draw
            with fade
            n "Was malt die denn da?"
            window hide
            show mantikoreve with fade
            pause 0.75
            hide mantikoreve with fade
            window auto
            #$ renpy.block_rollback() #JUMPER
            n "Ich kann gar nichts sehen. Die Anderen standen im Weg!"
            n "Aber es sah interessant aus, vielleicht kann ich es ja nachzeichnen!"
            n "Ich probier es mal."
            n "Erst einmal der Hintergrund!"
            scene memory bg
            
            n "Sooo, aber welche Farbe hatte das Tier?"
            
            menu:
                n "Sooo, aber welche Farbe hatte das Tier?"
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
                n "Moment, was war es überhaupt für ein Tier?"
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
            n "Welchen Schwanz hat das Tier?"
            menu:
                n "Welchen Schwanz hat das Tier?"
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
                n "Egal, Flügel!"
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
                $ eve_points += 5
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
                $ eve_points -= 1
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
    play music happytheme1 fadeout 1.0
    scene bg grura
    show randy talk at center
    with fade
    r "[name]!"
    n "Was will denn Randy von mir?"
    r "Lust auf eine Runde Oligopoly? Wir brauchen noch jemanden um Zwei gegen Zwei zu spielen!"
    n "Oligopoly ist super."
    p "Auja, da bin ich dabei! Bin nur noch nicht wirklich gut."
    show randy happy
    r "Dann bist du eben in meinen Team, ich kenne die Tricks."
    scene bg grura2
    show randy happy at center
    with fade
    r "Das sind wieder 200!"
    p "Randy und ich sind wohl ein echt gutes Team, noch ein bisschen und wir haben das in der Tasche."
    show mum talk at left with moveinleft
    m "Hallo, mein Schatz!"
    p "Och nööö."
    n "Wir haben doch nicht gar nicht so lange gespielt!"
    m "Nööö was?"
    show mum mad
    p "Ich war nur gerade am gewinnen und jetzt bist du da."
    show mum talk
    m "Ach so, aber dann hat's dir doch Spaß gemacht. Und wie war dein Wochenende beim Papa?"
    n "Ich zeig ihr einfach was Papa mir geschenkt hat."
    show dis gameboy with dissolve
    show mum vmad
    m "DAS KANN NICHT SEIN ERNST SEIN!"
    hide dis gameboy with dissolve
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
    play music playtheme1 fadeout 1.0
    scene bg black with fade
    show tue with dissolve
    $ renpy.pause(0.6, hard = True)
    scene bg grura
    play sound child1
    with fade
    n "...oder auch nicht. Wieso wurde alles aufgeräumt?"
    show karin go at center with dissolve
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
    show karin yoga with moveinbottom
    n "Was macht Karin da jetzt auf den Boden?"
    k "Das nennt man Yoga! Puuh."
    k "Alle gesehen? Da könnt ihr euch richtig austoben!"
    n "Na gut, dann linker Fuß nach hinten..."
    scene bg black with dissolve
    k "So, die dritte Übung ist die Folgende..."
    k "..."
    k "Genau, so wie bei Octavia!"
    o "ist auch voll leicht."
    k "Nun, weiter..."
    n "..."
    play music maintheme fadeout 1.0
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
    n "Vielleicht hat ja Evelynn Lust was zu..."
    show karin shock at rightish
    show eve talk2 at leftish
    with dissolve
    k "Evelynn, tut mir Leid. Das ist die letzte Kreide."
    e "Danke Karin."
    hide karin
    hide eve
    with dissolve
    n "Ahh, also keine Kreide mehr für mich ..."
    n "Dann muss ich wohl anderswo mitmachen, aber wo?"
    n "Octavia ruft gerade alle zum Ball spielen zusammen."
    n "Louis und Randy sitzen im Sandkasten. Wenn ich schnell genug bin spielen die vielleicht lieber mit mir als mit Octavia."
    n "Mit wem spiel ich denn jetzt?" #JUMPER

    menu:
        n "Mit wem spiel ich denn jetzt?"
        "Mit Louis und Randy im Sandkasten!":
            n "Mal sehen, was die zwei da so machen!"
            jump scenew2_5

        "Mit Octavia und den Anderen Ball!":
            $ anja_points += 2
            $ octa_points += 2
            scene bg ball
            n "Wenn jeder spielt, dann muss ich wohl auch mitmachen."
            jump startballgame
            
label scenew2_5:
    window hide
    play music happytheme2 fadeout 1.0
    scene bg sand
    show burg
    show sandauto
    show sandkuchen
    show sandpyramide
    with fade
    $ scastlep = 0
    pt "Hey, Louis!"
    Lt "Oh, hi [name], willst du mitmachen?"
    pt "Ja! Viel besser als Ball spielen! Moment ..."
    pt "Bei was denn?"
    Lt "Na, wir spielen Geschichten erzählen."
    pt "Wie spielt man denn etwas zu erzählen?"
    Lt "Wie, das weißt du nicht?"
    Lt "Na gut, okay ich erklärs."
    Lt "Also ich fange einen Satz an und du vervollständigst den dann. Und da wird dann eine Geschichte draus."
    Lt "Schau ich hab hier zum Beispiel ein Schloss gebaut."
    nt "Naja, ob das wie ein Schloss aussieht... Wie hat er es überhaupt geschafft, dass das so schief steht."
    nt "Ist das ... Haargel in dem Sand?"
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
        "Äh... Schloss... äh... Sand... gel.":
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
            
        "Ich weiß nicht. Mir fällt nichts ein... vielleicht... Fort... Knight?":
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
    Lt "Ähh... sie drei Teile eines magischen Schlüssels erhalten."
    Lt "Ihre Reise beginnt also. Als Erstes müssen sie..."
#JUMPER
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
        "...mit dem magischen Aut...äh..pferdelosen Wagen gegen das schnellste Pferd des Landes behaupten.":
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
            
    Lt "Super! Bis jetzt haben sie alle Prüfungen bestanden. Aber die letzte Prüfung soll auch die Härteste sein, denn …"
    
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
            with Movetransition(1.0)
            Lt "Die Helden suchen Fürst Randolph auf, weil jeder weiß, dass er einen Teil des Schlüssels besitzt."
            Lt "Randolph will aber ihn aber nicht einfach so hergeben. Er stellt ihnen eine Aufgabe. Wenn sie ein Stück seines unglaublich trockenen Kuchen verspeisen können ohne zu Staub zu zerfallen, dann gibt er ihnen sein Schlüsselstück.."
            show sandkuchen2 
            hide sandkuchen with dissolve
            Lt "Die Helden schaffen es nur zu dritt, in dem sie das Stück genau unter sich aufteilen."
            Lt "Fürst Randolph ist beeindruckt und gibt den letzen Teil des Schlüssels frei."
            
    Lt "Okay, jetzt kommt das große Finale!"
    Lt "Nach diesen schweren Prüfungen erreichen die Helden endlich die [burg]."
    Lt "Noch sind die großen schweren Tore verschlossen. Aber mit den drei Schlüsselstücken öffnen sie sich."
    show burg behind badboy with dissolve
    show badboy at center
    show wizzard at center
    show knight at center
    show held at center
    with MoveTransition(1.5)
    Lt "Im Innenhof der Festung treffen die Helden nun endlich auf den [enemy]. Ein schwerer Kampf steht bevor. Der [enemy] schafft es fast die Helden zu überwältigen, aber am Ende besiegen sie ihn…"
    
    
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
            show duck behind badboy with dissolve
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
        Lt "Ist ja fast als würde man mit Evelynn spielen."
        Lt "Habt ihr euch vorher abgesprochen was du mir erzählen sollst?"
        pt "Häh, nee, wieso das denn?"
        Lt "Weil du fast so gute Ideen hast wie sie!"
        Lt "Vielleicht macht sie ja das nächste Mal auch mit."
        
    else:
        Lt "..."
        Lt "Ich glaube das mit den Geschichten übst du nochmal."
        pt "Häh, wieso das denn?"
        Lt "..."
        Lt "Vielleicht zeigt dir Evelynn mal wie das richtig geht."
        Lt "Dann spielen wir drei mal zusammen!"
            
            
            
            
            
    window auto
    
label scenew2_6:
    play music playtheme1 fadeout 1.0
    scene bg grura2
    show karin n at right
    with fade
    n "Hmmh... Meine Mama müsste mich eigentlich schon lange abgeholt haben..."
    n "Wo bleibt die nur?"
    n "Die anderen wurden alle schon abgeholt, doch wieso sitze ich noch hier und muss warten?"
    n "Wenigstens ist Karin noch da."
    show karin talk
    k "[name]?"
    p "Was ist Karin?"
    k "Hat deine Mama dir gesagt ob Sie heute später kommt?"
    p "Nein, eigentlich kommt sie nie zu spät..."
    show karin mad
    k "Ich muss deswegen leider auch warten bis du abgeholt wirst... Weißt du ich hab' auch Kinder zu Hause."
    show karin shock
    k "Aber du kannst ja nichts dafür."
    show karin talk
    k "Das nächste mal, wenn Sie sich so sehr verspätet soll sie bitte den Kindergarten anrufen."
    k "Aber das kann ich ihr dann wohl auch selbst sagen, keine Sorge. Jetzt warten wir einfach zusammen."
    scene bg black with fade
    k "Die ist bestimmt bald da."
    n "..."
    scene bg grura
    show karin mad at center
    with fade
    n "Endlich!"
    show mum n at right with moveinright
    m "Na mein Schatz? Du wartest sicherlich schon ewig hier, oder? Tut mir leid, aber lass uns gleich nach Hause gehen!"
    show mum mad
    m "Tut mir Leid Karin, ich bin einfach nicht mit der Arbeit fertig geworden und konnte es auch nicht aufschieben."
    k "Kein Problem, dass kann zwar passieren aber, bitte geben Sie mir vorher Bescheid oder rufen Sie mich an."
    k "Ich konnte Sie auch nicht erreichen, als ich versucht habe Sie anzurufen."
    m "Also..."
    k "Das ist nicht nur nervig für mich, sondern stresst auch ihr Kind."
    show mum vmad
    k "Ich bin ja schließlich auch an Sie gebunden und verpflichtet zu bleiben, bis alle Kinder abgeholt wurden."
    k "Außerdem warten meine Kinder und mein Mann auf mich."
    show mum talk
    m "Sie haben ja Recht."
    p "Können wir endlich gehen?"
    show mum happy
    m "Natürlich!"
    m "Auf Wiedersehen!"
    scene bg black with dissolve
    hide mum
    hide karin
    n "Mama sieht heute auch irgendwie so müde aus."
    p "Willst du schlafen gehen Mama?"
    m "Nichts lieber als das, also heute."
    p "Aber kannst du damit noch bis zu Hause warten?"
    m "Haha, aber natürlich Schatz."
    p "Ich bin auch müde!"
    m "Na dann halten wir nachher ein Nickerchen zusammen ..."
    
label scenew2_7:
    play music maintheme fadeout 1.0
    scene bg black with fade
    show wed with dissolve
    $ renpy.pause(0.6, hard = True)
    scene bg street
    play sound audio.cardoor1
    show mum n at center
    with fade
    n "Es ist schon wieder ein neuer Tag, ich bin gespannt wie es heute wird!"
    n "Moment."
    p "Mama, wieso steigst du mit aus?"
    show mum talk
    m "Hmmh?"
    m "Ach, ich wollte nur mal mit reinschauen."
    show mum n
    n "Mann, bin ich heute müde!"
    n "Ich kann kaum die Augen offen halten."
    n "Dabei haben wir doch extra gestern das Nickerchen gemacht..."
    show mum talk
    m "Schatz. Sag mal. Wie ist es eigentlich hier im Kindergarten?"
    m "Sind alle nett zu dir und hast du mittlerweilie auch schon andere Freunde außer Randy kennengelernt?"
    p "Was?"
    n "Ich kann mich gar nicht darauf konzentrieren, was Mama sagt."
    scene bg flur
    show mum talk at center
    with fade
    p "Warum bist du eigentlich reingekommen? Ich finde doch selbst den Weg. Bin ja kein Baby mehr!"
    show mum happy
    m "Ach, ich wollte nur kurz mit Karin reden."
    n "Was will die mit Karin bereden?"
    show mum n
    m "Hab einen schönen Tag und spiel diesmal nicht mit deinen Videospiel-Teil!"
    hide mum with moveoutright
    n "Und weg ist sie im Nebenzimmer, was die wohl besprechen?"
    n "Hah! Ich hör einfach mal zu!"
    scene bg office
    show mum talk at leftish
    show karin n at rightish
    with fade
    m "...kann ich gut verstehen. Und hat sich [name] schon mit anderen Gleichaltrigen angefreundet?"### Flagge und Affinitycheck
    
#JUMPER
    if anja_points >= eve_points and anja_points > octa_points:
        show karin talk
        k "Ihr [name] ist hier gut aufgehoben und passt wunderbar in unsere bunte Gruppe."
        k "Am meisten ist [name] mit Anja unterwegs."
        k "Die beiden sind ständig am Quatschen!"
        k "Wobei Anja ehrlich gesagt viel mehr redet als [name]."
        show mum happy
        k "Aber die beiden zusammen wirken recht augeweckt."
        show karin n
        m "Und was ist diese Anja für ein Typ?"
        k "Oh Anja. Das ist eine ga... und außerdem..."
        scene bg black with dissolve
        n "Nanu!"
        scene bg office
        show mum mad at leftish
        show karin go at rightish
        with fade
        k "Nun, sie --- relativ neu. Es macht Sinn, dass die beiden --- kommunikativ und gut im Zuhören."
        k "Am Freitag werde---"
        show mum happy
        show karin n
            
    elif eve_points > anja_points and eve_points > octa_points:
        show karin talk
        k "Ihr [name] ist ein wirklich kreatives Kind, weswegen es kein WUnder ist, dass [pro2] sich so gut mit Evelynn versteht."
        k "Die beiden sind ständig am Maltisch und produzieren ihre kleinen Kunstwerke."
        show karin go
        k "Evelynn ist ein Naturtalent und manchmal frag ich mich, ob Sie besser malen kann als ich. Zumindest was Beleuchtung angeht."
        k "[name] hat sich deshalb auch unter ihrer Kritik künstlerisch stark verbessert."
        show mum happy
        m "Das ist ja gut. Und was für ein Typ ist diese Evelynn?"
        k "Musikalisch talentiert, künstlerisch sehr talentiert, aber--- "
        scene bg black with dissolve
        n "Nanu!"
        scene bg office
        show mum mad at leftish
        show karin go at rightish
        with fade
        k "Leider ein --- zurück--- Mädchen. Beidenehmen---Freundschaft mit, denn--- Kokon heraus."
        k "Am Freitag werde..."
        show mum happy
        show karin n
        
    elif octa_points >= anja_points and octa_points >= eve_points:
        show karin go
        k "[name] ist wirklich sehr ergeizig und gibt sich mit allem was er macht wirklich mühe."
        k "Das ist schon bemerkenswert für [pro] Alter, deswegen wundert es mich auch nicht, dass [pro2] sich mit den, wie soll ich sagen, Musterkind Octavia angefreundet hat."
        show karin n
        show mum mad
        m "Hmmmh..."
        m "Und was ist diese Octavia für ein Typ?"
        show karin happy
        k "Ein richtiger Engel. Unkompliziert! Aber wenn --- Spiele--- nur einen Hauch von Wettbewerb."
        scene bg black with dissolve
        n "Nanu!"
        scene bg office
        show mum mad at leftish
        show karin go at rightish
        with fade
        k "...deshalb ist es gut, dass [name] jetzt hier ist --- jemandern der [pro2] fordert."
        k "Deshalb, werde ich am Freitag..."
        show mum happy
        show karin n
            
            
    else:
        #$boo = True
        show karin shock
        k "Leider scheint [pro2] ja eher zurückgezogen zu sein. Zwar bemüht sich Ihr Kind immer wieder, aber so richtig klappen will es scheinbar nicht. Zumindest, soweit ich das beurteilen kann." 
        k "Wenn Sie wollen, werde ich Freitag mal ein genaueren Blick auf [pro5] werfen."            
        show mum talk
        m "Was ist denn am Freitag?"
        show karin talk
        show mum n
        k "Ich dachte, Frau Heidenau hätte allen Eltern Bescheid gegeben, dass wir zur Bernerhütte im Eichelgebirge fahren und dort im Wald wandern."
        show mum talk
        m "Ein Wandertag also? Nein, davon habe ich nichts gehört."
        show karin shock
        k "Entschuldigen Sie vielmals. Möchten Sie denn, dass ihr Kind mitkommt? Bis auf eine Brotzzeit und etwas zu trinken wird [pro2] nicht brauchen."
        m "Bei mir spricht eigentlich nichts dagegen, wann genau muss ich mein Kind dann abholen?"
        show karin vhappy
        k "Es könnte etwas später werden, wohl etwa gegen 17 Uhr vermutlich..."
        n "Wieso sagt mir denn niemand von einen Wandertag!"
        jump secenew2_8
        
            
    n "Ich versteh gar nichts mehr, wieso sind die soweit weg von der Tür aufeinmal."
    n "Ich schleich mal ein Stück näher ran."
    show mum talk
    m "Was ist denn am Freitag?"
    show karin talk
    show mum n
    k "Ich dachte, Frau Heidenau hätte allen Eltern bescheid gegeben, dass wir zur Bernerhütte im Eichelgebirge fahren und dort im Wald wandern."
    show mum talk
    m "Ein Wandertag also? Nein, davon habe ich nichts gehört."
    show karin shock
    k "Entschuldigen Sie vielmals. Möchten Sie denn, dass ihr Kind mitkommt? Bis auf eine Brotzzeit und etwas zu trinken wird [pro2] nichts brauchen."
    m "Bei mir spricht eigentlich nichts dagegen, wann genau muss ich mein Kind dann abholen?"
    show karin vhappy
    k "Es könnte etwas später werden, wohl etwa gegen 17 Uhr vermutlich..."
    n "Ein Wandertag! Cool!"
    n "Wieso erzählt mir denn niemand von einen Wandertag?"
    
label scenew2_8:
    play music octatheme fadeout 1.0
    scene bg grura
    show karin mhappy
    with fade
    k "So Kinder, für heute sind wir erst einmal fertig!"
    k "Dann viel Spaß beim Spielen!"
    hide karin with dissolve
    n "Was soll ich denn nach dem Morgenkreis machen? Ich weiß nie was ich machen will..."
    r "Hey [name]!"
    n "Randy kommt in meine Richtung, will der vielleicht spielen?"
    show randy talk at rightish with moveinright
    r "Wir wollen Verstecken spielen, wir brauchen noch jemand der suchen will."
    r "Hast du Lust mitzumachen?"
    
    menu:
        r "Hast du Lust mitzumachen?"
        "Ja klar!":
            p "Ja, klar! Ich weiß eh nicht was ich machen soll."
            show randy happy
            r "Alles klar!"
            
        "Können wir nicht was anderes machen?":
            p "Auf Verstecken hab ich eigentlich keine Lust."
            p "Aber ich bin mir auch nicht wirklich sicher was ich sonst machen will..."
            show randy shock
    
    play sound whoosh3
    show papierflieger at flight with moveinleft
    hide papierflieger with moveoutright
    play sound ballhit1
    p "AUAA! Mein Auge!"
    p "Das war gemein, wer war das?"
    o "TUT MIR LEID!"
    show octa happy at leftish with moveinleft
    n "Jetzt kichert sie. Aber das ist überhaupt nicht lustig!"
    p "Was sollte denn das!"
    show octa smug
    o "Jetzt stell dich doch nicht so an, ich hab mich doch schon entschuldigt!"
    o "Wenn du willst, dann darfst du auch Einen zurückwerfen. Oder wir machen einen Wettbewerb daraus!"
    o "Meine Papierflieger sind eh die Besten."
    show randy talk
    r "Wenn du willst, kannst du auch versuchen gegen Sie zu gewinnen!"
    n "Hmmh, Papierflieger basteln oder verstecken spielen?"
    
    menu:
        n "Hmmh, Papierflieger basteln oder verstecken spielen?"
        "Verstecken spielen":
            $ octa_points -= 1
            $ seek = True
            $ paper = False
            p "Ne, ich wollte eigentlich schon lieber verstecken spielen. Papierflieger sind mir egal!"
            show octa shock
            show randy happy
            o "Was?"
            r "Super."
            o "Na gut, dann halt nicht."
            jump suchen
            
        "Papierfliegerwettbewerb":
            $ octa_points += 1
            $ paper = True
            $ seek = False
            p "Also Papierflieger hört sich schon lustig an."
            show randy happy
            r "Ich hab auch irgendwie Lust drauf!"
            show octa vhappy
            o "Wird sicher lustig euch zu besiegen."
            p "Werden wir ja sehen."
            jump wettbewerb
        
        
label wettbewerb:
    scene bg bastel with dissolve

    n "Ich will unbedingt einen besseren Flieger als Octavia bauen!"
    n "Doch wie soll mein Papierflieger am besten aussehen, damit ich Sie besiege?"
    n "Wie falte ich so ein Ding überhaupt?"
    
    menu:
        
        "Erstmal in der Mitte falten":
            n "Erst einmal das Ding in der Mitte machen, dass haben ja alle Flieger!"
            n "Dann noch die Flügel, doch wie soll ich die Flügel machen?"
            
            menu:
                n "Dann noch die Flügel, doch wie soll ich die Flügel machen?"
                "Breit":
                    $ dynamik = True
                    n "Zum Gewinnen braucht es viel Luft und Wind, deswegen sind wohl Breite Flügel klüger!"
                    scene bg black with dissolve
                    n "Dann noch hier etwas."
                    n "Eine Kante noch."
                    n "Ne moment."
                    n "Hab ich irgendwas vergessen? Ach was!"
                    n "Fertig!"
                    
                    
                "Schmal":
                    n "Wenn er dünner ist, dann kann ich ihn schneller werfen und so komm ich sicher weiter als Octavia!"
                    scene bg black with dissolve
                    n "Jawohl, so wirds gemacht!"
                    n "Klassisch."
                    n "Also eigentlich."
                    n "Eigentlich bin ich ja fertig!"
                    
            
        
        "Die Spitze muss super werden!":
            $ tip = True
            n "Ich habe mal gehört, dass die Spitze das Wichtigste ist."
            n "Wenn das stimmt, gewinne ich hunderprozentig!"
            n "Freu ich mich schon auf Octavias Gesicht!"
            n "Jetzt fehlt aber noch was!"
            n "Ach ja!"
            
            menu:
                n "Das fehlt noch!"
                "Farbe":
                    $ farbflug = True
                    n "Ich muss Octavia auch mit Stil besiegen!"
                    scene bg black with dissolve
                    n "Dann mal los, ich hab ja hier die ganzen Farben."
                    n "Etwas Orange und Gelb."
                    n "Fert... Moment, Flügel!"
                    n "So, dass wird schon hinhauen."
                    n "Jetzt aber wirklich, fertig!"
                    
                "Breite Flügel":
                    $ dynamik = True
                    n "Zum Gewinnen braucht es viel Luft und Wind, deswegen sind wohl Breite Flügel klüger!"
                    scene bg black with dissolve
                    n "Dann noch hier etwas."
                    n "Eine Kante noch."
                    n "Nee, Moment."
                    n "Hab ich irgendwas vergessen? Ach was!"
                    n "Fertig!"                   

                                                                         
        
        "Einfach loslegen!":
            $ chaos = True
            n "Ach, dass wird schon irgendwie klappen."
            scene bg black with dissolve
            n "Erst einmal etwas hiervon. Etwas davon."
            n "Nein, nein so nicht, nochmal zurück."
            n "Geht das noch?"
            n "Einfach in die Form eines Flugzeugs bringen."
    
    
    scene bg grura2
    show octa happy at rightish
    with fade
    n "So, fertig. Sieht doch ziemlich cool aus!"
    n "So, Octavia hat gesagt ich darf zurückwerfen. Das mache ich jetzt einfach!"
    n "Sie faltet gerade auch einen Flieger, also gut zielen und ..."
    p "LOS!"
    
    if chaos == True:
        $ octa_points -= 2
        show papierkneul at flight with moveinleft
        show octa shock
        hide papierkneul with moveoutbottom
        n "Oh Mist, dass ist ja gar nichts!"
        n "Hat das wer gesehen?"
        n "Sie scheint nicht zu wissen, dass der von mir kam ..."
        n "Ich will nicht ausgelacht werden..."
        n "Ich glaube... Ich glaube ich verstecke mich lieber für heute."
        scene bg cuddle with dissolve
        n "Hier findet mich heute niemand mehr."
        n "Erst wenn Mama kommt."
        n "Das dauert hoffentlich nicht mehr lang."
        scene bg black with dissolve
        n "..."
        n "*schnarch*"
        n "Oh mann, Mama ist schon da?"
        jump scenew2_9
        
    elif dynamik == True:
        show papierflieger_stromlinienförmig at flight with moveinright
        show octa shock
        hide papierflieger_stromlinienförmig with moveoutleft
        
    elif farbflug == True:
        show papierflieger_bunt with moveinright
        show octa shock
        hide papierflieger_bunt with moveoutleft
        
    else:
        show papierflieger with moveinleft
        show octa shock
        hide papierflieger with moveoutright
    
    
    n "Zwar getroffen, aber nicht richtig."
    o "Was soll denn..."
    show octa smug
    o "Ach du warst das!"
    o "Das war nicht schlecht. Aber mein Flieger ist trotzdem viel besser als alle Anderen hier!"
    o "Wollen wir schauen wessen Flieger am Weitesten fliegt?"
    n "Oh, wie es aussieht sind da noch mehr Leute die mitmachen."
    n "Anja hat ihren angemalt, Randy hat einen wahren Klassiker und Evelynn ..."
    show origami at flight with dissolve
    n "Ein Vogel? WOW! Der kann sicher fliegen solange es kein Pinguin ist!"
    hide origami dissolve
    o "Kommt mal alle ran, wir werfen unsere Flieger hintereinander und wer am Weitesten kommt gewinnt!"
    show anja hihi at left with moveinleft
    a "Alles klar!"
    hide anja with moveoutleft
    show randy vmad at left with moveinleft
    r "Dann zeig ichs dir Octavia!"
    hide randy with moveoutleft
    o "So, alle bereit?"
    hide octa with moveoutright
    o "Ich werfe als Erste und dann schaut ihr ob ihr auch so weit kommt!"
    show papierflieger_stromlinienförmig at flight with moveinright
    hide papierflieger_stromlinienförmig with moveoutleft
    show papierflieger_bunt at flight with moveinright
    hide papierflieger_bunt with moveoutleft
    a "Fast!"
    o "Hey! Ich hab gesagt nacheinander!"
    show papierflieger at flight with moveinleft
    hide papierflieger with moveoutright
    p "Randy?"
    o "Randy das war die falsche Richtung!?"
    n "Dann bin nurnoch ich übrig!"
    
    if dynamik == True and tip == True:
        $ anja_points += 3
        $ octa_points += 2
        show papierflieger_stromlinienförmig at flightright with moveinright
        hide papierflieger_stromlinienförmig with moveoutleft
        n "WOOOAH!"
        show octa shock at center with dissolve
        a "[name] ist weiter als Octavia!"
        r "Ich glaubs nicht!"
        o "Aber... nur um ein paar Zentimeter!"
        o "Außerdem hat Randy mich abgelenkt."
        show randy shock at left with moveinleft
        r "Ich hab was?"
        o "Beim nächsten Mal gewinne ich!"
    
    elif dynamik == True:
        $ anja_points += 3
        $ octa_points += 1
        show papierflieger_stromlinienförmig at flight with moveinright
        hide papierflieger_stromlinienförmig with moveoutleft        
        p "So knapp!"
        show octa smug at center with dissolve
        o "Nicht schlecht."
        show anja happy at left with moveinleft
        a "Noch mal, dann gewinnst du sicher [name]!"
        o "Niemals! Ich verliere nie!"
        o "Aber ich hab auch nicht wirklich Lust das nochmal zu machen. Mir reicht einmal gewinnen."
        n "Hmmh..."
    
    elif farbflug == True:
        $ anja_points += 2
        $ octa_points += 1
        $ eve_points += 2
        show papierflieger_bunt at flight with moveinright
        hide papierflieger_bunt with moveoutleft
        p "So knapp!"
        show octa smug at center with dissolve
        o "Nicht schlecht."
        show anja happy at left with moveinleft
        a "Noch mal, dann gewinnst du sicher [name]!"        
        o "Niemals! Ich verliere nie!"
        o "Aber ich hab auch nicht wirklich Lust das nochmal zu machen. Mir reicht einmal gewinnen."
        o "Naja, bis dann ihr Verlierer!"
        hide octa with moveoutright
        n "Und da ist sie weg."
        show eve happy2 at center with dissolve
        e "Du [name], ich mag deinen Flieger."
        p "Du hast einen ganzen Vogel gemacht, kannst du mir zeigen wie das geht?"
        show eve vhappy2
        e "Ja sehr gerne, zunächst must du..."
    
    else:
        $ anja_points += 1
        $ octa_points -= 2
        $ eve_points += 2
        show papierflieger2 at flight with moveinright
        hide papierflieger2 with moveoutleft
        p "Hmmmh."
        show octa smug
        o "Sag ichs doch."
        r "Was will man denn erwarten."
        o "Genau, meiner ist der Beste. Hab ichs euch doch gesagt. Ich mach dann mal was anderes."
        hide octa with moveoutright
        n "Hmmh."
        p "Du Evelynn, wie hast du eigentlich einen ganzen Vogel gemacht?"
        e "Das ist einfach, zunächst must du..."
    
    k "[name]!"
    n "Nanu?"
    show karin talk at right with moveinright
    k "Deine Mutter wartet draußen, die ist heute etwas früher da."
    p "Oh."
    p "Okay, komme sofort!"
    scene bg flur
    show karin talk at center
    with fade
    k "Ja, dann helf ich dir schnell beim anziehen und..."
    p "Ich kann das aber schon alleine!"
    k "Ach na dann, dann mach mal. Bis morgen [name]!"
    hide karin with moveoutright
    n "Hier sind meine Schuhe und meine Jacke."
    n "Ach mann, wenn Schuhe nicht sooo..."
    n "Ich brauch wieder Klettverschluss..."
    
    


  
    
    
label scenew2_9:
    play music happytheme1
    show bg street with dissolve
    show mum talk at rightish
    m "Hallo mein Schatz! Wie ist es denn gelaufen? Hattest du einen schönen Tag?"
    p "Ähhm. Ja."
    m "Was hast du denn heute so gemacht?"
    
    if paper == True:
        p "Flieger gebastelt!"
        p "Also, aus Papier."
        p "Und dann haben wir uns abgeworfen, dass war lustig."
        show mum happy
        p "Das müssen wir daheim auch mal machen!"
        p "Zeig mir wie du das machst!"
    
    elif seekwin == True:
        p "Wir haben heute alle zusammen Verstecken gespielt und ich musste suchen." 
        p "Ich musste die Augen zu machen, dann drei mal bis 20 zählen und ich hab gewonnen."
        show mum happy
        p "Alle gefunden!"
        
    else:
        p "Wir haben heute alle zusammen verstecken gespielt und ich musste suchen." 
        p "Ich musste die Augen zu machen, dann drei mal bis 20 zählen und dann suchen."
        show mum n
        p "Konnte Sie aber nicht alle erwischen, ich war zu langsam und dann sind Sie aus ihren Verstecken gekommen."
        p "Leider verloren."

    show mum talk
    m "Naja, hört sich ja nach einer schönen Zeit an!"
    m "Ich muss dir noch etwas sagen: Wusstest du, dass ihr am Freitag einen Wandertag habt?"
    n "Ja! Aber Mama darf nich wissen, dass ich gelauscht hab..."
    p "Ähm, nein..."
    show mum happy
    m "Ich hab dich gleich mal angemeldet, dass wird sicher toll."
    m "Du wirst da ganz viel Spaß haben."
    p "Du hast mich angemeldet?"
    p "Und wenn ich garkeine Lust habe?"
    show mum talk
    m "Sei mal nicht so. Wandertage sind immer schön, durch die gegen mit deinen Freunden laufen, ein bisschen Erkunden und spielen!"
    m "Ich mochte die immer."
    show mum happy
    p "Ich mach ja auch nur Spaß, ich freu mich schon auf morgen!"
    
label scenew2_10:
    scene bg black with fade
    show thr with dissolve
    $ renpy.pause(0.6, hard = True)
    scene bg grura2
    show karin talk at slightright
    show octa smug at slightleft
    with fade
    n "Heute ist der Morgenkreis sehr lustig. Wir spielen \"Reise nach Jerusalem\". Das macht Spaß."
    n "Aber Octavia gewinnt dauernd. Gegen die hat echt keiner eine Chance!"
    scene bg flur with dissolve
    n "Mhh… ich hab mir noch gar nicht überlegt, was ich danach heut eigentlich machen will..."
    scene bg grura
    show randy vhappy at slightleft
    show louis really at slightright
    with fade
    n "Randy spielt schon wieder mit Louis Oligopoly."
    n "Laaaangweilig…"
    n "Vielleicht schau ich lieber mal nach, was die Anderen gerade so machen."
    scene bg flur with dissolve
    n "Octavia ist vorhin direkt nach draußen gerannt und Anja ist da wahrscheinlich auch irgendwo Klettern. Nur wo Evelynn ist weiß ich gerade nicht, aber die malt bestimmt wieder."
    ##############################################################JUMPER
    menu:
        n "Octavia ist vorhin direkt nach draußen gerannt und Anja ist da wahrscheinlich auch irgendwo Klettern. Nur wo Evelynn ist weiß ich gerade nicht, aber die malt bestimmt wieder."
        "Ich sollte mal nach Octavia schauen.":
            play music octatheme fadeout 1.0
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
                    $ octa_points += 3
                    $ anja_points += 1
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
                            $ octa_points += 2
                            $ anja_points += 1
                            jump runokay
                            
                        "Nö.":
                            $ octa_points -= 4
                            $ anja_points -= 1
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
                    $ octa_points -= 5
                    $ eve_points += 3
                    $ anja_points += 3
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
                    $ octa_points += 5
                    $ eve_points -= 3
                    $ anja_points -= 3
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
            jump scenew2_12
            
                
                
        "Ich glaub ich geh mal zu Anja.":
            n "Heute ist es echt schön warm draußen!"
            n "Und natürlich hängt Anja wieder im Baum. Wie so einer dieser orangenen Affen. Die hab ich mal im Zoo gesehen."
            a "[name]! Draußen ist es doch echt am coolsten, oder?"
            a "Außerdem sagt meine Mama immer, dass frische Luft gesund ist. Nur die Luft auf dem Land soll noch besser sein. Meine Oma und mein Opa zum Beispiel wohnen auf dem Land. Die haben einen ganz eigenen Bauernhof!"
            
            menu:
                "Das ist ja echt cool!":
                    $ octa_points -= 1
                    $ eve_points += 1
                    $ anja_points += 2
                    p "Ich fin-"
                
                "Ich finde es in der Stadt besser als auf dem Land.":
                    $ octa_points += 1
                    $ eve_points -= 1
                    $ anja_points -= 2
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
                    $ anja_points += 2
                    
                "Nichts schmeckt besser als Mamas Kekse!":
                    p "Das klingt-"
                    $ anja_points -= 2
                    
            a "Aber die Tiere sind trotzdem das Coolste! Ich will später auch mal irgendwas mit ganz viel Tieren machen. Aber nicht Bauer."
            a "Lieber Tierarzt oder so. Dann kann ich den ganzen Tieren helfen und dann werden die alle meine Freunde. Aber niemand wird ein besserer Freund als unsere Kuh Elsa. Die ist die Allerbesteste!"
            a "Was ist denn- Komm auch hoch! Das musst du sehen! Schnell!"
            menu:
                "Ich kann da nicht hochklettern.":
                    $ anja_points -= 2
                    a "Jetzt komm schon! Du verpasst es!"
                
                "Ich beeil mich.":
                    $ anja_points += 2
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
                    $ anja_points += 2
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
                    $ anja_points -= 2
                    p "Lass uns was anderes Spielen. Das ist doof!"
                    a "Ist ja schon gut, aber ich sag‘s dir! Irgendwann wird sie dich fressen und dann bist du froh, wenn du mich hast!"
                    p "Das werden wir dann sehen!"
                    n "Anja kommt jetzt auch runter und schaut mich kurz fragend an. Ich hab mir noch gar nichts überlegt, was wir stattdessen machen können..."
                    
            p "Lass uns doch lieber schnell wippen gehen."
            n "Die Schlangenwippe ist echt lustig. Aber irgendwie ist Anja nicht bei der Sache."
            a "Weißt du, das da oben war schon echt seltsam. Und meine Mama sagt ja auch immer, dass Heidenau eine Greiterhex ist. Meinst du, die ist wirklich eine echte Hexe? Mit Besen und Allem?"
            
            menu:
                "Ja, das glaube ich auch!":
                    $ anja_points += 2
                    $ eve_points += 2
                    a "Wir sollten sie auf jeden Fall weiter beobachten!"
                    
                "Hexen gibt es doch nicht in echt!":
                    $ anja_points -= 2
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
                    jump scenew2_12
                    
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
                        "Anja warnen.":
                            $ anja_points += 2
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
                            jump scenew2_12
                            
                        "Dem Heu ausweichen.":
                            $ anja_points -= 2
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
                            jump scenew2_12
            
                            
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
             
            
            menu rassenwahl:
                p "Hm…mal sehen was zur Auswahl steht…"
                "Zwerg":
                    menu:
                        e "Ein bisschen ... simpel. Aber dafür total stark!"
                        
                        "Dann will ich ein Zwerg sein!":
                            $ race = "Zwergen"
                            $ pnpstr += 3
                            $ pnpdex += 2
                            $ pnpint += 1
                            n "Stark sein ist das Wichtigste!!"
                        
                        "Doch was anderes...":
                            jump rassenwahl
                            
                "Elf":
                    menu:
                        e "Ganz zerbrechlich aber dafür auch total schnell und agil!"
                        
                        "Dann will ich ein Elf sein!":
                            $ race = "Elfen"
                            $ pnpstr += 1
                            $ pnpdex += 3
                            $ pnpint += 2
                            n "Elfen sehen total cool aus!"
                            
                        "Doch was anderes...":
                            jump rassenwahl
                    
                "Mensch":
                    menu:
                        e "Körperlich nicht so toll aber dafür recht schlau!"
                        
                        "Dann will ich ein Mensch sein!":
                        
                            $ race = "Menschen"
                            $ pnpstr += 2
                            $ pnpdex += 1
                            $ pnpint += 3
                            n "Ich glaub ich bleibe einfach ein Mensch."
                            
                        "Doch was anderes...":
                            jump rassenwahl
                    
            e "…und dann wählst du deine Rolle. Das ist was du gut kannst."
            n "Was für eine Rolle habe ich?"

            
            menu klassenwahl:
                n "Was für eine Rolle habe ich?"
                "Zauberer":
                    menu:
                        e "Die sind so schlau, dass sie jemandem damit weh tun können. Sie beherrschen die mächtigste Magie!"
                        
                        "Dann will ich ein Zauberer sein!":
                             $ role = "Zauberer"
                             $ pnpstr += 1
                             $ pnpdex += 1
                             $ pnpint += 3
                             n "Niemand besiegt mich, wenn ich zaubern kann!"
                         
                        "Doch was anderes...":
                            jump klassenwahl    
                    
                "Bogenschießer":
                    menu:
                        e "Greifen lieber aus der Ferne an und können viele Tricks!"                       
                        
                        "Dann will ich ein Bogenschießer sein!":
                            $ role = "Bogenschießer"
                            $ pnpstr += 1
                            $ pnpdex += 3
                            $ pnpint += 1
                            n "Ich bin der besteste Pfeilbogenschießer der Welt!"
                             
                        "Doch was anderes...":
                            jump klassenwahl
                
                "Kämpfer":
                    menu:
                        e "Verlassen sich hauptsächlich auf rohe Gewalt um Probleme zu lösen ..."
                         
                        "Dann will ich ein Kämpfer sein!":
                            $ role = "Kämpfer"
                            $ pnpstr += 3
                            $ pnpdex += 1
                            $ pnpint += 1
                            n "Mit meinem großen Schwert, hau ich alle um!"
                             
                        "Doch was anderes...":
                            jump klassenwahl
                    
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
            e "Da sagte die mutige Bardin zu ihre[r/m] Freund[in] dem [race] [role]:"
            e "Was willst du tun? Das könnte ein Bandit sein. Sollen wir uns verstecken?"
            n "Oh..."
            n "Ich glaub, ich soll jetzt was sagen."
           
            menu:
                "Äh...worum geht's?":
                    $ eve_points -= 2
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
                            $ pnp1winpoints += 4
                            p "Ich hab noch Platz hier in meiner Tasche."
                            e "Beide Helden stecken sich ein paar der Beeren in die Beutel, essen sie aber nicht, weil sie nicht wissen, ob man das darf."
                            e "Dann bemerken sie, dass die komische Person nicht mehr zu sehen ist und kriechen wieder aus dem Gebüsch."    
                            
                        "Wieso mitnehmen und nicht gleich essen?":
                            $ eve_points -= 10
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
                            $ eve_points += 2
                            e "Der Händler lachte. \"Somonoa, davon gibt es wirklich schon mehr als genug. Wollt ihr euch nicht noch kurz meine Tücher anschauen?\" "
                            e "\"Das ist sehr nett\", sagte die Bardin.\"Aber wir besitzen momentan kein Geld.\" "
                            e "\"Zu schade! Dann will ich euch nicht länger stören.\" "
                            p "Kann er uns nicht einfach was schenken?"
                            e "\"Der Händler lacht nur und geht weiter."
                            
                        "Wir sind auf dem Weg ins nächste Dorf.":
                            $ eve_points += 3
                            e "\"Oh...\" Der Händler schaut kurz komisch. \"Dann hab ich vielleicht was, was ihr gebrauchen könntet.\""
                            e "Er kramt in seiner Tasche und zieht anschließend ein Glas mit einem schwarzen Pulver raus."
                            e "\"Vertraut mir, ihr werdet es brauchen!\" "
                            
                            menu:
                                "Oh...danke!":
                                    $ eve_points += 2
                                    $ powder = True
                                    e "\"Aber wir können das gar nicht bezahlen\", sagte die Bardin."
                                    e "\"Keine Sorge!\", sagte der Händler. \"Das ist ein Geschenk. Wir Reisenden müssen zusammen halten.\" Er lächelte noch kurz komisch, drehte sich um und ging wieder weiter."
                                    
                                "Nein, danke!":
                                    p "Mama sagt, man nimmt nichts von Fremden an."
                                    e "\"Was mein Freund eigentlich sagen will\", sagte die Bardin,\"ist, dass wir kein Geld haben. Und wir können keine Geschenke annehmen.\""
                                    e "\"Das ist schade\", sagte der Händler, lächelte noch kurz komisch, drehte sich um und ging wieder weiter."
                                    
                        "Wie soll ein Händler Helden helfen?":
                            $ eve_points -= 4
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
                            $ eve_points -= 8
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
                            $ eve_points -= 4
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
                    $ eve_points -= 4
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
                    $ eve_points += 6
                    $ pnp1winpoints += 1
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
    jump scenew2_12
    
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
    jump scenew2_12
    
    
    
label scenew2_12:
    play music happytheme1
    scene bg street
    n "Ja, endlich Wandertag!"
    n "Ich war schon länger nicht mehr im Wald. Das letzte mal war im Winter, da ging es Papa aber nciht so gut."
    n "Ich hoffe ich bekomme einen Fensterplatz, doch da muss ich schnell sein."
    n "Warte, die Tür geht schon auf!"
    k "So, dann alle einsteigent."
    n "Waaah!"
    scene bus with dissolve
    n "Warum sind die alle so schnell? Jetzt ist ja schon alles besetzt."
    n "Moment, noch 1 Platz HAHA!"
    n "Ich hasse es am Gang zu sitzen, da kann man gar nicht richtig rausgucken."
    #JUMPER
    if eve_points > anja_points and eve_points > octa_points:
        $ mapa = "Evelynn"
        n "Da kommt ja Evelynn."
        show eve happy2 at rightish
        e "Hallo [name], darf ich neben dir?"
        p "Gerne, setz dich hin!"
        show eve happy2 at rightish
        n "..."
        n "..."
        n "Heute ist sie schon wieder so still, vielleicht kann ich ja."
        e "Hey, ich hab meine Malsachen dabei, wollen wir was malen?"
        p "Wo denn?"
        show eve mad
        play sound "Briefumschlag.ogg"
        show eve happy2
        p "Woah, an den Sitzen ist ein Tisch?"
        e "Wir malen Draußen."
        p "Wie Draußen?"
        show eve shy2
        e "Na, was draußen am Fenster ist. Der Bus fährt zwar schnell, aber das geht schon."
        e "Hier, Papier und Stifte!"
        p "Dankeschön!"
        show eve happy2
        play sound "Malgeäusche_Zackig.ogg"
        n "So langsam komm ich rein ins malen."
        n "Welche Farben man nehmen soll, wie man eine Sonne malt, was Kontraste sind."
        n "Alles von Evelynn gelernt."
        n "Ich sollte ihr mal danken."
    
    elif octa_points >= anja_points and octa_points >= eve_points:
        $ mapa = "Octavia"
        n "Hey, da ist ja Octavia! Da war wohl ich mal schneller."
        show octa happy
        n "Sie setzt sich einfach hin."
        p "Meine Mama sagt, dass man erst etwas sagen soll bevor man sich hinsetzt."
        show octa talk
        o "Hey."
        p "Hmmmh."
        n "Sie sagt ja kaum etwas. Will sie nicht neben mir sitzen?"
        show octa shock
        p "Da vorne ist auch noch ein Platz, weil du willst bestimmt nicht neben mir"
        o "Was? Nein, passt schon..."
        show octa happy
        p "Hmmmh."
        n "Wie ist die heute drauf?"
        show octa talk
        o "Du [name]. Warst du schon mal im Wald? Also den hier jetzt?"
        p "Ich bin doch neu hier. Aber ich war schon öfters im Wald, mit meinen Vater und so."
        show octa smug
        o "Dann muss ich dir was voll cooles zeigen!"
        n "Mir was cooles zeigen?"
        p "Bin dabei!"
    
    elif anja_points >= eve_points and anja_points > octa_points:
        $ mapa = "Anja"
        a "Hey [name]."
        p "Da ist ja Anja."
        show anja talk
        a "Ich setz mich mal neben dich. Macht dir ja nichts aus, oder?"
        show anja mad
        a "Die anderen Plätze sind schon belegt und ich will nicht vorne zu Frau Heidenau, weißt du?"
        p "Gerne."
        show anja jabber
        a "Freust du dich auch schon so auf den Wandertag? So wie ich? Wir sollen außerdem in Zweiergruppen laufen, willst du mit mir?"
        p "Ich freu mich aufjedenfall."
        a "Dann ist das ja geklärt. Weißt du eigentlich wie lange wir fahren werden? Bei lange fahrten langweile ich mich."
        p "Bin doch auch neu, ich weiß es nicht."
        a "Ach ja, stimmt ja. Willst du dann so lange etwas spielen?"
        n "Sie redet schon wieder so schnell! Aber beim spielen langweile ich mich wenigstens nicht."
        p "Was denn?"
        show anja hihi
        a "Ich sehe was was du nicht siehst und es ist rot!"
        n "Es geht schon los? Das kann ja noch was werden mit ihr."
        
        show anja 
    
    "end of week 2"
    

    
label scenew3_0:

    kg "Brabbel"
    k "Kinder..."
    kg "Brabbel"
    k "Kinder wenn ich..."
    kg "Brabbel"
    h "KINDER! RUHE!"
    kg "..."
    n "Wow das war laut! Sogar Anja ist ruhig."
    k "Tschuldigung, aber ich brauch nur mal kurz eure Aufmerksamkeit."
    k "Wir sind ja jetzt hier am Wald angekommen. Aber bevor wir aus dem Bus aussteigen und uns auf den Weg zur Bernerhütte machen, müssen wir noch einige Regeln klären."
    h "Also zuhören!"
    k "Ja äh genau... also Regel 1."
    k "Regel 1 ist einfach. Ihr bleibt immer bei der Gruppe."
    k "Regel 2 ist, dass wir euch in Paare einteilen. Euer Sitznachbar ist auch euer ... äh wie hatten sie das nochmal genannt Frau Heidenau?"
    h "Marschpartner."
    k "Genau euer Sitznachbar ist euer Marschpartner."
    n "Ahh, also ist [mapa] mein Marschpartner! Toll!"
    k "Ach und Regel 3 ist das ihr nichts ohne unsere Erlaubnis im Wald sammelt. Das ist nämlich gefährlich."
    h "Wenn ich jemanden von euch etwas aufsammeln sehe dann gnade euch Gott."
    h "Denn ich werde nicht so gnädig sein. Verstanden?"
    kg "..."
    h "Verstanden?!"
    kg "Ja."
    h "Ich meine hier auch ganz explizit dich Louis."
    h "Wenn du nur daran denkst was in deine Jacke zu stecken, dann war es das letzte Mal, dass du deine Jacke gesehen hast."
    show louis mad at left with moveinleft
    L "..." 
    hide louis with moveoutleft
    k "Nun...äh...gut."
    k "Dann mal los. Schnappt euren Marschpartner und folgt mir."
    
    if mapa == "Anja":
        jump anjas_ending
        
    elif mapa == "Octavia":
        jump octas_ending
        
    else:
        jump eves_ending
    
    
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
    nvln "Euer Team von Babys First Visual Novel"
    "diojasppjdaps"
    "diuashdsaoi"
    "daosijdaos"
    
    
    #"Testtest."
        

    
    
    # This ends the game.

    return
