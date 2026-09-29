---
title: "Concevoir avant de coder"
description: "Un contrat vérifiable entre exigences, diagrammes UML et code."
---

Pour chaque exercice, l’étude de conception précède l’implémentation. Le diagramme sert à prendre et vérifier des décisions ; il ne sert pas seulement à illustrer du code déjà écrit.

## Partir d’un contrat

Décris les entrées, les sorties, les contraintes et les erreurs attendues. Pour une commande de LED, précise par exemple l’état initial, les événements acceptés et le comportement lorsque deux événements se suivent. Ne choisis pas encore une classe simplement parce que le langage le permet.

## Choisir les vues utiles

| Question | Vue UML adaptée | Ce que le code devra respecter |
| --- | --- | --- |
| Qui est responsable de quoi ? | Composants ou classes | Responsabilités, interfaces, relations et dépendances |
| Qui appelle qui et dans quel ordre ? | Séquence | Messages, ordre, réponses et scénarios d’erreur |
| Quelles décisions suit un traitement ? | Activité | Conditions, branches et terminaison |
| Quels événements changent le comportement ? | États | États, gardes, transitions et actions |

Tous les exercices n’ont pas besoin de tous les diagrammes. Un traitement procédural en C peut demander une activité sans aucune classe. Une machine à états exige de modéliser les transitions, même si son implémentation utilise une simple énumération.

## Relier précisément modèle et code

L’étude comporte une table de correspondance : élément UML, élément C++ ou C, invariant et vérification associée. Les noms, types, signatures, visibilités et relations retenus dans le modèle détaillé doivent correspondre à l’implémentation.

Une flèche d’association ne détermine pas, à elle seule, s’il faut employer un pointeur, une référence ou une valeur. Ce choix appartient à l’étude de durée de vie et de propriété ; il doit être écrit explicitement.

Un diagramme UML ne décrit pas automatiquement chaque instruction. Pour obtenir une correspondance précise, complète les vues structurelles par les contrats et les vues comportementales nécessaires. Aucun générateur de code ni test ne prouve à lui seul cette conformité.

## Valider puis implémenter

1. Relire les exigences et les cas limites.
2. Vérifier les responsabilités et les dépendances.
3. Retirer les abstractions sans besoin concret.
4. Valider ensemble l’étude et sa correspondance avec le code.
5. Cloner le dépôt et implémenter dans l’IDE.
6. Exécuter les tests et comparer le résultat à l’étude.

Si le code révèle un défaut de conception, on corrige et revalide l’étude. On ne conserve pas deux descriptions contradictoires du même système.

## Conserver l’étude avec la pratique

Le dépôt de pratique contiendra la spécification, les sources PlantUML, leur rendu SVG, la table de correspondance, le point de départ et les tests. Une correction éventuelle sera explicitement identifiée.

**État actuel :** cette page définit la méthode. Les études propres aux futurs exercices restent à valider ; elles ne sont pas remplacées par ce texte général.
