
# Analyse de la vidéo "Basic Security"

![[Pasted image 20250304105740.png]]
La commande "show privilege" dans Packet Tracer est utilisée pour afficher le niveau de privilège actuel de l'utilisateur sur le routeur ou le commutateur. Cela permet de vérifier si l'utilisateur a les droits nécessaires pour exécuter certaines commandes ou effectuer des configurations spécifiques.

![[Pasted image 20250304111443.png]]
Cela définirait le mot de passe "cisco" pour la console, obligerait les utilisateurs à se connecter, et définirait un délai d'inactivité de 10 minutes avant la déconnexion automatique.

![[Pasted image 20250304111017.png]]
Cela supprimerait le mot de passe "cisco" qui avait été configuré pour la ligne de console.

![[Pasted image 20250304112412.png]]
Cela définirait la longueur minimale des mots de passe à 8 caractères. Cela signifie que tout mot de passe configuré après cette commande doit avoir au moins 8 caractères.

![[Pasted image 20250304112525.png]]
On s'aperçoit que le mot de passe "cisco" est trop court désormais

![[Pasted image 20250304113019.png]]
La commande "username baptiste password cisco1234" dans Packet Tracer (et sur les équipements Cisco en général) est utilisée pour créer un compte utilisateur avec un nom d'utilisateur (baptiste) et un mot de passe spécifique (cisco1234).

![[Pasted image 20250304114742.png]]
La commande "login local" dans Packet Tracer (et sur les équipements Cisco en général) est utilisée pour activer l'authentification locale pour une ligne de console

![[Pasted image 20250304114806.png]]
Le nom d'utilisateur et son mot de passe sont donc à renseigner pour pouvoir se connecter

![[Pasted image 20250304140203.png]]
La commande "username bob secret november" dans Packet Tracer (et sur les équipements Cisco en général) est utilisée pour créer un compte utilisateur avec un nom d'utilisateur (bob) et un mot de passe secret (november) de manière cryptée.

![[Pasted image 20250304142250.png]]
La commande "enable password september" dans Packet Tracer (et sur les équipements Cisco en général) est utilisée pour définir un mot de passe (september) qui sera requis pour passer du mode utilisateur privilégié au mode de configuration globale.

![[Pasted image 20250304142359.png]]
La commande "enable secret september" dans Packet Tracer (et sur les équipements Cisco en général) est utilisée pour définir un mot de passe crypté (ciscocisco) qui sera requis pour passer du mode utilisateur privilégié au mode de configuration globale.

![[Pasted image 20250304143240.png]]
La commande "service password-encryption" dans Packet Tracer (et sur les équipements Cisco en général) est utilisée pour chiffrer les mots de passe en texte clair stockés dans le fichier de configuration. Cela ajoute une couche de sécurité en empêchant les utilisateurs non autorisés de voir facilement les mots de passe lorsqu'ils accèdent au fichier de configuration.

https://www.firewall.cx/cisco/cisco-routers/cisco-type7-password-crack.html

![[Pasted image 20250304144041.png]]
La commande "username joe privilege 15 secret cisco4321" est utilisée pour créer un compte utilisateur nommé "joe" avec un mot de passe crypté "cisco4321" et pour attribuer un niveau de privilège spécifique à cet utilisateur.

![[Pasted image 20250304144738.png]]
La commande "username paul privilege 3 secret ciscociscocisco" est utilisée pour créer un compte utilisateur nommé "paul" avec un mot de passe crypté "ciscociscocisco" et pour attribuer un niveau de privilège spécifique à cet utilisateur.

![[Pasted image 20250304145137.png]]
La commande "privilege exec level 3 show startup-config" dans Packet Tracer (et sur les équipements Cisco en général) est utilisée pour attribuer un niveau de privilège spécifique à une commande EXEC. Elle attribue le niveau de privilège 3 à la commande "show startup-config". Normalement, la commande "show startup-config" est accessible uniquement aux utilisateurs avec un niveau de privilège 15 (le plus élevé).

![[Pasted image 20250304145709.png]]
La commande "login block-for 120 attempts 5 within 45" sur les équipements Cisco est utilisée pour empêcher les tentatives de connexion par force brute en imposant des restrictions après un certain nombre d'échecs de connexion.
En résumé, si un utilisateur échoue à se connecter 5 fois en 45 secondes, toutes les tentatives de connexion suivantes seront bloquées pendant 120 secondes.

![[Pasted image 20250304150053.png]]
La commande "banner motd & DO NOT ATTEMPT TO LOGIN AND ACCESS THIS ROUTER &" est utilisée pour configurer un message d'avertissement qui s'affiche lorsque quelqu'un tente de se connecter à un routeur ou un commutateur Cisco. "MOTD" signifie "Message of the Day" (Message du jour), et ce message peut être utilisé pour fournir des informations ou des avertissements aux utilisateurs.

![[Pasted image 20250304160050.png]]
Avec ces commandes, les utilisateurs devront entrer un nom d'utilisateur et un mot de passe configurés localement pour se connecter au routeur via Telnet ou SSH.

![[Pasted image 20250304160814.png]]
La commande "ip domain-name remotetrainingsolutions" dans Packet Tracer (et sur les équipements Cisco en général) est utilisée pour configurer le nom de domaine sur un routeur.
En définissant ce nom de domaine, tu peux ensuite générer des clés cryptographiques pour sécuriser les connexions SSH, ou configurer d'autres services nécessitant un nom de domaine.

![[Pasted image 20250304161209.png]]
La commande "crypto key generate rsa" dans Packet Tracer (et sur les équipements Cisco en général) est utilisée pour générer une paire de clés RSA (Rivest-Shamir-Adleman) pour la sécurité des communications.
Après avoir exécuté cette commande, tu seras invité à spécifier la taille de la clé en bits (par exemple, 1024 ou 2048 bits), ce qui détermine le niveau de sécurité.

![[Pasted image 20250304161459.png]]
La commande "transport input ssh" dans Packet Tracer (et sur les équipements Cisco en général) est utilisée pour spécifier le protocole de transport à utiliser pour les connexions aux lignes vty (Virtual Teletype) sur le routeur ou le commutateur.

![[Pasted image 20250304162648.png]]
Avec cette configuration, le port FastEthernet0/1 apprendra dynamiquement les adresses MAC des périphériques connectés et les enregistrera comme adresses MAC sécurisées. Cela permet d'améliorer la sécurité du réseau en empêchant les périphériques non autorisés de se connecter à ce port.

![[Pasted image 20250304162820.png]]
La commande "switchport port-security violation shutdown" dans Packet Tracer (et sur les équipements Cisco en général) est utilisée pour configurer le comportement d'un port sécurisé lorsqu'une violation de sécurité se produit. Si une violation de sécurité se produit sur le port FastEthernet0/1, le port sera automatiquement désactivé pour prévenir tout risque de sécurité.

![[Pasted image 20250304163010.png]]
La commande "switchport port-security maximum 1" est utilisée pour configurer la sécurité des ports sur un commutateur Cisco en limitant le nombre maximal d'adresses MAC autorisées à se connecter à un port spécifique.

Pour changer l'adresse mac enregistrée sur le port du switch, il faut arrêter et redémarrer le port du switch (shutdown / no shutdown).


# ACLs (Access Control List)

L'ordre des ACLs est important

2 types d'ACLs :
- Standards 
	numérotées : 1-99 et 1300-1999
	filtrage : IPv4 source

- Etendues
	numérotées : 100-199 et 2000-2699
	nommées 
	filtrage : IPv4 source et destination
		  IPv6 source et destination
		  Ports
		  Protocoles
		  MAC (option)

Mots clés : 
	Any
	Host
	*Established (ACL étendue*)

Wild card (l'inverse du subnet mask)

Les ACLs sont composées d'ACE (Acces Control Elements)

Méthodes de saisie :
- access-list
- ip access-list

Vérification : 
- show access-list
- show ip interface

Les ACLs standards se positionnent toujours proche de la destination
Une ACL sur une interface en entrée et en sortie par interface

## 4.1.4 Packet Tracer - ACL Demonstration

![[Pasted image 20250305093838.png]]
![[Pasted image 20250305093859.png]]
L'ACL 10 bloque tous les paquets originaires du réseau 192.168.10.0/24 (ping inclus) tandis que l'ACL 20 autorise tous les trafics de tous les autres réseaux

![[Pasted image 20250305094304.png]]
Pour l'interface Serial0/0/0, l'ACL 11 s'applique en sortie. 

![[Pasted image 20250305094633.png]]
Cette commande désactive l'application de l'ACL 11 pour le trafic sortant sur l'interface en question. En d'autres termes, elle retire l'ACL 11 de l'interface.
![[Pasted image 20250305094644.png]]
Cette commande supprime l'ACL 11 de la configuration du routeur. Après l'exécution de cette commande, l'ACL 11 n'existera plus sur le routeur.

## 5.1.8 Packet Tracer - Configure Numbered Standard IPv4 ACLs

![[Pasted image 20250305104831.png]]
La première commande refuse tout le trafic provenant du réseau 192.168.11.0/24 à destination du réseau 192.168.20.0/24.
La deuxième commande permet tout autre trafic provenant de n'importe quelle source vers n'importe quelle destination.

![[Pasted image 20250305105000.png]]
Cette commande applique l'ACL 1 à l'interface GigabitEthernet0/0 en sortie.

![[Pasted image 20250305103958.png]]
La première commande refuse tout le trafic IP provenant du réseau 192.168.10.0/24 à destination du réseau 192.168.30.0/24.
La deuxième commande permet tout autre trafic provenant de n'importe quelle source vers n'importe quelle destination.

![[Pasted image 20250305104059.png]]
Cette commande applique l'ACL 102 à l'interface GigabitEthernet0/0 en sortie.

![[Pasted image 20250305105118.png]]
![[Pasted image 20250305105159.png]]
Vérification des ACL sur les routeurs 2 et 3.

## 5.1.9 Packet Tracer - Configure Named Standard IPv4 ACLs

![[Pasted image 20250305105718.png]]
Ces commandes créent une ACL qui autorise uniquement le trafic provenant des adresses IP 192.168.20.4 et 192.168.100.100, et refuse tout autre trafic. Cela peut être utilisé, par exemple, pour restreindre l'accès à un serveur de fichiers uniquement à ces deux adresses IP spécifiques.

![[Pasted image 20250305105904.png]]

![[Pasted image 20250305105955.png]]
Cette commande applique l'ACL nommée "File_Server_Restrictions" à l'interface FastEthernet0/1 pour le trafic sortant. Cela signifie que les règles définies dans l'ACL seront appliquées à tout le trafic quittant l'interface Fa0/1.

![[Pasted image 20250305110522.png]]

## 5.2.7 Packet Tracer - Configure and Modify Standard IPv4 ACLs 

![[Pasted image 20250305111319.png]]
Ces commandes créent une ACL qui permet l'accès aux réseaux locaux de R1 (192.168.10.0/24 et 192.168.20.0/24) et refuse tout autre trafic. Cela garantit que seuls les réseaux spécifiés peuvent accéder aux ressources protégées par cette ACL.

![[Pasted image 20250305111436.png]]
Cette commande applique l'ACL 1 à l'interface GigabitEthernet0/0/0 en sortie.

![[Pasted image 20250305111853.png]]

![[Pasted image 20250305112033.png]]
Ces commandes créent une ACL qui autorise uniquement le trafic provenant de l'adresse IP 192.168.30.3 et du réseau 192.168.40.0/24. La politique "BRANCH-OFFICE-POLICY" peut être appliquée à une interface pour contrôler l'accès en fonction des adresses IP spécifiées.
On aurait aussi pu utiliser "permit 192.168.30.3 0.0.0.0" à la place du premier ACE.

![[Pasted image 20250305112752.png]]
Ces commandes créent une ACL qui autorise uniquement le trafic provenant de la plage d'adresses IP 209.165.200.224 à 209.165.200.255, et refuse tout autre trafic. La politique "BRANCH-OFFICE-POLICY" peut être appliquée à une interface pour contrôler l'accès en fonction des adresses IP spécifiées.

## 5.4.12 Packet Tracer - Configure Extended IPv4 ACLs - Scenario 1

![[Pasted image 20250305113523.png]]
Cette commande crée une règle dans l'ACL 100 qui permet le trafic TCP provenant de la plage d'adresses IP 172.22.34.64 à 172.22.34.95 à destination de l'adresse IP 172.22.34.62 sur le port FTP (port 21).

![[Pasted image 20250305113727.png]]
Cette commande crée une règle dans l'ACL 100 qui permet le trafic ICMP provenant de la plage d'adresses IP 172.22.34.64 à 172.22.34.95 à destination de l'adresse IP 172.22.34.62.

Tous les autres trafics sont bloqués par défaut.

![[Pasted image 20250305113853.png]]
Ces commandes configurent l'application de l'ACL 100 sur l'interface GigabitEthernet0/0 pour contrôler le trafic entrant selon les règles définies dans l'ACL.

![[Pasted image 20250305114306.png]]
Ces commandes créent une ACL étendue nommée "HTTP_ONLY" qui permet le trafic TCP HTTP (port 80) et le trafic ICMP provenant de la plage d'adresses IP 172.22.34.96 à 172.22.34.111 à destination de l'adresse IP 172.22.34.62.

![[Pasted image 20250305114432.png]]

![[Pasted image 20250305114509.png]]
Cette commande applique l'ACL nommée "HTTP_ONLY" à l'interface GigabitEthernet0/1 pour le trafic entrant. Cela signifie que les règles définies dans l'ACL "HTTP_ONLY" seront appliquées à tout le trafic entrant sur cette interface.

## 5.4.13 Packet Tracer - Configure Extended IPv4 ACLs - Scenario 2

![[Pasted image 20250305123615.png]]
Cette commande crée une liste de contrôle d'accès (ACL) étendue nommée "LimitedAccess".

![[Pasted image 20250305123708.png]]
Ces commandes configurent des règles dans une ACL étendue pour refuser le trafic TCP de l'hôte 172.31.1.101 vers les hôtes 64.101.255.254 et 64.103.255.254 sur les ports 80 (HTTP) et 443 (HTTPS). Ces règles empêchent ainsi l'hôte source d'accéder aux hôtes de destination via les services HTTP et HTTPS.

![[Pasted image 20250305123840.png]]
Ces commandes configurent des règles dans une ACL étendue pour refuser le trafic TCP de l'hôte 172.31.1.102 vers les hôtes 64.101.255.254 et 64.103.255.254 sur le port 21 (FTP). Cela empêche ainsi l'hôte source d'accéder aux hôtes de destination via le service FTP.

![[Pasted image 20250305125847.png]]
Ces commandes configurent des règles dans une ACL étendue pour refuser le trafic ICMP de l'hôte 172.31.1.103 vers les hôtes 64.101.255.254 et 64.103.255.254. Cela empêche ainsi l'hôte source d'envoyer des messages ICMP (tels que des requêtes ping) aux hôtes de destination spécifiés.

![[Pasted image 20250305130105.png]]
Cette règle permet d'assurer que tout le trafic non explicitement refusé par les autres entrées de l'ACL sera autorisé.

![[Pasted image 20250305130525.png]]
Sur la base des informations fournies, la liste de contrôle d'accès étendue nommée "LimitedAccess" doit être placée sur l'interface de RT1 la plus proche de la source du trafic, qui est le réseau 172.31.1.96/27. En supposant que l'interface la plus proche de la source soit GigabitEthernet0/0, l'ACL doit être appliquée dans la direction entrante pour filtrer le trafic lorsqu'il entre dans l'interface.

![[Pasted image 20250305131421.png]]

## 5.5.1 Packet Tracer - IPv4 ACL Implementation Challenge 

![[Pasted image 20250305134852.png]]
L'ACL 101 bloque tout d'abord le trafic TCP vers l'adresse IP 192.168.1.70 sur le port FTP, puis bloque le trafic ICMP vers le sous-réseau 192.168.1.0/26, et enfin permet tout le reste du trafic IP.

![[Pasted image 20250305135222.png]]
Ces commandes configurent l'interface série 0/1/0 pour utiliser l'ACL 101 afin de filtrer tout le trafic entrant selon les règles spécifiées dans cette ACL.

![[Pasted image 20250305135417.png]]
L'ACL 111 bloque tout d'abord le trafic IP provenant du sous-réseau 192.168.1.0/26 à destination de l'adresse IP 192.168.2.45, puis permet tout le reste du trafic IP.

![[Pasted image 20250305135559.png]]
Ces commandes configurent l'interface GigabitEthernet 0/0/0 pour utiliser l'ACL 111 afin de filtrer tout le trafic entrant selon les règles spécifiées dans cette ACL.

![[Pasted image 20250305135800.png]]
Ces commandes créent une liste de contrôle d'accès standard nommée "vty_block" et autorisent le trafic IP provenant des adresses IP sources dans la plage 192.168.1.64 - 192.168.1.71.

![[Pasted image 20250305140046.png]]
Ces commandes configurent les lignes VTY 0 à 4 pour utiliser l'ACL "vty_block" afin de contrôler et sécuriser les connexions à distance en fonction des adresses IP sources spécifiées.

![[Pasted image 20250305140404.png]]
L'ACL étendue "branch_to_hq" bloque tout d'abord le trafic IP provenant des sous-réseaux 192.168.2.0/27 et 192.168.2.32/28 à destination du sous-réseau 192.168.1.0/26, puis permet tout le reste du trafic IP.

![[Pasted image 20250305140543.png]]
Ces commandes configurent l'interface série 0/1/1 pour utiliser l'ACL "branch_to_hq" afin de filtrer tout le trafic sortant selon les règles spécifiées dans cette ACL.


## 5.5.2 Packet Tracer - Configure and Verify Extended IPv4 ACLs - Physical Mode


