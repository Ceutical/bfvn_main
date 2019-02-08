



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
    k "Oh, gute Frage Louis!"
    show karin go
    k "Das ist ein Ort, mitten im Wald. Aber da stehen keine Bäume, da ist nur Wiese oder Waldboden."
    k "Im Wald ist es ja meistens ziemlich dunkel wegen den vielen Bäumen."
    show karin talk
    k "Aber bei einer Lichtung ist es heller weil ja dort keine Bäume sind."
    k "Deswegen heißt es nämlich auch Lichtung, das kommt von Licht, verstehst du?"
    show louis talk
    L "Äh, ja... Ich glaub' schon..."
    show anja hihi at left with moveinleft
    a "Also ich glaub' nicht, hihi."
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
            a "Alles klar!"
            scene bg woods
            show anja n at center
            with fade
            n "Der Platz ist echt schön. Man hört die Vögel zwitschern...!"
            
            
            menu:
                "Was hast du denn als Brotzeit dabei Anja?":
                    show anja what
                    a "Meine Mama hat mir 2 Brote gemacht, eins mit Schinken und eins mit Salami und Käse."
                    show anja talk
                    a "Ich liebe Schinken, weißt du?"
                    show anja what
                    a "Einen Apfel hat sie mir auch eingepackt!"
                    a "Mama sagt immer ich soll mehr Obst essen, aber ich mag Äpfel eigentlich nicht so..."
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
                    a "Hier gibt's glaube ich keine... Aber ich will heute unbedingt Rehe sehen!"
                    show anja n
                    a "Aber die gibts nur tief im Wald. Vielleicht finden wir ja noch andere Tiere!"
                    show anja happy
                    a "Hey, weißt du was?"
                    show anja hihi
                    a "Lass uns doch mal gucken gehen."
                    p "Aber die Karin hat doch gesagt wir sollen nicht weg gehen."
                    show anja what
                    a "Ja schon..."
                    show anja talk
                    a "Aber zu zweit finden wir bestimmt wieder zurück bevor die es überhaupt bemerkt..."
                    
            show anja hihi
            a "Boah, glaubst du hier im Wald ist die Hexenhütte von der Frau Heidenau? Hihi..."
            p "Meinst du wirklich?"
            a "Naja..."
            k "Okay Kinder! Die Pause ist gleich vorbei! Esst noch alle auf wenn ihr noch nicht fertig seid, dann laufen wir weiter!"
            k "Sind alle fertig? Weiter geht's! So weit ist es nicht mehr bis zu der Lichtung."
            show anja what
            a "Ahh! Schnell, wir müssen hinterher!"
            hide anja with moveoutright
            
        "Nein, lass uns doch zu den anderen setzen.":
            
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
            a "Der Käfer ist echt voll schön Randy!"
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
            a "Du darfst nur mitkommen wenn du dich traust!"
            r "Äh... Okay! Ich komme mit! Ich bin mutig!"
            
        "Nein.":
            p "Naja... Eigentlich wollten nur Anja und ich zusammen laufen... Tut mir leid."
            $ tookrandy = False
            r "Och Schade... Aber na gut, dann lauf' ich wo anders mit..."
            hide randy with moveoutleft
            show anja at center
            
    show anja hihi
    a "Alsoa gut, die Erkundung beginnt!"
    
    if tookrandy == True:
        scene bg woods 
        show anja n at rightish
        show randy bug at leftish
        with fade
        p "Man, ist ja ganz schön dunkel hier. Gruselig."
        show anja what
        a "WOAH!"
        show anja happy
        a "Da guck mal die Spinne! Die ist voll groß!"
        play sound scream3 fadeout 50.0 loop
        hide randy bug
        show randydance
        show anja what
        r "WÄÄÄÄH! SPINNEEE!"
        r "ICH HASSE SPINNEN! ICH HAB ANGST VOR SPINNEN!"
        show anja mad
        a "Jetzt schrei doch mal nicht so rum! Das ist nur 'ne Spinne... Die tut uns doch nichts."
        r "DIE IST BESTIMMT GIFTIG!"
        r "ICH WILL NICHT STERBEN!"
        hide randydance with moveoutleft
        stop sound fadeout 5.0
        p "Hey! Bleib bei uns!"
        show anja vmad at center with move
        a "RANDY!"
        show anja what
        a "Hmm... Ich glaub' der kommt nicht wieder..."
        p "Oh Mann..."
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
    p "Bist du sicher? Ich meine wir sind ja schon ganz schön weit gelaufen..."
    show anja what
    a "Klar bin ich sicher! Es gibt so viel zu entdecken hier!"
    p "Hmm... Ich weiß nicht..."
    show anja mad
    a "Stell dich nicht so an. Komm, wir müssen weiter!"
    p "Naja okay..."
    scene bg river with fade
    show anja what at left with moveinleft    
    p "Puh, also langsam sollten wir wirklich umdrehen Anja!"
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
    p "Was wenn sie uns verhext?"
    show anja vmad
    a "Aber wir müssen es wissen! Wir müssen doch wissen wo ihre Hexenhütte ist!"
    hide anja with moveoutright
    n "Verdammt! Die soll nicht einfach weg rennen."
    scene bg woods with fade
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
    scene bg woods2 with fade
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
    p "Ich glaub du hast Recht!"
    show anja mad
    a "Du auch!"
    p "Wie, ich auch?"
    show anja schmoll
    a "Ja! Du hast doch vorhin gesagt, dass wir das den Anderen erzählen müssen!"
    p "Schau! Die hat ein Buch dabei."
    p "Da stehen bestimmt alle Zutaten für ‘nen Vergiftungstrank drin!"
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
            p "Boah Anja, jetzt komm' hinter den Felsen! Die sieht dich noch!"
            
        "Hinter dem Baumstamm!":
            a "Okay, dann los!"
            hide anja with moveoutbottom
            p "Ja ja ja, ich mach' ja schon!"
            play sound woodcrack2
            p "Mist..."
            a "Was machst du denn!? Pass doch auf wo du hintrittst!"
    
    show heidetalks 1 at leftish with MoveTransition(0.3)
    h "HEY! Wer ist da!?"
    h "Komm! raus!"
    h "Ach ihr Kinder seid das nur!"
    h "Ihr sollt doch nicht so weit weg laufen, könnt ihr denn nie zu hören!?"
    h "Diese nichtsnutzige Karin!"
    h "Kann euch nicht mal ein paar Minuten unter Kontrolle halten."
    
    menu:
        h "Ihr kommt jetzt sofort hier her!"
        
        "Lauf weg!":
            p "Wir müssen hier weg Anja!"
            a "Aber wohin denn?"
            p "Na zurück zur Lichtung!"
            a "Aber da wird die Hexe uns doch finden!"
            p "Ja, aber da sind doch Karin und die Anderen."
            p "Da sind wir in Sicherheit!"
            a "Okay, gute Idee!"
            p "Ja ja, komm schnell!"
            #(Wieder an der Lichtung)
            p "Puh... Wir sind da. Geschafft."
            a "Während wir gerannt sind hab' ich nachgedacht…"
            a "Wir dürfen bis nächste Woche nix erzählen."
            p "Aber warum?"
            a "Vertrau mir einfach. Ich hab ‘nen Plan!"
            a "Am Montag erzählen wir’s den anderen."
            p "Na gut… Aber wir sollten auf jeden Fall Karin was sagen!"
            a "Nein, bloß nicht!"
            a "Was, wenn Karin auch ‘ne Hexe ist?"
            a "Wenn wir mit der reden weiß die ja, dass wir das mit der Heidenau rausgefunden haben."
            a "Und dann verhext die uns damit wir nichts mehr sagen können!"
            p "Hm... Ja, vielleicht hast du ja Recht, aber das..."
            k "Oh, hey, da seid ihr ja, ihr beiden!"
            k "Na? Spaß gehabt?"
            k "Wir müssen bald zurück zum Bus. Geht schon mal zu den anderen. Ich komm gleich nach."
            k "Ich warte noch auf die Frau Heidenau."
            a "Okay, machen wir..."
            #...
            p "Anja, schau! Die Heidenau!"
            a "Man, die schaut mega böse…"
            a "Guck! Die redet mit der Karin."
            a "Bestimmt über uns!"
            a "Mist!"
            a "Karin ist bestimmt auch ‘ne Hexe!"
            k "Kinder! Sind alle wieder da?"
            k "Ich muss mal durchzählen."
            k "Bleibt mal kurz stehen!"
            #...
            h "So, sind wir vollzählig?"
            k "Ja, sieht gut aus."
            h "Also los! Auf zum Bus, ich bin froh wenn ich wieder zuhause bin."
            #...
            
        "Hervorkommen...":
            a "Oh nein! Ich will nicht vergiftet werden!"
            p "Wir können uns gegenseitig beschützen, komm!"
            #...
            h "So so... Ihr beiden..."
            h "Was fällt euch eigentlich ein? Was macht ihr denn so weit weg von der Lichtung?"
            h "Wir haben doch ausdrücklich gesagt, dass ihr in der Nähe bleiben sollt!"
            p "Wir... hm... Wir wollten..."
            a "So weit ist die Lichtung doch gar nicht."
            a "Aber wir haben uns glaube ich verlaufen, oder?"
            p "Hm… Ja genau! Wir haben uns verlaufen!"
            h "Verlaufen habt ihr euch also…"
            h "Wisst ihr was?"
            h "Lügen bringt euch mit mir nichts."
            h "Ihr seid neugierige kleine Käfer."
            h "Wie die Küchenschaben in der Speisekammer…" 
            h "Egal, jetzt seht gefälligst zu, dass ihr wieder zur Lichtung kommt!"
            h "Und ich komme mit!"
            h "Euch zwei kann man ja scheinbar nicht alleine lassen!"
            #(Wieder an der Lichtung)
            h "So, ihr geht jetzt zu den anderen."
            h "Ich muss noch ein Wörtchen mit Karin wechseln."
            h "Wegen euch sind wir nämlich schon hinter dem Zeitplan."
            p "Tut uns leid Frau Heidenau..."
            h "Ja ja, jetzt geht!"
            #...
            a "Du, [name]...."
            a "Während wir zurückgelaufen sind, hab' ich nachgedacht…"
            a "Wir dürfen bis nächste Woche nix erzählen."
            p "Aber warum?"
            a "Vertrau mir einfach. Ich hab ‘nen Plan!"
            a "Am Montag erzählen wir’s den anderen."
            p "Na gut. Aber wir sollten auf jeden Fall Karin was sagen!"
            a "Nein, bloß nicht!"
            a "Was, wenn Karin auch ‘ne Hexe ist?"
            a "Wenn wir mit der reden weiß die ja, dass wir das mit der Heidenau rausgefunden haben."
            a "Und dann verhext die uns damit wir nichts mehr sagen können!"
            p "Hm... Ja, vielleicht hast du Recht…"
            a "Guck! Die Heidenau redet mit der Karin."
            a "Bestimmt über uns!"
            a "Mist!"
            a "Karin ist wirklich auch ‘ne Hexe!"
            k "Kinder! Sind alle wieder da?"
            #...
            h "Sind wir vollzählig?"
            k "Ja, sieht gut aus."
            h "Also los! Auf zum Bus, ich bin froh wenn ich wieder zuhause bin."
            #...
            
    #(Im Bus)
    a "Also pass auf: Ich hab' zuhause ein Buch, da geht's auch um eine Hexe."
    a "Das bring' ich am Montag mit und wir lesen das dann okay?"
    p "Okay, gut! Dann können wir alle anderen Kinder warnen und beschützen!"
    #(Montag nach Wandertag)
    a "Hey, hey! Ich hab' das Buch dabei!"
    a "Und du wirst nicht glauben was man darin sieht!"
    a "Lass uns in die Ecke setzen, dann schauen wir es gemeinsam an!"
    p "Okay."
    p "Mega spannend!"
    #...
    a "So, hier ist das Buch."
    p "Die böse Hexe Rubina?"
    a "Ja! Da sind ganz viele Bilder drin, pass auf!"
    a "Hier. Siehst du?"
    p "Warte mal... Das ist die Hexe Rubina? Die sieht ja fast so aus wie Frau Heidenau!"
    a "Ja, die sehen sich voll ähnlich oder?"
    a "Aber das ist noch nicht alles!"
    p "Wow! Sammelt die da auch Pilze!? Oh mein Gott!"
    a "Und wie ich’s im Wald gesagt habe: Die hat ein Buch dabei für all ihre Tränke!"
    a "Wegen dem Buch hie weiß ich das nämlich auch alles!"
    p "Okay, dann stimmt das alles ja!"
    p "Die Heidenau ist wirklich ‘ne Hexe!"
    r "Hey... Was macht ihr da?"
    p "Oh, hi Randy. Das ist jetzt voll wichtig okay?"
    p "Du musst die anderen Kinder schnell her holen! Kannst du das machen?"
    a "Es geht um ein Geheimnis, sag ihnen das!"
    r "Hm... Okay... Wenn ihr meint… Mach ich."
    #...
    r "So, hab versucht alle zu holen."
    o "Und?"
    o "Was sollen wir jetzt hier? Was macht ihr da überhaupt!?"
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
    r "Aber... Aber..."
    r "Ich will nicht vergiftet werden!"
    e "Ich auch nicht! Was machen wir denn jetzt!?"
    o "Ach kommt schon... Das ist doch voll der Quatsch. Hexen gibt es doch nicht wirklich!"
    r "Aber woher willst du das denn wissen?"
    a "Ob du uns glaubst oder nicht, wir könnens beweisen!"
    p "Wir müssen alle vorsichtig sein! Wir dürfen der Hexe nicht zu nahe kommen!"
    k "Kinder, was macht ihr denn da alle in der Ecke?"
    k "Kommt her, wir machen ein Gruppenspiel!"
    a "Oh nein! Frau Heidenau ist auch da!"
    o "Hm... komisch vielleicht habt ihr ja doch Recht!"
    e "Was flüstert die Karin denn mit der Heidenau?"
    L "Keine Ahnung, aber die schauen zu uns!"
    r "Vorsicht! Die Hexe kommt!"
    h "Sagt mal... Die Karin hat gerade mit mir geredet..."
    h "Und ich glaube ich muss mal ein Wörtchen mit Anja und *Name von P* reden!"
    h "Ihr seid mir seit dem Wandertag nämlich schon aufgefallen ihr beiden!"
    
    #...
    menu:
        h "Kommt mal mit!"
        
        "Folgt der \"Hexe\".":
            r "NEIN! TUT DAS NICHT!"
            e "Oh Gott nein!"
            h "So ihr beiden. Was zur Hölle ist hier los?"
            h "Ihr plant doch irgendwas."
            h "Warum herrscht hier so ein Chaos?"
            a "SIE SIND EINE HEXE!"
            h "Ich bin bitte WAS?"
            p "EINE HEXE!"
            a "Sie wollen uns alle vergiften und haben am Wandertag die Zutaten für den giftigen Trank gesammelt!"
            p "Und in ihrem Buch da ist die Anleitung dafür!"
            a "Ja GENAU! Und HIER in meinem Buch steht das genau so drin!"
            a "WIR HABEN BEWEISE!"
            h "..."
            h "..."
            h "Aaaahahahahahahahaha! Buahaaaahahahaha!"
            h "Hahaaaaaaaaahahaha! Ich kann nicht mehr!"
            h "Hahaaa! Das ist ja köstlich!"
            h "Karin! Komm mal her, das musst du hören! Haaahahahah!"
            p "Huh?!"
            k "Was denn?"
            h "Ich bin eine Hexe! Wusstest du das schon?"
            k "Hehe, eine Hexe?"
            k "Wie kommt ihr 2 denn bitte auf so etwas?"
            h "Ich war am Wandertag doch Pilze sammeln, du weist schon, an dem Bach."
            h "Und die beiden hier haben mich dabei wohl \"erwischt\" und denken ich will alle vergiften."
            k "Ach Gottchen, hihi!"
            h "Also gut, passt auf ihr 2 Quatschköpfe."
            h "Wisst ihr, ich sammle einfach gerne Pilze und Kräuter."
            h "Daheim koche ich daraus dann immer ein leckeres Gericht."
            h "An dem Bach wachsen nämlich ganz viele gesunde Sachen, da gehe ich öfter entlang."
            a "Aber... Aber was ist mit dem Buch?"
            h "Das ist ein Pilzalmanach!"
            h "Ein Buch über Pilze."
            h "Wenn man Pilze sammelt muss man nämlich ganz genau aufpassen, dass man nur die Essbaren mitnimmt."
            h "Manchmal, wenn ich mir bei einem Pilz nicht sicher bin, schau ich in mein Buch."
            p "..."
            a "..."
            a "Das... heißt das stimmt alles garnicht?"
            a "Aber in meinem Buch..."
            k "Ach Anja... Das ist nur ein Märchen. Das ist erfunden!"
            k "Ihr müsst also keine Angst vor uns oder irgendwem sonst hier haben. Es gibt keine Hexen!"
            a "Hm..."
            k "Na kommt!"
            k "Ich glaube wir müssen den anderen Kindern mal was erklären."
            p "Na gut... Nicht dass die anderen Angst haben..."
            #...
            #(2 Wochen später)
            #Transition zu Anja die vom Baum runterwinkt
            jump credits
            
            
        "Flieht vor der \"Hexe\".":
            p "NIEMALS!"
            e "Ja! Rennt weg!"
            h "HEY! Bleibt hier!"
            a "NEEEEIN!"
            h "Passt doch auf! Ihr rennt ja alles um!"
            h "KARIN! KOMM SCHNELL!"
            k "KOMME!"
            k "Was ist denn HIER los!?"
            h "Das reinste Chaos!"
            h "So etwas dulde ich hier nicht!"
            k "KINDER! Beruhigt euch!"
            r "ALLE AUF DIE HEXEEE!"
            k "STOPP RANDY!"
            h "DAS IST JA UNERHÖRT!"
            k "STOP! ALLE HINSETZEN! SOFORT!"
            #...
            k "SO! Und jetzt..."
            h "JETZT ERKLÄRT MIR MAL WAS IN EUCH GEFAHREN IST!"
            "Alle Kinder" "HEXE! HEXE!"
            h "Bitte WAS? ICH!?"
            e "Ja! Anja und [name] haben gesagt, Sie sind eine Hexe!"
            a "Sie wollen uns alle vergiften und haben am Wandertag die Zutaten für den giftigen Trank gesammelt!"
            p "Genau, sie hatten das Buch dabei mit der Anleitung dafür!"
            a "JA! Und HIER in meinem Buch steht das genau so drin!"
            a "WIr HABEN BEWEISE!"
            h "Aaaahahahahahahahaha! Buahaaaahahahaha!"
            h "Hahaaaaaaaaahahaha! Ich kann nicht mehr!"
            h "Hahaaa! Das ist ja köstlich!"
            k "Wie kommt ihr 2 denn bitte auf so etwas?"
            h "Ich war am Wandertag doch Pilze sammeln, du weißt schon, an dem Bach."
            h "Also gut, passt auf ihr 2 Quatschköpfe."
            h "Wisst ihr, ich sammle einfach gerne Pilze und Kräuter."
            h "Daheim koche ich daraus dann immer ein leckeres Gericht."
            h "An dem Bach wachsen nämlich ganz viele gesunde Sachen, da gehe ich öfter entlang."
            a "Aber... Aber was ist mit dem Buch?"
            h "Das ist ein Pilzalmanach!"
            h "Ein Buch über Pilze."
            h "Wenn man Pilze sammelt muss man nämlich ganz genau aufpassen, dass man nur die Essbaren mitnimmt."
            h "Manchmal, wenn ich mir bei einem Pilz nicht sicher bin, schau ich in mein Buch."
            p "..."
            a "..."
            r "Das... heißt das stimmt alles garnicht?"
            a "Aber in meinem Buch..."
            k "Ach Anja... Das ist nur ein Märchen. Das ist erfunden!"
            k "Ihr müsst also keine Angst vor uns oder irgendwem sonst hier haben. Es gibt keine Hexen!"
            k "So und jetzt geht spielen! Wir müssen hier erst mal wieder aufräumen."
            #...
            e "Lügner!"
            r "JA! Ihr seid Lüger!"
            o "Randy das heißt Lügner."
            r "HAB ICH DOCH GESAGT!"
            a "Das wollten wir doch nicht!"
            p "Wir wollten euch warnen! Wir dachten wirklich die Heidenau ist eine Hexe!"
            r "Aber das ist sie nicht! Ihr habt uns angelogen!"
            "Alle Kinder" "LÜGNER"
            #Transition zu Traurige Anja auf dem Baum die in die Ferne blickt
            jump credits
            
            
    
            
            
    
            
    
                
