transform credits_scroll(speed):
    ypos 340
    linear speed ypos -5070

## Credits screen.



screen credits():
    style_prefix "credits"

    add "#000"

    frame at credits_scroll(30.0):
        background None
            

        vbox:
            
            

            image "images/Backgrounds/bg titel.png"
            text "\n\n\n{b}Team:{/b}\nBaby's First Visual Novel\n\n" at left
            text "{b}Fabian \"Ceutical\" Pfannmüller{/b}\nProduct Owner, Lead Writer\n\n" at left
            text "{b}Frederik \"Flumpor\" Haas{/b}\nScrum Master, Coding, Minigames, Dialektmensch\n\n" at left
            text "{b}Kilian \"Raghnal\" Petry{/b}\nLead Scenedesigner, Lead Coder, Animator, Playtester\n\n" at left
            text "{b}Natalie \"Illuminati{/b}\" Kuhrt\nLead Artist, Writer, Coder, Scenedesigner, Playtester, Lizenzberatung\n\n" at left
            text "{b}Florian Menzel{/b}\nWriter, Editor\n\n" at left
            text "{b}Sascha \"LeFuxi\" Fuchs{/b}\nWriter, PR\n\n" at left
            text "{b}Luca \"DuckEmoji\" Pfeiffermann{/b}\nLead Sounddesigner\n\n" at left
            text "{b}Musik{/b}\n" at left
            text "Doug Maxwell - {b}Hollywood Traffic Jam{/b}\n" at left
            text "Twin Musicom - {b}Video game Soldiers{/b}\n" at left
            text "Twin Musicom - {b}Journey in the New World{/b}\n" at left
            text "Twin Musicom - {b}8-Bit March{/b}\n" at left
            text "Silent Partner - {b}Hemispheres{/b}\n"  at left
            text "The 129ers - {b}We Can Hear You Big Eyes{/b}\n" at left 
            text "Endless Love - {b}Natural{/b}\n" at left
            text "Bad Snacks - {b}Kawaii!{/b}\n" at left
            text "The Green Orbs - {b}Racing The Clock{/b}\n" at left
            text "The Green Orbs - {b}Broccoli On My Plate{/b}\n" at left
            text "The Green Orbs - {b}After School Jamboree{/b}\n" at left
            text "Chris Haugen - {b}Campfire Song{/b}\n" at left
            text "Dan Lebowitz - {b}Parkside{/b}\n" at left
            text "Quincas Moreira - {b}Rainbow Forest{/b}\n" at left
            text "Quincas Moreira - {b}Bubinga{/b}\n" at left
            text "Sir Cubworth - {b}Magical Forest{/b}\n" at left
            text "Emily A. Sprague - {b}Mind And Eye Journey{/b}\n" at left
            text "The Whole Other - {b}Beyond The Lows{/b}\n" at left
            text "{b}Alle Musikstücke sind aus der Youtube Audio Library:{/b}\nhttps://www.youtube.com/audiolibrary/music?ar=2n\n\n\n" at left
            text "{b}SFX{/b}\n" at left
            text "{b}Kindergeräusche:{/b}\n{b}Ambience, Children Playing, Distant, A.wav{/b}\nInspectorJ (www.jshaw.co.uk)\nFreesound.org\nhttps://freesound.org/people/InspectorJ/sounds/398160/\n" at left
            text "{b}Katzenschnurren:{/b}\nhttps://www.youtube.com/audiolibrary_download?vid=2cbaacc1e00b220e\n" at left
            text "{b}Hahnwecker:{/b}\n{b}Rooster Calling, Close, A.wav{/b}\nInspectorJ (www.jshaw.co.uk)\nof Freesound.org\nhttps://freesound.org/people/InspectorJ/sounds/439472/\n" at left
            text "{b}Regen:{/b}\nhttps://www.youtube.com/audiolibrary_download?vid=46ff000248dac484\n" at left
            text "{b}Fahrrad:{/b}\nhttps://www.youtube.com/audiolibrary_download?vid=8d296f5f763b76b4\n" at left
            text "{b}Fahrrad mit alter Kette:{/b}\nhttps://www.youtube.com/audiolibrary_download?vid=59a705aed0890b62\n" at left
            text "{b}Whoosh:{/b}\nhttps://www.youtube.com/audiolibrary_download?vid=29d6a8554d0758c9\nhttps://www.youtube.com/audiolibrary_download?vid=c90f630b33d69a38\n" at left
            text "{b}Straßenkulisse:{/b}\n{b}Ambience, London Street, A.wav{/b}\nInspectorJ (www.jshaw.co.uk)\nFreesound.org\nhttps://freesound.org/people/InspectorJ/sounds/398159/\n" at left
            text "{b}Magie:{/b}\nhttps://www.youtube.com/audiolibrary_download?vid=e9eebea0804634e0\n\n{b}another magic wand spell tinkle.flac{/b}\nTimbre\nhttps://freesound.org/people/Timbre/sounds/221683/\n\n{b}SFX Magic{/b}\nrenatalmar\nhttps://freesound.org/people/renatalmar/sounds/264981/\n\n{b}Magic Strike.wav{/b}\nAleks41 https://freesound.org/people/Aleks41/sounds/406063/\n" at left
            text "{b}Kinderschrei:{/b}\n{b}Child screaming in rage or horror (2), short.{/b}\nSoundBits Sound FX\nhttps://www.soundsnap.com/screams_shouts_human_child_020_wav\n\n{b}A child screaming - Ahhh!{/b}\nSFX Bible\nhttps://www.soundsnap.com/node/51558\n\n{b}Child screams{/b}\nSFX Source\nhttps://www.soundsnap.com/node/107654\n" at left
            text "{b}Wald Atmo:{/b}\n{b}Khao Yai National Park, nightime forest atmosphere under deep canopy, very still with insects{/b}\nBBC Sound Effects\nhttp://bbcsfx.acropolis.org.uk/assets/07070189.wav\n\n{b}Bamboo and reed forest wind through undergrowth with birds. San Martin de los Andes, Argentina.{/b}\nBBC Sound Effects\Nhttp://bbcsfx.acropolis.org.uk/assets/07063061.wav\n" at left
            text "{b}Ast zerbricht:{/b}\nhttps://www.youtube.com/audiolibrary_download?vid=32084e5d652ed77c\n" at left
            text "{b}Goblingeräusche:{/b}\n{b}FUN MONSTER Jaja silly talk gibberish 10.wav{/b}\nArticulated Sounds (Sonniss.com)\nhttps://gamesounds.xyz/?dir=Sonniss.com%20-%20GDC%202018%20-%20Game%20Audio%20Bundle/Articulated%20Sounds%20-%20Fun%20Monsters\n\n{b}FUN MONSTER Wooly cartoony laugh talk gibberish.wav{/b}\nArticulated Sounds (Sonniss.com)\nhttps://gamesounds.xyz/?dir=Sonniss.com%20-%20GDC%202018%20-%20Game%20Audio%20Bundle/Articulated%20Sounds%20-%20Fun%20Monsters\n" at left
            text "{b}Fledermausgeräusch:{/b}\nBat.wav\nMike Koenig\nhttp://soundbible.com/1132-Bat.html\n" at left
            text "{b}Licenses under Creative Commons:{/b} By Attribution 3.0 Licensen\n\n\n\n" at left
            text "{b}Vielen Dank für's Spielen!{/b}\n\n\n\n\n\n\n\n\n\n\n\n"
            text "{b}The End.{/b}\n\n\n\n\n\n\n\n\n\n\n\n\n"
            text "{i}Linksklick oder Rechtsklick und Main Menu / Quit zum Beenden der Credits.{/i}"
            
            
            
                



style credits_hbox:
    spacing 40
    ysize 30

style credits_label:
    xalign 0.5

style credits_text:
    xalign 0.5
    

## Show credits screen.

label credits:
    window hide
    scene bg black
    show screen credits
    $ renpy.pause()
    hide screen credits
    jump endgame

