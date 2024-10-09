
# Qu'est ce que c'est ? 

Stockage, réseaux, travail collaboratif "distants" 
--> Tout ce qui est vu en physique se fait dans le cloud
200 services (considéré comme une formation à part)

Toute maintenance "réseau" est à la charge de l'utilisateur, le fournisseur ne prend à sa charge que l'alimentation électrique et la sécurité physique des outils.
La maintenance et la mise à jour des équipements sont assurées par le fournisseur

### Principaux Fournisseurs

AWS (Amazon) / AZURE (Microsoft) / GOOGLE

### Fonctionnement 

Première chose mise en place : IaaS (infrastructure as a Service)
--> responsable de toute l'installation 

PaaS (Platform as a Service)

SaaS (Software as a Service) (Microsoft 365, suite Google)
--> responsable de presque aucune installation
## Formation initiale 

Cloud computing : déploiement à la demande de puissance de calcul, de stockage, de bases de données, d'application etc...
--> tarification à l'utilisation

"délocalisation" d'un réseau traditionnel 

Modèle de déploiement : full cloud / hybride / sur site (cloud privé)

#### Avantages du cloud : 

6 avantages : 
- moins d'investissements (temps/argent), paiement en fonction de l'utilisation
- économie d'échelle (réduction de prix vis à vis de l'achat du fournisseur)
- pas de problème d'estimation de taille de serveur (sur ou sous estimation)
- temps de mise en place (seulement quelques minutes)
- pas de coût/temps de maintenance
- déploiement international en quelques minutes, pas de "panne", assure une continuité de service

Dépense opérationnelle et non d'investissement 
Toute la gestion se fait à distance avec les langages XML ou JSON
Une multitude de services sont mis à disposition en fonction des exigences et des besoins 

Accès aux services : AWS management console / AWS CLI (interface de ligne de commande) / SDK (kits de développement logiciel)

Framework d'adoption AWS Cloud 
Regarder les contraintes / les demandes, former les personnes, préparer en amont le cadre avant l'utilisation du Cloud
==> perte d'argent si l'on est pas prêt 

#### Base de la tarification 

Trois facteurs fondamentaux de coût avec AWS : Calcul / Stockage / Transfert de données

Le transfert de données dans une même région est gratuit 
Possibilité de lancer ou arrêter un service à tout moment 
Pas de dépenses initiales, on ne paie que ce que l'on utilise, sans maintenance
Pas de contrat 
Tarification échelonnée et progressive
AWS a baissé ses prix 75 fois entre 2006 et 2019

Une tarification sur mesure est possible si aucune proposée de correspond à nos besoins
Certains services peuvent être gratuits pour la première année d'utilisation 

Services sans frais : Amazon VPC, Elastic Beanstalk, Auto Scaling, AWS Cloudformation

Le coût total de possession (TCO) regroupe aussi bien le coût du matériel, que tous les coûts associés (licences, maintenance, mise à jour etc...). Il peut être difficile de le calculer pour un réseau physique.
Une entreprise délivrant un service de cloud (comme AWS) donne une facture claire et facile à comprendre, regroupant tous ces coûts, il est ainsi facile de voir quels composants ou quelle partie du réseau est la plus onéreuse, permettant de viser plus facilement les changements à faire en fonction des besoins 

L'outil de calculatrice mis à disposition sur AWS permet de simuler la facture potentielle en fonction des services que l'on souhaite utiliser.
On peut voir l'estimation sur 12 mois ou encore avoir le détail de chaque service

L'outil de suivi des factures et coûts de nos services AWS permet de visualiser l'évolution de notre facture sur plusieurs mois et de prévisualiser la prochaine facture en plus de pouvoir analyser tous les détails de notre facture 

#### Infrastructure mondiale AWS

région AWS, zone de disponibilité et emplacements périphériques
22 régions disponibles isolées les unes des autres. Les données ne sont pas répliquées d'une zone à une autre. Une région doit être activée. Il est important de se renseigner sur la gouvernance des données de la région que l'on choisit
Il est recommandé de choisir une région proche de ses utilisateurs 
Il est important de noter que tous les services AWS ne sont pas disponibles dans toutes les régions 

Plusieurs zones de disponibilité par région qui contiennent plusieurs centres de données 
Les zones de disponibilité possèdent leurs propres installations électriques 
réplication synchrone entre les zones de dispo
Répliquer les données sur plusieurs zones de dispo permet une meilleure résilience 
Les centres de données sont conçus de sortent à être résistant aux incidents climatiques et pour rester à la pointe de la technologie + hautement disponible 

Infrastructure AWS : élastique, évolutive, s'adapte, redondance intégrée des composants, haute disponibilité 

#### Services et catégories de services

Utilisation à la demande

Liste des plus utilisés : 
- stockage : Amazon S3, EBS (machine virtuelle), EFS, NFS, S3 glacier (plutôt pour les archives)
- calcul : Amazon EC2, ECS, ECR, Elastic Beanstalk, EKS, Amazon Fargate
- base de données : Amazon Aurora, Redshift, DynamoDB
- mise en réseau : Amazon VPC, CloudFront, Transit Gateway, Route 53, Direct Connect, VPN
- sécurité, identité et conformité : Organizations, Cognito, Artifact, KMS, Shield
- gestion des coûts : Budgets, Cost Explorer
- gestion et gouvernance : Config, CloudWatch, Auto Scaling, Command Line Interface, Trusted Advisor, Well-Architect Tool

#### Modèle de responsabilité partagée AWS

AWS est responsable de la sécurité du Cloud (installation physique : infrastructure, composants, maintenance etc...), de l'hébergement de sa plateforme AWS
Le client est responsable de tout ce qui se passe sur son réseau et ses données
AWS met à disposition plusieurs outils et logiciels afin de renforcer la sécurité de nos données

IaaS : le client dispose d'une plus grande responsabilité sur la sécurité de son réseau
Paas : le client est limité sur la responsabilité de la sécurité du réseau
Saas : le client ne possède presque pas de responsabilité sur la sécurité du réseau

#### Mise en réseau et diffusion de contenu

Une fois le réseau VPC créé, on ne peut plus modifier la plage d'adresses 
AWS réserve 5 adresses IP dans les sous-réseaux

#### Sécurité des VPC

Chaque sous-réseau d'un VPC doit être associé à une ACL
Statefull / Stateless
Amazon Route 53

#### Calcul

Amazon EC2 fournit des machines virtuelles 
Amazon ECS est un organisateur de conteneurs 
AWS Lambda est une solution de calcul sans serveur, on ne paie que pour le temps de calcul utilisé
AWS Beanstalk est considéré comme une PaaS

![[Capture d’écran 2024-10-08 à 08.57.32.png]]

Applications courantes Amazon EC2 : serveurs d'applications, serveurs web, serveurs de bases de données

![[Capture d’écran 2024-10-08 à 09.05.27.png]]

Différents types et instances d'EC2, il est possible de choisir les caractéristiques de nos machines en fonction de nos besoins 
Au delà des composants de la machine virtuelle, il est aussi possible de régler la bande passante 
Des machines pré faites sont proposées par AWS permettant de les déployer en quelques minutes seulement 
Par défaut, toutes les instances sont limitées à 5 adresses IP elastic par région 


AWS Lambda : On peut créer un code dans une fonction sans se soucier du serveur et on ne paie que lorsque le code est déclenché (facturé tous les 100 millisecondes) 
 