---
title: "Suivre plusieurs affichages"
description: "Observer l’ordre des instructions et distinguer lignes du code et lignes affichées."
---

**Objectif :** prévoir le texte produit par plusieurs écritures successives. **Prérequis :** [lire un premier programme](../programme-minimal/), notamment `std::cout`, le bloc de `main` et `return 0;`.

**Disponible :** trois programmes complets en C++17 pour ordinateur, à lire après la configuration de TOOL-01. Chacun doit produire la sortie indiquée, sans diagnostic sur la sortie d’erreur, puis terminer avec le statut de réussite 0. Leur projet autonome à cloner n’est pas encore publié. Aucun matériel ni variable n’est nécessaire.

## Deux messages dans un ordre choisi

Le besoin : écrire `Program started`, puis `Program finished`, chacun sur sa propre ligne. Ces messages sont de simples textes ; ils ne déclenchent pas de traitement caché.

L’activité décrit deux écritures successives, suivies du retour de réussite. Nous conservons la structure de la fiche précédente ; les messages changent et une seconde instruction d’affichage est ajoutée.

![Deux messages ordonnés : actions dans leur ordre d’exécution.](/diagrams/examples/program-ordered.svg)

<a href="/diagrams/examples/program-ordered.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand - nouvel onglet</a>

<!-- example:program-ordered -->
```cpp wrap
#include <iostream>

int main() {
    std::cout << "Program started\n";
    std::cout << "Program finished\n";
    return 0;
}
```

<details class="uml-panel" data-uml="program-ordered">
<summary>Voir la conception UML</summary>

**Comment retrouver les actions dans ce programme ?**

![Deux messages ordonnés : actions dans leur ordre d’exécution.](/diagrams/examples/program-ordered.svg)

<a href="/diagrams/examples/program-ordered.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand - nouvel onglet</a>

| Action du modèle | Instruction C++ |
| --- | --- |
| Écrire Program started puis un saut de ligne | `std::cout << "Program started\n";` |
| Écrire Program finished puis un saut de ligne | `std::cout << "Program finished\n";` |
| Renvoyer le statut de réussite | `return 0;` |

Les deux actions d’écriture suivent le même ordre que les deux instructions `std::cout`. Chaque texte contient son propre saut de ligne.

</details>

**Sortie attendue :**

```text
Program started
Program finished
```

La première écriture précède la seconde. Chaque `\n` fait commencer le texte suivant sur une nouvelle ligne. `return 0;` vient après les deux écritures ; il n’ajoute pas une troisième ligne de texte.

## Inverser uniquement les instructions

Nouveau besoin de comparaison : afficher les mêmes messages, mais dans l’ordre inverse. Les mots et les sauts de ligne restent identiques ; seule leur position change. Ce n’est pas une solution au besoin précédent : c’est une variante volontaire dont nous annonçons le résultat différent.

![Inverser les messages : actions dans leur ordre d’exécution.](/diagrams/examples/program-reversed.svg)

<a href="/diagrams/examples/program-reversed.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand - nouvel onglet</a>

<!-- example:program-reversed -->
```cpp wrap
#include <iostream>

int main() {
    std::cout << "Program finished\n";
    std::cout << "Program started\n";
    return 0;
}
```

<details class="uml-panel" data-uml="program-reversed">
<summary>Voir la conception UML</summary>

**Comment retrouver les actions dans ce programme ?**

![Inverser les messages : actions dans leur ordre d’exécution.](/diagrams/examples/program-reversed.svg)

<a href="/diagrams/examples/program-reversed.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand - nouvel onglet</a>

| Action du modèle | Instruction C++ |
| --- | --- |
| Écrire Program finished puis un saut de ligne | `std::cout << "Program finished\n";` |
| Écrire Program started puis un saut de ligne | `std::cout << "Program started\n";` |
| Renvoyer le statut de réussite | `return 0;` |

La première action écrit désormais Program finished. Les noms des messages ne déterminent pas leur ordre : les instructions le déterminent.

</details>

**Sortie attendue :**

```text
Program finished
Program started
```

Même si le message contient le mot `finished`, l’ordinateur ne le déplace pas à la fin. Il écrit le texte demandé à l’endroit où l’instruction est exécutée.

## Deux instructions ne font pas forcément deux lignes

Dernier besoin : écrire `System ready` sur une seule ligne, au moyen de deux écritures. La première fournit `System` suivi d’un espace ; la seconde fournit `ready` suivi du seul saut de ligne.

![Deux écritures, une ligne : actions dans leur ordre d’exécution.](/diagrams/examples/program-joined.svg)

<a href="/diagrams/examples/program-joined.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand - nouvel onglet</a>

<!-- example:program-joined -->
```cpp wrap
#include <iostream>

int main() {
    std::cout << "System ";
    std::cout << "ready\n";
    return 0;
}
```

<details class="uml-panel" data-uml="program-joined">
<summary>Voir la conception UML</summary>

**Comment retrouver les actions dans ce programme ?**

![Deux écritures, une ligne : actions dans leur ordre d’exécution.](/diagrams/examples/program-joined.svg)

<a href="/diagrams/examples/program-joined.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand - nouvel onglet</a>

| Action du modèle | Instruction C++ |
| --- | --- |
| Écrire System suivi d’un espace | `std::cout << "System ";` |
| Écrire ready puis un saut de ligne | `std::cout << "ready\n";` |
| Renvoyer le statut de réussite | `return 0;` |

La première écriture ne contient pas de saut de ligne. La seconde poursuit donc la même ligne, après l’espace, puis la termine.

</details>

**Sortie attendue :**

```text
System ready
```

| Point d’observation | Texte produit jusque-là |
| --- | --- |
| Après la première écriture | `System` suivi d’un espace, sans saut de ligne. |
| Après la seconde | `System ready` suivi d’un saut de ligne. |

L’espace est à l’intérieur des premiers guillemets. Le retour à la ligne du fichier source, entre les deux instructions, ne demande aucun saut de ligne dans la sortie. C’est `\n`, dans le texte, qui le demande ici.

## Relier les trois comparaisons

| Ce qui change | Ce qui explique le résultat |
| --- | --- |
| Ajouter une écriture | Une action supplémentaire est exécutée. |
| Inverser deux écritures | L’ordre des messages change. |
| Choisir où placer les sauts de ligne | Le nombre de lignes affichées ne dépend pas du nombre de lignes du code. |

Les diagrammes décrivent les demandes d’écriture dans leur ordre ; ils ne modélisent ni la gestion interne des buffers ni l’instant physique d’apparition de chaque caractère à l’écran.

Tu disposes maintenant d’une structure connue pour lire les prochaines instructions. La saisie au clavier et les erreurs d’entrée viendront plus tard. La pratique reste dans l’IDE après clonage, pas dans le navigateur.

**Suite :** [initialiser une variable](../cpp-01/). L’affichage te donne un premier exemple d’instruction ; la prochaine fiche introduit une donnée nommée.
