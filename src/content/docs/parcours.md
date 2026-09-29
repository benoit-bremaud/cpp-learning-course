---
title: "Parcours progressif"
description: "Des sujets courts et des prérequis explicites, du poste de travail à l’ESP32."
---

Le parcours se découpe en petits modules centrés sur une seule notion. Les familles ci-dessous servent à se repérer ; elles ne sont pas des chapitres à terminer d’un bloc.

**État : proposition à valider ensemble.** Les trois liens de la première partie ouvrent des introductions disponibles. Les autres sujets sont prévus, pas encore des leçons complètes.

## Construire les premières bases

| Famille | Notions principales | Point d’entrée |
| --- | --- | --- |
| Outils | Compilation, édition de liens, diagnostics, débogage, tests | [TOOL-01 : compilation](../notions/tool-01/) |
| C++ fondamental | Initialisation, types, conversions, conditions, fonctions, portée | [CPP-01 : initialisation](../notions/cpp-01/) |
| Objets constants | Intention et limites de `const` | [CPP-09 : objets constants](../notions/cpp-09/) |
| UML | Structure, interactions, activités et états | [Méthode de conception](../methode-uml/) |

## Comprendre les données et les objets

**Prévu.** Tableaux, chaînes, références et pointeurs ; classes et invariants ; construction et destruction ; durée de vie, ownership et RAII. L’objectif est d’expliquer qui possède une ressource, qui peut l’utiliser et quand elle cesse d’exister.

Les notions de C sont introduites à leur point d’utilisation : représentation mémoire, pointeurs, tableaux, structures et liaison avec une API C. Le C++ n’est pas présenté comme du C auquel on ajouterait seulement des classes.

## Passer au matériel

**Prévu.** Broches numériques, entrées et sorties, contraintes électriques, lecture de la documentation d’une carte et premier périphérique. La carte exacte et le câblage devront être choisis avant les manipulations.

On distingue la carte physique, le microcontrôleur, le framework logiciel et les outils. Arduino désigne un écosystème ; un ESP32 peut notamment être programmé avec un framework Arduino adapté ou avec ESP-IDF.

## Réagir sans bloquer

**Prévu.** Temps écoulé, tâches périodiques, débordement des compteurs, machines à états, anti-rebond et séparation de la logique métier des accès au matériel. Les diagrammes d’états deviennent le contrat des transitions autorisées.

## Communiquer avec les périphériques

**Prévu.** UART, I²C, SPI, acquisition analogique et PWM. Chaque sujet aborde le protocole, le contrat d’interface, les erreurs et une étude UML adaptée avant l’exercice.

## Maîtriser concurrence et ressources

**Prévu.** Interruptions, partage de données, limites de `volatile`, sections critiques et primitives de synchronisation ; programmation générique lorsque son intérêt est concret ; ESP-IDF et FreeRTOS sur une cible compatible.

L’accès concurrent n’est abordé qu’après les durées de vie, les machines à états et le temps non bloquant.

## Construire un système robuste

**Prévu.** Gestion des erreurs, watchdog, budgets mémoire, observabilité, tests sur ordinateur puis sur carte, et projets d’intégration. Les allocations dynamiques, exceptions et fonctionnalités standard sont évaluées selon les contraintes de la cible ; aucune interdiction universelle n’est supposée.

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

Ces sujets sont des orientations de futurs modules, pas des leçons disponibles ni un nouveau catalogue déjà validé.

## Revenir sur une difficulté

Une difficulté avec les interruptions peut demander un retour sur le partage de données. Une erreur de pointeur peut demander un retour sur les durées de vie. Un périphérique qui répond mal peut demander un retour sur son protocole avant toute modification du code.

Chaque future fiche détaillée conservera un identifiant stable, ses prérequis directs, un objectif et une preuve de compréhension.
