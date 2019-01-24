
define m = Character("Mama", color="#DC143C")
define p = Character("Protagonist", color="#4169E1")


label start:

    # Bilder aus der directory greifen!
    # show character.png



    # play music "tuer1"

    "Pfomp!"
    "So wuerde ich den Ton beschreiben den unser blauer BW Tennis ausstößt, wenn seine Türen mit einer Leichtigkeit ins Schloss fallen."
    "Klar, neu ist dieser Ton mir nicht."
    "Ehrlich gesagt ist er sogar alt und vertraut."
    "Schließlich chauffiert mich der vom Parkremplern gezeichnete und innen fleckig ausgekleidete Wagen schon seit dem ich denken kann überall hin."
    "Aber dennoch weckt dieser Ton, so häufig ich ihn schon unbewusst vernommen habe, dieses mal etwas neues in mir."
    "Ein Gefühl, dass ich nicht so richtig beschreiben kann..."
    
    scene bg_kitaraum
    with Dissolve(.5)
    show mama froh
    
    
    m "Haaaaaaallooooo..." 
    m "Jemand da?"
    
    p "Mmmmmmhh... was?"
    
    show mama at right
    show boi john at left
    
    m "Bist du wieder aus deiner Gedankenwelt aufgewacht?"
    # play music strase1
    
    m "Super, dann kann sich der feine Herr ja endlich auf den Weg machen."
    m "Wir sind eh schon zu spät und ich muss noch mit der Erzieherin reden."
    
    "Ich blieb still, alles was ich sage kann und wird gegen mich verwendet werden."
    # play music kita1
    
    "Irgendwie geht mir hier eh alles zu schnell. Erst die Sache mit Papa, die neue Wohnung und ich werde nochmal in einen Kindergarten gesteckt"
    "und das obwohl ich in zwei Monaten schon in die Schule soll."
    "Warum können die Dinge nicht so sein wie sie davor waren, ich vermisse eh schon die ganze Zeit meine alten Freunde."
    "Maxi, Roland, Ralf und sogar Linda, eine Erzieherin die uns jeden morgen mit High Fives begrüßte..."
    "Warum muss ich hier überhaupt hin, wenn ich eh niemanden kenne..."
    "Nun ja, wenn ich schonmal hier bin mach ich wohl das beste draus."
    
    #show Titlecard
    
    #stop 
    

    return
