---
title: "Premières multiplications — compter des groupes identiques"
description: "Calculer le contenu de plusieurs kits, distinguer quantité par kit et total, puis vérifier le choix de l’opération."
---

**Objectif :** choisir la multiplication pour compter des groupes de même taille et expliquer le résultat. **Prérequis :** [lire une expression](../premieres-expressions/) ; la [soustraction](../premieres-soustractions/) a déjà montré qu’une formule peut compiler sans respecter le besoin.

**Disponible :** cinq exemples de lecture avec leurs cartes UML. Le projet de pratique autonome à cloner n’est pas encore publié.

## Comprendre ce que nous comptons

Nous préparons **3 kits contenant chacun 4 composants**. Le besoin est de connaître le nombre de composants contenus dans l’ensemble des kits : **12**.

On peut compter quatre composants pour le premier kit, quatre pour le deuxième et quatre pour le troisième : **4 + 4 + 4 = 12**. La multiplication exprime directement ce regroupement : **3 × 4 = 12**. Cette explication ne signifie pas que le processeur effectuera trois additions ou que notre code contient une boucle.

Les deux données ont des rôles différents : le **nombre de kits**, et le **nombre de composants par kit**. Tous les kits ont ici le même contenu. Si leurs contenus diffèrent, multiplier par une seule quantité commune ne décrit plus nécessairement le besoin.

Pour ces exemples, nous choisissons des quantités connues de 0 à 10, donc des produits de 0 à 100, représentables par `int`. Cette hypothèse n’est pas un contrôle d’entrée ni une description des limites générales du type.

Chaque fragment ci-dessous se lit indépendamment, dans le corps de `main`. Les tableaux indiquent les valeurs obtenues : aucun extrait ne contient d’affichage, ne fabrique un kit et ne pilote du matériel.

## 1 — Écrire la multiplication

La conception prévoit de calculer **3 fois 4**, puis de créer `component_count`, le nombre total de composants, avec le résultat **12**.

![Calculer trois fois quatre et initialiser le total à douze.](/diagrams/examples/multiplication-literal.svg)

<a href="/diagrams/examples/multiplication-literal.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:multiplication-literal -->
```cpp
int component_count = 3 * 4;
```

<details class="uml-panel" data-uml="multiplication-literal">
<summary>Voir la conception UML</summary>

![Calculer trois fois quatre et initialiser le total à douze.](/diagrams/examples/multiplication-literal.svg)

<a href="/diagrams/examples/multiplication-literal.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Conception attendue | Correspondance C++ |
| --- | --- |
| Calculer le produit | `3 * 4` donne `12`. |
| Initialiser le total | La déclaration crée `component_count` avec `12`. |

Calculer puis initialiser sont deux étapes du raisonnement. Une déclaration peut réaliser les deux ; le diagramme n’impose ni variable intermédiaire ni nombre d’instructions du processeur.

</details>

En C++, la multiplication s’écrit avec **l’astérisque `*`**, pas avec la lettre `x` ni le signe typographique `×`. Ici, il est placé entre les deux nombres : les opérandes sont 3 et 4, et leur **produit** est 12.

Le `=` sert à initialiser la nouvelle variable avec ce résultat. La variable conserve **12**, pas une formule qui serait recalculée automatiquement.

Dans l’activité UML, le point noir marque le début, les rectangles arrondis les actions et le symbole final la fin du fragment. Cette fin n’ajoute pas d’instruction `return`.

## 2 — Distinguer le nombre de kits et leur contenu

Nommons maintenant les deux données. `kit_count` compte les kits ; `components_per_kit` indique le nombre de composants dans **un** kit. Nous voulons conserver leurs valeurs 3 et 4 et créer le total 12.

![Initialiser trois kits et quatre composants par kit, puis calculer et conserver douze composants.](/diagrams/examples/multiplication-named.svg)

<a href="/diagrams/examples/multiplication-named.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:multiplication-named -->
```cpp
int kit_count = 3;
int components_per_kit = 4;
int component_count = kit_count * components_per_kit;
```

<details class="uml-panel" data-uml="multiplication-named">
<summary>Voir la conception UML</summary>

![Initialiser trois kits et quatre composants par kit, puis calculer et conserver douze composants.](/diagrams/examples/multiplication-named.svg)

<a href="/diagrams/examples/multiplication-named.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Conception attendue | Correspondance C++ |
| --- | --- |
| Initialiser le nombre de kits | `int kit_count = 3;` |
| Initialiser le contenu d’un kit | `int components_per_kit = 4;` |
| Calculer et conserver le total | `kit_count * components_per_kit` initialise `component_count` à `12`. |

Calculer puis initialiser sont deux étapes du raisonnement. Une déclaration peut réaliser les deux ; le diagramme n’impose ni variable intermédiaire ni nombre d’instructions du processeur.

</details>

| Après l’instruction | `kit_count` | `components_per_kit` | `component_count` |
| --- | --- | --- | --- |
| Première déclaration | 3 | Pas encore créée | Pas encore créée |
| Deuxième déclaration | 3 | 4 | Pas encore créée |
| Déclaration du total | 3 | 4 | 12 |

Le calcul se lit : **nombre de kits × composants par kit = nombre de composants**. Lire les deux variables pour les multiplier ne les modifie pas. À la fin, elles valent toujours 3 et 4 ; seule la nouvelle variable contient 12.

Nous ne multiplions donc pas deux stocks indépendants : l’une des données exprime la quantité associée à chaque groupe.

## 3 — Que se passe-t-il avec un seul kit ?

Changeons uniquement le nombre de kits : il passe de 3 à **1**. Le contenu par kit reste **4**. Le total attendu est donc **4 composants**.

![Un kit de quatre composants donne un total de quatre.](/diagrams/examples/multiplication-one.svg)

<a href="/diagrams/examples/multiplication-one.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:multiplication-one -->
```cpp
int kit_count = 1;
int components_per_kit = 4;
int component_count = kit_count * components_per_kit;
```

<details class="uml-panel" data-uml="multiplication-one">
<summary>Voir la conception UML</summary>

![Un kit de quatre composants donne un total de quatre.](/diagrams/examples/multiplication-one.svg)

<a href="/diagrams/examples/multiplication-one.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Conception attendue | Correspondance C++ |
| --- | --- |
| Initialiser les données | `kit_count` vaut `1` et `components_per_kit` vaut `4`. |
| Calculer le produit | `1 * 4` donne `4`. |
| Conserver le total | La dernière déclaration initialise `component_count` à `4`. |

Calculer puis initialiser sont deux étapes du raisonnement. Une déclaration peut réaliser les deux ; le diagramme n’impose ni variable intermédiaire ni nombre d’instructions du processeur.

</details>

| Après l’instruction | `kit_count` | `components_per_kit` | `component_count` |
| --- | --- | --- | --- |
| Première déclaration | 1 | Pas encore créée | Pas encore créée |
| Deuxième déclaration | 1 | 4 | Pas encore créée |
| Déclaration du total | 1 | 4 | 4 |

**Multiplier ne rend pas toujours une quantité plus grande.** Un seul groupe de quatre contient quatre éléments. Le total est ici égal au nombre de composants par kit, mais les deux variables gardent des rôles différents.

## 4 — Et lorsqu’il n’y a aucun kit ?

Changeons encore uniquement le nombre de kits : **0**. La description d’un kit prévoit toujours quatre composants, mais aucun kit n’est présent. Le total attendu dans les kits est **0**.

![Zéro kit de quatre composants donne un total de zéro.](/diagrams/examples/multiplication-zero.svg)

<a href="/diagrams/examples/multiplication-zero.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:multiplication-zero -->
```cpp
int kit_count = 0;
int components_per_kit = 4;
int component_count = kit_count * components_per_kit;
```

<details class="uml-panel" data-uml="multiplication-zero">
<summary>Voir la conception UML</summary>

![Zéro kit de quatre composants donne un total de zéro.](/diagrams/examples/multiplication-zero.svg)

<a href="/diagrams/examples/multiplication-zero.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Conception attendue | Correspondance C++ |
| --- | --- |
| Initialiser les données | `kit_count` vaut `0` et `components_per_kit` vaut `4`. |
| Calculer le produit | `0 * 4` donne `0`. |
| Conserver le total | La dernière déclaration initialise `component_count` à `0`. |

Calculer puis initialiser sont deux étapes du raisonnement. Une déclaration peut réaliser les deux ; le diagramme n’impose ni variable intermédiaire ni nombre d’instructions du processeur.

</details>

| Après l’instruction | `kit_count` | `components_per_kit` | `component_count` |
| --- | --- | --- | --- |
| Première déclaration | 0 | Pas encore créée | Pas encore créée |
| Deuxième déclaration | 0 | 4 | Pas encore créée |
| Déclaration du total | 0 | 4 | 0 |

Les **4 composants par kit** décrivent le contenu d’un kit ; ce n’est pas un stock de quatre composants déjà présent. Avec zéro kit, le produit donne zéro. Nous connaissons ici l’absence de kits : zéro ne remplace pas une donnée inconnue.

## 5 — Une addition peut compiler et répondre à la mauvaise question

Reprenons le besoin initial : **3 kits de 4 composants, soit 12 composants attendus**. Le diagramme de référence reste celui du deuxième exemple.

**Erreur volontaire :** seule l’opération change dans la dernière ligne. Nous utilisons `+` à la place de `*`.

<!-- example:multiplication-wrong -->
```cpp
int kit_count = 3;
int components_per_kit = 4;
int component_count = kit_count + components_per_kit;
```

<details class="uml-panel" data-uml="multiplication-wrong">
<summary>Comprendre l’écart avec la conception</summary>

**Conception attendue : 12 ; résultat du code incorrect : 7.** Le diagramme décrit le calcul attendu, pas l’exécution de l’addition incorrecte.

![Initialiser trois kits et quatre composants par kit, puis calculer et conserver douze composants.](/diagrams/examples/multiplication-named.svg)

<a href="/diagrams/examples/multiplication-named.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Conception attendue | Correspondance C++ |
| --- | --- |
| Garder les données 3 et 4 | Les deux premières déclarations sont correctes. |
| Multiplier kits et contenu par kit | Le code additionne à tort `kit_count + components_per_kit`. |
| Obtenir 12 composants | Le code conserve en réalité `7`. |

L’écart porte sur l’opérateur, pas sur les valeurs initiales.

</details>

Ce code calcule **3 + 4 = 7**. Il additionne un nombre de kits et une quantité par kit : cela ne donne pas le nombre de composants demandé. Les entrées restent 3 et 4.

Les deux données sont des `int`. Le compilateur accepte leur addition ; leurs noms ne lui imposent pas de vérifier les unités ni notre intention.

**Correction :** retrouver `kit_count * components_per_kit`, comme dans le deuxième exemple. Les valeurs initiales sont bonnes ; c’est le choix de l’opérateur qui est incorrect.

## Choisir des valeurs qui révèlent une erreur

Imaginons maintenant que nous ayons vérifié les deux formules uniquement avec **2 kits de 2 composants**. Le résultat attendu serait 4, et l’addition incorrecte donnerait elle aussi 4.

| Nombre de kits | Composants par kit | Produit attendu | Addition incorrecte | L’écart est-il visible ? |
| --- | --- | --- | --- | --- |
| 3 | 4 | 12 | 7 | Oui |
| 2 | 2 | 4 | 4 | Non |

Ce tableau réutilise les deux expressions précédentes avec des données différentes. **Obtenir le bon nombre une fois ne prouve pas que la formule est bonne.** Les valeurs 3 et 4 permettent de distinguer les formules ; 2 et 2 masquent cette erreur précise.

Le besoin reste la référence : le résultat attendu vient du comptage des composants dans les kits. On ne décide pas qu’une formule est correcte uniquement parce qu’elle produit une valeur plausible. Même plusieurs exemples réussis ne remplacent pas ce raisonnement.

## Vérifier sa compréhension

Avant de relire les explications, essaie de répondre :

- Quelle différence y a-t-il entre `components_per_kit` et `component_count` ?
- Pourquoi un seul kit donne-t-il quatre composants, et zéro kit aucun ?
- Pourquoi l’addition incorrecte peut-elle passer inaperçue avec 2 et 2 ?

**Repères pour te corriger :** la première donnée décrit un kit, la seconde le total ; le nombre de groupes détermine combien de fois compter leur contenu ; avec 2 et 2, somme et produit coïncident sans que les deux formules répondent au même besoin général.

**Suite :** [regrouper les calculs avec des parenthèses](../parentheses-calculs/). La division et la mise à jour d’une variable suivront dans le [parcours progressif](../../parcours/). Les exercices pratiques resteront dans les dépôts dédiés à cloner dans ton IDE.

## Référence

L’[opérateur de multiplication](https://eel.is/c++draft/expr.mul) est décrit dans cette présentation HTML du projet de norme C++. Ce document évolutif n’est pas l’édition ISO C++17 publiée. Les cinq fragments et les résultats comparés de cette fiche sont vérifiés en mode C++17.
