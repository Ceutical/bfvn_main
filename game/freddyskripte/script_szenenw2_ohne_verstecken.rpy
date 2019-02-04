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
define rmum = Character("Randy's Mutter") ### new
define nvln = Character(name=None, kind=nvl)

######################################

##### MUSIC DEFINITIONS #####

define audio.introtheme = "music/soundtracks/introtheme.mp3"
define audio.anjatheme = "music/soundtracks/anjatheme.mp3"
define audio.evetheme = "music/soundtracks/evetheme.mp3"
define audio.octatheme = "music/soundtracks/octatheme.mp3"
define audio.maintheme = "music/soundtracks/maintheme.mp3"
define audio.happy1 = "music/soundtracks/Happy_Theme1.ogg"
define audio.Whoosh3 = "music/sfx/Whoosh3.ogg"
define audio.Ball_Getroffen1 = "music/sfx/Ball_Getroffen1.ogg"
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


transform flight:
    xalign .5
    yalign .4

transform flightright:
    xalign .8
    yalign .4


transform rotation:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 10
    

######################################


label start:
    play music introtheme

    ##### AFFINITY SYSTEM INITIATE #####
    $ randyname = True
    $ hasknappers = True
    $ snackersdeal = True
    $ anjatreat = True
    $ octa_points = 1
    $ eve_points = 4
    $ anja_points = 3
    $ paper =""
    $farbflug = ""
    $dynamik = ""
    $chaos =""
    $tip =""
    $ seekwin = "True"
    $ seekloss = ""

    
    ##### AFFINITY SYSTEM END #####
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
            suf2 = "" ### neu
            ddd = "der" ### neu
    else:
        python:
            pro = "ihr"
            pro2 = "sie"
            pro3 = "ihr"
            pro4 = "Tochter"
            pro5 = "sie"
            suf = "e"
            suf2 = "in" ### neu
            ddd = "die" ### neu

label scenew2_2:
    
    menu:
        "Tag 2":
            "YEET"
            jump scenew2_8
        
        "Tag1":
            "And so it begins."
    

label scenew2_4:
    play music introtheme
    scene bg grura
    n "...oder auch nicht. Wieso wurde alles aufgeräumt?"
    show karin go
    k "Kinder! Alle herkommen! Der Morgenkreis fängt an!"
    show karin talk
    k "Diesen morgen wollen wir uns erst einmal alle ein bisschen aufwärmen."
    k "Ich zeige euch etwas und ihr versucht mir das dann nach zu machen, okay?"
    "Alle" "Ja, machen wir Karin."
    show karin vhappy
    k "Denn wenn wir heute fertig sind mit unserem Morgenkreis gehen wir gemeinsam nach draußen."
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
    show bg black with dissolve
    k "So, die dritte Übung ist folgende."
    hide karin with moveoutbottom
    k "..."
    k "Genau, so wie bei Octavia!"
    O "ist auch voll leicht."
    k "Nun, weiter..."
    n "..."
    stop music fadeout 1.0
    play music maintheme
    show bg court with dissolve
    n "Endlich ist das vorbei."
    n "Das wurde ja echt anstregend mit diesem komischen Hund hab ichs irgendwie gar nicht mehr verstanden."
    n "Naja, wenigstens darf ich mich ausruhen."
    a "Dich krieg ich noch."
    o "Vielleicht in 100 Jahren!"
    n "Moment. Wieso rennt jeder rum."
    n "Ich kann ja trotzdem zu..."
    k "Evelynn, tut mir Leid. Dass ist die letzte Kreide."
    e "Danke Karin."
    n "Dann muss ich wohl wo mit machen, doch wo?"
    
    menu:
        "Sandkasten":
            n "Im Sandkasten ist es wohl wenigstens immer noch entspannt, dann auf zu den!"
        
        "Ball spielen":
            n "Wenn jeder spielt, dann muss ich wohl auch mit machen."
        
label scenew2_5:
    "Hier ist das Ende der Demo!"

label scenew2_6:
    scene bg grura2
    play music maintheme
    show karin n at right
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
    k "Das nächste mal, wenn Sie sich so sehr verspätet soll Sie bitte den Kindergarten anrufen."
    k "Aber das kann ich ihr dann wohl auch selbst sagen, keine Sorge. Jetzt warten wir einfach zusammen."
    hide karin
    scene bg black
    k "Die ist bestimmt bald da."
    n "..."
    n "..."
    n "Karin?"
    k "hmmh?"
    n "ach nichts..."
    n "pffff..."
    scene bg grura
    n "Endlich!"
    show mum n at left with moveinleft
    show karin mad at right
    m "Na mein Schatz? Du wartest sicherlich schon ewig hier, oder? Tut mir leid, aber lass uns gleich nach Hause gehen!"
    m "Tut mir Leid Karin, ich bin einfach nicht mit der Arbeit fertig geworden und konnte es auch nicht aufschieben."
    k "Kein Problem, dass kann zwar passieren aber, bitte geben Sie mir bescheid oder rufen Sie mich an."
    k "Ich konnte Sie auch nicht erreichen, als ich versucht habe Sie anzurufen."
    show mum mad
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
    n "Wieso ist Mama so müde?"
    p "Willst du schlafen?"
    m "Nichts lieber als das, also heute."
    p "Ich bin auch müde!"
    m "Ach so..."
    "next day" ###Transition
    
label scenew2_7:
    scene bg street
    play music maintheme
    play sound audio.cardoor1
    show mum n at rightish
    n "Es ist schon wieder ein neuer Tag, ich bin gespannt wie es heute wird!"
    n "Moment."
    p "Mama, wieso steigst du mit aus?"
    show mum talk
    m "Hmmh?"
    m "Ach, ich wollte nur mal mit reinschauen."
    show mum n
    n "Man, bin ich heute müde!"
    n "Ich kann kaum die Augen offen halten."
    show mum talk
    m "Schatz. Sag mal. Wie ist es eigentlich hier im Kindergarten?"
    m "Sind alle nett zu dir unt hast du mittlerweilie auch schon andere Freunde außer Randy kennengelernt?"
    p "Was?"
    n "Ich kann mich gar nicht darauf konzentrieren, was Mama sagt."
    p "Warum bist du eigentlich reingekommen? Ich finde doch selbst den Weg. Bin ja kein Baby mehr!"
    show mum happy
    m "Ach, ich wollte nur kurz mit Karin reden."
    n "Was will die mit Karin bereden?"
    show mum n
    m "Hab einen schönen Tag und spiel diesmal nicht mit deinen Videospiel-Teil!"
    hide mum with moveoutright
    n "und weg ist sie im Nebenzimmer, was die wohl besprechen?"
    n "Ich hör einfach mal zu!"
    scene bg office
    show mum talk at leftish
    show karin n at rightish
    m "...kann ich gut verstehen.Und hat sich [name] schon mit anderen Gleichaltrigen angefreundet?"### Flagge und Affinitycheck
    

    if anja_points > octa_points and anja_points > eve_points :
        $anjaday = "True"
        show karin talk
        k "Ihr [name] ist hier gut aufgehoben und passt wunderbar in unsere bunte Gruppe."
        k "Am meisten ist [name] mit Anja unterwegs."
        k "Die beiden sind ständig am Quatschen, wobei ehrlich gesagt, Sie mehr als [name]."
        show mum happy
        k "aber beide wirken recht aufgeweckt."
        show karin n
        m "Und was ist diese Anja für ein Typ?"
        k "Oh Anja. Das ist eine ga... und außerdem..."
        scene bg black with dissolve
        n "Nanu!"
        scene bg office with dissolve
        show mum mad at leftish
        show karin go at rightish
        k "Nun, sie --- relativ neu. Es macht Sinn, dass die beiden --- kommunikativ und gut im zuhören."
        k "Am Freitag werde---"
        show mum happy
        show karin n
            
    elif eve_points > anja_points and eve_points > octa_points:
        $eveday = "True"
        show karin talk
        k "Ihr [name] ist ein wirklich kreatives Kind, weswegen es kein WUnder ist, dass [pro2] sich so gut mit Evelynn versteht."
        k "Die beiden sind ständig am Maltischu und produzieren ihre kleinen Kunstwerke."
        show karin go
        k "Evelynn ist ein Naturtalent und manchmal frag ich mich, ob Sie besser malen kann als ich. Zumindest was Beleuchtung angeht."
        k "[name] hat sich deshalb auch unter ihrer Kritik auch künstlerisch stark verbessert."
        show mum happy
        m "Das ist ja gut. Und was für ein Typ ist diese Evelynn?"
        k "Musikalisch talentiert, sehr talentiert, aber--- "
        scene bg black with dissolve
        n "Nanu!"
        scene bg office with dissolve
        show mum mad at leftish
        show karin go at rightish
        k "Leider ein --- zurück--- Mädchen. Beidenehmen---Freundschaft mit, denn--- Kokon heraus."
        k "Am Freitag werde..."
        show mum happy
        show karin n
        
    elif octa_points > anja_points and octa_points > eve_points:
        $octaday = "True"
        show karin go
        k "[name] ist wirklich sehr ergeizig und gibt sich mit allem was er macht wirklich mühe."
        k "Das ist schon bemerkenswert für [pro] Alter, deswegen wundert es mich auch nicht, dass [pro2] sich mit den, wie soll ich sagen, Musterkind Octavia angefreundet hat."
        show karin n
        show mum mad
        m "Hmmmh..."
        m "Und was ist diese Octavia für ein Typ?"
        show karin happy
        k "Ein richtiger Engel. Unkompliziertz, aber wenn --- Spiele--- nur einen Hauch von Wettbewerb."
        scene bg black with dissolve
        n "Nanu!"
        scene bg office with dissolve
        show mum mad at leftish
        show karin go at rightish
        k "...deshalb ist es gut, dass [name] jetzt hier ist --- jemandern der [pro2] fordert."
        k "Deshalb, werde ich am Freitag..."
        show mum happy
        show karin n
            
    else:
        $boo = "True"
        show karin shock
        k "Leider scheint er/sie ja eher zurückgezogen zu sein. Zwar bemüht sich Ihr Kind immer wieder, aber so richtig klappen will es scheinbar nicht. Zumindest, soweit ich das beurteilen kann." 
        k "Wenn Sie wollen, werde ich Freitag mal ein genaueren Blick auf ihn/sie werfen."            
        show mum talk
        m "Was ist denn am Freitag?"
        show karin talk
        show mum n
        k "Ich dachte, Frau Heidenau hätte allen Eltern bescheid gegeben, dass wir zur Bernerhütte im Eichelgebirge wandern."
        show mum talk
        m "Ein Wandertag also? Nein, davon habe ich nichts gehört."
        show karin shock
        k "Entschuldigen Sie vielmals. Möchten Sie denn, dass ihr Kind mitkommt? Bis auf eine Brotzzeit und etwas zu trinken wird [pro2] nicht brauchen."
        m "Bei mir spricht eigentlich nichts dagegen, wann genau muss ich mein Kind dann abholen?"
        show karin vhappy
        k "Es könnte etwas später werden, wohl etwa gegen 14 Uhr vermutlich..."
        n "Wieso sagt mir denn niemand von einen Wandertag!"
        jump secenew2_8
        
            
    n "Ich versteh gar nichts mehr, wieso sind die soweit weg von der Tür aufeinmal."
    n "Dann halt näher ran."
    show mum talk
    m "Was ist denn am Freitag?"
    show karin talk
    show mum n
    k "Ich dachte, Frau Heidenau hätte allen Eltern bescheid gegeben, dass wir zur Bernerhütte im Eichelgebirge wandern."
    show mum talk
    m "Ein Wandertag also? Nein, davon habe ich nichts gehört."
    show karin shock
    k "Entschuldigen Sie vielmals. Möchten Sie denn, dass ihr Kind mitkommt? Bis auf eine Brotzzeit und etwas zu trinken wird [pro2] nicht brauchen."
    m "Bei mir spricht eigentlich nichts dagegen, wann genau muss ich mein Kind dann abholen?"
    show karin vhappy
    k "Es könnte etwas später werden, wohl etwa gegen 14 Uhr vermutlich..."
    n "Wieso sagt mir denn niemand von einen Wandertag!"
    "End of scene"
    hide karin
    hide mum
    scene bg black
    
label scenew2_8:
    play music maintheme
    scene bg grura with dissolve
    show karin mhappy
    k "So Kinder, für heute sind wir erst einmal fertig!"
    k "Dann viel Spaß beim Spielen!"
    hide karin with dissolve
    n "Was soll ich denn nach dem Morgenkreis machen? Ich weiß nie was ich machen will..."
    r "Hey [name]!"
    n "Randy kommt in meine Richtung, will der vielleicht spielen?"
    show randy talk at rightish
    r "Wir wollen verstecken spielen, wir brauchen noch jemand der suchen will."
    r "Hast du Lust mitzumachen?"
    
    menu:
        "Verstecken spielen":
            p "Ja, ich weiß eh nicht was ich machen soll."
            show randy happy
            r "Alles klar!"
            
        "Was anderes machen":
            p "Ich bin mir noch nicht wirklich sicher was ich machen will..."
            show randy shock
    
    play sound Whoosh3
    show papierflieger at flight with moveinleft
    hide papierflieger with moveoutright
    play sound Ball_Getroffen1
    p "AUAA! Mein Auge!"
    p "Das war gemein, wer war das?"
    o "TUT MIR LEEEID!"
    stop music fadeout 1.0
    play music octatheme
    show octa happy at leftish
    n "Jetzt kcihert sie. Aber das ist überhaupt nicht lustig!"
    p "Was sollte denn das!"
    show octa smug
    o "Jetzt stell dich doch nicht so an, ich hab mich doch schon Entschuldigt!"
    o "Wenn du willst, dann darfst du auch einen zurückwerfen. Oder wir machen einen Wettbewerb daraus!"
    o "Meine Papierflieger sind eh die besten."
    show randy talk
    r "Wenn du willst, kannst du auch versuchen gegen Sie zu gewinnen!"
    n "Hmmh, Papierflieger basteln oder verstecken spielen?"
    
    menu:
        "Verstecken spielen":
            $seek = "True"
            p "Ne, ich wollte eigentlich schon lieber verstecken spielen. Papierflieger sind mir egal!"
            show octa shock
            show randy happy
            o "Was?"
            r "Super."
            o "Na gut, dann halt nicht."
            jump suchen
            
        "Papierfliegerwettbewerb":
            $paper = "True"
            p "Also Papierflieger hört sich schon lustig an."
            show randy happy
            r "Ich hab auch irgendwie lust drauf!"
            show octa vhappy
            o "Wird sicherlich lustig euch zu besiegen."
            p "Werden wir ja sehen."
            jump wettbewerb
        
        
label wettbewerb:
    hide octa with dissolve
    hide randy with dissolve
    show bg bastel with dissolve

    n "Ich will unbedingt einen besseren Flieger als Octavia bauen!"
    n "Doch wie soll mein Papierflieger am besten aussehen, damit ich Sie besiege?"
    n "Wie falte ich so ein Ding überhaupt?"
    
    menu:
        
        "Mitte Falten":
            n "Erst einmal das Ding in der Mitte machen, dass haben ja alle Flieger!"
            n "Dann noch die Flügel, doch wie soll ich die Flügel machen?"
            
            menu:
                "breit":
                    $dynamik = "True"
                    n "Zum gewinnen braucht es viel Luft und Wind, deswegen sind wohl Breite Flügel klüger!"
                    scene bg black with dissolve
                    n "Dann noch hier etwas."
                    n "Eine Kante noch."
                    n "Ne moment."
                    n "Hab ich irgendwas vergessen? Ach was!"
                    n "Fertig!"
                    
                    
                "schmal":
                    n "Wenn er dünner ist, dann kann ich ihn schneller werfen und so kom ich sicher weiter als Octavia!"
                    scene bg black with dissolve
                    n "Jawohl, so wirds gemacht!"
                    n "Klassisch."
                    n "Also eigentlich."
                    n "Eigentlich bin ich ja fertig!"
                    
            
        
        "Spitze Falten":
            $tip = "True"
            n "Ich habe mal gehört, dass die Spitze das wichtigste ist."
            n "Wenn das stimmt, gewinne ich hunderprozentig!"
            n "Freu ich mich schon auf Octavias Gesicht!"
            n "Jetzt fehlt aber noch was!"
            n "Ach ja!"
            
            menu:
                "Farbe":
                    $farbflug = "True"
                    n "Ich muss Octavia auch mit Stil besiegen!"
                    scene bg black with dissolve
                    n "Dann mal los, ich hab ja hier die ganzen Farben."
                    n "Etwas Orange und Gelb."
                    n "Fert... Moment, Flügel!"
                    n "So, dass wird schon hinhauen."
                    n "Jetzt aber wirklich, fertig!"
                    
                "Flügel":
                    $dynamik = "True"
                    n "Zum gewinnen braucht es viel Luft und Wind, deswegen sind wohl Breite Flügel klüger!"
                    scene bg black with dissolve
                    n "Dann noch hier etwas."
                    n "Eine Kante noch."
                    n "Ne moment."
                    n "Hab ich irgendwas vergessen? Ach was!"
                    n "Fertig!"                   

                                                                         
        
        "Einfach loslegen!":
            $chaos = "True"
            n "Ach, dass wird schon irgendwie klappen."
            scene bg black with dissolve
            n "Erst einmal etwas hiervon. Etwas davon."
            n "Nein, nein so nicht, nochmal zurück."
            n "Geht das noch?"
            n "Einfach in die Form eines Flugzeugs bringen."
    
    
    scene bg grura2 with dissolve
    n "So, fertig. Sieht doch ziemlich cool aus!"
    n "So, Octavia hat gesagt ich darf zurückwerfen. Das mache ich jetzt einfach!"
    show octa happy at rightish
    n "Sie faltet gerade auch einen Flieger, also gut zielen uuuuund"
    p "LOS!"
    
    if chaos == "True":
        show papierkneul at flight with moveinleft
        hide papierkneul with moveoutbottom
        n "Oh mist, dass ist ja gar nichts!"
        n "Hat das wer gesehen?"
        n "Zum Glück nicht, oh was mach ich nur."
        n "Ich will nicht ausgelacht werden..."
        n "Ich glaube... Ich glaube ich verstecke mich lieber für heute."
        hide octa
        show bg cuddle with dissolve
        n "Hier findet mich heute niemand mehr, erst wenn meine Mutter kommt."
        n "Das dauert hoffentlich nicht mehr lang."
        n "..."
        n "..."
        scene bg black with dissolve
        n "..."
        n "*schnarch*"
        n "*schnarch*"
        k "Oh mann, meine Mutter ist schon da?"
        jump scenew2_9
        
    elif dynamik == "True":
        show papierflieger_stromlinienförmig at flight with moveinright
        hide papierflieger_stromlinienförmig with moveoutleft
        
    elif farbflug == "True":
        show papierflieger_bunt with moveinright
        hide papierflieger_bunt with moveoutleft
        
    else:
        show papierflieger with moveinleft
        hide papierflieger with moveoutright
    
    show octa shock
    n "Zwar getroffen, aber nicht richtig."
    o "Was soll denn..."
    show octa smug
    o "Ach so, das war nicht schlecht. mein Flieger ist trotzdem viel besser als die anderen hier!"
    o "Wollen wir schauen wessen am weitesten fliegt?"
    n "Oh, wie es aussieht sind da noch mehr leute die mitmachen."
    n "Anja hat ihren angemalt, Randy geht für den Klassiker und Evelynn."
    show origami at flight
    n "Ein Vogel? WOW! Der kann sicher fliegen solange es kein Pinguin ist!"
    hide origami
    o "Kommt mal alle ran, wir werfen unsere Flieger hintereinander und wer am weitesten kommt gewinnt!"
    a "Alles klar!"
    r "Dann zeig ichs dir Octavia!"
    hide octa
    o "So, alle bereit?"
    o "Ich wirf als erstes und dann schaut ob ihr so weit kommt!"
    show papierflieger_stromlinienförmig at flight with moveinright
    hide papierflieger_stromlinienförmig with moveoutleft
    show papierflieger_bunt at flight with moveinright
    hide papierflieger_bunt with moveoutleft
    a "Fast!"
    o "Nacheinander!"
    show papierflieger at flight with moveinleft
    hide papierflieger with moveoutright
    p "Randy?"
    o "Was machst du denn jetzt?"
    n "Dann bin nurnoch ich übrig!"
    
    if dynamik == "True" and tip == "True":
        show papierflieger_stromlinienförmig at flightright with moveinright
        hide papierflieger_stromlinienförmig with moveoutleft
        n "WOOOAH!"
        show octa shock at rightish
        a "[name] ist weiter als Octavia!"
        r "Ich glaubs nicht!"
        o "Aber... nur um ein paar Zentimeter!"
        o "Außerdem hast du mich ja abgelenkt als du ihn auf mich geworfen hast."
        o "Beim nächsten gewinne ich!"
    
    elif dynamik == "True":
        show papierflieger_stromlinienförmig at flight with moveinright
        hide papierflieger_stromlinienförmig with moveoutleft        
        p "So knapp!"
        show octa smug
        o "Nicht schlecht."
        a "Noch mal, dann gewinnst du sicher [name]!"
        o "Niemals, aber ich hab auch nicht wirklich lust das nochmal zu machen. Mir reicht einmal gewinnen."
        hide octa
        n "Hmmh..."
    
    elif farbflug == "True":
        show papierflieger_bunt at flight with moveinright
        hide papierflieger_bunt with moveoutleft
        p "So knapp!"
        show octa smug
        o "Nicht schlecht."
        a "Noch mal, dann gewinnst du sicher [name]!"        
        o "Niemals, aber ich hab auch nicht wirklich lust das nochmal zu machen. Mir reicht einmal gewinnen."
        hide octa with moveoutright
        n "Und da ist sie weg."
        show eve happy2
        e "Du [name], ich mag deinen Flieger."
        p "Du hast einen ganzen Vogel gemacht, kannst du mir zeigen wie das geht?"
        show eve vhappy2
        e "Ja sehr gerne, zunächst must du..."
        hide eve
    
    else:
        show papierflieger2 at flight with moveinright
        hide papierflieger2 with moveoutleft
        p "Hmmmh."
        show octa smug
        o "Sag ichs doch."
        r "Was will man denn erwarten."
        o "Genau, meiner ist der beste. Hab ichs euch doch gesagt. Ich mach dann mal was anderes."
        hide octa with moveoutright
        n "Hmmh."
        p "Du Evelynn, wie hast du eigentlich einen ganzen Vogel gemacht?"
        e "Das ist einfach, zunächst must du..."
    
    k "[name]!"
    n "Nanu?"
    show karin talk at leftish
    k "Deine Mutter wartet draußen, die ist heute etwas früher da."
    p "Oh."
    k "Ja, dann helf ich dir schnell beim anziehen und..."
    p "Ich kann das schon alleine."
    hide karin with dissolve
    scene bg flur with dissolve
    n "Hier sind meine Schuhe und meine Jacke."
    n "Ach mann, wenn Schuhe nicht sooo..."
    n "Ich brauch wieder Klettverschluss..."
    
    
    
    jump scenew2_9


label suchen:
    
    "Hier wird gesucht!"    
    
    
label scenew2_9:
    play music happy1
    show bg street with dissolve
    show mum talk at rightish
    m "Hallo mein Schatz! Wie ist es denn geloffen? Hattest du einen schönen Tag?"
    p "Ähhm. Ja."
    m "Was hast du denn heute so gemacht?"
    
    if paper = "True":
        p "Flieger gebastelt!"
        p "Also, aus Papier."
        p "Und dann haben wir uns abgeworfen, dass war lustig."
        show mum happy
        p "Das müssen wir daheim auch mal machen!"
        p "Zeig mir wie du das machst!"
    
    elif seekwin = "True":
        p "Wir haben heute alle zusammen verstecken gespielt und ich musste suchen." 
        p "Ich musste die Augen zu machen, dann drei mal bis 20 zählen und ich hab gewonnen."
        show mum happy
        p "Alle gefunden!"
        
    else:
        p "Wir haben heute alle zusammen verstecken gespielt und ich musste suchen." 
        p "Ich musste die Augen zu machen, dann drei mal bis 20 zählen und dann suchen."
        show mum n
        p "Konnte Sie aber nicht alle erwischen, ich war zu langsam und dann sind Sie aus ihren verstecken gekommen."
        p "Leider verloren."

    show mum talk
    m "Naja, hört sich ja nach einer schönen Zeit an!"
    m "Ich muss dir noch etwas sagen: Wusstest du, dass ihr am Freitag Wandertag habt?"
    p "Ähm, nein..."
    show mum happy
    m "Ich hab dich gleich mal angemeldet, dass wird sicher toll."
    m "Du wirst da ganz viel Spaß haben."
    p "Du hast mich angemeldet? Aber was, wenn ich keine Lust habe?"
    show mum talk
    m "Sei mal nicht so. Wandertage sind immer schön, durch die gegen mit deinen Freunden laufen, ein bisschen Erkunden und spielen!"
    m "Ich mochte die Immer."
    show mum happy
    p "Klingt ja gar nicht so blöd."
    
label scenew2_12:
    play music happy1
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
    
    if eve_points > anja_points and eve_points > octa_points:
        $ scenario = "eve"
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
    
    elif octa_points > anja_points and octa_points > eve_points:
        $ scenario = "octa"
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
    
    else:
        $scenario = "anja"
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
    
    

    return