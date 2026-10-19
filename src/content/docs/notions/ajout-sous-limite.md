---
title: "Contrôler un ajout avec une limite"
description: "Autoriser une seule augmentation, refuser à la limite et comprendre ce que le contrôle ne corrige pas."
---

**Objectif :** expliquer pourquoi une mise à jour s’exécute ou est refusée, puis prévoir la valeur finale. **Prérequis :** [mettre à jour un compteur](../mise-a-jour-compteur/), [comparer avec une limite](../en-dessous-ou-au-maximum/) et [choisir entre deux chemins](../premiere-alternative/). Le [recalcul d’une comparaison](../premiere-comparaison/) rappelle pourquoi une réponse stockée ne se met pas à jour seule.

**Disponible :** cinq programmes complets de lecture avec sorties, traces et cartes UML. Le projet autonome de pratique à cloner pour cette leçon n’est pas encore publié.

## Du constat à la modification contrôlée

Une limite constante ne suffit pas à bloquer une augmentation. Nous voulons maintenant autoriser **un seul ajout de 1** lorsque le compteur est strictement inférieur à la limite. Sinon, il reste inchangé.

La limite vaut 3. `can_add` conserve la réponse à la question « peut-on effectuer cet ajout ? », calculée **avant l’opération**. `Count increased` signifie « compteur augmenté » ; `Addition refused`, « ajout refusé ».

Les entiers fournis sont compris entre 0 et 20, avec une limite positive de 3, ou une capacité de 8 pour la boîte. Ce domaine est une hypothèse de lecture, pas un contrôle des entrées. Les programmes tournent sur ordinateur avec une console fonctionnant normalement. Augmenter ce compteur ne lit aucun capteur et ne place aucun objet physique dans une boîte.

## Lire aussi la valeur affichée

Jusqu’ici, nous affichions surtout des textes. Dans le premier programme, `std::cout << measurement_count;` transmet à la console **la valeur actuelle de la variable** : si elle vaut 3, le caractère `3` est affiché. Le nom n’est pas entre guillemets. Entre guillemets, ce serait un texte littéral, pas une lecture de la variable.

L’instruction suivante, `std::cout << "\n";`, écrit le saut de ligne. Ces deux écritures sont séparées pour conserver une action simple par ligne ; elles correspondent aux deux actions finales d’affichage dans l’UML. La valeur affichée permet de vérifier l’effet du programme, au-delà du message choisi.

## 1 — Autoriser le dernier ajout disponible

Le compteur vaut **2**, la limite **3**. Deux est strictement inférieur à trois : nous voulons passer à trois, puis afficher cette valeur.

**Sortie attendue :**

```text
Count increased
3
```

![Activité UML : choisir si le compteur peut augmenter, puis afficher sa valeur.](/diagrams/examples/guarded-room.svg)

<a href="/diagrams/examples/guarded-room.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

Le premier losange choisit un chemin à partir de `can_add`. Les gardes `[can_add]` et `[not can_add]` sont exclusives. Le chemin vrai contient maintenant une **modification**, puis un message. Le second losange réunit les chemins avant l’affichage commun ; il ne synchronise pas deux traitements. Calculer puis affecter sont les deux étapes de la même instruction C++, sans variable supplémentaire.

<!-- example:guarded-room -->
```cpp
#include <iostream>

int main() {
    const int measurement_limit = 3;
    int measurement_count = 2;
    bool can_add = measurement_count < measurement_limit;

    if (can_add) {
        measurement_count = measurement_count + 1;
        std::cout << "Count increased\n";
    } else {
        std::cout << "Addition refused\n";
    }
    std::cout << measurement_count;
    std::cout << "\n";
    return 0;
}
```

<details class="uml-panel" data-uml="guarded-room">
<summary>Voir la conception UML</summary>

| Étape UML attendue | Correspondance C++ |
| --- | --- |
| Préparer | Compteur à 2, limite à 3. |
| Calculer la réponse avant l’opération | `can_add` reçoit `true`. |
| Choisir un chemin | Le bloc `if` est sélectionné. |
| Modifier ou conserver | Le compteur passe de 2 à 3. |
| Affichage commun | La valeur du compteur est écrite, puis un saut de ligne. |
| Terminer | `return 0;` renvoie le statut 0 sans l’afficher. |

![Activité UML : choisir si le compteur peut augmenter, puis afficher sa valeur.](/diagrams/examples/guarded-room.svg)

<a href="/diagrams/examples/guarded-room.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

### Suivre les valeurs

| Point d’observation | `measurement_count` | `can_add` | Action |
| --- | --- | --- | --- |
| Après le calcul de la réponse | 2 | `true` | Comparaison effectuée sur la valeur initiale. |
| Après le bloc choisi | 3 | `true` | Augmentation, puis message `Count increased`. |
| Suite commune | 3 | `true` | Affichage du compteur, puis du saut de ligne. |

La limite reste à 3. Le bloc `else` est sauté ; le programme termine avec le statut 0.

**Attention au moment de la réponse :** après l’ajout, `can_add` vaut encore `true`, alors que le compteur a atteint trois. Il décrit l’autorisation de l’ajout qui vient d’être effectué, pas la place restante. Une variable booléenne ne relance pas son calcul automatiquement. Pour une nouvelle tentative, il faudrait une nouvelle décision ; nous n’en faisons qu’une ici.

C’est la place de l’affectation **dans le bloc contrôlé** qui conditionne l’augmentation. `const` empêche de modifier la limite elle-même ; il ne protège pas le compteur à lui seul.

## 2 — Refuser lorsque la limite est atteinte

Le compteur vaut **3**, comme la limite. Il respecte déjà la limite, mais il ne reste aucune place pour ajouter un élément. La valeur doit rester trois.

**Sortie attendue :**

```text
Addition refused
3
```

![Activité UML : choisir si le compteur peut augmenter, puis afficher sa valeur.](/diagrams/examples/guarded-full.svg)

<a href="/diagrams/examples/guarded-full.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:guarded-full -->
```cpp
#include <iostream>

int main() {
    const int measurement_limit = 3;
    int measurement_count = 3;
    bool can_add = measurement_count < measurement_limit;

    if (can_add) {
        measurement_count = measurement_count + 1;
        std::cout << "Count increased\n";
    } else {
        std::cout << "Addition refused\n";
    }
    std::cout << measurement_count;
    std::cout << "\n";
    return 0;
}
```

<details class="uml-panel" data-uml="guarded-full">
<summary>Voir la conception UML</summary>

| Étape UML attendue | Correspondance C++ |
| --- | --- |
| Préparer | Compteur à 3, limite à 3. |
| Calculer la réponse avant l’opération | `can_add` reçoit `false`. |
| Choisir un chemin | Le bloc `else` est sélectionné. |
| Modifier ou conserver | Le compteur passe de 3 à 3. |
| Affichage commun | La valeur du compteur est écrite, puis un saut de ligne. |
| Terminer | `return 0;` renvoie le statut 0 sans l’afficher. |

![Activité UML : choisir si le compteur peut augmenter, puis afficher sa valeur.](/diagrams/examples/guarded-full.svg)

<a href="/diagrams/examples/guarded-full.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

### Suivre les valeurs

| Point d’observation | `measurement_count` | `can_add` | Action |
| --- | --- | --- | --- |
| Après le calcul de la réponse | 3 | `false` | Comparaison effectuée sur la valeur initiale. |
| Après le bloc choisi | 3 | `false` | Aucune affectation du compteur ; message `Addition refused`. |
| Suite commune | 3 | `false` | Affichage du compteur, puis du saut de ligne. |

La limite reste à 3. Le bloc `if` est sauté ; le programme termine avec le statut 0.

**Être dans la limite et pouvoir encore ajouter sont deux questions différentes.** Trois respecte un maximum de trois, mais trois plus un le dépasserait. Pour cet ajout de un, nous demandons donc « strictement inférieur ? » avant de modifier.

## 3 — Transposer à une boîte

La boîte contient **7 éléments** pour une capacité de **8**. Nous modélisons seulement un nombre d’éléments identiques : ni leur poids ni leur géométrie. Le compteur doit passer à huit.

**Sortie attendue :**

```text
Count increased
8
```

![Activité UML : choisir si le compteur peut augmenter, puis afficher sa valeur.](/diagrams/examples/guarded-box.svg)

<a href="/diagrams/examples/guarded-box.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:guarded-box -->
```cpp
#include <iostream>

int main() {
    const int box_capacity = 8;
    int item_count = 7;
    bool can_add = item_count < box_capacity;

    if (can_add) {
        item_count = item_count + 1;
        std::cout << "Count increased\n";
    } else {
        std::cout << "Addition refused\n";
    }
    std::cout << item_count;
    std::cout << "\n";
    return 0;
}
```

<details class="uml-panel" data-uml="guarded-box">
<summary>Voir la conception UML</summary>

| Étape UML attendue | Correspondance C++ |
| --- | --- |
| Préparer | Compteur à 7, limite à 8. |
| Calculer la réponse avant l’opération | `can_add` reçoit `true`. |
| Choisir un chemin | Le bloc `if` est sélectionné. |
| Modifier ou conserver | Le compteur passe de 7 à 8. |
| Affichage commun | La valeur du compteur est écrite, puis un saut de ligne. |
| Terminer | `return 0;` renvoie le statut 0 sans l’afficher. |

![Activité UML : choisir si le compteur peut augmenter, puis afficher sa valeur.](/diagrams/examples/guarded-box.svg)

<a href="/diagrams/examples/guarded-box.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

### Suivre les valeurs

| Point d’observation | `item_count` | `can_add` | Action |
| --- | --- | --- | --- |
| Après le calcul de la réponse | 7 | `true` | Comparaison effectuée sur la valeur initiale. |
| Après le bloc choisi | 8 | `true` | Augmentation, puis message `Count increased`. |
| Suite commune | 8 | `true` | Affichage du compteur, puis du saut de ligne. |

La limite reste à 8. Le bloc `else` est sauté ; le programme termine avec le statut 0.

| Compteur initial | Réponse avant ajout | Compteur final |
| --- | --- | --- |
| 7 | `true` | 8 |
| 8 | `false` | 8 |
| 9 | `false` | 9 |

Chaque ligne décrit une exécution indépendante. La dernière annonce déjà la limite du mécanisme : refuser ne remet pas en état une donnée initialement excessive.

## 4 — Autoriser un ajout de trop avec <=

**Erreur volontaire :** remplaçons `<` par `<=` avec un compteur de **3**. Le besoin reste de refuser cet ajout. La conception attendue est celle du deuxième exemple, qui conserve trois.

<!-- example:guarded-inclusive-error -->
```cpp
#include <iostream>

int main() {
    const int measurement_limit = 3;
    int measurement_count = 3;
    bool can_add = measurement_count <= measurement_limit;

    if (can_add) {
        measurement_count = measurement_count + 1;
        std::cout << "Count increased\n";
    } else {
        std::cout << "Addition refused\n";
    }
    std::cout << measurement_count;
    std::cout << "\n";
    return 0;
}
```

<details class="uml-panel" data-uml="guarded-inclusive-error">
<summary>Comprendre l’écart avec la conception</summary>

**Attendu : 3 → 3 ; obtenu : 3 → 4.** Le diagramme montre le refus attendu, pas l’exécution fautive. Le message attendu est `Addition refused`, mais le programme écrit `Count increased`.

| Étape UML attendue | Correspondance C++ ou écart |
| --- | --- |
| Préparer | Compteur à 3, limite à 3. |
| Calculer la réponse avant l’opération | Écart : `<=` donne `true` à égalité, au lieu de `false` avec `<`. |
| Choisir un chemin | Écart : le bloc `if` est pris au lieu du refus. |
| Modifier ou conserver | Écart : le compteur passe à 4 au lieu de rester à 3. |
| Affichage commun | La valeur du compteur est écrite, puis un saut de ligne. |
| Terminer | `return 0;` renvoie le statut 0 sans l’afficher. |

![Activité UML : choisir si le compteur peut augmenter, puis afficher sa valeur.](/diagrams/examples/guarded-full.svg)

<a href="/diagrams/examples/guarded-full.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

### Suivre les valeurs

| Point d’observation | `measurement_count` | `can_add` | Action |
| --- | --- | --- | --- |
| Après le calcul de la réponse | 3 | `true` | Comparaison effectuée sur la valeur initiale. |
| Après le bloc choisi | 4 | `true` | Augmentation, puis message `Count increased`. |
| Suite commune | 4 | `true` | Affichage du compteur, puis du saut de ligne. |

La limite reste à 3. Le bloc `else` est sauté ; le programme termine avec le statut 0.

**Sortie réelle :**

```text
Count increased
4
```

**Sortie attendue :**

```text
Addition refused
3
```

La comparaison `<=` vérifie que le compteur actuel ne dépasse pas la limite. Elle ne vérifie pas qu’il reste une place. À égalité, elle donne `true`, donc l’affectation s’exécute et produit quatre. Le programme compile, mais viole le besoin.

**Correction :** utiliser `<`, comme au deuxième exemple. Le compteur et la limite n’ont pas à être changés pour masquer le défaut.

| Compteur initial | Avec `<`, règle attendue | Avec `<=`, règle fautive |
| --- | --- | --- |
| 0 | 1 | 1 |
| 2 | 3 | 3 |
| 3 | 3, ajout refusé | 4, ajout autorisé à tort |
| 4 | 4, ajout refusé | 4, ajout refusé |

Le cas d’égalité révèle cette erreur. Tester seulement une valeur sous la limite ou au-dessus ne suffit pas.

## 5 — Refuser ne signifie pas réparer

Le compteur fourni vaut déjà **4** pour une limite de **3**. Nous voulons refuser un ajout supplémentaire. Aucune instruction ne ramène automatiquement cette valeur à trois.

**Sortie attendue :**

```text
Addition refused
4
```

![Activité UML : choisir si le compteur peut augmenter, puis afficher sa valeur.](/diagrams/examples/guarded-already-above.svg)

<a href="/diagrams/examples/guarded-already-above.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:guarded-already-above -->
```cpp
#include <iostream>

int main() {
    const int measurement_limit = 3;
    int measurement_count = 4;
    bool can_add = measurement_count < measurement_limit;

    if (can_add) {
        measurement_count = measurement_count + 1;
        std::cout << "Count increased\n";
    } else {
        std::cout << "Addition refused\n";
    }
    std::cout << measurement_count;
    std::cout << "\n";
    return 0;
}
```

<details class="uml-panel" data-uml="guarded-already-above">
<summary>Voir la conception UML</summary>

| Étape UML attendue | Correspondance C++ |
| --- | --- |
| Préparer | Compteur à 4, limite à 3. |
| Calculer la réponse avant l’opération | `can_add` reçoit `false`. |
| Choisir un chemin | Le bloc `else` est sélectionné. |
| Modifier ou conserver | Le compteur passe de 4 à 4. |
| Affichage commun | La valeur du compteur est écrite, puis un saut de ligne. |
| Terminer | `return 0;` renvoie le statut 0 sans l’afficher. |

![Activité UML : choisir si le compteur peut augmenter, puis afficher sa valeur.](/diagrams/examples/guarded-already-above.svg)

<a href="/diagrams/examples/guarded-already-above.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

### Suivre les valeurs

| Point d’observation | `measurement_count` | `can_add` | Action |
| --- | --- | --- | --- |
| Après le calcul de la réponse | 4 | `false` | Comparaison effectuée sur la valeur initiale. |
| Après le bloc choisi | 4 | `false` | Aucune affectation du compteur ; message `Addition refused`. |
| Suite commune | 4 | `false` | Affichage du compteur, puis du saut de ligne. |

La limite reste à 3. Le bloc `if` est sauté ; le programme termine avec le statut 0.

Le message de refus ne signifie pas « le compteur est valide ». Il signifie seulement que cet ajout n’a pas été autorisé. Ici, le programme n’aggrave pas la valeur excessive, mais ne la corrige pas non plus.

Si le compteur initial est compris entre zéro et la limite, cette opération conserve cette propriété. Nous n’avons pas construit un contrôle complet de valeurs arbitraires : les valeurs négatives restent hors des hypothèses de la leçon, et aucun code ne les rejette ici. Une correction automatique demanderait un autre besoin explicite.

## Vérifier sa compréhension

- Pourquoi trois respecte-t-il la limite sans autoriser un ajout ?
- Quelle instruction modifie réellement le compteur ?
- Après le passage de deux à trois, pourquoi `can_add` reste-t-il vrai ?
- Quelle valeur initiale révèle le défaut de `<=` ?
- Un refus garantit-il que la valeur initiale était correcte ?

**Repères :** respecter la limite ne garantit pas une place supplémentaire ; l’affectation `measurement_count = measurement_count + 1;` ; le booléen conserve la réponse calculée avant l’ajout ; trois ; non, quatre est refusé mais reste quatre.

**À retenir :** vérifier avant de modifier, choisir la comparaison pour l’opération demandée et distinguer la réponse passée de l’état actuel. Un ajout refusé ne répare pas automatiquement une donnée.

Le [parcours](../../parcours/) situe la suite des applications de contrôle. La pratique reste dans les projets dédiés à cloner, dans ton IDE.

## Références

Le projet de norme décrit le [choix du bloc avec `if`](https://eel.is/c++draft/stmt.if), les [comparaisons](https://eel.is/c++draft/expr.rel) et l’[affectation](https://eel.is/c++draft/expr.assign). Les programmes présentés sont vérifiés en C++17. Les décisions et réunions de chemins suivent les sections 15.3.3.5–15.3.3.6 de la [norme UML 2.5.1](https://www.omg.org/spec/UML/2.5.1/PDF).
