label tsugumi_ch4_mauvais:
    pass

scene bg port
with dissolve
show ezo B4 S1 Y2 at left, xflip
with dissolve
ezo "Laisse tomber tout ça ! Je ne peux pas me passer de toi, peu importe les autres. Pour le reste, Clateau s’en occupera."
show tsugumi B2 S2 Y2 at right
with dissolve
tsugumi "Je vois bien que tu m’apprécie Ezo, mais je ne peux pas laisser les autres comme ça. Si tu ne peux pas comprendre ça, alors c’est que visiblement on n’est pas faites pour être ensemble."
"Tsugumi tourna le dos à Ezo et remonta la barrière avant que celle-ci puisse protester. Ezo resta un moment au pied de la barrière à l’appeler, espérant qu’elle revienne sur sa décision."
scene bg Black
with dissolve

scene bg rue
with dissolve
"Le soir venu, elle rentra au restaurant. Elle marchait d’un pas lourd, et elle entendait, venant du port, les tirs des soldats et les cris des ouvriers."

scene bg Black
with Dissolve(3)
stop music fadeout 1.0
show chapter_ch4_mauvais:
    yanchor 0.5 ypos 0.5
    xanchor 0.5 xpos 0.5
with dissolve
$renpy.pause(10, hard='True')

scene bg Black
with dissolve
jump credits
