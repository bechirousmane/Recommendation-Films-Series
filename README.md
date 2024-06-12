README

# Recommendation-Films-Series

## 1 Présentation du Projet

Ce projet implémente un système de recommandation de films en utilisant le dataset MovieLens. Il combine le traitement des données, le machine learning et le développement d'une interface utilisateur pour fournir des recommandations personnalisées de films. Les principaux composants incluent la pré-traitement des données, l'entraînement du modèle, la génération de recommandations et une interface utilisateur simple pour l'interaction.

## 2 Fonctionnalités

`Pré-traitement des données : Nettoyage et préparation du dataset MovieLens.`
`Machine Learning : Construction et entraînement d'un modèle de recommandation.`
`Génération de Recommandations : Fourniture de recommandations personnalisées de films.`
`Interface Utilisateur : Interface basique permettant aux utilisateurs de recevoir leurs recommandations.`

## 3 Exigences

    Python 3.x
    Bibliothèques : pandas, numpy, scikit-learn, Flask, SQLAlchemy
    Dataset : MovieLens (version 20M)

## 4 Attribution

Ce projet utilise le dataset MovieLens. Le dataset est fourni par MovieLens et est publié sous une licence Creative Commons. L'attribution appropriée est fournie dans la documentation du projet, comme requis par les conditions d'utilisation.

## 5 Installation
### 5.1 Cloner le dépôt :
    
    sh
    git clone https://github.com/bechirousmane/Recommendation-Films-Series.git


### 5.2 Installer les bibliothèques requises :
    
    sh
    pip install -r requirements.txt

**Télécharger le dataset MovieLens et le placer dans le répertoire data/.**

## 6 Utilisation

**Pré-traiter les données :**
    
    sh
	python preprocess.py

**Entraîner le modèle de recommandation :**

    sh
	python train_model.py

**Lancer le serveur web :**
    
    sh
	python app.py

**Ouvrir votre navigateur web et aller sur `http://localhost:5000` pour utiliser l'application.**

## 7 Détails du Modèle

Le modèle de recommandation utilise des techniques de filtrage collaboratif. Les principaux algorithmes utilisés incluent :

    Factorisation de Matrice
    k-Nearest Neighbors (k-NN)
    Filtrage Basé sur le Contenu

## 8 Résultats

Le système de recommandation a été testé sur le dataset MovieLens et fournit des recommandations précises et personnalisées basées sur les évaluations des utilisateurs.

## 9 Contribution

Les contributions sont les bienvenues ! Veuillez forker le dépôt et créer une pull request pour toute amélioration ou correction de bug.

