---
title: "Premières divisions — compter les kits complets"
description: "Comprendre la division entière, le quotient tronqué et la différence entre stock nul et diviseur nul."
---

**Objectif :** calculer combien de kits complets un stock permettrait de constituer. **Prérequis :** [lire une expression](../premieres-expressions/) et [relier kits et composants par multiplication](../premieres-multiplications/).

**Disponible :** quatre exemples de lecture et leurs cartes UML. Le projet de pratique autonome à cloner n’est pas encore publié.

## Partir d’un stock et d’une taille de kit

Nous disposons de **12 composants**. Chaque kit en demande **4**. Le besoin est de compter les kits **complets** possibles : ici, **3 kits**, car trois groupes de quatre utilisent douze composants.

Dans cette leçon, le stock est connu et compris entre 0 et 20. Le nombre de composants par kit est compris entre 1 et 10 : **il est strictement positif**. Nous le garderons égal à 4 pour ne changer qu’une donnée à la fois. Ces bornes conviennent à `int` ; ce sont des hypothèses de nos exemples, pas des contrôles réalisés par le code.

Les extraits se lisent séparément, dans le corps de `main`. Ils ne constituent pas à eux seuls des programmes complets. Ils calculent un nombre de kits possibles, sans assembler les kits ni modifier le stock. Ils n’affichent rien : les tableaux sont des observations expliquées.

## 1 — Une division exacte

La conception prévoit de conserver le stock 12 et la taille de kit 4, de calculer leur quotient entier, puis de créer `kit_count` avec le résultat **3**.

![Initialiser le stock à 12 et le contenu par kit à quatre, calculer le quotient entier puis initialiser kit_count à 3.](/diagrams/examples/division-exact.svg)

<a href="/diagrams/examples/division-exact.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:division-exact -->
```cpp
int component_count = 12;
int components_per_kit = 4;
int kit_count = component_count / components_per_kit;
```

<details class="uml-panel" data-uml="division-exact">
<summary>Voir la conception UML</summary>

![Initialiser le stock à 12 et le contenu par kit à quatre, calculer le quotient entier puis initialiser kit_count à 3.](/diagrams/examples/division-exact.svg)

<a href="/diagrams/examples/division-exact.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Action UML | Correspondance C++ |
| --- | --- |
| Initialiser le stock | `component_count` reçoit `12`. |
| Fixer la quantité par kit | `components_per_kit` reçoit `4`. |
| Calculer le quotient entier | `component_count / components_per_kit` produit `3`. |
| Conserver le nombre de kits complets | La troisième déclaration initialise `kit_count` à `3`. |

La division et l’initialisation sont des étapes du raisonnement, réalisées ici dans la même déclaration. Aucun composant n’est retiré du stock ; aucun reste n’est enregistré dans une variable.

</details>

| Après l’instruction | `component_count` | `components_per_kit` | `kit_count` |
| --- | --- | --- | --- |
| Première déclaration | 12 | Pas encore créée | Pas encore créée |
| Deuxième déclaration | 12 | 4 | Pas encore créée |
| Déclaration du quotient | 12 | 4 | 3 |

Le signe `/` est l’opérateur de **division**. Dans `component_count / components_per_kit`, le stock est le **dividende**, la quantité par kit est le **diviseur**, et le résultat est le **quotient**.

Ici, 12 se répartit exactement en trois groupes de quatre. La valeur de `kit_count` est **3**. Les deux entrées restent 12 et 4 : le calcul n’a pas consommé les composants.

Dans le diagramme d’activité UML, le point noir marque le début, les rectangles arrondis les actions et le symbole final la fin du fragment. Cette fin n’ajoute pas une instruction `return`.

## 2 — Un stock qui ne remplit pas un kit supplémentaire

Changeons uniquement le stock : nous disposons maintenant de **14 composants**, toujours avec quatre composants par kit. Trois kits complets nécessiteraient douze composants ; un quatrième en nécessiterait seize. Le résultat attendu est donc **3 kits complets**.

![Initialiser le stock à 14 et le contenu par kit à quatre, calculer le quotient entier puis initialiser kit_count à 3.](/diagrams/examples/division-partial.svg)

<a href="/diagrams/examples/division-partial.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:division-partial -->
```cpp
int component_count = 14;
int components_per_kit = 4;
int kit_count = component_count / components_per_kit;
```

<details class="uml-panel" data-uml="division-partial">
<summary>Voir la conception UML</summary>

![Initialiser le stock à 14 et le contenu par kit à quatre, calculer le quotient entier puis initialiser kit_count à 3.](/diagrams/examples/division-partial.svg)

<a href="/diagrams/examples/division-partial.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Action UML | Correspondance C++ |
| --- | --- |
| Initialiser le stock | `component_count` reçoit `14`. |
| Fixer la quantité par kit | `components_per_kit` reçoit `4`. |
| Calculer le quotient entier | `component_count / components_per_kit` produit `3`. |
| Conserver le nombre de kits complets | La troisième déclaration initialise `kit_count` à `3`. |

La division et l’initialisation sont des étapes du raisonnement, réalisées ici dans la même déclaration. Aucun composant n’est retiré du stock ; aucun reste n’est enregistré dans une variable.

</details>

| Après l’instruction | `component_count` | `components_per_kit` | `kit_count` |
| --- | --- | --- | --- |
| Première déclaration | 14 | Pas encore créée | Pas encore créée |
| Deuxième déclaration | 14 | 4 | Pas encore créée |
| Déclaration du quotient | 14 | 4 | 3 |

En mathématiques, 14 divisé par 4 vaut **3,5**. Mais les deux opérandes de notre expression sont des `int` : **la division entière produit 3**. Elle ne fournit pas 3,5 et n’applique pas une règle d’arrondi au plus proche.

Le terme **troncature vers zéro** désigne cette règle : la partie fractionnaire est abandonnée. Avec les quantités positives ou nulles de cette leçon, le résultat compte les groupes complets. Les nombres négatifs seront étudiés séparément.

**Point important :** le quotient vaut déjà 3 lors de l’évaluation de la division. Ce n’est pas simplement le fait de le ranger dans `kit_count` qui retire la fraction. Changer seulement le type de la variable de destination ne permettrait pas de retrouver cette fraction perdue ; les divisions avec des nombres à virgule viendront avec leurs prérequis.

Dans notre raisonnement sur les kits, trois kits utiliseraient douze composants et il en resterait deux. **L’extrait ne calcule ni ne conserve ce reste** : il laisse `component_count` à 14. Le calcul du reste fera l’objet d’une étude dédiée.

## 3 — Des composants, mais pas assez pour un kit

Le stock passe à **3 composants**, et un kit en demande toujours **4**. On ne peut constituer aucun kit complet : le résultat attendu est **0**.

![Initialiser le stock à 3 et le contenu par kit à quatre, calculer le quotient entier puis initialiser kit_count à 0.](/diagrams/examples/division-insufficient.svg)

<a href="/diagrams/examples/division-insufficient.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:division-insufficient -->
```cpp
int component_count = 3;
int components_per_kit = 4;
int kit_count = component_count / components_per_kit;
```

<details class="uml-panel" data-uml="division-insufficient">
<summary>Voir la conception UML</summary>

![Initialiser le stock à 3 et le contenu par kit à quatre, calculer le quotient entier puis initialiser kit_count à 0.](/diagrams/examples/division-insufficient.svg)

<a href="/diagrams/examples/division-insufficient.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Action UML | Correspondance C++ |
| --- | --- |
| Initialiser le stock | `component_count` reçoit `3`. |
| Fixer la quantité par kit | `components_per_kit` reçoit `4`. |
| Calculer le quotient entier | `component_count / components_per_kit` produit `0`. |
| Conserver le nombre de kits complets | La troisième déclaration initialise `kit_count` à `0`. |

La division et l’initialisation sont des étapes du raisonnement, réalisées ici dans la même déclaration. Aucun composant n’est retiré du stock ; aucun reste n’est enregistré dans une variable.

</details>

| Après l’instruction | `component_count` | `components_per_kit` | `kit_count` |
| --- | --- | --- | --- |
| Première déclaration | 3 | Pas encore créée | Pas encore créée |
| Deuxième déclaration | 3 | 4 | Pas encore créée |
| Déclaration du quotient | 3 | 4 | 0 |

Le quotient mathématique 3 divisé par 4 vaut **0,75**. La division entière donne **0** : aucun groupe complet de quatre ne peut être constitué.

**Zéro kit ne veut pas dire zéro composant.** Le stock contient toujours trois composants. Le quotient répond à la question « combien de kits complets ? », pas à la question « combien de composants possède-t-on ? ».

## 4 — Aucun composant disponible

Enfin, le stock vaut **0**, avec une taille de kit qui reste à **4**. Le calcul est valide et le nombre de kits complets attendu est **0**.

![Initialiser le stock à 0 et le contenu par kit à quatre, calculer le quotient entier puis initialiser kit_count à 0.](/diagrams/examples/division-empty.svg)

<a href="/diagrams/examples/division-empty.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:division-empty -->
```cpp
int component_count = 0;
int components_per_kit = 4;
int kit_count = component_count / components_per_kit;
```

<details class="uml-panel" data-uml="division-empty">
<summary>Voir la conception UML</summary>

![Initialiser le stock à 0 et le contenu par kit à quatre, calculer le quotient entier puis initialiser kit_count à 0.](/diagrams/examples/division-empty.svg)

<a href="/diagrams/examples/division-empty.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Action UML | Correspondance C++ |
| --- | --- |
| Initialiser le stock | `component_count` reçoit `0`. |
| Fixer la quantité par kit | `components_per_kit` reçoit `4`. |
| Calculer le quotient entier | `component_count / components_per_kit` produit `0`. |
| Conserver le nombre de kits complets | La troisième déclaration initialise `kit_count` à `0`. |

La division et l’initialisation sont des étapes du raisonnement, réalisées ici dans la même déclaration. Aucun composant n’est retiré du stock ; aucun reste n’est enregistré dans une variable.

</details>

| Après l’instruction | `component_count` | `components_per_kit` | `kit_count` |
| --- | --- | --- | --- |
| Première déclaration | 0 | Pas encore créée | Pas encore créée |
| Deuxième déclaration | 0 | 4 | Pas encore créée |
| Déclaration du quotient | 0 | 4 | 0 |

Le résultat est identique au cas précédent, mais la situation de départ diffère : ici il n’y a aucun composant ; auparavant il y en avait trois. Connaître seulement `kit_count` ne suffit donc pas à retrouver le stock initial.

## Distinguer les deux places de zéro

Dans le dernier exemple, zéro est le **stock**, à gauche de `/`. Le diviseur, à droite, reste 4.

| Situation | Conclusion |
| --- | --- |
| Stock nul, quatre composants par kit | Division valide : zéro kit complet. |
| Trois composants, quatre composants par kit | Division valide : zéro kit complet, mais trois composants présents. |
| Taille de kit égale à zéro | Hors de notre besoin ; une division entière par zéro a un comportement indéfini. |

**Comportement indéfini** signifie ici que C++ ne garantit aucun résultat ni comportement utilisable. Il ne faut pas compter sur un résultat zéro, une erreur de compilation ou un arrêt systématique du programme. Nous n’exécutons donc pas de division par zéro pour l’illustrer.

Dans nos quatre extraits, le diviseur est explicitement initialisé à 4. Un programme recevant une quantité de l’extérieur devrait vérifier sa validité avant la division. Cette vérification viendra avec les conditions ; elle n’est pas réalisée par les exemples actuels.

## Comparer les résultats

| Stock disponible | Composants par kit | Kits complets calculés | Ce que le cas apporte |
| --- | --- | --- | --- |
| 12 | 4 | 3 | Division exacte. |
| 14 | 4 | 3 | La fraction ne devient pas un kit supplémentaire. |
| 3 | 4 | 0 | Un stock non nul peut être insuffisant. |
| 0 | 4 | 0 | Un dividende nul est autorisé. |

## Vérifier sa compréhension

- Pourquoi obtient-on trois kits avec quatorze composants, et non quatre ?
- Le stock est-il réduit par la déclaration de `kit_count` ?
- Un résultat nul prouve-t-il que le stock est vide ?
- Quelle donnée doit rester strictement positive dans notre besoin ?

**Repères pour te corriger :** seuls trois groupes complets de quatre sont possibles ; le stock est inchangé ; zéro kit peut correspondre à un stock trop petit ; le nombre de composants par kit doit être positif.

**À retenir :** la division entre entiers convient ici parce que le besoin porte sur des kits complets. Elle ne convient pas automatiquement à un besoin de résultat fractionnaire.

**Suite :** [mettre à jour un compteur à partir de sa valeur courante](../mise-a-jour-compteur/), puis introduire les booléens et les comparaisons dans le [parcours progressif](../../parcours/). Le calcul du reste et les nombres à virgule seront étudiés dans leurs modules dédiés. La pratique restera dans les dépôts à cloner dans ton IDE.

## Référence

La [règle de division entière](https://eel.is/c++draft/expr.mul) précise la troncature vers zéro et le comportement indéfini d’une division par zéro. Cette page présente le projet de norme C++ en HTML, pas l’édition ISO C++17 publiée. Les quatre extraits de la leçon sont vérifiés en mode C++17, avec des diviseurs strictement positifs.
