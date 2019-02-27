transform credits_scroll(speed):
    ypos 720
    linear speed ypos -720

## Credits screen.


screen credits():
    style_prefix "credits"

    add "#000"

    frame at credits_scroll(5.0):
        background None
        xalign 0.5
            

        vbox:
            label "Credits"

            image "images/Backgrounds/bg titel.png"
            text "Krams"
            
            
                
hide screen credits
jump credits


style credits_hbox:
    spacing 40
    ysize 30

style credits_label:
    xalign 0.5

style credits_text:
    xalign 0.5
    

## Show credits screen.

label credits:
    call screen credits

