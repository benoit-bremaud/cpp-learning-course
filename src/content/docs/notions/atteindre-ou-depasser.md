---
title: "Atteindre ou dépasser — distinguer > et >="
description: "Comparer deux questions à la même limite, avec trois cas et deux erreurs de choix d’opérateur."
---

**Objectif :** choisir entre un dépassement strict et une limite atteinte ou dépassée. **Prérequis :** [la première comparaison](../premiere-comparaison/), qui réutilise les entiers, `const` et les booléens.

**Disponible :** cinq exemples de lecture et leurs cartes UML. Le projet de pratique autonome à cloner pour cette leçon n’est pas encore publié.

## Deux questions pour les mêmes données

Nous gardons notre limite fictive de **3 mesures**. Nous voulons désormais conserver **deux réponses distinctes** :

| Question | Variable de résultat | Opérateur adapté |
| --- | --- | --- |
| Le compteur dépasse-t-il strictement la limite ? | `limit_exceeded` | `>` |
| Le compteur atteint-il ou dépasse-t-il la limite ? | `limit_reached` | `>=` |

Dans tout ce module, **« atteinte » dans le nom `limit_reached` inclut le dépassement**. Cela ne signifie pas « exactement égal » ni « atteint à un moment quelconque dans le passé ».

| Compteur | Limite | Dépassée ? | Atteinte ou dépassée ? |
| --- | --- | --- | --- |
| 2 | 3 | `false` | `false` |
| 3 | 3 | `false` | `true` |
| 4 | 3 | `true` | `true` |

Les nombres sont fournis directement, dans un domaine de 0 à 20. La limite de 3 est pédagogique, pas une capacité matérielle. Chaque extrait est indépendant, à lire dans le corps de `main`, et n’affiche rien. Aucune mesure n’est acquise ; les comparaisons ne modifient pas les nombres et ne déclenchent aucune action.

## 1 — Poser les deux questions sous la limite

Le compteur vaut **2** et la limite vaut **3**. Nous attendons deux réponses fausses : la limite n’est ni dépassée, ni atteinte.

![Activité UML : pour 2 mesures, comparer le dépassement strict puis la limite atteinte ou dépassée.](/diagrams/examples/inclusive-below.svg)

<a href="/diagrams/examples/inclusive-below.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

Le diagramme d’activité enchaîne les initialisations, puis le calcul et la conservation de chaque réponse. Il ne contient pas de losange de décision : calculer deux booléens ne choisit pas un chemin d’exécution. Évaluer et conserver sont des étapes du raisonnement, réalisées dans la même déclaration sans ajouter de variable temporaire.

<!-- example:inclusive-below -->
```cpp
const int measurement_limit = 3;
int measurement_count = 2;
bool limit_exceeded = measurement_count > measurement_limit;
bool limit_reached = measurement_count >= measurement_limit;
```

<details class="uml-panel" data-uml="inclusive-below">
<summary>Voir la conception UML</summary>

| Action UML | Correspondance C++ |
| --- | --- |
| Initialiser les nombres | La limite vaut 3 et le compteur vaut 2. |
| Calculer puis conserver le dépassement strict | `measurement_count > measurement_limit` initialise `limit_exceeded` à `false`. |
| Calculer puis conserver la réponse inclusive | `measurement_count >= measurement_limit` initialise `limit_reached` à `false`. |

![Activité UML : pour 2 mesures, comparer le dépassement strict puis la limite atteinte ou dépassée.](/diagrams/examples/inclusive-below.svg)

<a href="/diagrams/examples/inclusive-below.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

Dans le tableau, « dépassée » désigne `limit_exceeded` et « atteinte ou dépassée » désigne `limit_reached`.

| Après l’instruction | Limite | Compteur | Dépassée ? | Atteinte ou dépassée ? |
| --- | --- | --- | --- | --- |
| Déclaration de la limite | 3 | Pas encore créé | Pas encore créée | Pas encore créée |
| Déclaration du compteur | 3 | 2 | Pas encore créée | Pas encore créée |
| Déclaration de la première réponse | 3 | 2 | `false` | Pas encore créée |
| Déclaration de la seconde réponse | 3 | 2 | `false` | `false` |

L’opérateur `>=` signifie **« supérieur ou égal à »**. Il s’écrit avec les deux caractères adjacents, `>` puis `=`. C’est **un seul opérateur de comparaison**, pas une comparaison suivie d’une affectation.

Dans la dernière ligne, lis « le compteur est supérieur ou égal à la limite ». Avec 2 et 3, cette expression produit `false`. Le `=` situé juste après le nom `limit_reached` fait partie de son initialisation, tandis que `>=` compare les deux nombres.

Les deux questions donnent ici la même réponse. Cela ne suffit pas à conclure qu’elles sont équivalentes : regardons le cas d’égalité.

## 2 — Distinguer les réponses exactement à la limite

Le compteur vaut maintenant **3**, comme la limite. Nous attendons **`false` pour « dépassée »**, mais **`true` pour « atteinte ou dépassée »**. C’est le cas qui distingue les deux questions.

![Activité UML : pour 3 mesures, comparer le dépassement strict puis la limite atteinte ou dépassée.](/diagrams/examples/inclusive-equal.svg)

<a href="/diagrams/examples/inclusive-equal.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:inclusive-equal -->
```cpp
const int measurement_limit = 3;
int measurement_count = 3;
bool limit_exceeded = measurement_count > measurement_limit;
bool limit_reached = measurement_count >= measurement_limit;
```

<details class="uml-panel" data-uml="inclusive-equal">
<summary>Voir la conception UML</summary>

| Action UML | Correspondance C++ |
| --- | --- |
| Initialiser les nombres | La limite vaut 3 et le compteur vaut 3. |
| Calculer puis conserver le dépassement strict | `measurement_count > measurement_limit` initialise `limit_exceeded` à `false`. |
| Calculer puis conserver la réponse inclusive | `measurement_count >= measurement_limit` initialise `limit_reached` à `true`. |

![Activité UML : pour 3 mesures, comparer le dépassement strict puis la limite atteinte ou dépassée.](/diagrams/examples/inclusive-equal.svg)

<a href="/diagrams/examples/inclusive-equal.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

Dans le tableau, « dépassée » désigne `limit_exceeded` et « atteinte ou dépassée » désigne `limit_reached`.

| Après l’instruction | Limite | Compteur | Dépassée ? | Atteinte ou dépassée ? |
| --- | --- | --- | --- | --- |
| Déclaration de la limite | 3 | Pas encore créé | Pas encore créée | Pas encore créée |
| Déclaration du compteur | 3 | 3 | Pas encore créée | Pas encore créée |
| Déclaration de la première réponse | 3 | 3 | `false` | Pas encore créée |
| Déclaration de la seconde réponse | 3 | 3 | `false` | `true` |

Trois n’est pas strictement supérieur à trois : `>` donne `false`. En revanche, trois est égal à trois : `>=` donne `true`.

Le signe `=` inclus dans `>=` indique que **l’égalité est acceptée par cette comparaison**. Il ne change pas la limite ni le compteur. La déclaration du second booléen ne modifie pas non plus le premier.

Les deux réponses ne se contredisent pas. Elles répondent à deux questions distinctes : la limite est atteinte, sans être dépassée.

## 3 — Vérifier que « supérieur ou égal » inclut aussi le dépassement

Le compteur vaut **4**, avec une limite toujours à **3**. Nous attendons cette fois **deux réponses vraies** : le compteur dépasse la limite et il est bien au moins égal à celle-ci.

![Activité UML : pour 4 mesures, comparer le dépassement strict puis la limite atteinte ou dépassée.](/diagrams/examples/inclusive-above.svg)

<a href="/diagrams/examples/inclusive-above.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:inclusive-above -->
```cpp
const int measurement_limit = 3;
int measurement_count = 4;
bool limit_exceeded = measurement_count > measurement_limit;
bool limit_reached = measurement_count >= measurement_limit;
```

<details class="uml-panel" data-uml="inclusive-above">
<summary>Voir la conception UML</summary>

| Action UML | Correspondance C++ |
| --- | --- |
| Initialiser les nombres | La limite vaut 3 et le compteur vaut 4. |
| Calculer puis conserver le dépassement strict | `measurement_count > measurement_limit` initialise `limit_exceeded` à `true`. |
| Calculer puis conserver la réponse inclusive | `measurement_count >= measurement_limit` initialise `limit_reached` à `true`. |

![Activité UML : pour 4 mesures, comparer le dépassement strict puis la limite atteinte ou dépassée.](/diagrams/examples/inclusive-above.svg)

<a href="/diagrams/examples/inclusive-above.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

Dans le tableau, « dépassée » désigne `limit_exceeded` et « atteinte ou dépassée » désigne `limit_reached`.

| Après l’instruction | Limite | Compteur | Dépassée ? | Atteinte ou dépassée ? |
| --- | --- | --- | --- | --- |
| Déclaration de la limite | 3 | Pas encore créé | Pas encore créée | Pas encore créée |
| Déclaration du compteur | 3 | 4 | Pas encore créée | Pas encore créée |
| Déclaration de la première réponse | 3 | 4 | `true` | Pas encore créée |
| Déclaration de la seconde réponse | 3 | 4 | `true` | `true` |

`>=` ne veut pas dire « exactement égal ». Il accepte aussi les valeurs **supérieures** : avec quatre mesures pour une limite de trois, les deux comparaisons donnent `true`.

Dans cette leçon, `limit_reached` signifie précisément **« la valeur comparée atteint ou dépasse la limite »**. Ce nom ne mémorise pas si le compteur a atteint cette limite dans le passé : l’expression répond seulement pour les valeurs au moment du calcul.

Le compteur reste à 4. Aucun des deux opérateurs ne bloque le dépassement ou n’arrête un traitement.

## 4 — Manquer une limite atteinte en utilisant >

Le besoin reste celui du deuxième exemple : avec un compteur de **3** et une limite de **3**, nous attendons **`false` puis `true`**. **Erreur volontaire :** la dernière ligne utilise `>` pour répondre à la question « atteinte ou dépassée ? ».

La conception attendue est celle du deuxième exemple. La carte distingue ses résultats attendus des résultats de ce code volontairement incorrect.

<!-- example:inclusive-strict-for-inclusive -->
```cpp
const int measurement_limit = 3;
int measurement_count = 3;
bool limit_exceeded = measurement_count > measurement_limit;
bool limit_reached = measurement_count > measurement_limit;
```

<details class="uml-panel" data-uml="inclusive-strict-for-inclusive">
<summary>Comprendre l’écart avec la conception</summary>

**Attendu : `false` / `true` ; obtenu : `false` / `false`.** L’ordre est toujours `limit_exceeded`, puis `limit_reached`. Le diagramme représente la conception attendue ; il ne décrit pas l’exécution de ce code fautif.

| Conception attendue | Correspondance ou écart |
| --- | --- |
| Conserver la limite 3 et le compteur 3 | Les deux déclarations numériques sont conformes. |
| Dépassement strict : `false` | La règle utilise bien `>` et donne `false`. |
| Limite atteinte ou dépassée : `true` | La règle utilise incorrectement `>` et donne `false`. |

![Activité UML : pour 3 mesures, comparer le dépassement strict puis la limite atteinte ou dépassée ; conception attendue false puis true.](/diagrams/examples/inclusive-equal.svg)

<a href="/diagrams/examples/inclusive-equal.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

Dans le tableau, « dépassée » désigne `limit_exceeded` et « atteinte ou dépassée » désigne `limit_reached`.

| Après l’instruction | Limite | Compteur | Dépassée ? | Atteinte ou dépassée ? |
| --- | --- | --- | --- | --- |
| Déclaration de la limite | 3 | Pas encore créé | Pas encore créée | Pas encore créée |
| Déclaration du compteur | 3 | 3 | Pas encore créée | Pas encore créée |
| Déclaration de la première réponse | 3 | 3 | `false` | Pas encore créée |
| Déclaration de la seconde réponse | 3 | 3 | `false` | `false` |

La première réponse est correcte : la limite n’est pas dépassée. Mais la seconde devrait être `true`, puisque la limite est atteinte. Le code obtient `false` parce qu’il pose deux fois la question du dépassement strict.

**Correction :** remettre `>=` dans l’initialisation de `limit_reached`, comme dans le deuxième exemple. L’initialisation de `limit_exceeded` reste avec `>`.

Ce code compile : les deux comparaisons sont autorisées. Le défaut est le choix d’une règle qui exclut une situation que notre besoin devait accepter.

## 5 — Annoncer un dépassement trop tôt en utilisant >=

Gardons exactement les mêmes données et les mêmes questions : la réponse attendue est toujours **`false` puis `true`**. **Erreur volontaire inverse :** c’est maintenant l’initialisation de `limit_exceeded` qui utilise `>=`.

La conception attendue est celle du deuxième exemple. La carte distingue ses résultats attendus des résultats de ce code volontairement incorrect.

<!-- example:inclusive-inclusive-for-strict -->
```cpp
const int measurement_limit = 3;
int measurement_count = 3;
bool limit_exceeded = measurement_count >= measurement_limit;
bool limit_reached = measurement_count >= measurement_limit;
```

<details class="uml-panel" data-uml="inclusive-inclusive-for-strict">
<summary>Comprendre l’écart avec la conception</summary>

**Attendu : `false` / `true` ; obtenu : `true` / `true`.** L’ordre est toujours `limit_exceeded`, puis `limit_reached`. Le diagramme représente la conception attendue ; il ne décrit pas l’exécution de ce code fautif.

| Conception attendue | Correspondance ou écart |
| --- | --- |
| Conserver la limite 3 et le compteur 3 | Les deux déclarations numériques sont conformes. |
| Dépassement strict : `false` | La règle utilise incorrectement `>=` et donne `true`. |
| Limite atteinte ou dépassée : `true` | La règle utilise bien `>=` et donne `true`. |

![Activité UML : pour 3 mesures, comparer le dépassement strict puis la limite atteinte ou dépassée ; conception attendue false puis true.](/diagrams/examples/inclusive-equal.svg)

<a href="/diagrams/examples/inclusive-equal.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

Dans le tableau, « dépassée » désigne `limit_exceeded` et « atteinte ou dépassée » désigne `limit_reached`.

| Après l’instruction | Limite | Compteur | Dépassée ? | Atteinte ou dépassée ? |
| --- | --- | --- | --- | --- |
| Déclaration de la limite | 3 | Pas encore créé | Pas encore créée | Pas encore créée |
| Déclaration du compteur | 3 | 3 | Pas encore créée | Pas encore créée |
| Déclaration de la première réponse | 3 | 3 | `true` | Pas encore créée |
| Déclaration de la seconde réponse | 3 | 3 | `true` | `true` |

La seconde réponse est correcte : la limite est atteinte. Mais la première annonce un dépassement alors que le compteur est seulement égal à la limite.

**Correction :** remettre `>` dans l’initialisation de `limit_exceeded`. L’initialisation de `limit_reached` reste avec `>=`.

Remplacer systématiquement `>` par `>=` ne serait donc pas une amélioration. Il faut choisir l’opérateur qui correspond à la question, sans changer le nom ou le besoin pour justifier un mauvais résultat.

## Pourquoi vérifier exactement la limite ?

Avec un compteur de 2, `>` et `>=` donnent tous deux `false`. Avec un compteur de 4, ils donnent tous deux `true`. Dans ces deux situations, les mauvaises substitutions des derniers exemples passent inaperçues.

| Compteur | Version correcte : deux réponses | Deux fois `>` | Deux fois `>=` |
| --- | --- | --- | --- |
| 2 | `false` / `false` | `false` / `false` | `false` / `false` |
| 3 | **`false` / `true`** | `false` / `false` | `true` / `true` |
| 4 | `true` / `true` | `true` / `true` | `true` / `true` |

Dans chaque cellule, l’ordre reste « dépassée », puis « atteinte ou dépassée ». **Le test à égalité révèle ici le mauvais choix d’opérateur.** Cela complète la leçon précédente : pour repérer une inversion des opérandes, tester seulement l’égalité ne suffisait pas. Le jeu de cas utile dépend de l’erreur que l’on cherche à détecter.

## Vérifier sa compréhension

- Pour une limite de 3, pourquoi `>=` donne-t-il `true` avec un compteur de 4 ?
- À quel compteur les deux réponses diffèrent-elles dans les cas étudiés ?
- Si le besoin dit « strictement au-dessus », faut-il inclure l’égalité ?
- Un résultat `true` remet-il le compteur à la limite ?
- Pourquoi les seuls tests avec 2 et 4 ne détectent-ils pas les deux erreurs présentées ?

**Repères pour te corriger :** `>=` accepte aussi les valeurs supérieures ; à 3 ; non, il faut `>` ; aucune valeur numérique n’est modifiée ; les opérateurs donnent les mêmes résultats hors égalité pour ces entiers.

**À retenir :** `>` répond à « dépasse ? » ; `>=` répond à « atteint ou dépasse ? ». Aucun n’est meilleur dans l’absolu : le besoin fixe la bonne question.

**Suite :** [en dessous ou au maximum](../en-dessous-ou-au-maximum/) présente `<` et `<=`, puis les applique à une boîte pleine. Le [parcours progressif](../../parcours/) situe ces étapes ; la pratique reste dans les dépôts à cloner dans ton IDE.

## Référence

La [règle des opérateurs relationnels](https://eel.is/c++draft/expr.rel) définit les résultats booléens des comparaisons, dont `>` et `>=`. Cette page présente le projet de norme, pas l’édition ISO C++17 publiée. Les cinq extraits de cette leçon sont vérifiés en mode C++17.
