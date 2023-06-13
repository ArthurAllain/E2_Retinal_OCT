# Contexte du projet

Vous venez de rejoindre une start-up MedTech en tant que développeur.se IA.

L'entreprise a remporté un appel d'offre du CHRU de Nancy pour la réalisation d'un POC (Proof Of Concept) d'une solution IA capable de diagnostiquer les maladies de la rétines à partir d'imagerie par OCT.

​L’imagerie par OCT permet de détecter soit un épaississement de la rétine, soit la présence d’anomalie dans ou sous la rétine (œdème, néovaisseaux, atrophie, membrane, etc.) Cet examen permet d’analyser les conséquences de pathologies rétiniennes comme la dégénérescence maculaire liée à l’âge, la rétinopathie diabétique, les occlusions vasculaires, etc.

Une première version a été développée par un doctorant de l'INRIA. Il s'agit d'une API qui permet de prédire à partir d'une imagerie par OCT :

une néovascularisation choroïdienne
un Œdème maculaire diabétique
de multiples drusen
une rétine normale
Vous avez comme mission d'améliorer le modèle (en modifiant ses paramètres ou en utilisant une autre architecture) et de développer une application avec une page de prédiction (chargement d'une imagerie par OCT et affichage de la prédiction).

# Data:

Le jeu de données utilisé pour ce projet est disponible : https://www.kaggle.com/datasets/paultimothymooney/kermany2018.

# Models

## Modèle initial

Le code complet permettant de générer le modèle est disponible via ce lien : https://colab.research.google.com/drive/1UzymPZ7DOG9JO2nOEA4IndMaed1kzQyK?usp=sharing.
ou dans le fichier "retinal_oct_classification.ipynb" situé à la racine du projet.

## Modèle amélioré

Ce modèle est basé sur le modèle initial. J'ai effectué plusieurs modification permettant une amélioration des métriques d'évaluation.
Le code utilisé ce situe, à la racine du projet, dans le fichier "retinal_oct_v2.ipynb".
Le model déjà entrainé doit être téléchargé via ce lien : https://drive.google.com/file/d/1p1eWodsnvJIaij2e9uChDKBaqsP77g9e/view?usp=drive_link.
Une fois le téléchargement effectué le ".h5" doit être placé dans le dossier "./model/v2"

# Remerciements

Data : https://data.mendeley.com/datasets/rscbjbr9sj/2
Citation: http://www.cell.com/cell/fulltext/S0092-8674(18)30154-5
