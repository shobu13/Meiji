label bar_ch1:
    pass

show chapter_bar_ch1:
    yanchor 0.5 ypos 0.5
    xanchor 0.5 xpos 0.5
with dissolve
$renpy.pause(3, hard='True')

scene bg grenier
with dissolve
"Au petit matin, les rayons du soleil commençaient tout juste à filtrer par la lucarne du grenier. Ezo grognait, gênée par la lumière, et se réveilla."
show ezo Y1 B6 S3 eH
with dissolve
ezo "Gnnn… Il est encore tôt. Mais c’est l’heure de bosser !"
hide ezo
with dissolve
"Elle se réveilla et descendit au premier étage, dans l’appartement de Clateau. Il était déjà descendu et avait juste laissé le petit-déjeuner sur la table. Ezo s’empressa d’avaler un croissant et de descendre aussi."
scene bg cuisine
with dissolve
show clateau B1 S1 Y4 at right
with dissolve
clateau "Bonjour, Ezo !"
hide clateau
with dissolve
show yoshino B1 S1 Y1 at right
with dissolve
yoshino "Salut."
hide yoshino
with dissolve
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Bonjour à vous deux. Où sont les autres ?"
show clateau B1 S1 Y4 at right
with dissolve
clateau "Akié et Sei sont déjà en salle. Ran t’attends au bar, je l’ai prévenue que tu allais la rejoindre."
show ezo B2 S3 Y2 at left, xflip
with dissolve
ezo "D’accord, je vais aller la rejoindre"
hide clateau
with dissolve
show yoshino B2 S1 Y1 at right
with dissolve
yoshino "Ah! Comme tu travailles ici, tu dois porter l’uniforme du restaurant. Tiens."
show ezo B1 S3 Y3 at left, xflip
with dissolve
ezo "Ça m’enchante pas mais je suppose que je n’ai pas le choix…"
show yoshino B2 S1 Y4 at right
hide ezo
with dissolve
yoshino "Contente que tu l’ai compris. Mais attends deux secondes."
"La porte claqua dans un bruit fracassant."
hide clateau
with dissolve
clateau "Hm ? Yoshino, tu as refermé la porte de la réserve."
show yoshino B3 S1 Y2 at right
with dissolve
yoshino "Voilà, tu peux te changer."
hide clateau
with dissolve
clateau "Je n’aurai pas essayé de mater tu sais, je suis pas un collégien."
show yoshino B5 S1 Y2 at right
with dissolve
yoshino "On est jamais trop prudente."
hide clateau
with dissolve
clateau "D’accord, d’accord."
hide clateau
with dissolve
clateau "…"
hide clateau
with dissolve
clateau "Yoshino ? Tu vas rouvrir la porte hein."
# TODONE fondu en noir
scene bg Black
with dissolve
# TODONE Ezo porte son uniforme de serveuse
$ ezo_outfit = "Se"
scene bg bar
with dissolve
"Ezo avait passé l’uniforme de serveuse du restaurant et s’était rendue au bar. En arrivant, elle trouva Ran, devant son bar, un chiffon à la main, en train de nettoyer le plan de travail."
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Ran, désolée de l’attente, me voilà. Ran ?"
show ran B7 S1 Y6 at right
with dissolve
ran "ZZZzzz"
show ezo B8 -S3 Y5 at left, xflip
with dissolve
ezo "OH !"
show ran B1 S1 Y4 at right
with dissolve
ran "Ah,veuillez m’en excuser, il me semble que je suis assoupie pendant mon office."
show ezo B4 S2 Y6 at left, xflip
with dissolve
ezo "Tu dors en travaillant ? j’aurais tout vu…"
show ran B1 S1 Y2 at right
with dissolve
ran "Alors comme ça, vous avez choisis le bar n’est-ce pas ? Vous aurais-je tapé dans l’oeil ?"
menu:
    "Je préfère travailler en charmante compagnie, oui.":
        $relation_ran += 1
        show ezo B1 S3 Y4 at left, xflip
        with dissolve
        ezo "Je préfère travailler en charmante compagnie, oui."
        show ran B1 S1 Y1 at right
        with dissolve
        ran "Oh, vous m'embarrassez ! Voilà que ma taquinerie se retourne contre moi"
    "Je préfère surtout être en contact avec les ouvriers.":
        $relation_tsugumi += 1
        show ezo B1 S3 Y4 at left, xflip
        with dissolve
        ezo "Je préfère surtout être en contact avec les ouvriers."
        show ran B1 S3 Y3 at right
        with dissolve
        ran "Le contact du petit peuple à quelque chose d’intéressant, je dois l’admettre."
show ezo B2 S3 Y2 at left, xflip
with dissolve
ezo "En tout cas, je m’en remet à toi."
show ran B1 S1 Y4 at right
with dissolve
ran "Moi de même, mademoiselle Ezo. J’espère que nous nous entendrons bien."
hide ezo
with dissolve
hide ran
with dissolve
"Le matin, la salle du bar était presque vide. Le quartier était populaire et les ouvriers étaient déjà parti dans les manufactures. Les clients plus aisés prenaient place en salle, laissant donc le bar dans le calme. Quelques petits vieux venaient tout de même prendre un verre d’alcool avant de commencer leur journée."
show ran B1 S1 Y2 at right
with dissolve
ran "Le travail ici est plutôt simple. Il suffit de prendre les commandes des clients, puis de les transmettre à mademoiselle Yoshino. Il ne reste plus qu’à les servir."
show ezo B2 S3 Y4 at left, xflip
with dissolve
ezo "Pas très dur en effet."
hide ezo
with dissolve
hide ran
with dissolve
"La matinée se passa sans trop de mal. Les rares clients ne commandaient pas grand-chose. C’était une bonne chose pour Ezo, qui put prendre ses marques petit à petit dans son nouvel environnement."
"Ran se trouvait assez attentionnée à son encontre, et lui expliquait en détail tout ce qu’il fallait savoir sur le fonctionnement du bar."
"Alors que midi approchait, Ezo regarda les étagères derrière Ran. Elles montaient presque jusqu’au plafond et était remplies de bouteilles. Ce mur de verre donnait presque le vertige, et on espérait que les planches furent bien fixée quand on se trouvait juste en dessous."
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Impressionnante collection."
show ran B1 S1 Y2 at right
with dissolve
ran "On ne peut plus, en effet ! Vous avez l’oeil."
ran "Habituellement, Ran est plutôt passive, et n’exprime pas beaucoup ses émotions. Mais là, elle avait bombé un peu le torse et on sentait dans sa voix une certaine fiertée."
show ran B1 S1 Y2 at right
with dissolve
ran "Grâce au patron, nous avons eu accès à tout un étalage d’alcools étrangers. Nous disposons de grands crus venus de toute l’europe et d’une gamme de spiritueux de haut niveau. Ah, tenez, voici de la chartreuse, vous devez connaître, n’est-ce pas ?"
show ezo B2 S3 Y2 at left, xflip
with dissolve
ezo "Oui, j’en ai déjà bu."
hide ezo
with dissolve
hide ran
with dissolve
"Entra alors dans le bar Tsugumi. Elle marcha rapidement jusqu’au comptoir, et sauta agilement sur un des fauteuils."
show tsugumi B1 S1 Y2 at left, xflip
with dissolve
tsugumi "Salut Ran ! La même chose que d’habitude."
show ran B1 S1 Y4 at right
with dissolve
ran "Mademoiselle Tsugumi ! Vous êtes bien en avance, aujourd’hui."
show tsugumi B1 S1 Y1 at left, xflip
with dissolve
tsugumi "Oui, héhéhé, j’ai réussi à avoir ma pause du midi en avance, pour une fois."
show ran B1 S1 Y4 at right
with dissolve
ran "Tenez, voici votre bière. Votre collation arrive bientôt."
show tsugumi B1 S1 Y1 at left, xflip
with dissolve
tsugumi "Oooh, je l’attendais celle-là ! Rien de tel qu’une bonne bière, hein !"
show ran B4 S1 Y1 at right
with dissolve
ran "Moui… Je vous avouerai que je préfère le raffinement des spiritueux. Regardez cette bouteille d’absinthe : cette belle couleur émeraude n’est-elle pas magnifique ?"
show tsugumi B2 S1 Y3 at left, xflip
with dissolve
tsugumi "La couleur ? N’importe quoi ! Seul le goût compte."
show ran B5 S1 Y1 at right
with dissolve
ran "Mais le goût est très important aussi, et il en fait un apéritif très appréciable."
show tsugumi B3 S1 Y2 at left, xflip
with dissolve
tsugumi "Il en reste que, je préfère la bière."
show ran B1 S1 Y1 at right
with dissolve
ran "Eh bien, vous avez tort de vous limiter, mademoiselle Tsugumi ! Voilà quelque chose que je réprouve chez les prolétaires, c’est leur manque de goût !"
show tsugumi B4 S3 Y1 at left, xflip
with dissolve
tsugumi "Les gens de la haute société ne sont pas en reste, avec leurs petites manies idiotes."
hide tsugumi
with dissolve
show ezo B4 S3 Y1 at left, xflip
with dissolve
ezo "Euhm…"
# TODONE: [Tsugumi&Ran] “Et toi Ezo, tu préfères quoi ?”]
# TODONE: comment on fait là ? Si tu peux faire quelque chose, genre les superposer ou les mettre cote à cote
show tsugumi B4 S3 Y1 at right
show ran B4 S3 Y1 behind tsugumi at right, multiple_right
$tsugumi_nom = "Tsugumi & ran"
tsugumi "Et toi Ezo, tu préfères quoi ?"
$tsugumi_nom = "Tsugumi"
hide tsugumi
hide ran
with dissolve
menu:
    "Je préfère l'absinthe":
        $relation_ran += 1
        show ezo B1 S1 Y2 at left, xflip
        with dissolve
        ezo "Je préfère l'absinthe"
        show ran B1 S1 Y4 at right
        with dissolve
        ran "Oh, je suis bien contente de voir que vous partagez mes goûts, mademoiselle Ezo."
        hide ran
        with dissolve
        show tsugumi B7 S3 Y1 at right
        with dissolve
        tsugumi "Eh bien je boirai ma bière toute seule alors !"
    " J’aime bien la bière":
        $relation_tsugumi += 1
        show ezo B1 S1 Y2 at left, xflip
        with dissolve
        ezo "J’aime bien la bière"
        show tsugumi B1 S1 Y2 at center
        with dissolve
        tsugumi "Je vois qu’on se comprend !"
        show ran B4 S3 Y3 at right
        with dissolve
        ran "Hum, mademoiselle Ezo, vous me décevez."
        "Après la discussion, Ran resta immobile devant son robinet à bière, mais cette fois-ci elle ne somnolait pas, elle arborait juste une tête grognon."

hide tsugumi
with dissolve
show yoshino B5 S1 Y1 at right
with dissolve
yoshino "La commande est prête !"
hide yoshino
with dissolve
"Ezo se leva et alla porter sa commande à Tsugumi."
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "Voilà ton sandwich."
show tsugumi B1 S1 Y1 at right
with dissolve
tsugumi "Oh, merci bien !"
show ezo B1 S3 Y4 at left, xflip
with dissolve
ezo "Alors comme ça t’es ouvrière ? T’es pas un peu jeune ?"
show tsugumi B1 S3 Y1 at right
with dissolve
tsugumi "Et toi alors ? Tu m’as pas l’air bien vieille non plus !"
show ezo B2 S3 Y4 at left, xflip
with dissolve
ezo "C’est pas faux ! Disons que je suis là par la force des choses. Et toi ?"
show tsugumi B1 S1 Y1 at right
with dissolve
tsugumi "Moi, c’est pour manger, tout simplement. Si je travaille pas, je mange pas, c’est aussi simple que ça. Mais ça m’a pas l’air d’être ton cas. T’étais en uniforme militaire hier, t’étais dans l’armée ou quelque chose comme ça ? C’est rare pour une étrangère."
show ezo B2 S1 Y1 at left, xflip
with dissolve
ezo "Dans l’armée, oui… enfin quelque chose comme ça."
"La réponse évasive d’Ezo laissa Tsugumi dubitative, mais elle n’y prêta pas vraiment attention. Elles parlèrent ensuite de choses et d’autres pendant plusieurs minutes."
scene bg Black
with Dissolve(1)
scene bg salle
with dissolve

show tsugumi B1 S1 Y2 R2 at right
with dissolve
tsugumi "Donc, je disais, rien ne vaut un barbecue…"
hide tsugumi
with dissolve
hide ezo
with dissolve
show yoshino B8 Y5 at left, xflip
with dissolve
yoshino "Ezo ! Ran ! Qu’est-ce que vous foutez !? Je ne reçois plus de commandes depuis un moment ! Au travail !"
show ran B4 S3 Y6 at right
with dissolve
ran "Oui…"
hide ran
with dissolve
show tsugumi B2 S1 Y6 at right
with dissolve
tsugumi "Oups, désolée de vous avoir distraite pendant votre travail."
hide yoshino
with dissolve
menu:
    "C’était sympa de parler ensemble, faudra qu’on remette ça ! Je te laisse, faut que je reprenne le taff.":
        $relation_tsugumi += 1
        show ezo B1 S3 Y4 at left, xflip
        with dissolve
        ezo "C’était sympa de parler ensemble, faudra qu’on remette ça ! Je te laisse, faut que je reprenne le taff."
    "Argh, je dois y aller sous peine de me faire tailler en pièce par Yoshino ! Bye !":
        $relation_tsugumi -= 1
        show ezo B6 S3 Y8 at left, xflip
        with dissolve
        ezo "Argh, je dois y aller sous peine de me faire tailler en pièce par Yoshino ! Bye !"
show tsugumi B1 S1 Y1 at right
with dissolve
tsugumi "Je comprends, et moi aussi il va falloir que je me remette au turbin ! Je repasserai ce soir."
hide tsugumi
with dissolve
"Tsugumi avala son dernier morceau de sandwich et quitta le bar. Ezo nettoyait le comptoir tandis que Ran s’occupait de donner les dernières commandes aux clients."
show ran B5 S1 Y2 at right
with dissolve
ran "je pense que le plus dur est passé."
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "C’était pas très compliqué, et on serait allé plus vite si tu t’endormais pas toute les cinq minutes."
show ran B3 S1 Y2 at right
with dissolve
ran "Héhéhé…"
hide ran
with dissolve
hide ezo
with dissolve
"Dans l’après-midi, le bar redevenait beaucoup plus calme. Ezo et Ran en profitèrent pour remettre un peu d’ordre dans la pièce. Puis, n’ayant rien à faire, Ezo, assise derrière le comptoir, posa sa tête dans ses bras, en attendant les clients."
show ran B1 S1 Y2 at right
with dissolve
ran "Dites voir, je voulais vous demander, mais l’uniforme que vous portiez hier, c’était bien un genre d’uniforme de l’armée shogunale, n’est-ce pas ?"
show ezo B1 S2 Y2 at left, xflip
with dissolve
ezo "Hein ? Mouais, en effet. Comment tu sais ça ? Ce n’est pourtant pas commun."
show ran B1 S1 Y4 at right
with dissolve
ran "En fait, j’ai déjà eu l’occasion de voir des uniformes occidentaux, ma famille était proche du Shogoun."
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Ah bon ? Comment vous avez fait pour qu’il ne vous arrive rien ?"
show ran B4 S1 Y3 at right
with dissolve
ran "Eh bien… mon père a choisi de se ranger assez vite du côté de l’empereur."
menu:
    " Il a eu raison. C’était peine perdue de toute manière.":
        $relation_ran += 1
        show ezo B1 S1 Y2 at left, xflip
        with dissolve
        ezo "Il a eu raison. C’était peine perdue de toute manière."
        show ran B4 S3 Y3 at right
        with dissolve
        ran "C’est triste, mais c’était en effet la meilleure décision possible."
    "Ah ? C’est à cause de gens comme lui qu’on a perdu la guerre.":
        $relation_ran -= 1
        show ezo B1 S1 Y2 at left, xflip
        with dissolve
        ezo "Ah ? C’est à cause de gens comme lui qu’on a perdu la guerre."
        show ran B4 S3 Y3 at right
        with dissolve
        ran "Je suis désolée pour vous, mais la guerre aurait été perdue de toute manière, nous n’avions pas le choix."
show ran B1 S1 Y2 at right
with dissolve
ran "Mais vous semblez plutôt jeune pour avoir participé à la guerre. Pourquoi vous être enrôlée ? Venir de l’étranger juste pour la guerre, voilà un étrange voyage…"
show ezo B4 S2 Y4 at left, xflip
with dissolve
ezo "J’ai pas eu le choix…"
"Ezo avait murmuré sa réponse à demi-mot, et elle avait tourné la tête pour ne pas croiser le regard de Ran."
hide ezo
with dissolve
hide ran
with dissolve
"Vers dix-huit heures, les premiers clients revinrent enfin. Le calme s’estompa peu à peu, et le bar était à nouveau plein."

"C’est à ce moment qu’Ezo découvrit qu’il était en fait plutôt populaire, vu la masse de personne s’y pressant. En plus de proposer des prix abordables pour les ouvriers et les travailleurs, les spécialités étrangères attiraient aussi beaucoup de clients plus aisés, et aux heures de pointes la salle devenait rapidement bondée."
"Le coup de feu de de midi n’était qu’un avant-goût avant celui du soir. Que ce soit derrière le comptoir ou entre les tables, Ezo se démenait pour récupérer les commandes, les porter à Yoshino, et ensuite les redistribuer aux clients sans se tromper."
show yoshino B5 S1 Y2 at right
with dissolve
yoshino "Voilà les deux cafés, pour la 18 !"
show ezo B2 S3 Y4 at left, xflip
with dissolve
ezo "Bien compris !"
show yoshino B1 S1 Y2 at right
with dissolve
yoshino "Et appelle Ran, j’ai les sandwichs pour la 14 !"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "D’accord ! Ran ! Ran…?"
hide yoshino
with dissolve
"Ezo se retourna pour voir Ran à l’autre bout du bar, en train de somnoler."
show ezo B5 Y5 at left, xflip
with dissolve
ezo "RAN !"
show ran B6 S1 Y7 at right
with dissolve
ran "AH !"
hide ezo
with dissolve
"Le réveil en sursaut de Ran provoqua le rire dans toute la salle. Visiblement, les somnolences de Ran étaient connues et en étaient même devenues une attraction pour les habitués du bar."
show yoshino B8 Y5 at left, xflip
with dissolve
yoshino "Ran ! Bordel, si tu continues à dormir au boulot, t’auras affaire à moi !"
show ran B6 S1 Y8 at right
with dissolve
ran "Mais enfin, voyons, nul besoin de s’énerver ainsi, mademoiselle Yoshino… Vous voyez bien que mademoiselle Ezo gère très bien le bar."
show yoshino B4 S2 Y1 at left, xflip
with dissolve
yoshino "Justement, ce serait bien que tu lui files un coup de main… Laisse-la préparer un peu les alcools et prends le relais au service."
show ran B5 S1 Y2 at right
with dissolve
ran "Mais vous n’y pensez pas ! Une enfant, si jeune, manipuler les bouteilles !"
hide ran
with dissolve
show yoshino B4 S2 Y1 Go at xflip, right
with dissolve
yoshino "Mouais, t’as pas forcément tort…"
show ezo B7 Y5 at left, xflip
with dissolve
ezo "Eh ! Oh ! Je suis pas une gamine !"
show yoshino B1 S1 Y4 -Go at right
with dissolve
yoshino "Ah bon ? C’est vrai que je t’ai pas demandé ton âge…"
show ezo B1 Y5 at left, xflip
with dissolve
ezo "J’ai 14 ans !"
"En disant cela, Ezo s’était tenue bien droite, et avait annoncé son âge bien haut. Ce n’était plus une gamine, après tout. Mais Ran et Yoshino restèrent de marbre."
hide yoshino
with dissolve
show ran B4 S1 Y3 at right
with dissolve
ran "C’est bien ce que je pensais, elle est bien trop jeune pour ça…"
show ezo B8 Y5 at left, xflip
with dissolve
ezo "QUOI !? Je suis pas trop jeune ! Et pis d’abord, vous avez quel âge, vous ?"
hide ran
with dissolve
show yoshino B1 S1 Y2 at right
with dissolve
yoshino "17."
hide yoshino
with dissolve
show ran B2 S1 Y2 at right
with dissolve
ran "J’ai 16 ans."
show ezo B1 S3 Y7 at left, xflip
with dissolve
ezo "Que…"
show ran B2 S1 Y2 at right
with dissolve
ran "Vous devez être la plus jeune des employées. Sei et Akié ont 15 ans toutes les deux. Quant à Clateau, eh bien…"
hide ran
with dissolve
show yoshino B2 S2 Y3 at right
with dissolve
yoshino "Il est vieux."
hide yoshino
with dissolve
show ran B2 S1 Y4 at right
with dissolve
ran "Je ne l’aurais pas dit ainsi mais…"
show ezo B4 S1 Y2 at left, xflip
with dissolve
ezo "Vous allez voir !"
hide ezo
with dissolve
"Ezo s’empara des bouteilles que tenait Ran, et commença à répondre aux commandes à sa place. Étonnamment, elle connaissait chaque alcool qui lui était demandé, et elle n’hésitait qu’au moment de chercher la bouteille sur l’immense présentoir sur lesquelles elles trônaient."
show yoshino B1 S1 Y1 at left, xflip
with dissolve
yoshino "Eh ben…"
show ran B2 S1 Y2 at right
with dissolve
ran "Mademoiselle Ezo, c’est impressionnant !"
hide yoshino
with dissolve
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "Voilà ce que c’est que de vivre la moitié de sa vie avec des soudards ! Il n’y a pas un alcool que je ne connaisse !"
hide ezo
with dissolve
hide ran
with dissolve
show clateau B1 S1 Y1 at left, xflip
with dissolve
clateau "Yoshino ? J’ai besoin d’aide. Qu’est-ce qui se passe ?"
show yoshino B5 S1 Y2 at right
with dissolve
yoshino "Incapable de tenir une cuisine sans moi hein ? Pfff… J’arrive."
hide yoshino
with dissolve
hide clateau
with dissolve
show clateau B1 S1 Y4 at right
with dissolve
clateau "Ah, Ezo ! Alors, comment ça se passe au bar ? Tu t’y habitues ?"
show ezo B1 S3 Y4 at left, xflip
with dissolve
ezo "Plutôt ouais !"
hide clateau
with dissolve
show ran B1 S1 Y4 at right
with dissolve
ran "Elle est formidable, cette petite !"
show ezo B1 S1 Y8 at left, xflip
with dissolve
ezo "Chuis pas petite…"
show ran B1 S1 Y3 at right
with dissolve
ran "Mais quand même, faire boire des enfants si jeunes, les soldats sont vraiment dénués de morale…"
show ezo B2 S3 Y4 at left, xflip
with dissolve
ezo "Reconnais que c’est plutôt pratique au final."
hide ran
with dissolve
hide ezo
with dissolve
show yoshino B4 S3 Y1 at left, xflip
with dissolve
yoshino "Hein ? C’est toi qui lui a appris toutes ces choses sur les alcools ? Tu l’as quand même pas fait boire à son âge ?"
show clateau B6 S1  Y2 Go at right
with dissolve
clateau "Bah.... Vous savez, en occident les mœurs sont différentes, et quand on est soldat…"
show yoshino B4 S3 Y4 at left, xflip
with dissolve
yoshino "Viens voir par ici, qu’on s’explique"
show clateau B6 S1  Y2 -Go at right
with dissolve
clateau "Hein ? Non, attends…!!"
"Yoshino attrapa Clateau par le col et la porte de la cuisine se referma avec fracas."
hide yoshino
with dissolve
hide clateau
with dissolve
show ran B4 S1 Y2 Go at right
with dissolve
ran "Toujours aussi effrayante, cette Yoshino…"
show ezo B1 S3 Y4 at left, xflip
with dissolve
ezo "Tu crois ? Clateau, il a toujours été un peu mou."
show ran B1 S1 Y2 at right
with dissolve
ran "Ah bon ? Je ne puis dire que le patron soit quelqu’un de caractère, mais il a toujours été motivé dans son restaurant."
show ezo B2 S2 Y2 at left, xflip
with dissolve
ezo "Je vois…"
"Ezo s’assit sur une chaise, et repensa un peu à Clateau pendant la guerre. C’était un petit lieutenant d’artillerie. Il n’était pas très bon, ni très mauvais, et se contentait de remplir ses ordres comme on le lui demandait."
"Quand elle lui parlait, elle se souvenait qu’il était souvent pessimiste sur le cours des choses, le déroulement des batailles. Mais il était vif d’esprit, et quand la situation l’exigeait, il parvenait à sortir son bataillon des plus mauvais coups."
"Ezo avait toujours pensé que ce défaitisme arboré était la marque de son expérience en tant que soldat."
show ezo B2 S2 Y2 at left, xflip
with dissolve
ezo "Au final, la guerre, c’était juste pas son truc…"
show ran B1 S1 Y2 at right
with dissolve
ran "Hum ? Vous avez dit quelque chose ?"
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "Non, rien ! Maintenant, au travail ! La table 14 attends ses sandwichs depuis tout à l’heure."
show ran B5 S1 Y2 at right
with dissolve
ran "Oh, diantre ! Vous avez raison !"
hide ezo
with dissolve
hide ran
with dissolve
"Pendant leur discussion avec Yoshino et Clateau, l’heure tournait, et le bar se remplissait de plus en plus. Ezo et Ran, bien réveillée cette fois-ci, s’affairaient à faire tourner le bar."
show ezo B5 S3 Y2 at left, xflip
with dissolve
ezo "Ça se remplit de plus en plus !"
show ran B1 S1 Y4 at right
with dissolve
ran "Oui, mais on est bientôt à notre limite. La plupart des clients qui vont venir par la suite viendront pour manger au restaurant."
hide ran
with dissolve
$akie_nom = "???"
akie "Excusez-moi, un sandwich s’il vous plaît !"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Oui, j’arr.. Akié ?"
show akie B1 S1 Y4 at right
with dissolve
$akie_nom = "Akié"
akie "Héhé ! Alors, tout va bien ici ?"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Tu devrais pas être en salle avec Sei pour accueillir les clients ?"
show akie B1 S1 Y2 at right
with dissolve
akie "Si si, d’ailleurs le moment difficile de la soirée ne va pas tarder à commencer. On prend notre pause à tour de rôle avec Sei juste avant."
show ezo B2 S3 Y2 at left, xflip
with dissolve
ezo "Voilà ton sandwich."
show akie B2 S1 Y4 at right
with dissolve
akie "Miam ! Merci bien ! Ton travail au bar se passe bien ?"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Je m’y suis plutôt habituée oui."
show akie B1 S1 Y2 at right
with dissolve
akie "C’est bien ça ! J’aime les gens avec de l’énergie !"
hide ezo
with dissolve
show ran B1 S1 Y4 at left, xflip
with dissolve
ran "Mademoiselle Akié est la plus énergique de tout le personnel."
show akie B2 S1 Y3 at right
with dissolve
akie "Et toi la plus indolente !"
show ran B1 S1 Y4 at left, xflip
with dissolve
ran "En effet…"
show akie B1 S1 Y2 at right
with dissolve
akie "Bon, il est l’heure d’y retourner. À plus !"
hide akie
with dissolve
hide ran
with dissolve
"Akié se lécha les doigts, épousseta d’un revers de main son uniforme de serveuse, et repartit en direction de la salle."
"Immédiatement après, c’est Sei qui arriva. Contrairement à Akié, elle était plutôt calme."
"Elle prit place dans un coin moins agité et elle sortit un livre. Ran, qui avait l’habitude, se contenta de demander un sandwich à Yoshino, sans que Sei n’ait eu à dire quoi que ce soit."
"Ezo était un peu intriguée, et elle se décida à lui parler un peu lorsqu’elle vint lui apporter son sandwich."
show ezo B3 S3 Y2 at left, xflip
with dissolve
ezo "Un livre de poésie, hein ?"
show sei B2 S1 Y1 at right
with dissolve
sei "Oui, en effet. J’adore la littérature."
show ezo B2 S3 Y2 at left, xflip
with dissolve
ezo "Je dirais que ça te va bien, en effet."
show sei B2 S1 Y3 at right
with dissolve
sei "Ah bon ? En tout cas, je ne pensais pas qu’une étrangère aurait reconnu le Manyôshû."
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Je ne m’y connais pas trop en littérature non plus, mais un soldat à Hakodate en lisait des passages, parfois."
show sei B2 S1 Y2 at right
with dissolve
sei "Hakodate… je… je n’ose pas trop te demander comment c’était, la guerre, je suppose que…"
show ezo B4 S3 Y3 at left, xflip
with dissolve
ezo "C’était pas top, si tu veux tout savoir, en effet."
show sei B4 S1 Y2 at right
with dissolve
sei "Désolée…"
show ezo B4 S3 Y4 at left, xflip
with dissolve
ezo "Ne t’inquiète pas, ça a été mon quotidien pendant un moment, ça ne me dérange pas."
show sei B1 S1 Y1 at right
with dissolve
sei "Je te le prête, si tu veux."
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Hein ? Ah, merci mais tu en a besoin non ?"
show sei B1 S1 Y1 at right
with dissolve
sei "Je le connais déjà par cœur."
show ezo B1 S3 Y7 at left, xflip
with dissolve
ezo "HEIN ? La vache, c’est énorme !"
show sei B1 S1 Y3 at right
with dissolve
sei "C’est juste ma passion."
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Avec une telle connaissance, pourquoi travailler dans un restaurant comme serveuse ? Tu pourrais passer un certificat ou quelque chose de mieux, non ?"
show sei B1 S1 Y1 at right
with dissolve
sei "Même si la société est réformée, c’est toujours difficile pour une fille d’étudier… et j’aimerais vraiment découvrir la littérature étrangère ! Mais pour ça il me faut de l’argent."
show ezo B2 S3 Y2 at left, xflip
with dissolve
ezo "Donc tu travailles ici ?"
show sei B2 S1 Y3 at right
with dissolve
sei "Oui. Ce n’est pas trop dur et Clateau est plutôt gentil, des fois il parvient à me récupérer des livres en langues étrangères grâce à ses contacts."
show ezo B4 S2 Y1 at left, xflip
with dissolve
ezo "Ah, ouais ? En effet c’est gentil de sa part… mais je me demande s’il n’y aurait pas une raison cachée… ce sale lolicon !"
show sei B4 S2 Y1 at right
with dissolve
sei "Tu as dit quelque chose ?*"
show ezo B2 S3 Y4 at left, xflip
with dissolve
ezo "Ahaha, rien du tout ! Bon, je vais te laisser manger, il faut que je retourne bosser."
show sei B1 S1 Y1 at right
with dissolve
sei "Moi aussi. Bonne chance pour la suite du service."
hide sei
with dissolve
"Après avoir salué Sei, Ezo retourna au comptoir. Elle y retrouva Ran qui s’était encore endormie debout. Cette fois, elle était carrément plantée au milieu de la salle bondée, avec un plateau dans les mains."
show ezo B7 S3 Y6 at left, xflip
with dissolve
ezo "Sérieusement…"
"Au même moment, huit heures venaient de sonner et les ouvriers arrivaient en masse. Parmis les gros bras et les muscles saillant, une petite tête se faufilait entre eux jusqu’au comptoir et sauta sur une chaise."
"Elle salua Ezo qui essuyait un verre derrière le bar."
show tsugumi B1 S1 Y4 at right
with dissolve
tsugumi "Me revoilà ! Alors mon petit fantassin, ça a été, la première journée de travail ?"
show ezo B1 S3 Y4 at left, xflip
with dissolve
ezo "Comme tu peux le voir, ça va plutôt bien."
show tsugumi B1 S1 Y1 at right
with dissolve
tsugumi "Et Ran ?"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Juste là."
"Tsugumi se retourna pour voir Ran toujours endormie et toujours plantée au milieu de la salle."
show tsugumi B1 S2 Y1 at right
with dissolve
tsugumi "Tu vas pas la réveiller ?"
show ezo B1 S3 Y6 at left, xflip
with dissolve
ezo "J’hésite entre ça et attendre que Yoshino le fasse."
show tsugumi B1 S1 Y2 at right
with dissolve
tsugumi "Pas faux, ça nous fera un bon divertissement. Bon, mets-moi une pression bien fraîche s’teuplaît !"
show ezo B2 S3 Y2 at left, xflip
with dissolve
ezo "Ça arrive."
show tsugumi B1 S1 Y1 at right
with dissolve
tsugumi "T’en prendras bien une avec moi ? Pour fêter ton premier jour dans la Gargotte de Clateau !"
menu:
    "boire":
        $relation_tsugumi += 1
        show ezo B1 S3 Y4 at left, xflip
        with dissolve
        ezo "Ouais, allez. Mais je te préviens, j’ai une bonne descente !"
        show tsugumi B1 S1 Y2 at right
        with dissolve
        tsugumi "Pas autant que moi, tu verras !"
    " ne pas boire":
        $relation_tsugumi -= 1
        show ezo B1 S1 Y2 at left, xflip
        with dissolve
        ezo "Je ne bois jamais pendant le service !"
        show tsugumi B2 S1 Y4 at right
        with dissolve
        tsugumi "Pff, t’es trop rigide, toi…"
"Ezo et Tsugumi discutaient toutes les deux alors que Ran restait plantée comme un piquet au milieu de la salle."
"Derrière le bar, Ezo, qui avait vu la scène et qui s'apprêtait à lancer une assiette dans la tête du malotru, reposa son arme, l’air stupéfaite."
show ezo B1 S3 Y7 at left, xflip
with dissolve
ezo "Eh bien… je croyais qu’elle dormait…"
show tsugumi B3 S1 Y2 at right
with dissolve
tsugumi "Mais elle dort ! À force de pioncer en plein travail, elle a développé des capacités étonnantes. On l’appelle « Ran l’impassible ». Elle résiste à tout."
hide ezo
with dissolve
hide tsugumi
with dissolve
"La porte de la cuisine s’ouvrit avec fracas, et une Yoshino encore plus en colère que d’habitude en sortit."
show yoshino B8 Y5 at right
with dissolve
yoshino "RAN !"
hide yoshino
with dissolve
"Lorsqu’elle avait crié dans le bar, tout le monde s’était tu. Même les armoires à glace rentrées plus tôt ne bronchaient pas."
show ezo B4 S3 Y8 at left, xflip
with dissolve
ezo "Là, elle va y passer…"
show tsugumi B1 S1 Y1 at right
with dissolve
tsugumi "Non, attends, tu vas voir…"
"Yoshino précipita un de ses couteaux en direction de Ran, qui esquiva magistralement."
show ezo B7 S3 Y7 at left, xflip
with dissolve
ezo "Wow…"
hide ezo
with dissolve
hide tsugumi
with dissolve
"S'ensuivit ensuite une courte passe d’arme où Yoshino, qui devenait de plus en plus furieuse coup après coup, tentait de dégommer une Ran qui esquivait dans sa somnolence chaque lancer tout en gardant son équilibre."
show yoshino B4 S3 Y4 at left, xflip
with dissolve
yoshino "Hmpff… ça sera le dernier coup."
show clateau B3 S4 Y3 at right
with dissolve
clateau "Stop !"
"Clateau venait de surgir de derrière Yoshino, et avait attrapé celle-ci par le col avant qu’elle ne lance son dernier couteau."
show yoshino B6 S1 Y2 at left, xflip
with dissolve
yoshino "Mais patron ! Elle… elle…"
show clateau B4 S3 Y1 at right
with dissolve
clateau "Je sais bien, mais tu effraie les clients, là."
"Suspendue dans les airs, Yoshino ne trouva rien à dire et se contenta d’arborer un visage boudeur."
show clateau B3 S3 Y1 at right
with dissolve
clateau "Ran !"
"Ran, au milieu du champs de bataille qu’était devenue la pièce, se réveilla enfin."
show clateau B3 S3 Y1 at right
with dissolve
clateau "Ran, essaye d’être un peu plus active ! Tu vois bien que Yoshino croule sous le travail à cause de toi !"
"Ran se contenta d'acquiescer et de revenir à sa place derrière le bar. Enfin, Clateau et Yoshino retournèrent d’où ils étaient venus."
hide clateau
with dissolve
hide yoshino
with dissolve
show tsugumi B1 S1 Y1 at right
with dissolve
tsugumi "Ça ne serait pas arrivé si tu l’avais réveillée dès le début."
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Bah, vu le spectacle, ça valait le coup."
hide ezo
with dissolve
hide tsugumi
with dissolve
"Les discussions et le brouhaha reprirent de plus belle. On voyait les allers et venues de ceux qui s’arrêtaient manger au restaurant. Le soir commençait à tomber et de plus en plus de gens rentraient chez eux."
"Le bar tout comme le restaurant se vidaient petit à petit. Finalement, Tsugumi resta la seule dans le bar. L’équipe allait bientôt terminer son service, et Akié et Sei vinrent au bar aussi, alors que le restaurant venait de fermer."
show akie B1 S1 Y2 at right
with dissolve
akie "Pfiou, c’était bien crevant !"
show sei B1 S1 Y1 at left, xflip
with dissolve
sei "C’était encore une rude journée."
"Elles prirent chacune un verre. Sei, étonnamment, prit un verre de chartreuse. Ezo fut interloquée de ce choix d’alcool fort, mais finalement elle trouva que cela reflétait bien le côté mature qui se dégageait d’elle."
hide sei
with dissolve
"Akié opta pour un jus de fruit, ce qui collait mieux à son air enfantin. Le temps passa, et ce fut au tour de Clateau et de Yoshino de sortir des cuisines."
hide akie
with dissolve
"Yoshino se mit à l’un des tabourets et s’étira longuement."
show yoshino B2 S1 Y4 at left, xflip
with dissolve
yoshino "Bon, une journée de plus en moins !"
show clateau B2 S1 Y4 at right
with dissolve
clateau "Vous avez tous bien travaillé."
hide yoshino
with dissolve
show akie B1 S1 Y4 at left, xflip
with dissolve
akie "Comme toujours !"
hide akie
with dissolve
show clateau B1 S1 Y1 at right
with dissolve
clateau "Et toi Ezo ? Comment a été ta première journée ?"
show ezo B2 S3 Y3 at left, xflip
with dissolve
ezo "Bien. Je ne peux pas dire que j’ai été aidée, mais au moins l’ambiance était bonne."
hide clateau
with dissolve
show ran B6 S1 Y4 at right
with dissolve
ran "Que dites vous, mademoiselle Ezo ! Alors que j’ai toujours été là pour vous."
show ezo B2 S3 Y1 at left, xflip
with dissolve
ezo "Et encore, elle au moins sait se tenir."
hide ran
with dissolve
show yoshino B5 S3 Y1 at right
with dissolve
yoshino "Si vous travailliez correctement, je n’aurais pas à intervenir !"
hide yoshino
with dissolve
show clateau B1 S1 Y1 at right
with dissolve
clateau "Ahaha, je vois que tu t’es déjà bien intégrée au groupe."
show ezo B4 S3 Y3 at left, xflip
with dissolve
ezo "Difficile de faire autrement."
hide clateau
with dissolve
show tsugumi B2 S1 Y3 at right
with dissolve
tsugumi "Alalah, t’en as de la chance quand même, d’avoir des camarades pareils au travail…"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "C’est pas ton cas ?"
show tsugumi B2 S1 Y1 at right
with dissolve
tsugumi "Bof… Les autres ouvriers ont tendance à mépriser qu’une gamine comme moi travaille avec eux. Sans parler du patron, une vraie plaie !"
show ezo B4 S3 Y2 at left, xflip
with dissolve
ezo "Si c’était moi, je les aurai déjà remis à leur place."
show tsugumi B1 S1 Y1 Go at right
with dissolve
tsugumi "Je n’ai pas cette force, et je ne suis pas militaire, on ne peut pas faire ce qu’on veut."
hide tsugumi Go
with dissolve
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Donc il n’y a rien que tu puisses faire ?"
show tsugumi B2 S1 Y1 at right
with dissolve
tsugumi "Bah… On a bien un syndicat, mais c’est difficile de faire bouger les choses. C’est pour ça que je te disais que tu avais de la chance d’avoir des camarades pour te soutenir."
menu:
    "C’est parce que j’ai eu une bonne collègue que ça s’est bien passé":
        $relation_ran += 1
        show ezo B1 S3 Y4 at left, xflip
        with dissolve
        ezo "C’est parce que j’ai eu une bonne collègue que ça s’est bien passé."
        hide tsugumi
        with dissolve
        show ran B6 S1 Y4 R2 at right
        with dissolve
        ran "Con… Contente d’avoir pu vous être utile."
    "Tu sais, j’ai aussi une très bonne clientèle":
        $relation_tsugumi += 1
        show ezo B1 S3 Y4 at left, xflip
        with dissolve
        ezo "Tu sais, j’ai aussi une très bonne clientèle"
        show tsugumi B1 S1 Y1 R1 at right
        with dissolve
        tsugumi "Ah… Tu crois ? Eh bien… Je suis contente d’avoir pu t’aider."
hide tsugumi
with dissolve
hide tsugumi
with dissolve
hide ran
with dissolve
show clateau B1 S1 Y1 at right
with dissolve
clateau "Quand je pense à tout ce que nous avons vécu avant d’en arriver là, je me demande si ce n’est pas un miracle de pouvoir vivre aussi paisiblement maintenant."
show ezo B2 S3 Y2 at left, xflip
with dissolve
ezo "La guerre est finie, on ne craint plus grand-chose maintenant."
show clateau B1 S1 Y1 at right
with dissolve
clateau "La guerre ne se termine jamais, regarde."
"Clateau lui tendit un journal froissé daté d’il y a déjà plusieurs semaines."
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "Un journal français ? Ça faisait un moment que j’en avais pas vu un."
show clateau B3 S1 Y1 at right
with dissolve
clateau "Les nouvelles ne sont pas très réjouissante. La France et la Prusse viennent de rentrer en guerre l’une contre l’autre."
show ezo B4 S1 Y2 at left, xflip
with dissolve
ezo "Encore une…"
hide ezo
hide clateau
with dissolve
"Ezo se colla aux étagères de bouteilles du bar et se mit à penser. Depuis toute petite elle n’avait fait que suivre les armées en campagne, et c’était jusqu’alors son seul moyen de survivre."
show tsugumi B2 S1 Y1 at left, xflip
with dissolve
tsugumi "J’ai peut-être parlé un peu vite tout à l’heure. Ça m’a l’air d’être dur de votre coté aussi. Entre être prise dans les combats, et ma condition actuelle, je préfère largement la deuxième option."
show clateau B1 S1 Y1 at right
with dissolve
clateau "Tu sais, au final, on finit par s’y habituer, mais c’est loin d’être une bonne vie. Si vous pouvez vous tenir éloigner de la guerre autant que possible, tant mieux. C’est le conseil d’un ancien soldat."
show tsugumi B2 S1 Y1 at left, xflip
with dissolve
tsugumi " Hmm…"
hide tsugumi
with dissolve
hide clateau
with dissolve
"Suite à ces déclarations, l’ambiance s’était un peu refroidie. Comme plus personne ne relançait de discussion, c’est finalement Akié qui brisa la glace. La conversation put reprendre, sur des choses plus banales. Finalement, l’heure de partir arriva."
show yoshino B1 S1 Y1 at right
with dissolve
yoshino "Il est tard, il serait l’heure de rentrer chez nous."
show sei B1 S1 Y1 at left, xflip
with dissolve
sei "Oui, mieux vaut ne pas partir trop tard, la nuit tombe vite et les ruelles sont dangereuses."
show akie B1 S1 Y2 at left, xflip
hide sei
with dissolve
akie "Tu stresses trop, y’a pas de problème !"
show yoshino B1 S1 Y4 Go at right
with dissolve
yoshino "Rappelle-moi qui s’est fait sauver d’une agression hier matin…"
show akie B1 S1 Y4 at left, xflip
with dissolve
akie "Héhé…"
hide akie
with dissolve
hide yoshino
with dissolve
show sei B1 S1 Y1 at right
with dissolve
sei "On ferait mieux de rentrer ensemble, Yoshino. Avec toi il ne nous arrivera rien."
hide yoshino
with dissolve
hide sei
with dissolve
# Si point tsugumi>point Ran
if relation_tsugumi > relation_ran:
    show tsugumi B3 S1 Y1 at right
    with dissolve
    tsugumi "Si c’est une question de protection, je pense qu’Ezo aussi pourrait très bien le faire, non ?"
    show akie B2 S1 Y4 at left, xflip
    with dissolve
    akie "Je peux confirmer qu’elle est très forte, oui !"
else:
    # Si point Ran>point Tsugumi
    show ran B1 S1 Y2 at right
    with dissolve
    ran "Si c’était mademoiselle Ezo qui m’accompagnait, je me sentirais en sécurité."
    show akie B2 S1 Y4 at left, xflip
    with dissolve
    akie "Ça, je peux te l’assurer !"
    hide akie
    with dissolve
    hide ran
    with dissolve
    hide tsugumi
    with dissolve
# TODONE fondu en noir
scene bg Black
with dissolve

scene bg grenier
with dissolve
"Cette déclaration fit rire l’assemblée, qui se dispersa bien vite, fatigue et heure tardive aidant. Ezo monta dans sa chambre. En passant, elle vit Clateau, qui terminait de ranger la salle."
show clateau B1 S1 Y1 at right
with dissolve
clateau "Alors, ce premier jour ?"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "C’était dur, mais aussi amusant !"
show clateau B1 S1 Y1 at right
with dissolve
clateau "Content que tu t’y plaises."
show ezo B2 S3 Y2 at left, xflip
with dissolve
ezo "Je me souviens qu’il y a longtemps tu avais dit que tu prendrais soin de moi, je ne peux pas dire que tu aies menti."
"Clateau se passa la main dans les cheveux, rougissant."
show clateau B2 S1 Y1 R1 at right
with dissolve
clateau "Tu sais… en tant que militaire, je n’ai jamais eu d’enfants… et je ne pouvais pas te laisser passer ta vie dans l’armée."
"Ezo lui sourit. Elle était vraiment heureuse qu’il l'ait ramenée ici."
hide clateau
with dissolve
"Dans sa chambre, Ezo marchait à taton dans la pièce maintenant noire. Elle se déshabilla à peine avant de tomber sur son lit."
hide ezo
with dissolve
# TODONE fondu en noir
scene bg Black
with dissolve

scene bg grenier
with dissolve
"Le lendemain, en se réveillant, elle remarqua aux rayons du soleil déjà bien fort qu’elle avait beaucoup dormi. Elle ne rechignait pas à faire des grassses matinées, mais c’était bien la première fois que son horloge de soldat ne l’avait pas réveillée."
"En voulant enfiler ses vêtements, elle se fit la réflexion que là encore elle portait un uniforme. Mais cette fois-là, elle n’avait pas cette espèce de pression qui se manifestait habituellement quand elle portait son uniforme de soldat."
"Pendant qu’elle s'habillait, elle fut dérangée par Clateau qui toquait à sa porte."
hide clateau
with dissolve
clateau "Ezo ? Il est l’heure !"
"Puis, Clateau tenta d’ouvrir la porte."
"Furieuse qu’on la dérange, elle envoya dans la tête de Clateau une boule d’habits."
show ezo B4 S2 Y8 at left, xflip
with dissolve
ezo "Non mais !"
"Elle continua ce qu’elle était en train de faire, puis elle s’arrêta net, devenant progressivement toute rouge."
"De son coté, Clateau aussi était cramoisi. Dans la boule de vêtement catapulté, la pièce blanche brodée sur les cotés était visiblement une culotte. Il n’osait pas vraiment le notifier à Ezo, sachant à l’avance que son sort serait scellé."
"Au final, ce fut Ezo qui entrouvrit légèrement la porte."
show ezo B1 S3 Y2 R2 at left, xflip
with dissolve
ezo "Clateau… tu… tu as ma culotte ?"
show clateau B1 S1 Y1 at right
with dissolve
clateau "Ah ! Oui ! Mais ne crois pas que je l’ai gardée pour moi, je ne savais juste pas comment te la rendre…"
show ezo B1 S3 Y2 R2 at left, xflip
with dissolve
ezo "Je sais je sais… mais rends-la moi."
show clateau B1 S1 Y1 R1 at right
with dissolve
clateau "Bien sûr !"
hide clateau
with dissolve
hide ezo
with dissolve
"Le petit déjeuner dans l'appartement de Clateau fut silencieux. Pour échapper à cette ambiance bizarre et parce qu’elle était déjà bien en retard, Ezo attrapa un croissant et fila en salle. En le prenant, elle se fit la réflexion que décidément, Clateau n’avait jamais réussi à se faire au petit déjeuner japonais."
# TODONE fondu en noir
scene bg Black
with dissolve

scene bg bar
with dissolve
"Une fois au bar, Ezo s’étonna de croiser Tsugumi."
show ezo B4 S3 Y6 at left, xflip
with dissolve
ezo "Déjà venue picoler !?"
show tsugumi B1 S1 Y2 at right
with dissolve
tsugumi "Mais non ! Je suis venue prendre quelques restes. J’ai été appelée au travail plus tôt que prévu et j’ai pas eu le temps de déjeuner."
"Ezo prit le croissant qu’elle avait fourré dans sa poche."
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Tiens, prends ça aussi."
show tsugumi B1 S1 Y1 at right
with dissolve
tsugumi "Oh, merci Ezo ! Ça me remonte le moral !"
show ezo B1 S3 Y4 at left, xflip
with dissolve
ezo "Et bonne chance !"
show tsugumi B3 S1 Y1 at right
with dissolve
tsugumi "Je vais essayer."
"La petite ouvrière partit en courant comme à son habitude. Ezo se demanda si tout irait bien pour elle…"
hide tsugumi
with dissolve
hide ezo
with dissolve
"Dans la matinée, rien de spécial, si ce n’est que le restaurant reçut le journal. Comme elle n’avait rien de mieux à faire Ezo entreprit de le lire. Alors qu’elle était concentrée, c’est Clateau qui arriva derrière elle."
show ezo B6 S3 Y7 at left, xflip
with dissolve
ezo "Wah ! Je glandouillais pas !"
"Le militaire regardait le journal avec intérêt. Il pointa du doigt un des articles."
show clateau B1 S1 Y1 at right
with dissolve
clateau "Regarde, dans les pages de l’actualité étrangère."
"Un des articles parlait d’un défaite française contre la Prusse, à Sedan. Et de préciser que l’empereur Napoléon avait été capturé."
show ezo B4 S3 Y2 at left, xflip
with dissolve
ezo "Ah, c’est marrant ça ! On vient de restaurer un empereur ici et voilà qu’un autre chute à l’autre bout du monde."
show clateau B3 S1 Y1 at right
with dissolve
clateau "Je me demande ce qu’il va se passer."
"Ran, qui somnolait à coté, se permit d’intervenir en entendant les deux militaires parler."
hide clateau
with dissolve
show ran B4 S1 Y2 at right
with dissolve
ran "Ce sera sûrement difficile pour les survivants. Moi-même, je viens d’une petite famille de samouraïs attachée au shogun, et si jamais mon père n’avait pas prit des mesures pour garantir notre survie, je suis sûre qu’un jour nous aurions été décimés."
show ezo B4 S3 Y2 at left, xflip
with dissolve
ezo "C’est vrai, mais… après tout, cela ne faisait même pas vingt ans que le second empire existait, les gens s’en remettront. Par contre, pour le shogunat… j’espère que tout ira bien pour toi dans le futur."
show ran B5 S1 Y2 at right
with dissolve
ran "Ne vous inquiétez pas, mademoiselle Ezo ! Je suis pleine de ressources, et je suis bien consciente que notre statut n’a rien d’éternel."
hide ran
hide ezo
with dissolve
"Ezo n’eut pas trop le temps de réfléchir aux déclarations de Ran. Le midi arrivait et les clients avec. Plus habituée à son poste, le travail fut moins difficile pour Ezo. Et elle savait aussi comment s’y prendre pour réveiller Ran quand elle piquait du nez."
"Puis, Tsugumi revint."
show tsugumi B1 S1 Y2 at right
with dissolve
tsugumi "Me revoilà ! Ran, comme d’habitude s’il te plait, mais vite, je n’ai pas beaucoup de temps !"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Elle dort… Qu’est-ce que je te mets ?"
show tsugumi B3 S1 Y1 at right
with dissolve
tsugumi "Un sandwich s’il te plaît."
show ezo B4 S3 Y2 at left, xflip
with dissolve
ezo "Pas trop dur aujourd’hui ?"
show tsugumi B2 S1 Y3 at right
with dissolve
tsugumi "Si, carrément ! Mon patron est bien trop dur avec moi, je n’en peux plus ! Et les cadences sont infernales, on a l’impression de devoir construire toute une flotte de guerre pour le mois prochain."
show ezo B4 S3 Y3 at left, xflip
with dissolve
ezo "C’est vrai que tu travailles dans une usine navale…"
show tsugumi B2 S1 Y1 at right
with dissolve
tsugumi "Yep ! Depuis le retour de l’empereur les gros bonnets du gouvernement n’ont que le mot modernisation à la bouche… Comme si ils voulaient attaquer la Chine ou la Russie dans les prochaines années. Enfin bon, pour le moment, ça me fait vivre, alors je ne me plains pas trop !"
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "Ça doit pas être facile quand même…"
show tsugumi B1 S1 Y2 at right
with dissolve
tsugumi "Ça non ! Mais ça ira bientôt mieux. Si le gouvernement se modernise, nous aussi ! On a appris un truc d’un marin anglais y’a pas longtemps : le syndicat ! On va se réunir avec les autres ouvriers pour en parler, ça semble super !"
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "Oh, bonne initiative !"
hide tsugumi
with dissolve
show ran B4 S1 Y3 at right
with dissolve
ran "Si mon père savait que je m'acoquine avec des républicains syndicalistes… le pauvre n’en survivrait pas…"
hide ran
with dissolve
show tsugumi B1 S1 Y5 at right
with dissolve
tsugumi "Ouah, t’es réveillée ?"
hide tsugumi
with dissolve
show ran B4 S1 Y8 at right
with dissolve
ran "Depuis un moment !"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Dit voir, Ran, ça ne te dérange pas, ce qu’on dit ?"
show ran B1 S1 Y4 at right
with dissolve
ran "Tu sais, avant de m’occuper de politique, je m’occupe déjà de moi-même, et quand j’ai su à quel rythme devait travailler mademoiselle Tsugumi, j’en ai été horrifiée !"
show ezo B2 S3 Y4 Go at left, xflip
with dissolve
ezo "Je m’en doutais…"
hide ezo
with dissolve
hide ran
with dissolve
"Tsugumi avala son sandwich, et remercia Ezo et Ran pour la discussion."
show tsugumi B1 S1 Y2 at left, xflip
with dissolve
tsugumi "Bon, c’est pas tout ça, mais je dois y aller ! Bonne journée à vous !"
hide tsugumi
with dissolve
"La fin de journée se passa comme d’habitude. Ran et Ezo travaillèrent, ou en tout cas essayèrent. Le soir, Tsugumi revint, un peu plus tôt que d’habitude."
$tsugumi_route = False
# Si les points tsugumi>points Ran
if relation_tsugumi > relation_ran:
    show tsugumi B4 S1 Y1 at right
    with dissolve
    tsugumi "Dit Ezo, ça te dirait de venir à notre fameuse réunion syndicale ? Tu m’avais l’air intéressée."
    hide tsugumi
    with dissolve
    menu:
        " Oui, pour sûr !":
            show ezo B2 S3 Y4 at left, xflip
            with dissolve
            ezo "Oui, pour sûr !"
            show tsugumi B1 S1 Y2 at right
            with dissolve
            tsugumi "Je savais que tu serais partante ! Elle se tiendra sur le port, pas loin de l’usine, lors de ton prochain jours de repos. Soit là à l’heure, on attendra pas les retardataires !"
            show ezo B2 S3 Y2 at left, xflip
            with dissolve
            ezo "Compte sur moi !"
            $tsugumi_route = True
        " Non, désolée.":
            show ezo B1 S3 Y2 Go at left, xflip
            with dissolve
            ezo "Non, désolée. j’ai encore beaucoup de choses à faire avec ma récente arrivée."
            show tsugumi B2 S2 Y1 at right
            with dissolve
            tsugumi "Oh, je vois… dommage."
hide tsugumi
with dissolve
hide ezo
with dissolve
"Tsugumi se posa sur le bar, fatiguée par sa journée de travail. Elle sembla un moment dans ses pensées, avant de reprendre de plus belle."
show tsugumi B1 S1 Y2 at right
with dissolve
tsugumi "Allez Ran, une bière ! Et cette fois, buvez avec moi, vous deux !"
show ran B4 S1 Y4 at left, xflip
with dissolve
ran "Bon, d’accord… mais alors pas de bière ! Je vais vous faire goûter de la liqueur ; regardez cette chartreuse que j’ai chipée à Clateau… C’est plutôt rare par ici."
hide ran
with dissolve
show tsugumi B4 S1 Y1 Go at right
with dissolve
tsugumi "Quitte à boire de l’alcool fort je préférerais du saké…"
hide tsugumi
show ran B5 S1 Y2 at right
with dissolve
ran "Allons, mademoiselle Tsugumi ! C’est l’occasion de découvrir une nouvelle saveur ! Cela ne vous intéresse-t-il donc pas !"
show tsugumi B1 S2 Y3 Go at left, xflip
with dissolve
tsugumi "Bon d’accord, envoie."
hide tsugumi
with dissolve
hide ran
with dissolve
"Ran sortit, toute fière, la grande bouteille verte, et servit un verre à chacune de ses comparses."
"L’alcool leur monta vite à la tête, et les rires qui en découlaient attirèrent à elles Clateau."
show clateau B2 S1 Y1 at right
with dissolve
clateau "Tiens, vous buvez ?"
show ran B7 S1 Y7 at left, xflip
with dissolve
ran "Euh, c’est juste pour goûter, je ne voulais pas…"
show clateau B1 S1 Y4 at right
with dissolve
clateau "Ça me fait penser à la première fois où Ezo a bu de l’alcool…"
hide ran
with dissolve
show ezo B4 S1 Y8 at left, xflip
with dissolve
ezo "Euh, pas la peine de raconter ça…"
show clateau B1 S1 Y4 at right
with dissolve
clateau "Elle l’a tellement mal supporté qu’elle s’était mise à se balader cul nul dans toute la caserne ! Je regrette de ne pas avoir de souvenir photo !"
show ezo B8 Y5 at left, xflip
with dissolve
ezo "AAAAAH, TAIS-TOI, LOLICON !"
"Ezo envoya son shot sur Clateau pour l'assommer."
"Celui-ci le reçut entre les deux yeux. Pendant ce temps, Ran et Tsugumi regardaient Ezo en se retenant de rire."
hide clateau
with dissolve
show ran B2 S1 Y4 at right
with dissolve
ran "Pfff, je ne pensais pas ça de vous, mademoiselle Ezo."
show ezo B8 Y5 at left, xflip
with dissolve
ezo "Te marre pas !"
hide ran
with dissolve
hide ezo
with dissolve
"À la fin de la journée, Tsugumi retourna chez elle."
# Si refus Tsugumi ou point Ran>Tsugumi
if tsugumi_route:
    jump tsugumi_ch2
show ran B2 S1 Y1 at right
with dissolve
ran "Ma chère Ezo…  Je me demandais, que diriez-vous de prendre le thé avec moi lors de notre jour de repos ?"
show ezo B1 S3 Y4 at left, xflip
with dissolve
ezo "Le thé ? Bah, si tu veux."
show ran B1 S1 Y4 at right
with dissolve
ran "Parfait ! Voici mon adresse."
hide ran
with dissolve
hide ezo
with dissolve
"Ezo, fatiguée de sa journée, salua Ran de la main, et pendant que cette dernière repartait, Ezo aussi se dirigea vers sa chambre."
jump ran_ch2
