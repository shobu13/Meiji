label akie_ch4_mauvais:
    pass

"Ran, piétinait le sol sans oser se lancer. Ezo repoussa le contrebandier qui venait sur elle, et sprinta en direction du bateau."
"À mi-chemin, elle reçu sur le haut du crâne un violent coup. Le type qu’elle venait de repousser s’était relevé trop vite et venait de lui asséner un coup sur la tête avec une barre en fer."
"La vision d’Ezo se troubla, pendant qu’elle voyait Akié s’éloigner."
# Fondu en noir
scene bg Black
with dissolve
scene bg grenier
with dissolve

"Quand elle se réveilla, Ezo était dans sa chambre. Elle avait un bandage autour de la tête. Elle passa ses doigts dessus."
show ezo B6 S3 Y2 at left, xflip
with dissolve
ezo "Mais qu’est-ce qui s’est passé ?"
hide ezo
with dissolve
"En repensant à Akié, elle déboula en cuisine après avoir descendu l’escalier quatre à quatre."
show ezo B1 S2 Y1 at left, xflip
with dissolve
ezo "Ou… ou est Akié."
hide ezo
with dissolve
"Clateau et Yoshino attendait dans la cuisine, devant un café. Leurs traits tirés n’annonçait rien de bon."
show clateau B3 S1 Y3 at right
with dissolve
clateau "Ils… ils sont partis avec elle."
show ezo B5 S1 Y2 at left, xflip
with dissolve
ezo "Quoi, comment ?!"
hide clateau
with dissolve
show yoshino B4 S1 Y1 at right
with dissolve
yoshino "Après que tu te sois évanouis, ils sont parti avec pour éviter de se faire remarquer."
show ezo B6 S2 Y2 at left, xflip
with dissolve
ezo "Mais…"
show yoshino B5 S1 Y2 at right
with dissolve
yoshino "Je sais que c’est dur, mais tu ne reverras plus Akié."
"Ezo n’avait ni eu le temps de protester, ni même de pleurer, Yoshino lui avait asséné la vérité."
"Fidèle à elle-même jusqu’au bout, elle se contenta de répondre succinctement."
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "Je vois."
"Elle passa le reste de la semaine sans parler. Les autres aussi étaient encore sous le choc, et personne ne la dérangea."
"Un matin, Ezo n’était plus dans sa chambre. Il n’y avait qu’une lettre, de quelques mots, qui expliquait à Clateau qu’elle retournait dans l’armée. Elle ne revint plus jamais au restaurant."

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
