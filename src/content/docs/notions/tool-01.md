---
title: "TOOL-01 — Comprendre la compilation"
description: "À partir d’une alarme de température, comprendre ce que vérifie le compilateur et ce qui lui échappe."
---

**Objectif :** expliquer ce qu’une compilation réussie permet de conclure, et ce qu’elle ne garantit pas. **Prérequis :** aucun ; il n’est pas nécessaire de connaître la syntaxe C++ pour suivre cette page.

**État :** cours illustré par des situations commentées. Les fichiers d’exemple et l’exercice local ne sont pas encore disponibles ; leur étude UML reste à valider.

## Partons d’une alarme de température

Imagine un dispositif qui affiche la moyenne de deux mesures. Notre besoin est précis : pour deux températures de **20 °C et 30 °C**, le résultat attendu est **25 °C**.

Tu modifies le programme sur ton ordinateur. Ton IDE — le logiciel dans lequel tu écris et construis le programme — affiche ensuite « compilation réussie ».

Ce message confirme une étape technique. Il ne dit pas encore que le programme calcule 25 °C, ni que ta carte utilise la version modifiée. Pour comprendre pourquoi, regardons le rôle de cette étape.

## Ce que fait le compilateur

Tu écris le programme dans un **fichier source**, un fichier texte contenant des instructions C++. Le **compilateur** analyse ces instructions et les traduit pour une **cible**, c’est-à-dire le processeur et l’environnement auxquels le programme est destiné.

Dans une construction classique, la traduction d’un fichier source produit un **fichier objet**. Celui-ci contient notamment du code traduit, mais ce n’est pas nécessairement un programme exécutable complet. Une autre étape, l’édition de liens, l’assemble avec les autres éléments nécessaires.

| Élément | Dans notre situation |
| --- | --- |
| Source | Le texte qui décrit le calcul de la température moyenne. |
| Compilateur | L’outil qui analyse ce texte et le traduit pour la cible choisie. |
| Fichier objet | Un résultat intermédiaire de la construction. |
| Besoin | Obtenir une moyenne correcte : 25 °C pour 20 °C et 30 °C. |

Le point essentiel est la dernière ligne : **le compilateur reçoit le source, pas ton intention**. Si tu écris une formule incorrecte mais autorisée par le langage, il peut la traduire sans erreur.

:::note[Un bouton peut lancer plusieurs étapes]
Dans un IDE, un bouton appelé « Compiler » peut lancer toute une chaîne de construction. Ici, nous isolons le rôle du compilateur. TOOL-02 expliquera l’édition de liens ; il n’est pas nécessaire de la maîtriser pour poursuivre cette page.
:::

## Premier cas : le texte contient une erreur

Imagine que tu oublies un point-virgule à un endroit où la syntaxe C++ en exige un. Le compilateur ne peut pas interpréter correctement cette instruction et signale une erreur.

Un diagnostic peut ressembler à ceci. C’est une illustration de lecture, pas une sortie reproduite d’un exercice fourni :

```text
temperature.cpp:8:5: error: expected ';' before 'return'
```

| Partie du message | Ce qu’elle indique |
| --- | --- |
| `temperature.cpp` | Le fichier concerné. |
| `8:5` | La ligne et la colonne où le problème a été détecté. |
| `error` | Un diagnostic d’erreur. |
| `expected ';' before 'return'` | L’outil attendait un point-virgule avant le mot indiqué. |

La position signalée n’est pas forcément celle de l’oubli : il faut parfois regarder l’instruction précédente. Le texte exact et les positions varient selon le compilateur et le programme.

**Bonne habitude :** lis le premier diagnostic pertinent, examine le code autour de la position indiquée, corrige la cause puis relance la construction. Une seule faute peut déclencher plusieurs messages ; les corriger tous séparément peut faire perdre du temps.

## Deuxième cas : le texte est accepté, le calcul est faux

Reprenons les mesures de 20 °C et 30 °C. Voici deux calculs arithmétiques, sans syntaxe C++ à apprendre pour le moment :

| Calcul | Déroulement | Résultat |
| --- | --- | --- |
| Moyenne attendue : `(20 + 30) / 2` | Additionner les deux mesures, puis diviser la somme par deux. | 25 °C |
| Erreur : `20 + 30 / 2` | Diviser 30 par deux, puis ajouter 20. | 35 °C |

Les deux expressions peuvent être valides dans un programme. Dans la seconde, la division est effectuée avant l’addition : le calcul ne correspond pas au besoin.

**Pourquoi le compilateur ne corrige-t-il pas la formule ?** Parce que rien ne lui dit que tu voulais calculer une moyenne. Le second calcul pourrait être volontaire dans un autre programme.

Un test compare un résultat obtenu à un résultat attendu. Pour notre cas, il ferait apparaître l’écart entre **35 °C obtenus** et **25 °C attendus**. Cet exemple montre l’utilité d’un test ; il ne constitue pas une preuve suffisante pour tous les calculs et toutes les températures. Les types numériques et leurs limites seront étudiés séparément.

## Troisième cas : le source a changé, la carte n’a pas changé

Tu corriges la formule et la construction réussit. Pourtant, la carte affiche encore l’ancien résultat.

Une explication possible est simple : le nouveau programme a été construit sur l’ordinateur, mais pas transféré sur la carte. Construire un programme et le faire exécuter par le microcontrôleur sont deux opérations distinctes.

Ce n’est pas la seule explication possible. Il faudra vérifier le transfert, la carte ciblée et la version réellement exécutée. Ces vérifications appartiennent au futur module TOOL-07 ; nous retenons ici uniquement que **compiler ne suffit pas à mettre à jour une carte**.

## Comparer les trois situations

| Observation | Conclusion possible | Conclusion à ne pas tirer |
| --- | --- | --- |
| Le compilateur signale une erreur de syntaxe. | Le source doit être corrigé pour cette étape. | Le capteur est défectueux. |
| La compilation réussit. | Cette compilation s’est terminée sans erreur bloquante. | La formule respecte forcément le besoin. |
| La construction réussit après une modification. | De nouveaux artefacts ont pu être produits sur l’ordinateur. | La carte exécute forcément la nouvelle version. |

Un **avertissement** est un autre type de diagnostic : il attire l’attention sur un problème potentiel. Selon la configuration, il peut être toléré ou traité comme une erreur. Il ne faut pas le masquer sans comprendre sa cause ; TOOL-03 lui sera consacré.

## Concevoir avant la future pratique

Le cas de la moyenne illustre le cours ; ce n’est pas encore un exercice prêt à cloner. Son étude devra fixer les entrées acceptées, le résultat attendu, les cas limites et la correspondance entre UML, code et tests. Elle sera validée avant d’écrire les fichiers d’exemple.

Aucun design pattern n’est nécessaire pour expliquer la compilation. En revanche, deux bonnes pratiques sont déjà visibles : **écrire le résultat attendu avant de vérifier le programme** et **distinguer une erreur de traduction d’une erreur de comportement**.

La pratique se déroulera exclusivement dans ton IDE, depuis le dépôt dédié. Le cours ne propose ni compilateur ni exercice à exécuter dans le navigateur.

## L’essentiel à retrouver plus tard

- Le compilateur analyse et traduit un source pour une cible.
- Un diagnostic aide à localiser une cause ; sa position demande parfois d’examiner le code voisin.
- Un calcul accepté peut produire un résultat contraire au besoin.
- Construire le programme ne garantit pas que la carte exécute cette version.

**Pour se repérer :** [vue d’ensemble de la chaîne de construction](../../du-source-au-programme/).

**Suite disponible :** [initialiser une variable](../cpp-01/). Les modules TOOL-02, TOOL-03 et TOOL-07 restent prévus.
