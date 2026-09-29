---
title: "CPP-09 — Exprimer une valeur constante"
description: "Utiliser const pour exprimer qu’une valeur ne doit pas être modifiée."
---

**Objectif :** expliquer l’intention de `const` pour une variable simple. **Prérequis :** [CPP-01](../cpp-01/). **État :** introduction théorique disponible ; étude et exercice à venir.

## Identifier ce qui doit rester stable

Imagine une limite du nombre de mesures à conserver. Si cette limite ne doit pas changer pendant le traitement, le programme doit exprimer cette intention clairement.

Pour une variable simple telle qu’un entier, `const` indique que sa valeur ne peut pas être modifiée après son initialisation. Sa valeur de départ reste donc nécessaire : déclarer une variable constante ne signifie pas remettre son initialisation à plus tard.

## Faire vérifier cette intention

Si le code tente directement d’affecter une autre valeur à cet entier constant, le compilateur doit signaler le problème. Le nom de la variable peut expliquer son rôle ; `const` ajoute une contrainte que les outils peuvent contrôler.

Cette contrainte ne garantit pas que la valeur choisie est pertinente. Une limite constante mais incorrecte reste une erreur de conception.

## Une valeur connue pendant l’exécution

Une valeur constante peut être obtenue au démarrage du programme puis rester stable. `const` ne signifie donc pas nécessairement « valeur déjà connue lors de la compilation ».

Le calcul à la compilation, avec notamment `constexpr`, sera traité séparément. Il n’est pas nécessaire pour comprendre ce premier usage de `const`.

## Lien avec l’embarqué

Dans une conception de traitement de mesures, distingue la limite stable et le compteur qui évolue. Le choix de ce qui reste constant dépend du besoin : une limite réglable pendant le fonctionnement ne respecte pas le même contrat.

**À retenir :** pour une variable entière simple, `const` exprime l’interdiction de modifier sa valeur après son initialisation. Il ne remplace pas la réflexion sur la bonne valeur de départ.

## Plus tard

Les références et les pointeurs nécessitent de distinguer un objet constant d’un accès qui interdit certaines modifications. Cette nuance sera abordée après leurs modules dédiés. Elle n’est pas un prérequis de cette introduction.
