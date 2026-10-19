---
title: "Deux chemins avec else — choisir une alternative"
description: "Exécuter un seul des deux blocs, puis retrouver la suite commune, avec cinq programmes expliqués."
---

**Objectif :** prévoir quel bloc s’exécute dans un `if` accompagné de `else`, puis expliquer ce que signifie le chemin choisi. **Prérequis :** [la première condition](../premiere-condition/), [l’égalité et la différence](../egal-ou-different/), les variables et les booléens. Pour l’affichage, tu peux revoir [les messages successifs](../premiers-affichages/).

**Disponible :** cinq programmes complets de lecture, leurs sorties et leurs cartes UML. Le projet autonome de pratique à cloner pour cette leçon n’est pas encore publié.

## Donner aussi une action au chemin faux

Dans la leçon précédente, une réponse fausse sautait le bloc du `if`, puis le programme continuait. Nous voulons maintenant écrire un message dans ce cas aussi. `else` se lit **« sinon »** : il introduit le bloc exécuté quand la condition du `if` est fausse.

Nous gardons une cible exacte de **3 mesures**. `Target matched` signifie « la valeur correspond à la cible » ; `Target not matched`, « la valeur ne correspond pas à la cible ». `Check finished` signifie « vérification terminée » et reste exigé après chacun des deux chemins.

Les valeurs sont fournies dans le programme, dans le domaine entier de 0 à 20. Les programmes s’exécutent sur ordinateur avec une sortie standard reliée à la console et fonctionnant normalement. Aucune acquisition de capteur ni saisie n’est introduite ici.

## 1 — Une réponse vraie choisit le premier bloc

Le compteur vaut **3** et la cible vaut **3**. Le booléen vaut donc `true`. Nous voulons écrire le message de correspondance, puis le message commun de fin.

**Sortie attendue :**

```text
Target matched
Check finished
```

![Activité UML : deux chemins exclusifs puis une écriture commune.](/diagrams/examples/first-else-matched.svg)

<a href="/diagrams/examples/first-else-matched.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

Le premier **losange UML** représente le choix. La garde `[target_matched]` autorise le chemin vrai ; `[not target_matched]` désigne ici le chemin faux. Ces deux gardes sont exclusives : une seule convient à ce passage.

Le second losange **réunit les chemins** avant `Check finished`. Il n’attend pas deux traitements : nous ne parcourons pas les deux branches. Les rectangles sont des actions ; les symboles initial et final délimitent l’activité dans `main`. `#include` n’est pas une action exécutée dans ce chemin.

<!-- example:first-else-matched -->
```cpp
#include <iostream>

int main() {
    const int measurement_target = 3;
    int measurement_count = 3;
    bool target_matched = measurement_count == measurement_target;

    if (target_matched) {
        std::cout << "Target matched\n";
    } else {
        std::cout << "Target not matched\n";
    }
    std::cout << "Check finished\n";
    return 0;
}
```

<details class="uml-panel" data-uml="first-else-matched">
<summary>Voir la conception UML</summary>

| Étape UML attendue | Correspondance C++ |
| --- | --- |
| Préparer les valeurs | Valeur fournie : 3 ; valeur attendue : 3. |
| Calculer la réponse | `==` initialise `target_matched` à `true`. |
| Choisir un chemin | `if (target_matched)` lit cette réponse ; le bloc `if` est choisi. |
| Écriture du chemin | `Target matched` est écrit ; `Target not matched` est sauté. |
| Suite commune | `Check finished` est écrit après les deux blocs. |
| Terminer | `return 0;` renvoie le statut 0 sans l’afficher. |

![Activité UML : deux chemins exclusifs puis une écriture commune.](/diagrams/examples/first-else-matched.svg)

<a href="/diagrams/examples/first-else-matched.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

### Lire la syntaxe

| Élément | Rôle |
| --- | --- |
| `if (target_matched)` | Choisit à partir du booléen déjà calculé. |
| Premier bloc `{ ... }` | S’exécute quand la condition est vraie. |
| `else` et son bloc `{ ... }` | S’exécutent quand cette même condition est fausse. |
| Écriture après le second bloc | Appartient à la suite commune. |

`else` ne reçoit pas une deuxième condition entre parenthèses. Il complète ce `if`. Ici, chaque bloc contient une écriture ; les accolades en rendent le périmètre explicite. Elles restent distinctes de celles de `main`, qui entourent l’ensemble. L’indentation aide à lire ; les accolades déterminent les blocs.

Il n’y a pas de point-virgule entre la condition et son bloc, ni entre la fermeture de ce bloc et `else`. Les instructions `std::cout` gardent leur point-virgule.

### Suivre ce passage

| Point d’observation | Exécution réelle |
| --- | --- |
| Initialisations | 3 face à 3 donne `true` pour `target_matched`. |
| Branche choisie | Le bloc `if` écrit `Target matched` et un saut de ligne. |
| Branche sautée | Le bloc `else` n’écrit pas `Target not matched`. |
| Après les deux blocs | `Check finished` et un saut de ligne sont écrits. |
| Retour | Le programme termine avec le statut 0. |

La comparaison est calculée pendant l’initialisation du booléen. Le `if` lit ensuite cette valeur ; il ne recalcule pas `==`. Aucun nombre ni booléen ne change ici. Une visite du `if` choisit un chemin une fois : elle n’attend pas une nouvelle valeur et ne recommence pas seule.

## 2 — Une réponse fausse choisit le bloc else

Changeons seulement le compteur : il vaut **2**, pour une cible de **3**. La réponse est `false`. Cette fois, le chemin faux possède sa propre écriture.

**Sortie attendue :**

```text
Target not matched
Check finished
```

![Activité UML : deux chemins exclusifs puis une écriture commune.](/diagrams/examples/first-else-below.svg)

<a href="/diagrams/examples/first-else-below.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:first-else-below -->
```cpp
#include <iostream>

int main() {
    const int measurement_target = 3;
    int measurement_count = 2;
    bool target_matched = measurement_count == measurement_target;

    if (target_matched) {
        std::cout << "Target matched\n";
    } else {
        std::cout << "Target not matched\n";
    }
    std::cout << "Check finished\n";
    return 0;
}
```

<details class="uml-panel" data-uml="first-else-below">
<summary>Voir la conception UML</summary>

| Étape UML attendue | Correspondance C++ |
| --- | --- |
| Préparer les valeurs | Valeur fournie : 2 ; valeur attendue : 3. |
| Calculer la réponse | `==` initialise `target_matched` à `false`. |
| Choisir un chemin | `if (target_matched)` lit cette réponse ; le bloc `else` est choisi. |
| Écriture du chemin | `Target not matched` est écrit ; `Target matched` est sauté. |
| Suite commune | `Check finished` est écrit après les deux blocs. |
| Terminer | `return 0;` renvoie le statut 0 sans l’afficher. |

![Activité UML : deux chemins exclusifs puis une écriture commune.](/diagrams/examples/first-else-below.svg)

<a href="/diagrams/examples/first-else-below.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

### Suivre ce passage

| Point d’observation | Exécution réelle |
| --- | --- |
| Initialisations | 2 face à 3 donne `false` pour `target_matched`. |
| Branche choisie | Le bloc `else` écrit `Target not matched` et un saut de ligne. |
| Branche sautée | Le bloc `if` n’écrit pas `Target matched`. |
| Après les deux blocs | `Check finished` et un saut de ligne sont écrits. |
| Retour | Le programme termine avec le statut 0. |

Dans la leçon précédente, ce même compteur produisait seulement `Check finished`. L’ajout de `else` donne une action au chemin faux. Il ne rend pas le message commun conditionnel : celui-ci reste après les deux blocs.

## 3 — Au-dessus de la cible, la réponse reste fausse

Le compteur vaut maintenant **4**. Avant de lire la sortie, formule la question exacte : « Est-ce égal à trois ? » Quatre est supérieur à trois, mais il ne lui est pas égal.

**Sortie attendue :**

```text
Target not matched
Check finished
```

![Activité UML : deux chemins exclusifs puis une écriture commune.](/diagrams/examples/first-else-above.svg)

<a href="/diagrams/examples/first-else-above.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:first-else-above -->
```cpp
#include <iostream>

int main() {
    const int measurement_target = 3;
    int measurement_count = 4;
    bool target_matched = measurement_count == measurement_target;

    if (target_matched) {
        std::cout << "Target matched\n";
    } else {
        std::cout << "Target not matched\n";
    }
    std::cout << "Check finished\n";
    return 0;
}
```

<details class="uml-panel" data-uml="first-else-above">
<summary>Voir la conception UML</summary>

| Étape UML attendue | Correspondance C++ |
| --- | --- |
| Préparer les valeurs | Valeur fournie : 4 ; valeur attendue : 3. |
| Calculer la réponse | `==` initialise `target_matched` à `false`. |
| Choisir un chemin | `if (target_matched)` lit cette réponse ; le bloc `else` est choisi. |
| Écriture du chemin | `Target not matched` est écrit ; `Target matched` est sauté. |
| Suite commune | `Check finished` est écrit après les deux blocs. |
| Terminer | `return 0;` renvoie le statut 0 sans l’afficher. |

![Activité UML : deux chemins exclusifs puis une écriture commune.](/diagrams/examples/first-else-above.svg)

<a href="/diagrams/examples/first-else-above.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

### Suivre ce passage

| Point d’observation | Exécution réelle |
| --- | --- |
| Initialisations | 4 face à 3 donne `false` pour `target_matched`. |
| Branche choisie | Le bloc `else` écrit `Target not matched` et un saut de ligne. |
| Branche sautée | Le bloc `if` n’écrit pas `Target matched`. |
| Après les deux blocs | `Check finished` et un saut de ligne sont écrits. |
| Retour | Le programme termine avec le statut 0. |

### Deux valeurs différentes, un même chemin

| Compteur fourni | `target_matched` | Bloc choisi | Messages, dans l’ordre |
| --- | --- | --- | --- |
| 2 | `false` | `else` | `Target not matched`, puis `Check finished` |
| 3 | `true` | `if` | `Target matched`, puis `Check finished` |
| 4 | `false` | `else` | `Target not matched`, puis `Check finished` |

Chaque ligne décrit une exécution indépendante ; chaque message est suivi d’un saut de ligne. **Le chemin `else` ne distingue pas ici « en dessous » et « au-dessus ».** Il signifie que la réponse à l’égalité est fausse. Le sens du chemin dépend de la question posée, pas du mot `else` seul.

## 4 — Retrouver le choix pour un identifiant

Le numéro attendu vaut **7** et le numéro fourni vaut **9**. `Identifier matched` signifie « identifiant correspondant » ; `Identifier not matched`, « identifiant non correspondant ». Nous comparons des étiquettes entières : ce programme ne détecte ni n’authentifie un appareil.

**Sortie attendue :**

```text
Identifier not matched
Check finished
```

![Activité UML : deux chemins exclusifs puis une écriture commune.](/diagrams/examples/first-else-identifier.svg)

<a href="/diagrams/examples/first-else-identifier.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:first-else-identifier -->
```cpp
#include <iostream>

int main() {
    const int expected_identifier = 7;
    int observed_identifier = 9;
    bool identifier_matched = observed_identifier == expected_identifier;

    if (identifier_matched) {
        std::cout << "Identifier matched\n";
    } else {
        std::cout << "Identifier not matched\n";
    }
    std::cout << "Check finished\n";
    return 0;
}
```

<details class="uml-panel" data-uml="first-else-identifier">
<summary>Voir la conception UML</summary>

| Étape UML attendue | Correspondance C++ |
| --- | --- |
| Préparer les valeurs | Valeur fournie : 9 ; valeur attendue : 7. |
| Calculer la réponse | `==` initialise `identifier_matched` à `false`. |
| Choisir un chemin | `if (identifier_matched)` lit cette réponse ; le bloc `else` est choisi. |
| Écriture du chemin | `Identifier not matched` est écrit ; `Identifier matched` est sauté. |
| Suite commune | `Check finished` est écrit après les deux blocs. |
| Terminer | `return 0;` renvoie le statut 0 sans l’afficher. |

![Activité UML : deux chemins exclusifs puis une écriture commune.](/diagrams/examples/first-else-identifier.svg)

<a href="/diagrams/examples/first-else-identifier.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

### Suivre ce passage

| Point d’observation | Exécution réelle |
| --- | --- |
| Initialisations | 9 face à 7 donne `false` pour `identifier_matched`. |
| Branche choisie | Le bloc `else` écrit `Identifier not matched` et un saut de ligne. |
| Branche sautée | Le bloc `if` n’écrit pas `Identifier matched`. |
| Après les deux blocs | `Check finished` et un saut de ligne sont écrits. |
| Retour | Le programme termine avec le statut 0. |

| Identifiant fourni | `identifier_matched` | Premier message |
| --- | --- | --- |
| 5 | `false` | `Identifier not matched` |
| 7 | `true` | `Identifier matched` |
| 9 | `false` | `Identifier not matched` |

Dans chaque cas, `Check finished` suit ; les deux messages ont chacun leur saut de ligne. Un numéro plus grand n’est pas « davantage correct » : nous recherchons une correspondance exacte.

## 5 — Un message plausible, mais faux

**Erreur volontaire :** pour le compteur de **4**, remplaçons le message du `else` par `Below target`, qui signifie « inférieur à la cible ». Le besoin reste celui du troisième exemple : annoncer une absence de correspondance exacte. Sa conception UML, visible plus haut, reste la référence attendue.

<!-- example:first-else-wrong-message -->
```cpp
#include <iostream>

int main() {
    const int measurement_target = 3;
    int measurement_count = 4;
    bool target_matched = measurement_count == measurement_target;

    if (target_matched) {
        std::cout << "Target matched\n";
    } else {
        std::cout << "Below target\n";
    }
    std::cout << "Check finished\n";
    return 0;
}
```

<details class="uml-panel" data-uml="first-else-wrong-message">
<summary>Comprendre l’écart avec la conception</summary>

**Attendu : Target not matched ; obtenu : Below target.** Dans les deux cas, `Check finished` suit sur la ligne suivante. Le diagramme représente le comportement attendu, pas le message du programme fautif.

| Étape UML attendue | Correspondance C++ ou écart |
| --- | --- |
| Préparer les valeurs | Valeur fournie : 4 ; valeur attendue : 3. |
| Calculer la réponse | `==` initialise `target_matched` à `false`. |
| Choisir un chemin | `if (target_matched)` lit cette réponse ; le bloc `else` est choisi. |
| Écriture du chemin | Écart : `Below target` remplace le message requis `Target not matched`. |
| Suite commune | `Check finished` est écrit après les deux blocs. |
| Terminer | `return 0;` renvoie le statut 0 sans l’afficher. |

![Activité UML : deux chemins exclusifs puis une écriture commune.](/diagrams/examples/first-else-above.svg)

<a href="/diagrams/examples/first-else-above.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

### Suivre ce passage

| Point d’observation | Exécution réelle |
| --- | --- |
| Initialisations | 4 face à 3 donne `false` pour `target_matched`. |
| Branche choisie | Le bloc `else` écrit `Below target` et un saut de ligne. |
| Branche sautée | Le bloc `if` n’écrit pas `Target matched`. |
| Après les deux blocs | `Check finished` et un saut de ligne sont écrits. |
| Retour | Le programme termine avec le statut 0. |

**Sortie réelle :**

```text
Below target
Check finished
```

**Sortie attendue :**

```text
Target not matched
Check finished
```

La comparaison et le choix du bloc sont corrects : quatre n’est pas trois. L’erreur se trouve dans ce que le message affirme. Le compilateur accepte ce texte, mais quatre n’est pas inférieur à trois.

**Correction :** remplacer `Below target` par `Target not matched`, comme dans le troisième programme. Changer la comparaison pour sauver ce message changerait le besoin : nous voulons toujours vérifier une égalité exacte.

| Compteur | Ce que révèle le programme fautif |
| --- | --- |
| 2 | « Inférieur » décrit bien la valeur, mais ce n’est pas le message exigé. |
| 3 | Le chemin fautif n’est pas exécuté ; le message affiché est correct. |
| 4 | Le chemin fautif affirme une relation fausse. |

Tester seulement trois ne montre donc pas l’erreur. Deux révèle un écart de texte avec le besoin ; quatre révèle aussi une affirmation fausse. Le statut 0 indique une terminaison normale, pas le respect du besoin.

## Vérifier sa compréhension

- Pour un compteur de 4, quel bloc écrit le premier message ? Pourquoi ?
- Les deux blocs s’exécutent-ils successivement quand la condition est vraie ?
- Pourquoi `Check finished` apparaît-il quel que soit le chemin ?
- `else` signifie-t-il toujours « inférieur » ?
- Pourquoi le programme fautif compile-t-il malgré son message trompeur ?

**Repères pour te corriger :** le bloc `else`, car 4 n’est pas égal à 3 ; non, seul le bloc `if` est exécuté ; l’écriture commune est après les deux blocs ; non, il correspond à une condition fausse ; le texte est valide en C++, mais son sens ne satisfait pas le besoin.

**À retenir :** lors de ce passage, `if` et `else` sélectionnent un seul de leurs deux blocs. Le programme continue ensuite après l’ensemble. Pour comprendre le chemin faux, relis la question exacte dont le booléen contient la réponse.

**Suite :** [contrôler un ajout avec une limite](../ajout-sous-limite/) utilise une condition pour autoriser ou refuser une modification du compteur. La pratique reste dans les dépôts à cloner et dans ton IDE.

## Références

La [règle du `if`](https://eel.is/c++draft/stmt.if) décrit la sélection du premier ou du second bloc selon la condition. Cette référence est le projet de norme ; les programmes de cette page sont vérifiés en C++17.

La [norme UML 2.5.1](https://www.omg.org/spec/UML/2.5.1/PDF), sections 15.3.3.5–15.3.3.6 et 15.3.4.3, définit les décisions, les réunions de chemins et leur notation.
