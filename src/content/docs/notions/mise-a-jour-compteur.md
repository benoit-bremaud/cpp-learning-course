---
title: "Mettre à jour un compteur — repartir de la valeur courante"
description: "Lire une valeur, calculer sa nouvelle valeur et la conserver : six exemples avec conception UML."
---

**Objectif :** modifier une variable à partir de sa valeur courante. **Prérequis :** [initialiser et affecter une variable](../cpp-01/), [calculer une addition](../premieres-expressions/) et [comprendre une soustraction](../premieres-soustractions/).

**Disponible :** six exemples de lecture et leurs cartes UML. Le projet de pratique autonome à cloner pour cette leçon n’est pas encore publié.

## Partir du besoin : conserver un nombre qui évolue

Un compteur doit conserver ce qui a déjà été compté, puis prendre en compte une quantité supplémentaire. Écrire une valeur fixe ne suffit pas : il faut utiliser la valeur courante pour calculer la suivante.

Chaque extrait est **indépendant**, à lire dans le corps de `main` : ce ne sont pas six morceaux à coller dans le même bloc. Les extraits n’affichent rien ; les tableaux montrent les valeurs observées après chaque instruction.

Nous utilisons des entiers compris entre **0 et 20**, résultats intermédiaires inclus. Pour le retrait, la quantité utilisée ne dépasse pas le stock. Ces hypothèses rendent nos exemples simples ; **le code ne vérifie pas ces limites**. Un `int` ne peut pas augmenter sans limite : les bornes des types seront étudiées avant les compteurs de longue durée.

## 1 — Ajouter une mesure au compteur

Nous représentons un nombre de mesures déjà comptabilisées. Il vaut **0**, puis nous voulons lui ajouter **une mesure** : le résultat attendu est **1**. Nous écrivons seulement la mise à jour du nombre ; aucune mesure de capteur n’est effectuée.

![Activité UML : ajouter une mesure au compteur.](/diagrams/examples/counter-single.svg)

<a href="/diagrams/examples/counter-single.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

Dans le diagramme d’activité UML, le point noir marque le début, les rectangles arrondis les actions et les flèches leur enchaînement. Le symbole final termine le fragment, sans ajouter de `return`. Calculer et affecter sont des étapes du raisonnement : le diagramme ne crée pas de variable intermédiaire et ne décrit pas les instructions du processeur.

<!-- example:counter-single -->
```cpp
int measurement_count = 0;
measurement_count = measurement_count + 1;
```

<details class="uml-panel" data-uml="counter-single">
<summary>Voir la conception UML</summary>

| Étape du raisonnement | Code et valeur |
| --- | --- |
| Créer le compteur | `int measurement_count = 0;` initialise la variable à 0. |
| Calculer la valeur suivante | `measurement_count + 1` utilise 0 et produit 1. |
| Remplacer la valeur courante | L’affectation conserve 1 dans la même variable. |

![Activité UML : ajouter une mesure au compteur.](/diagrams/examples/counter-single.svg)

<a href="/diagrams/examples/counter-single.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

| Après l’instruction | `measurement_count` |
| --- | --- |
| Déclaration | 0 |
| Mise à jour | 1 |

Lis la deuxième ligne comme « prendre la valeur actuelle, lui ajouter un, puis conserver le résultat dans le compteur ». À droite de `=`, le nom sert à **lire** la valeur ; à gauche, il désigne la variable à **modifier**.

Ce n’est pas une égalité mathématique qui affirmerait qu’un nombre est égal à lui-même plus un. Ici, `=` exprime une affectation. Le compteur existe déjà : on ne remet pas `int` devant son nom.

L’addition seule calcule une valeur ; c’est l’affectation qui la conserve. Le calcul et le remplacement sont deux étapes de notre explication, réalisées par une seule instruction C++.

## 2 — Effectuer deux mises à jour successives

Partons à nouveau de **0**, dans un extrait indépendant. Deux mesures sont à comptabiliser, une par mise à jour. Nous attendons **0 → 1 → 2**.

![Activité UML : effectuer deux mises à jour successives.](/diagrams/examples/counter-repeated.svg)

<a href="/diagrams/examples/counter-repeated.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:counter-repeated -->
```cpp
int measurement_count = 0;
measurement_count = measurement_count + 1;
measurement_count = measurement_count + 1;
```

<details class="uml-panel" data-uml="counter-repeated">
<summary>Voir la conception UML</summary>

| Action UML | Correspondance C++ |
| --- | --- |
| Initialiser le compteur | La déclaration donne 0. |
| Calculer puis conserver 1 | La première affectation utilise 0 + 1. |
| Calculer puis conserver 2 | La seconde affectation utilise désormais 1 + 1. |

![Activité UML : effectuer deux mises à jour successives.](/diagrams/examples/counter-repeated.svg)

<a href="/diagrams/examples/counter-repeated.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

| Après l’instruction | Valeur utilisée par l’addition | `measurement_count` |
| --- | --- | --- |
| Déclaration | Aucune addition | 0 |
| Première mise à jour | 0 | 1 |
| Deuxième mise à jour | 1 | 2 |

Les deux dernières lignes ont exactement le même texte, mais pas la même valeur de départ. La seconde lit **1**, puisque la première a déjà modifié le compteur.

Il n’y a aucune boucle : nous avons écrit deux instructions, exécutées dans l’ordre. Le programme ne recommence pas indéfiniment et ne cherche pas à savoir si un capteur a produit une nouvelle mesure.

## 3 — Continuer à partir de cinq

Le nombre de mesures déjà comptabilisées est maintenant **5**. Deux mises à jour doivent l’amener à **7**, en passant par **6**. La valeur initiale est connue et écrite dans le code ; nous ne la récupérons pas depuis une mémoire persistante.

![Activité UML : continuer à partir de cinq.](/diagrams/examples/counter-resumed.svg)

<a href="/diagrams/examples/counter-resumed.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:counter-resumed -->
```cpp
int measurement_count = 5;
measurement_count = measurement_count + 1;
measurement_count = measurement_count + 1;
```

<details class="uml-panel" data-uml="counter-resumed">
<summary>Voir la conception UML</summary>

| Action UML | Correspondance C++ |
| --- | --- |
| Initialiser à cinq | La déclaration donne 5. |
| Ajouter une mesure | La première affectation remplace 5 par 6. |
| Ajouter encore une mesure | La seconde remplace 6 par 7. |

![Activité UML : continuer à partir de cinq.](/diagrams/examples/counter-resumed.svg)

<a href="/diagrams/examples/counter-resumed.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

| Après l’instruction | `measurement_count` |
| --- | --- |
| Déclaration | 5 |
| Première mise à jour | 6 |
| Deuxième mise à jour | 7 |

La règle ne dépend pas d’un départ à zéro. Elle dépend de la **valeur courante** à chaque exécution. Recommencer le programme depuis sa déclaration à 5 ferait repartir cet exemple de 5 : aucune sauvegarde automatique n’est réalisée.

## 4 — Comprendre pourquoi affecter un ne compte pas

Reprenons le besoin du deuxième exemple : partir de **0** et comptabiliser deux mesures, pour finir à **2**. Sa conception UML reste notre référence. **Erreur volontaire :** les deux affectations ci-dessous remplacent systématiquement la valeur par 1.

La conception attendue est celle de la section « Effectuer deux mises à jour successives » ; la carte précise l’écart avec ce code.

<!-- example:counter-reset -->
```cpp
int measurement_count = 0;
measurement_count = 1;
measurement_count = 1;
```

<details class="uml-panel" data-uml="counter-reset">
<summary>Comprendre l’écart avec la conception</summary>

**Attendu : 0 → 1 → 2 ; obtenu : 0 → 1 → 1.** Le diagramme représente la conception attendue du deuxième exemple, pas l’exécution de cet extrait volontairement incorrect pour le besoin.

| Conception attendue | Écart dans le code |
| --- | --- |
| Initialiser à 0 | La déclaration respecte le besoin. |
| Ajouter un à la valeur courante | Les affectations ne lisent pas cette valeur ; elles écrivent 1. |
| Finir à 2 après deux mises à jour | Le compteur reste à 1. |

![Activité UML : ajouter deux mesures pour atteindre deux, conception attendue.](/diagrams/examples/counter-repeated.svg)

<a href="/diagrams/examples/counter-repeated.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

| Après l’instruction | Valeur attendue | Valeur obtenue |
| --- | --- | --- |
| Déclaration | 0 | 0 |
| Première affectation | 1 | 1 |
| Deuxième affectation | 2 | 1 |

**Le premier résultat masque l’erreur** : à partir de zéro, ajouter un et remplacer par un donnent tous deux 1. La deuxième étape révèle la différence. En partant de 5, remplacer par 1 échouerait dès la première mise à jour : nous attendrions 6.

Ce code compile. Il est autorisé par C++, mais ne réalise pas le comptage demandé. La correction est celle du deuxième exemple : calculer `measurement_count + 1` avant d’affecter le résultat.

## 5 — Ajouter plusieurs composants en une fois

Transférons le même raisonnement à un stock. Nous avons **5 composants** et recevons un lot de **3**. Le stock numérique doit passer à **8** ; la quantité du lot reste **3**.

![Activité UML : ajouter plusieurs composants en une fois.](/diagrams/examples/counter-batch.svg)

<a href="/diagrams/examples/counter-batch.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:counter-batch -->
```cpp
int component_count = 5;
int added_count = 3;
component_count = component_count + added_count;
```

<details class="uml-panel" data-uml="counter-batch">
<summary>Voir la conception UML</summary>

| Action UML | Correspondance C++ |
| --- | --- |
| Initialiser les quantités | Le stock vaut 5, le lot vaut 3. |
| Calculer le nouveau stock | `component_count + added_count` produit 8. |
| Mettre à jour le stock | L’affectation remplace la valeur de `component_count` par 8. |

![Activité UML : ajouter plusieurs composants en une fois.](/diagrams/examples/counter-batch.svg)

<a href="/diagrams/examples/counter-batch.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

| Après l’instruction | `component_count` | `added_count` |
| --- | --- | --- |
| Déclaration du stock | 5 | Pas encore créée |
| Déclaration du lot | 5 | 3 |
| Mise à jour | 8 | 3 |

La quantité ajoutée porte un nom et n’est plus forcément 1. Le mécanisme reste le même : lire, calculer, remplacer. Seule la variable à gauche de l’affectation est modifiée ; lire `added_count` ne la transforme pas en zéro.

Contrairement aux premiers exemples d’addition qui créaient une variable pour le total, nous modifions ici **le stock existant**. Sa valeur initiale 5 n’est plus conservée dans `component_count`. Le code ne déplace aucun composant physique.

## 6 — Retirer des composants du stock

Un autre stock contient **8 composants**, dont **2** sont utilisés. Nous voulons que sa valeur courante devienne **6**, tout en conservant **2** dans la quantité utilisée.

![Activité UML : retirer des composants du stock.](/diagrams/examples/counter-withdrawal.svg)

<a href="/diagrams/examples/counter-withdrawal.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:counter-withdrawal -->
```cpp
int component_count = 8;
int used_count = 2;
component_count = component_count - used_count;
```

<details class="uml-panel" data-uml="counter-withdrawal">
<summary>Voir la conception UML</summary>

| Action UML | Correspondance C++ |
| --- | --- |
| Initialiser les quantités | Le stock vaut 8, la quantité utilisée vaut 2. |
| Calculer le stock restant | `component_count - used_count` produit 6. |
| Mettre à jour le stock | L’affectation remplace 8 par 6 dans `component_count`. |

![Activité UML : retirer des composants du stock.](/diagrams/examples/counter-withdrawal.svg)

<a href="/diagrams/examples/counter-withdrawal.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

| Après l’instruction | `component_count` | `used_count` |
| --- | --- | --- |
| Déclaration du stock | 8 | Pas encore créée |
| Déclaration de la quantité utilisée | 8 | 2 |
| Mise à jour | 6 | 2 |

Le stock se trouve à gauche de `-` : nous retirons la quantité utilisée au stock courant. Comme pour l’addition, le résultat remplace ensuite la valeur du stock.

Avec une quantité utilisée de **0**, le stock resterait à 8. Avec une quantité de **8**, il deviendrait 0. Retirer plus que le stock disponible ne respecte pas notre hypothèse : le code ne contient pas encore de vérification pour l’interdire.

## Vérifier sa compréhension

Essaie de répondre sans regarder les tableaux :

- Si le compteur vaut 9, quelle valeur aura-t-il après deux ajouts successifs de 1 ?
- Pourquoi la valeur initiale n’est-elle pas réutilisée à chaque affectation ?
- Pourquoi tester seulement le premier passage à partir de zéro peut-il masquer l’erreur d’affectation à 1 ?
- Le lot `added_count` est-il modifié quand on l’ajoute au stock ?
- Ce code sait-il si un capteur vient de produire une mesure ?

**Repères pour te corriger :** 11 en passant par 10 ; chaque affectation remplace la valeur courante ; le premier passage produit 1 dans les deux versions ; le lot reste inchangé ; aucune détection n’est réalisée.

**À retenir :** une mise à jour utilise la valeur courante pour en calculer une nouvelle, puis la conserve dans la même variable. Le symbole `=` exprime ici une affectation, pas une égalité à résoudre.

**Suite :** [découvrir les booléens](../premiers-booleens/), puis les comparaisons et les conditions, dans le [parcours progressif](../../parcours/). Les écritures abrégées et les boucles viendront avec leurs explications dédiées. La pratique reste dans les dépôts à cloner dans ton IDE ; les bilans interactifs et les fiches téléchargeables restent prévus pour plus tard.

## Référence

La [règle d’affectation](https://eel.is/c++draft/expr.assign) précise le calcul des valeurs avant leur stockage. Cette présentation HTML du projet de norme ne remplace pas l’édition ISO C++17 publiée. Les extraits de la leçon sont vérifiés en mode C++17, avec des valeurs représentables par `int`.
