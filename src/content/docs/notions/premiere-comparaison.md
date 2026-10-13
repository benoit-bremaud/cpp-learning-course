---
title: "Première comparaison — le compteur dépasse-t-il la limite ?"
description: "Comprendre >, tester le cas d’égalité et recalculer une réponse booléenne à travers cinq exemples UML."
---

**Objectif :** calculer une valeur booléenne en comparant deux entiers. **Prérequis :** [initialisation et affectation](../cpp-01/), [limite constante](../cpp-09/) et [valeurs booléennes](../premiers-booleens/).

**Disponible :** cinq exemples de lecture et leurs cartes UML. Le projet de pratique autonome à cloner pour cette leçon n’est pas encore publié.

## Partir du besoin : constater un dépassement

Dans CPP-09, notre session de démonstration avait une limite fictive de **3 mesures**. Nous voulons maintenant répondre à une question précise : **« le nombre de mesures comptabilisées dépasse-t-il strictement cette limite ? »**

| Compteur fourni | Limite | Réponse attendue |
| --- | --- | --- |
| 2 | 3 | `false` : limite non atteinte. |
| 3 | 3 | `false` : limite atteinte, sans dépassement. |
| 4 | 3 | `true` : limite dépassée. |

La limite est un choix pédagogique, pas une capacité matérielle. Les compteurs sont des entiers connus compris entre 0 et 20. Nous comparons seulement des nombres : le programme n’acquiert aucune mesure et ne réserve pas de mémoire pour les conserver.

Chaque extrait est indépendant, à lire dans le corps de `main`. Les tableaux décrivent les valeurs après les instructions ; les extraits n’affichent rien. Nous calculons une réponse sans encore choisir une action en fonction de cette réponse.

## 1 — Comparer un compteur inférieur à la limite

La limite vaut **3 mesures** et le compteur vaut **2**. À la question « le compteur dépasse-t-il la limite ? », nous attendons **`false`**. La comparaison doit laisser la limite à 3 et le compteur à 2.

![Activité UML : comparer un compteur inférieur à la limite.](/diagrams/examples/comparison-below.svg)

<a href="/diagrams/examples/comparison-below.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

Le diagramme d’activité montre des actions successives : initialiser, évaluer, conserver. Il n’a pas de losange de décision, car le code ne choisit pas entre deux chemins. Évaluer et conserver sont deux étapes du raisonnement réalisées ici dans une seule déclaration, sans variable temporaire ajoutée. Le symbole final termine l’extrait, sans ajouter de `return`.

<!-- example:comparison-below -->
```cpp
const int measurement_limit = 3;
int measurement_count = 2;
bool limit_exceeded = measurement_count > measurement_limit;
```

<details class="uml-panel" data-uml="comparison-below">
<summary>Voir la conception UML</summary>

| Action UML | Correspondance C++ |
| --- | --- |
| Initialiser les deux quantités | La constante vaut 3 et le compteur vaut 2. |
| Évaluer le dépassement strict | `measurement_count > measurement_limit` produit `false`. |
| Conserver la réponse | La déclaration initialise `limit_exceeded` avec ce résultat. |

![Activité UML : comparer un compteur inférieur à la limite.](/diagrams/examples/comparison-below.svg)

<a href="/diagrams/examples/comparison-below.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

| Après l’instruction | `measurement_limit` | `measurement_count` | `limit_exceeded` |
| --- | --- | --- | --- |
| Déclaration de la limite | 3 | Pas encore créé | Pas encore créé |
| Déclaration du compteur | 3 | 2 | Pas encore créé |
| Déclaration du résultat | 3 | 2 | `false` |

L’opérateur `>` signifie **« strictement supérieur à »**. Lis l’expression dans l’ordre : « `measurement_count` est strictement supérieur à `measurement_limit` ». Les deux valeurs comparées sont les **opérandes** : 2 à gauche, 3 à droite.

Comme une addition produit une valeur, cette comparaison produit une valeur : ici, le booléen `false`. **L’expression de comparaison est déjà de type `bool`** ; la déclaration sert à conserver son résultat dans `limit_exceeded`, dont le nom signifie « limite dépassée ».

La comparaison lit les deux nombres sans les modifier. `const` conserve la limite fixe, tandis que `>` répond à la question posée : ces deux éléments ont des rôles différents.

## 2 — Atteindre la limite sans la dépasser

Changeons seulement le compteur : il vaut maintenant **3**, comme la limite. Le besoin reste « strictement supérieur ». Nous attendons donc encore **`false`**.

![Activité UML : atteindre la limite sans la dépasser.](/diagrams/examples/comparison-equal.svg)

<a href="/diagrams/examples/comparison-equal.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:comparison-equal -->
```cpp
const int measurement_limit = 3;
int measurement_count = 3;
bool limit_exceeded = measurement_count > measurement_limit;
```

<details class="uml-panel" data-uml="comparison-equal">
<summary>Voir la conception UML</summary>

| Action UML | Correspondance C++ |
| --- | --- |
| Initialiser les quantités | La limite et le compteur valent chacun 3. |
| Évaluer le dépassement strict | `3 > 3` produit `false`. |
| Conserver le résultat | `limit_exceeded` est initialisé à `false`. |

![Activité UML : atteindre la limite sans la dépasser.](/diagrams/examples/comparison-equal.svg)

<a href="/diagrams/examples/comparison-equal.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

| Après l’instruction | `measurement_limit` | `measurement_count` | `limit_exceeded` |
| --- | --- | --- | --- |
| Déclaration de la limite | 3 | Pas encore créé | Pas encore créé |
| Déclaration du compteur | 3 | 3 | Pas encore créé |
| Déclaration du résultat | 3 | 3 | `false` |

**Atteindre la limite n’est pas la dépasser.** Le mot « strictement » exclut l’égalité. `false` est donc ici la bonne réponse, pas une erreur de calcul.

Le résultat est le même que dans le premier exemple, mais les situations diffèrent : auparavant, le compteur était sous la limite ; ici, il l’atteint. Une réponse à la question « dépasse-t-il ? » ne suffit pas à distinguer ces deux situations.

## 3 — Constater un dépassement

Le compteur vaut désormais **4**, pour une limite toujours fixée à **3**. Nous attendons **`true`** : quatre est strictement supérieur à trois. Le compteur doit toutefois rester à **4** après la comparaison.

![Activité UML : constater un dépassement.](/diagrams/examples/comparison-above.svg)

<a href="/diagrams/examples/comparison-above.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:comparison-above -->
```cpp
const int measurement_limit = 3;
int measurement_count = 4;
bool limit_exceeded = measurement_count > measurement_limit;
```

<details class="uml-panel" data-uml="comparison-above">
<summary>Voir la conception UML</summary>

| Action UML | Correspondance C++ |
| --- | --- |
| Initialiser les quantités | La limite vaut 3, le compteur vaut 4. |
| Évaluer le dépassement strict | `4 > 3` produit `true`. |
| Conserver le résultat | `limit_exceeded` est initialisé à `true`. |

![Activité UML : constater un dépassement.](/diagrams/examples/comparison-above.svg)

<a href="/diagrams/examples/comparison-above.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

| Après l’instruction | `measurement_limit` | `measurement_count` | `limit_exceeded` |
| --- | --- | --- | --- |
| Déclaration de la limite | 3 | Pas encore créé | Pas encore créé |
| Déclaration du compteur | 3 | 4 | Pas encore créé |
| Déclaration du résultat | 3 | 4 | `true` |

**Constater un dépassement ne l’empêche pas.** Aucun code ne rejette une mesure, ne remet le compteur à 3 ou n’arrête un traitement. Nous avons seulement calculé et conservé une réponse.

Le cas prolonge la distinction vue avec `const` : déclarer une limite ne contrôle pas les autres variables. Ajouter une comparaison permet d’obtenir une information sur le dépassement ; agir en fonction de cette information viendra avec les conditions.

## 4 — Repérer une comparaison écrite dans le mauvais sens

Gardons le besoin du troisième exemple : le compteur **4** dépasse la limite **3**, donc la réponse attendue reste **`true`**. **Erreur volontaire :** nous échangeons les deux opérandes de `>`.

La conception de référence est celle de la section « Constater un dépassement ». La carte UML explique l’écart entre cette conception et le code inversé.

<!-- example:comparison-reversed -->
```cpp
const int measurement_limit = 3;
int measurement_count = 4;
bool limit_exceeded = measurement_limit > measurement_count;
```

<details class="uml-panel" data-uml="comparison-reversed">
<summary>Comprendre l’écart avec la conception</summary>

**Attendu : `true` ; obtenu : `false`.** Le diagramme décrit la conception attendue : comparer le compteur à la limite. Il ne décrit pas l’exécution de l’expression inversée.

| Conception attendue | Écart dans le code |
| --- | --- |
| Conserver la limite 3 et le compteur 4 | Les deux premières déclarations sont correctes. |
| Comparer le compteur à la limite | Le code compare la limite au compteur : `measurement_limit > measurement_count`. |
| Obtenir `true` | L’expression calcule `3 > 4`, donc obtient `false`. |

![Activité UML : comparer le compteur 4 à la limite 3 pour obtenir true, conception attendue.](/diagrams/examples/comparison-above.svg)

<a href="/diagrams/examples/comparison-above.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

| Après l’instruction | `measurement_limit` | `measurement_count` | `limit_exceeded` |
| --- | --- | --- | --- |
| Déclaration de la limite | 3 | Pas encore créé | Pas encore créé |
| Déclaration du compteur | 3 | 4 | Pas encore créé |
| Déclaration du résultat | 3 | 4 | `false` au lieu de `true` |

Ce fragment compile, mais pose la question « la limite est-elle strictement supérieure au compteur ? ». Ce n’est pas la question du besoin. La correction consiste à reprendre `measurement_count > measurement_limit`, comme dans le troisième exemple.

L’ordre des opérandes compte. Voici pourquoi vérifier seulement le cas d’égalité ne suffirait pas à repérer cette erreur :

| Compteur | Limite | Compteur supérieur à limite | Limite supérieure à compteur |
| --- | --- | --- | --- |
| 2 | 3 | `false` | `true` |
| 3 | 3 | `false` | `false` |
| 4 | 3 | `true` | `false` |

**À égalité, les deux expressions donnent `false`.** Ce seul cas masquerait l’inversion. Les cas sous la limite et au-dessus permettent de la distinguer.

## 5 — Recalculer après avoir modifié le compteur

Nous partons de **2 mesures**, puis nous affectons **4** au compteur. La limite reste à **3**. Le premier calcul donne `false`. Après la modification du compteur, le booléen doit conserver cette ancienne réponse **jusqu’à ce que nous recalculions la comparaison** ; il passera alors à `true`.

![Activité UML : recalculer après avoir modifié le compteur.](/diagrams/examples/comparison-refresh.svg)

<a href="/diagrams/examples/comparison-refresh.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:comparison-refresh -->
```cpp
const int measurement_limit = 3;
int measurement_count = 2;
bool limit_exceeded = measurement_count > measurement_limit;
measurement_count = 4;
limit_exceeded = measurement_count > measurement_limit;
```

<details class="uml-panel" data-uml="comparison-refresh">
<summary>Voir la conception UML</summary>

| Action UML | Correspondance C++ |
| --- | --- |
| Initialiser les quantités | La limite vaut 3 et le compteur vaut 2. |
| Calculer et conserver la première réponse | La déclaration de `limit_exceeded` conserve `false`. |
| Modifier seulement le compteur | `measurement_count = 4;` laisse le booléen inchangé. |
| Recalculer et remplacer la réponse | La dernière affectation conserve le nouveau résultat `true`. |

![Activité UML : recalculer après avoir modifié le compteur.](/diagrams/examples/comparison-refresh.svg)

<a href="/diagrams/examples/comparison-refresh.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

| Après l’instruction | `measurement_limit` | `measurement_count` | `limit_exceeded` |
| --- | --- | --- | --- |
| Déclaration de la limite | 3 | Pas encore créé | Pas encore créé |
| Déclaration du compteur | 3 | 2 | Pas encore créé |
| Premier calcul du résultat | 3 | 2 | `false` |
| Modification du compteur | 3 | 4 | **`false`**, ancienne réponse |
| Nouveau calcul du résultat | 3 | 4 | `true` |

La quatrième ligne ne modifie que le compteur. Elle ne relance pas les expressions utilisées plus tôt pour initialiser d’autres variables. À ce point du programme, le booléen contient encore la réponse calculée pour **2 mesures**.

La cinquième ligne évalue de nouveau l’expression, avec le compteur courant à **4**, puis remplace la valeur de `limit_exceeded`. Le résultat représente alors les données actuelles.

Cela prolonge la leçon sur les copies booléennes : **une valeur conservée n’est pas un lien qui se met à jour tout seul**. L’affectation de 4 est une donnée de démonstration, pas une acquisition de mesures ni une boucle.

## Vérifier sa compréhension

- Avec une limite de 3, quel résultat produit la comparaison pour les compteurs 0, 3 et 5 ?
- Un résultat `false` permet-il de savoir si la limite est atteinte exactement ?
- Comparer le compteur à la limite change-t-il leurs valeurs ?
- Pourquoi le seul cas d’égalité ne révèle-t-il pas l’inversion des opérandes ?
- Après la quatrième ligne du dernier exemple, pourquoi le booléen vaut-il encore `false` ?

**Repères pour te corriger :** `false`, `false`, `true` ; non, `false` couvre les cas sous la limite et à égalité ; les nombres restent inchangés ; les deux ordres donnent `false` à égalité ; le booléen conserve l’ancien résultat jusqu’au nouveau calcul.

**À retenir :** une comparaison répond à une question sur les valeurs au moment où elle est évaluée. `>` exclut l’égalité. Conserver la réponse ne crée ni mise à jour automatique ni contrôle empêchant le dépassement.

**Suite prévue :** distinguer « dépasser » de « atteindre ou dépasser », puis compléter les comparaisons avant les conditions. Le [parcours progressif](../../parcours/) situe ces étapes. La pratique reste dans les dépôts à cloner dans ton IDE.

## Référence

La [règle des opérateurs relationnels](https://eel.is/c++draft/expr.rel) précise que leur résultat est de type `bool` et dépend de la relation entre les valeurs comparées. Cette page présente le projet de norme, pas l’édition ISO C++17 publiée. Les cinq extraits de cette leçon sont vérifiés en mode C++17.
