# Master, exécution du JenKinsFile

[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)  [![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](http://forthebadge.com)

Une petite description du projet

## Pour commencer

Cette branch "Master" est conçu pour pouvoir effectuer le fichier Jenkinsfile depuis notre Jenkins qui est stocké sur notre docker.
Il contient entre autre notre projet backend qui est "app.py".
Tout ça a été effectué sur une machine Windows.

### Pré-requis

- Docker Desktop
- Editeur de code (Vscode par exemple)
- Jenkins 

### Installation

Tout d'abord, il faudra le projet frontend ainsi que le projet backend.
Le front se trouve https://github.com/raoufcherfa/Imad-aws dans le dossier angular.

Une fois le dossier angular récupéré, il faudra le backend, ici le backend a été écrit via python qui est le fichier app.py.

Avant de créer une image docker, il faut exécuter la commande ``wsl --update`` pour pouvoir créer un environnement linux et pouvoir utiliser docker convenablement.

Maintenant, il faut exécuter via un terminal la commande suivante : ``docker build -t "nom de l'image"`` . Dans le dossier ou se trouve le frontend (angular) et le backend qui est dans cette branche.
Cela va créer une image docker et ensuite pour pouvoir exécuter l'image, il faut la mettre en container tous sur le port 80.

Une fois les containers réalisés, tester le front et le back si tout fonctionne correctement.

Si les test sont OK, il faut télécharger le JenkinsFile via ce github : https://github.com/raoufcherfa/employe
Une fois le fichier téléchargé, il faudra installer jenkins tout se trouve sur leur site officiel : https://www.jenkins.io/download/
Une fois jenkins installé et déployé sur votre machine docker, il faudra utiliser le jenkinsfile précedemment pour pouvoir effectuer les tests.

Vous allez être bloqué à l'étape du build si votre code est bon si ce n'est pas le cas revoyez votre code. Pour passer l'erreur Build, il faudra exécuter les commandes suivantes : 

``docker exec -it -u 0 “ID de container” /bin/bash
apt-get update / apt-get upgrade
apt-get install python3
apt-get install pip
pip install pytest``

Vous devriez obtenir ceci : 
![image](https://user-images.githubusercontent.com/125256927/219599238-2804615e-8b75-44da-b771-f6d7c7395a97.png)

## Fabriqué avec

* [VsCode](https://code.visualstudio.com/) - Editeur de code
* [Docker](https://www.docker.com/) - Tester et déployer rapidement des applications à l'aide de conteneurs
* [Jenkins](https://www.jenkins.io/) - Outil open source de serveur d'automatisation
* [ChatGPT](https://chat.openai.com/) - Agent conversationnel utilisant l'intelligence artificielle

## Versions
Le projet étant un projet débutant, le versionning n'est pas considéré.

## Auteurs
Listez le(s) auteur(s) du projet ici !
* **Mikail ALBAYRAK** _alias_ [@regnat0r](https://github.com/mikailsupdevinci)
[Raouf CHERFA](https://github.com/raoufcherfa/employe) pour voir qui à aidé au projet !
