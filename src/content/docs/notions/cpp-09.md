---
title: "CPP-09 - Exprimer une valeur constante"
description: "Observer une limite constante et distinguer rejet de compilation et valeur initiale incorrecte."
---

**Objectif :** expliquer et observer ce que `const` impose à un entier. **Prérequis :** [CPP-01](../cpp-01/). **État :** programmes de lecture disponibles ; exercice autonome à venir.

## Identifier ce qui doit rester stable

Le besoin fixe une limite fictive de **3 mesures** pour une session. Un compteur indépendant vaut d’abord **0**, puis reçoit le total fourni **1**. Nous voulons observer ces deux paires : **(3, 0)**, puis **(3, 1)**.

La limite reste fixe pendant la vie de cet objet local ; le compteur peut changer. Déclarer une limite ne réserve pas de mémoire pour les mesures et ne vérifie pas automatiquement le compteur. Ces programmes ne lisent aucun capteur et ne font aucun calcul d’incrément.

Pour un entier local simple, `const` interdit de modifier sa valeur après son initialisation. Nous devons donc lui donner sa valeur dès sa création. Le compilateur vérifie la contrainte de modification ; il ne choisit pas la bonne valeur pour notre besoin.

## Observer la limite et le compteur

![Initialiser la limite à trois et le compteur à zéro, observer la paire, affecter un au compteur, observer à nouveau, puis renvoyer zéro.](/diagrams/examples/constant-limit.svg)

<a href="/diagrams/examples/constant-limit.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand - nouvel onglet</a>

Le diagramme se lit de haut en bas. Chacune des deux actions d’observation regroupe quatre instructions : écrire la limite et son saut de ligne, puis le compteur et son saut de ligne. Lire une variable pour l’afficher ne la modifie pas.

Voici un programme complet pour ordinateur, avec la structure et les affichages déjà étudiés. Prédis les quatre lignes, puis compile-le avec la configuration de TOOL-01 utilisée dans CPP-01.

<!-- example:program-constant-stable -->
```cpp wrap
#include <iostream>

int main() {
    const int measurement_limit = 3;
    int measurement_count = 0;
    std::cout << measurement_limit;
    std::cout << "\n";
    std::cout << measurement_count;
    std::cout << "\n";
    measurement_count = 1;
    std::cout << measurement_limit;
    std::cout << "\n";
    std::cout << measurement_count;
    std::cout << "\n";
    return 0;
}
```

<details class="uml-panel" data-uml="constant-valid">
<summary>Voir la conception UML</summary>

**Quelle donnée reste fixe entre les deux observations ?**

![Quelle donnée reste fixe entre les deux observations ?](/diagrams/examples/constant-limit.svg)

<a href="/diagrams/examples/constant-limit.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand - nouvel onglet</a>

<table class="observable-values">
<thead><tr><th>Action ou référence UML</th><th>Instructions C++</th><th>Observation</th></tr></thead>
<tbody>
<tr><td>Initialiser la limite constante</td><td><code>const int measurement_limit = 3;</code></td><td>La limite vaut 3.</td></tr>
<tr><td>Initialiser le compteur</td><td><code>int measurement_count = 0;</code></td><td>Le compteur vaut 0.</td></tr>
<tr><td>Écrire la limite puis le compteur, chacun sur sa ligne</td><td><code>std::cout &lt;&lt; measurement_limit;</code> puis <code>std::cout &lt;&lt; &quot;\n&quot;;</code> puis <code>std::cout &lt;&lt; measurement_count;</code> puis <code>std::cout &lt;&lt; &quot;\n&quot;;</code></td><td>Deux lignes : 3, puis 0.</td></tr>
<tr><td>Affecter le total fourni au compteur</td><td><code>measurement_count = 1;</code></td><td>La limite reste inchangée ; le compteur vaut 1.</td></tr>
<tr><td>Écrire à nouveau la paire</td><td><code>std::cout &lt;&lt; measurement_limit;</code> puis <code>std::cout &lt;&lt; &quot;\n&quot;;</code> puis <code>std::cout &lt;&lt; measurement_count;</code> puis <code>std::cout &lt;&lt; &quot;\n&quot;;</code></td><td>Deux lignes supplémentaires : 3, puis 1.</td></tr>
<tr><td>Renvoyer le statut de réussite</td><td><code>return 0;</code></td><td>Aucune écriture supplémentaire.</td></tr>
</tbody>
</table>

Les six actions couvrent les douze instructions du corps de `main`. L’inclusion, la signature et les accolades sont la structure du programme ; les nœuds initial et final ne sont pas des instructions supplémentaires.

</details>

**Sortie attendue :**

```text
3
0
3
1
```

L’ordre est toujours limite puis compteur : les deux premières lignes montrent (3, 0), les deux suivantes (3, 1). Chaque `std::cout << "\n";` termine une ligne ; les retours à la ligne du fichier source ne suffisent pas. `return 0;` renvoie un statut de réussite sans écrire une cinquième ligne.

## Suivre ce qui change

`const int measurement_limit = 3;` crée et initialise l’entier constant. `int measurement_count = 0;` crée un autre entier, modifiable. L’affectation `measurement_count = 1;` remplace seulement sa valeur par le total fourni ; elle ne calcule pas « le précédent plus un » et n’attend pas une mesure.

Dans cette trace, `\n` représente un saut de ligne et « inchangée » signifie qu’aucun texte n’est ajouté.

<table class="observable-values">
<thead><tr><th>Instructions parcourues</th><th>Limite</th><th>Compteur</th><th>Sortie accumulée</th></tr></thead>
<tbody>
<tr><td><code>const int measurement_limit = 3;</code></td><td>3</td><td>Pas encore créé</td><td>Vide</td></tr>
<tr><td><code>int measurement_count = 0;</code></td><td>3</td><td>0</td><td>Vide</td></tr>
<tr><td>Quatre écritures de la première paire</td><td>3</td><td>0</td><td><code>3\n0\n</code></td></tr>
<tr><td><code>measurement_count = 1;</code></td><td>3</td><td>1</td><td><code>3\n0\n</code> (inchangée)</td></tr>
<tr><td>Quatre écritures de la seconde paire</td><td>3</td><td>1</td><td><code>3\n0\n3\n1\n</code></td></tr>
<tr><td><code>return 0;</code></td><td>3</td><td>1</td><td>Inchangée ; statut 0</td></tr>
</tbody>
</table>

La limite garde la valeur 3 au cours de la mise à jour : c’est ici un **invariant**. Afficher `measurement_limit` lit sa valeur courante ; ce nom n’est pas un texte entre guillemets.

## Essayer une modification interdite

Prédis maintenant ce qui se passe à la compilation. Ce deuxième fichier est complet, mais **volontairement incorrect** : il tente d’affecter 4 à l’entier constant.

<!-- example:program-constant-rejected -->
```cpp wrap
#include <iostream>

int main() {
    const int measurement_limit = 3;
    measurement_limit = 4;
    std::cout << measurement_limit;
    std::cout << "\n";
    return 0;
}
```

<details class="uml-panel" data-uml="constant-rejected">
<summary>Comprendre l’écart avec la conception</summary>

**Pourquoi cette source ne peut-elle pas exécuter le modèle attendu ?**

![Pourquoi cette source ne peut-elle pas exécuter le modèle attendu ?](/diagrams/examples/constant-limit.svg)

<a href="/diagrams/examples/constant-limit.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand - nouvel onglet</a>

<table class="observable-values">
<thead><tr><th>Action ou référence UML</th><th>Instructions C++</th><th>Observation</th></tr></thead>
<tbody>
<tr><td>Première action de référence</td><td><code>const int measurement_limit = 3;</code></td><td>Initialisation conforme à la limite attendue.</td></tr>
<tr><td>Aucune action valide pour cette tentative</td><td><code>measurement_limit = 4;</code></td><td>Affectation interdite : la compilation échoue.</td></tr>
<tr><td>Écriture présente dans le fichier, non exécutée</td><td><code>std::cout &lt;&lt; measurement_limit;</code></td><td>Aucun affichage de 4 ne peut en être déduit.</td></tr>
<tr><td>Saut de ligne présent, non exécuté</td><td><code>std::cout &lt;&lt; &quot;\n&quot;;</code></td><td>Aucune sortie de ce programme rejeté.</td></tr>
<tr><td>Retour présent, non exécuté</td><td><code>return 0;</code></td><td>Aucun statut d’exécution réussi à annoncer.</td></tr>
</tbody>
</table>

**Conception attendue de référence :** le diagramme conserve la limite à 3. Il ne décrit pas une exécution de cette source invalide. Les cinq instructions sont comparées ici ; cette source omet entièrement le compteur et ses actions. Une erreur de compilation n’est pas un statut renvoyé par `main`.

</details>

Le compilateur refuse la modification. Voici un extrait réel du diagnostic de **GCC 15.2.0**, avec le nom de fichier neutralisé :

```text
constant-rejected.cpp: In function 'int main()':
constant-rejected.cpp:5:23: error: assignment of read-only variable 'measurement_limit'
```

Le texte exact dépend du compilateur et de sa version ; l’observation à retenir est le **rejet de compilation**. N’exécute pas un ancien fichier exécutable après cet échec : il ne représenterait pas cette source. Il n’y a ni sortie attendue ni statut d’exécution à lui attribuer.

Dans le premier programme, affecter 1 au compteur est autorisé parce que cet objet n’est pas déclaré `const`. Dans celui-ci, affecter 4 à la limite est interdit parce que cet autre objet l’est.

## Une constante peut porter une mauvaise valeur

Le besoin reste **3**. Ce troisième programme ne change que la valeur initiale de la limite : **30**. Prédis sa sortie et distingue « accepté par C++ » de « conforme au besoin ».

![Comportement réel erroné : initialiser la limite à trente, observer les deux paires puis renvoyer zéro.](/diagrams/examples/constant-wrong-limit.svg)

<a href="/diagrams/examples/constant-wrong-limit.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand - nouvel onglet</a>

<!-- example:program-constant-wrong -->
```cpp wrap
#include <iostream>

int main() {
    const int measurement_limit = 30;
    int measurement_count = 0;
    std::cout << measurement_limit;
    std::cout << "\n";
    std::cout << measurement_count;
    std::cout << "\n";
    measurement_count = 1;
    std::cout << measurement_limit;
    std::cout << "\n";
    std::cout << measurement_count;
    std::cout << "\n";
    return 0;
}
```

<details class="uml-panel" data-uml="constant-wrong">
<summary>Comprendre l’écart avec la conception</summary>

**Où la valeur réelle diverge-t-elle du besoin fixé à trois ?**

![Où la valeur réelle diverge-t-elle du besoin fixé à trois ?](/diagrams/examples/constant-wrong-limit.svg)

<a href="/diagrams/examples/constant-wrong-limit.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand - nouvel onglet</a>

<table class="observable-values">
<thead><tr><th>Action ou référence UML</th><th>Instructions C++</th><th>Observation</th></tr></thead>
<tbody>
<tr><td>Initialiser la limite constante</td><td><code>const int measurement_limit = 30;</code></td><td>La limite vaut 30.</td></tr>
<tr><td>Initialiser le compteur</td><td><code>int measurement_count = 0;</code></td><td>Le compteur vaut 0.</td></tr>
<tr><td>Écrire la limite puis le compteur, chacun sur sa ligne</td><td><code>std::cout &lt;&lt; measurement_limit;</code> puis <code>std::cout &lt;&lt; &quot;\n&quot;;</code> puis <code>std::cout &lt;&lt; measurement_count;</code> puis <code>std::cout &lt;&lt; &quot;\n&quot;;</code></td><td>Deux lignes : 30, puis 0.</td></tr>
<tr><td>Affecter le total fourni au compteur</td><td><code>measurement_count = 1;</code></td><td>La limite reste inchangée ; le compteur vaut 1.</td></tr>
<tr><td>Écrire à nouveau la paire</td><td><code>std::cout &lt;&lt; measurement_limit;</code> puis <code>std::cout &lt;&lt; &quot;\n&quot;;</code> puis <code>std::cout &lt;&lt; measurement_count;</code> puis <code>std::cout &lt;&lt; &quot;\n&quot;;</code></td><td>Deux lignes supplémentaires : 30, puis 1.</td></tr>
<tr><td>Renvoyer le statut de réussite</td><td><code>return 0;</code></td><td>Aucune écriture supplémentaire.</td></tr>
</tbody>
</table>

Ce modèle décrit le comportement réel erroné : six actions, douze instructions. La divergence apparaît dès l’initialisation à 30 ; la limite reste ensuite constante à cette mauvaise valeur. Le besoin de référence demeure 3. Il ne s’agit pas d’une modification ultérieure de la constante.

</details>

**Sortie réelle de cette variante :**

```text
30
0
30
1
```

La compilation et l’exécution réussissent ; le statut vaut 0. Pourtant, la sortie demandée était `3\n0\n3\n1\n`. La limite vaut 30 lors des deux observations. `const` empêche sa modification ultérieure, mais ne garantit pas que l’initialisation satisfait le besoin.

## Une valeur connue pendant l’exécution

Imagine un réglage fourni au démarrage d’une session, puis conservé pour toute cette session. Conceptuellement, une valeur constante peut ainsi être connue pendant l’exécution : `const` ne signifie pas nécessairement « valeur connue à la compilation ».

Le code d’une telle acquisition et le calcul à la compilation avec `constexpr` viendront séparément. Aucun appel à une API d’entrée n’est nécessaire pour cette introduction.

## Lien avec l’embarqué

Le choix dépend du besoin : une limite réglable pendant le fonctionnement ne porte pas le même contrat qu’une limite fixe pour une session. Notre compteur représente un total fourni, sans acquisition ni contrôle de capacité.

En lecture facultative, le [voyant guidé](../../exemple-voyant/) utilise un seuil stable de 30 et une température fournie qui peut varier d’un cas à l’autre. Le contexte change, mais la distinction « seuil fixe, donnée variable » reste la même. Comprendre ses conditions et sa fonction n’est pas nécessaire pour terminer cette leçon.

**À retenir :** `const` interdit de modifier cet entier après son initialisation. Un programme peut être rejeté pour une affectation interdite, ou réussir avec une valeur constante pourtant incorrecte pour le besoin. Sortie affichée, statut d’exécution et conformité au besoin sont trois observations distinctes.

## Plus tard

Les références et les pointeurs nécessiteront de distinguer un objet constant d’un accès qui interdit certaines modifications. Ils ne sont pas des prérequis ici.

Tu peux essayer les trois fichiers dans ton IDE : les premier et troisième s’exécutent, le deuxième doit échouer à la compilation. L’exercice autonome dédié n’est pas encore publié dans le dépôt de pratique.

**Suite :** [calculer une nouvelle valeur](../premiers-calculs/).
