---
title: "Première condition — exécuter ou sauter un bloc avec if"
description: "Suivre une condition vraie ou fausse, puis retrouver les instructions communes après le bloc."
---

**Objectif :** prévoir les instructions exécutées avec `if`, puis expliquer où le programme continue. **Prérequis :** [égal ou différent](../egal-ou-different/), les variables et les booléens. Pour revoir l’affichage, consulte [le premier programme](../programme-minimal/) et [les affichages successifs](../premiers-affichages/).

**Disponible :** quatre programmes complets de lecture avec leurs sorties et leurs cartes UML. Le projet autonome de pratique à cloner pour cette leçon n’est pas encore publié.

## Passer de la réponse à l’action

Jusqu’ici, une comparaison produisait une réponse vraie ou fausse. Nous voulons maintenant **écrire un message seulement si cette réponse est vraie**, puis écrire un message de fin dans les deux cas.

Nous réutilisons une cible exacte de **3 mesures**. `Target matched` signifie « la valeur correspond à la cible » ; `Check finished` signifie « vérification terminée ». Ces textes ne déclenchent aucun traitement caché.

Les programmes s’exécutent sur ordinateur avec une sortie standard reliée à la console et fonctionnant normalement. Les nombres sont fournis directement, dans le domaine entier de 0 à 20. Aucun capteur n’est lu et aucune saisie n’est demandée.

## 1 — Exécuter le bloc quand la réponse est vraie

Le compteur vaut **3**, comme la cible. Nous voulons afficher le message de correspondance, puis celui de fin.

**Sortie attendue :**

```text
Target matched
Check finished
```

![Activité UML : lire target_matched, exécuter ou contourner le message, puis rejoindre Check finished.](/diagrams/examples/first-if-matched.svg)

<a href="/diagrams/examples/first-if-matched.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

Le diagramme conserve les deux chemins possibles, même si la valeur fournie permet déjà de savoir lequel sera suivi.

- Le premier **losange** représente la décision. `[target_matched]` est une **garde** : ce chemin convient quand le booléen est vrai.
- `[not target_matched]` désigne le chemin où il est faux. Dans cette garde UML, `not` se lit « non » ; aucune instruction supplémentaire n’est à ajouter à notre programme.
- Le second losange **réunit les chemins** avant l’écriture commune. Il n’attend pas que deux traitements se terminent : dans cet exemple, un seul chemin est suivi.

Les rectangles restent les actions ; le point initial et le symbole final délimitent l’activité. Le diagramme commence dans `main` : `#include` rend l’affichage disponible, mais n’est pas une action exécutée à cet endroit.

<!-- example:first-if-matched -->
```cpp
#include <iostream>

int main() {
    const int measurement_target = 3;
    int measurement_count = 3;
    bool target_matched = measurement_count == measurement_target;

    if (target_matched) {
        std::cout << "Target matched\n";
    }
    std::cout << "Check finished\n";
    return 0;
}
```

<details class="uml-panel" data-uml="first-if-matched">
<summary>Voir la conception UML</summary>

| Étape UML attendue | Correspondance C++ |
| --- | --- |
| Préparer les valeurs et la réponse | `measurement_target` vaut 3, `measurement_count` vaut 3, `target_matched` vaut `true`. |
| Choisir le chemin | `if (target_matched)` lit le booléen déjà calculé. |
| Écriture conditionnelle | `Target matched` est écrit dans le bloc. |
| Suite commune | `Check finished` est écrit après le bloc, quel que soit le chemin choisi. |
| Terminer | `return 0;` renvoie le statut 0 sans l’afficher. |

![Activité UML : lire target_matched, exécuter ou contourner le message, puis rejoindre Check finished.](/diagrams/examples/first-if-matched.svg)

<a href="/diagrams/examples/first-if-matched.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

### Lire la nouvelle syntaxe

| Élément | Rôle |
| --- | --- |
| `if` | Introduit l’exécution conditionnelle ; on le lit « si ». |
| `(target_matched)` | La condition : ici, lire un booléen déjà calculé. |
| `{` et `}` après la condition | Délimitent le bloc contrôlé. |
| L’écriture à l’intérieur | S’exécute seulement si la condition est vraie. |
| L’écriture après l’accolade fermante | Appartient à la suite commune. |

Les accolades de `main` entourent tout le programme étudié ; celles du `if` entourent seulement son bloc. L’indentation aide à les distinguer. Nous utilisons des accolades dès le début pour rendre ce périmètre explicite, même si le C++ permet aussi de contrôler une seule instruction sans elles.

Observe qu’il n’y a pas de point-virgule entre `if (target_matched)` et son bloc. Les instructions d’affichage à l’intérieur ou après le bloc conservent leur point-virgule habituel.

### Suivre ce passage

| Point d’observation | Ce qui se produit |
| --- | --- |
| Initialisations | Les entiers valent 3 et 3 ; `target_matched` vaut `true`. |
| Condition | La valeur `true` sélectionne le chemin qui entre dans le bloc. |
| Bloc contrôlé | Écriture de `Target matched` et d’un saut de ligne. |
| Après le bloc | Écriture de `Check finished` et d’un saut de ligne. |
| Retour | Le programme termine avec le statut 0. |

La comparaison `==` est évaluée lors de l’initialisation de `target_matched`. Le `if` lit ensuite cette réponse ; il ne recalcule pas la comparaison. Aucun nombre ni booléen n’est modifié dans ce passage.

Le `if` n’attend pas un changement de valeur et ne recommence pas tout seul. Nous suivons une seule visite de cette instruction ; la répétition sera étudiée avec les boucles.

## 2 — Sauter le bloc, puis continuer

Nous changeons seulement la valeur fournie : le compteur vaut maintenant **2**, pour une cible toujours à **3**. La comparaison donne `false`. Avant de lire la sortie, repère l’instruction située après l’accolade fermante du `if`.

**Sortie attendue :**

```text
Check finished
```

Le message de correspondance doit être absent. Le message de fin reste requis.

![Activité UML : lire target_matched, exécuter ou contourner le message, puis rejoindre Check finished.](/diagrams/examples/first-if-unmatched.svg)

<a href="/diagrams/examples/first-if-unmatched.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:first-if-unmatched -->
```cpp
#include <iostream>

int main() {
    const int measurement_target = 3;
    int measurement_count = 2;
    bool target_matched = measurement_count == measurement_target;

    if (target_matched) {
        std::cout << "Target matched\n";
    }
    std::cout << "Check finished\n";
    return 0;
}
```

<details class="uml-panel" data-uml="first-if-unmatched">
<summary>Voir la conception UML</summary>

| Étape UML attendue | Correspondance C++ |
| --- | --- |
| Préparer les valeurs et la réponse | `measurement_target` vaut 3, `measurement_count` vaut 2, `target_matched` vaut `false`. |
| Choisir le chemin | `if (target_matched)` lit le booléen déjà calculé. |
| Écriture conditionnelle | Le bloc est sauté : `Target matched` n’est pas écrit. |
| Suite commune | `Check finished` est écrit après le bloc, quel que soit le chemin choisi. |
| Terminer | `return 0;` renvoie le statut 0 sans l’afficher. |

![Activité UML : lire target_matched, exécuter ou contourner le message, puis rejoindre Check finished.](/diagrams/examples/first-if-unmatched.svg)

<a href="/diagrams/examples/first-if-unmatched.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

### Suivre ce passage

| Point d’observation | Ce qui se produit |
| --- | --- |
| Initialisations | Les entiers valent 2 et 3 ; `target_matched` vaut `false`. |
| Condition | La valeur `false` sélectionne le chemin qui contourne le bloc. |
| Bloc contrôlé | L’écriture conditionnelle est sautée. |
| Après le bloc | Écriture de `Check finished` et d’un saut de ligne. |
| Retour | Le programme termine avec le statut 0. |

**Faux ne signifie pas « arrêter le programme ».** Seul le bloc du `if` est sauté. L’instruction suivante, à l’extérieur, s’exécute ensuite.

Sur l’UML, suis la garde `[not target_matched]` : la flèche contourne le message de correspondance et rejoint l’autre chemin avant `Check finished`. Le mot `not` exprime ici la condition du chemin UML ; le code conserve simplement `if (target_matched)`.

| Compteur fourni | `target_matched` | Texte affiché, dans l’ordre |
| --- | --- | --- |
| 2 | `false` | `Check finished` |
| 3 | `true` | `Target matched`, puis `Check finished` |
| 4 | `false` | `Check finished` |

Chaque message est suivi d’un saut de ligne. Quatre n’est pas exactement trois : ce cas suit le même chemin que deux. Il s’agit de trois exécutions indépendantes avec des valeurs fournies différentes.

## 3 — Signaler un identifiant reconnu

Réutilisons les étiquettes entières de la leçon précédente. Le numéro recherché vaut **7** et la valeur fournie vaut également **7**. Nous voulons afficher `Identifier matched` (« identifiant correspondant »), puis terminer la vérification.

**Sortie attendue :**

```text
Identifier matched
Check finished
```

La valeur est écrite dans le programme : cet exemple ne détecte pas un appareil et ne l’authentifie pas. Il applique le même choix de chemin à un autre besoin.

![Activité UML : lire identifier_matched, exécuter ou contourner le message, puis rejoindre Check finished.](/diagrams/examples/first-if-identifier.svg)

<a href="/diagrams/examples/first-if-identifier.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

<!-- example:first-if-identifier -->
```cpp
#include <iostream>

int main() {
    const int expected_identifier = 7;
    int observed_identifier = 7;
    bool identifier_matched = observed_identifier == expected_identifier;

    if (identifier_matched) {
        std::cout << "Identifier matched\n";
    }
    std::cout << "Check finished\n";
    return 0;
}
```

<details class="uml-panel" data-uml="first-if-identifier">
<summary>Voir la conception UML</summary>

| Étape UML attendue | Correspondance C++ |
| --- | --- |
| Préparer les valeurs et la réponse | `expected_identifier` vaut 7, `observed_identifier` vaut 7, `identifier_matched` vaut `true`. |
| Choisir le chemin | `if (identifier_matched)` lit le booléen déjà calculé. |
| Écriture conditionnelle | `Identifier matched` est écrit dans le bloc. |
| Suite commune | `Check finished` est écrit après le bloc, quel que soit le chemin choisi. |
| Terminer | `return 0;` renvoie le statut 0 sans l’afficher. |

![Activité UML : lire identifier_matched, exécuter ou contourner le message, puis rejoindre Check finished.](/diagrams/examples/first-if-identifier.svg)

<a href="/diagrams/examples/first-if-identifier.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

### Suivre ce passage

| Point d’observation | Ce qui se produit |
| --- | --- |
| Initialisations | Les entiers valent 7 et 7 ; `identifier_matched` vaut `true`. |
| Condition | La valeur `true` sélectionne le chemin qui entre dans le bloc. |
| Bloc contrôlé | Écriture de `Identifier matched` et d’un saut de ligne. |
| Après le bloc | Écriture de `Check finished` et d’un saut de ligne. |
| Retour | Le programme termine avec le statut 0. |

La structure du choix est identique, mais le message exprime une correspondance d’étiquette plutôt qu’un nombre de mesures.

| Identifiant fourni | `identifier_matched` | Texte affiché, dans l’ordre |
| --- | --- | --- |
| 5 | `false` | `Check finished` |
| 7 | `true` | `Identifier matched`, puis `Check finished` |
| 9 | `false` | `Check finished` |

Les messages se terminent chacun par un saut de ligne. Un numéro supérieur au numéro recherché ne convient pas davantage qu’un numéro inférieur. Dans tous ces cas, la vérification se termine par le message commun.

## 4 — Rendre la suite conditionnelle par erreur

Revenons au compteur de **2** pour une cible de **3**. Le besoin reste celui du deuxième exemple : **afficher `Check finished` suivi d’un saut de ligne**, même si la cible ne correspond pas.

**Erreur volontaire :** nous déplaçons cette écriture à l’intérieur du bloc contrôlé. La conception attendue est celle du deuxième exemple, visible plus haut. La carte distingue cette conception de l’exécution incorrecte.

<!-- example:first-if-misplaced -->
```cpp
#include <iostream>

int main() {
    const int measurement_target = 3;
    int measurement_count = 2;
    bool target_matched = measurement_count == measurement_target;

    if (target_matched) {
        std::cout << "Target matched\n";
        std::cout << "Check finished\n";
    }
    return 0;
}
```

<details class="uml-panel" data-uml="first-if-misplaced">
<summary>Comprendre l’écart avec la conception</summary>

**Attendu : `Check finished` suivi d’un saut de ligne ; obtenu : aucun texte.** Le diagramme décrit la conception attendue, pas l’exécution de ce programme fautif.

| Étape UML attendue | Correspondance C++ ou écart |
| --- | --- |
| Préparer les valeurs et la réponse | `measurement_target` vaut 3, `measurement_count` vaut 2, `target_matched` vaut `false`. |
| Choisir le chemin | `if (target_matched)` lit le booléen déjà calculé. |
| Écriture conditionnelle | Le bloc est sauté : `Target matched` n’est pas écrit. |
| Suite commune | Écart : l’écriture de `Check finished` est dans le bloc ; elle est sautée elle aussi. |
| Terminer | `return 0;` renvoie le statut 0 sans l’afficher. |

![Activité UML : lire target_matched, exécuter ou contourner le message, puis rejoindre Check finished.](/diagrams/examples/first-if-unmatched.svg)

<a href="/diagrams/examples/first-if-unmatched.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

</details>

### Suivre ce passage

| Point d’observation | Ce qui se produit |
| --- | --- |
| Initialisations | Les entiers valent 2 et 3 ; `target_matched` vaut `false`. |
| Condition | La valeur `false` sélectionne le chemin qui contourne le bloc. |
| Bloc contrôlé | Les deux écritures sont sautées. |
| Après le bloc | Aucune écriture ne reste à cet endroit : aucun texte n’a été produit. |
| Retour | Le programme termine avec le statut 0. |

**Sortie réelle : aucun texte, pas même une ligne vide.** Pourtant, le programme compile et termine avec le statut 0. Il n’a simplement pas exécuté une écriture exigée par le besoin.

La faute ne vient ni de la comparaison ni de sa réponse : `false` est correct pour deux face à trois. Elle vient de la place de `Check finished`, désormais contrôlé par la condition.

**Correction :** replacer cette écriture après l’accolade fermante du `if`, comme dans le deuxième exemple. Changer uniquement l’indentation sans déplacer l’instruction hors des accolades ne corrigerait pas le comportement.

| Compteur | Programme attendu | Programme avec la suite mal placée |
| --- | --- | --- |
| 2 | `Check finished` | Aucun texte |
| 3 | `Target matched`, puis `Check finished` | Les deux mêmes messages |
| 4 | `Check finished` | Aucun texte |

Avec trois, le défaut passe inaperçu : les deux écritures du bloc s’exécutent. **Vérifier aussi une condition fausse est indispensable pour révéler cette erreur.** Les virgules du tableau séparent les messages ; elles ne font pas partie de la sortie.

## Vérifier sa compréhension

- Quand `target_matched` vaut `false`, le programme s’arrête-t-il au `if` ?
- Pourquoi `Check finished` apparaît-il dans les deux premiers programmes ?
- Quelle différence y a-t-il entre calculer `target_matched` et l’utiliser dans `if` ?
- Pourquoi le second losange UML n’attend-il pas deux chemins ?
- Quel test révèle la suite mal placée : un compteur de 3 ou de 2 ?

**Repères pour te corriger :** non, il continue après le bloc ; l’écriture est hors du bloc contrôlé ; la comparaison calcule la réponse, le `if` sélectionne un chemin à partir de cette réponse ; un seul chemin a été suivi ; 2.

**À retenir :** `if` contrôle son bloc. Une condition fausse saute ce bloc ; elle ne saute pas la suite du programme. Les accolades indiquent les instructions contrôlées.

**Suite prévue :** ajouter une action alternative avec `else`, dans un module distinct. Le [parcours](../../parcours/) conserve ce découpage ; la pratique s’effectue dans les dépôts à cloner, pas dans le navigateur.

## Références

La [règle du `if`](https://eel.is/c++draft/stmt.if) décrit l’exécution conditionnelle et la [règle des blocs](https://eel.is/c++draft/stmt.block) leur regroupement par accolades. Ces références sont le projet de norme ; les programmes de la page sont vérifiés en C++17.

La [norme UML 2.5.1](https://www.omg.org/spec/UML/2.5.1/PDF), sections 15.3.3.5 et 15.3.3.6, distingue la réunion des chemins sans synchronisation et la sélection d’un chemin par une décision.
