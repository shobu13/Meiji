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
show thanks:
    yanchor 0.5 ypos 0.5
    xanchor 0.5 xpos 0.5
with dissolve
$renpy.pause(3, hard='True')
hide thanks
$ MainMenu(confirm=False)()

init python:
    credits = ('Backgrounds', 'Airgoof'), ('Backgrounds', 'Dorktwerp'), ('Sprites and CG', 'Ballclown'), ('GUI', 'Cuddlywad'), ('Writing', 'Dorktwerp'), ('Writing', 'Fingerpookie'), ('Programming', 'Dorktwerp'), ('Music', 'Grumblemuck'), ('Music', 'Headwookum')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n6.15.7.374" #Don't forget to set this to your Ren'py version

init:
    image cred = Text(credits_s, font="gui/Sofia-Regular.otf", text_align=0.5, color="#ff9900") #use this if you want to use special fonts
    # image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}Fin !",
     font="gui/Sofia-Regular.otf", text_align=0.5, color="#ff9900")
    image thanks = Text("{size=80}Merci d'avoir jouer",font="gui/Sofia-Regular.otf", text_align=0.5, color="#ff9900")
