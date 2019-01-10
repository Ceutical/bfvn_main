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
    $ octa_points = 0
    $ eve_points = 0
    $ anja_points = 0

    
    ##### AFFINITY SYSTEM END #####

    
label scene15:
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
    
    scene bg grura
    
    "Es ist Freitag. Also praktisch Wochenende. Da bin ich immer bei Papa. Vielleicht bekomme ich ja wieder Eis und Schokolade als Abendessen?"
    "Hoffentlich!"
    "Außerdem muss ich Papa unbedingt meine Bilder zeigen."
    "So schön wie die von Evelynn sind sie leider nicht, aber fast!"
    "Wo ist Evelynn eigentlich?"
    "Vielleicht weiß Karin ja wo sie ist."
    show karin talk at rightish
    p "Du... Karin..."
    k "Ja [name]?"
    p "Kann ich dich was fragen?"
    show karin happy at rightish
    k "Gerne. Was willst du denn Fragen?"
    p "Wo ist denn Evelynn? Ich find die nicht."
    show karin talk at rightish
    k "Du musst die Evelynn nicht suchen. Die ist heute Zuhause geblieben."
    k "Ihre Mutter muss angeblich etwas einkaufen und braucht dafür Evelynn. Hab leider auch keine genaue Ahnung."
    
    p "Mhhh. Man."
    p "Ist ja voll doof, wollte was mit ihr malen."
    show karin vhappy at rightish
    k "Ich kann ja mit dir malen."
    p "Ne, dass macht dann keinen Spaß!"
    show karin mad at rightish
    k "Also gut..."
    p "Dann halt was anderes."
    hide karin mad with dissolve

    "Scheibenkleister!"
    "Na gut. Dann muss ich eben mit Anja den Tag verbringen."
    "Die hat sicherlich wieder viel zu erzählen, außerdem muss man die nicht suchen. Anja hört man immer!"
    
    a "Gar nicht wahr!"
    stop music fadeout 1.0
    play music anjatheme
    "Ich hör Sie sogar jetzt."
    a "Mit den hula hoop Reifen bin ich viel besser als du!"
    "Was is da los? Ich sollte mal nachschauen."
    show anja mad at rightish
    show octa mad at leftish
    o "Ich kann ihn bis zu 32 mal drehen bis er umfallen wird."
    a "Stimmt doch gar nicht. So schnell kann man nicht mal zählen!"
    show octa smug at leftish
    o "Für dich wohl. Ich kann das aber schon!"
    a "Lügnerin!"
    show octa vmad at leftish
    o "Nenn mich nicht so, wenn ich keine bin!"
    a "Aber, du kannst das nicht!"
    o "Kann ich wohl!"
    "Irgendwie blick ich nicht durch, aber eigentlich hört sich hula hoop lustig an"
    p "Darf ich vielleicht den Reifen haben?"
    "{color=#0099ff}Octavia:{/color} Du erst recht nicht! \n{color=#0099ff}Anja:{/color} Gerade nicht!"
    "Wie es aussieht bin ich hier nicht erwünscht. Ich sollte wohl einfach gehen."
    hide octa vmad with dissolve
    hide anja vmad with dissolve
    stop music fadeout 1.0
    play music maintheme
    "Och man, was soll ich dann machen... Murmelbahn vielleicht? Auch langweilig..."
    "Hmmh..."
    #### zweiter Hintergrund
    "(einige Zeit vergeht mit grüblen)"
    "Was solls, auf zur Murmelbahn!"
    "(weitere Zeit vergeht)"
    p "Dann kommt das noch hier hin und dann..."
    p "LAAANGWEILIG!"
    if randyname == True:
        r "Da, [name]"
        p "hmmh?"
        show randy happy at leftish
        "Ich hörte Randys Stimme von hinten. Also drehe ich mich um. Randy steht mit einer Karte in der Hand, die er mir entgegenhält."
        r "Du bist zu meiner Monster Party eingeladen!"
        p "Was ist das?"
        show randy vhappy at leftish
        r "Wir verkleiden uns als Monster! Das wird voll cool!"
        p "Moment, warum?"
        r "Ich hab dich zu meinen Geburtstag eingeladen und ich möchte, dass wir uns alle verkleiden können."
        "Ich nehme die Einladung an und schaue auf die Karte und lese vor:"
        p "Ein..laadung zum Kinder... Kindergeb.Geburtstag von Randy!"
        show randy talk at leftish
        r "Genau!"
        r "aber... tut mir leid, dass ich dir das nicht früher gesagt habe."
        p "Wieso?"
        r "Es ist heute, aber wir kannten uns ja nicht und erst Anja hat mir gesagt, dass du mitmachen willst."
        show randy happy at leftish
        r "Ich hoffe du kannst trotzdem kommen... Wie heißt du eigentlich Neuer?"
        p "[name]."
        r "Frag einfach deine Mama, die wird bestimmt nichts dagegen haben. Außerdem wenn du das nicht tust sagt meine Mama du darfst nicht kommen."
        p "Werd ich machen. Anja hat mir erzählt, dass du Monsterfilme anschauen darfst."
        show randy talk at leftish
        r "Stimmt, die sind super. Mein Bruder hat da ganz viele!"
        r "Was hat denn Anja noch so über mich gesagt?"
        p "Schoko ist besser als Vanille."
        show randy mad at leftish
        r "Die hört damit auch nie auf, oder?"
        r "Naja, schön dich kennengelernt zu haben."
        p "WARTE!"
        show randy talk at leftish
        r "hmmh."
        p "Mir ist langweilig, willst du was spielen?"
        r "Gerne. Dann kennen wir uns erst richtig."
        scene bg black with dissolve
        "Wir saßen also beide an der Murmelbahn und erzählten uns voneinander, verbrachten somit also den Vormittag zusammen."
        "Ich hoffe nur, dass meine Mutter mich dann auch zur Feier fährt."
        

    else:
        "???" "Hallo!"
        show randy talk at leftish
        p "Äähm, hallo."
        "???" "Du bist doch der Neue hier! Anja hat mir von dir erzählt. Ich glaube es wäre lustig wenn du mit zu meiner Monsterparty kommst!"
        p "Monsterparty? Gerne!"
        p "Warte. Anja? Du bist doch der mit dem Sie sich gestritten hat."
        r "Ach ja, mein Name ist Randy! Anja hat mir gesagt, dass du [name] bist."
        p "Warte, ich bin verwirrt."
        r "Hier, meine Mutter hat mir diese Karte mitgegeben. Dann wissen deine Eltern wo Sie hinfahren müssen."
        r "Die Party ist übrigens heute, aber weil wir uns nicht kannten, konnte ich dich nicht vorher einladen."
        p "Danke... wieso aber Monsterparty?"
        show randy happy at leftish
        r "Weil wir uns als Monster verkleiden dürfen!"
        p "Ich frag meine Mama ob ich kommen darf."
        r "Alles klar."
        r "Du,[name]. Ich muss aber noch kurz zu jemand anderes, bis später!"
        scene bg black with dissolve
        "Und schon war er weg. Aber ich hoffe, dass meine Mutter mich auf diese Party lässt." 
        "Zurück zur Mur... Murmelbahn... LAAANGWEILIG!"
        
label scene16:
    scene bg grura
    "Nach einiger Zeit spielen tippt mir jemand von hinten auf die Schulter."
    p "huh?"
    show karin n at rightish
    show mum n at leftish
    k "Hey, [name]. Deine Mutter ist etwas früher gekommen um dich abzuholen."
    m "Hallo Klein[suf]. Ich muss noch etwas in der Stadt erledigen und wollte, dass du mitkommst."
    p "in Ordnung."
    "Ich packte also meine Sachen und ging mit Mama zum Auto."
    scene bg street with dissolve
    "Auf der Straße fällt mir wieder etwas ein."
    show mum n at rightish
    p "Mama!"
    m "Ja?"
    p "Ich wurde auf einen Geburtstag eingeladen. Darf ich da hingehen?"
    show mum happy at rightish
    m "Schön, dass du schon Freunde gefunden hast. Meinetwegen gerne. Wann genau ist denn der Geburtstag?"
    "Ich geb ihr meine Einladung"
    p "Da!"
    m "Hmmmh..."
    show mum mad at rightish
    m "15 UHR!"
    m "Wieso bekomm ich das erst jetzt?"
    p "Ich hab die Einladung aber doch erst heute bekommen."
    show mum talk at rightish
    m "Na gut. Ich muss dann aber noch deinen Vater sagen, dass er dich von der Feier abholen soll."
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
    "Man, hier haben Sie ja wirklich alles! Von klassischen Monsterkostümen wie eine Riesenmotte mit bunten Flügeln und Maske, bis hin zu... huh"
    "Ein Tier... Tier... Hasensäbelzahnelchwolf?"
    "Rehhundkatzenkanninchen?"
    p "Mama! Was ist denn das? Das sieht ja falsch aus."
    show mum talk
    m "Hmmmh..."
    m "Ich glaube ein Wolpertinger!"
    p "Ein Wolterdinger?"
    show mum happy
    m "Wolpertinger. Ein Fabelwesen, welches aus ganz vielen Tieren besteht. Das Wesen kommt aus Bayern."
    p "cool."
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
            m "Viel enthusiasmus hier."
            p "Wieso?"
            m "Weil du dich auf das Kostüm freust. Gefällt dir doch, oder?"
            "Ich nicke"
            show mum happy
        
        "Motte":
            $ costume = "moth"
            p "Mofpa!"
            m "Die sieht ja schäußlich aus."
            p "Die ist aus nen ganz coolen Film!"
            m "Wenn du meinst, ich überlass dir heute ja die Entscheidung."
            p "Ja, ich will das Kostüm."
            
        "Wolper...dings":
            $ costume = "wolp"
            p "Wolterdimper. Der ist voll cool!"
            show mum happy 
            m "Gerne kauf ich dir den Wol-Per-Ting-Er, wenn du ihn richtig aussprichst."
            p "Wieso?"
            m "Weil ichs süß finde."
            p "Ok... Wol-Per-Ting-Er... Wolperdinger."
            show mum vhappy
    
    m "Na dann. Ab zur Kasse"
    hide mum vhappy with dissolve
    show bg black with dissolve
    
    "Jetzt wo Ich mein tolles Kostüm habe kann ich auf den Geburtstag gehen!"
    "Das wird sicherlich Super!"
    "Aber erstmal noch mit Mama einkaufen gehen... ob ich wohl rechtzeitig komme?"

label scene17:
    
    play sound cardoor1
    play music maintheme
    show mum talk at rightish
    m "So, wir sind da."
    "Ich steige vollkostümiert aus dem Auto aus und bin schon ganz gespannt was die anderen an haben werden!"
    "Mama nimmt mich an die Hand und führt mich zur Tür und klingelt."
    "kurz darauf geht die Tür auf und meine Mutter sagt:"
    m "So, geh mal zu deinen Freunden. Ich bin dann gleich weg. Vergiss nicht, dein Papa holt dich abends ab."
    p "OK. Tschüss Mama."
    hide mum talk with moveoutright
    "Ich gehe kaum durch die Tür und auf den Flur sehe ich bereits Louis. Dieser geht direkt auf mich zu."
    show lparty n 
    L "Hey,[name]."
    p "Hey, Louis."
    
    if snackersdeal == True:
        L "Und, hast du drann gedacht?"
        p "An?"
        L "Ja, ans Knappers!"
        if hasknappers == True:
            menu:
                "Knappers geben":
                    $ trade = "true"
                    p "Einen Moment... Hier!"
                    show lparty happy
                    L "Gut, dass auf dich verlass ist."
                    p "Jetzt, sind wir quitt, oder?"
                    L "Ja klar. Wenn du noch einmal was willst, komm wieder zu mir."
                    "Du bist doch zu mir gekommen..."
                    L "Wollte mich für unser erstes treffen Entschuldigen. War nicht OK."
                    p "Warum?"
                    L "Hab zu dick aufgetragen."
                    p "Wenn... wenn du meinst."

                    p "Sag mal, was bist du für ein Monster?"
                    show lparty smug
                    L "Dr. Acula! Der weltbekannte Arzt."
                    L "Kennst du den wohl nicht?"
                    p "Natürlich!"
                    "Wenn er weltbekannt ist, dann muss ich ihn ja kennen."
                    L "Also... weißt du wo genau der Eingang ist? Meine Mutter hat mich hier abgesetzt und hier im Erdgeschoss ist niemand."

                
                "Kein Knappers geben":
                    $ trade = "false"
                    p "Ich hab leider keins dabei. Nächste Woche vielleicht?"
                    show lparty mad
                    L "Idiot!"
                    L "Du hast es mir versprochen, du bekommst nichts mehr von mir!"
                    p "Wieso so wütend?"
                    L "Versprechen werden nicht gebrochen!"
                    "Irgendwie ist mir das unangenehm..."
                    p "Was bist du denn eigentlich für ein Monster?"
                    L "Sag ich nicht!"
                    "Wie komm ich aus dieser Situation?"

        else:
            menu:
                "Kein Knappers geben":
                    $ trade = "false"
                    p "Ich hab leider keins dabei. Nächste Woche vielleicht?"
                    show lparty mad
                    L "Idiot!"
                    L "Du hast es mir versprochen, du bekommst nichts mehr von mir!"
                    p "Wieso so wütend?"
                    L "Versprechen werden nicht gebrochen!"
                    "Irgendwie ist mir das unangenehm..."
                    p "Was bist du denn eigentlich für ein Monster?"
                    L "Sag ich nicht!"
                    "Wie komm ich aus dieser Situation?"

    else:
        L "Wollte mich für unser erstes treffen Entschuldigen. War nicht OK."
        p "Warum?"
        L "Hab zu dick aufgetragen."
        p "Wenn... wenn du meinst."
        
        p "Sag mal, was bist du für ein Monster?"
        show lparty smug
        L "Dr. Acula! Der weltbekannte Arzt."
        L "Kennst du den wohl nicht?"
        p "Natürlich!"
        "Wenn er weltbekannt ist, dann muss ich ihn ja kennen."
        L "Also... weißt du wo genau der Eingang ist? Meine Mutter hat mich hier abgesetzt und hier im Erdgeschoss ist niemand."
    
    show lparty really
    "???" "Hallo Kinder"
    "Ich höre eine Stimme, die von oben kommt."
    show lparty really at leftish
    show rmum talk at rightish
    "???" "Hallo Louis und du da musst das neue Kind sein, von den mir mein Sohn erzählt hat."
    rmum "Ich bin Erika, also Randy's Mama Erika. Schön euch zu sehen."
    rmum "Wir haben oben das Zimmer hergerichtet, kommt. Folgt mir."
    rmum "Niedliche Kostüme übrigens."
    p "Danke."
    "Och man. Ich wollte doch furchteinflößend sein, ich bin doch ein Monster!"
    hide lparty really with moveoutright
    hide rmum talk with moveoutright

label scene18:
    show bg party with dissolve
    "Ich schau mich erst einmal um, es sind einige Leute da. Ich seh sogar schon Octavia und Anja! Und Randy spielt mit jemanden den ich nicht kenne."
    "Auf dem Fernseher läuft ein Film: Radzilla vs. Mofpa!"
    r "Hey [name], konntest ja doch kommen."
    if costume == "moth":
        show rparty happy
        r "MOFPA!"
        "Randy spricht mich an und er ist... natürlich Radzilla."
        p "Mein Erzfeind... Irgendwie."
        r "Naja, nicht immer."
        p "Toll, dass du gekommen bist."
        
    else:
        show rparty talk
    
    p "Hier Randy, dein geschenk."
    p "Cooles Kostüm."
    "Irgendwie ist er wohl von etwas abgelenkt."
    r "Danke, mach ich später auf. Leg es bitte auf den Tisch, OK?"
    p "Gerne."
    "Ich lege den Tisch und dreh mich um. Ich sehe nichts besonderes, auf was hat Randy geschaut?"
    hide rparty happy
    if costume == "moth":
        jump scene19
    elif costume == "wolp":
        jump scene20
    else:
        jump scene21
    
label scene19:
    
    "Na dann, auf zum Tisch und Kuchen essen."
    a "Nimm das Mofpa!"
    "Jemand sticht mir an meine Seiten."
    play music anjatheme
    show aparty mad
    p "Hey, lass das!"
    a "Aber du bist doch Böse!"
    p "Nicht immer...Tut trotzdem weh."

    if trade == "true":
        show aparty n
        a "Hehe, Louis hat gesagt du hast Knappers dabei?"
        p "Hatte ich. Louis gab mir auch drei Snackers dafür und ich hab Sie ihn gegeben."
        a "Gut, dass man sich auf dich verlassen kann!"
        
        if anjatreat == "True":
            a "Waren das die die du mir gegeben hast? Ahhhw. Ist ja Süß."
            p "Ja Snackers sind süß."
            show aparty jabber
            a "Oh man. Finde es trotzdem toll, dass du extra Snackers für mich besorgt hast."
            "Was redet die denn?"
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
            a "War nur nen Jucks."
            a "hmmmh?"
            jump scene19f

    elif trade == "false":
        a "Doch bist du!"
        show aparty mad
        p "Was?"
        a "Louis hats mir gesagt. Du bist doof. Du versprichst ihn Knappers, bringst es ihm aber nicht mit!"
        p "Ich konnte noch keine..."
        a "Mach so etwas NIE WIEDER!"
        a "Versprechen bricht man nicht und die anderen finden das auch dumm."

        if anjatreat == "True":
            p "Aber, du hattest doch auch nichts dagegen, als du welche angenommen hast!"
            a "Was?"
            show aparty shock
            p "Ich hab dir doch was abgegeben!"
            show aparty mad
            a "DU VOLLIDIOT HAST MIR GESTOHLENES GEGEBEN?!"
            a "Ich dachte das wäre deins gewesen du Lügner!"
            "Irgendwie kommt es mir so vor, als würde mich jeder anschauen."
            hide aparty mad
            "Ich hab es aber auch irgendwie verdient."
            "Irgendwie fühl ich mich nicht gut, ich versuch aber trotzdem zu feiern."
            "..."
            "..."
            "Einige Zeit vergeht und wie es aussieht nehmen mir die anderen es nicht so übel."
            rmum "Kommt mal alle zusammen ihr kleinen Monsterlein!"
            rmum "Gruppenfoto!"
            "Wenigstens darf ich auch noch auf das Foto."
            rmum "Sagt Käsekuchen"
            "Alle" "Käsekuchen"
        
            scene bg street with Dissolve
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
    "Was ist denn mit Anja los?"
    "Wieso schaut Sie mich so an?"
    a "Ich hab eine Idee!"
    p "?"
    a "Siehst du diese Stadt?"
    p "Die Pappkartons?"
    a "Wenn du schon so angezogen bist, dann mach es wie in den Radzilla Filmen!"
    p "Kämpfen?"
    a "Ja klar. Du bist doch Mofpa. Die Riesenmotte. Und Randy ist Radzilla!"
    p "Ja schon, aber... Ich weiß nicht."
    "Anja zieht an meinen linken Flügel. Die ist stark."
    a "RANDY!"
    show aparty talk at rightish
    show rparty talk at leftish
    r "Ja."
    a "Radzilla, hier, Mofpa da."
    a "LOS!"
    "Jetzt wird Randy auch noch herumkommandiert."
    show rparty happy at leftish
    r "Ich verstehe."
    p "Ich nicht!"
    r "Also in Radzilla gegen Prince Ape, kämpft er gegen Prince Ape und in..."
    a "Er kämpft gegen Mofpa."
    r "In einen Film, eigentlich sind Sie..."
    a "EGAL! LOS!"
    r "Bereit für einen Monsterkampf in der Stadt?"
    menu:
        "bereit":
            "Es ist sein Geburtstag, muss ja sein..."
            p "Bereit!"
    
    a "3"
    a "2"
    a "1"
    a "Los!"
    r "WAAAAH!"
    "Wir kämpften für einige Zeit... ein Tackle hier, etwas ringen. Ein Laserstrahl."
    "Blocken parrieren."
    "Es machte wirklich Spaß..."
    "...Doch nicht für die Stadt, die Pappkartons sind wohl nicht mehr zu gebrauchen."
    "Natürlich gibt es im Anschluss noch Kuchen!"
    p "ooof... Fertig"
    rmum "Keine Müdigkeit vortäuschen."
    rmum "Kommt mal alle zusammen für ein Gruppenfoto."
    "Auch noch so was. Na gut."
    rmum "Los alle. Käsekuchen!"
    scene cg selfiemoth
    "alle" "Käsekuchen!"
    "... Nett."
    
    
    scene bg street with dissolve

    jump scene22

label scene20:
    "Aber da drüben seh ich Evelynn. Ich sollte mal Hallo sagen."
    show eparty talk2
    play music evetheme
    p "Hi, Evelynn."
    e "Wow! Du siehst ja wild aus [name]."
    e "Komm mal mit mir mit."
    p "Wohin denn?"
    show eparty happy2
    "Sie packt mich an meinem Arm und zeigt auf jemanden der sich komisch bewegt, während andere..."
    p "Oh nein!" 
    p "Scharade."
    e "Genau."
    show eparty happy2 at rightish with dissolve
    show rparty talk at leftish with dissolve
    "Ich bin doch schlecht in Scharade"
    r "Hey ihr zwei, spielt dohc mal was vor."
    e "Gleich zu Anfang an?"
    e "Ich wollte doch erst raten."
    p "Genau! Können wir uns nicht erst hinsetzen?"
    show rparty vhappy at leftish
    r "Nein. Ihr seit die Neuen, ihr dürft gleich starten."
    menu:
        "Ich möchte anfangen.":
            show eparty happy2 at rightish
            p "Gut, dann fang ich eben an. Aber Evelynn, du wirst danach auch dran kommen."
            e "Danke trotzdem."
            "Randy gibt mir einen Zettel auf dem steht... natürlich."
            hide rparty vhappy
            "Radzilla..."
            show eparty happy2 at rightish
            show oparty happy at center
            show aparty n at leftish
            
            menu:
                "Dinosauriergebrüll":
                    p "Roooaaaar"
                    show oparty mad
                    show eparty talk2
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
                    "Lampenfieber. OK ich komm darüber."
            
            "Ich sollte wohl noch mehr machen."
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
                    r "Also, so toll hast du den jetzt nicht gespielt. Aber du wolltest wohl etwas kapputt machen."
                    p "Ääääähhhm... Richtig."
                    "Falsch."
            
            show eparty talk2
            r "So,jetzt bist du dran Evelynn."
            e "Jetzt schon?"
            r "Ihr seit die Neuen, also ja."
            e "O... OK."
            "Wir spielen noch ein bisschen und gehen dann zum Kuchen essen über."
            
        "Evelynn darf anfangen.":
            p "Komm Evelynn, du fängst an."
            show eparty mad at rightish
            e "Was? Wieso?"
            p "Wir müssen eh beide spielen und du hast mich hier her gebracht."
            show eparty talk2 at rightish
            e "Na gut."
            r "Evelynn, dein Wort ist..."
            "Randy gibt ihr einen Zettel."
            hide rparty talk
            show eparty talk2 at center
            r "Bereit?"
            e "Ja."
            r "Los."
            show eparty mad at rotation
            "Was macht die da?"
            
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
            
            "Evelynn nimmt einen Karton und stellt sich darauf, ich glaube es könnte..."
            menu:
                "Ein Surfer":
                    "...sein."
                    p "Surfer!"
                    show eparty happy2 at center
                    e "Richtig!"
                    "Wieso staren die mich an?"
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
                            "Wir spielen noch ein bisschen und gehen dann zum Kuchen essen über."
                            
                        "Nichts sagen.":
                            p "..."
                            show eparty mad at center
                            "Evelynn schaut mich einfach weiter an."
                            e "Du bist dran!"
                            r "Stimmt, hier dein Zettel!"
                            "Wir spielen noch ein bisschen und gehen dann zum Kuchen essen über."

                "Noch mehr nichts":
                    "...sein."
                    r "Prince Ape? Der klettert auf Bäume."
                    a "Ein Affe? Das kann stimmen."
                    o "Ääähm. Breitbeiniger Specht?"
                    e "Wooosh."
                    r "Keine Geräusche!"
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
                            "Wir spielen noch ein bisschen und gehen dann zum Kuchen essen über."

                        "Mit dem Rest schweigen":
                            "..."
                            show eparty talk2 at center
                            e "Du bist dran!"
                            r "Stimmt, hier dein Zettel!"
                            "Wir spielen noch ein bisschen und gehen dann zum Kuchen essen über."
                            
                    
                "Baumkletterer":
                    "...sein."
                    p "Kletterer?"
                    r "Prince Ape? Der klettert auf Bäume."
                    a "Ein Affe? Das kann stimmen."
                    o "Ääähm. Breitbeiniger Specht?"
                    e "Wooosh."
                    r "Keine Geräusche!"
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
                            "Wir spielen noch ein bisschen und gehen dann zum Kuchen essen über."

                        "Mit dem Rest schweigen":
                            "..."
                            show eparty talk2 at center
                            e "Du bist dran!"
                            r "Stimmt, hier dein Zettel!"
                            "Wir spielen noch ein bisschen und gehen dann zum Kuchen essen über."
    
    p "ooof... Fertig"
    rmum "Keine Müdigkeit vortäuschen."
    rmum "Kommt mal alle zusammen für ein Gruppenfoto."
    "Auch noch so was. Na gut."
    rmum "Los alle. Käsekuchen!"
    scene cg selfiefriendo
    "alle" "Käsekuchen!"
    "... Nett."
    
    
    scene bg street with dissolve

    jump scene22
    
label scene21:
    "Na dann. Auf zum Tisch."
    show oparty buh at rightish
    play music octatheme
    o "BOOOH"
    o "Haha."
    show oparty happy
    p "Octavia."
    o "Cooles Kostüm [name]"
    o "Sieht sogar mal gut aus."
    show oparty talk
    p "Danke? Seh ich wohl sonst lahm aus?"
    o "Ja. Aber du scheinst ja doch was zu können."
    p "Du siehst auch gut aus."
    show oparty happy
    o "Ich bin die Medusa aus der Antike."
    p "Die Schlangen Haare sehen mega gruselig aus."
    o "Sag mal."
    p "?"
    o "Willst du mir bei was helfen?"
    p "Was willst du denn genau machen?"
    show oparty talk
    o "Anja erschrecken, so wie dich."
    o "Die ist zwar etwas zäh, aber ich glaub ich kann das schaffen."
    o "Es ist eine Monsterparty. Sie wird es uns nicht übel nehmen."
    p "Mmmh. Na gut und wie willst du sie erschrecken?"
    o "Schau mal. Die Bäume da hinten, ich duck mich dahinter und bin dann versteckt."
    o "Du lockst Anja dort hin und dann..."
    p "Und dann?"
    show oparty buh
    "Die hat echtes Talent für sowas."
    show oparty talk
    o "Ich hoffe Sie erschreckt sich so, das Sie zu Stein erstarrt."
    p "Zu Stein?"
    o "Jeder der die Schlangen der Medusa anschaut wird zu Stein laut Legende, aber ich hab ja nur ein Kostüm."
    o "Bereit?"
    p "In Ordnung."
    "Zu Stein erstarren? Das will ich sehen!"
    "Aber Octavia hat auch recht, Anja ist Zäh."
    hide oparty talk
    scene bg partyocta
    "So, wo ist Anja."
    show aparty n
    p "Hey Anja!"
    show aparty jabber
    a "Hi [name], was bist du denn?"
    p "Ein KILLERwal!"
    p "Und du bist der Sherriff dieser Stadt... Die zerstört wird... oft."
    show aparty talk
    a "Wies aussieht ja."
    p "Aber Cowboys sind doch keine Monster?"
    a "Laut meinem Vater sind Sie riesige Monster gewesen, zumindest gegen die Einheimischen."
    p "Wer sind die Einheimischen?"
    show aparty n
    a "Keine Ahnung."
    a "ABER! Ich kann auch ein MonsterJÄGER sein."
    p "Macht wenig Sinn."
    a "Aber ein Killerwal?"
    "Guter Punkt!"
    p "Willst du vielleicht bei den Bäumen spielen?"
    a "Aber das sind doch gar keine echten Bäume?"
    p "Ja und? Ist doch egal."
    show aparty mad
    a "Wale können nicht klettern."
    "Mmmh, irgeendwie will Sie nicht. Hab ich was falsches gesagt?"
    "Egal. Ich kann Sie überzeugen."
    menu:
        "WALDKILLERwal":
            "Dann bin ich eben der erste WALDKILLERwal und du wirst berühmt für deine Entdeckung!"
            show aparty jabber
            a "So richtig glaub ich dir das nicht."
            a "Aber egal, lass spielen!"
        
        "Im Panama gibt es Dschungel-Wale":
            p "Ich hab mal gehört, im Panama gibt es Wale die im Dschungel sind. Auf so großen Wassern."
            show aparty shock
            a "So etwas kann es geben?"
            a "Wow."
            show aparty talk
            a "Na gut,lass klettern."
        
        "Klettern ist klettern":
            p "Klettern ist klettern. Macht doch trotzdem Spaß."
            show aparty mad
            a "Recht haste ja."
            "..."
            show aparty talk
            a "Na gut, dann wenn du es willst."
            "Irgendwie hats ja doch geklappt."
            
    show aparty n
    a "Die Bäume sind echt klein, aber eventuell wenn wir..."
    scene bg party
    show oparty buh at rightish
    show aparty shock at leftish
    o "HSSSSSS!"
    "{color=#0099ff}[name]:{/color} AAAAH! \n{color=#0099ff}Anja:{/color} AAAH! HIMMEL HERRGOTT SACKERER!"
    "Jetzt hab sogar ich mich selbst erschreckt!"
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
    o "Also bist du doof?"
    a "AAAAH!"
    "Oh man, wieder ein Streit. Aber diesmal gibt es einen Ausweg!"
    p "LEUTE! LEUTE! RUHIG!"
    show oparty talk
    show aparty n
    "...."
    p "Kuchen!"
    o "Wie bitte?"
    a "Ich verstehs auch nicht."
    p "Wir sind hier auf einer Feier, wollen wir nicht erst etwas Kuchen essen?"
    o "Ich mein. Eigentlich schon."
    show aparty talk
    a "Kuchen hört sich gut an."
    p "Dann wär das geklärt, auf zum Kuchen Mampfen."
    hide oparty talk
    hide aparty n
    p "Sag mal, was hast du da vorhin eigentlich gesagt Anja."
    a "Verwendet mein Vater öfters."
    o "Ach sooo! Hab mich das auch schon gefragt."
    p "???"
    o "Mist, versprochen."
    "Wir redeten noch ein bisschen und spielten dann im Dschungel, es wendete sich doch irgendwie zum Guten."
    
    p "ooof... Fertig"
    show rmum nerv
    rmum "Keine Müdigkeit vortäuschen."
    show rmum talk
    rmum "Kommt mal alle zusammen für ein Gruppenfoto."
    "Auch noch so was. Na gut."
    rmum "Los alle. Käsekuchen!"
    scene cg selfieorca
    "alle" "Käsekuchen!"
    "... Nett."


    jump scene22
    
label scene22:
    stop music fadeout 1.0
    play music maintheme    
    "Papa:" "Hi, [name]! Lang nicht mehr gesehen."
    p " PAPA!"
    "Papa:" "Na, wie wars die Feier? Cool, dass du schon neue Freunde gefunden hast."
    p "Ich weiß nicht."
    "Papa:" "hmmmh, naja das wird schon. Im Kindergarten gibt es öfters nak was. Ich kann mich noch daran erinnern wie wir immer..."
    "Super... Jetzt erzählt er wieder von damals, dass kann ja eine tolle Heimfahrt werden."
    play sound cardoor2
    
    
    "End of Day 5 -1"
    "End of Day 5 -2"
    "End of Day 5 -3"
    "End of Day 5 -4"
    "End of Day 5 -5"

    return
