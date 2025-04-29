# Ali Celebi - Assi Karim - DANY Raphael -  ZASEMPA JOAN - KACEM Hamid Hackathon IA

## Introduction

Ce projet a été réalisé dans le cadre du module hackathon. Il s'agit d'une application, permettant d'intéragir avec nos utilisateurs via un chatbot. Le projet inclut également une application Streamlit pour le frontend pour  télécharger des fichiers pour le RAG, discuter avec le chatbot que ce soit par écrit ou via la fonctionnalité audio.

## Structure du projet

Le projet est structuré en plusieurs fichiers :

- `.streamlit/secrets.toml` : Le fichier `secrets.toml` dans le dossier `.streamlit/` sont à créer à l'init du projet (cf. Section Installation).
- `chromadb/` : Le dossier contenant la base de donnée ChromaDB.
- `downloaded_files/` : Le dossier contenant les fichiers déposés via le front `raw/` pour les fichiers pdf et `prepared/` pour ceux traités et insérés dans la db.
- `functions/` : Le dossier contenant les fonctions principales.
- `pages/` : Le dossier contenant nos différentes pages.
- `api.py` : Le fichier principal .
- `Chatbot-RAG.py` : L'application front développée avec Streamlit + le dossier `pages` pour nos différentes pages.
- `requirements.txt` : Les dépendances nécessaires au projet.

## Installation

Pour installer les dépendances nécessaires, exécutez la commande suivante dans un terminal :

Créer un dossier `.streamlit/` à la racine du projet contenant un fichier à créer `secrets.toml`.
Ajouter ces lignes dans le fichier nouvellement créé : 
```shell
MISTRAL_API_KEY = "<votre clé API mistral>"
OPENAI_API_KEY = "<votre clé API openai>"
```

Ensuite placez vous à la racine de votre projet et créez un environnement virtuel pour votre projet : 
```shell
python -m venv .venv\nom_de_votre_environnement
```
Attention le fichier `.gitignore` est configuré pour ignorer le dossier `.venv\` donc nommez votre environnement virtuel en commençant par `.venv\` afin qu'il ne soit pas pris en compte dans un push du projet si vous faites un fork.

Activez votre environnement virtuel : 
```shell
.venv\nom_de_votre_environnement\Scripts\activate
```

Enfin une fois votre environnement virtuel activé lancez cette commande pour installer toutes les librairies du projet :
```shell
pip install -r requirements.txt
```

## Lancement à la racine du dossier

L'application streamlit :
```shell
streamlit run .\Chatbot-RAG.py
```

