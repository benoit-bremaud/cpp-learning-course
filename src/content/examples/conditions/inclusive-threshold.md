---
id: inclusive-threshold
title: "Seuil — inclure ou exclure exactement 30 °C"
category: deeper
prerequisites: [exemple-voyant]
---

## Comprendre le rôle de l’égalité

**Objectif :** traduire précisément un besoin qui inclut ou exclut une valeur limite. Nous comparons deux règles différentes, sans modifier la règle du voyant existant.

**Prérequis de lecture :** avoir suivi le voyant guidé, notamment la comparaison et les deux retours. La difficulté supplémentaire consiste à choisir une température qui révèle une différence entre deux besoins. Il ne s’agit pas d’apprendre à écrire une nouvelle structure de fonction.

### Distinguer les deux besoins

- **Règle stricte du cours :** allumer lorsque la température dépasse 30 °C.
- **Nouvelle règle inclusive :** allumer lorsque la température atteint ou dépasse 30 °C.

Les températures sont des entiers fournis au programme. Aucun capteur ni matériel n’est piloté. Une seule entrée, exactement 30, suffit ici à distinguer les règles.

### Comparer les deux activités UML

**Règle stricte :**

![Comparer la température à 30 avec supérieur strict et renvoyer vrai ou faux.](/diagrams/examples/07-activity-strict.svg)

<a href="/diagrams/examples/07-activity-strict.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

**Règle inclusive :**

![Comparer la température à 30 avec supérieur ou égal et renvoyer vrai ou faux.](/diagrams/examples/08-activity-inclusive.svg)

<a href="/diagrams/examples/08-activity-inclusive.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

Le déroulé reste identique. La condition du losange change, car le besoin change. Chaque code ci-dessous correspond à son propre diagramme.

### Lire les deux fonctions de seuil

```cpp
bool should_light_indicator(int temperature_celsius) noexcept {
    const int threshold_celsius = 30;
    if (temperature_celsius > threshold_celsius) {
        return true;
    } else {
        return false;
    }
}
```

<details class="uml-panel" data-uml="strict">
<summary>Voir la conception UML</summary>

**Pourquoi exactement 30 est-il exclu ?**

![Diagramme de référence : Pourquoi exactement 30 est-il exclu ?](/diagrams/examples/07-activity-strict.svg)

<a href="/diagrams/examples/07-activity-strict.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Élément de conception | Correspondance C++ |
| --- | --- |
| Établir le seuil | `const int threshold_celsius = 30;` |
| Décision stricte | `temperature_celsius > threshold_celsius` |
| Réponses possibles | `return true; / return false;` |

Avec 30, la garde stricte est fausse et la fonction répond false. Avec 31, elle répond true. Le diagramme correspond uniquement à la fonction stricte ci-dessus.

</details>

```cpp
bool should_light_indicator_inclusive(int temperature_celsius) noexcept {
    const int threshold_celsius = 30;
    if (temperature_celsius >= threshold_celsius) {
        return true;
    } else {
        return false;
    }
}
```

<details class="uml-panel" data-uml="inclusive">
<summary>Voir la conception UML</summary>

**Quelle branche inclut le cas d’égalité ?**

![Diagramme de référence : Quelle branche inclut le cas d’égalité ?](/diagrams/examples/08-activity-inclusive.svg)

<a href="/diagrams/examples/08-activity-inclusive.svg" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>

| Élément de conception | Correspondance C++ |
| --- | --- |
| Établir le seuil | `const int threshold_celsius = 30;` |
| Décision inclusive | `temperature_celsius >= threshold_celsius` |
| Réponses possibles | `return true; / return false;` |

Avec 30, la comparaison inclusive est vraie et mène à return true. Avec 29, la branche false est suivie. Ce diagramme correspond à la fonction inclusive, dont le besoin diffère de celui de la fonction stricte.

</details>

`>` exclut l’égalité ; `>=` l’inclut. Le nom distinct de la seconde fonction permet de comparer les deux contrats sans remplacer la référence du cours. Les seuils et les branches explicites restent identiques aux activités UML.

### Tester la frontière entre les règles

| Température | Stricte `> 30` | Inclusive `>= 30` |
| --- | --- | --- |
| 29 | Faux | Faux |
| 30 | Faux | Vrai |
| 31 | Vrai | Vrai |

**Pourquoi choisir 30 ?** À 29, les deux règles répondent faux ; à 31, elles répondent vrai. Ces deux essais restent utiles, mais ils ne permettent pas de savoir quelle règle est réalisée. À 30, les réponses diffèrent : cette entrée distingue les deux contrats. Un programme pourrait donc utiliser le mauvais opérateur tout en réussissant les essais à 29 et à 31.

**À retenir :** un opérateur n’est pas meilleur dans l’absolu. C’est le besoin qui fixe le choix, et le test à la frontière vérifie qu’il est respecté.


**Pratique :** cette fiche est une lecture locale. Son projet autonome à cloner n’est pas encore publié ; aucun matériel n’est nécessaire pour suivre le raisonnement.
