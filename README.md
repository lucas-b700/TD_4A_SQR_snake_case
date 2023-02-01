# TD_4A_SQR_snake_case 
By [Falkowski Maxime](https://github.com/FLKprod) et [Blanchard Lucas](https://github.com/lucas-b700)
**Spécialité SQR**  

![esirem](https://www.u-bourgogne.fr/wp-content/uploads/logo-couleur.jpg)

## Exercice "Automatiser votre dépôt"

![example workflow](https://github.com/lucas-b700/TD_4A_SQR_snake_case/actions/workflows/blank.yml/badge.svg)
![example workflow](https://github.com/lucas-b700/TD_4A_SQR_snake_case/actions/workflows/blank2.yml/badge.svg)

## Projet

Nous avons décidé de réaliser le sujet guidé n'ayant aucune base en CI/CD avant ce cours.

### 2.1.1  Réaliser une première version de l’API REST  

En utilisant Flask, nous avons réaliser une première version de l’API.  
  
Voici une liste des actions qui ont été mises en place via un appel HTTP sur API:
* E1 - Enregistrer une transaction.
* E2 - Afficher une liste de toutes les transactions dans l’ordre chronologique.
* E3 - Afficher une liste des transactions dans l’ordre chronologique liées à une personne.
* E4 - Afficher le solde du compte de la personne.
* E5 - Importer des données depuis un fichier csv.

Par rapport au point E5 nous avons mis en place le fichier csv en suivant la syntaxe suivante :  
P1 | P2 | t | s  
Avec P1 et P2 des personnes, t l'heure de la transaction et s la somme de la transaction.  
  
### 2.1.2  Documenter l’API via des READMEs et un fichier Swagger

Comme dis précédemment nous avons décidé de réaliser le sujet guidé n'ayant aucune base en CI/CD avant ce cours.  
  
Le fichier swagger est disponible sur le dépot.

### 2.1.3 Préparer l’intégration continue (CI)

Les trois github actions demandées ont été réalisée :
* Une déclenchée à chaque changement pour builder l’application. (Script Python)
* Une déclenchée manuellement pour utiliser le fichier Dockerfile pour créer une image. (Docker push GCR)
* Une déclenchée pour chaque tag semver pour utiliser le fichier Dockerfile pour créer et pousser l’image de l’API avec en tag la version semver spécifiée. (Docker push GCR semver)
  
![example workflow](https://github.com/lucas-b700/TD_4A_SQR_snake_case/actions/workflows/blank3.yml/badge.svg)
![example workflow](https://github.com/lucas-b700/TD_4A_SQR_snake_case/actions/workflows/Docker_push_GCR.yaml/badge.svg)
![example workflow](https://github.com/lucas-b700/TD_4A_SQR_snake_case/actions/workflows/Docker_push_GCR_semver.yml/badge.svg)
  
Cependant Script Python affiche failing au lieu de passing, le problème étant que le workflow, lorsque l'on fait un commit, tourne sans jamais s'arrêter. Cependant lorsque l'on fais un test en local cela fonctionne.

### 2.1.4 Anticiper le déploiement continue (CD)

Cette étape a été réalisé au cours de la dernière séance de TP et le badge est disponible à l'étape 2.1.3 sous le nom "Docker push GCR"

### Procédure d'exécution de l'API

Entrez dans le fichier fichierClient.csv les noms des personnes participant à une transaction que vous souhaitez mettre en place, l'heure de la transaction ainsi que le montant de celle ci, le tout en respectant la syntaxe vu à l'étape 2.1.1 (P1 | P2 | t | s)  
  
Vous pouvez alors vous rendre dans le fichier main.py et modifier ligne 53 le numero de fin de la boucle for en fonction du nombre de transactions que vous avez ajoutés au fichier fichierClient.csv  
  
Si vous souhaitez mettre en place une transaction avec une personne qui n'existe pas actuellement en plus de t'étape précédente vous devez créer cette personne ligne 39 en respectant la syntaxe "p[numero] = Person("[nom]",[solde du compte])" en modifiant ce qui se trouve entre crochet.  
Enfin veuillez ajouter ligne 41 la personne à la liste "people" en suivant la syntaxe "[numero suivant dans la liste]:p[numero de la personne renseigné ligne 39]" toujours en modifiant ce qui se trouve entre crochet.
