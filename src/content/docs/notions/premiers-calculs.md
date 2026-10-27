---
title: "Calculer une nouvelle valeur"
description: "Lire la valeur courante d’un entier, lui ajouter un, puis stocker le résultat."
---

**Objectif :** distinguer un calcul à partir de la valeur courante d’un remplacement par un total fourni. **Prérequis :** [CPP-01](../cpp-01/). **État :** programmes de lecture disponibles ; exercice autonome dédié à venir.

## Partir de ce qui est déjà connu

Dans CPP-01, l’affectation remplaçait le compteur par un total connu. Ici, le compteur vaut **2** et le besoin est différent : **calculer un de plus que sa valeur courante**. Le résultat demandé est donc **3**.

Le seul nouvel opérateur de cette leçon est `+`. Il calcule ici la somme de deux entiers : la valeur lue dans le compteur et le nombre `1`. Le programme n’attend aucune mesure et ne réagit à aucun événement matériel.

## Observer une mise à jour calculée

Prédis les deux lignes affichées : la valeur avant la mise à jour, puis celle après.

![Initialiser le compteur à deux, l’observer, lire sa valeur et ajouter un puis stocker le résultat, l’observer à nouveau et renvoyer zéro.](/diagrams/examples/program-arithmetic-update.svg)

<a href="/diagrams/examples/program-arithmetic-update.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand - nouvel onglet</a>

Le diagramme se lit de haut en bas. Chaque observation regroupe deux écritures : la valeur du compteur, puis son saut de ligne. L’action centrale lit, calcule et stocke ; elle sera réalisée par une seule instruction.

Voici un fichier C++ complet pour ordinateur. Compile-le avec la configuration de [TOOL-01](../tool-01/) déjà utilisée dans CPP-01.

<!-- example:program-arithmetic-update -->
```cpp wrap
#include <iostream>

int main() {
    int measurement_count = 2;
    std::cout << measurement_count;
    std::cout << "\n";
    measurement_count = measurement_count + 1;
    std::cout << measurement_count;
    std::cout << "\n";
    return 0;
}
```

<details class="uml-panel" data-uml="program-arithmetic-update">
<summary>Voir la conception UML</summary>

**Comment la nouvelle valeur dépend-elle de la valeur déjà stockée ?**

![Comment la nouvelle valeur dépend-elle de la valeur déjà stockée ?](/diagrams/examples/program-arithmetic-update.svg)

<a href="/diagrams/examples/program-arithmetic-update.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand - nouvel onglet</a>

<table class="observable-values">
<thead><tr><th>Action UML</th><th>Instructions C++</th><th>Observation</th></tr></thead>
<tbody>
<tr><td>Initialiser le compteur</td><td><code>int measurement_count = 2;</code></td><td>Le compteur vaut 2.</td></tr>
<tr><td>Observer la valeur initiale</td><td><code>std::cout &lt;&lt; measurement_count;</code> puis <code>std::cout &lt;&lt; &quot;\n&quot;;</code></td><td>Première ligne : 2.</td></tr>
<tr><td>Calculer puis remplacer la valeur</td><td><code>measurement_count = measurement_count + 1;</code></td><td>La valeur courante devient 3. Aucune écriture ici.</td></tr>
<tr><td>Observer la valeur après affectation</td><td><code>std::cout &lt;&lt; measurement_count;</code> puis <code>std::cout &lt;&lt; &quot;\n&quot;;</code></td><td>Seconde ligne : 3.</td></tr>
<tr><td>Renvoyer le statut de réussite</td><td><code>return 0;</code></td><td>Pas de ligne supplémentaire.</td></tr>
</tbody>
</table>

L’action de mise à jour lit 2, calcule 3 puis stocke 3. Elle correspond à une seule instruction C++, pas à trois instructions séparées. Les cinq actions couvrent les sept instructions du corps de `main`. L’inclusion, la signature, les accolades et les nœuds initial/final sont structurels.

</details>

**Sortie attendue :**

```text
2
3
```

Les deux lectures par `std::cout` ne changent pas le compteur. Chaque `"\n"` termine une ligne. `return 0;` renvoie le statut de réussite sans écrire une troisième ligne.

## Lire, calculer, puis stocker

Dans `measurement_count = measurement_count + 1;`, le même nom apparaît deux fois, avec deux rôles :

1. À droite, le programme lit la valeur courante **2** et calcule **2 + 1**, soit **3**.
2. L’affectation remplace ensuite la valeur de l’objet désigné à gauche par ce résultat **3**.

Le symbole `=` exprime ici une affectation, pas une équation algébrique à résoudre. Le programme ne garde pas une formule attachée au compteur. Il effectue ce calcul une fois, lorsqu’il rencontre cette instruction.

La trace suivante distingue la valeur stockée du texte déjà écrit. Dans sa dernière colonne, `\n` représente un saut de ligne.

<table class="observable-values">
<thead><tr><th>Instruction parcourue</th><th>Compteur après l’instruction</th><th>Sortie accumulée</th></tr></thead>
<tbody>
<tr><td><code>int measurement_count = 2;</code></td><td>2</td><td>Vide</td></tr>
<tr><td><code>std::cout &lt;&lt; measurement_count;</code></td><td>2</td><td><code>2</code></td></tr>
<tr><td><code>std::cout &lt;&lt; &quot;\n&quot;;</code></td><td>2</td><td><code>2\n</code></td></tr>
<tr><td><code>measurement_count = measurement_count + 1;</code></td><td>3</td><td><code>2\n</code> (inchangée)</td></tr>
<tr><td><code>std::cout &lt;&lt; measurement_count;</code></td><td>3</td><td><code>2\n3</code></td></tr>
<tr><td><code>std::cout &lt;&lt; &quot;\n&quot;;</code></td><td>3</td><td><code>2\n3\n</code></td></tr>
<tr><td><code>return 0;</code></td><td>3</td><td>Inchangée ; statut 0</td></tr>
</tbody>
</table>

## Comparer avec un remplacement fourni

Le besoin reste « ajouter un à la valeur courante ». Dans le fichier suivant, une seule instruction change : nous affectons directement le total fourni **1**. Prédis sa sortie avant de l’exécuter.

![Comportement réel de la variante : initialiser le compteur à deux, l’observer, lui affecter un, l’observer puis renvoyer zéro.](/diagrams/examples/program-literal-replacement.svg)

<a href="/diagrams/examples/program-literal-replacement.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand - nouvel onglet</a>

<!-- example:program-literal-replacement -->
```cpp wrap
#include <iostream>

int main() {
    int measurement_count = 2;
    std::cout << measurement_count;
    std::cout << "\n";
    measurement_count = 1;
    std::cout << measurement_count;
    std::cout << "\n";
    return 0;
}
```

<details class="uml-panel" data-uml="program-literal-replacement">
<summary>Comprendre l’écart avec la conception</summary>

**Quelle information le remplacement littéral n’utilise-t-il pas ?**

![Quelle information le remplacement littéral n’utilise-t-il pas ?](/diagrams/examples/program-literal-replacement.svg)

<a href="/diagrams/examples/program-literal-replacement.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand - nouvel onglet</a>

<table class="observable-values">
<thead><tr><th>Action UML</th><th>Instructions C++</th><th>Observation</th></tr></thead>
<tbody>
<tr><td>Initialiser le compteur</td><td><code>int measurement_count = 2;</code></td><td>Le compteur vaut 2.</td></tr>
<tr><td>Observer la valeur initiale</td><td><code>std::cout &lt;&lt; measurement_count;</code> puis <code>std::cout &lt;&lt; &quot;\n&quot;;</code></td><td>Première ligne : 2.</td></tr>
<tr><td>Remplacer par le total fourni</td><td><code>measurement_count = 1;</code></td><td>La valeur courante devient 1. Aucune écriture ici.</td></tr>
<tr><td>Observer la valeur après affectation</td><td><code>std::cout &lt;&lt; measurement_count;</code> puis <code>std::cout &lt;&lt; &quot;\n&quot;;</code></td><td>Seconde ligne : 1.</td></tr>
<tr><td>Renvoyer le statut de réussite</td><td><code>return 0;</code></td><td>Pas de ligne supplémentaire.</td></tr>
</tbody>
</table>

Ce diagramme décrit le comportement réel de cette variante : remplacer 2 par le total fourni 1. Le besoin « ajouter un à la valeur courante » demandait 3. Cette source est autorisée par C++ ; elle ne réalise pas le calcul demandé. Les cinq actions couvrent les sept instructions du corps de `main`. L’inclusion, la signature, les accolades et les nœuds initial/final sont structurels.

</details>

**Sortie réelle de cette variante :**

```text
2
1
```

La compilation et l’exécution réussissent, avec un statut de 0. Pourtant, le résultat demandé après la mise à jour était **3**, pas **1**. Cette affectation ne se sert pas de l’ancienne valeur pour calculer la nouvelle : elle la remplace par le nombre fourni.

## Choisir un exemple qui montre la différence

Partir de zéro masquerait la distinction : les deux instructions donneraient alors 1. Avec le départ à 2, leurs résultats deviennent différents.

<table class="observable-values">
<thead><tr><th>Valeur avant l’affectation</th><th>Après le calcul « valeur courante + 1 »</th><th>Après le remplacement par 1</th></tr></thead>
<tbody>
<tr><td>0</td><td>1</td><td>1</td></tr>
<tr><td>2</td><td>3</td><td>1</td></tr>
</tbody>
</table>

Un autre piège consiste à remplacer le calcul par `measurement_count = 3;`. Pour le seul départ à 2, les affichages seraient encore 2 puis 3. Mais cette instruction n’exprime plus la dépendance à la valeur courante. Une sortie correcte sur un seul cas ne suffit donc pas à prouver que le calcul demandé est présent.

## Garder des limites claires

Ces exemples utilisent de petits entiers initialisés. Le type `int` ne représente pas des nombres sans limite ; ses valeurs représentables et les dépassements seront étudiés séparément. Nous ne provoquons aucun dépassement ici et ne supposons pas une taille universelle de 32 bits.

Une exécution de notre premier programme contient exactement une mise à jour calculée. Afficher le compteur ou laisser du temps s’écouler n’en déclenche pas une autre. Les entrées, les boucles, les autres opérateurs et les écritures abrégées telles que `+=` ou `++` viendront dans leurs leçons dédiées.

## Vérifier ce que tu as compris

- Quelle valeur le nom désigne-t-il à droite de l’affectation avant que le résultat soit stocké ?
- À quel moment le compteur passe-t-il de 2 à 3 ? Cette instruction écrit-elle du texte ?
- Pourquoi le remplacement par 1 est-il autorisé par C++ tout en manquant le besoin ?
- Pourquoi partir de zéro rend-il ce contraste moins visible ?
- Pourquoi affecter directement 3 peut-il réussir le premier essai sans exprimer le bon calcul ?

**À retenir :** une expression calcule une valeur au moment où elle est évaluée ; l’affectation stocke ensuite son résultat. Une lecture pour affichage ne remplace pas la valeur stockée.

Tu peux essayer les deux fichiers complets dans ton IDE. Aucun exercice autonome dédié à cette mise à jour n’est encore publié dans le dépôt de pratique. Cette introduction ne remplace pas le futur module CPP-02 sur la représentation des entiers.
