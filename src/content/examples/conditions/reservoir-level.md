---
id: reservoir-level
title: "Réservoir — signaler un niveau trop bas"
category: other-contexts
prerequisites: [exemple-voyant]
---

## Transposer la décision à un réservoir

**Objectif :** réutiliser une comparaison de seuil dans un autre contexte. Pour le voyant de température, on alertait au-dessus d’un seuil ; ici, on alerte en dessous.

**Prérequis de lecture :** avoir suivi les deux branches du voyant guidé. Nous réutilisons la même forme de fonction ; le changement à comprendre est le sens de la comparaison, avec `<` au lieu de `>`.

Le programme reçoit un niveau entier entre 0 et 100 %. Il doit indiquer si un avertissement serait nécessaire. Le seuil fictif de 20 % sert uniquement à l’exemple ; il ne constitue pas une consigne industrielle.

### Fixer la règle du niveau bas

L’avertissement doit être actif seulement pour un niveau **strictement inférieur à 20 %**. À 20 % exactement, il reste inactif. La valeur fournie doit être comprise entre 0 et 100 ; la mesure physique et le traitement des entrées invalides sont hors de ce contrat.

Cette hypothèse sur l’entrée s’appelle une **précondition** : la partie du programme qui appelle la fonction doit garantir un niveau valide avant de lui transmettre la valeur. Le type `int` accepte aussi des entiers hors de l’intervalle 0 à 100 ; il ne vérifie pas à lui seul un pourcentage.

Par exemple, si l’appelant fournit −5, la comparaison avec 20 serait vraie. Cela ne prouve pas que le réservoir est presque vide : l’entrée ne respecte déjà plus le contrat. La réponse booléenne ne distingue pas un niveau bas valide d’une entrée invalide. Le contrôle de la mesure devra être conçu séparément ; il ne figure pas dans cette fonction.

### Suivre la comparaison du réservoir

![Recevoir un niveau valide, fixer le seuil à 20 et renvoyer vrai si le niveau est strictement inférieur, faux sinon.](/diagrams/examples/06-activity-reservoir.svg)

<a href="/diagrams/examples/06-activity-reservoir.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

Le losange pose une question. La branche `true` termine avec la réponse vraie ; la branche `false` termine avec la réponse fausse. Il s’agit d’une décision, pas d’un pilotage réel de lampe.

### Lire la fonction de niveau bas

```cpp
bool should_warn_low_level(int level_percent) noexcept {
    const int threshold_percent = 20;
    if (level_percent < threshold_percent) {
        return true;
    } else {
        return false;
    }
}
```

<details class="uml-panel" data-uml="reservoir">
<summary>Voir la conception UML</summary>

**Quel chemin suit un niveau égal au seuil ?**

![Diagramme de référence : Quel chemin suit un niveau égal au seuil ?](/diagrams/examples/06-activity-reservoir.svg)

<a href="/diagrams/examples/06-activity-reservoir.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Élément de conception | Correspondance C++ |
| --- | --- |
| Entrée supposée valide | `int level_percent` |
| Établir le seuil | `const int threshold_percent = 20;` |
| Décision du losange | `level_percent < threshold_percent` |
| Deux fins possibles | `return true; / return false;` |

Avec 20, la comparaison 20 < 20 est fausse : on suit la branche false. Avec 19, on suit true. Le domaine 0 à 100 est une précondition ; le type int ne le vérifie pas.

</details>

`level_percent` est l’entrée de l’activité. `threshold_percent` correspond à l’action établissant le seuil. La comparaison `<` correspond au losange. Les deux `return` correspondent aux deux fins possibles. `bool` signifie que la réponse est vraie ou fausse ; `const` garde le seuil inchangé. Comme dans le cours, `noexcept` indique l’absence d’exception sortante.

### Vérifier les limites du réservoir

| Niveau fourni | Avertissement attendu | Pourquoi |
| --- | --- | --- |
| 0 | Vrai | Réservoir vide, sous le seuil |
| 19 | Vrai | Juste sous le seuil |
| 20 | Faux | L’égalité est exclue |
| 21 | Faux | Au-dessus du seuil |
| 100 | Faux | Limite haute du domaine valide |

**Contre-exemple :** utiliser `>` déclencherait l’avertissement lorsque le niveau est haut. La structure du programme resterait valide, mais son comportement ne respecterait plus le besoin.

**À retenir :** le contexte détermine le sens de la comparaison. La méthode reste besoin → UML → code → vérification des résultats.


**Pratique :** cette fiche est une lecture locale. Son projet autonome à cloner n’est pas encore publié ; aucun matériel n’est nécessaire pour suivre le raisonnement.
