label cuisine_ch1:
    pass

show chapter_cuisine_ch1:
    yanchor 0.5 ypos 0.5
    xanchor 0.5 xpos 0.5
with dissolve
$renpy.pause(3, hard='True')

scene bg grenier
with dissolve
"Les premiers rayons du soleil matinal vinrent caresser la joue d’Ezo, recroquevillée sur son lit. Elle passa sa main près de ses yeux comme pour les chasser, et ouvrit les yeux. Il était encore tôt, mais ses habitudes militaires la faisaient se lever aux aurores."
"Elle se roula un peu dans ses draps, ils étaient propres et frais. Cela faisait longtemps qu’elle n’avait pas dormi dans un confort relatif ; les camps militaires sont rarement des sinécures."
hide ezo
with dissolve
ezo "Allez, levons-nous ! Autant garder de bonnes habitudes. Et je ne pense pas que Yoshino me laisse flâner au lit."
"Ezo sortit du lit, puis récupéra ses habits qu’elle avait dispersé la veille dans toute la pièce."
# TODONE : Ezo porte son habit militaire
$ezo_outfit = 'Mi'
show ezo B3 S2 Y4 at left, xflip
with dissolve
ezo "Ouah, si j’étais encore au camp, je me serai tellement fait pourrir pour ça…"
"Elle s’habilla puis descendit en cuisine. Il était encore un peu tôt, et elle était vide."
scene bg cuisine
with dissolve
show ezo B2 S2 Y1 at left, xflip
with dissolve
ezo "Clateau n’est pas encore levé ? Quelle feignasse… … Je commence à avoir faim. Je devrais trouver quelque chose par ici, on est quand même dans un restaurant."
hide ezo
with dissolve
"Ezo fouilla un peu le plan de travail. C’était une belle cuisine, moderne, occidental. Clateau avait dû dépenser cher pour un tel équipement."
"Ezo se fit la réflexion qu’une cuisine moins grande et moins belle aurait tout autant suffit à faire cuire des aliments. Le feu reste le feu, peu importe qu’il soit dans une belle cuisine ou dans un vieux four en terre."
"Au-dessus des lourds tuyaux qui évacuaient les fumées se trouvaient des casseroles, reluisantes avec leur belle couleur cuivrée. Elles étaient toutes alignées, de la plus petite à la plus grande. Leur éclat orangé rappelait quelqu’un à Ezo…"
"En dessous, c’était des ustensiles en tout genre qui garnissaient les plans de travails. Ezo s’arrêta net en voyant les couteaux : ce n’était pas des couteaux occidentaux de basse facture, mais d’authentiques couteaux de maitre."
"Leurs lames effilées renvoyaient dans la pièce sombre un éclat puissant. Cela avait dû coûter bien cher, Ezo se demandait comment Clateau avait fait pour se payer tout ça."
"Tout au bout du présentoir, Ezo fini par y trouver une panière de pain. Quand elle les prit, elle remarqua qu’ils étaient tous un peu rassis."
show ezo B2 S3 Y2 at left, xflip
with dissolve
ezo "Certainement du pain oublié la veille. Tss, ce restaurant devrait apprendre à économiser un peu."
hide ezo
with dissolve
"Ezo prit quelques morceaux qu’elle mâchouilla en marchant dans la cuisine. Quand elle arriva près de la porte, celle-ci s’ouvrit brusquement et Ezo sursauta."
show ezo B1 S3 Y8 at left, xflip
with dissolve
ezo "Qu... Qui… qui va-là ?"
show yoshino B1 S3 Y1 Go at right
with dissolve
yoshino "C’est moi, idiote."
show ezo B2 S3 Y2 at left, xflip
with dissolve
ezo "Oh, salut."
show yoshino B1 S2 Y1 Go at right
with dissolve
yoshino "j’peux savoir ce que t’es en train de faire ?"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Bah j’attends les autres, je sais pas où est Clateau…"
show yoshino B1 S2 Y4 Go at right
with dissolve
yoshino "Non, je veux dire… Qu’est-ce que t’es en train de manger ?"
"Ezo avala la bouchée de pain qu’elle avait dans la bouche."
show ezo B2 S3 Y3 at left, xflip
with dissolve
ezo "Du pain."
show yoshino B3 S2 Y6 at right
with dissolve
yoshino "Oui. Mais non. Tu m’expliques pourquoi tu manges le pain rassis de la semaine dernière que j’avais l’intention de donner à Akié ?"
show ezo B2 S2 Y7 eH at left, xflip
with dissolve
ezo "Le pain de la semaine dernière…"
"Yoshino se passa la main dans les cheveux."
show yoshino B2 S3 Y4 -Go at right
with dissolve
yoshino "T’es quoi, un vrai chat errant ? D’ailleurs, qu’est-ce que tu fais là ?"
"Ezo mit ses deux mains sur les hanches, et bomba le torse."
show ezo B2 S1 Y3 -eH at left, xflip
with dissolve
ezo "À partir d’aujourd’hui, je vous aiderai en cuisine."
"Yoshino paru fortement dépitée suite à cette annonce."
show yoshino B4 S1 Y1 at right
with dissolve
yoshino "Attends, tu es bien sûre de toi ? T’as bien réfléchie à la question ? Et Clateau, qu’en penses-t-il…"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Il est d’accord, je lui en ai parlé hier."
hide yoshino
with dissolve
hide ezo
with dissolve
"Au même moment, la porte de la réserve de la cuisine s’ouvrit, laissant apparaitre Clateau."
show clateau B1 S3 Y1 at right
with dissolve
clateau "Ah ! Tiens, vous êtes là, vous deux."
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "Ah, qu’est-ce que tu foutais là ?"
show clateau B2 S3 Y1 at right
with dissolve
clateau "Je faisais l’inventaire de nos stocks pour la journée."
"Tout en parlant, Clateau mastiquait lui aussi quelque chose."
hide clateau
with dissolve
show yoshino B1 S3 Y1 at right
with dissolve
yoshino "Ne me dit pas que t’as aussi pris du pain rassis !?"
hide ezo
with dissolve
show clateau B5 S1 Y2 at left, xflip
with dissolve
clateau "Ah, euh…"
show clateau B2 S1 Y1 at left, xflip
with dissolve
clateau "Si."
hide clateau
with dissolve
hide yoshino
with dissolve
"Après un long soupir, Yoshino entra dans la cuisine sans rien dire et commença son travail."
"Peu après, les autres filles arrivèrent à la suite. Elles se réunirent dans la cuisine pour écouter l’annonce de Clateau avant de commencer la journée."
show clateau B1 S1 Y1 at right
with dissolve
clateau "Ezo va travailler en cuisine avec moi et Yoshino à partir de maintenant."
show akie B4 S1 Y2 at left, xflip
with dissolve
akie "Oh, quel dommage !"
hide akie
with dissolve
hide clateau
with dissolve
show yoshino B3 S1 Y4 at right
with dissolve
yoshino "Oui, quel dommage…"
show ezo B5 S1 Y2 at left, xflip
with dissolve
ezo "Hé !"
hide yoshino
with dissolve
show sei B1 S1 Y1 at right
with dissolve
sei "Mais je suis sûr que tu t’en tireras bien, Ezo !"
show ezo B2 S3 Y2 at left, xflip
with dissolve
ezo "Merci."
hide sei
with dissolve
show clateau B2 S1 Y4 at right
with dissolve
clateau "Allez, tout le monde au travail !"
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "Oui chef !"
hide clateau
with dissolve
hide ezo
with dissolve
"Akié partie en sautillant vers la salle, suivit par Sei. Ran traîna ses pieds vers le bar."
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "Je suis bien motivée ! D’abord…"
show yoshino B1 S1 Y3 at right
with dissolve
yoshino "D’abord tu vas enfiler ça."
"Yoshino lui tendit une tunique blanche de cuisiner."
show ezo B4 S2 Y2 at left, xflip
with dissolve
ezo "Qu’est-ce que c’est ?"
show yoshino B8 S1 Y1 at right
with dissolve
yoshino "Ta tenue de travail ! Tu ne pensais quand même pas qu’on bossait en cuisine avec des habits aussi crades ?"
show ezo B4 S1 Y2 at left, xflip
with dissolve
ezo "Ils sont pas crades, c’est mes habits fétiches, je les porte avec moi depuis des mois !"
show yoshino B5 S1 Y1 eH at right
with dissolve
yoshino "Raison de plus pour les retirer."
"Yoshino prit un ton plus strict, ses yeux froncés distillant l’autorité."
show ezo B4 S2 Y2 at left, xflip
with dissolve
ezo "Bon, d’accord…"
"Ezo attrapa la tunique et commença à se déshabiller."
show yoshino B1 S1 Y1 -eH at right
with dissolve
yoshino " Attends !"
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "Quoi encore ?"
hide ezo
with dissolve
"Yoshino se tourna vers Clateau."
show yoshino B5 S1 Y1 at right
with dissolve
yoshino "Euh, fiche-moi le camp ? Elle va se changer !"
hide yoshino
with dissolve
"Yoshino attrapa Clateau par la manche et le fit sortir. Celui-ci se retrouva dans la salle. Il attendit quelques minutes, jusqu’à ce que la main de Yoshino repasse les portes battantes pour le ramener en cuisine, sous les regards amusés de Ran et Sei."
# TODONE Ezo en cuistote
$ezo_outfit = 'Cui'
show ezo B1 S3 Y4 at left, xflip
with dissolve
ezo "Me voilà prête ! Je peux commencer à cuisiner."
"Ezo s’empara d’un couteau qu’elle regarda avec un sérieux à toute épreuve."
show yoshino B3 S1 Y2 at right
with dissolve
yoshino "Oui, commencer à cuisiner…"
hide ezo
with dissolve
"Elle retroussa ses manches, et s’empara d’une grosse cagette de patates. Elle poussa du pied un petit tabouret près de la réserve et posa la cagette à côté."
show yoshino B5 S1 Y1 at right
with dissolve
yoshino "Voilà, corvée de patates, pour commencer ! En tant qu’ancienne militaire, tu dois t’y connaitre, non ?"
hide yoshino
with dissolve
"Ezo paru un instant contrarié par la cagette, mais elle se retroussa les manches elle aussi, s’assit sur le tabouret, et saisit une patate qu’elle commença à éplucher. Yoshino semblait satisfaite."
"Ezo continua sa corvée de patates presque toute la matinée. Elle était habituée à éplucher des tubercules."
"Dans l’armée, elle l’avait fait maint et maint fois. Mais là, elle peinait. Il y en avait beaucoup, et Yoshino lui avait donné un beau couteau japonais, très aiguisée."
"Elle ne comprenait pas trop pourquoi d’ailleurs, c’était peu pratique, il était très coupant et elle devait prendre des précautions pour éviter qu’un de ses doigts y passe."
"Au bout de quelques heures, Clateau vint vers elle."
show clateau B3 S1 Y1 at right
with dissolve
clateau "Ça m’a l’air difficile. Tu ne veux pas que je t’aide un peu ?"
hide clateau
with dissolve
# TODONE “Oui, je veux bien.” = point Clateau/ “Non ! Je vais terminer seule.”= point Yoshino
menu:
    " Oui, je veux bien.":
        $ relation_clateau += 1
        show ezo B1 S3 Y4 at left, xflip
        with dissolve
        ezo "Oui, je veux bien."
        show clateau B3 S1 Y2 at right
        with dissolve
        clateau "Désolé pour ça. Je pense qu’elle voulait t’initier un peu au maniement des couteaux, mais la méthode…"
        "Ezo regarda sa main. En effet, elle était devenue plus habile à force de manier son couteau avec dextérité pour protéger ses mains."
        show ezo B1 S3 Y2 at left, xflip
        with dissolve
        ezo "Merci de m’aider."
        show clateau B1 S1 Y4 at right
        with dissolve
        clateau "De rien. Ça me rappelle le bon vieux temps."
        show ezo B4 S3 Y1 at left, xflip
        with dissolve
        ezo "Le bon vieux temps… Mais je suis contente que tu sois là."
        "Avec une paire de main supplémentaire, ils vinrent facilement à bout de la cagette de pommes de terre, qu’ils apportèrent à Yoshino. Celle-ci, en voyant que Clateau avait aidé, soupira, mais ne fit pas de commentaire."
    " Non ! Je vais terminer seule.":
        $relation_yoshino += 1
        show ezo B5 S1 Y2 at left, xflip
        with dissolve
        ezo "Non ! Je vais terminer seule."
        show clateau B3 S1 Y1 at right
        with dissolve
        clateau "D’accord…"
        hide ezo
        with dissolve
        hide clateau
        with dissolve
        "Malgré la difficulté, Ezo persévéra dans l’effort. Elle manqua de se couper le pouce plusieurs fois, et avait des crampes aux mains à force de serrer les couteaux."
        "Elle finit néanmoins par réussir à terminer la cagette. Elle remarqua qu’une fois terminée, elle avait acquis une certaine dextérité dans le maniement de ces couteaux particulièrement tranchant. Ezo revint vers Yoshino et lui apporta les patates épluchées."
        show yoshino B2 S1 Y1 at right
        with dissolve
        yoshino "Oh ! Impressionnant ! Je pensais que tu abandonnerai rapidement vu la quantité."
        show ezo B2 S1 Y3 at left, xflip
        with dissolve
        ezo "Tu me sous-estime !"
hide yoshino
with dissolve
hide ezo
with dissolve
"Yoshino et Clateau étaient tous les deux en train de s’occuper de la cuisine. Le rythme était important."
"Quand le service en salle tendait à se calmer, c’était le bar qui s’agitait. Ezo piétinait d’impatience de commencer à aider, elle aussi."
show ezo B1 S1 Y1 at left, xflip
with dissolve
ezo "J’ai terminé ma corvée de patate, je sais me servir des couteaux de cuisine, je peux commencer maintenant ?"
"Cette fois-ci, ce fut Clateau qui se tourna vers elle, avec un sourire un peu gêné."
show clateau B1 S2 Y2 at right
with dissolve
clateau "On a déjà presque terminé cette fournée… En fait, il faudrait plutôt que tu nous aide à distribuer les plats à l’équipe de service…"
hide ezo
with dissolve
hide clateau
with dissolve
"Ezo se mit les mains sur les hanches, gonflant ses joues, et marmonna quelque chose avant de prendre les plats qu’on lui tendait."
"Elle avait très envie de se plaindre mais sa rigueur militaire la restreignait."
"Ezo fut un peu déstabilisée par le nombre de plat qu’elle devait porter en une fois. Elle essaya de les mettre plus ou moins sur ses bras, en espérant ne pas les renverser."
"Quand elle arriva à la double-porte menant vers la salle, Akié et Sei les réceptionnèrent."
"Ezo fut surprise de leur habileté à tous les récupérer et à se déplacer avec pour les servir, alors qu’elle-même avait eu beaucoup de peine pour faire quelques mètres avec."
show yoshino B5 S1 Y1 at right
with dissolve
yoshino "Un autre plat !"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "J’arrive !"
show yoshino B1 S1 Y1 at right
with dissolve
yoshino "Celui-là, c’est un dessert, pour le bar."
show ezo B2 S1 Y2 at left, xflip
with dissolve
ezo "Compris !"
hide ezo
with dissolve
hide yoshino
with dissolve
"Ezo traversa la cuisine, et se mit face au passe-plat qui donnait sur le bar. Mais personne ne vint."
show ezo B1 S2 Y2 at left, xflip
with dissolve
ezo "Ran ?"
"Ezo passa la tête dans le trou, sans la voir. Peut-être était-elle en train de servir ?"
scene bg bar
with dissolve
"Ezo ouvrit la petite porte qui donnait sur le bar, et, se tournant vers le comptoir, elle eu la surprise de voir que Ran était en train de dormir debout."
"La salle était calme, comme pour respecter le sommeil de la barmaid. Quelques rires fusaient de ci de là de la part des clients, visiblement la scène leur était habituelle."
# TODONE “Réveiller Ran tout doucement.” = point Clateau/ “éveiller Ran en lui lançant un plateau dans la tête.” = point Yoshino
menu:
    " Réveiller Ran tout doucement.":
        $ relation_clateau += 1
        "Ezo soupira un coup, et s’approcha un peu de Ran. Elle lui posa le verre froid du sorbet sur le front, ce qui la réveilla."
        show ran B5 S3 Y8 at right
        with dissolve
        ran "Hiiiii ! C’est gelé !"
        show ezo B2 S2 Y2 at left, xflip
        with dissolve
        ezo "Voilà le dessert…"
        show ran B1 S1 Y4 at right
        with dissolve
        ran "Oh, merci à vous ! Il me semble que je me sois assoupie quelques instants."
        show ezo B2 S2 Y6 at left, xflip
        with dissolve
        ezo "Et ça t’arrive souvent ?"
        show ran B1 S1 Y3 at right
        with dissolve
        ran "De temps en temps, je ne supporte pas l’activité prolongée."
        "Ezo préféra ne pas répondre, et s’en retourna en cuisine, en se demandant comment Ran faisait pour gérer le bar avec un flegme pareil."
    " Réveiller Ran en lui lançant un plateau dans la tête.":
        $ relation_yoshino += 1
        "Voyant que Ran somnolait tranquillement alors qu’elle galérait avec les plats, Ezo commença à fulminer. Elle posa son sorbet sur une table, s’empara d’un des plats de service posée dessus, et l’envoya sur Ran. Le plateau tournoya puis vint s’écraser sur la tête de la pauvre dormeuse."
        show ran B5 S3 Y8 at right
        with dissolve
        ran "Aïïïïïeuh ! Cela fait terriblement mal !"
        show ezo B1 S3 Y2 at left, xflip
        with dissolve
        ezo "Tait-toi donc. Tiens, voilà le sorbet de la table 4."
        show ran B7 S2 Y8 at right
        with dissolve
        ran "Mademoiselle Ezo ! Je vous trouve bien trop violente ! On dirait mademoiselle Yoshino !"
        show ezo B8 S1 Y2 at left, xflip
        with dissolve
        ezo "AU TRAVAIL !"
        "Ezo retourna, avec sa droiture de militaire, dans les cuisines, laissant Ran seule avec sa bosse."
hide ezo
with dissolve
hide ran
with dissolve
scene bg cuisine
with dissolve
"Une fois de retour en cuisine, et n’ayant rien à faire, Ezo commença à observer Clateau. Il découpait habilement des légumes qu’il mettait à bouillir dans une marmite."
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "C’est vrai que pendant les campagnes, c’était toujours toi qui cuisinait dans le régiment…"
show clateau B1 S1 Y4 at right
with dissolve
clateau "Ahaha, ça a toujours été ma passion ! Je suis content de pouvoir enfin cuisiner dans un vrai restaurant, qui plus est, le miens."
show ezo B4 S2 Y2 at left, xflip
with dissolve
ezo "Mais si tu aimes tellement cuisiner, pourquoi tu t’es engagé ? C’est pas spécialement dur à faire."
"Lorsqu’Ezo posa sa question, Clateau commença à ralentir le rythme de ses découpes."
show clateau B3 S2 Y2 at right
with dissolve
clateau "À l’époque, mon père voulait que j’aie un travail prometteur, alors je suis rentrée à l’académie militaire. J’étais jeune, je pensais que ça ne durerai qu’un temps, que j’allais voyager… Mais une fois les campagnes de colonisation débutée, on peut difficilement s’extraire du corps colonial…"
show ezo B4 S2 Y2 at left, xflip
with dissolve
ezo "C’est vrai que c’est dur…"
show clateau B3 S2 Y2 at right
with dissolve
clateau "Et tu es la mieux placée pour le savoir !"
"Ezo serra dans ses mains une des tomates posées sur la table, et continua la discussion en la fixant."
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Au moins ici on a des produits frais… plus besoin de faire bouillir l’eau avant de la boire…"
show clateau B1 S2 Y4 at right
with dissolve
clateau "Rien à voir avec le champ de bataille, hein ?"
show ezo B1 S3 Y4 at left, xflip
with dissolve
ezo "Oui ! Mais déjà à l’époque tu faisais des merveilles avec les rations dégueulasses du gouvernement."
hide ezo
with dissolve
hide clateau
with dissolve
"Pendant qu’ils parlaient, Yoshino s’était un peu rapprochée, intriguée d’en savoir un peu plus sur le passé d’Ezo et de Clateau."
show yoshino B4 S1 Y3 at left, xflip
with dissolve
yoshino "Hmpf ! Si c’est un cuisinier hors-pair, il est vraiment inutile pour tenir un personnel ! C’est une vraie catastrophe."
show clateau B1 S3 Y1 at right
with dissolve
clateau "Mais heureusement je suis bien secondé !"
show yoshino B4 S1 Y2 at left, xflip
with dissolve
yoshino "…"
hide yoshino
with dissolve
hide clateau
with dissolve
# TODONE “En tous cas, merci à toi de m’avoir accueilli dans le restaurant.” = point Clateau/ “Merci de l’aider, Yoshino.” = point Yoshino
menu:
    " En tous cas, merci à toi de m’avoir accueilli dans le restaurant.":
        $ relation_clateau += 1
        show ezo B2 S3 Y4 at left, xflip
        with dissolve
        ezo "En tous cas, merci à toi de m’avoir accueilli dans le restaurant."
        show clateau B1 S3 Y4 at right
        with dissolve
        clateau "Content que tu te plaises ici. C’était bien la moindre des choses que je puisse faire."
    " Merci de l’aider, Yoshino. Si le resto avait coulé avant que j’arrive, je n’aurai plus eu nulle part où aller.":
        $ relation_yoshino
        show ezo B2 S3 Y4 at left, xflip
        with dissolve
        ezo "Merci de l’aider, Yoshino. Si le resto avait coulé avant que j’arrive, je n’aurai plus eu nulle part où aller."
        show yoshino B5 S1 Y1 at right
        with dissolve
        yoshino "Hm, bah… c’est dans mon intérêt aussi…"
hide ezo
with dissolve
hide yoshino
with dissolve
hide clateau
with dissolve
"Après un petit flottement après cette discussion, ils se remirent au travail. Ezo suivit Yoshino, et se posa devant elle."
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "Je pense que je peux commencer à cuisiner maintenant non ?"
show yoshino B5 S1 Y1 at right
with dissolve
yoshino "Pour commencer, va plutôt me chercher ça !"
hide ezo
with dissolve
hide yoshino
with dissolve
"Yoshino tendit à Ezo un petit papier avec quelques ingrédient marqué dessus. Ezo l’attrapa des mains de Yoshino et partie vers la réserve en bougonnant."
"La réserve était située juste à côté de l’escalier qui menait aux étages, au fond des cuisines. Ezo entra dans le réduit sombre et chercha les ingrédients. De la farine, de la viande…"
"Elle remarqua que la porte qui menait vers l’extérieur était ouverte. En l’entrouvrant, elle pu découvrir Akié, accroupie avec trois petits chatons à qui elle donnait du lait."
scene bg rue
with dissolve
show ezo B5 S2 Y2 at left, xflip
with dissolve
ezo "Akié ?"
show akie B6 S1 Y2 at right
with dissolve
akie "Oh, Ezo ! Ce n’est pas ce que tu crois ! Je m’occupe de ces petits, mais je vais aussi m’occuper de toi, ne t’inquiète pas !"
show ezo B7 S1 Y2 at left, xflip
with dissolve
ezo "Mais je ne suis pas un chaton ! Et plutôt, qu’est-ce que tu fais là ? Je ne pense pas que Yoshino accepte que tu sèches le travail pour nourrir des chats, surtout si tu piques dans le garde-manger."
show akie B6 S2 Y8 at right
with dissolve
akie "Je sais… mais ne me dénonce pas !"
show ezo B7 S1 Y2 at left, xflip
with dissolve
ezo "Hmm…"
show akie B4 S2 Y8 at right
with dissolve
akie "S’il vous plaît, capitaine Ezo !"
"En disant cela, Akié s’était mise au garde à vous, enfin, elle avait essayée. Ezo en rigola un peu."
"Elle se dit qu’il fallait laisser couler, d’autant qu’elle en était en partie responsable, puisqu’elle avait mangé le pain que Yoshino avait gardé pour que Akié puisse nourrir ses animaux."
show ezo B4 S3 Y3 at left, xflip
with dissolve
ezo "D’accord, d’accord, on va dire que j’ai rien vu."
show akie B1 S1 Y4 at right
with dissolve
akie "Merci ma petite Ezo ! La prochaine fois je penserai à toi."
show ezo B7 S1 Y8 at left, xflip
with dissolve
ezo "Mais je ne suis toujours pas un chat ! M’en fous de ta coupelle de lait !"
hide akie
with dissolve
hide ezo
with dissolve
scene bg cuisine
with dissolve
"En retournant en cuisine, Ezo trouva que l’ambiance avait changée."
"Clateau et Yoshino étaient tout agités, ils couraient partout dans la pièce, allant de casseroles en plateaux, pour ajouter des légumes, ajuster la sauce…"
show yoshino B1 S1 Y1 at right
with dissolve
yoshino "Ezo ! Tu tombes bien. Le moment le plus dur de la journée a commencé. T’as mes ingrédients ?"
show ezo B4 S1 Y2 at left, xflip
with dissolve
ezo "Euh, oui, mais…"
show yoshino B2 S1 Y1 at right
with dissolve
yoshino "Bien, donne. On va être occupé."
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Alors je suppose que c’est le moment de m’y mettre aussi ? je ne vais pas vous regarder faire toute la journée."
# TODONE “Je vais t’aider.”= point Yoshino/”je vais filer un coup de main à Clateau.”= point Clateau
menu:
    " Je vais t’aider.":
        $ relation_yoshino += 1
        show ezo B1 S3 Y4 at left, xflip
        with dissolve
        ezo "Je vais t’aider."
        # Si « Je vais t’aider. »
        show yoshino B4 S2 Y2 at right
        with dissolve
        yoshino "Je ne sais pas…"
        show ezo B1 S3 Y4 at left, xflip
        with dissolve
        ezo "Allons, tu es débordée… ne te fais pas prier."
        show yoshino B5 S3 Y3 at right
        with dissolve
        yoshino "Bon… alors prend ça et suis bien ce que je fais."
        hide ezo
        with dissolve
        hide yoshino
        with dissolve
        "Ezo prit un bol et un fouet, et imita Yoshino. De ce qu’elle comprit, c’était elle qui était en charge des entrées et des desserts."
        "Elle faisait tout un tas de sorbets et de parfaits pour le bar, mais aussi des entrées élaborées pour la salle, et même des gâteaux. Certains étaient si élaborés qu’ils ressemblaient presque à des pièces montées."
        show ezo B1 S3 Y2 at left, xflip
        with dissolve
        ezo "Dit donc, tu es drôlement adroite… Je ne t’imaginais pas aussi raffinée…"
        show yoshino B8 S3 Y1 at right
        with dissolve
        yoshino "Hé ! Tu m’as pris pour qui ?"
        hide yoshino
        with dissolve
        hide ezo
        with dissolve
        "Yoshino terminait de dresser une salade de foie gras une assiette immaculée, puis s’attaqua à la préparation d’un gâteau coloré."
        "Ezo, elle, s’occupait de battre des œufs en neige ou de malaxer la pâte que préparait Yoshino."
        show yoshino B2 S1 Y3 at right
        with dissolve
        yoshino " Tu vois, ici, à part les ouvriers comme Tsugumi, on a aussi des clients un peu plus raffinés qui viennent, il faut savoir satisfaire leurs attentes."
        "Yoshino posa avec grande précaution son gâteau son l’assiette. La chantilly était élégamment entortillée sur le dessus et un biscuit était planté dedans."
        show ezo B2 S2 Y2 at left, xflip
        with dissolve
        ezo "Ou peut-être que c’est la clientèle fortunée qui vient pour tes plats et non l’inverse…"
        show yoshino B1 S1 Y1 at right
        with dissolve
        yoshino "Hm ? T’as dit quelque chose ?"
        show ezo B2 S1 Y2 at left, xflip
        with dissolve
        ezo "Non, rien ! Je l’apporte tout de suite !"
        show ezo B2 S1 Y4 at left, xflip
        with dissolve
        hide yoshino
        with dissolve
        ezo "Elle est assez féminine, cette Yoshino…"
        hide ezo
        with dissolve
    " je vais filer un coup de main à Clateau.":
        $ relation_clateau += 1
        show ezo B1 S3 Y4 at left, xflip
        with dissolve
        ezo "je vais filer un coup de main à Clateau."
        # Si « je vais filer un coup de main à Clateau. »
        show yoshino B3 S1 Y1 at right
        with dissolve
        yoshino "Ne va pas le gêner !"
        show ezo B1 S3 Y1 at left, xflip
        with dissolve
        ezo "Mais non !"
        hide yoshino
        with dissolve
        hide ezo
        with dissolve
        "Clateau était concentré sur ses casseroles. Il goûtait un plat pour s’assurer du dosage d’épices."
        show ezo B4 S3 Y1 at left, xflip
        with dissolve
        ezo "Euh… je peux venir t’aider ?"
        show clateau B1 S1 Y4 at right
        with dissolve
        clateau "Bien sûr. Tu peux de préparer les viandes ?"
        show ezo B1 S3 Y4 at left, xflip
        with dissolve
        ezo "Oui !"
        hide ezo
        with dissolve
        hide clateau
        with dissolve
        "Ezo commença son œuvre sur la planche à découper. Elle remarqua qu’elle était bien plus adroite avec les couteaux tranchants qu’avant, grâce à la séance d’épluchage de patate du matin."
        "Clateau était lui en train de gérer plusieurs plats à la fois. Il faisait ça avec une très grande habileté : tandis qu’une grande casserole en fonte mijotait, il préparait un sashimi, tout en surveillant la friture d’autre chose."
        show ezo B2 S3 Y1 at left, xflip
        with dissolve
        ezo "Il est vraiment dans son élément ! C’est tellement dommage que son talent ait été gâché par l’armée…"
        show ezo B2 S3 Y2 at left, xflip
        with dissolve
        ezo "Et il va falloir que je me mette au travail aussi si je ne veux pas être à la traîne !"
        hide ezo
        with dissolve
        "Le rythme frénétique des commandes ne laissait pas de répit. Akié ou Sei rentraient dans la pièce, récupéraient un plat, et en demandait trois nouveaux. Malgré tout, Clateau ne semblait pas décontenancé, et continuait ses préparations avec sérieux."
        show clateau B1 S1 Y2 at right
        with dissolve
        clateau "Tu sais, Ezo, je suis vraiment content que tu ai décidée de me rejoindre ici."
        show ezo B1 S3 Y3 at left, xflip
        with dissolve
        ezo "J’avais pas trop le choix… Mais merci de m’avoir fourni un endroit où aller, je n’ai connu que la guerre jusqu’à maintenant."
        show clateau B3 S1 Y2 at right
        with dissolve
        clateau "Je sais… j’aurais voulu faire quelque chose avant, mais ça me rassure de savoir que tu es là. Et j’apprécie d’avoir un camarade avec moi !"
        hide clateau
        with dissolve
        hide ezo
        with dissolve
        #  Fin des “si”

"Le coup de feu ne dura très longtemps, mais la pression qu’il mit sur les cuisines épuisa tout le monde. Yoshino se posa sur une chaise, presque essoufflée. Ezo fit de même. Bien qu’elle n’ai pas été aussi active, l’assimilation de toutes ces nouvelles choses avait été épuisante. Clateau leur apporta des cafés."
show ezo B5 S2 Y2 at left, xflip
with dissolve
ezo "Je n’imaginais pas le travail en cuisine aussi épuisant."
show yoshino B3 S1 Y4 at right
with dissolve
yoshino "Des regrets ?"
show ezo B5 S1 Y2 at left, xflip
with dissolve
ezo "Aucun ! Je suis en train de dépasser mes limites."
"Yoshino la regarda avec empathie, puis repris un visage plus sérieux."
show yoshino B5 S1 Y2 at right
with dissolve
yoshino "Tout à l’heure, tu as croisée Akié, n’est-ce pas ?"
show ezo B1 S3 Y1 at left, xflip
with dissolve
ezo "Moi ? Non non…"
show yoshino B4 S1 Y1 at right
with dissolve
yoshino "Pas la peine de mentir, je vous ai entendu."
show ezo B5 S2 Y2 Go at left, xflip
with dissolve
ezo "Écoute, c’est…"
"Yoshino allait fouiller dans un des placards de la cuisine pour en sortir un petit sac de toile."
show yoshino B1 S1 Y1 at right
with dissolve
yoshino "Tiens, c’est que des trucs qu’on ne peut plus servir. Ça lui évitera de piller le garde-manger."
show ezo B1 S3 Y4 -Go at left, xflip
with dissolve
ezo "Oh, c’est si gentil !"
hide ezo
with dissolve
show clateau B1 S1 Y4 at left, xflip
with dissolve
clateau "Tu peux te montrer mignonne des fois."
show yoshino B5 S3 Y1 at right
with dissolve
yoshino "On n’en aurait pas eu besoin si vous aviez pas boulotté le pain que je lui avais mis de côté, idiots ! Allez, il faut se remettre au travail."
hide ezo
with dissolve
hide clateau
with dissolve
hide yoshino
with dissolve
"Ezo et Clateau repartirent au travail en vitesse."
show ezo B2 S3 Y2 at left, xflip
with dissolve
ezo "Je vais aller donner ça à Akié avant, mais Yoshino est étonnamment sympa."
show clateau B1 S1 Y1 at right
with dissolve
clateau "En fait, c’est vraiment une gentille fille, elle a juste un peu de mal à communiquer."
hide ezo
with dissolve
hide clateau
with dissolve
scene bg salle
with dissolve
"Ezo attendit un moment de calme en salle, pour aller trouver Akié et lui remettre le sac que lui avait confiée Yoshino."
show ezo B2 S3 Y4 at left, xflip
with dissolve
ezo "Tiens, c’est pour les chats."
show akie B2 S1 Y2 at right
with dissolve
akie "Oh, merci ! Je suppose que je dois remercier Yoshino ?"
show ezo B5 S3 Y2 at left, xflip
with dissolve
ezo "Hein ? Comment tu le sais ?"
show akie B2 S1 Y4 at right
with dissolve
akie "Elle est plutôt mignonne, tu sais ! Elle est un peu brusque, mais il faut passer outre. Je sais qu’elle fait souvent semblant de ne rien voir quand Clateau me donne de quoi nourrir les animaux errants."
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Ça alors…"
hide ezo
with dissolve
hide akie
with dissolve
"Ezo remit le sac à Akié. Elle ne pensait pas que Yoshino était aussi sympa."
scene bg cuisine
with dissolve
"Une fois revenue, elle trouva Yoshino et Clateau assis devant l’un des comptoirs du restaurant, en train de manger."
show ezo B1 S1 Y8 Go at left, xflip
with dissolve
ezo "Qu’est-ce que vous foutez ?!"
show yoshino B1 S1 Y1 at right
with dissolve
yoshino "On prend notre pause ! Personne ne vient manger en début d’après-midi. D’ailleurs tu devrais en faire de même, dans pas longtemps, c’est le bar qui recommencera à s’agiter."
hide ezo
with dissolve
hide yoshino
with dissolve
"Ezo s’assit et commença à manger ce que Clateau leur avait préparé."
show clateau B2 S1 Y1 at right
with dissolve
clateau "Tiens, pendant le temps mort, et si je t’apprenais un peu à cuisiner ?"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Vraiment ?"
show clateau B1 S1 Y1 at right
with dissolve
clateau "Tu pourras nous aider plus efficacement."
hide clateau
with dissolve
show yoshino B4 S1 Y3 at right
with dissolve
yoshino "Je ne sais pas si c’est le moment, on va gâcher des ingrédients…"
show ezo B5 S1 Y2 at left, xflip
with dissolve
ezo "Si ! Je veux apprendre à cuisiner !"
hide yoshino
with dissolve
show clateau B1 S1 Y4 at right
with dissolve
clateau "Allez Yoshino, elle est motivée !"
hide clateau
with dissolve
show yoshino B4 S1 Y2 at right
with dissolve
yoshino "Bon…"
hide yoshino
with dissolve
"Clateau sortit une grosse marmite en fer des placards, et la posa sur le feu."
show clateau B1 S1 Y1 at right
with dissolve
clateau "Ezo, tu peux m’apporter ces légumes ? Ah, et ce morceau de bœuf…"
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "Bien chef !"
hide ezo
with dissolve
hide clateau
with dissolve
"Ezo revint rapidement avec les aliments. Elle était toute excitée d’apprendre sérieusement à cuisiner."
"Avec l’aide de Clateau, elle apprit à découper proprement les légumes, et aussi à gérer le feu pour ne pas assécher la viande. Chaque geste de Clateau était dûment dosé et Ezo s’efforçait d’en imiter la pratique."
"Il lui fallut bien une grosse quinzaine de minutes pour réussir à maîtriser les bases. Une fois le couvercle posé, Ezo pu souffler un peu."
show yoshino B5 S1 Y2 at right
with dissolve
yoshino "Attendez un peu, vous êtes pas en train de faire un pot-au-feu ?"
show clateau B1 S1 Y4 at left, xflip
with dissolve
clateau "Si si. Tu aurais préférée qu’on fasse un nabe ?"
show yoshino B1 S3 Y1 at right
with dissolve
yoshino "C’est la même chose ! Non, je sais que c’est un restaurant français, mais on aurait pu choisir quelque chose de mieux qu’un plat de campagnard…"
show clateau B4 S1 Y1 at left, xflip
with dissolve
clateau "Mais c’est très bien le pot-au-feu !"
show yoshino B1 S3 Y1 Go at right
with dissolve
yoshino "Si j’avais su je lui aurais appris à faire des sorbets ou un parfait…"
hide clateau
with dissolve
hide yoshino
with dissolve
# TODONE “C’est vrai que j’aurais préférée apprendre à faire des desserts.”= point Yoshino/”Le pot-au-feu, c’est nourrissant” = Clateau
menu:
    " C’est vrai que j’aurais préféré apprendre à faire des desserts.":
        $ relation_yoshino += 1
        show ezo B4 S2 Y3 at left, xflip
        with dissolve
        ezo "C’est vrai que j’aurais préférée apprendre à faire des desserts."
        show clateau B4 S2 Y1 Go at right
        with dissolve
        clateau "Mais ! Et le pot-au-feu ?"
        hide clateau
        with dissolve
        hide yoshino
        with dissolve
        show yoshino B7 S2 Y2 at left, xflip
        with dissolve
        yoshino "Pfff, tu comprends rien aux filles… Bien évidemment qu’elle préfère les desserts !"
    " Le pot-au-feu, c’est nourrissant, c’est rustique, bref, c’est parfait pour un militaire.":
        $ relation_clateau += 1
        show ezo B1 S1 Y1 at left, xflip
        with dissolve
        ezo "Le pot-au-feu, c’est nourrissant, c’est rustique, bref, c’est parfait pour un militaire."
        show clateau B1 S1 Y4 at right
        with dissolve
        clateau "Ah, voilà ! Qu’est-ce que je disais !"
        hide clateau
        with dissolve
        show yoshino B4 S1 Y2 at right
        with dissolve
        yoshino "Hmm, je croyais que tu serais de mon côté…"
scene bg bar
with dissolve
"Au même moment, ils entendirent un grand bruit dans la salle du bar. Ils allèrent voir, soupçonnant que Ran était encore endormie."
"Une fois au bar, ils y trouvèrent bien Ran à sa place en train de dormir, et Tsugumi, plantée au milieu et humant l’air."
show tsugumi B1 S1 Y2 at right
with dissolve
tsugumi "Mais qu’est-ce que je sens ? On se fait un nabe sans moi ?"
show clateau B2 S3 Y2 at left, xflip
with dissolve
clateau "En fait c’est un pot-au-feu."
hide tsugumi
with dissolve
show yoshino B8 S3 Y2 Go at right
with dissolve
yoshino "C’est. La. Même. Chose."
hide yoshino
with dissolve
hide clateau
with dissolve
show ezo B4 S3 Y4 at left, xflip
with dissolve
ezo "Tu veux goûter ? C’est moi qui l’ai fait !"
show tsugumi B1 S1 Y2 at right
with dissolve
tsugumi "Je dirais pas non !"
"Ezo sortit une assiette à Tsugumi. Clateau ramena la marmite, devant les yeux pétillants de Tsugumi."
show tsugumi B1 S1 Y1 at right
with dissolve
tsugumi "Ça m’a l’air parfait !"
show ezo B2 S3 Y2 at left, xflip
with dissolve
ezo "Tu verras, c’est un plat parfait pour les ouvriers !"
hide ezo
with dissolve
hide tsugumi
with dissolve
"Ezo servit à Tsugumi une bonne assiette, qu’elle s’empressa d’entamer. Yoshino quant à elle, parti corriger Ran. Après lui avoir crié dans les oreilles pour la réveiller, elle revint voir le résultat de la dégustation."
show yoshino B5 S2 Y1 at right
with dissolve
yoshino "Alors ?"
show tsugumi B1 S1 Y1 at left, xflip
with dissolve
tsugumi "Délicieux !"
hide tsugumi
with dissolve
show ran B1 S1 Y2 at left, xflip
with dissolve
ran "Et si c’est Tsugu qui le dit, c’est que c’est vrai…"
show yoshino B4 S2 Y1 Go at right
with dissolve
yoshino "Je ne sais pas si son palais est assez fin…"
hide yoshino
with dissolve
hide ran
with dissolve
show tsugumi B1 S1 Y2 at left, xflip
with dissolve
tsugumi "Et j’peux avoir un verre de bière… non, de vin avec !"
show ezo B1 S3 Y4 at right
with dissolve
ezo "Ah, j’aime ça !"
hide tsugumi
with dissolve
show ran B1 S1 Y4 at left, xflip
with dissolve
ran "Que le petit peuple est amusant !"
hide ran
with dissolve
hide tsugumi
with dissolve
hide ezo
with dissolve
show yoshino B5 S3 Y3 at right
with dissolve
yoshino "C’est gentil tout ça, mais il faudrait retourner bosser !"
hide yoshino
with dissolve
"Yoshino attrapa Clateau et Ezo par le col, les traînant en cuisine, tout en lançant un regard noir à Ran, la prévenant qu’il allait falloir bosser au risque de s’en prendre une."
scene bg cuisine
with dissolve
"Le coup de feu du soir fut plus simple que celui du midi. Ezo commençait à s’habituer au rythme, et elle pouvait aider Clateau et Yoshino efficacement. La nuit était presque tombée lorsqu’Ezo eu terminée son travail."
show ezo B1 S2 Y6 at left, xflip
with dissolve
ezo "Je crois que je vais commencer à regretter la bataille d’Hakodate…"
show yoshino B3 S3 Y1 at right
with dissolve
yoshino "Qu’est-ce que tu croyais ? En cuisine, chaque jour est une nouvelle bataille !"
hide yoshino
with dissolve
show clateau B1 S1 Y3 at right
with dissolve
clateau "Allons, elle s’est déjà bien démenée aujourd’hui. Tu peux aller prendre une pause avec les autres au bar, on te rejoint après."
hide clateau
with dissolve
hide ezo
with dissolve
# TODONE fondu en noir
scene bg Black
with dissolve

scene bg bar
with dissolve
"Ezo était passablement fatiguée par sa journée et se traîna presque jusqu’au bar. Elle eu la surprise d’y trouver Ran parfaitement éveillée, en train de servir les rares clients qui avaient tenu jusqu’à cette heure tardive."
"Tsugumi était encore là, devant une pile de pinte de bières vides, et rigolait à haute voix. Akié et Sei aussi avaient prit place au comptoir."
show akie B1 S1 Y2 at right
with dissolve
akie "Oh, ma petite Ezo ! Vient donc !"
hide akie
with dissolve
show sei B1 S1 Y1 at right
with dissolve
sei "Comment s’est passé ta journée ?"
show ezo B2 S3 Y4 at left, xflip
with dissolve
ezo "C’était épuisant, mais j’ai beaucoup appris."
show sei B2 S1 Y3 at right
with dissolve
sei "J’avais un peu peur que tu abandonnes après une journée aussi dure…"
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "J’en ai vu d’autres !"
hide ezo
with dissolve
hide sei
with dissolve
"Ezo regarda Tsugumi, qui semblait hilare sous les effets de l’alcool."
show ezo B1 S2 Y4 at left, xflip
with dissolve
ezo "Tu passes ta vie ici toi !"
show tsugumi B1 S1 Y2 at right
with dissolve
tsugumi "Il faut dire que la bière est bonne et pas cher, j’y peux rien !"
hide ezo
with dissolve
show ran B1 S1 Y4 at left, xflip
with dissolve
ran "Et mademoiselle Tsugumi met une bonne animation !"
show tsugumi B1 S1 Y1 at right
with dissolve
tsugumi "Ouais ! D’ailleurs on devrait boire pour féliciter Ezo d’avoir réussis à survivre à Yoshin…"
hide ran
with dissolve
hide tsugumi
with dissolve
"Yoshino surgit dans la salle, tétanisant Tsugumi eu beau milieu de sa phrase. Puis elle s’assit tranquillement sans faire de commentaire."
show yoshino B1 S1 Y1 at right
with dissolve
yoshino "Ran, sert moi une bière… Non, deux."
show tsugumi B2 S1 Y2 at left, xflip
with dissolve
tsugumi "Ooooh, finalement il arrive à la si stricte chef des cuisines de boire ?"
show yoshino B3 S1 Y4 at right
with dissolve
yoshino "Un peu ma petite, et je tiens bien mieux l’alcool que toi."
show tsugumi B1 S2 Y1 at left, xflip
with dissolve
tsugumi "C’est ce qu’on va voir !"
hide yoshino
with dissolve
hide tsugumi
with dissolve
"Un concours de boisson débuta. Yoshino, fatiguée, enchaîna les verres sans sourciller. Tsugumi, elle, avait déjà bu mais tiens bon encore 10 verres avant de tomber. Yoshino enchaîna avec Akié, Sei, et même Ran, qui elle s’évanouit au bout du troisième."
show yoshino B5 S1 Y4 R2 at right
with dissolve
yoshino "Alooooooors ?!"
hide yoshino
with dissolve
"Ce furent ses derniers mots, Yoshino finit par s’endormir, de fatigue et d’ivresse. Les autres membres de l’équipe, eux aussi épuisés, s’en allèrent, la nuit tombait et toutes les rues n’étaient pas sûres. Seule restait Yoshino qui dormait à poings fermées."
show ezo B1 S2 Y1 at left, xflip
with dissolve
ezo "Euh… qu’est-ce qu’on va faire d’elle ?"
"Clateau posa une couverture sur Yoshino."
show clateau B1 S1 Y3 at right
with dissolve
clateau "On va la laisser là. Ça lui arrive de temps en temps."
show ezo B1 S2 Y2 at left, xflip
with dissolve
ezo "Mais on ne va pas s’inquiéter, chez elle ?"
show clateau B3 S1 Y2 at right
with dissolve
clateau "Yoshino… est orpheline de guerre. Donc personne ne s'inquiètera."
show ezo B4 S3 Y2 at left, xflip
with dissolve
ezo "Oh…"
show clateau B3 S1 Y2 at right
with dissolve
clateau "Elle est stricte mais je suis sûr qu’elle est contente d’avoir une camarade de son âge à ses côtés."
hide clateau
with dissolve
hide ezo
with dissolve
"Clateau et Ezo allèrent se coucher eux aussi, laissant Yoshino dormir paisiblement."
scene bg grenier
with dissolve
"Ezo pénétra dans sa chambre, vraiment fatiguée. Elle se déshabilla tout en pensant à ce que Clateau lui avait dit. Yoshino était une orpheline de guerre ? Cela explique peut-être pourquoi elle est si renfermée sur elle-même."
"Ezo continua à réfléchir. Ses parents avaient donc participés à la guerre ? Était-ce des militaires, ou des civils ? Et dans quel camp étaient-ils ? Ezo se questionnait. Avec la fatigue et l’alcool, elle avait mal à la tête, du mal à penser."
"Puis elle eut une illumination. Et si, pendant la guerre, elle avait tué les parents de Yoshino ? Elle avait perdue le compte de ses victimes depuis bien longtemps, mais elle ne pouvait pas oublier cette possibilité."
"Ezo finit par s’endormir loin dans la nuit, torturée par ses pensées."
# TODONE fondu en noir
scene bg Black
with Dissolve(1)

scene bg grenier
with dissolve
"Le lendemain matin, le soleil filtrait encore par la lucarne du grenier. Mais Ezo avait cogitée une bonne partie de la nuit, stressée et confuse et ne se réveillait pas."
"Entortillée dans ses draps, elle se questionnait encore sur la possibilité qu’elle ait à voir avec la disparition des parents de Yoshino."
show clateau B1 S3 Y1 at right
with dissolve
clateau "Ezo ? Tu dors encore ? Ezo ?"
"Clateau pénétra dans le grenier."
show ezo B8 S1 Y2 at left, xflip
with dissolve
ezo "AAAAAH ! Hors de ma chambre, pédolicon !"
hide ezo
with dissolve
hide clateau
with dissolve
"Ezo expulsa vers Clateau son coussin pour le chasser de la pièce. Elle se roula en boule sur son lit, comme le ferait un chat. Les yeux dans le floue pendant quelques instants, elle décida finalement de se lever."
scene bg cuisine
with dissolve
"Elle descendit en cuisine pour y trouver Yoshino. Elle semblait aller mieux, et était posée sur le comptoir avec un café."
show yoshino B1 S1 Y1 at right
with dissolve
yoshino "Salut."
show ezo B1 S2 Y2 at left, xflip
with dissolve
ezo "S-salut ! Ça va depuis hier ?"
show yoshino B1 S2 Y3 at right
with dissolve
yoshino "Oui, désolée. Ça m’arrive de temps en temps. Et toi, pas trop fatiguée après ta première journée ?"
show ezo B1 S3 Y4 at left, xflip
with dissolve
ezo "Nan, je pète la forme !"
show yoshino B1 S1 Y1 at right
with dissolve
yoshino "Prend un peu de café si tu veux."
"Ezo se servit une tasse. Elle se souvint que le bar était effectivement équipé de quoi torréfier le café, mais elle ne l’avait pas remarqué."
show ezo B2 S3 Y4 at left, xflip
with dissolve
ezo "Hm, il est plutôt bon."
show yoshino B2 S1 Y4 at right
with dissolve
yoshino "C’est Clateau qui la fait."
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Oh, il fait aussi un bon barista."
show yoshino B2 S1 Y4 at right
with dissolve
yoshino "Quand on parle de cuisine, rien ne l’arrête. Sinon…"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Oui ?"
show yoshino B5 S1 Y1 at right
with dissolve
yoshino "Ça fait pas un peu gamine de se faire réveiller le matin ?"
"Ezo se mit à rougir. Yoshino les avait entendus avec Clateau, et c’était très gênant."
menu:
    " Je… euh… il s’occupe de moi et…":
        show ezo B1 S3 Y1 R3 at left, xflip
        with dissolve
        ezo "Je… euh… il s’occupe de moi et…"
        show yoshino B3 S2 Y2 at right
        with dissolve
        yoshino "C’est mignon…"
    " Je ne l’ai pas demandé !":
        show ezo B1 S1 Y2 at left, xflip
        with dissolve
        ezo "Je ne l’ai pas demandé !"
        show yoshino B3 S1 Y2 at right
        with dissolve
        yoshino "Je te taquine, je sais qu’il est trop protecteur."
show ezo B1 S3 Y1 R2 at left, xflip
with dissolve
ezo "B-bon, quoi qu’il en soit, il est l’heure de travailler. Je vais retourner à mes patates."
show yoshino B2 S1 Y1 at right
with dissolve
yoshino "Stop stop stop… Puisque tu as été aussi productive hier, et comme il est encore tôt, je vais t’apprendre à faire des sorbets."
show ezo B5 S3 Y2 -R2 at left, xflip
with dissolve
ezo "Oooh !"
hide ezo
with dissolve
hide yoshino
with dissolve
"Ezo commença son apprentissage avec Yoshino dans le monde sucré des desserts. Contrairement à Clateau, les plats étaient fondamentalement plus simples à préparer, il n’y avait pas de viande à découper ou de légumes à faire macérer."
"Mais Yoshino était d’une rigueur extrême, les dosages étant fait au milligramme près."

show ezo B2 S3 Y4 at left, xflip
with dissolve
ezo "Je m’en tire mieux que je pensais !"
show yoshino B1 S1 Y3 at right
with dissolve
yoshino "Pas mal, mais on peut mieux faire… on va rajouter un peu de chantilly sur le dessus."
"Cette fois-ci, ce fut Clateau qui intervint."
hide ezo
with dissolve
show clateau B1 S2 Y1 at left, xflip
with dissolve
clateau "De la chantilly ? Je pense que ce sorbet est déjà suffisamment chargé !"
show yoshino B4 S3 Y4 at right
with dissolve
yoshino "Non ! Il faut encore en ajouter. N’est-ce pas ?"
# TODONE “Plus de crème, oui.” = point Yoshino /”Ça risque de faire gras” = point Clateau
menu:
    " Plus de crème, oui.":
        $relation_yoshino += 1
        hide clateau
        with dissolve
        show ezo B2 S3 Y4 at left, xflip
        with dissolve
        ezo "Plus de crème, oui."
        show yoshino B2 S3 Y3 at right
        with dissolve
        yoshino "Qu’est-ce que je disais ?"
    " Ça risque de faire gras…":
        $ relation_clateau += 1
        hide yoshino
        with dissolve
        hide clateau
        with dissolve
        show ezo B1 S3 Y2 at left, xflip
        with dissolve
        ezo "Ça risque de faire gras…"
        show clateau B1 S3 Y3 at right
        with dissolve
        clateau "Oui, soyons mesurés."
        hide clateau
        with dissolve
        show yoshino B4 S2 Y6 at right
        with dissolve
        yoshino "Bon bon, allons pour moins de crème…"
hide yoshino
with dissolve
hide ezo
with dissolve
"Une fois le premier sorbet terminé, les premiers clients commencèrent à arriver en masse. Le matin était assez chargé, car les bourgeois et les occidentaux de passages avaient prit l’habitude d’y prendre le petit-déjeuner. Heureusement, cela ne durait pas longtemps puisqu’il leur fallait partir rapidement au travail."
show clateau B1 S1 Y1 at right
with dissolve
clateau "Demain, ce sera jour de repos. Vous aurez votre journée de libre."
show ezo B1 S3 Y4 Go at left, xflip
with dissolve
ezo "Déjà des vacances alors que je viens à peine d’arriver ?"
hide clateau
with dissolve
show yoshino B1 S1 Y1 at right
with dissolve
yoshino "Voilà ce que c’est d’arriver en plein milieu d’une semaine."
hide clateau
with dissolve
show clateau B1 S1 Y4 at right
with dissolve
clateau "Mais tu as bien travaillé pendant ces deux jours !"
# TODONE : Le choix des si, se fait en fonction du nombre de points de chaque persos
# Si Yoshino
if relation_yoshino > relation_clateau:
    "Pendant qu’Ezo rangeait les casseroles qu’elle venait de nettoyer, Yoshino se rapprocha discrètement d’Ezo."
    show yoshino B1 S1 Y2 at right
    with dissolve
    yoshino "Dit… pendant notre jour de repos… tu voudrais venir chez moi ?"
    "Ezo sursauta presque lors de la demande. Elle ne pensait pas que Yoshino l'inviterai ! Mais elle accepta avec joie."
    show ezo B1 S3 Y4 at left, xflip
    with dissolve
    ezo "Bien sûr !"
    show yoshino B2 S1 Y4 at right
    with dissolve
    yoshino "Parfait."
    "La fin de la journée fut rythmée comme la précédente, mais cette fois Ezo n’avait plus en tête que le lendemain. Fatiguée par sa courte nuit de la veille, elle s’endormit promptement."
    jump yoshino_ch2
else:
    # Si Clateau
    "Ezo commença à ranger les couteaux utilisés pendant la journée. Clateau vint l’aider et commença à lui parler."
    show clateau B1 S1 Y1 at right
    with dissolve
    clateau "Alors, tu t’habitues bien au travail ?"
    show ezo B1 S3 Y4 at left, xflip
    with dissolve
    ezo "Oui, plutôt."
    show clateau B1 S3 Y2 at right
    with dissolve
    clateau "Si tu veux, je peux te montrer un peu les environs lors de ton jour de repos. Sinon, tu vas le passer dans la cuisine à t’entrainer."
    "Ezo réfléchit quelques minutes. Clateau avait raison… alors autant accepter."
    show ezo B2 S3 Y2 at left, xflip
    with dissolve
    ezo "Pourquoi pas."
    "Plutôt content de cette réponse, Clateau repartit ranger un autre coin de la cuisine."
    scene bg grenier
    with dissolve
    "La fin de la journée fut rythmée comme la précédente, mais cette fois Ezo n’avait plus en tête que le lendemain. Fatiguée par sa courte nuit de la veille, elle s’endormit promptement."
    jump clateau_ch2
