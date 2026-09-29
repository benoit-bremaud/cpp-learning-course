---
title: "CPP-09 — Exprimer une valeur constante"
description: "Comprendre ce que garantit const et ce qu’il ne garantit pas."
---

**Objectif :** expliquer les limites de `const`. **Prérequis :** [CPP-01](../cpp-01/). **État :** introduction théorique disponible ; étude et exercice à venir.

## Exprimer une intention

Qualifier un objet avec `const` restreint les modifications autorisées. Une limite configurée au démarrage, puis seulement consultée, peut ainsi porter une intention claire : le traitement ne doit pas la réaffecter.

`const` participe au système de types. Une tentative de modification directement interdite par ce type doit être diagnostiquée ; ce n’est pas seulement une convention de nommage.

## Distinguer objet et accès

Une référence vers un objet constant et une référence constante au sens courant de « valeur qui ne change jamais » ne sont pas des concepts interchangeables. Un accès par référence à `const` empêche certaines modifications par cet accès ; l’objet sous-jacent peut parfois être modifié par un autre accès autorisé s’il n’est pas lui-même constant.

Les pointeurs ajoutent deux questions : peut-on changer l’adresse conservée, et peut-on modifier l’objet pointé ? Le module consacré aux pointeurs séparera explicitement ces deux propriétés.

## Ne pas confondre avec constexpr

Une valeur `const` peut être obtenue pendant l’exécution. `const` seul ne garantit donc pas qu’elle soit utilisable dans tous les contextes exigeant une expression constante. `constexpr` introduit d’autres exigences ; il sera étudié avec les calculs à la compilation.

## Lien avec la conception

L’étude doit préciser quelles données restent stables après construction et quelles opérations peuvent changer l’état. Le mot-clé aide à exprimer une partie de ce contrat ; il ne décrit pas à lui seul un invariant métier complet.

En embarqué, `const` ne garantit ni un placement particulier en mémoire flash, ni une synchronisation entre tâches. Ces sujets dépendent de la chaîne de compilation, de la cible et des mécanismes de concurrence.

**À retenir :** demande toujours « qu’est-ce qui est constant, et à travers quel accès ? ». La réponse est plus utile que l’idée vague de « variable protégée ».


## Pour approfondir

[Projet de norme C++ : dcl.type.cv](https://eel.is/c++draft/dcl.type.cv) — référence technique en anglais ; le projet de norme évolue et doit être distingué de la version du langage choisie pour un exercice.
