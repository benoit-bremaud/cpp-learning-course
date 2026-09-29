---
title: "CPP-01 — Initialiser une variable"
description: "Distinguer déclaration, initialisation et affectation."
---

**Objectif :** distinguer l’apparition d’un objet et la modification de sa valeur. **Prérequis :** [TOOL-01](../tool-01/). **État :** introduction théorique disponible ; étude et exercice à venir.

## Donner une valeur initiale

L’initialisation établit l’état initial d’un objet. L’affectation modifie la valeur d’un objet qui existe déjà. Cette différence devient essentielle lorsqu’un objet doit respecter un invariant dès sa construction, par exemple une mesure accompagnée de son unité.

Une déclaration introduit un nom et ses propriétés. Certaines déclarations sont aussi des définitions et créent un objet ; d’autres annoncent un élément défini ailleurs. Ces termes ne sont pas interchangeables.

## Ne pas supposer une valeur zéro

Un entier local de durée de stockage automatique, déclaré sans initialiseur, n’obtient pas systématiquement la valeur zéro. Utiliser sa valeur avant de l’avoir correctement établie ne constitue pas un programme fiable. Les règles exactes des valeurs indéterminées ou erronées dépendent notamment de la version du langage.

À l’inverse, les objets de durée de stockage statique suivent des règles d’initialisation différentes. Évite de généraliser à partir d’un seul essai dans un débogueur.

## Comprendre les accolades

L’initialisation par accolades aide notamment à détecter certaines conversions réductrices. Elle ne signifie pas que tous les types se construisent toujours de la même manière : les classes et leurs constructeurs introduisent des règles supplémentaires qui seront étudiées séparément.

Choisir une forme d’initialisation exige de comprendre le type et le contrat de l’objet, pas seulement de reproduire une ponctuation.

## Lien avec l’embarqué

Un état initial explicite rend le démarrage plus facile à raisonner. Il ne suffit toutefois pas d’initialiser une variable représentant une sortie pour configurer la broche physique correspondante. L’état logiciel et l’état du périphérique sont deux éléments à relier dans la conception.

**À retenir :** la valeur initiale appartient au contrat de l’objet. Une affectation ultérieure ne répare pas une utilisation qui aurait eu lieu trop tôt.

**Suite :** [objets constants et intention](../cpp-09/). Les exemples exécutables seront publiés dans le dépôt de pratique avec leur étude UML.


## Pour approfondir

[Projet de norme C++ : dcl.init](https://eel.is/c++draft/dcl.init) — référence technique en anglais ; le projet de norme évolue et doit être distingué de la version du langage choisie pour un exercice.
