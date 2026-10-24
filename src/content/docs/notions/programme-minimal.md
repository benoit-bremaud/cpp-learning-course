---
title: "Lire un premier programme"
description: "Reconnaître main, son bloc et ses instructions à partir d’un message affiché."
---

**Objectif :** relier un programme complet à ce qu’il affiche, puis repérer sa structure. **Prérequis :** [comprendre la compilation](../tool-01/). Aucune connaissance des variables n’est nécessaire.

**Disponible :** exemples de lecture vérifiés sur ordinateur. Le projet autonome de pratique à cloner pour cette fiche n’est pas encore publié.

## Un besoin visible et limité

Nous voulons afficher le mot anglais `Ready` (« prêt »), passer à la ligne, puis terminer normalement. C’est un message choisi pour apprendre : il ne prouve pas qu’un capteur ou une carte est prêt.

Nous étudions un programme C++17 sur ordinateur, avec une sortie standard reliée à la console et fonctionnant normalement. La carte Arduino ou ESP32 et son démarrage seront étudiés séparément.

## Concevoir puis lire le programme

L’activité commence à l’entrée du corps de `main`. Le point noir indique ce début, les rectangles arrondis les actions et le symbole final la fin de l’activité. Le début et la fin ne sont pas deux instructions supplémentaires à écrire.

![Un premier message : actions dans leur ordre d’exécution.](/diagrams/examples/program-ready.svg)

<a href="/diagrams/examples/program-ready.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand - nouvel onglet</a>

<!-- example:program-ready -->
```cpp
#include <iostream>

int main() {
    std::cout << "Ready\n";
    return 0;
}
```

<details class="uml-panel" data-uml="program-ready">
<summary>Voir la conception UML</summary>

**Comment retrouver les actions dans ce programme ?**

![Un premier message : actions dans leur ordre d’exécution.](/diagrams/examples/program-ready.svg)

<a href="/diagrams/examples/program-ready.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand - nouvel onglet</a>

| Action du modèle | Instruction C++ |
| --- | --- |
| Écrire Ready puis un saut de ligne | `std::cout << "Ready\n";` |
| Renvoyer le statut de réussite | `return 0;` |

Le message est écrit avant le retour. Le symbole final marque la fin de cette activité ; il ne correspond pas à une instruction d’affichage.

</details>

**Sortie attendue :**

```text
Ready
```


Le programme demande un saut de ligne après `Ready` ; les caractères `\n` ne sont pas affichés tels quels. Il n’affiche pas le zéro de `return 0;`. **Statut de fin attendu :** 0.

## Premier passage : comprendre les deux actions

Une **instruction** décrit ici une action à effectuer. Le corps de ce programme en contient deux : écrire le message, puis terminer `main` en renvoyant une valeur.

`std::cout << "Ready\n";` écrit le message vers la sortie standard, ici la console. `std::cout` désigne le flux de sortie ; `<<` lui transmet ici le texte placé entre guillemets. Les guillemets délimitent ce texte et ne font pas partie du résultat. `\n` représente un saut de ligne.

`return 0;` termine `main` en transmettant un statut de réussite à l’environnement. Ce statut est distinct du texte affiché. Il ne prouve pas que tout programme satisfait son besoin : ici, il faut aussi vérifier le message attendu.

## Second passage : reconnaître la structure

| Élément | Rôle dans ce programme |
| --- | --- |
| `#include <iostream>` | Rend disponibles les déclarations nécessaires pour utiliser `std::cout`. Ce n’est pas une action d’affichage du diagramme. |
| `int` devant `main` | Indique que cette fonction renvoie un entier ; ici, la valeur 0. |
| `main` | Nom de la fonction principale appelée par l’environnement dans cet exemple sur ordinateur. |
| `()` | Cette définition ne déclare aucun paramètre. Les paramètres seront étudiés plus tard. |
| `{` et `}` | Délimitent le corps de la fonction, un bloc contenant ses instructions. |
| `;` | Termine chacune des deux instructions du corps. La directive `#include` n’en reçoit pas. |

Une **fonction** est un traitement nommé. Ici, nous apprenons à reconnaître celle qui est fournie ; nous ne demandons pas encore d’en concevoir plusieurs. Le bloc contient l’écriture du message, puis le retour. Les retours à la ligne et l’indentation rendent cet ordre plus facile à lire ; les accolades délimitent le bloc.

Le préfixe `std::` situe ici `cout` dans la bibliothèque standard. Nous reviendrons sur les espaces de noms et le fonctionnement des flux ; il suffit pour cette lecture de reconnaître l’écriture complète `std::cout`.

Une instruction isolée comme `return 0;` n’est pas à elle seule un fichier source constituant un programme complet. Dans notre exemple, elle appartient au corps de `main`.

## Comparer : terminer sans afficher

Changeons le besoin : terminer normalement, sans produire de texte. Nous retirons l’instruction d’affichage et l’inclusion qui n’est plus utilisée. Ce programme reste complet.

![Terminer sans afficher : actions dans leur ordre d’exécution.](/diagrams/examples/program-silent.svg)

<a href="/diagrams/examples/program-silent.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand - nouvel onglet</a>

<!-- example:program-silent -->
```cpp
int main() {
    return 0;
}
```

<details class="uml-panel" data-uml="program-silent">
<summary>Voir la conception UML</summary>

**Comment retrouver les actions dans ce programme ?**

![Terminer sans afficher : actions dans leur ordre d’exécution.](/diagrams/examples/program-silent.svg)

<a href="/diagrams/examples/program-silent.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand - nouvel onglet</a>

| Action du modèle | Instruction C++ |
| --- | --- |
| Renvoyer le statut de réussite | `return 0;` |

Il ne reste qu’une action : renvoyer 0. Aucune action du modèle n’écrit du texte.

</details>

**Résultat attendu :** aucun texte affiché ; le statut de fin vaut 0.


Cette comparaison montre pourquoi « le programme a réussi » et « un message est apparu » sont deux observations différentes. L’absence de texte ne signifie pas automatiquement qu’un programme n’a pas été exécuté.

Dans `main`, atteindre la fin du corps sans retour explicite équivaut à renvoyer zéro. Nous gardons ici `return 0;` pour rendre la terminaison visible dans le code ; cette règle particulière ne doit pas être généralisée à toutes les fonctions.

## Vérifier la distinction

Les deux programmes renvoient 0. Ont-ils pour autant le même résultat attendu ? Non : le premier doit écrire `Ready` puis un saut de ligne ; le second ne doit écrire aucun texte. Pour chacun, il faut comparer la sortie au besoin annoncé, puis vérifier séparément le statut de fin.

## Ce que tu peux maintenant repérer

Tu peux retrouver le bloc, l’instruction qui affiche et celle qui termine la fonction. Si tu confonds encore sortie et statut, compare les deux résultats ci-dessus avant de poursuivre.

Ces programmes ne pilotent aucun matériel. `std::cout` n’est pas présenté comme un remplacement de l’interface série Arduino. Les essais se feront dans ton IDE depuis le dépôt dédié, lorsque ce projet sera disponible.

**Suite disponible :** [suivre plusieurs affichages](../premiers-affichages/).
