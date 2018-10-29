label clateau_ch4_mauvais:
    pass

scene bg port
with dissolve
show ezo B5 S1 Y2 at left, xflip
with dissolve
ezo "Alors, laisse-moi partir avec toi ! Au moins, je pourrais m’assurer qu’il ne t’arrive rien."
show clateau B4 S2 Y1 at right
with dissolve
clateau "Non Ezo. Je ne te renverrai pas à la guerre. Maintenant retourne auprès des autres, ils doivent s’inquiéter."
"Clateau monta dans le navire. Ezo resta jusqu’à la fin, hurlant à Clateau de rester. Elle s’égosilla jusqu’à ce que le bateau quitte le port. À la fin, elle était en larme."

scene bg Black
stop music fadeout 1.0
show chapter_ch4_mauvais:
    yanchor 0.5 ypos 0.5
    xanchor 0.5 xpos 0.5
with dissolve
with Pause(10)

scene bg Black
with dissolve
jump credits
