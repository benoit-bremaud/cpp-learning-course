---
title: "Premières soustractions — calculer ce qu’il reste"
description: "Calculer un reste, suivre les quantités et repérer une inversion des opérandes."
---

**Objectif :** calculer une quantité restante et expliquer pourquoi la position des deux quantités compte. **Prérequis :** [comprendre une expression et une addition](../premieres-expressions/).

**Disponible :** quatre exemples de lecture et leurs cartes UML. Le projet de pratique autonome à cloner n’est pas encore publié.

## Partir du besoin : combien reste-t-il de composants ?

Un atelier dispose de **12 composants** et en utilise **5**. Nous voulons calculer le nombre restant : **7**. La règle du besoin est « quantité initiale moins quantité utilisée ».

Dans les cas corrects, les quantités sont connues, comprises entre 0 et 20, et on n’utilise pas plus de composants qu’on en possède. C’est une hypothèse de départ, **pas un contrôle effectué par le code**. Les conditions permettant de vérifier une demande seront étudiées plus tard.

Chaque extrait se lit indépendamment, à l’intérieur du corps de `main`. Il ne constitue pas un programme complet. Les tableaux décrivent les valeurs ; les extraits n’affichent rien et ne détectent aucun retrait matériel.

## 1 — Soustraire deux quantités connues

Nous prévoyons de calculer **12 moins 5**, puis de créer `remaining_count`, le nombre de composants restants, avec le résultat **7**.

![Activité : calculer 12 moins 5, puis initialiser remaining_count à 7.](/diagrams/examples/subtraction-literal.svg)

<a href="/diagrams/examples/subtraction-literal.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

Le point noir marque le début de l’activité UML. Les rectangles arrondis décrivent les actions et les flèches leur enchaînement. Le symbole final termine ce fragment ; il n’ajoute pas une instruction `return`.

<!-- example:subtraction-literal -->
```cpp
int remaining_count = 12 - 5;
```

<details class="uml-panel" data-uml="subtraction-literal">
<summary>Voir la conception UML</summary>

![Activité : calculer 12 moins 5, puis initialiser remaining_count à 7.](/diagrams/examples/subtraction-literal.svg)

<a href="/diagrams/examples/subtraction-literal.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Conception attendue | Correspondance avec le code |
| --- | --- |
| Calculer le reste | `12 - 5` produit `7`. |
| Initialiser le résultat | La déclaration crée `remaining_count` avec `7`. |

Le diagramme sépare le calcul et l’initialisation pour expliquer le raisonnement. Une seule déclaration C++ peut réaliser ces deux actions ; aucune variable intermédiaire n’est ajoutée.

</details>

L’opérateur `-` soustrait ici **le second opérande au premier**. Dans l’expression `12 - 5`, 12 est la quantité dont on part, 5 celle qu’on retire. Le résultat 7 initialise la nouvelle variable.

Contrairement à l’addition de ces petits entiers, intervertir les deux quantités ne donne pas le même résultat. Nous examinerons cette erreur après les cas corrects.

## 2 — Donner un nom aux deux quantités

Gardons les mêmes données, mais nommons-les : `initial_count` représente les 12 composants de départ ; `used_count` représente les 5 utilisés. Nous créons une troisième variable pour conserver le reste.

Le besoin est de conserver **12 et 5** dans les deux premières variables et d’obtenir **7** dans `remaining_count`.

![Activité : initialiser les quantités à 12 et 5, calculer leur différence et conserver 7.](/diagrams/examples/subtraction-named.svg)

<a href="/diagrams/examples/subtraction-named.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:subtraction-named -->
```cpp
int initial_count = 12;
int used_count = 5;
int remaining_count = initial_count - used_count;
```

<details class="uml-panel" data-uml="subtraction-named">
<summary>Voir la conception UML</summary>

![Activité : initialiser les quantités à 12 et 5, calculer leur différence et conserver 7.](/diagrams/examples/subtraction-named.svg)

<a href="/diagrams/examples/subtraction-named.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Conception attendue | Correspondance avec le code |
| --- | --- |
| Initialiser les quantités | Les deux premières déclarations donnent `12` et `5`. |
| Calculer le reste | `initial_count - used_count` donne `7`. |
| Conserver le résultat | La dernière déclaration initialise `remaining_count`. |

Le diagramme sépare le calcul et l’initialisation pour expliquer le raisonnement. Une seule déclaration C++ peut réaliser ces deux actions ; aucune variable intermédiaire n’est ajoutée.

</details>

La dernière expression retrouve les valeurs 12 et 5 pour calculer 7. **Lire ces deux variables ne les modifie pas.** Le nom `initial_count` continue donc à désigner la quantité de départ, même après le calcul du reste.

| Après l’instruction | `initial_count` | `used_count` | `remaining_count` |
| --- | --- | --- | --- |
| Première déclaration | 12 | Pas encore créée | Pas encore créée |
| Deuxième déclaration | 12 | 5 | Pas encore créée |
| Déclaration du reste | 12 | 5 | 7 |

Ce code calcule une nouvelle donnée ; il ne remplace pas la valeur de `initial_count`. La mise à jour d’une même variable à partir de son ancienne valeur viendra dans une autre leçon.

## 3 — Utiliser exactement tout le stock

Changeons une seule donnée : cette fois, **12 composants sont utilisés sur les 12 disponibles**. Le reste attendu est **0**. Zéro signifie ici « aucun composant restant », pas « quantité inconnue ».

![Activité : initialiser les deux quantités à 12, calculer leur différence et conserver zéro.](/diagrams/examples/subtraction-empty.svg)

<a href="/diagrams/examples/subtraction-empty.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:subtraction-empty -->
```cpp
int initial_count = 12;
int used_count = 12;
int remaining_count = initial_count - used_count;
```

<details class="uml-panel" data-uml="subtraction-empty">
<summary>Voir la conception UML</summary>

![Activité : initialiser les deux quantités à 12, calculer leur différence et conserver zéro.](/diagrams/examples/subtraction-empty.svg)

<a href="/diagrams/examples/subtraction-empty.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Conception attendue | Correspondance avec le code |
| --- | --- |
| Initialiser les quantités | `initial_count` et `used_count` reçoivent chacun `12`. |
| Calculer le reste | `initial_count - used_count` donne `0`. |
| Conserver le résultat | `remaining_count` est initialisée à `0`. |

Le diagramme sépare le calcul et l’initialisation pour expliquer le raisonnement. Une seule déclaration C++ peut réaliser ces deux actions ; aucune variable intermédiaire n’est ajoutée.

</details>

| Après l’instruction | Quantité initiale | Quantité utilisée | Reste |
| --- | --- | --- | --- |
| Première déclaration | 12 | Pas encore créée | Pas encore créé |
| Deuxième déclaration | 12 | 12 | Pas encore créé |
| Déclaration du reste | 12 | 12 | 0 |

La formule n’a pas changé. Elle traite aussi ce cas où tout le stock est utilisé : **12 − 12 = 0**. Les deux variables d’entrée conservent leurs valeurs.

## 4 — Repérer une formule inversée

Revenons au besoin initial : **12 disponibles, 5 utilisés, 7 attendus**. Le diagramme de référence reste celui du deuxième exemple : soustraire la quantité utilisée à la quantité initiale.

**Erreur volontaire :** nous conservons les mêmes données, mais échangeons les positions des noms dans la dernière expression.

<!-- example:subtraction-reversed -->
```cpp
int initial_count = 12;
int used_count = 5;
int remaining_count = used_count - initial_count;
```

<details class="uml-panel" data-uml="subtraction-reversed">
<summary>Comprendre l’écart avec la conception</summary>

**Conception attendue : 7 ; résultat du code inversé : −7.** Ce diagramme décrit le calcul attendu, qui donne 7. Il ne représente pas l’exécution du code inversé : celui-ci calcule −7.

![Activité : initialiser les quantités à 12 et 5, calculer leur différence et conserver 7.](/diagrams/examples/subtraction-named.svg)

<a href="/diagrams/examples/subtraction-named.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Conception attendue | Correspondance avec le code |
| --- | --- |
| Garder les quantités 12 et 5 | Les deux premières déclarations sont correctes. |
| Calculer quantité initiale moins quantité utilisée | L’expression fait l’inverse : `used_count - initial_count`. |
| Obtenir un reste de 7 | Le code initialise en réalité `remaining_count` à `-7`. |


</details>

Ce fragment **compile**, puis calcule **5 − 12 = −7**. Le nombre −7 est inférieur à zéro et peut être représenté par `int`. Il ne signifie pas qu’un atelier possède physiquement « moins sept composants » : ici, il révèle une formule qui ne respecte pas le besoin.

| Vérification | Résultat |
| --- | --- |
| Les noms sont-ils déclarés avant leur utilisation ? | Oui. |
| La soustraction est-elle autorisée en C++ ? | Oui. |
| Quelles valeurs conservent les entrées ? | `initial_count` vaut 12 ; `used_count` vaut 5. |
| Quelle valeur reçoit `remaining_count` ? | −7. |
| Le résultat attendu de 7 est-il obtenu ? | Non. |

**Correction :** rétablir `initial_count - used_count`, comme dans le deuxième exemple. Les quantités 12 et 5 étaient bonnes ; les échanger ou renommer les variables masquerait l’erreur au lieu de corriger la formule.

Le compilateur vérifie des règles du langage. Il ne connaît pas notre intention de calculer un stock restant. C’est la comparaison entre le besoin, la conception et le résultat qui permet ici de trouver l’erreur.

## Vérifier sa compréhension

Essaie de répondre avant de relire les tableaux :

- Quelle quantité faut-il placer à gauche de `-` pour calculer le reste ?
- La création de `remaining_count` transforme-t-elle `initial_count` en 7 ?
- Pourquoi zéro est-il correct lorsqu’on utilise les 12 composants ?
- Pourquoi le dernier fragment peut-il compiler sans donner le bon reste ?

**Repères pour te corriger :** la quantité initiale se place à gauche ; les entrées restent inchangées ; utiliser tout le stock laisse zéro ; la formule inversée est autorisée par C++ mais ne respecte pas le besoin.

**À retenir :** choisir une opération ne suffit pas. Il faut aussi donner le bon rôle à chaque opérande et vérifier le résultat attendu.

**Suite :** [compter des groupes identiques avec la multiplication](../premieres-multiplications/). Les parenthèses, la division et la mise à jour d’une variable suivront dans le [parcours progressif](../../parcours/). Les fiches récapitulatives téléchargeables sont prévues pour plus tard.

## Références

Les règles de [soustraction](https://eel.is/c++draft/expr.add) et des [types entiers signés, dont `int`](https://eel.is/c++draft/basic.fundamental) sont consultables dans cette présentation HTML du projet de norme C++. Elle ne remplace pas l’édition ISO C++17 publiée. Les quatre extraits de cette fiche sont vérifiés en mode C++17, y compris le cas volontairement incorrect pour le besoin.
