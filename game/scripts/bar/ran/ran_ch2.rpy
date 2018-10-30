label ran_ch2:
    pass
# TODONE Ezo est en militaire
$ezo_outfit = 'Mi'

scene bg Black
with dissolve
show chapter_ch2:
    yanchor 0.5 ypos 0.5
    xanchor 0.5 xpos 0.5
with dissolve
$renpy.pause(3, hard='True')

scene bg grenier
with dissolve
"Ezo se roulait dans ses draps à la lumière tamisée du matin qui venait de passer par la lucarne. Comme l’automne arrivait, le fait que les rayons du soleil pénètrent dans le bâtiment signifiait que la matinée était déjà bien avancée."
"Ezo attrapa ses draps pour se réchauffer. La tête emmitouflée dedans, elle rigola."
show ezo B4 S3 Y4 at left, xflip
with dissolve
ezo "Un jour de congé hein ? Ça fait tellement longtemps que je n’en ai pas eu un…"
show ezo B5 S3 Y1 at left, xflip
with dissolve
ezo "Attends voir…"
show ezo B1 S1 Y7 at left, xflip
with dissolve
ezo "Je n’en ai jamais eu, en fait !"
hide ezo
with dissolve
"Elle se délectait de ce moment paisible quand elle se souvint d’un seul coup de son rendez-vous avez Ran. Elle s’enfonça de plus en plus dans ses draps pendant qu’elle rougissait."
scene bg cuisine
with dissolve
"Sans prendre de grandes précautions, elle descendit en cuisine pour y chercher de quoi se sustenter. Elle avait dormi avec son uniforme cradingue, et avec ses cheveux en bataille on aurait dit qu’elle venait de rentrer du champ de bataille."
"Quand elle entendit les pas de Clateau dans l’escalier, elle s’empressa de remettre son uniforme en place et de faire comme si de rien n’était."
show clateau B2 S1 Y4 at right
with dissolve
clateau "Alors, déjà levée ?"
show ezo B2 S1 Y3 at left, xflip
with dissolve
ezo "J’ai rendez-vous avec Ran aujourd’hui, pour boire le thé."
show clateau B2 S3 Y4 at right
with dissolve
clateau "Oh, un rendez-vous galant, déjà ? Tu vas vite en besogne !"
show ezo B8 S1 Y8 at left, xflip
with dissolve
ezo "Absolument pas, idiot !"
show clateau B1 S1 Y4 at right
with dissolve
clateau "Je rigole, je rigole ! C’est une bien bonne chose que tu te fasses des amis. J’avais peur que tu ne t’en fasses pas."
show ezo B1 S1 Y2 at left, xflip
with dissolve
ezo "Bah, qu’est-ce que tu crois ? Que j’allais rester avec des vieux toute ma vie ?"
hide ezo
with dissolve
hide clateau
with dissolve
"Ezo détourna le regard et fit mine de bouder, mais Clateau conservait son sourire. Il avait passé les premières journées après l’arrivée d’Ezo à s’inquiéter."
"Après tant d’années dans l’armée, il avait peur de se réaction avec les autres filles de son âge. Au final, il n’en était rien, et Ezo semblait s’adapter rapidement à son nouvel environnement."
show clateau B1 S1 Y1 at right
with dissolve
clateau "J’avais prévu de te proposer d’aller au port, mais visiblement tu seras occupée… du coup, voilà ta paie de la semaine."
show ezo B1 S3 Y4 at left, xflip
with dissolve
ezo "Merci ! je ne savais pas qu’on était payé de manière hebdomadaire…"
"Ezo ouvrit l’enveloppe garnit des nouveaux billets de yens que le gouvernement japonais commençait tout juste à imprimer sur le modèle occidental."
show ezo B6 S2 Y7 at left, xflip
with dissolve
ezo "Qu’est-ce que c’est que tout ça ! Il y en a pas un peu trop ?"
show clateau B1 S2 Y3 at right
with dissolve
clateau "Mais non, c’est ta paye !"
show ezo B1 S2 Y1 at left, xflip
with dissolve
ezo "C’est très différent de ce que je gagnais à l’armée…"
show clateau B3 S2 Y2 at right
with dissolve
clateau "Même à l’époque, c’était sous-évalué."
show ezo B2 S2 Y1 Go at left, xflip
with dissolve
ezo "J’étais déjà contente d’être nourris et logée, à vrai dire…"
show ezo B1 S3 Y2 Go at left, xflip
with dissolve
ezo "En tout cas, merci."
show clateau B1 S1 Y4 at right
with dissolve
clateau "Qu’est-ce que tu vas en faire ?"
show ezo B4 S2 Y1 at left, xflip
with dissolve
ezo "Je ne sais pas trop…"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "je sais ! Je vais acheter un kimono pour aller voir Ran. Combien ça peut valoir ?"
show clateau B6 S2 Y2 at right
with dissolve
clateau "Euh… plusieurs centaines de yens."
show ezo B5 S2 Y7 at left, xflip
with dissolve
ezo "Ah !"
hide ezo
with dissolve
hide clateau
with dissolve
# TODONE Ezo est en serveuse
$ezo_outfit = 'Se'

scene bg rue
with dissolve
"Ezo était un peu déçue, mais elle n’avait pas trouvé ce qu’elle ferait de sa paye. Elle décida d’en faire usage plus tard, et se prépara plutôt à rendre visite à Ran."
"Sur le chemin, Ezo était perdue dans ses pensées. Elle alternait entre l’excitation de voir une amie, et le stress d’une nouvelle relation sociale, deux choses totalement nouvelles pour elle."
"Pendant le cours laps de temps où elle s’était accommodée à la vie de barmaid au restaurant, elle avait goûté pour la première fois de sa vie à un environnement calme et pacifique."
"On aurait pu dire qu’elle s’y était déjà très bien habituée, mais au fond d’elle-même, elle était encore remplie d’inquiétude et de questionnement. N’était-elle pas un simple soldat, un rebut de l’armée qu’on avait essayé de caser dans la vie civile ? Arriverait-elle à s’adapter ?"
"Tout en cogitant, elle percuta Tsugumi au détour d’une rue."
show ezo B8 Y5 at left, xflip
with dissolve
ezo "Regarde ou tu marches, espèce de con…"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Ah, tiens, c’est toi, Tsugumi ?"
show tsugumi B1 S2 Y6 at right
with dissolve
tsugumi "Oui, c’est moi ! J’ai bien cru que tu allais me frapper !"
show ezo B3 S3 Y2 at left, xflip
with dissolve
ezo "C’est pas l’envie qui manque mais je suis occupée. Mais dis-moi, je peux savoir ce que tu fais là ?"
show tsugumi B1 S3 Y1 at right
with dissolve
tsugumi "Je travaille, pardi !"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Encore ?"
show tsugumi B1 S1 Y4 at right
with dissolve
tsugumi "Bien sûr, encore… tsss, ces français, toujours en RTT…"
show ezo B6 S1 Y8 at left, xflip
with dissolve
ezo "Cette remarque est totalement anachronique !"
show tsugumi B1 S1 Y1 at right
with dissolve
tsugumi "Mais qu’est-ce que tu fais dehors ? Toi aussi tu t’es fait sucrer ton jour de repos ?"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Je suis invitée chez Ran pour boire le thé."
show tsugumi B4 S1 Y2 at right
with dissolve
tsugumi "Oooh, le passe-temps de jeune fille bourgeoise… Bien, excuse-moi, mais j’ai à faire !"
hide ezo
with dissolve
hide tsugumi
with dissolve
"Tsugumi reprit son chemin. Sa dernière phrase interloquait Ezo. Elle comprenait bien qu’elle l’avait dite de manière ironique, sans méchanceté, mais pourtant, c’était vrai. Ezo allait prendre le thé dans une maison bourgeoise."
show ezo B4 S2 Y3 at left, xflip
with dissolve
ezo "J’espère que je ne ferai pas tâche…"
hide ezo
with dissolve

"La maison de Ran était une belle et grande bâtisse traditionnelle japonaise. Tout en bois, cerclé d’une promenade externe, jardin avec un étang, bâtiment orienté nord-sud…"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Ça fait très « Heian », finalement…"
hide ezo
with dissolve
"Ezo n’osait pas plus approcher. Elle piétina devant la porte quand elle fut attrapée par Ran. Elle lui fit un grand sourire et prit la main d’Ezo de ses doigts graciles."
show ran B1 S1 Y2 at right
with dissolve
ran "Mademoiselle Ezo, vous voilà ! Je vous attendais."
show ezo B1 S3 Y4 at left, xflip
with dissolve
ezo "Bien le bonjour, Ran !"
show ran B1 S1 Y2 at right
with dissolve
ran "Vous n’osiez pas entrer ? Ne soyez pas aussi gênée, voyons ! Si vous continuer à être aussi gênée, les lecteurs vont finir par vous assimiler à un personnage de tsundere, ce serait regrettable."
show ezo B7 S2 Y8 at left, xflip
with dissolve
ezo "Mais, enfin !"
hide ezo
with dissolve
hide ran
with dissolve
# TODONE fondu en noir
scene bg Black
with dissolve

scene bg chambre
with dissolve
"Ran conduisit Ezo à sa chambre. Toute la maisonnée était baignée dans une atmosphère japonaise, et elle détonnait beaucoup avec le restaurant, qui lui était construit sur un modèle occidental d’Europe de l’Ouest."
"C’était la première fois qu’Ezo s’y retrouvait confronté directement. Quand elle se trouvait sur l’île dont elle porte le nom, finalement, elle n’avait été que dans des fortins ou des navires occidentaux."
"La chambre de Ran était bien évidemment une pièce japonaise à tatami. En entrant, on pouvait voir un tokonoma, ces petites alcôves où l’on expose des estampes ou d’autres objets d’arts."
"Là était affiché le caractère de la paresse, joliment calligraphié, ainsi que de l’ikebana, qui diffusait une bonne odeur de fleur dans la pièce."
show ezo B1 S3 Y1 at left, xflip
with dissolve
ezo "C’est très... féminin."
show ran B5 S1 Y3 at right
with dissolve
ran "Mais non voyons, c’est trois fois rien !"
"Ezo regardait la pièce, et elle percuta d’un seul coup."
show ezo B1 S3 Y7 at left, xflip
with dissolve
ezo "Mais, on est seule toutes les deux !"
show ran B1 S1 Y2 at right
with dissolve
ran "Bien évidemment, pourquoi ?"
show ezo B6 S2 Y1 at left, xflip
with dissolve
ezo "Je… je pensais que ce serait une cérémonie du thé avec plusieurs personnes…"
hide ezo
with dissolve
hide ran
with dissolve
"Ezo était soudainement gênée par sa méprise. Dans son engouement pour la découverte de nouvelles choses, elle ne s’était pas rendue compte que Ran l’avait entrainée dans son intimité."
show ran B2 S1 Y2 at right
with dissolve
ran "Si vous le voulez bien, nous allons commencer…"
hide ran
with dissolve
"Ezo s’assit de manière traditionnelle sur un des coussins, en attendant que Ran prépare le thé. Elle n’avait jamais participé à une cérémonie du thé, et finalement, être seule avec Ran la rendait encore plus tendue."
"Si elle avait été entourée d’autres personnes, elle aurait pu cacher son ignorance. Dans le cas présent, elle était obligée de se laisser guider pas à pas par Ran, ne sachant pas quoi faire."
"Quand Ran lui tendit sa tasse, Ezo fut très étonnée."
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Mais, c’est du thé noir !"
show ran B6 S1 Y8 at right
with dissolve
ran "Je suis désolée, je pensais vous faire quelque chose de plus européen, alors j’ai importé du thé russe…"
show ezo B2 S3 Y4 at left, xflip
with dissolve
ezo "C’est gentil à toi… mais si on part sur les boissons européennes, je suis plus café en fait."
show ezo B1 S2 Y1 at left, xflip
with dissolve
ezo "C’est les anglais qui boivent du thé noir."
show ran B6 S1 Y8 at right
with dissolve
ran "Aaah, veuillez excuser mon absence de connaissance dans le monde occidental !"
show ezo B1 S2 Y4 Go at left, xflip
with dissolve
ezo "Calme-toi, c’est très gentil d’avoir voulu me ménager !"
show ezo B2 S3 Y2 -Go at left, xflip
with dissolve
ezo "La prochaine fois, tu pourras faire du matcha, j’en ai déjà bu quand j’étais stationnée sur l’île d’Ezo."
show ran B1 S1 Y2 at right
with dissolve
ran "C’est vrai que vous êtes militaire… Mais vous n’aviez pas de nom avant qu’on vous nomme ainsi ?"
show ezo B4 S2 Y1 at left, xflip
with dissolve
ezo "Pas vraiment. Je suis orpheline de guerre et j’ai été pris comme enfant de troupe. On m’a traînée de bataille en bataille sans se soucier de mon sort."
"C’est à partir de la retraite à Hakodate qu’on a commencé à me surnommer « Ezo », vu que je faisais une grande promotion de la nouvelle « République d’Ezo » que les partisans du Shogun avaient fondé sur l’île."
show ran B4 S3 Y3 at right
with dissolve
ran "Vous n’avez point eu une vie facile ! Comme je vous plaint."
"Ezo souria. Ran, que l’on pouvait penser très embourgeoisée, derrière ses manières traditionnelles et sa grande paresse, cachait un caractère d’une grande gentillesse et était pleine d’empathie pour les autres."
show ezo B4 S3 Y2 at left, xflip
with dissolve
ezo "Toi, de ton côté, la guerre n’a pas été trop dure ? Tu viens d’une famille de samouraï il me semble, non ?"
show ran B4 S1 Y1 at right
with dissolve
ran "C’est extrêmement gênant de vous dire cela, mademoiselle Ezo, mais même si mon père est un samouraï, il a choisi de se ranger du côté de l’empereur pendant la guerre."
"Comme Ezo ne répondait pas, Ran commença à paniquer."
show ran B6 S1 Y8 at right
with dissolve
ran "Je sais que ce comportement a provoqué la chute du Shogun, mais comprenez-nous bien, nous n’avons pas spécialement d’intention de trahison à l’encontre du Shogun, nous voulions juste garantir à l’Empire…"
show ezo B4 S3 Y2 at left, xflip
with dissolve
ezo "Pas la peine de te justifier Ran, je n’ai pas de rancune ou quoi que ce soit. En tout cas pas contre toi."
show ran B4 S3 Y2 at right
with dissolve
ran "Vous êtes sûre ? Mon comportement égoïste vous a causé de nombreux problèmes…"
show ezo B5 S1 Y2 at left, xflip
with dissolve
ezo "Arrête Ran, ce n’est pas « ton » comportement ! Ce sont les faits du gouvernement, pas les tiens. Ça ne nous empêchera pas d’être amies."
hide ezo
with dissolve
hide ran
with dissolve
"Ran semblait soulagée en entendant ces paroles. Ezo la sentait stressée depuis le début. Au vu de son flegme, même stressée, elle ne changeait que peu de d’habitude, mais Ezo comprit alors pourquoi elle avait voulu changer le matcha par du thé noir."
"Ran avait voulu mettre Ezo dans de bonnes dispositions pour aborder le sujet, et son échec l’avait tendue. Maintenant qu’elle était rassurée, Ezi tenta de changer de sujet."
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Mais vu ta maison, tu dois être assez aisée, non ? Pourquoi tu travailles chez Clateau ?"
show ran B4 S1 Y1 at right
with dissolve
ran "Mon père sait pertinemment que la fin des samouraïs est proche. Il a décidé m’envoyer travailler pour préparer le jour où nous aurons définitivement perdu nos privilèges."
show ezo B4 S3 Y2 at left, xflip
with dissolve
ezo "C’est pragmatique…"
show ran B5 S1 Y1 at right
with dissolve
ran "Mais, aussi…"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Oui ?"
show ran B1 S1 Y2 at right
with dissolve
ran "Avec l’ouverture du pays, j’ai pu découvrir des contrées nouvelles, et tout cela m’intrigue grandement. J’aimerai tellement voyager ! Mais je dois pour cela pouvoir me débrouiller par moi-même avant."
"Ezo fut stupéfaite. Ran, si coincée en apparence, voulait donc voir le monde occidental ?"
show ezo B1 S3 Y4 at left, xflip
with dissolve
ezo "je suis sûre que tu y arriveras, Ran !"
show ran B1 S1 Y4 at right
with dissolve
ran "merci de votre soutiens, mademoiselle Ezo !"
hide ezo
with dissolve
hide ran
with dissolve
"Les filles étaient plus détendues pour la suite de leur rencontre. Comme Ran dormait beaucoup au travail, elles n’avaient pas tellement l’occasion de parler longuement. Ran se montrait très curieuse, et la sagacité d’Ezo pour répondre à ses questions les rapprochaient."

show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "je vais pas devoir tarder. La prochaine fois, tu n’auras qu’à venir dans ma chambre, je te ferai un café !"
show ran B1 S1 Y4 at right
with dissolve
ran "C’est bien la première fois que j’ai hâte de retourner sur mon lieu de travail !"
hide ezo
with dissolve
hide ran
with dissolve
# TODONE fondu en noir
scene bg Black
with dissolve

scene bg rue
with dissolve
"Ezo quitta la grande demeure guillerette. L’air frais du soir des débuts d’automne la rendait un peu nostalgique, mais elle était aussi toutes joyeuse de sa première vraie interaction sociale. Elle avait même réussi à réinviter Ran !"
show ezo B4 S2 Y1 at left, xflip
with dissolve
ezo "Il va falloir que j’apprenne à faire du café, cela dit…"
hide ezo
with dissolve
scene bg cuisine
with dissolve
"Dans le restaurant, Ezo avançait à tâtons. Clateau avait dû passer la journée à ranger le restaurant, elle ne voulait pas le déranger, pensant qu’il se reposait à l’étage."
show clateau B3 S1 Y4 at right
with dissolve
clateau "Bon retour. Ça s’est bien passé ?"
"Clateau l’avait attendu dans un coin de la cuisine, juste avant les escaliers. Ezo fit mine d’être surprise, mais elle se doutait bien qu’il s’inquiétait et qu’il l’attendait. Il le connaissait, à force."
show clateau B3 S1 Y1 at right
with dissolve
clateau "Alors, comment ça s’est passé ?"
show ezo B2 S3 Y2 at left, xflip
with dissolve
ezo "Bien, merci de t’inquiéter."
show clateau B5 S2 Y2 at right
with dissolve
clateau "Je ne m’inquiétais pas spécialement…"
show ezo B3 S2 Y4 at left, xflip
with dissolve
ezo "Mais bien sûr !"
show clateau B1 S1 Y1 at right
with dissolve
clateau "Je suis content que tu te sois fait une amie."
show ezo B4 S3 Y1 at left, xflip
with dissolve
ezo "Pour tout te dire… moi aussi."
hide ezo
with dissolve
hide clateau
with dissolve
scene bg grenier
with dissolve
"Dans sa chambre, Ezo se sentait à la fois fatiguée et soulagée.  Elle avait l’impression d’avoir fait un bond de géant en une seule journée. Après avoir vaguement laissé son uniforme dans un coin, elle se jeta sur lit et s’endormit rapidement."
# TODONE fondu en noir
scene bg Black
with dissolve

scene bg bar
with dissolve
"Le lendemain, Ran semblait plus active au travail qu’à l’accoutumée. Elle ne négligeait pas ses siestes pour autant, mais elle surprit l’assemblée plus d’une fois en étant éveillée à un moment où on ne l’attendait pas."
"De son côté, Ezo s’habituait assez vite à sa collègue, et le travail lui paraissait moins compliqué."
show tsugumi B1 S1 Y3 at right
with dissolve
tsugumi "Vous vous entendez vraiment bien, toutes les deux."
show ezo B5 S2 Y6 at left, xflip
with dissolve
ezo "À quoi tu vois ça, toi ? T’es déjà saoule ?"
show tsugumi B4 S1 Y4 at right
with dissolve
tsugumi "Déjà, oui. Et puis, je vous regarde depuis tout à l’heure, et c’est assez étonnant de voir une synergie entre vous deux, vu vos caractères. J’imaginais plus que tu serais une deuxième Yoshino."
show ezo B8 S1 Y2 at left, xflip
with dissolve
ezo "Comment ! Ça va pas ou quoi ?"
show tsugumi B2 S2 Y6 at right
with dissolve
tsugumi "Ouais, désolé, c’était un peu fort."
show ezo B4 S2 Y6 at left, xflip
with dissolve
ezo "Si elle nous avait entendue, on serait déjà transformée en hachis…"
show tsugumi B1 S2 Y1 at right
with dissolve
tsugumi "Mais ça ne change rien au fait que je n’imaginais pas un tandem entre la militaire et la bourgeoise !"
show ezo B1 S1 Y3 at left, xflip
with dissolve
ezo "On a plus de points communs que tu ne le crois !"
"Tsugumi se redressa pour fixer un long moment Ezo et Ran. Son regard visait précisément leurs bustes."
show ezo B6 S2 Y6 R2 at left, xflip
with dissolve
ezo "Ah ! Je sais à quoi tu penses ! C’est petit de ta part !"
show tsugumi B4 S1 Y1 at right
with dissolve
tsugumi "Bah non, en l’occurrence, question petitesse…"
hide ezo
with dissolve
hide tsugumi
with dissolve
"Ezo attrapa Tsugumi et lui mit un coup de boule pour lui faire cesser sa phrase."
show ezo B8 S1 Y8 at left, xflip
with dissolve
ezo "Tu peux parler !"
show ran B5 S1 Y7 at right
with dissolve
ran "Oh mon dieu, mademoiselle Ezo, mademoiselle Tsugumi saigne du nez."
show ezo B1 S1 Y3 at left, xflip
with dissolve
ezo "Je gère."
hide ezo
with dissolve
hide ran
with dissolve
"À ce moment, Akié pénètra dans la pièce, venant prendre sa pause."
show akie B5 S1 Y4 at right
with dissolve
akie "Salut tout le monde !"
show ezo B7 S3 Y2 Go at left, xflip
with dissolve
ezo "On peut pas gagner contre ça…"
hide ezo
with dissolve
show tsugumi B1 S1 Y3 at left, xflip
with dissolve
tsugumi "Bon…"
show akie B1 S1 Y2 at right
with dissolve
akie "Qu’est-ce qu’il y a ?"
hide tsugumi
with dissolve
hide akie
with dissolve
"Ezo et Tsugumi firent mine de rien et reprirent leurs occupations. Ran commençait doucement à émerger de son sommeil."
"Il était temps, car les clients du soir commençaient à s’accumuler. Contrairement aux jours d’avant, elle semblait bizarrement réactive. Elle donnait même des indications à Ezo sur les tables à servir et quand."
show yoshino B1 S1 Y1 at left, xflip
with dissolve
yoshino "Tu es bizarrement active, Ran. Habituellement tu aurai attendu que Sei ou Akié prennent leurs pauses pour leur refiler discrètement ton taff."
show ran B2 S1 Y1 at right
with dissolve
ran "Oui, mais voir des gens travailleurs comme mademoiselle Tsugumi ou mademoiselles Ezo m'a motivée."
show yoshino B5 S2 Y3 at left, xflip
with dissolve
yoshino "Et tu ne nies même pas en plus !"
show ran B1 S2 Y8 at right
with dissolve
ran "Mais c’est la vérité ! Mademoiselle Ezo est une vraie source d’inspiration pour moi !"
show yoshino B1 S1 Y1 at left, xflip
with dissolve
yoshino "À ce point ?"
show ran B1 S1 Y4 at right
with dissolve
ran "Mais oui mademoiselle Yoshino, mademoiselle Ezo a fait beaucoup d’effort pour en arriver là, et je ne peux point l’ignorer ! N’est-il pas, mademoiselle Ezo ?"
hide yoshino
with dissolve
show ezo B6 S2 Y1 R1 at left, xflip
with dissolve
ezo "Ah, euh, oui…"
hide ezo
with dissolve
hide ran
with dissolve
"Ezo, qui écoutait discrètement mais d’une oreille attentive ce que Ran disait, se mit à rougir fortement. Elle ne répondit qu’évasivement avant de partir vers le fond du café prétextant devoir servir les clients."
"Ezo était toute contente que Ran pense cela d’elle. À part Clateau, et c’était dit sur un ton paternaliste, elle n’avait jamais été le « modèle » de quelqu’un. Ces déclarations l’avaient toute chamboulé."
"Tsugumi buvait bière sur bière au comptoir et la soirée coulait lentement. Ezo servait avec nonchalance les plats, se calquant sur le rythme de Ran."
"Ce n’était pas trop du goût de Yoshino, qui voyait là la gangrène progressive de son seul élément actif dans le café."
"Elle essayait bien de les invectiver de temps en temps, mais comme les clients étaient quand même servit dans des temps convenables, elle n’osa pas faire de nouvelle scène."
"Finalement, en passant un plat un peu brusquement à Ran, cette dernière l’échappa."
show yoshino B8 S3 Y1 at right
with dissolve
yoshino "Ah bah bravo, Ran ! Tu peux pas être un tout petit peu tendue ? T’es pas en argile, que je sache !"
show ran B4 S3 Y2 at left, xflip
with dissolve
ran "Je, je suis désolée, mademoiselle Yoshino. Je ferai plus attention à l’avenir..."
show yoshino B8 S3 Y1 at right
with dissolve
yoshino "Franchement, qu’est-ce qu’on va faire de toi, hein !"
hide ran
with dissolve
show ezo B1 S2 Y2 at left, xflip
with dissolve
ezo "Yoshino, c’est juste un plat tombé par terre non ? J’ai l’ouïe fine, aujourd’hui j’ai entendu Sei tomber au moins trois fois par terre, et tu lui as rien dit."
show yoshino B5 S3 Y3 at right
with dissolve
yoshino "J’aimerai surtout que Ran fasse plus d’effort !"
show ezo B5 S1 Y2 at left, xflip
with dissolve
ezo "Mais elle en fait bien ! Elle a passé une bonne partie de son temps à me former, tu sais. Est-ce que je suis venu vous déranger toi ou Clateau pour vous demander des conseils ?"
show yoshino B4 S1 Y2 at right
with dissolve
yoshino "Non, c’est vrai…"
show ezo B1 S1 Y8 at left, xflip
with dissolve
ezo "Même si Ran est très, peut-être trop détendu, c’est pas en la brusquant que tu réglera le problème."
show yoshino B4 S2 Y1 at right
with dissolve
yoshino "Ouais, bon… Ça ira pour cette fois, mais faites plus attention. Je ne fais pas de sorbets pour qu’on les étale par terre."
hide ezo
with dissolve
hide yoshino
with dissolve
# TODONE fondu en noir
scene bg Black
with dissolve
scene bg salle
with dissolve

show ran B6 S1 Y6 at right
with dissolve
ran "Merci de votre aide, mademoiselle Ezo !"
show ezo B1 S3 Y3 at left, xflip
with dissolve
ezo "Faut dire que Ran abuse, aussi !"
show ran B1 S1 Y2 at right
with dissolve
ran "C’est bien la première fois que je vois quelqu’un tenir tête à notre sous-chef."
show ezo B5 S3 Y6 at left, xflip
with dissolve
ezo "J’ai eu un peu peur moi aussi en réalité… c’était surtout du bluff."
show ran B1 S1 Y4 at right
with dissolve
ran "C’était très impressionnant ! Je vous jure que je vous revaudrai cette faveur."
show ezo B7 S3 Y7 at left, xflip
with dissolve
ezo "Essaye d’être plus éveillée, la prochaine fois… je ne sais pas si mon petit cœur tiendra une autre rencontre…"
hide ezo
with dissolve
hide ran
with dissolve
"Tsugumi, qui était accoudé au bar, rouge à cause de l’alcool, marmonnait la tête dans son verre."
show tsugumi B2 S2 Y1 at right
with dissolve
tsugumi "Si Ran est plus éveillé et que tu la protèges, alors ça voudra dire que les disputes avec Yoshino vont venir ? Ce serait dommage…"
show ezo B1 S3 Y4 at left, xflip
with dissolve
ezo "Quoi, tu comptes arrêter de nous fréquenter ?"
show tsugumi B1 S2 Y1 at right
with dissolve
tsugumi "Pour sûr, non ! Mais une Ran somnolente, ça fait un peu parti du patrimoine du restaurant !"
hide ezo
with dissolve
show ran B2 S1 Y4 at left, xflip
with dissolve
ran "Eh bien, nous rentrons dans l’ère où mademoiselle Ezo me protégera, ce n’est pas plus mal !"
hide ran
with dissolve
hide tsugumi
with dissolve
"Ezo resta pensive. Elle était en train de s’intégrer au restaurant, de faire parti des habitudes de ceux qui le fréquente. Cela lui laissait une sensation bizarre, pas désagréable, une sensation d’avoir trouvé un foyer."
# TODONE fondu en noir
scene bg Black
with dissolve

# TODONE Ezo est en militaire
$ezo_outfit = 'Mi'

scene bg grenier
with dissolve
"Le prochain jour de repos arriva vite. Avant que Ran vienne, Ezo se préparait à la recevoir. Elle se tenait au milieu de sa chambre, les bras sur les hanches, et observait autour d’elle son environnement fait de culottes sales et de vielles bouteilles vides."
show ezo B7 S2 Y7 at left, xflip
with dissolve
ezo "Mon dieu, cet endroit est un vrai cloaque !"
hide ezo
with dissolve
"Pas que ça la dérangeait tant que ça, mais elle voulait vraiment donner une bonne image d’elle à Ran."
"Elle commença à fourrer ses affaires sales dans un sac. Elle comptait les trier sur le moment. Mais en voyant la quantité, elle décida de se contenter de planquer le sac dans un coin pour l’instant."
scene bg cuisine
with dissolve
"Ezo demanda aussi à Clateau des chaises supplémentaires, ainsi que le droit d’utiliser la machine à torréfier de la cuisine."
show clateau B2 S1 Y4 at right
with dissolve
clateau "Bien sûr que tu peux, bien sûr. Tu veux que je t’aide ?"
show ezo B1 S1 Y3 at left, xflip
with dissolve
ezo "Non merci. Je veux que ce soit moi qui le fasse."
show clateau B2 S1 Y4 at right
with dissolve
clateau "C’est bien d’être motivée."
show ezo B7 S3 Y2 at left, xflip
with dissolve
ezo "…"
show ezo B8 S1 Y8 at left, xflip
with dissolve
ezo "J’peux savoir pourquoi tu souris comme ça, andouille ?"
show clateau B2 S1 Y4 at right
with dissolve
clateau "Mais pour rien !"
show ezo B8 S1 Y2 at left, xflip
with dissolve
ezo "T’as pas intérêt à venir nous voir, hein ! Vieux lolicon !"
show clateau B2 S1 Y4 at right
with dissolve
clateau "Ne t’inquiète pas !"
hide ezo
with dissolve
hide clateau
with dissolve
"Ezo s’approcha du torréfacteur en faisant un petit signe à Clateau pour lui dire de s’éloigner. Elle pouvait faire quelque chose sans qu’on lui tienne la main, non ?"
"Devant la machine, elle empoigna une poignée de grains de café."
show ezo B7 S2 Y7 at left, xflip
with dissolve
ezo "Bon, comment ça marche en fait ?"
hide ezo
with dissolve
"Ezo n’avait jamais utilisé ce genre de machine, en réalité. Elle voulait impressionner Ran par sa maitrise d’une technique occidentale, mais elle ne savait pas vraiment comment faire. Dans la théorie, il suffisait de « griller » des grains de cafés, puis de les moudre et ensuite de faire du café. En théorie…"
show ezo B4 S2 Y1 at left, xflip
with dissolve
ezo "Allez, ça pourra pas être pire que ce dont j’ai l’habitude…"
hide ezo
with dissolve
"Ezo tortura la machine en ferraille pendant un bon moment. Elle passa le café vert, en espérant faire de beaux grains noirs, au goût prononcé."
"Mais ce qui en ressorti était d’une teinte maronnasse, peu ragoutante."
show ezo B6 S2 Y8 at left, xflip
with dissolve
ezo "merde, j’ai plus de temps…"
hide ezo
with dissolve
scene bg bar
with dissolve
"Ran arrivait en effet au même moment. Ezo alla l’accueillir en laissant là son échec."
show ran B5 S1 Y4 at right
with dissolve
ran "Ezo ! Je suis contente que tu m’ais invitée."
show ezo B2 S3 Y2 at left, xflip
with dissolve
ezo "Moi aussi, Ran."
show ezo B1 S2 Y4 at left, xflip
with dissolve
ezo "Pas trop dur de revenir au travail un jour de repos ?"
show ran B1 S1 Y3 at right
with dissolve
ran "Habituellement la simple pensée de ce fait m’aurai conduit directement vers la Terre Pure d’Amida, mais si c’est pour te retrouver, pas le moins du monde !"
show ezo B3 S3 Y1 R2 at left, xflip
with dissolve
ezo "Oh…"
show ran B2 S1 Y4 at right
with dissolve
ran "D’autant que, depuis la petite ruelle, j’ai pu apercevoir monsieur Clateau en slip qui étendait son linge, cette expérience a été plus qu’amusante."
show ezo B8 S1 Y8 -R1 at left, xflip
with dissolve
ezo "Quoi ?!"
show ezo B1 S2 Y4 Go at left, xflip
with dissolve
ezo "Ahem, je vais devoir régler ça plus tard. Je t’en prie, allons dans ma chambre. J’arrive avec le café."
hide ezo
with dissolve
hide ran
with dissolve
# TODONE fondu en noir
scene bg Black
with dissolve

scene bg grenier
with dissolve
"Ezo conduisit Ran dans sa chambre. Quant elle était militaire, elle avait eu l’habitude de vivre dans la crasse, cela ne la gênait plus. Mais là, elle espérait que cela ne dérangerait pas Ran."
"Dans la petite pièce poussiéreuse, Ezo tira une chaise, invitant Ran à s’assoir."
show ezo B4 S2 Y1 at left, xflip
with dissolve
ezo "Ça… ça ne te parait pas trop sale ?"
show ran B1 S1 Y2 at right
with dissolve
ran "Non, point du tout ! C’est même étonnamment occidental, comme chambre. Je ne pensais que seule la façade du bâtiment avait été refaite dans ce style."
show ezo B4 S2 Y3 at left, xflip
with dissolve
ezo "Oui, j’ai été assez surprise moi aussi, mais je suppose que je ne peux pas commenter ce que Clateau fait avec son argent…"
show ezo B1 S3 Y2 at left, xflip
with dissolve
ezo "Passons. Je vais te chercher le café."
hide ezo
with dissolve
hide ran
with dissolve
"Ezo descendit les escaliers et retourna en cuisine. Elle reprit la torréfaction, essaya tant bien que mal de rattraper son coup."
"Mais au final, le café avait toujours une allure et une odeur bizarre. Dépitée, elle se contenta de servir deux tasses."
"Peut-être par peur, elle n’osa même pas le gouter. Elle se contenta de le remonter et de le servir à Ran."
"On pouvait voir à ses mains pleines de tâches qu’elle avait essayé autant que possible, sans résultat."
"L’odeur qui parvenait aux narines d’Ezo ne la trompait cependant pas : il allait être infecte. Quand Ran prit sa tasse, Ezo savait déjà comment cela allait se terminer. Elle avait retrouvé des yeux tristes et baissait la tête."
show ran B5 S1 Y4 at right
with dissolve
ran "Oh, ton café est délicieux, Ezo."
show ezo B1 S2 Y4 at left, xflip
with dissolve
ezo "Hein ?"
hide ezo
with dissolve
hide ran
with dissolve
"Ezo était surprise. Elle porta sa tasse à ses lèvres pour se rendre compte que comme elle le pensait, c’était Ran qui lui mentait. Ezo n’en était pas soulagée pour autant, les manière douce et prévenantes de Ran lui pesaient sur la conscience."
show ezo B4 S1 Y3 at left, xflip
with dissolve
ezo "Ne te moque pas de moi, il est dégueu, n’est-ce pas ?"
show ran B4 S3 Y8 at right
with dissolve
ran "Mais non, que dis-tu !"
show ezo B4 S1 Y2 at left, xflip
with dissolve
ezo "Pas la peine de sauver les apparences, je sais bien que je l’ai raté."
show ran B1 S1 Y2 at right
with dissolve
ran "Mais je suis quand même très heureuse que tu as fait tous ces efforts pour moi !"
show ezo B4 S2 Y1 at left, xflip
with dissolve
ezo "Quand bien même… Ran, tu es une jeune fille de bonne famille, bien élevée… et je suis une petite militaire crasseuse, qui n’arrive même pas à faire un café correctement ! Je crois que je ne suis pas faite pour la vie civile…"
show ran B4 S3 Y2 at right
with dissolve
ran "Mais non…"
show ezo B4 S2 Y2 at left, xflip
with dissolve
ezo "Si on retire ton intérêt pour l’occident, qu’est-ce qui me retient auprès de toi, finalement ? Peut-être devrais-je demander à Clateau de me renvoyer dans l’amée…"
show ran B6 S3 Y8 at right
with dissolve
ran "Surtout pas !"
"C’était la première fois qu’Ezo entendait Ran élever la voix. Voyant qu’elle ne régissait plus, Ran se racla la gorge et reprit."
show ran B4 S1 Y2 at right
with dissolve
ran "Ahem, excuse-moi. Non, Ezo, je ne tiens pas à toi comme à un bibelot occidental que j’aurai collectionnée. Tu vaux beaucoup plus que ça pour moi !"
show ezo B1 S3 Y1 R1 at left, xflip
with dissolve
ezo "Mais je…"
show ran B1 S1 Y3 at right
with dissolve
ran "Tu as raté ton café, ce n’est pas si grave. Je comprends que ta rigidité de militaire te fait te morfondre sur tes échecs, mais tu n’en es plus une, Ezo. Si tu as des doutes, tu peux venir me parler. Je ne suis pas que ta collègue somnolente, je suis aussi ton amie… et même plus."
"Ezo avait les larmes aux yeux, et elle se contenta de sourire à Ran en retour. Celle-ci soupira et la prit dans ses bras. Elle resta un moment comme ça, puis revint à sa place en se mouchant bruyamment."
show ran B3 S3 Y4 at right
with dissolve
ran "Roh, Ezo, je pensais qu’on irait plus loin !"
show ezo B6 S3 Y8 at left, xflip
with dissolve
ezo "Mais !"
show ran B1 S1 Y4 at right
with dissolve
ran "Je plaisante !"
hide ezo
with dissolve
hide ran
with dissolve
"Ezo remarqua que Ran était beaucoup plus détendue quand elle était seule avec elle depuis quelques temps. C’était une personne calme en toute circonstances, mais elle avait une certaine manière d’être et de parler, toujours vouvoyant et faisant assez peu d’humour."
"Ezo venait de se rendre compte que Ran la tutoyait et s’autorisait quelques traits d’esprit quand elles étaient toutes les deux."
show ran B1 S1 Y2 at right
with dissolve
ran "La nuit commence à tomber, je vais devoir te laisser. Mon père serait furieux si je rentrais trop tard."
show ezo B2 S3 Y2 R1 at left, xflip
with dissolve
ezo "Je comprends… on se verra demain alors."
show ran B1 S1 Y4 at right
with dissolve
ran "Que tu es mignonne, quand tu rougis !"
show ezo B6 S2 Y8 at left, xflip
with dissolve
ezo "Grraaah, arrête !"
hide ezo
with dissolve
hide ran
with dissolve
# TODONE fondu en noir
scene bg Black
with dissolve

# TODONE Ezo est en serveuse
$ezo_outfit = 'Se'

scene bg bar
with dissolve
"Le lendemain, Tsugumi regardait Ezo et Ran avec un petit sourire narquois. Akié était à côté, et prenait sa pause."
show tsugumi B1 S1 Y2 at right
with dissolve
tsugumi "J’ai l’impression que tout se passe bien, entre eux deux."
show akie B1 S1 Y7 at left, xflip
with dissolve
akie "Ah bon ? Moi qui pensait qu’elles s’évitaient, depuis ce matin."
show tsugumi B1 S1 Y1 at right
with dissolve
tsugumi "Mais non mais non ! Elles se sont rapproché pendant leur dernier jours de repos, et maintenant elles sont un peu gênée une fois en public, n’est-ce pas ?"
hide akie
with dissolve
show ezo B4 S3 Y6 at left, xflip
with dissolve
ezo "Qu’est-ce que tu vas pas chercher, toi…"
"Au même moment, Ran qui somnolait à côté, finit par s’endormir, et posa sa tête sur l’épaule d’Ezo."
show ezo B4 S3 Y2 R1 at left, xflip
with dissolve
ezo "…"
show tsugumi B1 S1 Y2 at right
with dissolve
tsugumi "Ah, qu’est-ce que je disais !"
hide tsugumi
with dissolve
show akie B1 S1 Y7 R1 at right
with dissolve
akie "Oh…"

jump ran_ch3
