---
title: "TOOL-01 — Comprendre la compilation"
description: "Comprendre le rôle du compilateur et reconnaître ses limites."
---

**Objectif :** expliquer comment un fichier source est traduit et à quoi sert un diagnostic du compilateur. **Prérequis :** aucun. **État :** introduction théorique disponible ; étude et exercice à venir.

## Traduire le source

Un fichier source contient le programme écrit en C++. Le compilateur analyse ce texte et le traduit pour une cible, c’est-à-dire le processeur et l’environnement auxquels le programme est destiné.

Dans une construction classique en plusieurs étapes, on obtient un fichier objet : un fichier contenant notamment du code traduit, qui sera ensuite assemblé avec d’autres éléments pour former le programme. Cet assemblage sera étudié dans TOOL-02, consacré à l’édition de liens.

## Lire un diagnostic

Le compilateur peut signaler une erreur, par exemple lorsqu’une instruction ne respecte pas la syntaxe du langage. Le message indique généralement un fichier, une position et une explication.

Une erreur peut en provoquer plusieurs autres. Commence par comprendre la première cause identifiée, corrige-la, puis relance la compilation avant d’interpréter les messages suivants.

Un avertissement attire l’attention sur un problème potentiel, même si les outils parviennent à poursuivre la construction. Le module TOOL-03 expliquera comment les examiner.

## Comprendre la limite

Une compilation réussie ne prouve pas que le programme produit le résultat voulu. Le compilateur ne connaît pas ton intention : un calcul peut être accepté tout en utilisant la mauvaise formule.

La compilation n’exécute pas non plus le programme sur une carte. Le transfert et les vérifications sur microcontrôleur seront abordés séparément.

## À retenir

Le compilateur traduit et diagnostique. Les tests servent à vérifier des comportements attendus ; ils ne sont pas remplacés par une compilation réussie.

**Pour se repérer :** [vue d’ensemble de la chaîne de construction](../../du-source-au-programme/). Cette lecture est facultative.

**Suite disponible :** [initialiser une variable](../cpp-01/). TOOL-02 et TOOL-03 restent prévus ; aucun exercice exécutable n’est encore publié.
