label credits:
    pass
$ credits_speed = 25 #scrolling speed in seconds
scene bg main_gui #replace this with a fancy background
with dissolve
show theend:
    yanchor 0.5 ypos 0.5
    xanchor 0.5 xpos 0.15
with dissolve
$renpy.pause(3, hard='True')
hide theend
with dissolve
show cred at Move((0.15, 5.0), (0.15, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
$renpy.pause(credits_speed, hard='True')
# show saucisse at Move((0.5, 2), (0.5, 0.0), 5, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
# $renpy.pause(5, hard='True')

show thanks:
    yanchor 0.5 ypos 100
    xanchor 0.5 xpos 0.5
with dissolve
$renpy.pause(5, hard='True')
hide thanks
with Dissolve(2)
$ MainMenu(confirm=False)()

init python:
    credits = ('Sprites et CG', 'Karamelow'), ('Scénario', 'Catablor'), ('Fonds', 'Ichi-gsm'), ('Programmation', 'Shobu13'), ('GUI', 'Karamelow'), ('Musique', 'Monteskieu'), ('Website', 'Wardmar', 'Shobu13'), ('GUI du site', 'Karamelow')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += '\n{size=16}Merci à BricedeFrance, \nNegi, Gmaquina, Antpersonn, \nSosso et tout les membres de la \ncommunauté de nous avoir aidé dans ce projet !'

init:
    image cred = Text(credits_s, font="gui/Sofia-Regular.otf", text_align=0.5, color="#ff9900") #use this if you want to use special fonts
    # image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}Fin !",
     font="gui/Sofia-Regular.otf", text_align=0.5, color="#ff9900")
    image thanks = Text("{size=80}Merci d'avoir jouer",font="gui/Sofia-Regular.otf", text_align=0.5, color="#ff9900")
