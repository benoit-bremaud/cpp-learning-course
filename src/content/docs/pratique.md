---
title: "Pratiquer dans son IDE"
description: "Un dépôt de pratique, des modules indépendants et une étude UML par exercice."
---

Le cours et la pratique disposent de deux dépôts séparés :

- [cpp-learning-course](https://github.com/benoit-bremaud/cpp-learning-course) contient le site.
- [cpp-learning](https://github.com/benoit-bremaud/cpp-learning) est le dépôt de pratique à cloner.

## Cloner une fois

Dans un terminal, choisis un répertoire de travail puis utilise :

```sh
git clone https://github.com/benoit-bremaud/cpp-learning.git
cd cpp-learning
```

Ouvre ensuite ce dossier dans VS Code ou un autre IDE. Tu pourras revenir dans un module sans cloner un nouveau dépôt à chaque séance.

:::note[Disponibilité]
Le dépôt distant contient actuellement son amorce. Les études et exercices ne sont pas encore publiés. Le clonage fonctionne, mais il ne fournit pas encore de programme à compiler.
:::

## Retrouver un exercice

Chaque futur module aura un dossier identifiable par son code, par exemple `CPP-01`. Son document d’entrée précisera l’objectif, les prérequis, l’étude UML validée, les outils nécessaires et les commandes de vérification. Les projets plus importants auront leur propre dossier.

Le cours pointera vers le dossier et la révision correspondants lorsqu’ils seront effectivement disponibles sur GitHub. Cela permettra de retrouver une étude et un point de départ compatibles.

## Comprendre l’autonomie des modules

Un module sera autonome dans sa construction et ses instructions ; il pourra néanmoins avoir des prérequis pédagogiques. Comprendre une machine à états peut demander de connaître les énumérations et les conditions, sans exiger que tu aies terminé tous les exercices précédents.

## Préparer le passage sur carte

Les premiers sujets pourront être travaillés sur ordinateur. Pour un exercice matériel, il faudra connaître la référence exacte de la carte, le framework choisi et le câblage validé. Les commandes de compilation et de transfert seront données dans le dépôt concerné ; elles dépendent de ces choix.

Le site ne compile pas et n’exécute aucun exercice. Tes modifications et tes essais restent dans ton environnement local.
