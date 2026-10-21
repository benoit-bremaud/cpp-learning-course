---
id: independent-copy
title: "Copie — modifier l’original sans changer la copie"
category: deeper
prerequisites: [notions/cpp-01]
---

## Comprendre une copie d’entier

**Objectif :** comprendre qu’une copie de valeur entre deux entiers ordinaires n’est pas une liaison permanente. La difficulté supplémentaire est de suivre deux variables au lieu d’une.

**Prérequis de lecture :** reconnaître l’initialisation et l’affectation dans CPP-01. Aucune connaissance des références ou des pointeurs n’est nécessaire.

Un atelier compte 12 composants. Nous gardons une photographie du total avant de mettre à jour le stock. `component_count` représente le total courant ; `snapshot_count` conserve le total au moment de la copie.

### Prévoir les valeurs des deux variables

Après la copie, les deux variables valent 12. Après l’affectation de 11 au stock courant, seule `component_count` change. La photographie reste à 12.

### Suivre l’ordre de la copie en UML

![Initialiser component_count à 12, copier sa valeur dans snapshot_count, puis affecter 11 au seul component_count.](/diagrams/examples/05-activity-copy.svg)

<a href="/diagrams/examples/05-activity-copy.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

Les actions se suivent de haut en bas. La copie intervient avant la modification. Cet ordre explique le résultat final ; le diagramme ne représente pas un lien qui resterait actif entre les deux variables.

### Lire les trois instructions de copie

```cpp
int component_count = 12;
int snapshot_count = component_count;
component_count = 11;
```

<details class="uml-panel" data-uml="copy">
<summary>Voir la conception UML</summary>

**À quel moment la valeur est-elle copiée ?**

![Diagramme de référence : À quel moment la valeur est-elle copiée ?](/diagrams/examples/05-activity-copy.svg)

<a href="/diagrams/examples/05-activity-copy.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Élément de conception | Correspondance C++ |
| --- | --- |
| Créer le total courant | `int component_count = 12;` |
| Copier sa valeur actuelle | `int snapshot_count = component_count;` |
| Modifier le total courant | `component_count = 11;` |

Après la deuxième action, les deux entiers valent 12. La dernière action ne modifie que component_count : snapshot_count reste à 12.

</details>

Lis la deuxième ligne en deux temps : à droite du signe `=`, retrouver la valeur 12 ; à gauche, créer `snapshot_count` avec cette valeur. Aucun lien permanent n’est enregistré. Dans la troisième ligne, la cible de l’affectation est uniquement `component_count` : `snapshot_count` conserve donc 12.

### Vérifier chaque étape de la copie

| Après l’instruction | Stock courant | Copie |
| --- | --- | --- |
| Initialiser le stock | 12 | Pas encore créée |
| Initialiser la copie | 12 | 12 |
| Modifier le stock | 11 | 12 |

**Erreur fréquente :** penser que la copie deviendra automatiquement 11 parce que sa déclaration mentionne le nom de l’autre variable. La déclaration a copié une valeur à un instant précis.

**À retenir :** ces deux variables entières possèdent des valeurs indépendantes. Cette explication ne décrit pas les références ni les pointeurs, qui seront étudiés séparément.


**Pratique :** cette fiche est une lecture locale. Son projet autonome à cloner n’est pas encore publié ; aucun matériel n’est nécessaire pour suivre le raisonnement.
