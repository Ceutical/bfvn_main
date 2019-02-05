



label anjas_ending:
    k "Gut, habt ihr jetzt noch Fragen?"
    L "Äh...was ist eine Lichtung?"
    k "Oh, gute Frage Louis!"
    k "Das ist ein Ort, mitten im Wald. Aber da stehen keine Bäume, da ist nur Wiese oder Waldboden."
    k "Im Wald ist es ja meistens ziemlich dunkel wegen den vielen Bäumen."
    k "Aber bei einer Lichtung ist es heller weil ja dort keine Bäume sind."
    k "Deswegen heißt es nämlich auch Lichtung, das kommt von Licht, verstehst du?"
    L "Äh, ja... Ich glaub' schon..."
    a "Also ich glaub' nicht, hihi." #flüstern
    k "Dann mal los. Schnappt euren Marschpartner und folgt mir."
    k "Ich laufe vor und ihr lauft hinterher, okay?"
    n "Anja ist meine Partnerin, wir laufen jetzt zusammen!"
    p "Der Wald ist voll spannend! Ich kann's kaum erwarten!"
    a "Ja, ich auch! Ich will den ganzen Wald erkunden!"
    #transition zu Waldpfad
    a "Hey, schau! Karin hat angehalten!"
    k "Alle mal aufpassen! Wir machen hier unsere Brotzeitpause!"
    k "Bitte nicht weglaufen, setzt euch her. Hier liegen ein paar große Baumstämme, da könnt ihr euch draufsetzen."
    h "Hört auf Karin. Hier gehbt keiner ohne Erlaubnis weg, ja?"
    
    
    menu:
        a "Hey, wollen wir uns da hinten hinsetzten? Auf den Stamm da?"
        
        "Ja, können wir machen!":
            a "Alles klar!"
            n "Der Platz ist echt schön. Man hört die Vögel zwitschern...!"
            
            menu:
                "Was hast du denn als Brotzeit dabei Anja?":
                    a "Meine Mama hat mir 2 Brote gemacht, eins mit Schinken und eins mit Salami und Käse."
                    a "Ich liebe Schinken, weißt du?"
                    a "Einen Apfel hat sie mir auch eingepackt!"
                    a "Mama sagt immer ich soll mehr Obst essen, aber ich mag Äpfel eigentlich nicht so..."
                    menu:
                        a "Magst du meinen Apfel haben?"
                        
                        "Gerne.":
                            p "Klar! Wenn du ihn nicht willst."
                            a "Okay, hier bitte!"
                            p "Boah... der ist voll lecker, danke!"                            
                            
                        "Lieber nicht...":
                            p "Nein danke. Deine Mama hat aber recht, Obst ist nämlich gesund!"
                            a "Hmm... Ja du hast wohl recht... Vielleicht sollte ich den Apfel doch selber essen..."
                            
                "Glaubst du, hier gibt's Wildschweine?":
                    a "Hier gibt's glaube ich keine... Aber ich will heute unbedingt Rehe sehen!"
                    a "Aber die gibts nur tief im Wald. Vielleicht finden wir ja noch andere Tiere!"
                    a "Hey, weißt du was?"
                    a "Lass uns doch mal gucken gehen."
                    p "Aber die Karin hat doch gesgat wir sollen nicht weg gehen."
                    a "Ja schon..."
                    a "Aber zu zweit finden wir besstimmt wieder zurück bevor die es überhaupt bemerkt..."
                    
            a "Boah, glaubst du hier im Wald ist die Hexenhütte von der Frau Heidenau? Hihi..."
            p "Meinst du wirklich?"
            a "Naja..."
            
        "Nein, lass uns doch zu den anderen setzen.":
            
            a "Na gut, dann gehen wir eben zu den anderen..."
            r "HEY! SCHAUT MAL HER!"
            n "Was hat Randy denn?"
            r "HIER IST VOLL DER COOLE KÄFER!"
            "{color=#0099ff}Anja:{/color} Cool!\n{color=#0099ff}Evelynn:{/color} Der ist aber schön!\n{color=#0099ff}Octavia:{/color} Der kann bestimmt voll schnell fliegen!\n{color=#0099ff}[name]:{/color} Woah!"
            a "Der Käfer ist echt voll schön Randy!"
            e "Wir sollten ihn mitnehmen!"
            e "Dann kann ich ihn zuhause abmalen!"
            L "Der ist doch mega langweilig..."
            e "Boah Louis..."
            r "DU bist langweilig! Such dir halt deinen eigenen Käfer!"
            menu:
                "Mann, Louis ...":
                    p "Mann, Louis... Sei doch nicht so gemein!"
                    L "Ist doch nur ein blöder Käfer, jetzt reg dich do..."
                
                "Toller Käfer!":
                    p "Also ich finde deinen Käfer auch echt cool Randy!"
                    
                    
    k "Okay Kinder! Die Pause ist gleich vorbei! Esst noch alle auf wenn ihr noch nicht fertig seid, dann laufen wir weiter!"
    k "Sind alle fertig? Weiter geht's! So weit ist es nicht mehr bis zu der Lichtung."
    #(Ankommen an der Lichtung)
    p "Das war ja wirklich gar nicht mehr so weit..."
    a "Stimmt. Ist voll schön hier."
    a "Hey Karin, dürfen wir jetzt herumlaufen?"
    k "Moment noch, ich will nur kurz durchzählen ob alle da sind."
    #...
    k "Sieht gut aus."
    k "Also gut, nochmal an alle: Ihr lauft bitte mindestens zu zweit! Und nicht zu weit weg laufen!"
    k "Wir wollen nicht, dass ihr euch verirrt!"
    h "Und wir wollen auch pünktlich wieder von hier weg!"
    k "Hat jeder einen Partner? Oder eine Gruppe?"
    a "Okay komm, wir gehen los!"
    p "Warte, da kommt Randy... Ich glaube er weiß noch nicht mit wem er jetzt läuft."
    
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
            
    a "Alsoa gut, die Erkundung beginnt!"
    #transition zu tief im Wald
    p "Man, ist ja ganz schön dunkel hier. Gruselig."
    a "WOAH!"
    a "Da guck mal die Spinne! Die ist voll groß!"
    if tookrandy == True:
        r "WÄÄÄÄH! SPINNEEE!"
        r "ICh HASSE SPINNEN! ICH HAB ANGST VOR SPINNEN!"
        a "Jetzt schrei doch mal nicht so rum! Das ist nur 'ne Spinne... Die tut uns doch nichts."
        r "DIe IST BESTIMMT GIFTIG!"
        r "ICH WILL NICHT STERBEN!"
        #(Randy rennt weg)
        p "Hey! Bleib bei uns!"
        a "RANDY!"
        a "Hmm... Ich glaub' der kommt nicht wieder..."
        p "Oh Mann."
    else:
        menu:
            n "Eine Spinne ..."
            
            "Igitt!":
                p "Ihgitt! Ich mag Spinnen überhaupt nicht!"
                p "Und die ist ja echt voll riesig"
                a "Ach komm, so schlimm ist das doch nicht."
                a "Also ich find Spinnen toll!"
                a "Ich hatte im Zoo sogar mal eine auf der Hand."
            
            "Cool!":
                p "Wow! Voll cool!"
                p "Ich hab die gar nicht gesehen."
                a "Die ist ja auch voll unsichtbar! Auf dem Boden sieht man sie fast nicht."
                a "Ich find Spinnen auch voll spannend!"
                
    a "Aber wir dürfen unsere Mission nicht vergessen! Ich will noch tiefer in den Wald!"
    p "Bist du sicher? Ich meine wir sind ja schon ganz schön weit gelaufen..."
    a "Klar bin ich sicher! Es gibt so viel zu entdecken hier!"
    p "Hmm... Ich weiß nicht..."
    a "Stell dich nicht so an. Komm, wir müssen weiter!"
    p "Naja okay..."
    #transition zu Bach im Wald
    p "Puh, also langsam sollten wir wirklich umdrehen Anja!"
    a "Jaja, wir laufen bald zurück."
    a "Schau! Da vorne!"
    a "Da ist ja ein Bach! Da ist es auch viel heller, da stehen nicht so viele Bäume!"
    a "Lass uns zum Bach gehen!"
    p "Warte! Bleib hier! Da ist was?"
    a "Was denn?"
    p "Na da am Bach. Das ist doch die Heidenau!"
    a "Du hast Recht! Was macht die denn hier?"
    p "Die sucht irgendwas auf dem Boden. Da! Sie hat was aufgehoben. Das sieht aus wie ne Pflanze."
    a "Voll gruselig... Vielleicht ist sie ja doch eine Hexe!"
    a "Und deswegen sammelt die gerade Pflanzen für einen Hexentrank! Die will uns bestimmt vergiften!"
    p "Meinst du echt?"
    p "Dann müssen wir schnell weg hier und es den anderen sagen!"
    a "Hey warte! Die macht was."
    a "Warum wirft die denn den Sack in den Bach?"
    p "Keine Ahnung. Und warum rennt sie jetzt weg?"
    p "Ich hab sie noch nie rennen gesehen."
    a "Wir müssen ihr folgen! Komm!"
    p "WAS!? Bist du verrückt?"
    p "Was wenn sie uns verhext?"
    a "Aber wir müssen es wissen! Wir müssen doch wissen wo ihre Hexenhütte ist!"
                
