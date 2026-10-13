---
title: "En dessous ou au maximum — distinguer < et <="
description: "Lire deux comparaisons, respecter une capacité et reconnaître une inversion des opérandes."
---

**Objectif :** choisir entre « strictement en dessous » et « au maximum », puis appliquer cette distinction à une capacité. **Prérequis :** [atteindre ou dépasser](../atteindre-ou-depasser/), avec les entiers, `const` et les résultats booléens.

**Disponible :** cinq exemples de lecture et leurs cartes UML. Le projet de pratique autonome à cloner pour cette leçon n’est pas encore publié.

## Poser la question dans le bon sens

Nous conservons une limite fictive de **3 mesures**, mais nous changeons les questions :

| Question | Réponse conservée | Expression |
| --- | --- | --- |
| Le compteur est-il strictement en dessous ? | `below_limit` | `measurement_count < measurement_limit` |
| Le compteur est-il au maximum égal à la limite ? | `within_limit` | `measurement_count <= measurement_limit` |

`<` signifie **« inférieur à »** et `<=` signifie **« inférieur ou égal à »**. Lis toujours la valeur de gauche, l’opérateur, puis la valeur de droite. « Au maximum trois » accepte trois ; « moins de trois » l’exclut.

Les compteurs fournis sont des `int` de 0 à 20 ; les limites positives sont de 1 à 20. Ce sont nos hypothèses de lecture, pas des vérifications réalisées par le code. `within_limit` répond seulement à la question de la borne supérieure dans ce cadre.

Chaque extrait est indépendant, à lire dans le corps de `main`. Il n’affiche rien et n’acquiert aucune mesure. Les comparaisons conservent les nombres et calculent des réponses ; elles ne contrôlent pas une action matérielle.

## 1 — Lire deux réponses sous la limite

Le compteur vaut **2**, la limite **3**. Deux est inférieur à trois, et est aussi inférieur ou égal à trois : **nous attendons `true` puis `true`**.

![Activité UML : measurement_count vaut 2 ; comparer au maximum 3, sans choisir de chemin.](/diagrams/examples/lower-below.svg)

<a href="/diagrams/examples/lower-below.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

Le disque initial marque le début, les rectangles arrondis les actions, puis le symbole final termine cette activité. Évaluer une comparaison et conserver sa réponse sont deux étapes du raisonnement réalisées par une seule déclaration. Il n’y a ni variable temporaire supplémentaire, ni losange : calculer un booléen ne choisit pas un chemin.

<!-- example:lower-below -->
```cpp
const int measurement_limit = 3;
int measurement_count = 2;
bool below_limit = measurement_count < measurement_limit;
bool within_limit = measurement_count <= measurement_limit;
```

<details class="uml-panel" data-uml="lower-below">
<summary>Voir la conception UML</summary>

| Action UML attendue | Correspondance C++  |
| --- | --- |
| Initialiser les nombres | `measurement_limit` vaut 3, `measurement_count` vaut 2. |
| Répondre à la question stricte | `measurement_count < measurement_limit` initialise `below_limit` à `true`. |
| Répondre à la question inclusive | `measurement_count <= measurement_limit` initialise `within_limit` à `true`. |

![Activité UML : measurement_count vaut 2 ; comparer au maximum 3, sans choisir de chemin.](/diagrams/examples/lower-below.svg)

<a href="/diagrams/examples/lower-below.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

La trace suit `below_limit`, puis `within_limit`. Elle montre les valeurs après chaque instruction.

| Après l’instruction | Maximum | Nombre | En dessous ? | Au maximum ? |
| --- | --- | --- | --- | --- |
| Déclaration du maximum | 3 | Pas encore créé | Pas encore créée | Pas encore créée |
| Déclaration du nombre | 3 | 2 | Pas encore créée | Pas encore créée |
| Déclaration de la première réponse | 3 | 2 | `true` | Pas encore créée |
| Déclaration de la seconde réponse | 3 | 2 | `true` | `true` |

Dans la troisième ligne, `measurement_count < measurement_limit` produit `true`. Le `=` qui suit `below_limit` initialise ce booléen avec la réponse calculée. La ligne suivante initialise une autre réponse ; elle ne modifie pas la première.

`<=` est **un seul opérateur**, écrit avec deux caractères adjacents. Il ne signifie pas « comparer, puis affecter ». Les deux expressions donnent ici le même résultat, mais elles ne posent pas exactement la même question.

Le lien avec `>` est utile : `measurement_count < measurement_limit` et `measurement_limit > measurement_count` expriment la même relation. « Deux est inférieur à trois » revient à dire « trois est supérieur à deux ». On a échangé **les valeurs et le sens de l’opérateur**.

## 2 — Accepter exactement le maximum

Le compteur vaut maintenant **3** et la limite reste **3**. Avant de lire la réponse, demande-toi : « moins de trois » et « au maximum trois » acceptent-ils tous deux trois ?

**Attendu : `false` puis `true`.** Seule la question inclusive accepte l’égalité.

![Activité UML : measurement_count vaut 3 ; comparer au maximum 3, sans choisir de chemin.](/diagrams/examples/lower-equal.svg)

<a href="/diagrams/examples/lower-equal.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:lower-equal -->
```cpp
const int measurement_limit = 3;
int measurement_count = 3;
bool below_limit = measurement_count < measurement_limit;
bool within_limit = measurement_count <= measurement_limit;
```

<details class="uml-panel" data-uml="lower-equal">
<summary>Voir la conception UML</summary>

| Action UML attendue | Correspondance C++  |
| --- | --- |
| Initialiser les nombres | `measurement_limit` vaut 3, `measurement_count` vaut 3. |
| Répondre à la question stricte | `measurement_count < measurement_limit` initialise `below_limit` à `false`. |
| Répondre à la question inclusive | `measurement_count <= measurement_limit` initialise `within_limit` à `true`. |

![Activité UML : measurement_count vaut 3 ; comparer au maximum 3, sans choisir de chemin.](/diagrams/examples/lower-equal.svg)

<a href="/diagrams/examples/lower-equal.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

La trace suit `below_limit`, puis `within_limit`. Elle montre les valeurs après chaque instruction.

| Après l’instruction | Maximum | Nombre | En dessous ? | Au maximum ? |
| --- | --- | --- | --- | --- |
| Déclaration du maximum | 3 | Pas encore créé | Pas encore créée | Pas encore créée |
| Déclaration du nombre | 3 | 3 | Pas encore créée | Pas encore créée |
| Déclaration de la première réponse | 3 | 3 | `false` | Pas encore créée |
| Déclaration de la seconde réponse | 3 | 3 | `false` | `true` |

Trois n’est pas strictement inférieur à trois. En revanche, il est inférieur **ou égal** à trois. `within_limit` vaut donc `true` même lorsque la limite est atteinte.

`<=` ne signifie pas « exactement égal » : il était déjà vrai avec deux mesures. La première réponse reste `false` après le calcul de la seconde.

## 3 — Constater un dépassement

Le compteur fourni vaut **4**, pour une limite de **3**. **Attendu : `false` puis `false`.** Quatre n’est ni inférieur, ni inférieur ou égal à trois.

![Activité UML : measurement_count vaut 4 ; comparer au maximum 3, sans choisir de chemin.](/diagrams/examples/lower-above.svg)

<a href="/diagrams/examples/lower-above.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:lower-above -->
```cpp
const int measurement_limit = 3;
int measurement_count = 4;
bool below_limit = measurement_count < measurement_limit;
bool within_limit = measurement_count <= measurement_limit;
```

<details class="uml-panel" data-uml="lower-above">
<summary>Voir la conception UML</summary>

| Action UML attendue | Correspondance C++  |
| --- | --- |
| Initialiser les nombres | `measurement_limit` vaut 3, `measurement_count` vaut 4. |
| Répondre à la question stricte | `measurement_count < measurement_limit` initialise `below_limit` à `false`. |
| Répondre à la question inclusive | `measurement_count <= measurement_limit` initialise `within_limit` à `false`. |

![Activité UML : measurement_count vaut 4 ; comparer au maximum 3, sans choisir de chemin.](/diagrams/examples/lower-above.svg)

<a href="/diagrams/examples/lower-above.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

La trace suit `below_limit`, puis `within_limit`. Elle montre les valeurs après chaque instruction.

| Après l’instruction | Maximum | Nombre | En dessous ? | Au maximum ? |
| --- | --- | --- | --- | --- |
| Déclaration du maximum | 3 | Pas encore créé | Pas encore créée | Pas encore créée |
| Déclaration du nombre | 3 | 4 | Pas encore créée | Pas encore créée |
| Déclaration de la première réponse | 3 | 4 | `false` | Pas encore créée |
| Déclaration de la seconde réponse | 3 | 4 | `false` | `false` |

Le compteur reste à **4** après les deux comparaisons. `false` est une réponse correcte aux questions posées, pas une erreur du programme. Aucun opérateur ne ramène le compteur à trois et aucune action n’est empêchée.

Nous avons maintenant couvert les trois positions : sous la limite, à égalité, au-dessus. Appliquons le raisonnement à un autre besoin.

## 4 — Une boîte pleine respecte encore sa capacité

Changeons de contexte : une boîte possède **8 emplacements**, chacun pouvant recevoir un objet. Elle contient déjà **8 objets**. Réfléchis aux deux questions : reste-t-il une place pour **un objet supplémentaire** ? Le nombre actuel respecte-t-il la capacité ?

**Attendu : `false` pour `has_space`, puis `true` pour `within_capacity`.** Notre modèle compte des emplacements identiques ; il ne calcule ni le volume ni le poids des objets.

![Activité UML : item_count vaut 8 ; comparer au maximum 8, sans choisir de chemin.](/diagrams/examples/lower-capacity.svg)

<a href="/diagrams/examples/lower-capacity.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:lower-capacity -->
```cpp
const int box_capacity = 8;
int item_count = 8;
bool has_space = item_count < box_capacity;
bool within_capacity = item_count <= box_capacity;
```

<details class="uml-panel" data-uml="lower-capacity">
<summary>Voir la conception UML</summary>

| Action UML attendue | Correspondance C++  |
| --- | --- |
| Initialiser les nombres | `box_capacity` vaut 8, `item_count` vaut 8. |
| Répondre à la question stricte | `item_count < box_capacity` initialise `has_space` à `false`. |
| Répondre à la question inclusive | `item_count <= box_capacity` initialise `within_capacity` à `true`. |

![Activité UML : item_count vaut 8 ; comparer au maximum 8, sans choisir de chemin.](/diagrams/examples/lower-capacity.svg)

<a href="/diagrams/examples/lower-capacity.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

La trace suit `has_space`, puis `within_capacity`. Elle montre les valeurs après chaque instruction.

| Après l’instruction | Maximum | Nombre | Une place libre ? | Capacité respectée ? |
| --- | --- | --- | --- | --- |
| Déclaration du maximum | 8 | Pas encore créé | Pas encore créée | Pas encore créée |
| Déclaration du nombre | 8 | 8 | Pas encore créée | Pas encore créée |
| Déclaration de la première réponse | 8 | 8 | `false` | Pas encore créée |
| Déclaration de la seconde réponse | 8 | 8 | `false` | `true` |

Dans ce modèle, `has_space` signifie « il reste une place pour un objet ». `within_capacity` signifie « le nombre actuel ne dépasse pas huit ». **Respecter la capacité ne suffit pas pour conclure qu’une place reste libre.**

| Nombre fourni | Une place libre ? | Capacité respectée ? |
| --- | --- | --- |
| 7 | `true` | `true` |
| 8 | `false` | `true` |
| 9 | `false` | `false` |

La dernière ligne représente un nombre enregistré excessif dans une autre situation hypothétique ; le code n’a pas ajouté un neuvième objet. Il ne réalise aucune insertion, ni aucun blocage. Le cas de plusieurs objets à ajouter demanderait une autre question.

## 5 — Diagnostiquer une question inversée

Revenons au compteur du premier exemple : **2 mesures**, avec une limite de **3**. Le besoin reste le même : **nous attendons `true` puis `true`**.

**Erreur volontaire :** la première comparaison échange les deux opérandes de `<`. Ce piège a déjà été rencontré avec `>` ; essaie maintenant de reformuler à voix haute la question réellement posée. La conception attendue reste celle du premier exemple, représentée avant ce code ; la carte explique l’écart.

<!-- example:lower-reversed -->
```cpp
const int measurement_limit = 3;
int measurement_count = 2;
bool below_limit = measurement_limit < measurement_count;
bool within_limit = measurement_count <= measurement_limit;
```

<details class="uml-panel" data-uml="lower-reversed">
<summary>Comprendre l’écart avec la conception</summary>

**Attendu : `true` / `true` ; obtenu : `false` / `true`.** L’ordre est `below_limit`, puis `within_limit`. Le diagramme décrit la conception attendue, pas l’exécution du code fautif.

| Action UML attendue | Correspondance C++ ou écart |
| --- | --- |
| Initialiser les nombres | `measurement_limit` vaut 3, `measurement_count` vaut 2. |
| Répondre à la question stricte | `below_limit` devrait valoir `true` ; les opérandes inversés donnent `false`. |
| Répondre à la question inclusive | `measurement_count <= measurement_limit` initialise `within_limit` à `true`. |

![Activité UML : measurement_count vaut 2 ; comparer au maximum 3, sans choisir de chemin.](/diagrams/examples/lower-below.svg)

<a href="/diagrams/examples/lower-below.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

La trace suit `below_limit`, puis `within_limit`. Elle montre les valeurs effectivement obtenues, malgré l’erreur.

| Après l’instruction | Maximum | Nombre | En dessous ? | Au maximum ? |
| --- | --- | --- | --- | --- |
| Déclaration du maximum | 3 | Pas encore créé | Pas encore créée | Pas encore créée |
| Déclaration du nombre | 3 | 2 | Pas encore créée | Pas encore créée |
| Déclaration de la première réponse | 3 | 2 | `false` | Pas encore créée |
| Déclaration de la seconde réponse | 3 | 2 | `false` | `true` |

La première expression demande « la limite est-elle inférieure au compteur ? », soit « trois est-il inférieur à deux ? ». Sa réponse `false` est correcte pour cette question, mais cette question ne correspond pas au besoin de `below_limit`.

**Correction directe :** employer `measurement_count < measurement_limit`, comme au premier exemple. **Formulation équivalente :** `measurement_limit > measurement_count`. La constante n’a donc pas l’obligation d’être à droite ; c’est la relation exprimée qui compte.

| Compteur | Expression attendue : compteur < limite | Expression inversée : limite < compteur |
| --- | --- | --- |
| 2 | `true` | `false` |
| 3 | `false` | `false` |
| 4 | `false` | `true` |

Avec trois mesures, les deux expressions donnent `false` : **tester seulement l’égalité masquerait l’inversion**. Les deux autres cas la révèlent. Cette fois, l’erreur concerne l’ordre des opérandes, pas le choix entre strict et inclusif.

## Récapituler les quatre questions

Pour nos entiers, voici les résultats avec la même limite de trois. Chaque colonne pose sa propre question ; ce tableau récapitule les opérateurs déjà rencontrés.

| Compteur | `> 3` | `>= 3` | `< 3` | `<= 3` |
| --- | --- | --- | --- | --- |
| 2 | `false` | `false` | `true` | `true` |
| 3 | `false` | `true` | `false` | `true` |
| 4 | `true` | `true` | `false` | `false` |

## Vérifier sa compréhension

- Pour « au maximum trois », quel opérateur conserve l’égalité ?
- Une boîte pleine respecte-t-elle sa capacité ? Peut-elle recevoir encore un objet dans notre modèle ?
- Comment reformuler `measurement_count < measurement_limit` en plaçant la limite à gauche ?
- Pourquoi l’égalité seule ne détecte-t-elle pas l’inversion du dernier exemple ?
- Un booléen à `false` corrige-t-il un compteur excessif ?

**Repères pour te corriger :** `<=` ; oui, mais elle n’a plus de place ; `measurement_limit > measurement_count` ; les deux comparaisons strictes sont fausses à égalité ; non, la comparaison laisse les nombres inchangés.

**À retenir :** « moins de » exclut l’égalité, « au maximum » l’accepte. Choisis la question avant l’opérateur, puis vérifie les cas sous la limite, à égalité et au-dessus.

**Suite prévue :** comparer l’égalité et la différence, puis utiliser une réponse pour choisir une action avec les conditions. Le [parcours](../../parcours/) garde ces étapes séparées ; les exercices exécutables restent dans les dépôts à cloner.

## Référence

La [définition des opérateurs relationnels](https://eel.is/c++draft/expr.rel) précise leurs résultats booléens et leur sens pour les valeurs arithmétiques. Il s’agit du projet de norme, pas de l’édition ISO C++17 publiée. Les extraits de cette page sont vérifiés en C++17.
