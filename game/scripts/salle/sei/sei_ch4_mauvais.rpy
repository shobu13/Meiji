label sei_ch4_mauvais:
    pass

scene bg salle
with dissolve
"Sei fit un non de la tête."
show sei B4 S2 Y2 at right
with dissolve
sei "Je vois que tu essayes de trouver une solution, mais ça ne marchera pas. On ne peut pas s’opposer à l’état, tu dois te faire une raison."
show ezo B2 S2 Y1 at left, xflip
with dissolve
ezo "Mais Sei, on pourrait…"
show sei B5 S1 Y1 at right
with dissolve
sei "Je suis désolée Ezo… Mais c’est comme ça."
"Le ton cassant de Sei dissuada Ezo de continuer plus loin."
show ezo B4 S2 Y2 at left, xflip
with dissolve
ezo "Bon. D’accord. J’y vais. A… adieu."
show sei B4 S1 Y1 at right
with dissolve
sei "Adieu, Ezo."
hide sei
hide ezo
with dissolve
"Le dernier sourire de Sei était emprunt de tristesse. Ezo sortie lentement de la pièce, elle avait l’impression que chaque pas qu’elle faisait rajoutait un poids sur elle."
"Ezo reprit son travail au restaurant. Elle n’avait plus que quelques contacts distants avec Sei. Son travail ne lui laissait pas énormément de temps."
"Le caractère d’Ezo se dégrada beaucoup. Elle devint plus sèche, moins aimable. Plus stricte aussi. Les nuits d’Ezo furent troublées pendant encore des années par ce soir où elle avait perdu Sei."

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
