---
title: "Premiers booléens — représenter le vrai et le faux"
description: "Comprendre bool, true et false avec des affectations, des copies et six exemples conçus en UML."
---

**Objectif :** conserver et modifier une information qui a deux valeurs possibles. **Prérequis :** [déclarer, affecter et copier une variable](../cpp-01/). Cette leçon réutilise ces mécanismes avec un nouveau type.

**Disponible :** six exemples de lecture et leurs cartes UML. Le projet de pratique autonome à cloner pour cette leçon n’est pas encore publié.

## Partir d’une affirmation précise

Un entier permet notamment de représenter une quantité. Un **booléen**, de type `bool`, possède deux valeurs : **`true` (vrai)** et **`false` (faux)**. Nous allons nous en servir pour représenter cette affirmation : **« une panne est signalée »**.

| Information fournie par notre scénario | Valeur choisie |
| --- | --- |
| Une panne est signalée. | `true` |
| Aucune panne n’est signalée. | `false` |

Les scénarios fournissent une information connue. **`false` ne signifie pas « inconnu ».** Un booléen seul n’offre pas de troisième valeur pour dire que le signalement manque ; nous étudierons plus tard comment représenter ce cas.

Chaque extrait est indépendant, à lire dans le corps de `main`. Les tableaux montrent les valeurs après chaque instruction ; le code n’affiche rien. Nous n’utilisons encore ni comparaison ni condition : les valeurs sont fournies directement, sans lecture de capteur.

## 1 — Représenter une absence de panne signalée

Notre premier scénario indique qu’**aucune panne n’est signalée**. L’affirmation « une panne est signalée » est donc fausse. Nous voulons conserver cette information dans `fault_present`, dont le nom signifie ici « panne présente dans le signalement ». La valeur attendue est **`false`**.

![Activité UML : représenter une absence de panne signalée.](/diagrams/examples/boolean-absent.svg)

<a href="/diagrams/examples/boolean-absent.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

Dans ce diagramme d’activité UML, le point noir marque le début et le rectangle arrondi décrit l’initialisation. Le symbole final termine l’extrait, sans ajouter de `return`. Il n’y a pas de choix entre deux chemins : conserver un booléen ne constitue pas encore une décision dans le programme.

<!-- example:boolean-absent -->
```cpp
bool fault_present = false;
```

<details class="uml-panel" data-uml="boolean-absent">
<summary>Voir la conception UML</summary>

| Conception | Correspondance C++ |
| --- | --- |
| Créer une information booléenne initialisée à faux | `bool fault_present = false;` crée la variable avec la valeur `false`. |

![Activité UML : représenter une absence de panne signalée.](/diagrams/examples/boolean-absent.svg)

<a href="/diagrams/examples/boolean-absent.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

| Après l’instruction | `fault_present` |
| --- | --- |
| Déclaration | `false` |

`bool` annonce le type de la variable. `fault_present` est son nom. `false` est la valeur avec laquelle nous l’initialisons. Le point-virgule termine la déclaration, comme dans les exemples avec `int`.

`false` et `true` sont deux valeurs du langage C++, écrites **en minuscules et sans guillemets**. On ne traduit pas ces mots dans le code.

Ici, `false` représente l’information fournie par le scénario. Cette déclaration ne vérifie pas l’état d’un appareil et ne prouve pas qu’un appareil réel fonctionne correctement.

## 2 — Représenter une panne signalée

Changeons une seule donnée du besoin : **une panne est maintenant signalée**. L’affirmation est vraie ; la valeur attendue dans `fault_present` est donc **`true`**.

![Activité UML : représenter une panne signalée.](/diagrams/examples/boolean-present.svg)

<a href="/diagrams/examples/boolean-present.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:boolean-present -->
```cpp
bool fault_present = true;
```

<details class="uml-panel" data-uml="boolean-present">
<summary>Voir la conception UML</summary>

| Conception | Correspondance C++ |
| --- | --- |
| Créer une information booléenne initialisée à vrai | `bool fault_present = true;` crée la variable avec la valeur `true`. |

![Activité UML : représenter une panne signalée.](/diagrams/examples/boolean-present.svg)

<a href="/diagrams/examples/boolean-present.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

| Après l’instruction | `fault_present` |
| --- | --- |
| Déclaration | `true` |

**Vrai ne veut pas dire « bon » ou « réussi ».** Cela veut dire que l’affirmation décrite par la variable est vraie. Ici, la valeur vraie représente justement une panne signalée.

Le nom aide donc à interpréter la valeur. Une variable qui décrirait « l’appareil est prêt » ne poserait pas la même question. Avant de choisir une valeur, formule en français l’affirmation que ta variable représente.

## 3 — Modifier une information au fil des instructions

Pour cette séquence de démonstration, le signalement commence à « aucune panne », passe à « panne signalée », puis revient à « aucune panne ». Nous attendons **`false` → `true` → `false`**. Ces informations sont écrites directement dans le code.

![Activité UML : modifier une information au fil des instructions.](/diagrams/examples/boolean-changes.svg)

<a href="/diagrams/examples/boolean-changes.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:boolean-changes -->
```cpp
bool fault_present = false;
fault_present = true;
fault_present = false;
```

<details class="uml-panel" data-uml="boolean-changes">
<summary>Voir la conception UML</summary>

| Action UML | Correspondance C++ |
| --- | --- |
| Initialiser l’information | La déclaration donne `false`. |
| Remplacer par vrai | La première affectation donne `true`. |
| Remplacer par faux | La seconde affectation donne `false`. |

![Activité UML : modifier une information au fil des instructions.](/diagrams/examples/boolean-changes.svg)

<a href="/diagrams/examples/boolean-changes.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

| Après l’instruction | `fault_present` |
| --- | --- |
| Déclaration | `false` |
| Première affectation | `true` |
| Deuxième affectation | `false` |

Le mécanisme est le même qu’avec un entier : la déclaration crée la variable, puis les affectations remplacent sa valeur. On ne remet pas `bool` devant son nom lors de ces modifications.

Les instructions s’enchaînent sans attente ni détection. Écrire `true` ne déclenche pas une panne ; écrire `false` ne la répare pas. Nous modifions seulement une information conservée par le programme.

## 4 — Copier une valeur, sans créer de lien automatique

Nous voulons conserver une copie du signalement initial dans `fault_snapshot` : le mot anglais *snapshot* désigne ici une copie de la valeur à un instant donné. Le signalement initial vaut `false`. Après sa copie, nous modifierons l’original à `true` ; **la copie doit rester à `false`**.

![Activité UML : copier une valeur, sans créer de lien automatique.](/diagrams/examples/boolean-copy.svg)

<a href="/diagrams/examples/boolean-copy.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:boolean-copy -->
```cpp
bool fault_present = false;
bool fault_snapshot = fault_present;
fault_present = true;
```

<details class="uml-panel" data-uml="boolean-copy">
<summary>Voir la conception UML</summary>

| Action UML | Correspondance C++ |
| --- | --- |
| Initialiser l’original | `fault_present` reçoit `false`. |
| Lire sa valeur et initialiser une copie | `fault_snapshot` reçoit la valeur `false` lue lors de sa déclaration. |
| Modifier seulement l’original | L’affectation à `fault_present` lui donne `true`. |

![Activité UML : copier une valeur, sans créer de lien automatique.](/diagrams/examples/boolean-copy.svg)

<a href="/diagrams/examples/boolean-copy.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

| Après l’instruction | `fault_present` | `fault_snapshot` |
| --- | --- | --- |
| Déclaration de l’original | `false` | Pas encore créée |
| Déclaration de la copie | `false` | `false` |
| Modification de l’original | `true` | `false` |

Dans la deuxième ligne, on lit la valeur de `fault_present` à ce moment-là pour initialiser une **autre variable**. On n’installe pas une règle qui recalculerait la copie à chaque modification de l’original.

À la fin, les deux variables ne se contredisent pas : elles représentent deux moments différents du scénario. Ce mécanisme de copie est celui déjà rencontré avec les entiers.

## 5 — Actualiser explicitement la copie

Reprenons le même scénario, mais ajoutons une exigence : après la modification de l’original, nous voulons que la copie conserve sa **nouvelle valeur**. Une affectation supplémentaire devra faire passer `fault_snapshot` de `false` à **`true`**.

![Activité UML : actualiser explicitement la copie.](/diagrams/examples/boolean-refresh.svg)

<a href="/diagrams/examples/boolean-refresh.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:boolean-refresh -->
```cpp
bool fault_present = false;
bool fault_snapshot = fault_present;
fault_present = true;
fault_snapshot = fault_present;
```

<details class="uml-panel" data-uml="boolean-refresh">
<summary>Voir la conception UML</summary>

| Action UML | Correspondance C++ |
| --- | --- |
| Initialiser l’original puis sa copie | Les deux variables valent d’abord `false`. |
| Modifier l’original | `fault_present` passe à `true` ; la copie reste à `false`. |
| Relire l’original et actualiser la copie | La dernière affectation remplace la valeur de `fault_snapshot` par `true`. |

![Activité UML : actualiser explicitement la copie.](/diagrams/examples/boolean-refresh.svg)

<a href="/diagrams/examples/boolean-refresh.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

| Après l’instruction | `fault_present` | `fault_snapshot` |
| --- | --- | --- |
| Déclaration de l’original | `false` | Pas encore créée |
| Déclaration de la copie | `false` | `false` |
| Modification de l’original | `true` | `false` |
| Actualisation de la copie | `true` | `true` |

La dernière ligne lit la valeur courante de `fault_present` et la conserve dans `fault_snapshot`. L’original n’est pas modifié par cette lecture.

Cette affectation ne crée toujours pas de suivi automatique. Une nouvelle modification ultérieure de l’original ne changerait pas la copie sans une nouvelle affectation. En actualisant la copie, nous avons aussi remplacé l’ancienne information : `fault_snapshot` ne conserve plus le signalement initial.

## 6 — Repérer une valeur qui contredit le besoin

Revenons au premier besoin : **aucune panne n’est signalée**, donc `fault_present` doit commencer à **`false`**. Le diagramme de la première section décrit cette conception. **Erreur volontaire :** le code ci-dessous choisit l’autre valeur.

La carte UML reprend la conception attendue de la première section et explique la différence avec ce code.

<!-- example:boolean-wrong -->
```cpp
bool fault_present = true;
```

<details class="uml-panel" data-uml="boolean-wrong">
<summary>Comprendre l’écart avec la conception</summary>

**Attendu : `false` ; obtenu : `true`.** Le diagramme représente le besoin d’absence de panne signalée. Il ne décrit pas l’exécution de cette déclaration volontairement incorrecte pour ce besoin.

| Conception attendue | Écart dans le code |
| --- | --- |
| Initialiser `fault_present` à `false` | La déclaration l’initialise à `true`. |
| Représenter l’absence de panne signalée | La valeur choisie représente au contraire une panne signalée. |

![Activité UML : initialiser fault_present à false, conception attendue.](/diagrams/examples/boolean-absent.svg)

<a href="/diagrams/examples/boolean-absent.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

| Vérification | Résultat |
| --- | --- |
| La déclaration compile-t-elle ? | Oui : `true` est une valeur de type `bool`. |
| Quelle valeur est obtenue ? | `true`. |
| Quelle valeur exige notre scénario ? | `false`. |
| Le besoin est-il respecté ? | Non. |

Cette ligne est **identique à celle du deuxième exemple**, où elle était correcte : le besoin n’était pas le même. `true` n’est donc pas une valeur interdite. C’est son choix dans ce scénario qui est incorrect.

La correction consiste à reprendre l’initialisation à `false` du premier exemple. Changer le nom de la variable ou le besoin pour justifier la valeur ne corrigerait pas l’erreur demandée ici.

## Vérifier sa compréhension

- Que signifie `true` pour notre variable `fault_present` ? Est-ce nécessairement une bonne nouvelle ?
- Peut-on utiliser `false` comme troisième valeur pour représenter une information inconnue ?
- Après avoir copié `false`, que contient la copie si l’original devient `true` ?
- Quelle instruction du cinquième exemple actualise la copie ?
- Pourquoi la même déclaration à `true` est-elle correcte dans le deuxième exemple et incorrecte dans le dernier ?

**Repères pour te corriger :** une panne est signalée, ce qui n’est pas une bonne nouvelle ; `false` est l’une des deux valeurs, pas une valeur « inconnue » ; la copie reste à `false` ; la dernière affectation actualise la copie ; les besoins des deux exemples diffèrent.

**À retenir :** choisis une affirmation claire pour comprendre une valeur booléenne. Déclarer ou affecter cette valeur ne vérifie pas la réalité ; copier sa valeur ne crée pas un lien automatique.

**Suite :** [produire un résultat booléen avec une première comparaison](../premiere-comparaison/), puis étudier les autres comparaisons avant les conditions. Ces notions restent distinctes dans le [parcours progressif](../../parcours/). Les conversions numériques et les opérations logiques seront expliquées dans leurs modules ; la pratique reste dans les dépôts à cloner dans ton IDE.

## Références

Les [valeurs du type `bool`](https://eel.is/c++draft/basic.fundamental#10) et la [règle d’affectation](https://eel.is/c++draft/expr.assign) sont décrites dans le projet de norme C++. Ces pages ne remplacent pas l’édition ISO C++17 publiée. Les six extraits de cette leçon sont vérifiés en mode C++17.
