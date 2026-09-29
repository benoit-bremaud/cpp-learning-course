---
title: "Exemple guidé — Le voyant à 30 °C"
description: "Lire le besoin, suivre le diagramme UML et comprendre la fonction C++ avant la pratique locale."
---

**Objectif :** relier une règle, son diagramme UML et le code qui la réalise. **État :** exemple de référence complet, validé et publié. Il fonctionne sur ordinateur ; aucune carte n’est nécessaire.

Lis d’abord [Comprendre la compilation](../notions/tool-01/). Les termes C++ utiles sont expliqués ci-dessous : tu peux suivre cet exemple sans savoir encore écrire une fonction seul. La pratique autonome viendra après les notions de types, conditions et fonctions.

## Le besoin avant le code

Le voyant devrait être allumé seulement lorsque la température **dépasse strictement 30 °C**. À 30 °C exactement, il doit rester éteint.

| Température | Résultat attendu |
| --- | --- |
| 29 °C | Éteint |
| 30 °C | Éteint |
| 31 °C | Allumé |

Nous utilisons des températures entières. La fonction détermine ce que le voyant devrait faire ; elle n’allume pas une vraie LED. La lecture du capteur et les erreurs de mesure ne font pas partie de ce premier exemple.

## Lire l’étude UML

![Activité UML : recevoir la température, comparer au seuil de 30, renvoyer vrai ou faux.](/cpp-learning-course/diagrams/threshold-indicator.svg)

Le point noir indique le début. Chaque rectangle arrondi représente une action. Le losange pose une question ; les indications `true` et `false` identifient les deux réponses possibles. Chaque chemin se termine au symbole de fin.

1. La fonction reçoit une température entière.
2. Elle établit le seuil à 30.
3. Elle vérifie si la température dépasse ce seuil.
4. Elle renvoie sa décision : vrai pour « devrait être allumé », faux pour « devrait être éteint ».

À 30 °C, la réponse à « strictement supérieur à 30 ? » est **non**. On suit donc la branche `false`.

[Lire l’étude complète](https://github.com/benoit-bremaud/cpp-learning/blob/6f6da4c440153c0709e35b823a3ef5b85c6b6b68/docs/architecture/specs/threshold-indicator.md) · [Voir la source PlantUML](https://github.com/benoit-bremaud/cpp-learning/blob/6f6da4c440153c0709e35b823a3ef5b85c6b6b68/docs/architecture/diagrams/threshold-indicator/01-activity-decision.puml)

## Retrouver la décision dans le code

Voici un extrait exact du [fichier publié](https://github.com/benoit-bremaud/cpp-learning/blob/6f6da4c440153c0709e35b823a3ef5b85c6b6b68/exercises/threshold-indicator/src/threshold_indicator.cpp). Les fichiers complets restent dans le dépôt de pratique.

```cpp
bool should_light_indicator(int temperature_celsius) noexcept {
    const int threshold_celsius = 30;

    // Keep both branches explicit to match the introductory UML activity.
    if (temperature_celsius > threshold_celsius) {
        return true;
    } else {
        return false;
    }
}
```

Une **fonction** est un traitement nommé auquel on peut fournir une donnée et qui peut renvoyer un résultat. Ici, `should_light_indicator` signifie « le voyant devrait-il s’allumer ? ».

| Élément C++ | Sens dans cet exemple | Correspondance UML |
| --- | --- | --- |
| `int temperature_celsius` | La température entière fournie au traitement. | Entrée de l’activité. |
| `bool` | Le résultat est soit vrai, soit faux. | Décision renvoyée au demandeur. |
| `const int threshold_celsius = 30` | Le seuil est initialisé à 30 et reste constant. | Action qui établit le seuil. |
| `if (... > ...)` | Suivre la première branche seulement si la comparaison est vraie. | Losange et branche `true`. |
| `return true` | Terminer la fonction en répondant « oui ». | Retour de la décision « allumé ». |
| `else` puis `return false` | Dans les autres cas, terminer en répondant « non ». | Branche `false` et décision « éteint ». |

`noexcept` indique que la fonction ne laisse pas sortir d’exception, un mécanisme C++ de signalement d’erreur qui sera étudié plus tard. Ce mot n’est pas nécessaire pour comprendre le choix entre les deux branches.

Les accolades délimitent les blocs. Les points-virgules terminent ici les déclarations et les instructions de retour. Le commentaire explique pourquoi les deux branches restent explicites : elles facilitent la lecture en parallèle du diagramme.

## Suivre un appel à la main

Avec **31**, la comparaison « 31 supérieur à 30 » est vraie : la fonction renvoie `true`. Avec **30**, elle est fausse : la fonction passe dans `else` et renvoie `false`.

Chaque appel est indépendant. Après une réponse vraie pour 31 °C, un appel avec 29 °C répond faux. La fonction ne mémorise pas l’ancien état du voyant.

Cette simplicité est volontaire : aucun pattern ni classe n’est nécessaire. La bonne pratique consiste ici à séparer la décision des accès au matériel, ce qui permet de la tester sur ordinateur.

## Ce que les tests vérifient

Le [fichier de tests](https://github.com/benoit-bremaud/cpp-learning/blob/6f6da4c440153c0709e35b823a3ef5b85c6b6b68/exercises/threshold-indicator/tests/threshold_indicator_test.cpp) fournit des températures puis compare les réponses obtenues aux réponses attendues. Il vérifie dix décisions, dont 29, 30 et 31, une température négative, les limites du type entier et plusieurs appels successifs.

Les vérifications ont réussi en Debug et en Release. Une variante volontairement incorrecte remplaçant `>` par `>=` a aussi été essayée dans une copie : **elle compile, mais le test à 30 °C échoue**. Cette observation relie directement l’exemple à la leçon sur la compilation.

## Passer à la pratique locale

Ouvre les [instructions de clonage, construction et test](https://github.com/benoit-bremaud/cpp-learning/blob/6f6da4c440153c0709e35b823a3ef5b85c6b6b68/exercises/threshold-indicator/README.md). Elles précisent les prérequis : CMake 3.20 minimum et un compilateur C++17.

Cet exemple est une solution de référence à étudier, pas un exercice à trous. Tout essai et toute modification se font dans ton IDE après clonage. Le README décrit aussi la variation incorrecte contrôlée ; elle ne change pas la conception validée.

Les liens de cette page désignent la révision validée `6f6da4c440153c0709e35b823a3ef5b85c6b6b68`. Un clonage normal récupère la version actuelle de `main`. Pour retrouver exactement cette référence dans ton clone, tu peux utiliser `git switch --detach 6f6da4c440153c0709e35b823a3ef5b85c6b6b68` avant de modifier des fichiers ; cela place Git sur cette révision sans branche active. Le [dépôt courant](https://github.com/benoit-bremaud/cpp-learning) reste accessible séparément.

## À retenir

Le besoin fixe la frontière à 30 °C, l’UML décrit les deux chemins, le code les réalise et les tests vérifient leurs résultats. Une compilation réussie ne remplace aucune de ces étapes.
