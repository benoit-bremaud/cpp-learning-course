---
title: "CPP-09 — Exprimer une valeur constante"
description: "Utiliser const pour exprimer qu’une valeur ne doit pas être modifiée."
---

**Objectif :** expliquer l’intention de `const` pour une variable simple. **Prérequis :** [CPP-01](../cpp-01/). **État :** exemples de lecture disponibles ; exercice autonome à venir.

## Identifier ce qui doit rester stable

Imagine une limite du nombre de mesures à conserver. Si cette limite ne doit pas changer pendant le traitement, le programme doit exprimer cette intention clairement.

Pour une variable simple telle qu’un entier, `const` indique que sa valeur ne peut pas être modifiée après son initialisation. Sa valeur de départ reste donc nécessaire : déclarer une variable constante ne signifie pas remettre son initialisation à plus tard.

## Faire vérifier cette intention

Si le code tente directement d’affecter une autre valeur à cet entier constant, le compilateur doit signaler le problème. Le nom de la variable peut expliquer son rôle ; `const` ajoute une contrainte que les outils peuvent contrôler.

Cette contrainte ne garantit pas que la valeur choisie est pertinente. Une limite constante mais incorrecte reste une erreur de conception.

## Observer une limite et un compteur

Le besoin fixe une limite fictive de **3 mesures**, inchangée pendant le traitement. Le compteur doit valoir **0**, puis **1** après une mise à jour. Déclarer cette limite ne contrôle pas automatiquement le compteur et ne réserve pas de mémoire pour les mesures.

![Initialiser la limite à trois, initialiser le compteur à zéro, puis affecter un au compteur.](/diagrams/examples/constant-limit.svg)

<a href="/diagrams/examples/constant-limit.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

Les actions se suivent de haut en bas. La limite reste à 3 : cette propriété stable est appelée un invariant. Les instructions suivantes seraient placées dans une fonction ; elles ne forment pas un programme complet.

```cpp
const int measurement_limit = 3;
int measurement_count = 0;
measurement_count = 1;
```

<details class="uml-panel" data-uml="constant-valid">
<summary>Voir la conception UML</summary>

**Quelle donnée reste fixe pendant la mise à jour ?**

![Diagramme de référence : Quelle donnée reste fixe pendant la mise à jour ?](/diagrams/examples/constant-limit.svg)

<a href="/diagrams/examples/constant-limit.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Élément de conception | Correspondance C++ |
| --- | --- |
| Initialiser la limite constante | `const int measurement_limit = 3;` |
| Initialiser le compteur | `int measurement_count = 0;` |
| Modifier seulement le compteur | `measurement_count = 1;` |

Après les initialisations, les valeurs sont 3 et 0. Après la dernière action, elles sont 3 et 1 : la limite reste inchangée.

</details>

`const` ajoute à l’entier la contrainte de ne pas changer après son initialisation. Le compteur, déclaré sans `const`, reste modifiable.

| Moment | Limite | Compteur |
| --- | --- | --- |
| Après les initialisations | 3 | 0 |
| Après l’affectation | 3 | 1 |

## Comparer deux erreurs différentes

Ce premier fragment est volontairement incorrect : il tente de modifier l’entier constant. Le compilateur le refuse ; il n’existe pas de résultat d’exécution valide à raconter.

```cpp
const int measurement_limit = 3;
measurement_limit = 4;
```

<details class="uml-panel" data-uml="constant-rejected">
<summary>Comprendre l’écart avec la conception</summary>

**Pourquoi ce fragment ne réalise-t-il pas la conception attendue ?**

![Diagramme de référence : Pourquoi ce fragment ne réalise-t-il pas la conception attendue ?](/diagrams/examples/constant-limit.svg)

<a href="/diagrams/examples/constant-limit.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Élément de conception | Correspondance C++ |
| --- | --- |
| Initialisation conforme | `const int measurement_limit = 3;` |
| Affectation interdite, absente du modèle valide | `measurement_limit = 4;` |

Conception attendue de référence : le diagramme complet impose de conserver la limite à 3. Ce fragment ne contient pas les actions concernant le compteur. La seconde instruction viole la contrainte const et est refusée à la compilation : aucun parcours exécuté menant à 4 ne doit être déduit de ce diagramme.

</details>

À l’inverse, ce second fragment est autorisé par C++, mais ne respecte pas le besoin fixé à 3 :

```cpp
const int measurement_limit = 30;
```

<details class="uml-panel" data-uml="constant-wrong">
<summary>Comprendre l’écart avec la conception</summary>

**Où la valeur choisie diverge-t-elle du besoin ?**

![Diagramme de référence : Où la valeur choisie diverge-t-elle du besoin ?](/diagrams/examples/constant-limit.svg)

<a href="/diagrams/examples/constant-limit.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Élément de conception | Correspondance C++ |
| --- | --- |
| Action attendue : initialiser à 3 | `const int measurement_limit = 3;` |
| Instruction réellement montrée : initialiser à 30 | `const int measurement_limit = 30;` |

Conception attendue de référence : seule la première action est comparée ici. Les actions sur le compteur ne figurent pas dans ce fragment. Celui-ci compile, mais produit 30 au lieu des 3 attendus dès l’initialisation ; le diagramme représente le besoin, pas son exécution fautive.

</details>

La valeur obtenue est 30, alors que 3 était attendu. `const` empêche une modification ultérieure ; il ne choisit pas la bonne valeur initiale.

## Une valeur connue pendant l’exécution

Une valeur constante peut être obtenue au démarrage du programme puis rester stable. `const` ne signifie donc pas nécessairement « valeur déjà connue lors de la compilation ».

Le calcul à la compilation, avec notamment `constexpr`, sera traité séparément. Il n’est pas nécessaire pour comprendre ce premier usage de `const`.

## Lien avec l’embarqué

Dans une conception de traitement de mesures, distingue la limite stable et le compteur qui évolue. Le choix de ce qui reste constant dépend du besoin : une limite réglable pendant le fonctionnement ne respecte pas le même contrat.

**À retenir :** pour une variable entière simple, `const` exprime l’interdiction de modifier sa valeur après son initialisation. Il ne remplace pas la réflexion sur la bonne valeur de départ.

## Plus tard

Les références et les pointeurs nécessitent de distinguer un objet constant d’un accès qui interdit certaines modifications. Cette nuance sera abordée après leurs modules dédiés. Elle n’est pas un prérequis de cette introduction.
