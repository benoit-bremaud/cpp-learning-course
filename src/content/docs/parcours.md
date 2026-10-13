---
title: "Parcours progressif"
description: "Un parcours sans calendrier, avec des prérequis et des acquis explicites, du premier programme au C++ embarqué."
---

Le parcours se compose de **petits modules centrés sur une seule notion**, sans dates ni échéances. Tu peux revenir sur une fiche à tout moment. Les étapes ci-dessous donnent un ordre recommandé ; elles ne sont pas des chapitres à terminer d’un bloc.

**État : progression validée, cours en construction.** Un sujet prévu n’est pas une leçon disponible. Les identifiants restent stables : CPP-09 désigne une fiche, pas une obligation de la lire en neuvième position.

## Commencer avec les lectures disponibles

1. [TOOL-01 — Comprendre la compilation](../notions/tool-01/) : distinguer construction, comportement attendu et transfert sur la carte.
2. [Lire un premier programme](../notions/programme-minimal/) : reconnaître le bloc et distinguer affichage et statut de fin.
3. [Suivre plusieurs affichages](../notions/premiers-affichages/) : comprendre l’ordre des instructions et les sauts de ligne.
4. [CPP-01 — Initialiser une variable](../notions/cpp-01/) : suivre une valeur initiale puis son remplacement ; les compléments abordent le stock et la copie.
5. [CPP-09 — Exprimer une valeur constante](../notions/cpp-09/) : distinguer une donnée modifiable d’un entier constant.

Ce chemin est utilisable en lecture accompagnée : la syntaxe nécessaire y est expliquée. Les deux fiches de programme et d’affichage précèdent désormais l’étude détaillée des variables.

Le [voyant guidé](../exemple-voyant/) est une **découverte facultative** reliant besoin, UML, code et tests. Il n’est pas nécessaire de savoir réécrire sa fonction pour poursuivre les premières lectures. Sa maîtrise autonome vient après les conditions et les fonctions. La [vue de la construction](../du-source-au-programme/) est une référence à consulter au besoin.

## 1 — Se repérer dans un programme

**Prérequis :** aucun.

**Ordre des petits modules :** source, construction et exécution → squelette minimal d’un programme → instructions et blocs. Les détails de l’édition de liens et du débogage seront approfondis au moment utile.

**Acquis attendu :** distinguer un fragment d’un programme complet et expliquer l’ordre des instructions, sans devoir comprendre tout le langage.

**Disponible :** TOOL-01, le premier programme et les affichages successifs, avec la lecture du bloc de `main`. **À développer :** les approfondissements sur les blocs et la portée.

## 2 — Suivre une donnée

**Prérequis :** reconnaître une instruction et suivre leur ordre ; l’écriture d’une fonction n’est pas encore demandée.

**Ordre :** entier simple → initialisation → affectation → copie d’une valeur → `const` appliqué à un entier simple.

**Acquis attendu :** expliquer la valeur de chaque variable après chaque instruction et identifier celle qui ne peut pas être modifiée.

**Disponible :** CPP-01, ses deux compléments et CPP-09, avec les comparaisons entre affectation répétée et comptage, puis entre modification et redéclaration dans le même bloc. Les différentes syntaxes d’initialisation et `constexpr` restent des approfondissements ultérieurs.

## 3 — Calculer puis comparer

**Prérequis :** initialisation et affectation.

**Ordre :** expression et valeur calculée → opérations simples et parenthèses → mise à jour à partir d’une ancienne valeur → booléens → comparaisons. Les exemples numériques restent dans un domaine explicitement choisi ; les limites des types et conversions seront étudiées avant les usages qui en dépendent.

**Acquis attendu :** distinguer remplacer une valeur, calculer un nouveau total et poser une question dont la réponse est vraie ou fausse.

**Disponible :** [les premières expressions et l’addition](../notions/premieres-expressions/), avec le cas d’un plateau vide, puis [la soustraction et le stock restant](../notions/premieres-soustractions/) et [la multiplication de groupes identiques](../notions/premieres-multiplications/), puis [le regroupement des calculs avec les parenthèses](../notions/parentheses-calculs/) et [la division entière pour compter les kits complets](../notions/premieres-divisions/). La [mise à jour d’un compteur à partir de sa valeur courante](../notions/mise-a-jour-compteur/) complète cette étape. Les [premiers booléens](../notions/premiers-booleens/) introduisent ensuite les valeurs vraie et fausse. La [première comparaison stricte](../notions/premiere-comparaison/) calcule ensuite si un compteur dépasse une limite. La leçon [atteindre ou dépasser](../notions/atteindre-ou-depasser/) distingue ensuite `>` et `>=` au cas d’égalité. La leçon [en dessous ou au maximum](../notions/en-dessous-ou-au-maximum/) applique `<` et `<=` à une limite et à une boîte pleine. La leçon [égal ou différent](../notions/egal-ou-different/) complète les comparaisons avec `==` et `!=`, puis une correspondance d’identifiant entier. Aucun compteur autonome n’est supposé acquis à partir des seules affectations de CPP-01.

## 4 — Prendre une décision

**Prérequis :** booléens, comparaisons et blocs.

**Ordre :** `if` et `else` → cas d’égalité à un seuil → contrôle d’une entrée ou d’une limite.

**Acquis attendu :** expliquer le chemin suivi et distinguer une hypothèse sur les entrées d’un contrôle réellement effectué par le code.

**À développer comme modules autonomes.** Les exemples du voyant et du réservoir en offrent déjà une lecture guidée. C’est ici que sera développée la comparaison entre une limite constante et une limite effectivement contrôlée ; CPP-09 conserve pour l’instant l’avertissement simple.

## 5 — Organiser un traitement

**Prérequis :** valeurs, expressions, conditions et blocs.

**Ordre :** rôle d’une fonction → paramètres et arguments → résultat et `return` → portée locale → tests de cas représentatifs et de frontières.

**Acquis attendu :** expliquer puis modifier la fonction du voyant sans recopier une solution incomprise. Les bases de vérification ont commencé dès TOOL-01 ; cette étape apprend à les appliquer à une fonction.

**Disponible :** la référence guidée du voyant et son dépôt de pratique. **À développer :** les modules de fonctions et leurs exercices progressifs. Les mécanismes avancés d’exception ne sont pas requis pour ce premier objectif.

## 6 — Répéter et observer

**Prérequis :** conditions, mise à jour d’une valeur et fonctions simples.

**Ordre :** répétition avec une boucle → trace des valeurs → débogage pas à pas → état conservé entre traitements et durée de vie nécessaire à cet usage.

**Acquis attendu :** suivre plusieurs itérations et distinguer valeur actuelle, historique et état persistant. Un programme qui ne termine pas sa boucle doit pouvoir être expliqué.

**À développer.**

## 7 — Relier la logique au matériel

**Prérequis :** fonctions simples, répétition et distinction entre une décision et une action.

**Ordre :** carte, microcontrôleur et outils → lecture de la documentation et précautions électriques → `setup` et `loop` → sortie numérique → entrée numérique → observation série.

**Acquis attendu :** relier un comportement logiciel à une entrée ou une sortie et distinguer une valeur reçue d’une mesure physique fiable.

**À développer.** La carte et le câblage seront choisis avant la pratique. Les premières manipulations n’attendent pas la maîtrise des classes, pointeurs ou de RAII. Arduino et ESP-IDF seront distingués comme environnements logiciels ; leur choix dépendra de la carte et du besoin.

## 8 — Réagir sans bloquer

**Prérequis :** entrées/sorties, conditions et état conservé.

**Ordre :** différence entre attendre et vérifier le temps → types entiers adaptés au temps et leurs limites → temps écoulé → périodicité et débordement → états et transitions → anti-rebond.

**Acquis attendu :** expliquer comment plusieurs comportements progressent sans qu’une attente empêche les autres de réagir.

**À développer.** Une machine à états simple ne nécessite pas une classe par état. Les diagrammes d’états arrivent avec les transitions, pas avant.

## 9 — Structurer les données et les ressources

**Prérequis :** fonctions, portée locale et première compréhension de la durée de vie.

**Ordre :** tableaux et buffers → représentation mémoire utile → références et pointeurs → contrat d’une API C si nécessaire → classes et invariants → construction, destruction, propriété et RAII.

**Acquis attendu :** expliquer qui possède une ressource, qui peut l’utiliser et quand elle cesse d’exister.

**À développer.** Les rappels de C accompagnent un besoin précis ; un cours complet de C n’est pas un passage obligé. Les allocations et fonctionnalités standard seront évaluées selon la cible.

## 10 — Approfondir l’embarqué

**Prérequis :** les modules réellement utilisés par chaque sujet, indiqués dans sa future fiche. Les interruptions et la concurrence attendent notamment les durées de vie, le partage des données et le temps non bloquant.

**Sujets à découper :** UART, I²C, SPI, analogique et PWM ; interruptions et limites de `volatile` ; synchronisation ; ESP-IDF et FreeRTOS ; gestion des erreurs, watchdog, mémoire, observabilité et projets d’intégration.

**Acquis attendu :** justifier un contrat d’interface, traiter les erreurs prévues et vérifier le système sur ordinateur puis sur carte.

**À développer.** Ce groupe décrit la suite du parcours, pas un unique module ni un ordre imposant de maîtriser tous les protocoles avant une première interruption.

## Apprendre aussi à lire l’UML

La [méthode de conception](../methode-uml/) accompagne le parcours. Chaque exemple conserve sa conception avant le code et son bouton UML pour retrouver la correspondance.

| Notion étudiée | Vue et symboles introduits au moment utile |
| --- | --- |
| Instructions successives | Activité : début, actions, fin. |
| Conditions | Décision et chemins associés aux conditions. |
| Comportement dans le temps | États, événements et transitions. |
| Objets et collaborations | Classes ou séquences si la question de conception le justifie. |

L’UML n’est pas un examen préalable à l’apprentissage du C++. On explique les symboles nécessaires à l’exemple, puis on enrichit progressivement le vocabulaire.

## Rencontrer beaucoup d’exemples, progressivement

Pour une notion, commencer par un cas entièrement expliqué, puis une variation qui change un seul élément. Un autre contexte aide ensuite à transférer le raisonnement ; un cas limite ou une erreur volontaire arrive lorsqu’il éclaire une difficulté déjà compréhensible.

Les acquis indiqués sont des repères pour revenir sur une difficulté, pas des échéances ni des notes. Toute pratique de code reste dans un dépôt dédié, cloné dans ton IDE. Une leçon disponible ne signifie pas que son exercice est déjà publié.

## Piste pour plus tard : exercices interactifs et bilan personnel

**Reporté, non disponible.** Une future évolution pourrait proposer du code à trous, avec des réponses à choisir à la souris ou au clavier, puis un bilan des réussites et des difficultés par notion. Cette idée ne change pas l’ordre d’apprentissage actuel et ne bloque aucun module.

Les modalités restent à concevoir : entraînement avec explications, questionnaire de bilan, note éventuelle, historique et recommandations de révision. Reconnaître une réponse correcte ne suffit pas à établir une maîtrise autonome du code ; les notions non évaluées devront être distinguées des difficultés observées.

Aucun mode de stockage, compte utilisateur ou seuil de réussite n’est encore retenu. Pour l’instant, le site reste consacré à la lecture et la pratique se fait dans l’IDE depuis les dépôts dédiés.

## Pour plus tard : fiches récapitulatives téléchargeables

**Prévu pour une étape ultérieure, non disponible.** Des fiches de synthèse accompagneront le cours pour retrouver les notions essentielles lors des révisions. Leur format, leur découpage par module ou par thème et leur contenu précis restent à définir. Cette évolution est conservée dans le plan sans modifier les priorités actuelles.

## Références qui inspirent la progression

- [LearnCpp](https://www.learncpp.com/) : découpage en notions courtes, premières introductions séparées des approfondissements.
- [Programming: Principles and Practice Using C++, troisième édition](https://www.informit.com/store/programming-principles-and-practice-using-c-plus-plus-9780138308681), de Bjarne Stroustrup : progression des valeurs et calculs vers les fonctions, erreurs et programmes structurés ; sommaire consulté chez l’éditeur.
- [Exemples officiels Arduino](https://docs.arduino.cc/built-in-examples) : situations matérielles concrètes et distinctes.

Notre ordre est une adaptation pour le C++ embarqué avec conception UML. Il ne reproduit pas intégralement celui de ces ressources et ne suppose pas l’achat d’un livre.

## Bonnes pratiques et design patterns

**Décision pédagogique retenue :** appliquer les bonnes pratiques dès les premiers exemples, puis étudier les patterns à partir d’un besoin concret. Un pattern est une solution de conception réutilisable ; son nom n’est pas une raison de l’introduire dans un exercice.

Dès le début, nous expliquons les noms choisis, les valeurs initiales, le rôle de chaque fonction et les résultats attendus. Les principes de séparation des responsabilités apparaissent lorsque l’exemple permet de comprendre leur utilité.

Les futurs modules sur les patterns suivront un même raisonnement : problème, solution simple, nouvelle contrainte, alternatives, choix justifié, UML et correspondance avec le code. Ils examineront aussi les coûts sur la cible : mémoire, temps d’exécution et complexité de maintenance.

| Sujet prévu | Situation qui permet de le comprendre | Connaissances nécessaires |
| --- | --- | --- |
| RAII, un idiome du C++ | Libérer une ressource à la fin de la vie de son propriétaire. | Durée de vie, construction, destruction et propriété. |
| Adapter | Utiliser deux bibliothèques de capteurs qui n’exposent pas la même interface. | Fonctions, classes et contrats d’interface. |
| Strategy | Choisir entre plusieurs algorithmes de filtrage réellement nécessaires. | Fonctions, objets et choix du mécanisme de sélection. |
| Observer | Prévenir plusieurs destinataires d’un événement. | Callbacks, durée de vie et contexte d’exécution. |
| State | Comparer différentes implémentations d’un comportement dépendant de l’état. | Énumérations, transitions et machines à états. |

Une machine à états ne demande pas automatiquement une classe par état. Une fonction ou une sélection explicite peut être plus claire qu’un pattern. Chaque étude doit permettre d’expliquer pourquoi la solution retenue convient au besoin.

Ces orientations font partie du parcours retenu ; les études et les leçons correspondantes restent à développer.

## Revenir sur une difficulté

Une difficulté avec les interruptions peut demander un retour sur le partage de données. Une erreur de pointeur peut demander un retour sur les durées de vie. Un périphérique qui répond mal peut demander un retour sur son protocole avant toute modification du code.

Chaque future fiche détaillée conservera un identifiant stable, ses prérequis directs, un objectif et une preuve de compréhension.
