label yoshino_ch4_mauvais:
    pass


scene bg bar
with dissolve
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Je vais retourner lui parler."
hide ezo
with dissolve
# fondu en noir
scene bg chambre
with dissolve
# TODONE Ezo est en militaire
$ezo_outfit = 'Mi'

"Ezo retourna dans la chambre de Yoshino. Elle était prostrée dans un coin. Les poupées de la chambre, mignonne lors des moments de bonheur, étaient toutes très glauques, quand l’ambiance n’y était pas."
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "Yoshino ! Je… Nous avons besoin de toi, revient !"
"Yoshino fit un mouvement de tête."
show yoshino B4 S2 Y1 at right
with dissolve
yoshino "Qu’est-ce que tu fais ici ? Tu vas finir comme moi."
show ezo B1 S3 Y at left, xflip
with dissolve
ezo "Devenir comme toi, ça ne me fait pas peur ! Alors reviens. Tout le monde t’attend."
show yoshino B5 S1 Y1 at right
with dissolve
yoshino "Mais laisse-moi tranquille ! Personne ne m’attend, je sais que je fais chier tout le monde à être tatillon sur les règles et à envoyer mes couteaux partout."
show ezo B1 S2 Y2 at left, xflip
with dissolve
ezo "Mais non…"
show yoshino B5 S1 Y1 at right
with dissolve
yoshino "Laisse moi tranquille Ezo."
show ezo B5 S2 Y2 at left, xflip
with dissolve
ezo "Mais, moi, je t’aime, je t’assure ! Je veux que tu reviennes !"
show yoshino B4 S2 Y1 at right
with dissolve
yoshino "Mais moi aussi je t’aime. Alors va-t-en, si je m’éloigne de toi, c’est pour ton bien."
show ezo B4 S2 Y2 at left, xflip
with dissolve
ezo "Mais…"
show yoshino B5 S1 Y1 at right
with dissolve
yoshino "Dehors, j’ai dit ! DEHORS !"
"Ezo tourna les talons, en laissant Yoshino dans sa chambre, seule dans la pénombre."

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
