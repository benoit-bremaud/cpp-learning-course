---
title: "Parcours progressif"
description: "Des sujets courts et des prérequis explicites, du poste de travail à l’ESP32."
---

Le parcours se découpe en petits modules centrés sur une seule notion. Les familles ci-dessous servent à se repérer ; elles ne sont pas des chapitres à terminer d’un bloc.

**État : proposition à valider ensemble.** Les trois liens de la première partie ouvrent des introductions disponibles. Les autres sujets sont prévus, pas encore des leçons complètes.

## Construire les premières bases

| Famille | Notions principales | Point d’entrée |
| --- | --- | --- |
| Outils | Compilation, édition de liens, diagnostics, débogage, tests | [TOOL-01 : chaîne de compilation](../notions/tool-01/) |
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

## Revenir sur une difficulté

Une difficulté avec les interruptions peut demander un retour sur le partage de données. Une erreur de pointeur peut demander un retour sur les durées de vie. Un périphérique qui répond mal peut demander un retour sur son protocole avant toute modification du code.

Chaque future fiche détaillée conservera un identifiant stable, ses prérequis directs, un objectif et une preuve de compréhension.
