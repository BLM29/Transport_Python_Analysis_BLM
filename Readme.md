## Analyse de la performance transport de notre Supply Chain avec Python 

Ce projet s’inscrit dans une démarche d’analyse de la performance transport d’une supply chain pour une entreprise de distribution.
Il est réalisé à titre d’exercice avec Python afin de simuler des données logistiques réalistes et d’en analyser la performance.

L’objectif est de construire un dataset logistique simulé, puis d’analyser la performance des transporteurs et des entrepôts à l’aide d’indicateurs opérationnels.

## Contexte

Une entreprise de distribution nationale livre ses clients B2B via plusieurs entrepôts régionaux et collabore avec différents transporteurs externes.

Dans une logique de pilotage de sa supply chain, l’entreprise doit suivre la performance transport afin de :

- Garantir un bon taux de service
- Réduire les coûts de transport
- Identifier les transporteurs les plus performants
- Identifier les entrepôts générant le plus de retards
- Comprendre l’impact de la distance et du volume sur la performance logistique
- Objectifs du projet

Ce projet vise à analyser la performance transport afin d’évaluer :

- Le taux de livraison à l’heure (On-Time Delivery)
- Le retard moyen de livraison
- La performance comparative des transporteurs
- La performance des entrepôts
- Le coût de transport
- Le coût par kilomètre
- L’impact de la distance sur les délais
- L’impact du volume mensuel sur la performance transport
- 
## Dataset

Les données sont générées de manière simulée via un script Python afin de reproduire un environnement logistique réaliste.

Le dataset contient notamment :

- Des entrepôts
- Des transporteurs
- Des régions de livraison
- Des distances de transport
- Des volumes mensuels
- Des dates d’expédition et de livraison
- Des retards de livraison
- Des coûts de transport

L’objectif est de disposer d’une base de données exploitable pour réaliser des analyses de performance transport.

## Indicateurs analysés (KPI)

Transport :

- Nombre d’expéditions
- Taux de livraison à l’heure
- Retard moyen
- Coût de transport total
- Coût par kilomètre
- Performance par transporteur
- Performance par entrepôt
- Performance par région

Analyse opérationnelle :

- Impact de la distance sur le retard
- Impact du volume sur la performance
- Comparaison des transporteurs
- Identification des axes d’amélioration de la performance logistique
- Méthodologie

Le projet est structuré en deux parties :

Génération des données :

- Création d’un dataset logistique simulé
- Génération des distances, coûts, délais et retards
- Création des variables de performance (retard, on-time, coût/km, etc.)

Analyse des données :

- Analyse via Pandas
- Calcul des KPI logistiques
- Analyse par transporteur, entrepôt, région
- Visualisation des résultats avec Matplotlib
- Technologies utilisées

## Compétences mises en œuvre

Python :

- Pandas
- Numpy
- Matplotlib

Outils :

- Jupyter Notebook

## Problématiques métier

Comment améliorer le taux de service tout en maîtrisant les coûts de transport ?

Dans quelle mesure la performance des transporteurs et des entrepôts influence-t-elle la performance globale de la supply chain ?

Quel est l’impact de la distance et du volume sur la performance transport ?

## Conclusions métier

Cette analyse permet de :

- Identifier les transporteurs les plus performants
- Identifier les entrepôts générant le plus de retards
- Mesurer l’impact de la distance sur les délais
- Mesurer l’impact du volume sur la performance
- Identifier des leviers d’amélioration pour réduire les coûts et améliorer le taux de service
