---
id: empty-tray
title: "Addition — un plateau peut être vide"
category: other-contexts
prerequisites: [notions/premieres-expressions]
---

## Compter avec un plateau vide

**Objectif :** reconnaître zéro comme une quantité valide dans une somme. **Prérequis :** lire une initialisation et une addition d’entiers.

Sur l’établi, le plateau gauche est vide et le droit contient 3 composants. Nous connaissons les deux quantités : zéro n’indique pas une donnée manquante. Le total attendu est **3 composants**.

Comme dans la leçon, nous choisissons de petits entiers entre 0 et 10 par plateau. Le seul changement par rapport à l’exemple 2 + 3 est le contenu du plateau gauche. Aucun contrôle de saisie ni capteur n’est représenté.

## Concevoir la somme

Initialiser les deux quantités à 0 et 3, calculer leur somme, puis créer le total avec le résultat 3. Les quantités des plateaux restent inchangées.

![Initialiser les quantités gauche et droite à zéro et trois, calculer leur somme et initialiser le total à trois.](/diagrams/examples/expression-empty-tray.svg)

<a href="/diagrams/examples/expression-empty-tray.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

Le point noir ouvre l’activité, les actions se lisent vers le bas et le symbole final termine le fragment. La séparation entre calcul et stockage aide à lire le raisonnement ; elle ne décrit pas le nombre d’instructions du processeur.

## Lire le code

Ces trois instructions forment un extrait indépendant à placer dans le corps de `main`.

<!-- example:expression-empty-tray -->
```cpp
int left_tray_count = 0;
int right_tray_count = 3;
int component_count = left_tray_count + right_tray_count;
```

<details class="uml-panel" data-uml="expression-empty-tray">
<summary>Voir la conception UML</summary>

![Initialiser les quantités gauche et droite à zéro et trois, calculer leur somme et initialiser le total à trois.](/diagrams/examples/expression-empty-tray.svg)

<a href="/diagrams/examples/expression-empty-tray.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Action UML | Correspondance C++ |
| --- | --- |
| Initialiser les quantités | Les deux premières déclarations donnent `0` et `3`. |
| Calculer la somme | `left_tray_count + right_tray_count` produit `3`. |
| Initialiser le total | La dernière déclaration crée `component_count` avec `3`. |

Les actions « calculer » et « initialiser » ou « affecter » détaillent le raisonnement. Elles ne correspondent pas nécessairement à des instructions C++ séparées. Aucun stockage intermédiaire nommé n’est ajouté au code.

</details>

## Observer les valeurs

| Après l’instruction | Quantité gauche | Quantité droite | Total |
| --- | --- | --- | --- |
| Première déclaration | 0 | Pas encore créée | Pas encore créé |
| Deuxième déclaration | 0 | 3 | Pas encore créé |
| Déclaration du total | 0 | 3 | 3 |

Ajouter zéro n’augmente pas la quantité : **0 + 3 donne 3**. Le même opérateur suffit ; le plateau vide n’impose pas une autre formule.

**À retenir :** une quantité connue égale à zéro peut participer normalement à un calcul. Cela ne justifie pas de remplacer une quantité inconnue par zéro. Le tableau est une trace explicative : cet extrait ne produit aucun affichage.

**Pratique :** le projet autonome de cet exemple n’est pas encore publié. La pratique restera dans un dépôt dédié à cloner dans ton IDE.
