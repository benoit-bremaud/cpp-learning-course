---
title: "CPP-09 — Exprimer une valeur constante"
description: "Comprendre const avec une limite fixe, un compteur modifiable et deux erreurs différentes."
---

**Objectif :** choisir ce qui doit rester stable et comprendre ce que `const` fait vérifier. **Prérequis :** [initialisation et affectation dans CPP-01](../cpp-01/). Nous restons sur des entiers locaux simples.

**Disponible :** un exemple conçu en UML et des comparaisons commentées. Le projet autonome à cloner pour cette leçon n’est pas encore publié.

**Pour cette lecture :** tu dois pouvoir distinguer une initialisation d’une affectation, comme dans CPP-01. Nous ajoutons une seule question : quelle donnée doit rester inchangée ? Les paramètres de fonction et `constexpr` ne sont pas des prérequis ; leur étude viendra plus tard.

## Choisir ce qui peut changer

Pour une session de mesures, le besoin fixe une limite de **3 mesures**. Cette limite doit rester inchangée pendant le traitement. Le nombre de mesures déjà reçues, lui, peut évoluer.

| Donnée | Nom dans le code | Rôle |
| --- | --- | --- |
| Limite choisie | `measurement_limit` | Rester à 3 |
| Nombre de mesures reçues | `measurement_count` | Représenter le total courant, d’abord 0 puis 1 dans cet exemple |

La valeur 3 est un choix fictif du besoin, pas une capacité matérielle. **Déclarer une limite ne suffit pas à empêcher son dépassement.** Notre exemple ne réserve aucune mémoire pour les mesures et ne contrôle pas encore le compteur par rapport à la limite.

Comme dans CPP-01, nous enregistrons un nouveau total connu : l’affectation de 1 ne détecte pas un capteur et n’incrémente pas automatiquement le compteur.

## Prévoir puis concevoir les valeurs

| Point d’observation | Limite | Compteur |
| --- | --- | --- |
| Après les deux initialisations | 3 | 0 |
| Après la mise à jour du compteur | 3 | 1 |

![Initialiser measurement_limit à 3 comme entier constant, initialiser measurement_count à zéro, puis affecter un au compteur. La limite reste à trois.](/diagrams/examples/constant-limit.svg)

<a href="/diagrams/examples/constant-limit.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

Le point noir marque le début ; les rectangles arrondis décrivent les trois actions successives. Le tableau précédent indique les valeurs à observer ; ces observations ne sont pas des instructions supplémentaires. L’**invariant** est ici une propriété qui reste vraie : une fois initialisée, la limite demeure égale à 3.

## Lire le cas valide

Ces instructions seraient placées dans une fonction, un traitement nommé. Elles ne constituent pas à elles seules un programme complet.

<!-- example:constant-valid -->
```cpp
const int measurement_limit = 3;
int measurement_count = 0;
measurement_count = 1;
```

<details class="uml-panel" data-uml="constant-valid">
<summary>Voir la conception UML</summary>

**Quelle donnée reste fixe pendant la mise à jour ?**

![Diagramme de référence : Quelle donnée reste fixe pendant la mise à jour ?](/diagrams/examples/constant-limit.svg)

<a href="/diagrams/examples/constant-limit.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Élément de conception | Correspondance C++ |
| --- | --- |
| Initialiser la limite constante | `const int measurement_limit = 3;` |
| Initialiser le compteur | `int measurement_count = 0;` |
| Modifier seulement le compteur | `measurement_count = 1;` |

Après les initialisations, les valeurs sont 3 et 0. Après la dernière action, elles sont 3 et 1 : la limite reste inchangée.

</details>

La première ligne reprend la forme d’initialisation de CPP-01, avec un mot supplémentaire : **`const`**. Il indique que cet entier ne pourra pas être modifié après son initialisation. La valeur initiale est donnée immédiatement : 3.

Le compteur est un autre entier, déclaré sans `const`. La troisième instruction peut donc remplacer sa valeur par 1. Rendre la limite constante ne rend pas les autres variables constantes.

| Action UML | Instruction | Résultat |
| --- | --- | --- |
| Initialiser la limite constante | `const int measurement_limit = 3;` | Limite égale à 3 |
| Initialiser le compteur | `int measurement_count = 0;` | Limite 3, compteur 0 |
| Modifier le compteur | `measurement_count = 1;` | Limite 3, compteur 1 |

La stabilité concerne cet objet local pendant sa durée de vie. Elle ne signifie pas que tous les futurs lancements du programme doivent utiliser la même configuration.

## Comparer deux modifications

Dans le cas valide, modifier `measurement_count` est autorisé. Essayons maintenant de modifier **la limite constante**, dans un fragment distinct volontairement incorrect :

<!-- example:constant-rejected -->
```cpp
const int measurement_limit = 3;
measurement_limit = 4;
```

<details class="uml-panel" data-uml="constant-rejected">
<summary>Comprendre l’écart avec la conception</summary>

**Pourquoi ce fragment ne réalise-t-il pas la conception attendue ?**

![Diagramme de référence : Pourquoi ce fragment ne réalise-t-il pas la conception attendue ?](/diagrams/examples/constant-limit.svg)

<a href="/diagrams/examples/constant-limit.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Élément de conception | Correspondance C++ |
| --- | --- |
| Initialisation conforme | `const int measurement_limit = 3;` |
| Affectation interdite, absente du modèle valide | `measurement_limit = 4;` |

Conception attendue de référence : le diagramme complet impose de conserver la limite à 3. Ce fragment ne contient pas les actions concernant le compteur. La seconde instruction viole la contrainte const et est refusée à la compilation : aucun parcours exécuté menant à 4 ne doit être déduit de ce diagramme.

</details>

La seconde ligne contredit la contrainte posée par `const`. Le compilateur refuse ce fragment. Il ne faut donc pas lire cet exemple comme « la limite vaut d’abord 3, puis 4 » : il n’existe pas d’exécution valide de ce fragment tel quel.

Voici l’extrait du diagnostic réellement obtenu avec **GCC/g++ 13.3.0**, en mode C++17, en plaçant ces instructions dans une fonction `main` de vérification :

```text
error: assignment of read-only variable 'measurement_limit'
```

Il signifie : « affectation à la variable non modifiable `measurement_limit` ». Le texte exact dépend du compilateur ; l’idée à comprendre est le refus de la modification. Le fragment est placé dans le corps de `main`, comme dans [le premier programme](../programme-minimal/), pour former le programme de vérification.

| Tentative | Compilation | Explication |
| --- | --- | --- |
| Affecter 1 au compteur du cas valide | Acceptée | Cet entier est modifiable |
| Affecter 4 à la limite constante | Refusée | Cet entier a été déclaré `const` |

## Une constante peut contenir une mauvaise valeur

Changeons une seule chose : la valeur initiale. **Le besoin reste fixé à 3 mesures.** Le fragment suivant est une erreur volontaire par rapport à ce besoin :

<!-- example:constant-wrong-value -->
```cpp
const int measurement_limit = 30;
```

<details class="uml-panel" data-uml="constant-wrong">
<summary>Comprendre l’écart avec la conception</summary>

**Où la valeur choisie diverge-t-elle du besoin ?**

![Diagramme de référence : Où la valeur choisie diverge-t-elle du besoin ?](/diagrams/examples/constant-limit.svg)

<a href="/diagrams/examples/constant-limit.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Élément de conception | Correspondance C++ |
| --- | --- |
| Action attendue : initialiser à 3 | `const int measurement_limit = 3;` |
| Instruction réellement montrée : initialiser à 30 | `const int measurement_limit = 30;` |

Conception attendue de référence : seule la première action est comparée ici. Les actions sur le compteur ne figurent pas dans ce fragment. Celui-ci compile, mais produit 30 au lieu des 3 attendus dès l’initialisation ; le diagramme représente le besoin, pas son exécution fautive.

</details>

Cette déclaration est autorisée par le langage. Elle crée un entier constant égal à 30. Pourtant, elle ne respecte pas la première action de notre étude, qui impose 3.

| Vérification | Résultat |
| --- | --- |
| La déclaration est-elle autorisée en C++ ? | Oui |
| La valeur choisie respecte-t-elle le besoin ? | Non : 30 au lieu de 3 |

**`const` protège une valeur contre une modification ; il ne choisit pas la bonne valeur à notre place.** C’est pourquoi nous écrivons le besoin et les résultats attendus avant de vérifier le programme.

## Retrouver la même idée dans le voyant

Dans l’[exemple guidé du voyant](../../exemple-voyant/), le seuil reste à 30 °C tandis que des températures différentes peuvent être fournies au traitement.

| Ici | Dans le voyant |
| --- | --- |
| La limite de 3 mesures reste fixe | Le seuil de 30 °C reste fixe |
| Le compteur peut être modifié | La température fournie peut varier entre les appels |
| La stabilité vient du besoin | La stabilité vient aussi du besoin |

Le contexte change, mais la question reste la même : **quelle donnée doit rester inchangée pendant ce traitement ?** La lecture de toute la fonction du voyant est facultative à ce stade.

## Une nuance à garder pour la suite

Une constante ne reçoit pas obligatoirement une valeur déjà connue lors de la compilation. Imagine un réglage fourni au début d’une session, puis conservé sans modification pendant son traitement : sa valeur peut être établie pendant l’exécution.

L’exemple de code correspondant viendra après les paramètres de fonction. Pour l’instant, retiens que **« non modifiable après initialisation » et « connu à la compilation » sont deux propriétés différentes**. `constexpr`, les pointeurs et les références seront étudiés avec leurs prérequis.

## À retenir sur const

- Choisir une constante exprime une intention du besoin : cette donnée doit rester stable.
- Pour l’entier simple de cette leçon, `const` interdit une affectation ultérieure.
- Le compilateur refuse la modification interdite ; il ne connaît pas la limite voulue par le besoin.
- Une limite constante ne contrôle pas automatiquement les autres données.

La pratique reste dans ton IDE depuis les projets dédiés. Les fragments incorrects ci-dessus sont des comparaisons de lecture explicitement identifiées, pas des solutions à reproduire comme exemples corrects.


**Suite :** [comprendre une expression et calculer une somme](../premieres-expressions/).
