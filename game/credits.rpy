transform credits_scroll(speed):
    ypos 340
    linear speed ypos -2650

## Credits screen.



screen credits():
    style_prefix "credits"

    add "#000"

    frame at credits_scroll(20.0):
        background None
            

        vbox:
            
            

            image "images/Backgrounds/bg titel.png"
            text "\n\n\n{b}Team:{/b}\nBaby's First Visual Novel\n\n" at left
            text "{b}Fabian \"Ceutical\" Pfannmüller{/b}\nProduct Owner, Lead Writer\n\n" at left
            text "{b}Frederik \"Flumpor\" Haas{/b}\nScrum Master, Coding, Minigames, Dialektmensch\n\n" at left
            text "{b}Kilian \"Raghnal\" Petry{/b}\nLead Scenedesigner, Lead Coder, Animator, Playtester\n\n" at left
            text "{b}Natalie \"Illuminati{/b}\" Kuhrt\nLead Artist, Writer, Coder, Scenedesigner, Playtester\n\n" at left
            text "{b}Florian Menzel{/b}\nWriter, Editor\n\n" at left
            text "{b}Sascha \"LeFuxi\" Fuchs{/b}\nWriter, PR\n\n" at left
            text "{b}Luca \"DuckEmoji\" Pfeiffermann{/b}\nLead Sounddesigner\n\n" at left
            text "{b}Musik{/b}\n" at left
            text "Doug Maxwell - Hollywood Traffic Jam\n" at left
            text "Twin Musicom - Video game Soldiers\n" at left
            text "Twin Musicom - Journey in the New World\n" at left
            text "Twin Musicom - 8-Bit March\n" at left
            text "Silent Partner - Hemispheres\n"  at left
            text "The 129ers - We Can Hear You Big Eyes\n" at left 
            text "Endless Love - Natural\n" at left
            text "Bad Snacks - Kawaii!\n" at left
            text "The Green Orbs - Racing The Clock\n" at left
            text "The Green Orbs - Broccoli On My Plate\n" at left
            text "The Green Orbs - After School Jamboree\n" at left
            text "Chris Haugen - Campfire Song\n" at left
            text "Dan Lebowitz - Parkside\n" at left
            text "Quincas Moreira - Rainbow Forest\n" at left
            text "Quincas Moreira - Bubinga\n" at left
            text "Sir Cubworth - Magical Forest\n" at left
            text "Emily A. Sprague - Mind And Eye Journey\n" at left
            text "The Whole Other - Beyond The Lows\n" at left
            text "Alle Musikstücke sind aus der Youtube Audio Library:\nhttps://www.youtube.com/audiolibrary/music?ar=2n\n\n" at left
            text "Licenses under Creative Commons: By Attribution 3.0 Licensen\n\n" at left
            text "Vielen Dank für's Spielen!\n\n\n\n\n\n\n\n\n\n\n\n"
            text "The End.\n\n\n\n\n\n\n\n\n\n\n\n\n"
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

