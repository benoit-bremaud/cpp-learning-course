---
title: "CPP-01 — Initialiser une variable"
description: "Distinguer déclaration, initialisation et affectation."
---

**Objectif :** distinguer la valeur initiale d’une variable et une modification ultérieure. **Prérequis :** [TOOL-01](../tool-01/). **État :** introduction théorique disponible ; étude et exercice à venir.

## Donner une première valeur

Imagine un compteur du nombre de mesures reçues. Au début, aucune mesure n’a été reçue : sa valeur initiale est zéro. Après réception d’une mesure, le programme modifie cette valeur.

L’**initialisation** établit la valeur de départ. L’**affectation** remplace ensuite la valeur d’une variable qui existe déjà. Ces deux opérations correspondent à des moments différents.

## Distinguer les mots

| Terme | Rôle |
| --- | --- |
| Déclaration | Introduire un nom et préciser ses propriétés, notamment son type. |
| Initialisation | Établir la valeur initiale lors de la création de la variable. |
| Affectation | Donner une nouvelle valeur à une variable déjà créée. |

Une même instruction peut déclarer une variable, la créer et l’initialiser. La distinction entre déclaration et définition sera approfondie avec l’organisation du programme en plusieurs fichiers.

## Ne pas supposer une valeur zéro

Un entier local ordinaire, créé à l’intérieur d’une fonction sans valeur initiale explicite, ne reçoit pas automatiquement zéro. Une fonction est une partie nommée du programme qui effectue un traitement ; elle sera étudiée dans CPP-07.

Pour notre compteur, choisis explicitement zéro comme valeur de départ. Une valeur observée par hasard lors d’un essai ne constitue pas une garantie du langage.

## Lien avec l’embarqué

Initialiser le compteur des mesures ne lance pas le capteur. Cela établit seulement l’état de départ du programme. La configuration du matériel est une action distincte, qui apparaîtra dans l’étude de l’exercice concerné.

**À retenir :** une valeur initiale doit être choisie selon le sens de la donnée. Zéro convient au nombre de mesures reçues au démarrage ; il ne remplace pas automatiquement une mesure absente.

## Plus tard

Les formes d’initialisation, les conversions numériques et les différentes durées de stockage seront étudiées dans leurs modules dédiés. Elles ne sont pas des prérequis pour cette introduction.

**Suite :** [exprimer une valeur constante](../cpp-09/). Les exemples exécutables seront disponibles dans le dépôt de pratique avec leur étude UML validée.
