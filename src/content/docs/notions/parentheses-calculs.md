---
title: "Parenthèses — regrouper les calculs selon le besoin"
description: "Comparer calcul par étapes, expression parenthésée et priorités à partir de deux besoins concrets."
---

**Objectif :** choisir ce qu’il faut regrouper pour traduire un besoin en calcul. **Prérequis :** [lire une addition](../premieres-expressions/) et [compter des groupes par multiplication](../premieres-multiplications/).

**Disponible :** cinq exemples de lecture avec leurs cartes UML. Le projet de pratique autonome correspondant n’est pas encore publié.

## Quel total voulons-nous obtenir ?

Nous possédons **3 kits** et en ajoutons **2 autres**. Chaque kit contient **4 composants**. Nous voulons compter les composants contenus dans **tous les kits**.

Avant d’écrire du code, nous prévoyons : **3 + 2 = 5 kits**, puis **5 × 4 = 20 composants**. Ce résultat attendu sert de référence aux quatre premiers exemples. Le cinquième changera explicitement le besoin.

Les quantités sont connues, comprises entre 0 et 10, et le contenu par kit est identique. Pour ce besoin, le nombre total de kits atteint au plus 20 et leur contenu total au plus 200 composants, ce qui convient à `int`. Ces hypothèses ne sont pas des contrôles réalisés par le code.

Chaque fragment est indépendant et se placerait dans le corps de `main`. Aucun n’affiche les valeurs ou ne manipule réellement du matériel. Les tableaux sont des traces de lecture, pas la sortie du programme.

## 1 — Nommer le résultat intermédiaire

Commençons avec des instructions déjà connues : créer les trois données, calculer le nombre total de kits dans `total_kit_count`, puis utiliser cette valeur pour calculer `component_count`.

![Initialiser les trois données, conserver cinq kits dans total_kit_count puis vingt composants dans component_count.](/diagrams/examples/grouping-intermediate.svg)

<a href="/diagrams/examples/grouping-intermediate.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:grouping-intermediate -->
```cpp
int existing_kit_count = 3;
int additional_kit_count = 2;
int components_per_kit = 4;
int total_kit_count = existing_kit_count + additional_kit_count;
int component_count = total_kit_count * components_per_kit;
```

<details class="uml-panel" data-uml="grouping-intermediate">
<summary>Voir la conception UML</summary>

![Initialiser les trois données, conserver cinq kits dans total_kit_count puis vingt composants dans component_count.](/diagrams/examples/grouping-intermediate.svg)

<a href="/diagrams/examples/grouping-intermediate.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Conception | Correspondance avec le code |
| --- | --- |
| Initialiser les données | Les trois premières déclarations donnent `3`, `2` et `4`. |
| Conserver le nombre total de kits | `total_kit_count` reçoit la somme `5`. |
| Conserver le nombre de composants | `component_count` reçoit le produit `20`. |

</details>

| Après la déclaration de… | Nouvelle valeur | Signification |
| --- | --- | --- |
| `existing_kit_count` | 3 | Kits déjà présents. |
| `additional_kit_count` | 2 | Kits supplémentaires. |
| `components_per_kit` | 4 | Composants dans chaque kit. |
| `total_kit_count` | 5 | Nombre total de kits. |
| `component_count` | 20 | Nombre total de composants. |

Les données d’entrée restent 3, 2 et 4. `total_kit_count` est ici une **vraie variable**, créée par sa déclaration et lue dans la suivante.

Cette écriture est correcte et rend les étapes visibles. La version suivante n’est pas une obligation de raccourcir le code : elle montre une autre façon d’exprimer le même calcul.

## 2 — Regrouper la somme avec des parenthèses

Le besoin ne change pas : compter les cinq kits, puis leurs vingt composants. Nous utilisons maintenant la somme directement comme une des deux quantités à multiplier.

![Initialiser les trois données, calculer cinq kits puis vingt composants sans variable intermédiaire nommée.](/diagrams/examples/grouping-grouped.svg)

<a href="/diagrams/examples/grouping-grouped.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:grouping-grouped -->
```cpp
int existing_kit_count = 3;
int additional_kit_count = 2;
int components_per_kit = 4;
int component_count = (existing_kit_count + additional_kit_count) * components_per_kit;
```

<details class="uml-panel" data-uml="grouping-grouped">
<summary>Voir la conception UML</summary>

![Initialiser les trois données, calculer cinq kits puis vingt composants sans variable intermédiaire nommée.](/diagrams/examples/grouping-grouped.svg)

<a href="/diagrams/examples/grouping-grouped.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Conception | Correspondance avec le code |
| --- | --- |
| Regrouper le nombre de kits | `(existing_kit_count + additional_kit_count)` produit `5`. |
| Multiplier cette somme | Le résultat de la somme est multiplié par `components_per_kit`, soit `4`. |
| Conserver le total | La dernière déclaration initialise `component_count` à `20`. |

</details>

Les parenthèses ouvrante `(` et fermante `)` délimitent la somme qui sert d’opérande à la multiplication. Le calcul se lit **« la somme des deux nombres de kits, multipliée par le contenu d’un kit »**.

| Partie de l’expression | Valeur | Ce qu’elle représente |
| --- | --- | --- |
| `(existing_kit_count + additional_kit_count)` | 5 | Tous les kits. |
| Cette somme multipliée par `components_per_kit` | 20 | Tous leurs composants. |

La valeur intermédiaire 5 apparaît dans notre explication, mais **aucune variable `total_kit_count` n’est créée dans cet extrait**. La seule nouvelle variable après les trois entrées est `component_count`.

Les activités UML décrivent les étapes nécessaires au raisonnement : le point noir ouvre l’activité, les actions sont dans les rectangles arrondis et le symbole final termine le fragment. Elles ne décrivent pas les instructions du processeur. Les parenthèses définissent un regroupement ; elles ne constituent pas une règle générale imposant l’ordre de lecture de tous les opérandes.

## 3 — Omettre les parenthèses change le calcul

Nous voulons toujours **20 composants dans les cinq kits**. Retirons seulement les parenthèses autour de la somme : c’est une **erreur volontaire par rapport à ce besoin**.

<!-- example:grouping-omitted -->
```cpp
int existing_kit_count = 3;
int additional_kit_count = 2;
int components_per_kit = 4;
int component_count = existing_kit_count + additional_kit_count * components_per_kit;
```

<details class="uml-panel" data-uml="grouping-omitted">
<summary>Comprendre l’écart avec la conception</summary>

**Conception attendue : 20 ; résultat de cet extrait : 11.** Ce diagramme décrit le besoin des cinq kits, pas l’exécution de la formule incorrecte.

![Initialiser les trois données, calculer cinq kits puis vingt composants sans variable intermédiaire nommée.](/diagrams/examples/grouping-grouped.svg)

<a href="/diagrams/examples/grouping-grouped.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Conception | Correspondance avec le code |
| --- | --- |
| Additionner les deux nombres de kits | La formule ne regroupe plus leur somme. |
| Multiplier le nombre total de kits par 4 | Le produit porte seulement sur `additional_kit_count` et `components_per_kit`. |
| Obtenir 20 composants | Le code conserve en réalité `11`. |

</details>

Dans cette expression, **`*` est prioritaire sur `+`** : la multiplication forme un groupe plus serré que l’addition. Ce n’est donc pas une lecture arithmétique systématiquement de gauche à droite.

| Décomposition du calcul écrit | Valeur |
| --- | --- |
| `additional_kit_count * components_per_kit` | 2 × 4 = 8 |
| `existing_kit_count` ajouté à ce produit | 3 + 8 = 11 |

Le fragment compile, mais `component_count` vaut **11**, pas 20. Il additionne ici un nombre de kits à un nombre de composants. Les noms rendent cette incohérence visible pour nous ; ils n’imposent pas au compilateur de vérifier les unités.

**Correction :** regrouper `existing_kit_count + additional_kit_count`, comme dans le deuxième exemple. Les données initiales restent bonnes.

## 4 — Entourer toute l’expression ne corrige pas son intérieur

Essayons une autre écriture, toujours pour le besoin des cinq kits : des parenthèses entourent maintenant **l’expression entière**. Cette variante est elle aussi volontairement incorrecte pour le résultat attendu de 20.

<!-- example:grouping-outer -->
```cpp
int existing_kit_count = 3;
int additional_kit_count = 2;
int components_per_kit = 4;
int component_count = (existing_kit_count + additional_kit_count * components_per_kit);
```

<details class="uml-panel" data-uml="grouping-outer">
<summary>Comprendre l’écart avec la conception</summary>

**Conception attendue : 20 ; résultat de cet extrait : 11.** Ce diagramme décrit le besoin des cinq kits, pas l’exécution de la formule incorrecte.

![Initialiser les trois données, calculer cinq kits puis vingt composants sans variable intermédiaire nommée.](/diagrams/examples/grouping-grouped.svg)

<a href="/diagrams/examples/grouping-grouped.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Conception | Correspondance avec le code |
| --- | --- |
| Utiliser la somme des kits comme opérande du produit | Les parenthèses englobent toute l’expression, pas seulement cette somme. |
| Obtenir 20 | Le regroupement interne reste identique au cas précédent : le résultat est `11`. |

</details>

L’intérieur des parenthèses reste la même expression qu’au cas précédent : le produit donne **8**, puis l’addition donne **11**. Les parenthèses sont présentes, mais elles ne délimitent pas la somme que notre besoin exige de multiplier.

Pour les **mêmes données et le même besoin**, comparons les quatre écritures :

| Écriture étudiée | Résultat | Conforme aux cinq kits ? |
| --- | --- | --- |
| Somme conservée dans une variable, puis multiplication | 20 | Oui |
| Somme parenthésée : `(3 + 2) * 4` | 20 | Oui |
| Sans regroupement de la somme : `3 + 2 * 4` | 11 | Non |
| Parenthèses extérieures : `(3 + 2 * 4)` | 11 | Non |

Ce n’est pas le nombre de parenthèses qui rend un calcul correct : c’est ce qu’elles regroupent.

## 5 — Changer de besoin : trois composants en vrac et deux kits

**Attention : le besoin change ici.** Nous ne possédons plus trois kits initiaux. Nous possédons **3 composants en vrac**, auxquels s’ajoutent **2 kits de 4 composants**.

Les kits contiennent 8 composants ; avec les trois en vrac, nous attendons donc **11 composants**. Nous gardons les mêmes nombres pour observer ce qui change dans leur signification.

![Compter huit composants dans les kits, ajouter les trois composants en vrac puis conserver onze composants.](/diagrams/examples/grouping-loose.svg)

<a href="/diagrams/examples/grouping-loose.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:grouping-loose -->
```cpp
int loose_component_count = 3;
int kit_count = 2;
int components_per_kit = 4;
int component_count = loose_component_count + kit_count * components_per_kit;
```

<details class="uml-panel" data-uml="grouping-loose">
<summary>Voir la conception UML</summary>

![Compter huit composants dans les kits, ajouter les trois composants en vrac puis conserver onze composants.](/diagrams/examples/grouping-loose.svg)

<a href="/diagrams/examples/grouping-loose.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Conception | Correspondance avec le code |
| --- | --- |
| Compter les composants dans les kits | `kit_count * components_per_kit` donne `8`. |
| Ajouter les composants en vrac | `loose_component_count` ajoute `3` à ce produit. |
| Conserver le bon total pour ce nouveau besoin | `component_count` reçoit `11`. |

</details>

| Donnée ou calcul | Valeur et unité |
| --- | --- |
| `loose_component_count` | 3 composants |
| `kit_count` | 2 kits |
| `components_per_kit` | 4 composants par kit |
| Produit du nombre de kits par leur contenu | 8 composants |
| Total avec les composants en vrac | 11 composants |

Cette fois, l’addition réunit bien deux quantités de composants. La priorité de la multiplication traduit directement le besoin : **l’expression sans parenthèses est correcte ici**.

Ce n’est pas une correction du troisième exemple par un simple changement de nom. Nous avons changé ce que représente la première donnée, donc le besoin lui-même. Pour les cinq kits des quatre premiers exemples, 20 reste le résultat attendu.

## Vérifier sa compréhension

- Pourquoi conserve-t-on une vraie variable `total_kit_count` dans le premier extrait, mais pas dans le deuxième ?
- Quelles parenthèses faut-il placer pour multiplier le nombre total de kits ?
- Pourquoi 11 est-il incorrect au troisième exemple, mais correct au cinquième ?

**Repères pour te corriger :** seul le premier extrait déclare la variable intermédiaire ; il faut regrouper la somme des kits ; au dernier exemple, les trois unités initiales sont des composants en vrac, pas des kits.

**À retenir :** partir du besoin et des unités, repérer les groupes du calcul, puis vérifier le résultat. Une écriture en plusieurs instructions reste un choix valable lorsqu’elle rend le raisonnement plus clair.

**Suite :** [compter les kits complets avec la division d’entiers](../premieres-divisions/). La mise à jour d’une variable à partir de son ancienne valeur suivra dans le [parcours progressif](../../parcours/). Les fiches téléchargeables et les évaluations interactives restent prévues pour plus tard.

## Références

Les règles des [expressions parenthésées](https://eel.is/c++draft/expr.prim.paren) et la structure des [expressions additives](https://eel.is/c++draft/expr.add) expliquent ces regroupements. Ces pages présentent le projet de norme C++ en HTML, pas l’édition ISO C++17 publiée. Les cinq fragments de cette leçon sont vérifiés en mode C++17.
