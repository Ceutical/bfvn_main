



label anjas_ending:
    python:
        renpy.music.set_volume(volume=0.12, channel='sound4')
        renpy.music.set_volume(volume=0.4, channel='sound3')
    play music anjatheme fadeout 1.0
    play sound4 woods1 fadein 2.0 loop
    play sound3 woods3 fadein 2.0 loop
    scene bg hut
    show karin vhappy at slightright
    with fade
    k "Gut, habt ihr jetzt noch Fragen?"
    show louis really at slightleft with moveinleft
    L "Äh...was ist eine Lichtung?"
    show karin happy
    k "Oh, gute Frage, Louis!"
    show karin go
    k "Das ist ein Ort, mitten im Wald. Aber da stehen keine Bäume, da ist nur Wiese oder Waldboden."
    k "Im Wald ist es ja meistens ziemlich dunkel, wegen den vielen Bäumen."
    show karin talk
    k "Aber bei einer Lichtung ist es heller, weil ja dort keine Bäume sind."
    k "Deswegen heißt es nämlich auch Lichtung, das kommt von Licht, verstehst du?"
    show louis talk
    L "Äh, ja... Ich glaub' schon..."
    show anja hihi at left with moveinleft
    a "Also, ich glaub nicht, hihi."
    hide anja with moveoutleft
    show louis mad
    L "Hey!"
    hide louis with moveoutleft
    k "Und jetzt schnappt euren Marschpartner und folgt mir."
    show karin go
    k "Ich laufe vor und ihr lauft hinterher, okay?"
    hide karin with moveoutright
    n "Anja ist meine Partnerin, wir laufen jetzt zusammen!"
    p "Der Wald ist voll spannend! Ich kann's kaum erwarten!"
    a "Ja, ich auch! Ich will den ganzen Wald erkunden!"
    scene bg woods with fade
    show karin go at left with moveinleft
    show karin at right with MoveTransition(1.0)
    show heide n at left with moveinleft
    show heide at center with MoveTransition(0.8)
    show anja happy at left with moveinleft
    a "Hey, schau! Karin hat angehalten!"
    show karin vhappy
    k "Alle mal aufpassen! Wir machen hier unsere Brotzeitpause!"
    k "Bitte nicht weglaufen, setzt euch her. Hier liegen ein paar große Baumstämme, da könnt ihr euch draufsetzen."
    show heide mad
    h "Hört auf Karin. Hier geht keiner ohne Erlaubnis weg, ja?"
    show heide n
    show anja talk
    a "Hey, wollen wir uns da hinten hinsetzten? Auf den Stamm da?"
    
    
    
    menu:
        a "Hey, wollen wir uns da hinten hinsetzten? Auf den Stamm da?"
        
        "Ja, können wir machen!":
            $ kaeferscene = False
            a "Alles klar!"
            scene bg woods
            show anja n at center
            with fade
            n "Der Platz ist echt schön. Man hört die Vögel zwitschern...!"
            
            
            menu:
                "Was hast du denn als Brotzeit dabei, Anja?":
                    show anja what
                    a "Meine Mama hat mir 2 Brote gemacht, eins mit Schinken und eins mit Salami und Käse."
                    show anja talk
                    a "Ich liebe Schinken, weißt du?"
                    show anja what
                    a "Einen Apfel hat sie mir auch eingepackt!"
                    a "Mama sagt immer, ich soll mehr Obst essen, aber ich mag Äpfel eigentlich nicht so..."
                    a "Magst du meinen Apfel haben?"
                    menu:
                        a "Magst du meinen Apfel haben?"
                        
                        "Gerne.":
                            p "Klar! Wenn du ihn nicht willst."
                            show anja jabber
                            a "Okay, hier bitte!"
                            p "Boah... der ist voll lecker, danke!"                            
                            
                        "Lieber nicht...":
                            p "Nein danke. Deine Mama hat aber recht, Obst ist nämlich gesund!"
                            show anja schmoll
                            a "Hmm... Ja du hast wohl recht... Vielleicht sollte ich den Apfel doch selber essen..."
                            
                "Glaubst du, hier gibt's Wildschweine?":
                    show anja what
                    a "Hier gibt's ,glaube ich, keine... Aber ich will heute unbedingt Rehe sehen!"
                    show anja n
                    a "Aber die gibts nur tief im Wald. Vielleicht finden wir ja noch andere Tiere!"
                    show anja happy
                    a "Hey, weißt du was?"
                    show anja hihi
                    a "Lass uns doch mal gucken gehen."
                    p "Aber die Karin hat doch gesagt, wir sollen nicht weg gehen."
                    show anja what
                    a "Ja schon..."
                    show anja talk
                    a "Aber zu zweit finden wir bestimmt wieder zurück, bevor die es überhaupt bemerkt..."
                    
            show anja hihi
            a "Boah, glaubst du hier im Wald ist die Hexenhütte von der Frau Heidenau? Hihi..."
            p "Meinst du wirklich?"
            a "Naja..."
            k "Okay Kinder! Die Pause ist gleich vorbei! Esst noch alle auf, wenn ihr noch nicht fertig seid, dann laufen wir weiter!"
            k "Sind alle fertig? Weiter geht's! So weit ist es nicht mehr bis zu der Lichtung."
            show anja what
            a "Ahh! Schnell, wir müssen hinterher!"
            hide anja with moveoutright
            
        "Nein, lass uns doch zu den anderen setzen.":
            $ kaeferscene = True
            show anja schmoll
            a "Na gut, dann gehen wir eben zu den anderen..."
            r "HEY! SCHAUT MAL HER!"
            n "Was hat Randy denn?"
            r "HIER IST VOLL DER COOLE KÄFER!"
            scene bg woods
            show louis really at right
            show octa vhappy at leftish
            show eve vhappy2 at rightish
            show randy bug at center
            with fade
            show anja jabber at left behind octa with moveinleft
            "{color=#0099ff}Anja:{/color} Cool!\n{color=#0099ff}Evelynn:{/color} Der ist aber schön!\n{color=#0099ff}Octavia:{/color} Der kann bestimmt voll schnell fliegen!\n{color=#0099ff}[name]:{/color} Woah!"
            show anja talk
            a "Der Käfer ist echt voll schön, Randy!"
            show eve shy2
            e "Wir sollten ihn mitnehmen!"
            show eve talk2
            e "Dann kann ich ihn zuhause abmalen!"
            show louis mad
            L "Der ist doch mega langweilig..."
            show eve mad
            show octa mad
            show anja mad
            e "Boah Louis..."
            show randy bugmad
            r "DU bist langweilig! Such dir halt deinen eigenen Käfer!"
            menu:
                "Mann, Louis ...":
                    p "Mann, Louis... Sei doch nicht so gemein!"
                    show louis really
                    L "Ist doch nur ein blöder Käfer, jetzt reg dich do..."
                    show randy bug
                    show octa talk
                    show eve happy2
                    show anja happy
                    show karin vhappy at slightleft behind louis with moveinleft
                
                "Toller Käfer!":
                    show randy bug
                    show octa talk
                    show eve happy2
                    show anja happy
                    p "Also ich finde deinen Käfer auch echt cool Randy!"
                    show karin vhappy at slightleft behind louis with moveinleft
                    
            k "Okay Kinder! Die Pause ist gleich vorbei! Esst noch alle auf wenn ihr noch nicht fertig seid, dann laufen wir weiter!"
            kg "Okay Karin!"
            show karin go
            k "Sind alle fertig? Weiter geht's! So weit ist es nicht mehr bis zu der Lichtung."
            hide karin with moveoutright
    
    scene bg woods2 with fade
    show karin go at left with moveinleft    
    show karin go at rightish with MoveTransition(1.0)
    show anja happy at leftish with moveinleft
    p "Das war ja wirklich gar nicht mehr so weit..."
    a "Stimmt. Ist voll schön hier."
    show anja what
    a "Hey Karin, dürfen wir jetzt rumlaufen?"
    show karin talk
    k "Moment noch, ich will nur kurz durchzählen ob alle da sind."
    show karin n
    k "Okay, 1, 2, 3..."
    scene bg woods2
    show karin happy at rightish
    show heide n at leftish
    with fade
    k "Sieht gut aus."
    show karin talk
    k "Also gut, nochmal an alle: Ihr lauft bitte mindestens zu zweit! Und nicht zu weit weg laufen!"
    show karin shock
    k "Wir wollen nicht, dass ihr euch verirrt!"
    show heide mad
    h "Und wir wollen auch pünktlich wieder von hier weg!"
    show heide n
    show karin talk
    k "Hat jeder einen Partner? Oder eine Gruppe?"
    scene bg woods2
    show anja jabber at center
    with fade
    a "Okay komm, wir gehen los!"
    p "Warte, da kommt Randy... Ich glaube er weiß noch nicht mit wem er jetzt läuft."
    show anja what at rightish with move
    show randy bug at leftish with moveinleft
    
    menu:
        r "Hey... Ähm... Darf... Darf ich mit euch mitkommen?"
        
        "Ja.":
            p "Na klar Randy, kommt mit!"
            $ tookrandy = True
            a "Hmm... Aber wir wollen tief in den Wald laufen."
            a "Du darfst nur mitkommen, wenn du dich traust!"
            r "Äh... Okay! Ich komme mit! Ich bin mutig!"
           
            if kaeferscene == False:
                a "Was hast du da eigentlich auf der Nase?"
                r "Das ist Rüdigär, der tollste Käfer der Welt! Den nehm ich jetzt überall hin mit!"
                a "...okay..."
            
        "Nein.":
            p "Naja... Eigentlich wollten nur Anja und ich zusammen laufen... Tut mir leid."
            $ tookrandy = False
            r "Och Schade... Aber na gut, dann lauf ich wo anders mit..."
            hide randy with moveoutleft
            show anja at center
            
    show anja hihi
    a "Also gut, schau ma uns a mal um!"
    
    if tookrandy == True:
        scene bg woods 
        show anja n at rightish
        show randy bug at leftish
        with fade
        p "Man, ist ja ganz schön dunkel hier. Gruselig."
        show anja what
        a "WOAH!"
        show anja happy
        a "Da, guck mal, die Spinne! Die ist voll groß!"
        play sound scream3 fadeout 50.0 loop
        hide randy bug
        show randydance
        show anja what
        r "WÄÄÄÄH! SPINNEEE!"
        r "ICH HASSE SPINNEN! ICH HAB ANGST VOR SPINNEN!"
        show anja mad
        a "Jetzt schrei doch mal nicht so rum! Das ist nur ne Spinne... Die tut uns doch nichts."
        r "DIE IST BESTIMMT GIFTIG!"
        r "ICH WILL NICHT STERBEN!"
        hide randydance with moveoutleft
        stop sound fadeout 5.0
        p "Hey! Bleib bei uns!"
        show anja vmad at center with move
        a "RANDY!"
        show anja what
        a "Hmm... Ich glaub, der kommt nicht wieder..."
        p "Oh Man..."
    else:
        scene bg woods
        show anja n at center
        with fade
        p "Man, ist ja ganz schön dunkel hier. Gruselig."
        show anja what
        a "WOAH!"
        show anja happy
        a "Da guck mal die Spinne! Die ist voll groß!"
        menu:
            n "Eine Spinne ..."
            
            "Igitt!":
                p "Ihgitt! Ich mag Spinnen überhaupt nicht!"
                p "Und die ist ja echt voll riesig"
                show anja what
                a "Ach komm, so schlimm ist das doch nicht."
                show anja talk
                a "Also ich find Spinnen toll!"
                show anja happy
                a "Ich hatte im Zoo sogar mal eine auf der Hand."
            
            "Cool!":
                p "Wow! Voll cool!"
                p "Ich hab die gar nicht gesehen."
                show anja talk
                a "Die ist ja auch voll unsichtbar! Auf dem Boden sieht man sie fast nicht."
                show anja jabber
                a "Spinnen sind voll spannend!"
                show anja happy
                a "Ich hatte im Zoo sogar mal eine auf der Hand."
    
    show anja jabber
    a "Aber wir dürfen unsere Mission nicht vergessen! Ich will noch tiefer in den Wald!"
    p "Bist du sicher? Ich meine, wir sind ja schon ganz schön weit gelaufen..."
    show anja what
    a "Klar, bin ich sicher! Es gibt so viel zu entdecken hier!"
    p "Hmm... Ich weiß nicht..."
    show anja mad
    a "Stell dich nicht so an. Komm, wir müssen weiter!"
    p "Naja okay..."
    scene bg river with fade
    show anja what at left with moveinleft    
    p "Puh, also langsam sollten wir wirklich umdrehen, Anja!"
    show anja schmoll
    a "Jaja, wir laufen bald zurück."
    show anja happy
    a "Schau! Da vorne!"
    show anja talk
    a "Da ist ja ein Bach! Da ist es auch viel heller, da stehen nicht so viele Bäume!"
    a "Lass uns zum Bach gehen!"
    play music spooky3 fadeout 1.0
    p "Warte! Bleib hier! Da ist was?"
    show anja what
    a "Was denn?"
    p "Na da am Bach. Das ist doch die Heidenau!"
    show heidetalks 2 at right with dissolve
    show anja mad
    a "Du hast Recht! Was macht die denn hier?"
    p "Die sucht irgendwas auf dem Boden. Da! Sie hat was aufgehoben. Das sieht aus wie ne Pflanze."
    show anja what
    a "Voll gruselig... Vielleicht ist sie ja doch eine Hexe!"
    show anja vmad
    a "Und deswegen sammelt die gerade Pflanzen für einen Hexentrank! Die will uns bestimmt vergiften!"
    p "Meinst du echt?"
    p "Dann müssen wir schnell weg hier und es den anderen sagen!"
    show anja what
    a "Hey warte! Die macht was."
    a "Warum wirft die denn so nen Sack in den Bach?"
    show bag at rightish behind anja
    show bag at bagaway with MoveTransition(3.0)
    p "Keine Ahnung. Und warum rennt sie jetzt weg?"
    hide heidetalks 2 with moveoutright
    p "Ich hab sie noch nie rennen gesehen."
    show anja mad at center with move
    a "Wir müssen ihr folgen! Komm!"
    p "WAS!? Bist du verrückt?"
    p "Was, wenn sie uns verhext?"
    show anja vmad
    a "Zefix. Wir müssen es wissen! Wir müssen doch wissen wo ihre Hexenhütte ist!"
    hide anja with moveoutright
    n "Verdammt! Die soll nicht einfach weg rennen."
    scene bg woods2 with fade
    show heidetalks 2 at left with moveinleft
    show heidetalks at right with MoveTransition(1.5)
    hide heidetalks with moveoutright
    show anja what at left with moveinleft
    p "Hey! Psst! Anja! Wart’ auf mich!"
    show anja mad at center with move
    a "Komm schnell, wir dürfen die Hexe nicht aus den Augen verlieren!"
    show anja hihi
    a "Wir können uns hinter den Bäumen in der Nähe verstecken, dann sieht sie uns nicht."
    hide anja with moveoutright
    scene bg woods with fade
    show heidetalks 2 at left with moveinleft
    show heidetalks at rightish with move
    show anja mad at left with moveinleft
     p "Da!"
    p "Sie hat gestoppt."
    show anja what
    a "Ja, aber warum?"
    p "Die sammelt Pilze. Guck!"
    show anja schmoll
    a "Oh nein! Die sind bestimmt giftig!"
    show anja vmad
    a "Ich habs dir doch gesagt, die will uns vergiften!"
    p "Ich glaub, du hast Recht!"
    show anja mad
    a "Du auch!"
    p "Wie, ich auch?"
    show anja schmoll
    a "Ja! Du hast doch vorhin gesagt, dass wir das den anderen erzählen müssen!"
    p "Schau! Die hat ein Buch dabei."
    p "Da stehen bestimmt alle Zutaten für nen Vergiftungstrank drin!"
    show anja vmad
    a "Ja! So ein Buch haben doch alle Hexen! Da stehen alle möglichen Tränke drin."
    a "Schnell! Die Heidenau geht weiter!"
    show heidetalks at right with move
    p "Ne warte!"
    p "Die ist schon wieder stehen geblieben."
    p "Lass mal lieber verstecken. Sonst findet die uns noch…"
    menu:
        p "Lass mal lieber verstecken. Sonst findet die uns noch…"
        
        "Hinter dem Felsen!":
            p "Der Felsen hier ist doch ein super Versteck!"
            a "Okay!"
            hide anja with moveoutbottom
            a "Woah, warte! Da ist ‘ne Spinne am Felsen! Cool!"
            a "Der ganze Wald ist voller Spinnen!"
            p "Boah Anja, jetzt komm hinter den Felsen! Die sieht dich noch!"
            
        "Hinter dem Baumstamm!":
            a "Okay, dann los!"
            hide anja with moveoutbottom
            p "Ja ja ja, ich mach ja schon!"
            play sound woodcrack2
            p "Mist..."
            a "Was machst du denn!? Pass doch auf, wo du hintrittst!"
    
    show heidetalks 1 at leftish with MoveTransition(0.3)
    h "HEY! Wer ist da!?"
    h "Komm raus!"
    h "Ach, ihr Kinder seid das nur!"
    h "Ihr sollt doch nicht so weit weg laufen, könnt ihr denn nie zu hören!?"
    h "Diese nichtsnutzige Karin!"
    h "Kann euch nicht mal ein paar Minuten unter Kontrolle halten."
    
    menu:
        h "Ihr kommt jetzt sofort hier her!"
        
        "Lauf weg!":
            p "Wir müssen hier weg Anja!"
            h "Hey bleibt gefälligst stehen!"
            hide heidetalks with moveoutleft
            a "Aber wohin denn?"
            p "Na zurück zur Lichtung!"
            a "Aber da wird die Hexe uns doch finden!"
            p "Ja, aber da sind doch Karin und die anderen."
            p "Da sind wir in Sicherheit!"
            a "Okay, gute Idee!"
            p "Ja ja, komm schnell!"
            scene bg black with fade
            scene bg woods2
            show anja schmoll at center
            with fade
            p "Puh... Wir sind da. Geschafft."
            a "Während wir gerannt sind, hab ich nachgedacht…"
            a "Wir dürfen bis nächste Woche nix erzählen."
            p "Aber warum?"
            a "Vertrau mir einfach. Ich hab nen Plan!"
            show anja vmad
            a "Am Montag erzählen wir’s den anderen."
            p "Na gut… Aber wir sollten auf jeden Fall Karin was sagen!"
            show anja mad
            a "Blouß nird!"
            a "Was, wenn Karin auch ne Hexe ist?"
            a "Wenn wir mit der reden, weiß die ja, dass wir das mit der Heidenau rausgefunden haben."
            a "Und dann verhext die uns, damit wir nichts mehr sagen können!"
            p "Hm... Ja, vielleicht hast du ja Recht, aber das..."
            show karin vhappy at right with moveinright
            k "Oh, hey, da seid ihr ja, ihr beiden!"
            k "Na? Spaß gehabt?"
            k "Wir müssen bald zurück zum Bus. Geht schon mal zu den anderen. Ich komm gleich nach."
            show karin happy
            k "Ich warte noch auf die Frau Heidenau."
            show anja what
            a "Okay, machen wir ..."
            scene bg woods2
            show karin n at leftish
            show heide n at rightish
            with fade
            p "Anja, schau! Die Heidenau!"
            a "Greiterhex…"
            show heide mad
            a "Guck! Die redet mit der Karin."
            a "Bestimmt über uns!"
            a "Dreck!"
            show karin shock
            a "Karin ist bestimmt auch ‘ne Hexe!"
            hide heide with moveoutright
            show karin mad at center with move
            k "Kinder! Sind alle wieder da?"
            k "Ich muss mal durchzählen."
            show karin n
            k "Bleibt mal kurz stehen!"
            k "1... 2... 3..."
            show heide mad at right with moveinright
            h "So, sind wir vollzählig?"
            show heide n
            k "Ja, sieht gut aus."
            show heide mad
            h "Also los! Auf zum Bus, ich bin froh, wenn ich wieder zu Hause bin."
            
        "Hervorkommen...":
            a "Oh nein! Ich will nicht vergiftet werden!"
            p "Wir können uns gegenseitig beschützen, komm!"
            show heidetalks at center with move
            show anja what at left with moveinbottom
            h "So so... Ihr beiden..."
            h "Was fällt euch eigentlich ein? Was macht ihr denn so weit weg von der Lichtung?"
            h "Wir haben doch ausdrücklich gesagt, dass ihr in der Nähe bleiben sollt!"
            show heidetalks 2
            p "Wir... hm... Wir wollten..."
            show anja schmoll
            a "So weit ist die Lichtung doch gar nicht."
            show anja what
            a "Aber wir haben uns ,glaube ich, verlaufen, oder?"
            p "Hm… Ja genau! Wir haben uns verlaufen!"
            show heidetalks 1
            h "Verlaufen habt ihr euch also…"
            h "Wisst ihr was?"
            h "Lügen bringt euch mit mir nichts."
            h "Ihr seid neugierige kleine Käfer."
            h "Wie die Küchenschaben in der Speisekammer…" 
            h "Egal, jetzt seht gefälligst zu, dass ihr wieder zur Lichtung kommt!"
            h "Und ich komme mit!"
            h "Euch zwei kann man ja scheinbar nicht alleine lassen!"
            scene bg woods2
            show heidetalks 1 at rightish
            show anja what at leftish
            with fade
            h "So, ihr geht jetzt zu den anderen."
            h "Ich muss noch ein Wörtchen mit Karin wechseln."
            h "Wegen euch sind wir nämlich schon hinter dem Zeitplan."
            p "Tut uns leid, Frau Heidenau..."
            h "Ja ja, jetzt geht!"
            scene bg woods2
            show anja schmoll at center
            with fade
            a "Du, [name]...."
            a "Während wir gerannt sind, hab ich nachgedacht…"
            a "Wir dürfen bis nächste Woche nix erzählen."
            p "Aber warum?"
            a "Vertrau mir einfach. Ich hab nen Plan!"
            show anja vmad
            a "Am Montag erzählen wir’s den anderen."
            p "Na gut… Aber wir sollten auf jeden Fall Karin was sagen!"
            show anja mad
            a "Nein, bloß nicht!"
            a "Was, wenn Karin auch ne Hexe ist?"
            a "Wenn wir mit der reden, weiß die ja, dass wir das mit der Heidenau rausgefunden haben."
            a "Und dann verhext die uns, damit wir nichts mehr sagen können!"
            p "Hm... Ja, vielleicht hast du Recht…"
            scene bg woods2
            show karin n at leftish
            show heide n at rightish
            with fade
            p "Anja, schau! Die Heidenau!"
            a "Man, die schaut mega böse…"
            show heide mad
            a "Guck! Die redet mit der Karin."
            a "Bestimmt über uns!"
            a "Mist!"
            show karin shock
            a "Karin ist bestimmt auch ne Hexe!"
            hide heide with moveoutright
            show karin mad at center with move
            k "Kinder! Sind alle wieder da?"
            k "Ich muss mal durchzählen."
            show karin n
            k "Bleibt mal kurz stehen!"
            k "1... 2... 3..."
            show heide mad at right with moveinright
            h "So, sind wir vollzählig?"
            show heide n
            k "Ja, sieht gut aus."
            show heide mad
            h "Also los! Auf zum Bus, ich bin froh, wenn ich wieder zu Hause bin."
    
    stop sound3
    stop sound4
    play music anjatheme fadeout 1.0        
    scene bg black with fade
    scene bg bus
    show anja schmoll at rightish
    with fade
    a "Also pass auf: Ich hab zu Hause ein Buch, da geht's auch um eine Hexe."
    a "Das bring ich am Montag mit und wir lesen das dann, okay?"
    p "Okay, gut! Dann können wir alle anderen Kinder warnen und beschützen!"
    scene bg black with fade
    show mnd with dissolve
    $ renpy.pause(0.6, hard = True)
    scene bg grura2
    show anja n at center
    with fade
    aa "Hey, hey! Ich hab das Buch dabei!"
    a "Und du wirst nicht glauben, was man darin sieht!"
    a "Lass uns in die Ecke setzen, dann schauen wir es gemeinsam an!"
    p "Okay."
    p "Mega spannend!"
    scene bg cuddle
    show anja what at left
    show witchbook
    with fade
    a "So, hier ist das Buch."
    p "Die böse Hexe Rubina?"
    show anja mad
    a "Ja! Da sind ganz viele Bilder drin, pass auf!"
    show heide woods at center with dissolve
    a "Hier. Siehst du?"
    p "Warte mal... Das ist die Hexe Rubina? Die sieht ja fast so aus wie Frau Heidenau!"
    hide heide with dissolve
    show anja schmoll
    a "Ja, die sehen sich voll ähnlich oder?"
    a "Aber das ist noch nicht alles!"
    p "Wow! Sammelt die da auch Pilze!? Oh mein Gott!"
    show anja vmad
    a "Und wer ich’s damals verzüllt hab: Die hat ein Buch dabei für all ihre Tränke!"
    a "Wegen dem Buch hier, weiß ich das nämlich auch alles!"
    p "Okay, dann stimmt das alles ja!"
    p "Die Heidenau ist wirklich ne Hexe!"
    show randy happy at right with moveinbottom
    r "Hey... Was macht ihr da?"
    p "Oh, Hi Randy. Das ist jetzt voll wichtig, okay?"
    p "Du musst die anderen Kinder schnell her holen! Kannst du das machen?"
    show anja mad
    a "Es geht um ein Geheimnis, sag ihnen das!"
    show randy shock
    r "Hm... Okay... Wenn ihr meint… Mach ich."
    scene bg grura2
    show louis really at right
    show octa happy at leftish
    show eve happy2 at rightish
    show randy talk at center
    with fade
    r "So, hab versucht alle zu holen."
    o "Und?"
    o "Was sollen wir jetzt hier? Was macht ihr da überhaupt!?"
    show anja schmoll at left behind octa with moveinleft
    a "Ihr müsst jetzt gut aufpassen! Wir haben ein schlimmes Geheimnis herausgefunden!"
    p "Ja! Wir sind ja am Wandertag zusammen herumgelaufen."
    p "Und mitten im Wald haben wir die Heidenau gesehen."
    a "Die hat so Kräuter und so gesammelt."
    a "Ach… und Pilze!"
    p "Und wisst ihr für was?"
    p "Frau Heidenau ist eine Hexe! Sie hat Zutaten für einen Trank gesammelt!"
    a "Und die will uns alle vergiften!"
    a "Die hat sogar ein Buch mit den ganzen Anleitungen für ihre Tränke!"
    r "Äh…seid... seid ihr sicher?"
    e "Ja, wahrscheinlich will die nur eine Suppe aus den Pilzen machen."
    a "Auf keinen Fall! Hier in dem Buch steht das alles!"
    p "Und da sammelt die Hexe auch Pilze und so und hat ein Buch dabei für ihren Gifttrank!"
    a "Und die Hexe in dem Buch sieht genauso aus wie die Heidenau!"
    show louis mad
    show octa shock
    show eve mad
    show randy vmad
    r "Aber... Aber..."
    r "Ich will nicht vergiftet werden!"
    e "Ich auch nicht! Was machen wir denn jetzt!?"
    o "Ach kommt schon... Das ist doch voll der Quatsch. Hexen gibt es doch nicht wirklich!"
    r "Aber woher willst du das denn wissen?"
    show anja mad
    a "Ob du uns glaubst oder nicht, wir könnens beweisen!"
    show louis really
    show octa mad
    show randy mad
    p "Wir müssen alle vorsichtig sein! Wir dürfen der Hexe nicht zu nahe kommen!"
    show karin shock at slightleft behind louis with moveinright
    k "Kinder, was macht ihr denn da alle in der Ecke?"
    show karin talk
    k "Kommt her, wir machen ein Gruppenspiel!"
    show anja vmad
    show heide n at slightright behind louis with moveinright
    a "Oh nein! Frau Heidenau ist auch da!"
    show octa shock
    show randy shock
    r "Vorsicht! Die Hexe kommt!"
    show heide talk
    h "Sagt mal... Die Karin hat gerade mit mir geredet..."
    h "Und ich glaube, ich muss mal ein Wörtchen mit Anja und [name] reden!"
    h "Ihr seid mir auf dem Wandertag nämlich schon aufgefallen, ihr beiden!"
    h "Kommt doch mal mit!"
    
    menu:
        h "Kommt doch mal mit!"
        
        "Folgt der \"Hexe\".":
            show randy vmad
            r "NEIN! TUT DAS NICHT!"
            e "Oh Gott nein!"
            scene bg office
            show heide talk at center
            with fade
            h "So ihr zwei Beiden."
            show heide mad
            h "Was zur Hölle ist hier los?"
            show heide talk
            h "Ihr plant doch irgendwas."
            h "Warum herrscht hier so ein Chaos?"
            show anja vmad at left with moveinleft
            a "SIE SAN A HEX!"
            show heide mad
            h "Ich bin bitte WAS?"
            p "EINE HEXE!"
            show anja schmoll
            a "Sie wollen uns alle vergiften und haben am Wandertag die Zutaten für den giftigen Trank gesammelt!"
            p "Und in ihrem Buch da ist die Anleitung dafür!"
            show witchbook dissolve
            show anja mad
            a "Ja GENAU! Und HIER in meinem Buch steht das genau so drin!"
            show anja vmad
            a "WIR HABEN BEWEISE!"
            hide witchbook with dissolve
            show heide n
            h "..."
            show anja what
            h "..."
            show heide laugh
            h "Aaaahahahahahahahaha! Buahaaaahahahaha!"
            h "Hahaaaaaaaaahahaha! Ich kann nicht mehr!"
            h "Hahaaa! Das ist ja köstlich!"
            show heide talk
            h "Karin! Komm mal her, das musst du hören!"
            show heide laugh
            h "Haaahahahah!"
            p "Huh?!"
            show karin shock at right with moveinright
            k "Was denn?"
            show heide talk
            h "Ich bin eine Hexe! Wusstest du das schon?"
            show heide laugh
            show karin happy
            k "Hehe, eine Hexe?"
            show karin talk
            k "Wie kommt ihr 2 denn bitte auf so etwas?"
            show heide talk
            h "Ich war am Wandertag doch Pilze sammeln, du weißt schon, an dem Bach."
            show heide laugh
            h "Und die zwei hier, haben mich dabei wohl \"erwischt\" und denken ich will alle vergiften."
            show karin vhappy
            k "Ach Gottchen, hihi!"
            show heide mad
            show karin happy
            h "Also gut, passt auf, ihr 2 Quatschköpfe."
            show heide talk
            h "Wisst ihr, ich sammle einfach gerne Pilze und Kräuter."
            h "Daheim koche ich daraus dann immer ein leckeres Gericht."
            h "An dem Bach wachsen nämlich ganz viele gesunde Sachen, da gehe ich öfter entlang."
            show heide n
            a "Aber... Aber was ist mit ihrem Buch?"
            show heide talk
            h "Das ist ein Pilzalmanach!"
            h "Ein Buch über Pilze."
            h "Wenn man Pilze sammelt, muss man nämlich ganz genau aufpassen, dass man nur die essbaren mitnimmt."
            h "Manchmal, wenn ich mir bei einem Pilz nicht sicher bin, schau ich in mein Buch."
            show heide n
            p "..."
            a "..."
            show anja schmoll
            a "Das... heißt, das stimmt alles garnicht?"
            show anja mad
            a "Aber in meinem Buch..."
            show karin talk
            k "Ach, Anja... Das ist nur ein Märchen. Das ist erfunden!"
            k "Ihr müsst also keine Angst vor uns oder irgendwem sonst hier haben. Es gibt keine Hexen!"
            show anja schmoll
            a "Hm..."
            show karin happy
            k "Na kommt!"
            k "Ich glaube wir müssen den anderen Kindern mal was erklären."
            p "Na gut... Nicht, dass die anderen Angst haben..."
            scene anja goodend with fade
            play music GoodEnd fadein 1.0
            n "Ich bin echt froh, dass wir nicht so großen Ärger bekommen haben."
            n "Auch die anderen Kinder waren uns gar nicht so sehr sauer, obwohl das ja gar nicht wahr war, was wir ihnen erzählt haben."
            n "Obwohl..."
            n "Vielleicht gibt es ja doch irgendwo Hexen."
            n "Nicht unbedingt in unserem Kindergarten. Aber irgendwo bestimmt."
            n "Aber Anja und ich werden es schon mit ihnen aufnehmen. Sie ist meine allerbeste Freundin und zusammen schaffen wir alles!"
            window hide
            $ renpy.pause ()
            window auto
            jump credits
            
            
        "Flieht vor der \"Hexe\".":
            p "NIEMALS!"
            show heide mad
            show karin shock
            e "Ja! Rennt weg!"
            h "HEY! Bleibt hier!"
            hide louis
            hide octa
            hide eve
            hide randy
            hide anja
            play sound scream3 loop
            show louischaos
            show octachaos
            show evechaos
            show randychaos
            show anjachaos
            show heide behind louischaos
            show karin behind louischaos
            a "NEEEEIN!"
            h "Passt doch auf! Ihr rennt ja alles um!"
            h "KARIN!"
            k "JA WAS DENN?!"
            h "Das reinste Chaos!"
            h "So etwas dulde ich hier nicht!"
            k "KINDER! Beruhigt euch!"
            r "ALLE AUF DIE HEXEEE!"
            k "STOPP RANDY!"
            h "DAS IST JA UNERHÖRT!"
            h "STOP! ALLE HINSETZEN! SOFORT!"
            stop sound fadeout 2.0
            scene bg grura
            show anja vmad at slightright
            show karin mad at left
            show heide mad at leftish
            with fade
            k "SO! Und jetzt..."
            h "JETZT ERKLÄRT MIR MAL, WAS IN EUCH GEFAHREN IST!"
            "Alle Kinder" "HEXE! HEXE!"
            h "Bitte WAS? ICH!?"
            show eve mad at right with moveinright
            show heide n
            e "Ja! Anja und [name] haben gesagt, Sie sind eine Hexe!"
            hide eve with moveoutright
            show anja mad
            a "Sie wollen uns alle vergiften und haben am Wandertag die Zutaten für den giftigen Trank gesammelt!"
            p "Genau, sie hatten das Buch dabei mit der Anleitung dafür!"
            a "JA! Und HIER in meinem Buch steht das genau so drin!"
            show anja vmad
            a "WIr HABEN BEWEISE!"
            show heide laugh
            h "Aaaahahahahahahahaha! Buahaaaahahahaha!"
            h "Hahaaaaaaaaahahaha! Ich kann nicht mehr!"
            h "Hahaaa! Das ist ja köstlich!"
            show karin talk
            k "Wie kommt ihr 2 denn bitte auf so etwas?"
            show heide talk
            h "Ich war am Wandertag doch Pilze sammeln, du weißt schon, an dem Bach."
            show heide mad
            h "Also gut, passt auf, ihr 2 Quatschköpfe."
            show heide talk
            h "Wisst ihr, ich sammle einfach gerne Pilze und Kräuter."
            h "Daheim koche ich daraus dann immer ein leckeres Gericht."
            h "An dem Bach wachsen nämlich ganz viele gesunde Sachen, da gehe ich öfter entlang."
            show anja what
            show heide n
            a "Aber... Aber was ist mit dem Buch?"
            show heide talk
            h "Das ist ein Pilzalmanach!"
            h "Ein Buch über Pilze."
            h "Wenn man Pilze sammelt, muss man nämlich ganz genau aufpassen, dass man nur die essbaren mitnimmt."
            h "Manchmal, wenn ich mir bei einem Pilz nicht sicher bin, schau ich in mein Buch."
            show heide n
            p "..."
            show anja schmoll
            a "..."
            show randy shock at right with moveinright
            r "Das... heißt, das stimmt alles garnicht?"
            a "Aber in meinem Buch..."
            show karin happy
            k "Ach, Anja... Das ist nur ein Märchen. Das ist erfunden!"
            show karin talk
            k "Ihr müsst also keine Angst vor uns oder irgendwem sonst hier haben. Es gibt keine Hexen!"
            k "So und jetzt geht spielen! Wir müssen hier erst mal wieder aufräumen."
            scene bg cuddle
            show octa vmad at right
            show eve mad at rightish
            show randy mad at center
            show anja schmoll at left
            with fade
            e "Lügner!"
            r "JA! Ihr seid Lüger!"
            show octa smug
            o "Randy das heißt Lügner."
            show randy vmad
            show octa mad
            r "HAB ICH DOCH GESAGT!"
            show randy mad
            a "Das wollten wir doch nicht!"
            p "Wir wollten euch warnen! Wir dachten wirklich, die Heidenau ist eine Hexe!"
            show randy vmad
            r "Aber das ist sie nicht! Ihr habt uns angelogen!"
            "Alle Kinder" "LÜGNER"
            scene anja badend with fade
            play music BadEnd fadein 1.0
            n "Die anderen sind echt sauer auf uns. Dabei war das alles doch gar keine Absicht!"
            n "Ich hab mich auch entschuldigt, aber sie wollen trotzdem nicht mehr mit mir oder Anja spielen."
            n "Und jetzt ist Anja deswegen auch noch auf mich sauer."
            n "Sie ist ja auch noch nicht so lange hier und das ärgert sie jetzt natürlich, dass niemand mehr mit ihr was machen will."
            n "Dabei wollte ich das doch gar nicht... aber nicht immer zugelabert zu werden, ist vielleicht auch ganz okay."
            n "Außerdem komm ich ja dann auch bald in die Schule. Da finde ich dann vielleicht Freunde."
            window hide
            $ renpy.pause ()
            window auto
            jump credits
            
            
    
            
            
    
            
    
                
