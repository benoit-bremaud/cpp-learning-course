---
title: "Répéter une décision jusqu’à la limite"
description: "Comprendre comment while réévalue une condition, progresse et termine — ou pourquoi une boucle reste bloquée."
---

**Objectif :** suivre une boucle `while` passage après passage et expliquer pourquoi elle s’arrête. **Prérequis :** [mettre à jour un compteur](../mise-a-jour-compteur/), [comparer avec une limite](../en-dessous-ou-au-maximum/) et [contrôler un ajout](../ajout-sous-limite/).

**Disponible :** sept programmes complets de lecture, avec sorties, traces et cartes UML. Le projet autonome de pratique à cloner pour cette leçon n’est pas encore publié.

## D’une décision unique à une décision répétée

Dans la leçon précédente, le programme calculait une réponse dans `can_add`, puis autorisait **au plus un ajout**. Pour tenter un nouvel ajout, il faut poser de nouveau la question avec la nouvelle valeur du compteur.

Une instruction `while` fait précisément cela :

```text
évaluer la condition
si elle est vraie : exécuter le corps, puis revenir à la condition
si elle est fausse : continuer après la boucle
```

La condition est placée directement dans `while`. Nous ne conservons pas une ancienne réponse dans un booléen : le but nouveau est justement de la **recalculer avant chaque passage éventuel**.

Les entiers fournis dans cette leçon sont compris entre 0 et 20. Les limites sont positives et les additions restent loin du maximum de `int`. Ces hypothèses simplifient l’étude ; le code ne valide pas des entrées arbitraires. Les programmes fonctionnent sur ordinateur avec une console disponible. Modifier un compteur ne lit aucun capteur et ne déplace aucun objet physique.

## 1 — Effectuer plusieurs passages

Le compteur commence à **1** et la limite vaut **3**. La condition est vraie à 1, puis à 2. Elle devient fausse à 3.

**Sortie attendue :**

```text
2
3
Loop finished
```

![Activité UML : réévaluer une condition et augmenter un compteur jusqu’à sa limite.](/diagrams/examples/repeated-multiple.svg)

<a href="/diagrams/examples/repeated-multiple.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:repeated-multiple -->
```cpp
#include <iostream>

int main() {
    const int measurement_limit = 3;
    int measurement_count = 1;

    while (measurement_count < measurement_limit) {
        measurement_count = measurement_count + 1;
        std::cout << measurement_count;
        std::cout << "\n";
    }
    std::cout << "Loop finished\n";
    return 0;
}
```

<details class="uml-panel" data-uml="repeated-multiple">
<summary>Voir la conception UML</summary>

| Étape UML | Correspondance C++ |
| --- | --- |
| Préparer | Limite à 3, compteur à 1. |
| Décider | `measurement_count < measurement_limit` est évalué avant chaque passage. |
| Progresser | L’affectation ajoute exactement 1 au compteur. |
| Observer | La nouvelle valeur est écrite, puis un saut de ligne. |
| Revenir | La flèche retourne vers la décision avec la valeur modifiée. |
| Sortir | À 3, la condition est fausse ; `Loop finished` est écrit. |
| Terminer | `return 0;` renvoie le statut 0 sans l’afficher. |

![Activité UML : réévaluer une condition et augmenter un compteur jusqu’à sa limite.](/diagrams/examples/repeated-multiple.svg)

<a href="/diagrams/examples/repeated-multiple.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

### Tracer chaque décision

| Évaluation | Compteur avant la question | Réponse | Compteur après le corps |
| ---: | ---: | --- | ---: |
| 1 | 1 | `true` | 2 |
| 2 | 2 | `true` | 3 |
| 3 | 3 | `false` | Corps non exécuté |

Le corps s’exécute deux fois, mais la condition est évaluée trois fois. La dernière évaluation est nécessaire pour découvrir qu’il faut sortir. La flèche de retour UML ne crée pas deux traitements simultanés : elle représente la prochaine étape du même traitement.

La distance `measurement_limit - measurement_count` vaut successivement 2, 1, puis 0. Elle diminue à chaque passage. Avec les hypothèses annoncées, cette progression explique pourquoi la boucle termine.

## 2 — N’effectuer qu’un passage

Changeons uniquement la valeur initiale : le compteur commence à **2**. La structure reste identique.

**Sortie attendue :**

```text
3
Loop finished
```

![Activité UML : une seule augmentation avant la sortie de boucle.](/diagrams/examples/repeated-one.svg)

<a href="/diagrams/examples/repeated-one.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:repeated-one -->
```cpp
#include <iostream>

int main() {
    const int measurement_limit = 3;
    int measurement_count = 2;

    while (measurement_count < measurement_limit) {
        measurement_count = measurement_count + 1;
        std::cout << measurement_count;
        std::cout << "\n";
    }
    std::cout << "Loop finished\n";
    return 0;
}
```

<details class="uml-panel" data-uml="repeated-one">
<summary>Voir la conception UML</summary>

| Étape UML | Correspondance C++ |
| --- | --- |
| Préparer | Limite à 3, compteur à 2. |
| Première décision | `2 < 3` donne `true`. |
| Progresser | Le compteur passe de 2 à 3 et la valeur 3 est écrite. |
| Décision suivante | `3 < 3` donne `false`. |
| Sortir et terminer | Le message commun est écrit, puis le statut 0 est renvoyé. |

![Activité UML : une seule augmentation avant la sortie de boucle.](/diagrams/examples/repeated-one.svg)

<a href="/diagrams/examples/repeated-one.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

| Évaluation | Valeur observée | Résultat | Effet |
| ---: | ---: | --- | --- |
| 1 | 2 | `true` | Passage à 3. |
| 2 | 3 | `false` | Sortie de la boucle. |

Le nombre de lignes écrites par le corps dépend de la valeur initiale. La boucle ne promet pas un nombre fixe de passages ; sa condition et la progression du compteur le déterminent.

## 3 — N’effectuer aucun passage à la limite

Le compteur commence maintenant à **3**, comme la limite. `while` teste avant d’entrer dans son corps.

**Sortie attendue :**

```text
Loop finished
```

![Activité UML : quitter immédiatement une boucle dont la condition initiale est fausse.](/diagrams/examples/repeated-zero-at-limit.svg)

<a href="/diagrams/examples/repeated-zero-at-limit.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:repeated-zero-at-limit -->
```cpp
#include <iostream>

int main() {
    const int measurement_limit = 3;
    int measurement_count = 3;

    while (measurement_count < measurement_limit) {
        measurement_count = measurement_count + 1;
        std::cout << measurement_count;
        std::cout << "\n";
    }
    std::cout << "Loop finished\n";
    return 0;
}
```

<details class="uml-panel" data-uml="repeated-zero-at-limit">
<summary>Voir la conception UML</summary>

| Étape UML | Correspondance C++ |
| --- | --- |
| Préparer | Limite et compteur valent 3. |
| Décider | `3 < 3` donne `false` dès la première évaluation. |
| Ignorer le corps | Aucune affectation et aucun affichage numérique ne sont exécutés. |
| Continuer | `Loop finished` se trouve après la boucle et est donc écrit. |
| Terminer | Le programme renvoie le statut 0. |

![Activité UML : quitter immédiatement une boucle dont la condition initiale est fausse.](/diagrams/examples/repeated-zero-at-limit.svg)

<a href="/diagrams/examples/repeated-zero-at-limit.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

Une boucle `while` peut donc effectuer **zéro passage**. Les accolades délimitent son corps ; elles ne l’obligent pas à être exécuté une première fois. Le programme ne s’arrête pas avec la boucle : il continue avec l’instruction suivante.

## 4 — Ne pas confondre arrêt et réparation

Le compteur commence à **4**, au-dessus de la limite 3. La condition initiale est encore fausse.

**Sortie attendue :**

```text
Loop finished
```

![Activité UML : ne pas entrer dans la boucle avec une valeur déjà excessive.](/diagrams/examples/repeated-zero-above.svg)

<a href="/diagrams/examples/repeated-zero-above.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:repeated-zero-above -->
```cpp
#include <iostream>

int main() {
    const int measurement_limit = 3;
    int measurement_count = 4;

    while (measurement_count < measurement_limit) {
        measurement_count = measurement_count + 1;
        std::cout << measurement_count;
        std::cout << "\n";
    }
    std::cout << "Loop finished\n";
    return 0;
}
```

<details class="uml-panel" data-uml="repeated-zero-above">
<summary>Voir la conception UML</summary>

| Étape UML | Correspondance C++ |
| --- | --- |
| Préparer | Limite à 3, compteur à 4. |
| Décider | `4 < 3` donne `false`. |
| Ne pas modifier | Le corps est ignoré ; le compteur reste à 4. |
| Continuer | Le message neutre `Loop finished` est écrit. |
| Terminer | Le programme renvoie le statut 0. |

![Activité UML : ne pas entrer dans la boucle avec une valeur déjà excessive.](/diagrams/examples/repeated-zero-above.svg)

<a href="/diagrams/examples/repeated-zero-above.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

Le message ne dit pas `Limit reached` : quatre n’est pas égal à trois. Il indique seulement que la boucle est terminée. La condition empêche une nouvelle augmentation, mais elle ne valide ni ne corrige la valeur initiale.

| Compteur initial | Passages | Compteur final |
| ---: | ---: | ---: |
| 1 | 2 | 3 |
| 2 | 1 | 3 |
| 3 | 0 | 3 |
| 4 | 0 | 4 |

## 5 — Transférer la règle à une boîte

Une boîte contient **5 éléments** pour une capacité de **8**. Nous changeons les noms et les valeurs, sans changer la règle de contrôle.

**Sortie attendue :**

```text
6
7
8
Loop finished
```

![Activité UML : augmenter un nombre d’éléments jusqu’à la capacité.](/diagrams/examples/repeated-box.svg)

<a href="/diagrams/examples/repeated-box.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:repeated-box -->
```cpp
#include <iostream>

int main() {
    const int box_capacity = 8;
    int item_count = 5;

    while (item_count < box_capacity) {
        item_count = item_count + 1;
        std::cout << item_count;
        std::cout << "\n";
    }
    std::cout << "Loop finished\n";
    return 0;
}
```

<details class="uml-panel" data-uml="repeated-box">
<summary>Voir la conception UML</summary>

| Étape UML | Correspondance C++ |
| --- | --- |
| Préparer | Capacité à 8, nombre d’éléments à 5. |
| Décider | `item_count < box_capacity` est recalculé avant chaque passage. |
| Progresser | `item_count` passe successivement à 6, 7 et 8. |
| Observer | Chaque nouvelle valeur est écrite. |
| Sortir | `8 < 8` est faux ; le message commun est écrit. |
| Terminer | Le programme renvoie le statut 0. |

![Activité UML : augmenter un nombre d’éléments jusqu’à la capacité.](/diagrams/examples/repeated-box.svg)

<a href="/diagrams/examples/repeated-box.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

Le programme modélise seulement un entier. Il ne connaît ni la taille, ni le poids, ni la présence physique des éléments. Le transfert montre que la même structure peut répondre à un besoin analogue lorsque les noms expriment correctement le nouveau contexte.

## 6 — Oublier de progresser

**Erreur volontaire :** retirons l’affectation qui modifie le compteur. Le programme compile, mais `measurement_count` reste toujours à 1. La condition `1 < 3` reste donc vraie.

![Activité UML : revenir indéfiniment vers une condition qui reste vraie.](/diagrams/examples/repeated-missing-update.svg)

<a href="/diagrams/examples/repeated-missing-update.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:repeated-missing-update -->
```cpp
#include <iostream>

int main() {
    const int measurement_limit = 3;
    int measurement_count = 1;

    while (measurement_count < measurement_limit) {
        std::cout << measurement_count;
        std::cout << "\n";
    }
    std::cout << "Loop finished\n";
    return 0;
}
```

<details class="uml-panel" data-uml="repeated-missing-update">
<summary>Comprendre l’écart avec la conception</summary>

**Attendu : 1 → 2 → 3 puis sortie ; obtenu : 1 → 1 → 1… sans sortie.** Le diagramme représente l’exécution fautive réelle : le chemin vrai ne modifie aucune donnée utilisée par la condition.

| Étape | Code ou écart |
| --- | --- |
| Préparer | Limite à 3, compteur à 1. |
| Décider | `1 < 3` donne `true`. |
| Avancer | Écart : aucune affectation ne rapproche le compteur de la limite. |
| Observer | La valeur 1 est écrite à chaque passage. |
| Revenir | La décision reçoit encore exactement les mêmes opérandes. |
| Sortir | Impossible pour cette exécution : la condition ne devient jamais fausse. |

![Activité UML : revenir indéfiniment vers une condition qui reste vraie.](/diagrams/examples/repeated-missing-update.svg)

<a href="/diagrams/examples/repeated-missing-update.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

Il n’existe pas de sortie complète finie à recopier : le programme écrit des lignes contenant `1` tant qu’il est laissé en exécution. L’instruction `Loop finished` reste hors d’atteinte avec ces valeurs.

La compilation vérifie la syntaxe et certaines règles du langage. Elle ne prouve pas qu’une boucle terminera. Pour analyser cet exemple sans abandonner un processus infini, nos tests compilent le fragment exact puis reproduisent un nombre limité de décisions dans un modèle instrumenté.

**Correction :** rétablir `measurement_count = measurement_count + 1;` dans le corps. Avec les hypothèses de cette leçon, la distance jusqu’à la limite diminuera alors à chaque passage.

## 7 — Dépasser la limite avec <=

**Erreur volontaire :** remplaçons `<` par `<=`. À l’égalité, la condition reste vraie et autorise un passage supplémentaire.

**Sortie réelle :**

```text
2
3
4
Limit exceeded
```

![Activité UML : exécuter un passage de trop avec une comparaison inclusive.](/diagrams/examples/repeated-inclusive-error.svg)

<a href="/diagrams/examples/repeated-inclusive-error.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:repeated-inclusive-error -->
```cpp
#include <iostream>

int main() {
    const int measurement_limit = 3;
    int measurement_count = 1;

    while (measurement_count <= measurement_limit) {
        measurement_count = measurement_count + 1;
        std::cout << measurement_count;
        std::cout << "\n";
    }
    std::cout << "Limit exceeded\n";
    return 0;
}
```

<details class="uml-panel" data-uml="repeated-inclusive-error">
<summary>Comprendre l’écart avec la conception</summary>

**Attendu : sortie à 3 ; obtenu : un passage supplémentaire jusqu’à 4.** Le diagramme représente le programme fautif avec sa condition inclusive réelle.

| Étape | Code ou écart |
| --- | --- |
| Préparer | Limite à 3, compteur à 1. |
| Décider à 1 et 2 | `<=` donne `true`, comme `<`. Le défaut reste masqué. |
| Décider à 3 | Écart : `3 <= 3` donne encore `true`. |
| Avancer | Le compteur passe à 4 et dépasse la limite. |
| Décider à 4 | `4 <= 3` donne `false`, trop tard pour préserver la limite. |
| Terminer | Le programme écrit `Limit exceeded` et renvoie 0. |

![Activité UML : exécuter un passage de trop avec une comparaison inclusive.](/diagrams/examples/repeated-inclusive-error.svg)

<a href="/diagrams/examples/repeated-inclusive-error.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

| Compteur avant la décision | Avec `<` | Avec `<=` |
| ---: | --- | --- |
| 1 | Continuer | Continuer |
| 2 | Continuer | Continuer |
| 3 | Sortir | Continuer à tort |
| 4 | Sortir | Sortir après le dépassement |

Le cas d’égalité révèle l’erreur. Tester seulement une valeur éloignée de la frontière peut donner une fausse impression de correction.

## Relire la structure complète

Une boucle bornée de cette leçon possède quatre éléments :

1. un état initial connu ;
2. une condition évaluée avant chaque passage ;
3. une modification qui rapproche l’état de la sortie ;
4. une suite exécutée lorsque la condition devient fausse.

Le mot `while` n’assure pas la terminaison à lui seul. La justification vient de la relation entre la condition, les valeurs initiales et la modification effectuée dans le corps.

## Vérifier sa compréhension

- Pourquoi la première boucle évalue-t-elle trois fois sa condition pour deux passages ?
- Quelle différence y a-t-il entre zéro passage et un programme qui ne fait rien ?
- Pourquoi une valeur initiale de 4 n’est-elle pas corrigée ?
- Quelle instruction garantit la progression dans les exemples corrects ?
- Pourquoi `<=` ne révèle-t-il son défaut qu’à la frontière ?
- Une compilation réussie prouve-t-elle qu’une boucle termine ?

**Repères :** la dernière évaluation découvre la sortie ; le programme continue après la boucle et écrit le message commun ; la condition interdit seulement le corps ; l’affectation qui ajoute 1 ; `<` et `<=` donnent la même réponse hors égalité dans les cas montrés ; non.

**À retenir :** `while` réévalue sa condition avant chaque passage éventuel. Suivre une boucle demande de tracer la décision, l’état avant et après le corps, puis la raison précise pour laquelle la condition finira par devenir fausse.

Le [parcours](../../parcours/) situe cette première boucle avant les fonctions et l’observation pas à pas. La pratique reste dans les projets dédiés à cloner et à ouvrir dans ton IDE.

## Références

Le projet de norme décrit l’instruction [`while`](https://eel.is/c++draft/stmt.while), les [comparaisons relationnelles](https://eel.is/c++draft/expr.rel) et l’[affectation](https://eel.is/c++draft/expr.assign). Les programmes sont vérifiés en C++17. Les décisions, gardes et retours de flux suivent la sémantique des activités UML 2.5.1.
