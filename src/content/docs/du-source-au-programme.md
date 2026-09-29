---
title: "Vue d’ensemble — Du source au programme"
description: "Distinguer compilation, édition de liens et transfert sur la cible."
---

Cette vue d’ensemble situe les étapes. Elle ne remplace pas leurs modules spécialisés et ne demande pas de maîtriser tous les termes dès maintenant.

## Le source n’est pas le programme exécuté

Un fichier C++ contient une description destinée aux outils et aux humains. Le processeur exécute des instructions machine. La chaîne de construction transforme les sources et assemble les éléments nécessaires pour produire un programme adapté à une cible.

## Une traduction par unité

Le prétraitement traite notamment les inclusions et les directives conditionnelles. Une unité de traduction correspond, de manière simplifiée, au contenu résultant d’un fichier source après ce traitement. Le compilateur analyse le programme et peut diagnostiquer des erreurs de syntaxe ou de types. La production de code machine passe généralement aussi par une étape d’assemblage.

Les fichiers objets ne constituent pas nécessairement un programme complet : ils peuvent faire référence à des fonctions définies dans d’autres unités.

## Assembler les définitions

L’éditeur de liens combine les fichiers objets et les bibliothèques. Une fonction déclarée et appelée, mais dont aucune définition nécessaire n’est fournie, peut produire une erreur à cette étape. Une déclaration permet de connaître un contrat ; elle ne remplace pas l’implémentation.

Toutes les violations du langage ne sont pas nécessairement détectées. Une construction réussie n’est donc pas une preuve de correction.

## Choisir une cible

Un programme construit pour ton ordinateur n’est pas automatiquement exécutable sur un ESP32. Architecture du processeur, conventions de communication entre éléments compilés, bibliothèques et organisation mémoire interviennent dans le résultat. Une chaîne de compilation croisée fonctionne sur une machine et produit du code pour une autre cible.

Pour un microcontrôleur, la construction peut produire plusieurs artefacts destinés à la mémoire flash. Le transfert sur la carte est une étape distincte de la compilation. La réussite du transfert ne prouve pas davantage le bon fonctionnement du programme.

## Retenir les distinctions

| Étape | Question principale |
| --- | --- |
| Compilation | Cette unité peut-elle être traduite pour la cible choisie ? |
| Édition de liens | Les éléments requis peuvent-ils être assemblés ? |
| Transfert | Les artefacts ont-ils été écrits sur la carte ? |
| Exécution et tests | Le comportement respecte-t-il le contrat ? |

Le diagnostic utile est le premier message qui explique une cause, pas nécessairement la dernière ligne affichée par l’IDE.

**Suite :** [étudier la compilation](../notions/tool-01/). La future pratique permettra de distinguer volontairement plusieurs catégories de diagnostics à partir d’une étude validée.
