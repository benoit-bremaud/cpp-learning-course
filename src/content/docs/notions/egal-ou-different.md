---
title: "Égal ou différent — comparer avec == et !="
description: "Reconnaître une cible exacte, distinguer les deux sens de différence et vérifier un identifiant entier."
---

**Objectif :** reconnaître une correspondance exacte et une différence, sans les confondre avec un seuil. **Prérequis :** [en dessous ou au maximum](../en-dessous-ou-au-maximum/), avec les déclarations, les booléens et les comparaisons déjà rencontrées.

**Disponible :** cinq exemples de lecture avec leur conception UML. Le projet de pratique autonome à cloner pour cette leçon n’est pas encore publié.

## Une cible exacte, plutôt qu’un maximum

Nous souhaitons maintenant savoir si le compteur vaut **exactement trois mesures**. Nous nommons donc la constante `measurement_target` : c’est une **cible**, pas une limite supérieure dont toutes les valeurs inférieures seraient acceptées.

| Question | Réponse conservée | Opérateur |
| --- | --- | --- |
| Le compteur est-il exactement égal à la cible ? | `target_matched` | `==` |
| Le compteur est-il différent de la cible ? | `target_different` | `!=` |

`==` se lit **« égal à »** ; `!=` se lit **« différent de »**. Chacun est un seul opérateur écrit avec deux caractères adjacents. « Différent » ne précise ni de quel côté se trouve la valeur, ni de combien elle s’écarte de la cible.

Tous les nombres fournis sont des `int` de 0 à 20. Chaque extrait est indépendant, à lire dans le corps de `main`. Il ne lit aucun capteur, n’affiche rien et ne déclenche aucune action. Nous comparons des entiers exacts ; les mesures physiques approximatives et les nombres à virgule demanderont une étude distincte.

## 1 — Reconnaître une correspondance exacte

Le compteur et la cible valent tous deux **3**. **Attendu : `true` pour la correspondance, puis `false` pour la différence.**

![Activité UML : comparer exactement measurement_count valant 3 à measurement_target valant 3.](/diagrams/examples/equality-equal.svg)

<a href="/diagrams/examples/equality-equal.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

Le disque initial marque le début ; les rectangles arrondis représentent les actions ; le symbole final termine l’activité. Évaluer puis conserver une réponse sont deux étapes du raisonnement réunies dans une déclaration. Aucun losange n’est nécessaire : les comparaisons calculent des booléens sans choisir un chemin.

<!-- example:equality-equal -->
```cpp
const int measurement_target = 3;
int measurement_count = 3;
bool target_matched = measurement_count == measurement_target;
bool target_different = measurement_count != measurement_target;
```

<details class="uml-panel" data-uml="equality-equal">
<summary>Voir la conception UML</summary>

| Action UML attendue | Correspondance C++ |
| --- | --- |
| Initialiser les entiers | `measurement_target` vaut 3 et `measurement_count` vaut 3. |
| Comparer l’égalité exacte | `measurement_count == measurement_target` initialise `target_matched` à `true`. |
| Comparer la différence | `measurement_count != measurement_target` initialise `target_different` à `false`. |

![Activité UML : comparer exactement measurement_count valant 3 à measurement_target valant 3.](/diagrams/examples/equality-equal.svg)

<a href="/diagrams/examples/equality-equal.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

La trace suit `target_matched`, puis `target_different`. Les nombres et la première réponse restent inchangés lors du calcul de la seconde.

| Après l’instruction | Valeur recherchée | Valeur fournie | Correspond ? | Diffère ? |
| --- | --- | --- | --- | --- |
| Déclaration de la constante | 3 | Pas encore créée | Pas encore créée | Pas encore créée |
| Déclaration de la valeur fournie | 3 | 3 | Pas encore créée | Pas encore créée |
| Déclaration de la première réponse | 3 | 3 | `true` | Pas encore créée |
| Déclaration de la seconde réponse | 3 | 3 | `true` | `false` |

Observe la troisième ligne en deux étapes :

1. `measurement_count == measurement_target` compare 3 et 3 et produit `true`.
2. Le premier `=` initialise `target_matched` avec cette réponse.

**Le `=` de l’initialisation et le `==` de la comparaison ont donc des rôles différents.** Avec une variable déjà déclarée, `measurement_count = 3;` serait une affectation qui lui donne la valeur 3, comme dans [la leçon sur les variables](../cpp-01/). Une comparaison avec `==`, elle, laisse les nombres inchangés.

La quatrième ligne pose l’autre question : trois est-il différent de trois ? `!=` produit `false`, qui initialise `target_different`. Ce n’est pas une soustraction : le résultat est un booléen, pas la taille d’un écart.

## 2 — Être différent en étant plus petit

Seul le compteur change : il vaut **2**, avec une cible de **3**. **Attendu : `false` puis `true`.** Deux n’est pas égal à trois, même s’il est inférieur à trois.

![Activité UML : comparer exactement measurement_count valant 2 à measurement_target valant 3.](/diagrams/examples/equality-below.svg)

<a href="/diagrams/examples/equality-below.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:equality-below -->
```cpp
const int measurement_target = 3;
int measurement_count = 2;
bool target_matched = measurement_count == measurement_target;
bool target_different = measurement_count != measurement_target;
```

<details class="uml-panel" data-uml="equality-below">
<summary>Voir la conception UML</summary>

| Action UML attendue | Correspondance C++ |
| --- | --- |
| Initialiser les entiers | `measurement_target` vaut 3 et `measurement_count` vaut 2. |
| Comparer l’égalité exacte | `measurement_count == measurement_target` initialise `target_matched` à `false`. |
| Comparer la différence | `measurement_count != measurement_target` initialise `target_different` à `true`. |

![Activité UML : comparer exactement measurement_count valant 2 à measurement_target valant 3.](/diagrams/examples/equality-below.svg)

<a href="/diagrams/examples/equality-below.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

La trace suit `target_matched`, puis `target_different`. Les nombres et la première réponse restent inchangés lors du calcul de la seconde.

| Après l’instruction | Valeur recherchée | Valeur fournie | Correspond ? | Diffère ? |
| --- | --- | --- | --- | --- |
| Déclaration de la constante | 3 | Pas encore créée | Pas encore créée | Pas encore créée |
| Déclaration de la valeur fournie | 3 | 2 | Pas encore créée | Pas encore créée |
| Déclaration de la première réponse | 3 | 2 | `false` | Pas encore créée |
| Déclaration de la seconde réponse | 3 | 2 | `false` | `true` |

`!=` est vrai alors que le compteur est **plus petit**. Cela suffit à montrer qu’il ne signifie pas « supérieur à ».

Les deux nombres restent 2 et 3. La comparaison ne complète pas le compteur pour atteindre la cible. Le booléen indique seulement si les valeurs sont différentes au moment du calcul.

## 3 — Être différent en étant plus grand

Le compteur vaut maintenant **4**, pour une cible toujours à **3**. Prévois les deux réponses : dépasser trois revient-il à avoir exactement trois ?

**Attendu : `false` puis `true`.** Le sens de l’écart change par rapport au deuxième exemple, mais les réponses à nos deux questions restent les mêmes.

![Activité UML : comparer exactement measurement_count valant 4 à measurement_target valant 3.](/diagrams/examples/equality-above.svg)

<a href="/diagrams/examples/equality-above.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:equality-above -->
```cpp
const int measurement_target = 3;
int measurement_count = 4;
bool target_matched = measurement_count == measurement_target;
bool target_different = measurement_count != measurement_target;
```

<details class="uml-panel" data-uml="equality-above">
<summary>Voir la conception UML</summary>

| Action UML attendue | Correspondance C++ |
| --- | --- |
| Initialiser les entiers | `measurement_target` vaut 3 et `measurement_count` vaut 4. |
| Comparer l’égalité exacte | `measurement_count == measurement_target` initialise `target_matched` à `false`. |
| Comparer la différence | `measurement_count != measurement_target` initialise `target_different` à `true`. |

![Activité UML : comparer exactement measurement_count valant 4 à measurement_target valant 3.](/diagrams/examples/equality-above.svg)

<a href="/diagrams/examples/equality-above.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

La trace suit `target_matched`, puis `target_different`. Les nombres et la première réponse restent inchangés lors du calcul de la seconde.

| Après l’instruction | Valeur recherchée | Valeur fournie | Correspond ? | Diffère ? |
| --- | --- | --- | --- | --- |
| Déclaration de la constante | 3 | Pas encore créée | Pas encore créée | Pas encore créée |
| Déclaration de la valeur fournie | 3 | 4 | Pas encore créée | Pas encore créée |
| Déclaration de la première réponse | 3 | 4 | `false` | Pas encore créée |
| Déclaration de la seconde réponse | 3 | 4 | `false` | `true` |

Quatre atteint ou dépasse trois, mais quatre n’est pas exactement trois. Nous retrouvons une distinction utile : **atteindre un seuil** et **correspondre à une valeur précise** ne posent pas la même question.

`!=` accepte les deux situations différentes : deux face à trois, ou quatre face à trois. Il ne dit pas si le compteur est trop petit ou trop grand, ni combien il faudrait ajouter ou retirer.

## 4 — Retrouver un identifiant précis

Imaginons des éléments portant chacun un numéro entier. Nous cherchons celui portant le numéro **7**, mais le numéro fourni est **9**. Ici, le nombre sert d’**étiquette** : un numéro plus grand n’est pas une meilleure correspondance.

**Attendu : `false` pour `identifier_matched`, puis `true` pour `identifier_different`.** Le nom `observed_identifier` désigne ici une valeur écrite dans le code, pas une lecture effectuée auprès d’un appareil.

![Activité UML : comparer exactement observed_identifier valant 9 à expected_identifier valant 7.](/diagrams/examples/equality-identifier.svg)

<a href="/diagrams/examples/equality-identifier.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:equality-identifier -->
```cpp
const int expected_identifier = 7;
int observed_identifier = 9;
bool identifier_matched = observed_identifier == expected_identifier;
bool identifier_different = observed_identifier != expected_identifier;
```

<details class="uml-panel" data-uml="equality-identifier">
<summary>Voir la conception UML</summary>

| Action UML attendue | Correspondance C++ |
| --- | --- |
| Initialiser les entiers | `expected_identifier` vaut 7 et `observed_identifier` vaut 9. |
| Comparer l’égalité exacte | `observed_identifier == expected_identifier` initialise `identifier_matched` à `false`. |
| Comparer la différence | `observed_identifier != expected_identifier` initialise `identifier_different` à `true`. |

![Activité UML : comparer exactement observed_identifier valant 9 à expected_identifier valant 7.](/diagrams/examples/equality-identifier.svg)

<a href="/diagrams/examples/equality-identifier.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

La trace suit `identifier_matched`, puis `identifier_different`. Les nombres et la première réponse restent inchangés lors du calcul de la seconde.

| Après l’instruction | Valeur recherchée | Valeur fournie | Correspond ? | Diffère ? |
| --- | --- | --- | --- | --- |
| Déclaration de la constante | 7 | Pas encore créée | Pas encore créée | Pas encore créée |
| Déclaration de la valeur fournie | 7 | 9 | Pas encore créée | Pas encore créée |
| Déclaration de la première réponse | 7 | 9 | `false` | Pas encore créée |
| Déclaration de la seconde réponse | 7 | 9 | `false` | `true` |

La question porte sur le numéro exact recherché. Ni « au moins sept », ni « au maximum sept » ne la remplace.

| Numéro fourni | Correspond au numéro 7 ? | Diffère du numéro 7 ? |
| --- | --- | --- |
| 5 | `false` | `true` |
| 7 | `true` | `false` |
| 9 | `false` | `true` |

Ces autres valeurs sont des situations indépendantes, pas des changements réalisés par le code. L’exemple représente uniquement des étiquettes entières fictives. Il ne détecte pas un appareil et n’en vérifie pas l’authenticité.

## 5 — Confondre une cible exacte avec un seuil

Revenons au troisième exemple : le compteur vaut **4**, la cible exacte vaut **3**. Le besoin reste inchangé : **nous attendons `false` puis `true`**.

**Erreur volontaire :** nous remplaçons `==` par `>=` dans la première comparaison. La conception attendue est celle du troisième exemple, présentée plus haut ; la carte montre où ce code s’en écarte.

<!-- example:equality-threshold -->
```cpp
const int measurement_target = 3;
int measurement_count = 4;
bool target_matched = measurement_count >= measurement_target;
bool target_different = measurement_count != measurement_target;
```

<details class="uml-panel" data-uml="equality-threshold">
<summary>Comprendre l’écart avec la conception</summary>

**Attendu : `false` / `true` ; obtenu : `true` / `true`.** L’ordre est `target_matched`, puis `target_different`. Le diagramme représente la conception attendue, pas l’exécution de ce code fautif.

| Action UML attendue | Correspondance C++ ou écart |
| --- | --- |
| Initialiser les entiers | `measurement_target` vaut 3 et `measurement_count` vaut 4. |
| Comparer l’égalité exacte | `target_matched` devrait valoir `false` ; `>=` donne ici `true`. |
| Comparer la différence | `measurement_count != measurement_target` initialise `target_different` à `true`. |

![Activité UML : comparer exactement measurement_count valant 4 à measurement_target valant 3.](/diagrams/examples/equality-above.svg)

<a href="/diagrams/examples/equality-above.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

La trace suit `target_matched`, puis `target_different`. Elle montre les résultats effectivement obtenus malgré l’erreur.

| Après l’instruction | Valeur recherchée | Valeur fournie | Correspond ? | Diffère ? |
| --- | --- | --- | --- | --- |
| Déclaration de la constante | 3 | Pas encore créée | Pas encore créée | Pas encore créée |
| Déclaration de la valeur fournie | 3 | 4 | Pas encore créée | Pas encore créée |
| Déclaration de la première réponse | 3 | 4 | `true` | Pas encore créée |
| Déclaration de la seconde réponse | 3 | 4 | `true` | `true` |

`>=` répond correctement à « le compteur atteint-il ou dépasse-t-il trois ? » : avec quatre, c’est vrai. Mais `target_matched` doit répondre à « le compteur vaut-il exactement trois ? » : c’est faux.

**Correction :** remettre `measurement_count == measurement_target` dans l’initialisation de `target_matched`, comme dans le troisième exemple. La comparaison avec `!=` reste correcte.

Ce code compile : le défaut porte sur la question choisie. Les deux réponses vraies signalent ici que le premier calcul ne respecte pas notre conception, qui demandait de comparer l’égalité et la différence sur les mêmes entiers inchangés.

## Choisir des valeurs qui révèlent la mauvaise question

Voici trois questions pour une cible de trois. La troisième colonne de résultats rappelle `>=`, utilisé à tort dans le dernier exemple.

| Compteur | Exactement trois : `==` | Différent de trois : `!=` | Au moins trois : `>=` |
| --- | --- | --- | --- |
| 2 | `false` | `true` | `false` |
| 3 | `true` | `false` | `true` |
| 4 | `false` | `true` | `true` |

Avec 2 ou 3, `==` et `>=` donnent le même résultat : ces seuls tests masqueraient la substitution. **Avec 4, la différence apparaît.** Dans la leçon « atteindre ou dépasser », l’égalité distinguait `>` de `>=` ; ici, c’est le dépassement qui révèle l’erreur. On choisit les cas de vérification selon la question.

Pour les mêmes entiers inchangés, les calculs corrects avec `==` et `!=` donnent une réponse vraie et une réponse fausse. **Cela ne crée pas de liaison entre les variables qui conservent ces réponses.** Si les nombres changent ensuite, les booléens stockés ne se recalculent pas automatiquement.

## Vérifier sa compréhension

- Deux est-il différent de trois, même s’il est plus petit ?
- Que répond `==` pour quatre face à une cible de trois ? Et `>=` ?
- Dans la troisième ligne du premier extrait, quel signe compare et quel signe initialise ?
- Pour retrouver l’identifiant 7, pourquoi 9 ne convient-il pas ?
- Quel cas révèle le remplacement erroné de `==` par `>=` : 2, 3 ou 4 ?

**Repères pour te corriger :** oui ; `false` puis `true` ; `==` compare, le premier `=` initialise ; le numéro demandé est exactement 7 ; 4.

**À retenir :** `==` demande « la même valeur ? », `!=` demande « une autre valeur ? ». Une différence n’indique ni direction ni distance. Les résultats décrivent les valeurs comparées, sans modifier celles-ci ni déclencher une action.

**Suite :** [la première condition](../premiere-condition/) utilise un booléen pour exécuter ou sauter un bloc avec `if`. L’[alternative avec `else`](../premiere-alternative/) est présentée dans un module distinct. Le [parcours](../../parcours/) situe cette prochaine étape ; les exercices exécutables restent dans les dépôts à cloner.

## Références

La [définition de `==` et `!=`](https://eel.is/c++draft/expr.eq) précise leurs résultats booléens. La [définition de l’initialisation](https://eel.is/c++draft/dcl.init) distingue le rôle du `=` présent dans une déclaration. Ces pages présentent le projet de norme, pas l’édition ISO C++17 publiée. Les extraits sont vérifiés en C++17.
