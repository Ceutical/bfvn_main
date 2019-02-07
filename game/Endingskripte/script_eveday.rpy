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
define audio.hoehletheme1 = "music/soundtracks/Fantasy_Höhle1.ogg" ###new
define audio.fantasyboss = "music/soundtracks/Fantasy_Boss1.ogg" ### new
define audio.happytheme1 = "music/soundtracks/Happy_Theme1.ogg"
define audio.happytheme2 = "music/soundtracks/Happy_Theme2.ogg"
define audio.playtheme1 = "music/soundtracks/Kinder_Beim_Spielen1.ogg"
define audio.playtheme2 = "music/soundtracks/Kinder_Beim_Spielen2.ogg"
define audio.opartytheme = "music/soundtracks/Kinder_Party_Theme1.ogg"
define audio.apartytheme = "music/soundtracks/Kinder_Party_Theme2.ogg"
define audio.epartytheme = "music/soundtracks/Kinder_Party_Theme3.ogg"


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
define audio.Whoosh3 = "music/sfx/Whoosh3.ogg"
define audio.Whoosh5 = "music/sfx/Whoosh5.ogg" ###new
define audio.Magie1 = "music/sfx/Magie1.ogg" ###new
define audio.Magie2 = "music/sfx/Magie2.ogg" ###new
define audio.Magie3 = "music/sfx/Magie3.ogg" ###new
define audio.Magie4 = "music/sfx/Magie4.ogg" ###new
define audio.Aufprall = "music/sfx/Herzschlag.ogg" ###new
define audio.Chicken = "music/sfx/Hahnwecker.ogg"
define audio.antiarmor = "music/sfx/Schutzausrüstung_ausziehen.ogg"
define audio.bike = "music/sfx/Fahrrad.ogg"
define audio.chain = "music/sfx/Fahrrad_alteKette.ogg"
define audio.bikebreak = "music/sfx/Fahrradbremse.ogg"


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


label start:
    play music introtheme
    python:
        if not persistent.set_volumes:
            persistent.set_volumes = True
            _preferences.volumes['music'] *= .80 
        renpy.music.set_volume(volume=0.5, channel='music')
    
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
    $ attackgoblin = False
    
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

label eves1:
    scene bg woods with dissolve
    show eve talk2 at rightish with dissolve
    e "Toll! Alles so schön grün hier. Das gibt mir eine Idee!"
    p "..."
    e "Du, [name]?"
    p "Ja?"
    e "Hast du Lust Das Blaue Auge zu spielen, wenn wir bei der Hütte sind?"
    p "Na klar, gerne. Ich hab doch den Helden dafür schon gestern gemacht!"
    ### eventuell Charactersheet Displayable? Points = Stats ###
    show eve happy2
    e "Super!"
    scene hut with dissolve
    show karin talk with dissolve
    k "So Kinder! Hier machen wir jetzt erstmal eine kurze Mittagspause!"
    k "Bitte bleibt alle hier in der nähe, damit ich euch nicht aus den Augen verliere."
    hide karin with dissolve
    show eve talk2
    e "Hey, lass uns hier einfach in die Ecke setzen, in der Hütte haben wir doch sicher unsere Ruhe."
    show eve mad
    e "Es sei denn..."
    p "Da bin ich dabei."
    show eve vhappy2
    e "Wollen wir anfangen?"
    p "Klar. Auf geht's!"
    play music fantheme1
    show eve talk2
    e "Unser Abenteuer startet in der Nähe des Königspalastes von Fantasien."
    e "Wir sind Helden, die gerufen wurden und müssen uns in Richtung einer Stadt aufmachen!"
    show eve mad
    e "[name] schau mal her!"
    e "Alles wie im Buch beschrieben."
    p "Was? Zeig mal!"
    show bg castle with dissolve
    show eve pnp2 with dissolve
    p "Alles voll bunt und föhlich hier. Was ist denn das auf deinem Rücken?"
    e "Oh, das ist wohl eine Laute! Das Werkzeug einer Bardin."
    p "Baden?"
    show eve pnpn
    e "Eine, die mit Musik zaubern kann."
    p "Das ist auch cool."
    show eve pnpask
    e "Auch wenn es schön ist, hier ist nicht viel los. Außerdem sollen wir doch in die Stadt gehen und Abenteuer machen."
    p "Ob es da fiese Monster gibt, die wir bekämpfen können?"
    e "Mit Sicherheit"

label eves2:
    scene bg pnpvillage with dissolve
    show eve pnpvhappy at rightish
    e "Wow! Sieh nur an, wie viele Leute hier sind. Die haben bestimmt spannende Geschichten zu erzählen!"
    p "Aber wir haben doch gar keine Zeit für sowas. Wir müssen wissen wo unsere Hilfe gebraucht wird."
    show eve pnpask
    e "Also, die Helden aus meinen Büchern bekommen Aufträge meistens in Tavernen."
    p "Was ist denn eine Taverne?"
    e "Sowas wie ein Restaurant wo sich Leute treffen."
    n "Die weiß so viel, Sie hätte ein Zauberer sein sollen!"
    p "OK, dann fragen wir mal jemanden nach dem Weg dahin?"
    show eve pnpvhappy
    e "Gute Idee!"
    show eve pnpask
    e "Verzeihung!"
    show cat n at leftish with moveinleft
    e "Können Sie mir sagen, wo wir die örtliche Taverne finden, gnädiger Herr?"
    n "Was ist los mit ihr?"
    show cat talk
    "Passant" "Ähm, Selbstverständlich, gnädiges Fräulein. Hinter dem Brunnen links und dann immer den Geruch nach."
    "Passant" "Möchten Sie wohl dort ein Ständchen singen?"
    show eve pnpvhappy
    e "Vielleicht."
    show eve pnpn
    e "Haben Sie vielen Dank und einen schönen Tag noch."
    hide cat with moveoutright
    p "Hast du seine Schnurrhaare gesehen? Sehen die hier alle so aus?"
    show eve pnp2
    e "Bestimmt nicht, es leben viele Wesen hier."
    p "Die will ich sehen!"
    e "Na dann. Los, auf in die Taverne!"

label eves3:
    scene bg pnppub with dissolve
    p "Ich glaube, ich fühle mich etwas unwohl hier. Wir sind die einzigen normalen Leute."
    show eve pnpmad
    e "Spinnst du= Alle hier sind normal. Eigentlich sind wir hier die besonderen, weil wir sind ja nur Menschen."
    n "???"
    p "Bekommen wir dann überhaupt Aufgaben? Und von wen?"
    e "Du kennst dich hier wirklcih nicht aus. Vom Wirt natürlich."
    p "Und das soll ich woher Wissen?"
    show eve pnpask
    e "Er ist der, der mit allen Gästen redet. Wenn also irgendwer Neuigkeiten hat, dann der."
    p "Na dann..."
    hide eve with moveoutright
    show eve pnpask at leftish with moveinleft
    show wirt n at rightish with dissolve
    e "Seien Sie gegrüßt werter Herr, mein Freund und ich hier sind Abenteuerer und haben uns gefragt, ob Sie uns ein paar interessante Geschichten aus der Gegend erzählen können."
    show wirt talk
    "Wirt" "Ihr seht mir aber ein bisschen jung aus für Abenteurer, aber wer bin ich um das zu hinterfragen?"
    "Wirt" "Aber selbstverständlich, hier ist immer viel los."
    show eve pnp2
    "Wirt" "Neulich hat die alte Brunhilde ihren Goldzahn in den Brunnen fallen lassen."
    "Wirt" "Viele Männer haben versucht den Zahn zu bergen, aber niemand hat ihn gefunden..."
    show eve pnpask
    e "Und schlimme Monster oder Bösewichte?"
    show wirt mad
    "Wirt" "Hmmmh... Achso, es gibt tatsächlich ein paar Gerüchte über ein furchteinflößendes Monsterm."
    "Wirt" "Viele Leute sind in den letzten Nächten verschollen und es wird vermutet, dass eine Kreatur namens Königsfüßler Sie mitgenommen hat."
    show wirt n
    show eve pnp2
    p "Wie schrecklich! Hat das Wesen irgendwelche Kräfte?"
    "Wirt" "Sie können den Willen der Menschen unterdrücken, ihre Opfer können sich dann nicht mehr wehren und werden schutzlos verspeißt!"
    n "Wille unterdrücken? Das ist ja gruselig, ich kann mir so etwas gar nicht vorstellen."
    p "Und gegen was ist es schwach?"
    "Wirt" "Ist ja nur ein Gerücht. Es soll aber einen harten Panzer und unzählige Beine Haben, wenn es also eine Weiche Stelle besitzt, dann wohl dort angreifen."
    show eve pnpask
    e "Und wo genau ist die Höhle von den Monster?"
    show wirt talk
    "Wirt" "Ich schätze im Wald, wenn es hier in der nähe ist. Aber genau kann ich das auch nicht sagen, ich hör halt nur manches."
    "Wirt" "Aber wenn ich es auf die Stadt abgesehen hätte, dann wäre ich wohl in der nähe. Etwa den Wald oder so."
    show eve pnpvhappy
    e "Vielen Dank!"
    hide wirt
    show eve pnpask
    e "Du [name], glaubst du wir sind stark genug für das Monster?"
    p "Bestimtt, wir sollten es auf jeden Fall versuchen."
    p "Ich bin ja stark!"
    show eve pnpmad
    e "Hast wohl recht."
    p "ZUR HÖHLE!"

label eves4:
    scene bg caveentry with dissolve
    n "Endlich angekommen an der Höhle."
    e "Du [name], glaubst du das ist die Höhle?"
    p "Ja."
    show eve pnp2 with dissolve
    e "Wieso bist du dir so sicher?"
    p "Weil es hier unheimlich aussieht."
    e "Wir müssen vorsichtig sein, man weiß nie was in der Dunkelheit lebt."
    p "Ich beschütze dich schon."
    show eve at rightish with move
    show eve pnpmad
    show eve at leftish with move
    show bat angst at rightish with moveinright
    e "EEEEK!"
    e "Schnell, mach was [name]!"
    ### $ time = 5
    ### $ timer_range = 5
    ### $ timer_jump = 'Abwarten'---> while time <0 "show menu" else: "Abwarten Text nochmal kopieren"
    menu:
        "Angreifen":
            n "Einfach Augen zu und draufhauen!"
            play sound Whoosh3
            scene bg black with dissolve
            e "Vorsicht, Sie greift an!"
            show bat angst at rightish
            scene bg caveentry with dissolve
            show bat angst at leftish with move
            p "Aua!"
            p "Nochmal..."
            play sound Whoosh3
            show bat dead
            hide bat with moveoutbottom
            e "Der hat gesessen."
            p "Wenn die Fledermaus Angst hatte, dann sind wir doch wohl hier richtig."
            e "Mmmmh."
            
        "Abwarten":
            n "Ich mach einfach nichts."
            p "Die geht von alleine weg."
            show eve pnpmad
            e "spinnst du? Wieso sollte..."
            hide bat with moveoutleft
            p "Eine Fledermaus, die wollen uns nichts böses."
            e "Aber ich dachte..."
            p "Lass uns reingehen, pass aber auf."
            
               
        "Musik":
            n "Fledermäuse sehen nicht, sondern hören nur hat mir Papa erzählt."
            p "LOS EVELYNN, SING!"
            show eve pnpmad
            e "Was?"
            p "Tus einfach"
            show eve pnpsing
            show bat happy
            e "Es tanzt ein Bi-Ba-Butzemann in unserm Haus herum, fidibum. Es tanzt ein Bi-Ba..."
            hide bat with moveoutleft
            p "Es hat funktioniert!"
            show eve pnpask
            e "Woher wusstest du das?"
            p "Sag ich dir später, aber wenn die Fledermaus Angst hat. Dann sind wir richtig."
            e "Mmmmh."
    
label eves5:
    scene bg cave with dissolve
    play music hoehletheme1
    show eve pnpn at leftish
    p "Ich wusste gar nicht, dass es hier gruselig ist. Dunkelheit macht mir Angst."
    e "Und Hunger."
    p "Hunger macht mir auch Angst."
    show eve pnpask
    p "Warte!"
    e "Was?"
    p "Du kannst doch hier zaubern, kannst du uns nicht essen machen?"
    e "Ich probier es mal."
    show eve pnpsing
    e "Ooooh... Pizza, Pepperoni, Mozzarella..."
    e "Tagliatelle find ich bella..."
    play sound Magie4
    show pizza
    p "WOAH! Pizza!"
    e "Mir gehört das große Stück!"
    p "Nicht wenn ich es zuerst esse!"
    show eve pnpmad
    e "NEIN!"
    n "Woah. Was ist auf einmal mit ihr los, ist doch nur Pizza. Egal, sie hat es auch hergezaubert."
    hide pizza
    show pizza2
    show eve pnp2
    e "Mmmh, lecker."
    p "Ja, sag mal. Du weißt ja viel, hatten die damals Pizza?"
    e "Wieso denn nicht?"
    p "Stimmt."
    hide pizza2 with dissolve
    show pizzastueck
    p "Willst du das letzte Stück noch?"
    show eve pnpn
    e "Ich schaff nichts mehr, wollen wir es mitnehmen?"
    p "Ich brauch doch mein schwert."
    "???" "Grrrmmmlll... Essen..."
    show eve pnpask
    e "Was war das?"
    show goblin1 happy
    show goblin2 happy at rightish
    show eve pnpmad
    e "Goblins und die sehen nicht freundlich aus!"
    menu:
        "Pizza werfen":
            n "Ich glaub ich habe essen gehört!"
            hide pizzastück with moveouttop
            p "FANG!"
            "Goblins" "Nicht das Essen!"
            hide goblin1 with moveouttop
            hide goblin2 with moveouttop
            p "Los, rennen!"
            show eve pnp2
            e "Das war klug von dir."
            p "Ich hab nur aufgepasst, jetzt los."
            hide eve with moveoutright
            
        "Falle auslösen":
            n "Die steine da oben!"
            p "Kannst du die Steine da oben lösen?"
            e "Ich versuch es!"
            show eve pnpsing
            e "Es kommt ein rollender Stein, herunter den Wein, zerstört was ist mein..."
            show goblin1 mad
            show goblin2 mad
            "Goblins" "Au, meine Ohren! Tut weh!"
            e "Oh, tut mir leid. Ich wollte niemanden weh tun."
            "Goblins" "Wir wollen doch nur essen."
            p "Uns isst ihr aber nicht!"
            hide pizzastueck
            e "Hier! Pizza"
            show goblin1 happy
            show goblin2 happy
            "Goblins" "JAAA!"
            hide goblin1 with moveouttop
            hide goblin2 with moveouttop
            p "Ach so."
            e "Die hatten Hunger."
            p "Gut gemacht, aber wir sollten jetzt wohl weiter."
            hide eve with moveoutright
            
        "Angreifen":
            $attackgoblin = True
            p "Keine Zeit, wir müssen angreifen."
            show goblin1 mad
            show goblin2 mad
            p "Eve einen Zauber..."
            show eve pnpsing
            p "Nimm das, du hässliches ding!"
            play sound Whoosh3
            hide goblin1 with moveoutbottom
            show goblin1 mad with moveinbottom
            p "AAAUU!"
            e "WAMBO!"
            play sound Magie3
            show amboss at rightish with moveintop
            show goblin1 dead
            show goblin2 dead
            n "Wow! Ein Amboss?"
            show eve pnp2
            e "Oh nein."
            p "Gut gemacht, aber wenn hier Monster sind dann müssen wir schnell weiter!"
            hide eve pnp

label eveboss:
    scene bg gang with dissolve
    show eve pnp2
    p "Wie tief sind wir jetzt eigentlich in dieser Höhle?"
    e "Ich weiß nicht, aber ich kann kaum noch was sehen..."
    play sound Whoosh5
    p "Hast du was gesagt?"
    show eve pnpask
    e "Nein, aber vielleicht schläft es ja"
    p "Hmmh..."
    scene bg black with dissolve
    scene bg gang with dissolve
    show eve pnpask at leftish
    e "Nichts."
    p "Ich will nicht mehr, dass dauert jetzt schon lange. Wir müssen doch eh bald mit den anderen Kindern wieder heim. Ist doch eh alles komisch."
    show eve pnp2
    e "Ich weiß nicht."
    e "Aber wo soll ich denn hin?"
    p "Hmmh?"
    show eve pnpask
    e "Ich kann mit niemanden reden."
    p "Aber, du redest doch mit mir."
    e "Daheim geht das aber nicht, ich will doch hier bleiben."
    p "Aber, daheim ist es doch schön. Ich kann Fernsehen, hab meine Spielsachen."
    play sound Whoosh5
    show eve pnpmad
    e "Darf ich doch nicht! Meine Mama sagt das immer."
    p "Gar nichts?"
    show eve pnpn
    e "Gar nichts."
    p "Hmmh, machs doch trotzdem oder geheim."
    e "Das bringt doch nichts, da kann ich gleich aufgeben."
    p "Schon einmal probiert?"
    show eve pnpask
    e "Nein."
    show monster n with moveintop
    hide eve with moveoutbottom
    play music fantasyboss
    e "AAAAAH!"
    e "Wir müssen etwas tun!"
    
    menu:
        "Angreifen":
            e "Schlag ihn!"
            play sound Aufprall    
            "???" "TSSS TSS"
            play sound cardoor2
            p "WAAAAH! Das tut unglaublich weh."
        
        "Pizza":
            p "Vielleicht will er auch Pizza essen?"
            play sound Magie4
            "???" "TSSS TSS"
            play sound cardoor2
            e "WAAAH!"
            p "EVELYNN!"
        
        "Angriffszauber!": 
            p "Eveylnn, wir brauchen einen weiteren Amboss!"
            e "Sofort!"
            play sound Magie3
            show amboss with moveintop
            play sound Aufprall
            "???" "TSSS TSS"
            play sound cardoor2
            hide amboss with moveoutbottom
            p "Ausweichen."
            e "Ouch!"
    
    p "Warum klappt das nicht? Ist doch nur ein Spiel!"
    e "Hey, mach irgendwas!"
    play sound magic1
    p "Ich kann mich nicht bewegen!"
    e "Ich auch nicht! Was ist das für ein Zauber!"
    e "Wir haben verloren!"
    hide monster with moveoutbottom
    e "EEEK!"
    p "WEHR DICH DOCH!"
    e "Ich kann nicht! Ich will nicht! Ich darf nicht!"
    menu:
        "Es ist nur ein Spiel!":
            p "Na gut, es ist ja doch nur ein Spiel."
            e "Wie kannst du sowas sagen?"
            p "Was ist denn jetzt dein Problem!"
            e "AAAAAAH"
            scene bg hut with dissolve
            show eve mad
            e "DU IDIOT MUSST MIR ALLES RUINIEREN!"
            hide eve with moveoutright
            p "Evelynn..."
            e "BLEIB WEG"
            play sound cardoor2
            ###move on to bad ending
        
        "Tu es einfach, schlimmer kann es nicht werden!":
            p "Das ist doch dein Problem!"
            p "Einfach dagegen ankämpfen, was soll denn schlimmeres für dich und mich passieren!"
            e "[name]!"
            p "Du schaffst das schon. Du bringst mir andauernd neue Sachen bei."
            p "Du weißt soviel, bist besser als alle im malen und dann darfst du doch nicht aufgeben."
            e "IN SCHLING UND DONNERTAL! BLEIBT MIR KEINE WAHL!"
            show monster n with moveinbottom
            n "Ich kann mich wieder bewegen!"
            e "HÖR DEN HALL UND SPÜR DEN WALL!"
            show monster plants with dissolve
            e "Jetzt greif ihn an wo er nicht geschützt ist!"
            play sound Whoosh3
            p "Mitten ins Gesicht!"
            "???" "EVELYNN!!!!"
            show monster dead with dissolve
            e "Wir habens geschafft."
            e "WIR HABENS GESCHAFFT!"
            p "Ich wüsste du kannst das."
            e "Ja, ja, JA!"
            p "Wollen wir unsere Belohnung von der Stadt abholen?"
            e "Gerne können wir das noch machen."
            scene bg caveentry with dissolve
            show eve pnp2
            p "Moment mal!"
            show eve pnpask
            e "Was ist denn?"
            p "Ich muss dich jetzt was Fragen, bevor ichs vergesse."
            e "Hmmmh?"
            p "Sag mal... ist das mit deinen Eltern real gewesen?"
            scene bg hut with dissolve
            show eve talk2 with dissolve
            e "Wieso das denn?"
            p "Darfst du daheim echt nichts machen?"
            show eve mad
            e "Nein, ich darf auch nicht zu freunden oder so. Da sind meine Eltern ganz streng."
            p "Evelynn, willst du zu mir heute mit nach hause?"
            e "Aber meine Eltern!"
            show eve shy2
            p "Fragen wir doch einfach!"
            p "Wir können ja auch bei mir malen."
            show eve vhappy2
            e "Wie wäre es mit einer Fledermaus oder einer viel zu großen Pizza?"
            p "Hört sich doch toll an!"
            show eve shy2
            e "Hör mal. Danke das du mit mir spielst, ich fühle mich wirklich gut."
            p "Mir hat es auch Spaß gemacht."
            e "Das wiederholen wir so schnell wie möglich."
            p "Dann aber bei mir und mit Randy!"
            e "Das klingt gut!"
            ### good ending/confrontation
    
    
    


    return
