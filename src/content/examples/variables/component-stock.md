---
id: component-stock
title: "Stock — partir de 12, puis enregistrer 11"
category: other-contexts
prerequisites: [notions/cpp-01]
---

## Comprendre la valeur de départ

**Objectif :** distinguer initialisation et affectation. Tu n’as pas besoin de savoir écrire une fonction seul : nous lisons deux instructions qui seraient placées dans une fonction.

Un atelier possède 12 composants. Après une sortie de stock, on souhaite enregistrer le nouveau total connu : 11. Contrairement au compteur de mesures du cours, la valeur de départ n’est pas zéro. Le principe reste le même : choisir la valeur initiale selon le besoin.

### Décrire le changement attendu

La variable `component_count` doit contenir 12 après sa création, puis 11 après la mise à jour. Le programme ne détecte pas physiquement le retrait d’un composant ; nous lui fournissons directement le nouveau total.

### Suivre les deux actions en UML

![Initialiser component_count à 12, puis lui affecter 11 et terminer.](/diagrams/examples/04-activity-stock.svg)

<a href="/diagrams/examples/04-activity-stock.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

Le point noir marque le début. Les deux rectangles arrondis sont des actions, exécutées de haut en bas. Le symbole final termine l’activité. Le tableau sous le code détaille les valeurs observées à chaque étape.

### Lire les instructions du stock

```cpp
int component_count = 12;
component_count = 11;
```

<details class="uml-panel" data-uml="stock">
<summary>Voir la conception UML</summary>

**Comment remplacer un total connu ?**

![Diagramme de référence : Comment remplacer un total connu ?](/diagrams/examples/04-activity-stock.svg)

<a href="/diagrams/examples/04-activity-stock.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Élément de conception | Correspondance C++ |
| --- | --- |
| Initialisation du stock | `int component_count = 12;` |
| Remplacement du stock | `component_count = 11;` |

Les actions donnent successivement les valeurs 12 puis 11. L’affectation remplace le total ; elle ne calcule pas une soustraction.

</details>

`int` introduit ici une variable entière. La première ligne déclare cette variable et l’initialise à 12 : elle correspond à la première action UML. La seconde ligne donne une nouvelle valeur à la variable existante : elle correspond à l’affectation du diagramme.

Le signe `=` signifie ici « recevoir cette valeur ». Il ne pose pas une question d’égalité. La seconde instruction ne calcule pas `12 - 1` : elle remplace la valeur par 11.

### Observer le résultat du stock

| Moment | Valeur de `component_count` |
| --- | --- |
| Après l’initialisation | 12 |
| Après l’affectation | 11 |

**Repère de lecture :** un bloc regroupe des instructions entre des accolades. Les deux lignes ci-dessus seraient placées dans un même bloc de fonction.

**Contre-exemple :** écrire à nouveau `int component_count = 11;` dans le même bloc chercherait à déclarer une seconde fois le même nom. Pour modifier cette variable, on utilise son nom sans répéter son type.

**À retenir :** initialiser crée la valeur de départ ; affecter remplace ensuite la valeur. Zéro n’est pas une valeur initiale universelle.


**Pratique :** cette fiche est une lecture locale. Son projet autonome à cloner n’est pas encore publié ; aucun matériel n’est nécessaire pour suivre le raisonnement.
