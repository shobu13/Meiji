label salle_ch1:
    pass

init:
    image chapter = Text("{size=60}Travail en salle", font="gui/Sofia-Regular.otf", text_align=0.5, color="#e5cdcd")
show chapter:
    yanchor 0.5 ypos 0.5
    xanchor 0.5 xpos 0.5
with dissolve
with Pause(3)

scene bg grenier
with dissolve
"Les premiers rayons du soleil matinal vinrent caresser la joue d’Ezo, recroquevillée sur son lit. Elle passa sa main près de ses yeux comme pour les chasser, et ouvrit les yeux. Il était encore tôt, mais ses habitudes militaires la faisaient se lever aux aurores."
"Elle se roula un peu dans ses draps, ils étaient propres et frais. Cela faisait longtemps qu’elle n’avait pas dormi dans un confort relatif ; les camps militaires sont rarement des sinécures."
hide ezo
with dissolve
ezo "Aaaah, il va falloir que je me lève. Commençons cette nouvelle vie sur de bonnes bases, soldat !"
scene bg Black
with dissolve
# TODONE Ezo porte son uniforme de militaire
"Motivée, elle enfila son uniforme, et sortit de sa chambre, descendant les escaliers deux à deux et arriva en cuisine."
scene bg cuisine
show ezo Mi B3 S1 Y1
with dissolve
"Assez étonnamment, toute l’équipe était déjà présente, pour accueillir Ezo."
show ezo B1 S3 Y2 at right
with dissolve
ezo "Vous êtes déjà tous là !? "
show akie B1 S1 Y1 at left, xflip
with dissolve
akie "Oui, nous sommes réunis plus tôt pour ton intronisation parmi nous !"
hide akie
with dissolve
show ran B1 S1 Y6 at left, xflip
with dissolve
ran "Sachez qu’habituellement nous ne nous levons pas aussi tôt… "
hide ezo
with dissolve
show yoshino B1 S1 Y1 at right
with dissolve
yoshino "Ran, tout le monde, SAUF TOI, se lève aussi tôt !"
hide yoshino
with dissolve
hide ran
with dissolve
"Ran soupira, ce qui provoqua un petit rire dans l’assemblée."
show clateau B1 S1 Y1 at right
with dissolve
clateau "Bien, à partir de maintenant, je voulais vous annoncer à tous que Ezo rejoint officiellement notre restaurant. Elle officiera avec Akié et Sei, en salle."
show akie B1 S1 Y2 at left, xflip
with dissolve
akie "Oh, c’est vrai ? C’est super, Ezo !"
hide akie
with dissolve
hide clateau
with dissolve
show sei B2 S1 Y3 at left, xflip
with dissolve
sei "J’espère qu’on s’entendra bien toutes les deux."
hide sei
with dissolve
show ran B5 S1 Y6 at left, xflip
with dissolve
ran "Quoi ? Mais… mais je voulais qu’on m’aide au bar moi…"
show yoshino B4 S1 Y6 at right
with dissolve
yoshino "Tu aurais surtout refilée tout le boulot à la nouvelle…"
show ran B4 S1 Y8 at left, xflip
with dissolve
ran "Mais point du tout !"
hide ran
with dissolve
hide yoshino
with dissolve
show clateau B1 S1 Y4 at right
with dissolve
clateau "Allons, allons. C’est bientôt l’heure, les filles, au travail !"
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "Je suis motivée !"
hide clateau
with dissolve
hide ezo
with dissolve
"Ezo voulu partir vers la salle directement, mais elle fut retenue par Yoshino."
show yoshino B5 S1 Y1 at right
with dissolve
yoshino "Enfin, tu ne voulais quand même pas partir dans une tenue aussi crade ?"
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "Comment ça crade ? C’est mon uniforme !"
hide yoshino
with dissolve
show akie B1 S1 Y6 at right
with dissolve
akie "C’est vrai qu’il est usé…"
hide akie
with dissolve
show clateau B1 S3 Y4 at right
with dissolve
clateau "Regarde, Ran nous a cousue de superbes tenues, c’est, en quelques sortes, l’uniforme du restaurant !"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "L’uniforme du restaurant…"
"Ran remit à Clateau un paquet enveloppé de papier grossier."
show clateau B1 S1 Y1 at right
with dissolve
clateau "Voilà, on en avait déjà un en stock, j’ai juste demandé à Ran de le retoucher. C’est le tiens !"
hide ezo
with dissolve
hide clateau
with dissolve
"Ezo ouvrit le paquet, heureuse de la sollicitude de Clateau et de Ran à son égard. Le tout était étonnamment léger. Quand Ezo l’ouvrit, elle découvrit un ensemble de sous-vêtements en dentelle."
show ezo B5 S3 Y7 R1 at left, xflip
with dissolve
ezo "Qu… que que que… qu’est-ce que c’est que ça ?"
show akie B2 S1 Y4 at right
with dissolve
akie "Que c’est mignon !"
show ezo B5 S1 Y8 at left, xflip
with dissolve
ezo "Ne me dit pas que c’est ça ton uniforme ! Pervers !"
hide akie
with dissolve
show clateau B4 S1 Y6 at right
with dissolve
clateau "Non, attends…"
"Ezo ne laissa pas le temps à Clateau de s’expliquer et lui mit une grande claque sur la joue."
show ezo B8 S1 Y8 at left, xflip
with dissolve
ezo "Non mais !"
hide clateau
with dissolve
show yoshino B7 S1 Y6 at right
with dissolve
yoshino "Calme-toi… je pense qu’il y a erreur."
hide yoshino
with dissolve
hide ezo
with dissolve
"En disant cela, Yoshino appuya fortement son regard sur Ran, qui somnolait dans son coin. Elle se réveilla, et ouvrit de grands yeux en voyant ce que brandissant Ezo."
show ran B5 S1 Y7 at right
with dissolve
ran "Oh, diantre ! Il semble, mademoiselle Ezo, que je vous ai confiée mes sous-vêtements de rechange."
show ezo B7 S2 Y1 at left, xflip
with dissolve
ezo "Hein, c’est pas l’uniforme ?"
show ran B6 S1 Y8 at right
with dissolve
ran "Non non, c’est un ensemble que j’avais cousu suivant les derniers modèles de l’occident…"
hide ran
with dissolve
show sei B3 S1 Y3 Go at right
with dissolve
sei "En tout cas c’est audacieux…"
hide sei
with dissolve
show akie B6 S1 Y8 at right
with dissolve
akie "Je n’imaginais pas Ran comme ça !"
hide akie
with dissolve
show ran B2 S1 Y2 at right
with dissolve
ran "Voilà ton uniforme, le vrai cette fois-ci."
show ezo B4 S2 Y4 at left, xflip
with dissolve
ezo "Oh… Euh… désolé."
hide ran
with dissolve
show clateau B1 S1 Y2 at right
with dissolve
clateau "Ahahah… ce n’est rien…"
#  TODONE : Mettre son habit de serveuse à Ezo
# fondu en noir
scene bg black
with dissolve
show ezo Se
scene bg salle
with dissolve
"Le malentendu dissipé, Ezo fut accompagnée par Sei et Akié pour aller en salle. La salle du restaurant était plongée dans une ambiance un peu tamisée, et calme."
"Son style second empire en plein milieu de la capitale nipponne l’avait rapidement fait connaître de la bourgeoise locale."
"Après plusieurs décennies de fermeture du pays, nombreux étaient ceux qui venaient ici pour goûter à leur morceau « d’occident »."
"Et ce, sans pour autant effectuer le long, coûteux, et dangereux voyage,jusqu’à Londres ou Paris, qui était, lui, réservé aux plus riches, ou tout du moins, aux plus aventureux."
"Ezo, qui ne savait pas trop quoi faire, commença par prendre les plats que donnait Yoshino pour les transférer à Sei et Akié. Elle fut assez étonnée par l’habileté de ses camarades. Alors qu’Ezo avait du mal à maintenir les plats dans les faire tomber, Akié, et même Sei, arrivaient à en prendre plusieurs à la fois et à les maintenir en équilibre."
show ezo B4 S3 Y2 at left, xflip
with dissolve
ezo "Impressionnant…"
show sei B1 S1 Y1 at right
with dissolve
sei "C’est une question d’habitude. Tu t’y feras vite."
hide sei
with dissolve
show akie B3 S1 Y4 at right
with dissolve
akie "Mais oui, je suis sûr que t’y t’en sortira. Et surtout, le service est une chose, mais il y a plus important !"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Plus important ?"
show akie B2 S1 Y2 at right
with dissolve
akie "L’accueil des clients !"
hide ezo
with dissolve
hide akie
with dissolve
"Pour illustrer son propos, Akié sautilla vers des clients qui venaient d’arriver dans la salle ? Après une brève courbette, elle leur souhaita la bienvenue, et les guida vers une bonne table. Une fois assis, elle prit leur commande et leur promit de faire au plus vite."
show akie B1 S1 Y4 at right
with dissolve
akie "Et voilà ! Allez, à toi, maintenant !"
"Akié poussa Ezo vers un autre client qui venait d’arriver. Surprise, Ezo n’était pas préparée et se mit à bafouiller."
show ezo B3 S3 Y1 R3 at left, xflip
with dissolve
ezo "Ah… B-Bonjour ! Bienvenue chez nous."
hide ezo
with dissolve
hide akie
with dissolve
"Ezo était toute tendue, et avait du mal à parler. Elle marchait vite et perdait les clients dans la salle. Quand elle faisait s’assoir les clients, elle était brusque et les malmenait un peu."
"Mais la rudesse avec laquelle ils étaient traités ne sembla pas provoquer de remontrance particulière de la part des clients."
"Certains chuchotaient même en se demandant si c’était un nouveau service. Yoshino, depuis le passe-plat, regardait la scène."
scene bg cuisine
with dissolve
show yoshino B5 S2 Y6 at right
with dissolve
yoshino "Bah tiens, manquerait plus que ça plaise, se faire maltraiter…"
show clateau B1 S3 Y4 at left, xflip
with dissolve
clateau "Il y aurait peut-être un concept à lancer là-dessus…"
show yoshino B8 Y5 at right
with dissolve
yoshino "Certainement pas ! Au travail !"
hide clateau
with dissolve
hide yoshino
with dissolve
"De leur côté, Sei et Akié firent cesser l’accueil à Ezo pour arrêter le massacre."
show akie B3 S2 Y4 Go at right
with dissolve
akie "Ah… C’est… c’est original…"
hide akie
with dissolve
show sei B3 S2 Y1 Go at right
with dissolve
sei "On sent que tu fais des efforts, en tout cas."
show ezo B4 S2 Y2 at left, xflip
with dissolve
ezo "C’est… pas facile."
hide sei
with dissolve
show akie B1 S1 Y2 at right
with dissolve
akie "Tu sais, l’important, c’est d’être détendue, d’être soi-même lorsqu’on sert les clients."
hide akie
with dissolve
show sei B2 S1 Y1 at right
with dissolve
sei "Servir, c’est un art tu sais. Reconnaitre les clients, savoir évaluer ce qu’il veulent, doser les mots… c’est comme une stratégie nouvelle pour chaque client."
hide sei
with dissolve
# TODONE : “Une stratégie ?” =point Sei/ “Être soi-même ?”=point Akié
menu:
    " Une stratégie ? Je crois que je vois quoi faire !":
        show ezo B2 S1 Y2 at left, xflip
        with dissolve
        ezo "Une stratégie ? Je crois que je vois quoi faire !"
        $relation_sei += 1
    " Être soi-même ? Je vais essayer !":
        show ezo B2 S1 Y2 at left, xflip
        with dissolve
        ezo "Être soi-même ? Je vais essayer !"
        $relation_akie += 1
hide ezo
with dissolve
"Ezo reparti motivée vers les clients qui arrivaient. Cette fois-ci, elle se mit au garde à vous, droite comme un i, et salua les clients."
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "Bienvenue ici, chef ! Veuillez me laisser vous conduire à votre siège, chef !"
hide ezo
with dissolve
"Elle marcha au pas jusqu’à une table, fit s’assoir les clients. Puis se remit droite en bout de table, toujours au garde-à-vous."
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "Prête à recevoir vos ordres, chef ! Quelle est votre commande ?"
"Les clients désabusés répondirent quelque chose d’évasif, et Ezo revint vers Akié et Sei, contente de sa performance."
show ezo B2 S3 Y2 at left, xflip
with dissolve
ezo "Alors ?"
show akie B2 S2 Y4 Go at right
with dissolve
akie "Euh…"
hide akie
with dissolve
show sei B2 S2 Y1 at right
with dissolve
sei "En tout cas tu as été bien organisée…"
hide akie
with dissolve
hide sei
with dissolve
scene bg cuisine
with dissolve
"Depuis les cuisines, Yoshino qui s’inquiétait avait jeté un coup d’œil en salle, et soupirait sur le désastre."
show yoshino B5 S2 Y6 at right
with dissolve
yoshino "Il y a du travail à faire…"
show clateau B2 S3 Y1 at left, xflip
with dissolve
clateau "Oh, c’est intéressant ! Je dois le noter, je suis sûr qu’il y a quelque chose qui pourrait devenir populaire !"
show yoshino B8 Y5 at right
with dissolve
yoshino "Arrête ça ! Retourne bosser !"
hide yoshino
with dissolve
hide clateau
with dissolve
scene bg salle
with dissolve
"Lorsque le midi arriva, le nombre de client augmenta drastiquement. La pression montait tant sur les serveuses que sur les cuisines."
"Pour préserver la réputation du restaurant, Akié et Sei avaient éloigné Ezo de l’accueil des clients pour la mettre au service en table, ou au débarrassage des tables que les clients venaient de quitter pour les rendre à nouveau présentable pour les prochains clients."
"Ezo ne savait plus où donner de la tête dans ce ballet infini de plat et de client qui allaient de venaient dans la salle. Yoshino, qui menait d’une main de fer le restaurant, ne manquait pas de recadrer le personnel quand celui-ci se relâchait."
"La plupart du temps, c’était Ran qui en faisait les frais, puisqu’elle avait cette fâcheuse habitude de dormir debout pendant son service."
"Mais cela arrivait aussi que ce soit Sei, trop maladroite, ou Akié, trop familière avec un client qui se prenaient une remontrance. Parfois même, c’était Clateau qui se faisait sermonner."
show ezo B5 S1 Y8 at left, xflip
with dissolve
ezo "Elle est pire qu’un instructeur militaire !"
show akie B1 S1 Y2 at right
with dissolve
akie "Yoshino est strict, mais c’est aussi grâce à elle que le restaurant est aussi bien géré !"
hide akie
with dissolve
hide ezo
with dissolve
"Une fois le gros des clients passés, Yoshino leur dit qu’elles pouvaient prendre leur pause. Comme des clients arrivaient encore, elles la prirent à tour de rôle, et la première fut Sei. Ezo se retrouva seule à servir avec Akié."
show akie B2 S1 Y4 at right
with dissolve
akie "Une fois midi passé, on peut déjà souffler un peu !"
show ezo B1 S2 Y1 at left, xflip
with dissolve
ezo "Oui, mais on est plus que deux, donc ça revient un peu au même…"
hide akie
with dissolve
hide ezo
with dissolve
"Ezo débarrassait une table avec Akié, quand elle vit une main baladeuse d’un client se rapprocher des fesses de cette dernière. Ezo la saisit brusquement."
# TODONE “Monsieur…”=point Akié/  “Ezo s’empara”=moins un point Akié
menu:
    " Monsieur… nous ne sommes pas ce genre d’établissement, veuillez sortir…":
        show ezo B4 S2 Y3 Go at left, xflip
        with dissolve
        ezo "Monsieur… nous ne sommes pas ce genre d’établissement, veuillez sortir…"
        "Ezo fit une clef de bras à l’homme et le ramena à la sortie du restaurant, dans le calme."
        show akie B1 S1 Y4 at right
        with dissolve
        akie "Oh, merci Ezo. Tu as bien géré ce type."
        $relation_akie += 1
    " Qu’est-ce que tu fous, connard ?":
        show ezo B8 Y5 at left, xflip
        with dissolve
        ezo "Qu’est-ce que tu fous, connard ?"
        "Ezo s’empara du bras du malotru, et le propulsa dans la salle. Akié poussa un petit cri."
        show akie B4 S2 Y4 at right
        with dissolve
        akie "Merci… mais je ne sais pas si c’était nécessaire d’en faire autant…"
        $relation_akie -= 1
hide akie
with dissolve
hide ezo
with dissolve
"Malgré cet incident, le calme revint dans la salle. Avec sa bonne humeur communicative, Akié pu facilement remettre l’ambiance."
"Ce fut finalement à Akié de prendre sa pause, quand Sei revint de la sienne."
show sei B1 S1 Y1 at right
with dissolve
sei "Me revoilà ! Tout s’est bien passée en mon absence ?"
show ezo B1 S3 Y4 at left, xflip
with dissolve
ezo "Juste un petit « incident » mais rien de grave !"
show sei B1 S1 Y3 at right
with dissolve
sei "Je suppose que tu t’en es occupé ?"
show ezo B2 S3 Y1 at left, xflip
with dissolve
ezo "On peut dire ça…"
hide akie
with dissolve
hide sei
with dissolve
hide ezo
with dissolve
"Sei était plutôt calme et gentille, et aussi assez maladroite. Ezo essayait de rattraper les assiettes qu’elle faisait tomber, mais chaque jour c’en était au moins une qui finissait en morceau par terre."
"Le plus gros des clients étant déjà passé, cette après-midi à deux fut assez facile, jusqu’à ce qu’un client étranger arrive."
"Le restaurant de Clateau, en plus d’être réputé parmi les Tokyoïtes, les expatriés occidentaux et les marchands de passages aimaient aussi y aller."
show sei B2 S2 Y1 Go at right
with dissolve
sei "E-Ezo, ce monsieur essaye de demander quelque chose, mais je ne comprends pas."
hide sei
with dissolve
# TODONE “Gérer le client seule.”=moins un point Sei/ “Aider Sei à lui parler.” = point Sei
menu:
    " Gérer le client seule.":
        "Ezo s’approcha pour voir un gros bonhomme en costume. Elle essaya de lui parler, et se rendit compte que ce devait être un américain."
        "Il y en avait pas mal ces temps-ci, venu pour affaires. Quand ils venaient au restaurant, ils essayaient tous de parler en français -parfois approximatif- pour se donner des airs bourgeois. Ezo commença à lui parler et prit sa commande."
        "La froideur d’Ezo calma l’enthousiasme du client et celui-ci s’assit sur sa chaise sans faire de bruit jusqu’à la fin de son repas."
        $relation_sei -= 1
    " Aider Sei à lui parler.":
        "Ezo s’approcha pour voir un gros bonhomme en costume. Elle essaya de lui parler, et se rendit compte que ce devait être un américain."
        "Il y en avait pas mal ces temps-ci, venu pour affaires. Quand ils venaient au restaurant, ils essayaient tous de parler en français -parfois approximatif- pour se donner des airs bourgeois."
        "Ezo souffla à Sei quelques mots à lui dire, et elle réussit à prendre sa commande dans une langue ou elle n’en touchait pas une. Le client fut particulièrement satisfait de l’effort de Sei et resta enjoué tout le long de son repas."
        $relation_sei += 1
show sei B1 S1 Y1 at right
with dissolve
sei "Merci de ton aide. D’ailleurs, tu sais parler d’autres langues ?"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Comme j’ai pas mal voyagé, j’ai quelques notions dans plusieurs d’entre elles, mais c’est tout."
show sei B1 S1 Y3 at right
with dissolve
sei "C’est vraiment super ça !"
show ezo B4 S3 Y1 at left, xflip
with dissolve
ezo "…"
hide ezo
with dissolve
hide sei
with dissolve
"Ezo ne répondit pas, légèrement gênée. Elle avait encore du mal à évoquer son passé aussi facilement. Akié finit par revenir en salle, et ce fut le tour d’Ezo de prendre sa pause."
scene bg bar
with dissolve
"La pause des serveuses était prise au bar, avec Ran. Clateau leur préparait un sandwich, et un café maison."
show ran B1 S1 Y4 at right
with dissolve
ran "Alors, pas trop dur, cette première journée ?"
show ezo B1 S3 Y1 at left, xflip
with dissolve
ezo "Disons qu’il se passe beaucoup de choses…"
show ran B1 S1 Y2 at right
with dissolve
ran "Prenez donc du repos pendant votre pause."
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "D’ailleurs, tu la prends quand ta pause, toi ?"
hide ran
with dissolve
show tsugumi B1 S1 Y1 at right
with dissolve
tsugumi "Elle est toujours en pause, elle !"
"Tsugumi venait de faire irruption dans le bar, souriant de toutes ses dents."
show ezo B1 S3 Y4 at left, xflip
with dissolve
ezo "Ah, te revoilà, toi. T’es pas au travail ?"
show tsugumi B1 S1 Y1 at right
with dissolve
tsugumi "J’ai terminé plus tôt aujourd’hui !"
show ezo B1 S3 Y4 at left, xflip
with dissolve
ezo "Tu peux pas vraiment critiquer Ran, alors !"
show tsugumi B1 S1 Y2 at right
with dissolve
tsugumi "Ahaha, c’est pas faux ! Et toi, tu travailles au bar maintenant ?"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Non, comme serveuse en salle."
show tsugumi B2 S1 Y1 at right
with dissolve
tsugumi "Serveuse en salle ? Bouahaha, rien que de t’imaginer servir les clients ça me fend la poire !"
show ezo B5 S1 Y2 at left, xflip
with dissolve
ezo "Hé !"
hide tsugumi
with dissolve
show ran B1 S1 Y1 at right
with dissolve
ran "Voyons, mademoiselle Tsugumi ! Je suis sûr que mademoiselle Ezo fait de son mieux…"
show ezo B4 S2 Y6 at left, xflip
with dissolve
ezo "Comment je dois le prendre ?"
show ezo B2 S3 Y1 at left, xflip
with dissolve
ezo "Bon, je vais retourner bosser, moi…"
hide ezo
with dissolve
hide ran
with dissolve
scene bg salle
with dissolve
"Ezo retourna en salle. L’heure du dîner arrivait à grand pas et déjà, comme pour le midi, les clients commençaient à se presser dans la salle."
"Ezo remarqua à quel point chacune de ses deux collègues étaient bien adaptées à leur travail."
"Akié, toujours souriante, toujours joyeuse, sautillait de table en table pour prendre les commandes, accueillait les clients et servait les plats."
"Son beau sourire faisait mieux passer l’attente qui s’accumulait lors des grosses affluences. De son coté, Sei connaissait les bons mots pour conseiller les gens : elle voyait d’un coup d’œil de quel milieu ils venaient, et ce qui leur plairait."
"Elle était aussi très douée en math et d’ailleurs Akié venait souvent lui demander de l’aide pour calculer les additions des clients. Elle était dotée d’un grand professionnalisme et était droite dans ses bottes."
"Ezo se fit la réflexion que, elle aussi, elle en avait, des bottes. Bon, des bottes de militaires, mais c’était des bottes quand même."
"La soirée fut ardue, bien que plus simple que le midi grâce à l’expérience qu’elle avait déjà acquise. Ezo avait encore du mal à bien parler aux clients, mais elle arrivait maintenant à prendre les commandes et à servir sans trop de problèmes."
"Une fois les derniers clients partis, les trois filles se posèrent sur leurs chaises, exténués."
"Ran apparu dans la salle, portant un plateau chargé de pintes de bières et quelques encas."
show ran B1 S1 Y4 at right
with dissolve
ran "Après l’effort, le réconfort ! C’est l’heure de se détendre."
hide ran
with dissolve
"Immédiatement après, l’ombre de Yoshino fondit derrière elle, et elle se prit une petite tape derrière la tête de la part de cette dernière."
show yoshino B2 S1 Y4 at right
with dissolve
yoshino "Tu crois pas que toi, tu te détends déjà suffisamment pendant la journée ?"
show ran B6 S1 Y6 at left, xflip
with dissolve
ran "Mais euh ! Mademoiselle Yoshino, je voulais aussi récompenser les efforts de l’équipe de service, qui s’est bien démenée aujourd’hui."
hide yoshino
with dissolve
hide ran
with dissolve
"Tout le monde rigola et on commença à boire."
"C’était ainsi que se finissait beaucoup de journée au restaurant, toutes les filles se rassemblaient pour discuter de ce qui s’était passée pendant leur service. Puis, chacun rentrait de son côté."
scene bg cuisine
with dissolve
"Ezo aperçue Clateau, qui l’attendait près des escaliers, alors qu’elle allait retourner dans sa chambre."
show clateau B1 S1 Y4 at right
with dissolve
clateau "Alors, comment s’est passé ta journée ?"
show ezo B2 S3 Y4 at left, xflip
with dissolve
ezo "On peut dire que ça s’est bien passé."
show clateau B1 S1 Y1 at right
with dissolve
clateau "Tu t’habitues au métier ?"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "C’est encore un peu dur, mais ça va aller."
show clateau B1 S1 Y4 at right
with dissolve
clateau "Bien. Si jamais tu as besoin de quoi que ce soit, dit-le moi."
show ezo B1 S3 Y4 at left, xflip
with dissolve
ezo "Merci, mais je suis plutôt bien entourée."
scene bg grenier
with dissolve
"Ezo se retrouva dans sa chambre. Le jour commençait à tomber et la pièce mal éclairée se retrouvait dans la pénombre."
show ezo B4 S3 Y1 at left, xflip
with dissolve
ezo "Je n’ai pas sommeil…"
# TODONE “Je dois dormir”=point Sei/ “Bah, pas la peine”= point Akié
menu:
    " Je dois dormir quand même, sinon demain je n’aurais pas les yeux en face des trous.":
        show ezo B2 S3 Y2 at left, xflip
        with dissolve
        ezo "Je dois dormir quand même, sinon demain je n’aurais pas les yeux en face des trous."
        $relation_sei += 1
        # Si “se coucher”
        scene bg grenier
        with dissolve
        "Ezo partit se coucher, et finalement elle ne mit pas longtemps avant de s’endormir. Mais elle se réveilla bientôt."
        show ezo B6 S2 Y3 at left, xflip
        with dissolve
        ezo "Puisque je suis levée, autant descendre…"
        hide ezo
        with dissolve
    " Bah, pas la peine de se forcer. Je vais aller faire un tour.":
        show ezo B2 S3 Y2 at left, xflip
        with dissolve
        ezo "Bah, pas la peine de se forcer. Je vais aller faire un tour."
        $relation_akie += 1
        # TODONE Si “aller faire un tour”
        scene bg rue
        with dissolve
        "Ezo sorti du restaurant. La nuit, c’était beaucoup plus calme qu’en journée."
        "Ezo fit quelques pas dans la rue : Elle aimait bien l’architecture japonaise. Malgré son statut d’enfant-soldat et de militaire, elle était restée assez curieuse et chaque escale qu’elle faisait était l’occasion de découvrir de nouveaux mondes."
        "La rue, un peu cossue, était constituée de maison plutôt traditionnelle -le restaurant à l’occidentale faisait d’ailleurs un peu tâche- et elle aimait regarder à travers les grilles les jardins raffinées,"
        "et voir les ombres des occupants qu’on devinait derrière une porte coulissante mal fermée."
        "Elle fit le tour du restaurant, et quand elle prit la petite ruelle sur le côté, elle y vit Akié. Elle portait un gros sac en papier, et quelques gamelles en bois qu’elle venait de laver."
        "Et autour d’Akié, encore une bande de petites frappes autour d’elle. Ceux-ci semblaient passablement éméchées."
        show ezo B4 S2 Y6 at left, xflip
        with dissolve
        ezo "Ma parole elle les attires…"
        "Ezo soupira, et vint à la rencontre des loubards. Elle savait comment s’y prendre, et n’engagea même pas la conversation. Après deux mandales et un croche-pied, ils prirent la fuite."
        show ezo B4 S2 Y6 at left, xflip
        with dissolve
        ezo "Merde, c’était presque trop facile."
        show akie B6 S2 Y2 at right
        with dissolve
        akie "Oh, merci Ezo ! Cette bande de lourds ne voulait plus me lâcher."
        show ezo B1 S3 Y2 at left, xflip
        with dissolve
        ezo "De rien… mais qu’est-ce que tu fais dehors à cette heure ?"
        show akie B1 S1 Y4 at right
        with dissolve
        akie "Je venais récupérer la nourriture que le restaurant allait jeter, pour la donner aux animaux que je recueille !"
        show ezo B2 S1 Y3 at left, xflip
        with dissolve
        ezo "Heureusement que j’étais là… Tu ne pouvais pas le récupérer plus tôt ?"
        show akie B1 S1 Y4 at right
        with dissolve
        akie "J’avais oublié…"
        hide akie
        with dissolve
        hide ezo
        with dissolve
        "Ezo et Akié discutèrent encore un peu, mais Ezo pressa cette dernière de se dépêcher de rentrer chez elle avant que la nuit ne tombe totalement et qu’elle se fasse de nouveau embêter."
        scene bg grenier
        with dissolve
        "Ezo grommela qu’elle ne pouvait décidément pas se balader tranquille et alla se coucher. Le lendemain, elle se réveilla assez tôt malgré s’être couché si tard."
# fondu en noir
show bg Black
with dissolve
scene bg cuisine
with dissolve
"Dans la cuisine encore vide, elle entendit un bruit dans la remise."
show ezo B1 S1 Y1 at left, xflip
with dissolve
ezo "Tiens ? on essayera de nous piquer nos réserves ?"
hide ezo
with dissolve
"Elle fit irruption dans la réserve. Mais il n’y avait que Sei, en train de prendre des sacs."
show sei B1 S1 Y3 at right
with dissolve
sei "Ezo ? Tu es déjà levée ?"
show ezo B2 S3 Y1 at left, xflip
with dissolve
ezo "Bah oui… et toi qu’est-ce que tu fais ?"
show sei B1 S1 Y1 at right
with dissolve
sei "Je devais aller faire des courses, donc je suis venu plus tôt, mais j’ai du mal à tout ramener, les livreurs ont tout déposés devant l’entrée, il y en a beaucoup."
"Ezo passa la tête pour voir tout un tas de caisses empilées dans la ruelle."
show ezo B1 S3 Y1 at left, xflip
with dissolve
ezo "C’est toi qui t’occupes de tout ça ?"
show sei B2 S1 Y1 at right
with dissolve
sei "Oui, si Yoshino s’occupe des cuisines, moi je m’occupe souvent des comptes, notamment. Et il m’arrive de gérer ça quand Clateau est occupé."
show ezo B3 S3 Y4 at left, xflip
with dissolve
ezo "Je ne savais pas que tu en faisais autant ! Moi qui pensais que tu étais juste un personnage cliché de fille maladroite…"
show sei B1 S3 Y3 at right
with dissolve
sei "Hé ! C’est pas gentil de dire ça !"
show ezo B2 S3 Y2 at left, xflip
with dissolve
ezo "Mais je suis vraiment impressionnée par ce que tu fais !"
show sei B1 S1 Y1 at right
with dissolve
sei "…"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Je vais t’aider à décharger les caisses restantes ! Je ne suis pas aussi douée pour compter et faire des commandes, mais pour la force brute, laisse-moi m’en occuper !"
hide ezo
with dissolve
hide sei
with dissolve
"Ezo aida Sei à s’occuper des caisses de vivres. Elle avait déjà fait ça tellement de fois qu’elle ne le comptait même plus."
"À chaque fois qu’elle faisait escale quelque part, il fallait charger de nouvelles provisions, des munitions, des armes… Ce n’était pas quelques caisses qui allaient lui faire peur."
"Une fois cela fait, il était déjà l’heure d’aller travailler."
# Fin des Si
scene bg salle
with dissolve
"Le travail repris de plus belle, et cette fois-ci, Ezo décida d’aller au service des clients. Dans un effort surhumain, elle réussis à faire une phrase complète comprenant toutes les formules de politesse."
show akie B2 S1 Y4 at right
with dissolve
akie "Oh, Ezo, c’était parfait ! Tu as réussi ! Bon, on voit que tu es exténué, tu peux retourner au service maintenant, je prends la suite."
hide akie
with dissolve
show sei B1 S1 Y2 at right
with dissolve
sei "Oui, on a fait un progrès, on verra pour le keigo une autre fois…"
hide sei
with dissolve
"Ezo sautillait dans la salle suite à sa « victoire ». C’était bien la première fois qu’elle réussissait à être polie."
show yoshino B5 S1 Y1 at right
with dissolve
yoshino "Hé, Ezo ! Au lieu de sauter partout comme une débile, va plutôt me chercher de la farine en réserve, je suis occupée et Clateau aussi."
hide yoshino
with dissolve
scene bg cuisine
with dissolve
"Ezo s’arrêta net en faisant la moue. Elle passa dans la réserve, prit son sac, et remarqua que la porte vers l’extérieur était entrouverte. Elle se mit le menton entre le pouce et l’index et fit une tête qui lui donnait l’air de réfléchir."
scene bg rue
with dissolve
show ezo B4 S1 Y1 at left, xflip
with dissolve
ezo "Voyons, Akié aussi était parti prendre un truc deux minutes avant, alors…"
hide ezo
with dissolve
"En sortant, elle vit ce qu’elle s’attendait à voir : Akié nourrissant les animaux du quartier."
show ezo B5 S1 Y2 at left, xflip
with dissolve
ezo "Ah ! je m’en doutais !"
show akie B5 S1 Y7 at right
with dissolve
akie "E-Ezo ? Je croyais que tu étais en salle à t’occuper de ton progrès…"
show ezo B5 S1 Y2 at left, xflip
with dissolve
ezo "Yoshino m’a envoyé chercher de la farine. Qu’est-ce que tu fais ?"
show akie B1 S1 Y1 at right
with dissolve
akie "Bah…"
hide ezo
with dissolve
hide akie
with dissolve
# TODONE : “Mais Yoshino avait” = moins un point Akié/ “Ne fais pas trop”= point Akié
menu:
    " Mais Yoshino avait dit de ne pas piquer dans le garde-manger !":
        $relation_akie -= 1
        show ezo B5 S1 Y2 at left, xflip
        with dissolve
        ezo "Mais Yoshino avait dit de ne pas piquer dans le garde-manger !"
        hide ezo
        with dissolve
        "En s’agitant, Ezo fit rappliquer Yoshino !"
        show akie B4 S2 Y8 at right
        with dissolve
        akie "Ah ! Yoshino ! Je peux t’expliquer"
        "Yoshino ne jetta qu’un regard en coin à Akié."
        show yoshino B4 S1 Y1 at left, xflip
        with dissolve
        yoshino "Et tu as ce qu’il faut pour les chats ?"
        show akie B2 S2 Y1 at right
        with dissolve
        akie "Hein ? Oui, j’ai ce qu’il me faut…"
        show yoshino B4 S1 Y2 at left, xflip
        with dissolve
        yoshino "Bon… mais que je ne t’y reprenne plus."
        hide akie
        with dissolve
        hide yoshino
        with dissolve
        "Ezo et Akié restèrent interdite devant la réaction de Yoshino, qui retourna en cuisine juste après."
        show ezo B1 S3 Y2 at left, xflip
        with dissolve
        ezo "Bah tiens, ça alors !"
        show akie B2 S1 Y4 at right
        with dissolve
        akie "Yoshino est plutôt gentille en fait, tu sais !"
    " Ne fais pas trop de bruit, tu va attirer Yoshino":
        $relation_akie += 1
        show ezo B1 S3 Y2 at left, xflip
        with dissolve
        ezo "Ne fais pas trop de bruit, tu vas attirer Yoshino."
        hide ezo
        with dissolve
        "Ezo sourit à Akié, qui lui rendit la pareil."
        "Ezo, sans trop de bruit, passa à Akié un morceau de pain qu’elle gardait dans sa poche."
        "Elle repartir ensuite, à pas feutrés. Pendant qu’Ezo donna le sac de farine à Yoshino, Akié retourna discrètement en salle."
# Fondu en noir
hide ezo
with dissolve
hide yoshino
with dissolve
scene bg salle
with dissolve
"La journée fut plus calme que la précédente. Quand vint l’heure de la pause, Akié proposa à Sei et Ezo de la prendre ensemble, après tout la salle était presque vide."
"Sei était posée à l’une des tables du bar et lisait tranquillement un livre en attendant que son café brûlant refroidisse."
# “Tiens, je”= point Sei/ “C’est quoi ?”= moins un point Sei
menu:
    " Tiens, je connais ça, c’est le Manyôshû !":
        show ezo B1 S3 Y4 at left, xflip
        with dissolve
        ezo "Tiens, je connais ça, c’est le Manyôshû !"
        show sei B1 S1 Y1 at right
        with dissolve
        sei "Oh, tu connais ce recueil ? Que c’est étonnant, pour une étrangère."
        "Ezo bomba le torse, fière de sa connaissance."
        show ezo B1 S3 Y2 at left, xflip
        with dissolve
        ezo "Oui, tu sais, quand j’étais à Hokkaidô, les soldats qui m’ont renommé « Ezo » pour mon nationalisme pro-shogun zélé m’on aussi fait découvrir quelques trucs… dont le Manyôshû."
        hide ezo
        with dissolve
        hide sei
        with dissolve
        "Sei, qui restait assez sérieuse, paru s’illuminer tout d’un coup et commença à bombarder Ezo sur sa culture poétique."
    " C’est quoi ?":
        show ezo B1 S3 Y2 at left, xflip
        with dissolve
        ezo "C’est quoi ? Le Manyôshû ?"
        show sei B1 S1 Y3 at right
        with dissolve
        sei "Oh, oui, tu connais ?"
        show ezo B4 S2 Y1 at left, xflip
        with dissolve
        ezo "Moui, mais bon… C’est pas très utile. Je préfère plutôt apprendre à me défendre."
        show sei B4 S2 Y1 at right
        with dissolve
        sei "Je vois…"
hide sei
with dissolve
hide ezo
with dissolve
"Le travail repris ensuite avec l’arrivée des clients pour l’heure du dîner. Tout ce passait plutôt bien, mais de menus problèmes arrivaient de temps en temps : assiettes cassés par Sei, Akié trop « enjouée » avec les clients, ou Ezo pas assez."
"Ce n’était pas de gros incidents, mais cela semblait taper sur les nerfs de Yoshino."
show yoshino B8 Y5 at right
with dissolve
yoshino "Bon, ça suffit vous trois ! Essayez de vous disciplinez un peu ! Surtout vous, Akié et Sei, vous êtes toutes deux pleines d’expériences, ça ne devrait plus arriver !"
show akie B5 S2 Y8 at left, xflip
with dissolve
akie "Je ne le fais pas exprès, et Sei non plus ! Et tu es trop sûr nous, ça nous stress !"
show yoshino B8 Y5 at right
with dissolve
yoshino "Dit que c’est de ma faute aussi ! Vous avez intérêt à vous reprendre !"
hide akie
with dissolve
show sei B1 S2 Y3 Go at left, xflip
with dissolve
sei "Allons, Yoshino…"
show yoshino B8 Y5 at right
with dissolve
yoshino "Ne t’en mêle pas Sei !"
hide sei
with dissolve
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "Euh…"
show yoshino B8 Y5 at right
with dissolve
yoshino "Quoi ?!"
# TODONE “ Lâche-nous un peu !” = point Sei/ “T’es trop strict !” = point Akié
menu:
    " Lâche-nous un peu ! Si tu n’étais pas tout le temps en train de crier, je suis sûr que Sei serait moins stressée !":
        $relation_sei += 1
        show ezo B5 S1 Y1 at left, xflip
        with dissolve
        ezo "Lâche-nous un peu ! Si tu n’étais pas tout le temps en train de crier, je suis sûr que Sei serait moins stressée !"
        show ezo B5 S1 Y1 at left, xflip
        with dissolve
        ezo "La dernière fois, c’est parce que tu l’as interpellé violemment, qu’elle a lâché les assiettes !"
        show yoshino B1 S2 Y1 Go at right
        with dissolve
        yoshino "Oui, bon…"
    " T’es trop strict ! Akié est juste enthousiaste, ça dérange rarement les clients !":
        $relation_akie += 1
        show ezo B5 S1 Y1 at left, xflip
        with dissolve
        ezo "T’es trop strict ! Akié est juste enthousiaste, ça dérange rarement les clients !"
        show yoshino B4 S2 Y2 at right
        with dissolve
        yoshino "Mais quand même…"
hide ezo
with dissolve
hide yoshino
with dissolve
"Yoshino ne s’attendait pas vraiment à ce qu’Ezo prenne la défense de ses camarades avec autant d’entrain, et elle les laissa tranquille."
show sei B2 S1 Y1 at right
with dissolve
sei "Oh, Ezo, c’est la première fois que je vois quelqu’un rembarrer Yoshino !"
hide sei
with dissolve
show akie B2 S1 Y4 at right
with dissolve
akie "Eh bah, ma petite Ezo ! T’es pas grande mais tu sais te défendre !"
show ezo B4 S1 Y4 at left, xflip
with dissolve
ezo "Hmpf, si je vous avais laissé vous faire engueuler, j’aurais été la prochaine sur la liste, alors…"
hide akie
with dissolve
hide ezo
with dissolve
if relation_sei > relation_akie:
    # TODONE : à déclencher Si beaucoup de point Sei
    scene bg bar
    with dissolve
    "Yoshino fut calmée pour la fin de la journée. Après le service, Sei vint voir Ezo."
    show sei B2 S1 Y1 at right
    with dissolve
    sei "Ezo… Je me demandais… tu n’as rien à faire, pour nos prochains jours de repos ?"
    show ezo B1 S3 Y2 at left, xflip
    with dissolve
    ezo "Non, rien."
    show sei B2 S1 Y1 at right
    with dissolve
    sei "Je me disais… tu voudrais venir chez moi ? J’aimerai… que tu me parles un peu de tes voyages."
    show ezo B2 S3 Y4 at left, xflip
    with dissolve
    ezo "Ah ? Pourquoi pas."
    "Sei remis un papier blanc plié en quatre, en expliquant qu’il s’agissait de son adresse, et d’un plan, pour ne pas qu’Ezo se perde."
    "Cette dernière protesta un peu sur ce point, mais elle la remercia et lui promit d’être à l’heure."
    show bg Black
    with dissolve
    jump sei_ch2
else:
    # TODONE : à déclencher Si beaucoup de point Akié
    scene bg bar
    with dissolve
    "Yoshino fut calmée pour la fin de la journée. Après le service, Akié vint voir Ezo."
    show akie B1 S1 Y2 at right
    with dissolve
    akie "Dit, dit, ma petite Ezo ! Tu fais quoi pour notre prochain jour de repos ?"
    show ezo B1 S3 Y2 at left, xflip
    with dissolve
    ezo "Hein ? Bah, rien."
    show akie B1 S1 Y4 at right
    with dissolve
    akie "Tu voudrais bien venir avec moi nourrir les petits animaux ? Il m’a semblé que ça te plaisait, à toi aussi."
    show ezo B2 S3 Y1 at left, xflip
    with dissolve
    ezo "Ah, bah… pourquoi pas…"
    show akie B1 S1 Y4 at right
    with dissolve
    akie "Super ! Je te rejoindrai devant le restaurant alors."
    "Ezo répondit évasivement. Elle avait peu l’habitude de ce genre de sociabilisation."
    show bg Black
    with dissolve
    jump akie_ch2
