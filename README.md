
# Programme de Scraping ETL (Version Bêta)

## Description
Ce projet est un programme de scraping conçu pour extraire, transformer et charger des données à partir du site [Books to Scrape](https://books.toscrape.com). Il est développé dans le cadre de la création d'un système de surveillance des prix des sites concurrents.

### Version Bêta
> **Attention :** Ce programme est en version bêta et ne fonctionne qu'avec le site `Books to Scrape`.

## Objectif du Projet
Le programme récupère les informations des livres du site, telles que :

- **Titre**
- **Prix**
- **Disponibilité**
- **Catégorie**
- **Description**
- **Image**
- **Classement (nombre d'étoiles)**
- **UPC**
- **Prix HT**
- **Prix TTC**

## Installation
1. **Cloner le dépôt :**
   ```bash
   git clone git@github.com:pierre-emma/OpenclassroomsProject_02.git
   cd OpenclassroomsProject_02
   ```

2. **Créer et activer un environnement virtuel :**
   ```bash
   python -m venv env
   # Sur Windows
   .\env\Scripts\activate
   # Sur macOS/Linux
   source env/bin/activate
   ```

3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

## Exécution du programme
Lancez le fichier `main.py` :

```bash
python main.py
```

## Fonctionnement
Le programme suit les étapes suivantes :

1. **Extraction (`extract.py`)** : Récupération des données des livres.
2. **Transformation (`transform.py`)** : Mise en forme et nettoyage des données.
3. **Chargement (`load.py`)** : Sauvegarde des données dans un fichier .csv et sauvegarde des images.

## Contributeur
- Pierre-Emma
