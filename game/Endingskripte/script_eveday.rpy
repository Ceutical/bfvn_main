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
define audio.hoehletheme1 = "music/soundtracks/Fantasy_Höhle1.ogg"###new
define audio.hoehletheme2 = "music/soundtracks/Fantasy_Höhle2.ogg"###new
define audio.fantasyboss = "music/soundtracks/Fantasy_Boss1.ogg" ### new
define audio.fantasyboss2 = "music/soundtracks/Fantasy_Boss2.ogg" ### new
define audio.spookywald3 = "music/soundtracks/SpookyWald3.ogg" ### new
define audio.happytheme1 = "music/soundtracks/Happy_Theme1.ogg"
define audio.happytheme2 = "music/soundtracks/Happy_Theme2.ogg"
define audio.playtheme1 = "music/soundtracks/Kinder_Beim_Spielen1.ogg"
define audio.playtheme2 = "music/soundtracks/Kinder_Beim_Spielen2.ogg"
define audio.opartytheme = "music/soundtracks/Kinder_Party_Theme1.ogg"
define audio.apartytheme = "music/soundtracks/Kinder_Party_Theme2.ogg"
define audio.epartytheme = "music/soundtracks/Kinder_Party_Theme3.ogg"
define audio.GoodEnd = "music/soundtracks/GoodEnd.ogg"###new
define audio.BadEnd = "music/soundtracks/BadEnd.ogg"###new


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


label eves_ending:
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
    #############################


label eves1:
    scene bg woods with dissolve
    stop music fadeout 1.0
    play music happytheme2 fadein 1.0
    show eve talk2 at rightish with dissolve
    e "Toll! Alles so schön grün hier. Das gibt mir eine Idee!"
    p "..."
    e "Du, [name]?"
    p "Ja?"
    e "Hast du Lust Das Blaue Auge zu spielen, wenn wir bei der Hütte sind?"
    p "Na klar, gerne!"
    ### eventuell Charactersheet Displayable? Points = Stats ###
    show eve happy2
    e "Super!"
    scene hut with dissolve
    show karin talk with dissolve
    k "So, Kinder! Hier machen wir jetzt erstmal eine kurze Mittagspause!"
    k "Bitte bleibt alle hier in der Nähe, damit ich euch nicht aus den Augen verliere."
    hide karin with dissolve
    show eve talk2
    e "Hey, lass uns einfach hier in die Ecke hocken, in der Hütte haben wir doch sicher unsere Ruhe."
    show eve mad
    e "Es sei denn..."
    p "Da bin ich dabei."
    show eve vhappy2
    e "Wollen wir anfangen?"
    p "Klar. Auf geht's!"
    stop music fadeout 3.0
    play music fantheme1
    show eve talk2
    e "Unser Abenteuer beginnt  ganz in der Nähe des Königspalastes von Müramoor."
    e "Wir sind Helden, die gerufen wurden, und müssen uns in Richtung einer Stadt aufmachen!"
    e "Erst am frühen Morgen, als die Sonne gerade aufgeht, können wir die Stadtmauern von Burenia erblicken."
    e "Wir machen dort kurz auf einem Hügel rast um uns zu Erholen und Frühstücken."
    n "Evelynn erzählt total toll! Ich kann mir ganz genau vorstellen, wie die Stadt aussehen würde."
    scene bg castle with dissolve
    p "Alles voll bunt und föhlich hier. Was ist denn das auf deinem Rücken?"
    show eve pnp2 with dissolve
    e "Oh, das ist wohl eine Laute! Das Werkzeug einer Bardin."
    p "Baden?"
    p "Und wieso Werkzeug? Kannst du damit bauen?"
    show eve pnpn
    e "Ne, die kann mit Musik zaubern.."
    p "Das ist auch cool."
    show eve pnpask
    e "Auch wenn es schön ist, hier ist nicht viel los. Außerdem sollen wir doch in die Stadt gehen und Abenteuer machen."
    p "Ob es da fiese Monster gibt, die wir bekämpfen können?"
    e "Mit Sicherheit"

label eves2:
    scene bg pnpvillage with dissolve
    show eve pnpvhappy at rightish with dissolve
    e "Wow! Sieh nur, wie viele Leute hier sind. Die haben bestimmt spannende Geschichten zu erzählen!"
    p "Aber wir haben doch gar keine Zeit für sowas. Wir müssen wissen, wo unsere Hilfe gebraucht wird."
    show eve pnpask
    e "Also, die Helden aus meinen Büchern bekommen Aufträge meistens in Tavernen."
    p "Was ist denn eine Taverne?"
    e "Sowas wie ein Restaurant wo sich Leute treffen. Da kann man Apfelsaft trinken und so."
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
    show eve pnp2
    e "Haben Sie vielen Dank und einen schönen Tag noch."
    hide cat with moveoutright
    p "Wieso hast du auf einmal so komisch geredet?"
    e "Das macht man hier so..."
    p "Und hast du seine Schnurrhaare gesehen? Sehen die hier alle so aus?"
    show eve pnp2
    e "Bestimmt nicht, es leben viele verschiedene Wesen hier."
    p "Die will ich sehen!"
    e "Na dann. Los, auf in die Taverne!"

label eves3:
    scene bg pnppub with dissolve
    stop music fadeout 3.0
    play music fantheme2 fadein 1.0
    p "Ich glaube, ich fühle mich doch etwas unwohl hier. Wir sind die einzigen normalen Leute."
    show eve pnpmad
    e "Spinnst du? Alle hier sind normal. Eigentlich sind wir hier die Besonderen, weil wir sind ja nur Menschen."
    n "???"
    p "Bekommen wir dann überhaupt Aufgaben? Und von wem?"
    e "Du kennst dich hier wirklich nicht aus. Vom Wirt natürlich."
    p "Und das soll ich woher wissen?"
    show eve pnpask
    e "Er ist der, der mit allen Gästen redet. Wenn also irgendwer Neuigkeiten hat, dann der."
    p "Na dann..."
    hide eve with moveoutright
    show eve pnpask at leftish with moveinleft
    show wirt n at rightish with dissolve
    e "Seien Sie gegrüßt werter Herr, mein Freund und ich hier sind Abenteuerer und haben uns gefragt, ob Sie uns ein paar interessante Geschichten aus der Gegend erzählen können."
    show wirt happy
    "Wirt" "Ihr seht mir aber ein bisschen jung aus für Abenteurer, aber wer bin ich um das zu hinterfragen?"
    "Wirt" "Aber selbstverständlich, hier ist immer viel los."
    show wirt talk
    show eve pnp2
    "Wirt" "Neulich hat die alte Brunhilde ihren Goldzahn in den Brunnen fallen lassen."
    "Wirt" "Viele Männer haben versucht den Zahn zu bergen, aber niemand hat ihn gefunden..."
    show eve pnpask
    e "Und schlimme Monster oder Bösewichte?"
    show wirt mad
    "Wirt" "Hmmmh... Achso, es gibt tatsächlich ein paar Gerüchte über ein furchteinflößendes Monster."
    "Wirt" "Viele Leute sind in den letzten Nächten verschollen und es wird vermutet, dass eine Kreatur namens Königsfüßler sie in seine Höhle mitgenommen hat."
    show wirt n
    show eve pnp2
    p "Wie schrecklich! Hat das Wesen irgendwelche Kräfte?"
    show wirt mad
    "Wirt" "Es kann den Willen der Menschen unterdrücken. Ihre Opfer können sich dann nicht mehr wehren und werden schutzlos verspeißt!"
    n "Wille unterdrücken? Das ist ja gruselig. Ich kann mir so etwas gar nicht vorstellen."
    show wirt n
    p "Und gegen was ist es schwach?"
    show wirt talk
    "Wirt" "Ist ja nur ein Gerücht. Es soll aber einen harten Panzer und unzählige Beine haben. Wenn es also eine weiche, unbepanzerte Stelle besitzt, dann sollte man wohl dort angreifen."
    show eve pnpask
    e "Und wo genau ist diese Höhle von dem Monster?"
    show wirt talk
    "Wirt" "Ich schätze, dass es hier irgendwo in der Nähe ist. Aber genau kann ich das auch nicht sagen, ich hör halt nur Manches."
    "Wirt" "Aber ich würde mir ein Lager in der Nähe suchen, wenn ich es auf die Stadt abgesehen hätte, etwa in dem Wald oder so."
    show eve pnpvhappy
    e "Vielen Dank!"
    hide wirt with dissolve
    show eve pnpask
    e "Du [name], glaubst du wir sind stark genug für das Monster?"
    p "Bestimt, wir sollten es auf jeden Fall versuchen."
    p "Ich bin ja stark!"
    show eve pnpmad
    e "Hast wohl Recht."
    p "ZUR HÖHLE!"

label eves4:
    scene bg caveentry with dissolve
    stop music fadeout 3.0
    play music hoehletheme1 fadein 3.0
    e "Du [name], glaubst du das ist die Höhle?"
    p "Bestimmt."
    show eve pnp2 with dissolve
    e "Wieso bist du dir so sicher?"
    p "Weil es hier unheimlich aussieht."
    e "Wir müssen vorsichtig sein, man weiß nie, was in der Dunkelheit lebt."
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
            scene bg caveentry with dissolve
            show eve pnpmad with dissolve
            show bat angst at leftish with move
            p "Aua!"
            p "Nochmal..."
            play sound Whoosh3
            show bat dead
            hide bat with moveoutbottom
            e "Der hat gesessen."
            e "Dabei sah die Fledermaus eigentlich gar nicht so gefährlich aus... Ich glaube sie hatte einfach nur Angst."
            p "Wenn die Fledermaus Angst hatte, dann sind wir doch wohl hier richtig."
            e "Mmmmh."
            
        "Abwarten":
            n "Ich mach einfach nichts."
            p "Die geht von alleine weg."
            show eve pnpmad
            e "Spinnst du? Wieso sollte..."
            hide bat with moveoutleft
            p "Ich glaub, die will uns gar nichts Böses. Die hat einfach nur Angst."
            e "Aber ich dachte..."
            p "Lass uns reingehen, pass aber auf."
            
               
        "Musik":
            n "Fledermäuse sehen nicht, sondern hören nur hat mir Papa erzählt."
            p "LOS EVELYNN, SING!"
            show eve pnpmad
            e "Was?"
            p "Tu's einfach"
            show eve pnpsing
            show bat happy
            e "Es tanzt ein Bi-Ba-Butzelmann in unserm Haus herum, fidibum. Es tanzt ein Bi-Ba..."
            hide bat with moveoutleft
            p "Es hat funktioniert!"
            show eve pnpask
            e "Woher wusstest du das?"
            p "Sag ich dir später. Aber siehst du, die hatte wahrscheinlich nur Angst und wenn die Fledermaus Angst hat, dann sind wir richtig."
            e "Mmmmh."
    
label eves5:
    scene bg cave with dissolve
    stop music fadeout 3.0
    play music hoehletheme2 fadein 3.0
    show eve pnpn at leftish
    p "Ich wusste gar nicht, dass es hier so gruselig ist. Dunkelheit macht mir Angst."
    e "Und Hunger."
    p "Hunger macht mir auch Angst."
    show eve pnpask
    p "Warte!"
    e "Was?"
    p "Du kannst doch hier zaubern, kannst du uns nicht Essen machen?"
    e "Ich probier es mal."
    show eve pnpsing
    e "Ooooh... Pizza, Pepperoni, Mozzarella..."
    e "Tagliatelle find ich bella..."
    play sound Magie4
    show pizza
    p "WOAH! Eine Monsterpizza!"
    e "Mir gehört das große Stück!"
    p "Nicht, wenn ich es zuerst esse!"
    show eve pnpmad
    e "NEIN!"
    n "Woah. Was ist auf einmal mit ihr los, ist doch nur Pizza. Egal, sie hat es auch hergezaubert."
    hide pizza
    show pizza2
    show eve pnp2
    e "Mmmh, lecker."
    p "Ja, sag mal. Du weißt ja viel, hatten die damals Pizza?"
    e "Wieso denn nicht?"
    p "Stimmt. Sonst wäre das traurig."
    hide pizza2 with dissolve
    show pizzastueck
    p "Willst du das letzte Stück noch?"
    show eve pnpn
    e "Ich schaff nichts mehr, wollen wir es mitnehmen?"
    p "Ich brauch doch mein Schwert."
    "???" "Grrrmmmlll... Essen..."
    show eve pnpask
    e "Was war das?"
    show goblin1 happy
    show goblin2 happy at rightish
    show eve pnpmad
    e "Goblins und die sehen nicht freundlich aus!"
    e "Was sollen wir denn jetzt tun?"
    menu:
        "Pizza werfen":
            n "Ich glaub ich habe Essen gehört!"
            hide pizzastueck with moveouttop
            p "FANG!"
            "Goblins" "Nicht das Essen!"
            hide goblin1 with moveouttop
            hide goblin2 with moveouttop
            p "Los, Rennen!"
            show eve pnp2
            e "Das war klug von dir."
            p "Ich hab nur aufgepasst, jetzt los."
            hide eve with moveoutright
            
        "Falle auslösen":
            n "Die Steine da oben!"
            p "Kannst du die Steine da oben lösen?"
            e "Ich versuch es!"
            show eve pnpsing
            e "Es kommt ein rollender Stein, herunter den Wein, zerstört was ist mein..."
            show goblin1 mad
            show goblin2 mad
            "Goblins" "Au, meine Ohren! Tut weh!"
            e "Oh, tut mir leid. Ich wollte niemanden weh tun."
            "Goblins" "Wir wollen doch nur essen."
            p "Uns esst ihr aber nicht!"
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
            p "Nimm das, du hässliches Ding!"
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
            hide eve pnp2

label eveboss:
    scene bg gang with dissolve
    show eve pnp2
    p "Wie tief sind wir jetzt eigentlich in dieser Höhle?"
    e "Ich weiß nicht, aber ich kann kaum noch was sehen..."
    play sound Whoosh5
    p "Hast du was gesagt?"
    show eve pnpask
    e "Nein. Vielleicht war es wieder nur eine Fledermaus..."
    p "Hmmh..."
    scene bg black with dissolve
    scene bg gang with dissolve
    show eve pnpask at leftish
    e "Nichts."
    p "Ich will nicht mehr, dass dauert jetzt schon lange. Wir müssen doch eh bald mit den anderen Kindern wieder heim. Ist doch eh alles komisch."
    show eve pnp2
    e "Ich weiß nicht..."
    p "Hmmh?"
    show eve pnpask
    e "Ich kann daheim mit niemanden reden."
    p "Aber, du redest doch mit mir."
    e "Aber nicht bei mir Zuhause. Ich will lieber hier bleiben. Hier darf ich wenigstens draußen spielen."
    p "Aber, daheim ist es doch schön. Da kann man Fernsehen, und hat seine Spielsachen."
    play sound Whoosh5
    show eve pnpmad
    e "Darf ich doch nicht! Meine Mama sagt immer, das macht dumm."
    p "Gar nichts?"
    show eve pnpn
    e "Gar nichts."
    p "Hmmh, mach's doch trotzdem oder geheim."
    e "Das bringt doch nichts, das gibt nur Ärger."
    p "Schon einmal probiert?"
    show eve pnpask
    e "Nein."
    show monster n with moveintop
    hide eve with moveoutbottom
    stop music fadeout 1.0
    play music fantasyboss
    e "AAAAAH!"
    e "Wir müssen etwas tun!"
    
    menu:
        "Angreifen":
            e "Schlag ihn!"
            play sound Aufprall    
            "Königsfüßler" "TSSS TSS"
            play sound cardoor2
            p "WAAAAH! Das tut unglaublich weh."
        
        "Pizza":
            p "Vielleicht will er auch Pizza essen?"
            play sound Magie4
            "Königsfüßler" "TSSS TSS"
            n "Wie kann man nur keine Pizza mögen?"
            play sound cardoor2
            e "WAAAH!"
            p "EVELYNN!"
            
        
        "Angriffszauber!": 
            p "Eveylnn, wir brauchen nochmal deine Magie!"
            e "Sofort!"
            play sound Magie3
            show amboss with moveintop
            play sound Aufprall
            "Königsfüßler" "TSSS TSS"
            play sound cardoor2
            hide amboss with moveoutbottom
            p "Ausweichen."
            e "Ouch!"
    
    p "Warum klappt das nicht?"
    e "Hey, mach irgendwas!"
    play sound Magie1
    p "Ich kann mich nicht bewegen!"
    e "Ich auch nicht! Was ist das für ein Zauber!"
    e "Wir haben verloren!"
    p "Wir haben nur verloren, wenn du aufgibst!"
    p "Vielleicht musst du dich einfach mal mehr durchsetzen!"
    hide monster with moveoutbottom
    e "EEEK!"
    show monster n at center with moveinbottom
    show eve pnpask at leftish with moveinbottom
    p "WEHR DICH DOCH!"
    e "Ich kann nicht! Ich will nicht! Ich darf nicht!"
    menu:
        "Es ist nur ein Spiel!":
            p "Ist doch nicht so schlimm."
            e "Wie kannst du sowas sagen?"
            p "Was ist denn jetzt dein Problem?!"
            e "AAAAAAH"
            stop music
            scene hut with dissolve
            show eve mad
            play music spookywald3 fadein 1.0
            e "DU IDIOT MUSST MIR ALLES RUINIEREN!"
            hide eve with moveoutright
            p "Evelynn..."
            e "BLEIB WEG"
            play sound cardoor2
            scene bg street
            show mum talk at leftish with dissolve
            m "Na, und wie war's?"
            p "...ganz gut..."
            n "Irgendwie war es nachdem Evelynn weggegangen ist, nicht mehr so toll."
            n "Sie hat nicht ein Wort mehr mit mir geredet. Dabei hat es doch soviel Spaß gemacht!"
            show emum n at slightright
            show edad n at right
            show mad at rightish
            with moveinright
            n "Sogar jetzt guckt sie mich nur böse an"
            show mum nett
            m "Hey, Püpschen, ich rede mit dir!"
            emum "...ich hab dir gesagt, dass das keine gute Idee ist! Und jetzt sieh dich an, ganz eingedreckt bist du!"
            edad "Hoffentlich hast du dir keine Zecke geholt. Das nächste Mal, bleibst du einfach lieber wieder Zuhause!"
            e "..mh hm..."
            hide emum n
            hide edad n
            hide eve mad
            with moveoutleft
            p "...ich bin müde..."
            m "Nanu, so kenn ich dich ja gar nicht! Hast du gar nichts Spannendes zu erzählen?"
            scene bg black with fade
            jump sceneevebad
            
            ###move on to bad ending
        
        "Tu es einfach, schlimmer kann es nicht werden!":
            p "Das ist doch dein Problem!"
            p "Du musst nur mehr an dich glauben!"
            e "[name]!"
            p "Du schaffst das schon. Du bringst mir andauernd neue Sachen bei."
            p "Du weißt soviel, bist besser als alle im Malen und dann darfst du doch nicht aufgeben."
            e "Aber..."
            p "Kein aber! Leuchttürme können auch nur im Dunkeln leuchten!"
            n "Das hab ich irgendwo mal in einem Glückskeks gelesen... ich weiß eigentlich gar nicht was das bedeutet. Aber Evelynn mag doch Leuchttürme."
            stop music fadeout 1.0
            play music fantasyboss2 fadein 1.0
            show eve pnpmad
            e "IN SCHLING UND DONNERTAL! BLEIBT MIR KEINE WAHL!"
            show monster n with moveinbottom
            p "Ich kann mich wieder bewegen!"
            show monster n at rightish with move
            "Königsfüßler" "NEIN!"
            show monster n at right with move
            e "HÖR DEN HALL UND SPÜR DEN WALL!"
            show monster plants at right with dissolve
            "Königsfüßler" "Das darfst du nicht!!! Das ist gefährlich!!!"
            e "Jetzt greif ihn an, wo er nicht geschützt ist!"
            play sound Whoosh3
            p "Mitten ins Gesicht!"
            "Königsfüßler" "EVELYNN!!!!"
            show monster dead with dissolve
            e "..."
            hide monster with dissolve
            stop music fadeout 4.0
            e "...wir...."
            play music fantheme2 fadein 1.0
            show eve pnpask
            e "Wir habens geschafft."
            show eve pnpvhappy
            e "WIR HABENS GESCHAFFT!"
            p "Ich wusste, du kannst das."
            e "Ja, ja, JA!"
            p "..."
            p "Und jetzt?"
            show eve pnp2
            p "Wollen wir unsere Belohnung von der Stadt abholen?"
            e "Gerne können wir das noch machen."
            scene bg caveentry with dissolve
            show eve pnp2
            p "Moment mal!"
            show eve pnpask
            e "Was ist denn?"
            p "Ich muss dich jetzt was Fragen, bevor ich's vergesse."
            e "Hmmmh?"
            p "Sag mal... ist das mit deinen Eltern real gewesen?"
            stop music fadeout 1.0
            scene hut with dissolve
            play music evetheme fadein 1.0
            show eve talk2 with dissolve
            e "Wieso das denn?"
            p "Darfst du daheim echt nichts machen?"
            show eve mad
            e "Nein, ich darf auch nicht zu Freunden oder so. Da sind meine Eltern ganz streng."
            p "Evelynn, willst du zu mir heute mit nach Hause?"
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
            k "So Kinder, packt mal langsam wieder euer Zueg zusammen!"
            scene bg street
            play sound cardoor2
            show mum talk at leftish with dissolve
            m "Na, und wie war's?"
            p "Supertoll! Wir waren in einer Stadt mit Burg, und da war ein Monster! Und Fledermäuse! Und eine Riesenpizza! Aber Evelynn hat das Monster dann besiegt, und die Pizza haben wir..."
            m "Oh hey, immer mit der Ruhe! Ich komm gar nicht mehr mit."
            m "Was für eine Burg? Ich dachte ihr habt euch eine Waldhütte angeschaut?"
            n "Mann, Erwachsene verstehen auch echt gar nix."
            n "Oh, da drüben ist ja auch Evelynn!"
            show emum n at slightright
            show edad n at right
            show eve happy2 at rightish
            with moveinright
            n "Sie sieht auch aus, als hätte sie Spaß gehabt."
            show mum nett
            m "Hey, Püpschen, ich rede mit dir!"
            emum "...ich hab dir gesagt, dass das keine gute Idee ist! Und jetzt sieh dich an, ganz eingedreckt bist du!"
            edad "Hoffentlich hast du dir keine Zecke geholt. Das nächste Mal, bleibst du einfach lieber wieder Zuhause!"
            show eve mad
            e "..."
            e "Mir hat's Spaß gemacht."
            show eve happy2
            e "Das war der allertollste Tag überhaupt!"
            emum "...was willst du denn jetzt damit sagen?"
            hide eve happy2
            with moveoutleft
            emum "...Evelynn?!"
            hide emum n
            hide edad n
            with moveoutleft
            p "Mama, darf ich am Wochenende vielleicht Evelynn besuchen? Wir wollten zusammen malen und vielleicht einen Schatz suchen gehen oder andere Abenteuer."
            show mum talk
            m "Also, von mir aus ja. Ich kann ja später mal ihre Eltern anrufen und fragen."
            scene bg black with fade
            jump sceneevegood
    
label sceneevegood:
    stop music fadeout 4.0
    scene eve goodend
    play music GoodEnd fadein 1.0
    n "Der Wandertag ist jetzt schon 3 Wochen her. Bald bin ich groß genug und darf in die Schule!"
    n "Aber der Ausflug war wirklich lustig. Und Evelynn ist seit dem auch ganz anders."
    n "Sie redet viel mehr, auch mit den Anderen. Und neulich haben wir sogar alle zusammen einen schwarzen Magier besiegt, der das ganze Königreich erobern wollte!"
    n "Octavia sagt, dass wir das nur ihretwegen geschafft haben, aber Evelynn hat auch ganz viel gemacht."
    n "Eigentlich sogar fast alles, weil Octavia sich andauernd mit Anja streitet, ob Elfen oder Zwerge besser im Kämpfen sind."
    n "Und einmal haben wir dann an einem Wochenende alle bei Evelynn Zuhause gespielt. Da gabs dann auch wieder Riesenpizza."
    n "Und diesmla sogar ganz in echt!"
    stop music fadeout 1.0
    jump credits



label sceneevebad:
    stop music fadeout 4.0
    scene eve badend
    play music BadEnd fadein 1.0
    n "Der Wandertag ist jetzt schon 3 Wochen her, aber Evelynn ist immernoch sauer auf mich."
    n "Sie redet kaum noch mit mir und spielen will sie auch nicht mehr."
    n "Im Grunde sitzt sie einfach nur noch irgendwo alleine und malt..."
    n "Und bei den anderen Ausflügen war sie auch nicht mehr mit dabei..."
    n "Aber bald bin ich schon groß und darf ich die Schule!"
    n "Vielleicht finde ich ja da Freunde..."
    stop music fadeout 1.0
    jump credits
    
    


    return
