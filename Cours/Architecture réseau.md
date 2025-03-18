
# Révisions 

## Découpage de plages 

172.16.0.0

SALES : 200 : 172.16.0.0 -> 172.16.0.255 
			255.255.255.0 /24
R&D : 50 : 172.16.1.0 -> 172.16.1.63 
			255.255.255.192 /26
MGT : 25 : 172.16.1.64 -> 172.16.1.95 
			255.255.255.224 /27
IT : 10 : 172.16.1.96 -> 172.16.1.111 
			255.255.255.240 /28
PRINTERS : 10 : 172.16.1.112 -> 172.16.1.127
			255.255.255.240 /28
SERVERS : 10 : 172.16.1.128 -> 172.16.1.143
			255.255.255.240 /28

SALES:
172.16.0.0
1010 1100 0001 0000 0000 0000 0000 0000
1111 1111 1111 1111 1111 1111 0000 0000
1010 1100 0001 0000 0000 0000 1111 1111
--> 172.16.0.255

R&D :
172.16.1.0
1010 1100 0001 0000 0000 0001 0000 0000
1111 1111 1111 1111 1111 1111 1100 0000
1010 1100 0001 0000 0000 0001 0011 1111
--> 172.16.1.63

MGT : 
172.16.1.64
1010 1100 0001 0000 0000 0001 0100 0000
1111 1111 1111 1111 1111 1111 1110 0000
1010 1100 0001 0000 0000 0001 0101 1111
--> 172.16.1.95

IT : 
172.16.1.96
1010 1100 0001 0000 0000 0001 0110 0000
1111 1111 1111 1111 1111 1111 1111 0000
1010 1100 0001 0000 0000 0001 0110 1111
--> 172.16.1.111

PRINTERS : 
172.16.1.112
1010 1100 0001 0000 0000 0001 0111 0000
1111 1111 1111 1111 1111 1111 1111 0000
1010 1100 0001 0000 0000 0001 0111 1111
--> 172.16.1.127

SERVERS : 
172.16.1.128
1010 1100 0001 0000 0000 0001 1000 0000
1111 1111 1111 1111 1111 1111 1111 0000
1010 1100 0001 0000 0000 0001 1000 1111
--> 172.16.1.143

## Classes d'adresses IP

Le modèle OSI : Open Systems Interconnection

7 couches :

-      7 : Application

-      6 : Présentation

-      5 : Session

-      4 : Transport (Port sur 16 bits, 65536 différents) (Protocol TCP avec accusé de réception et UDP, firewall, Segment)

-      3 : Réseau (adresse IP : IPv4 sur 32 bits, IPv6 sur 128 bits, routeur, Paquet(packet))

-      2 : Liaison de données (adresse MAC, 48 bits, 6 octets à 3 fabricant, 3 machine, switch(commutateur), Trame(Frame))

-      1 : Physique (Wireless (ondes électromagnétiques), câble Ethernet, câble coaxial, fibre, hub(concentrateur))
![[Pasted image 20241104092906.png]]
Combinaisons :
4 bits : 16
8 bits : 256
16 bits : 65536
24 bits : 16m
32 bits : 4md 

1000 0000 : 128 (début classe A)
1100 0000 : 192 (début classe B)
1110 0000 : 224 (début classe C)
1111 0000 : 240 (début classe D)
1111 1000 : 248 (début classe E)
1111 1100 : 252
1111 1110 : 254
1111 1111 : 255

# Router on a stick

(Voir la procédure "PROTOCOLE CONFIG RESEAU")

# Switch layer 3 en cœur de réseau 


SVI (switch virtual interface) : interface virtuelle pour chaque vlan
layer 3 : mettre une alimentation (AC-POWER-SUPPLY)


![[Pasted image 20241105112003.png]]

![[Pasted image 20241105112028.png]]

retaper les vlan à la main / mettre les vlan dans un bloc puis crtl c + crtl v / utiliser le vtp en utilisant le switch server

![[Pasted image 20241105112459.png]]

![[Pasted image 20241105112548.png]]


![[Pasted image 20241105114339.png]]

"Interface vlan 10" permet de créer une interface pour le vlan 10
"ip add x.x.x.x x.x.x.x" attribue l'adresse de la gateway à l'interface avec son masque de sous réseau
"show ip interface brief" pour afficher la liste des interfaces créées et leurs adresses ip

![[Pasted image 20241105114933.png]]

"ip routing" permet la communication entre les sous réseaux

![[Pasted image 20241105115206.png]]

![[Pasted image 20241105115345.png]]

On sélectionne le port qui communique avec le routeur puis "no switchport"
"Interface Gig1/0/4" pour sélectionner l'interface
"Ip add 10.10.10.2 255.255.255.252" pour lui attribuer l'adresse ip du même réseau que l'interface du routeur

![[Pasted image 20241105120011.png]]

"ip route x.x.x.x x.x.x.x y.y.y.y" pour définir la route 'x.x.x.x x.x.x.x' étant l'adresse de la gateway et le masque de sous réseau vers lequel la requête doit être transmise et 'y.y.y.y' étant l'adresse de l'interface du layer 3 avec lequel le routeur communique

SDN (Software Defined Networking)

Configuration NAT routage dynamique 

Dans le routeur : 
Interface côté privé : ip nat inside
Interface côté public : ip nat outside

Créer une access list pour le réseau : access-list 10 permit  x.x.x.x 0.0.0.255
x.x.x.x étant le réseau privé

Permettre à notre access list le passage par l'interface publique : ip nat inside source list 10 interface g0/0 overload

ATTENTION : penser à faire une ip route dans chaque routeur

# Configuration DHCP avec un serveur (packet tracer)

https://ccnareponses.com/7-2-10-packet-tracer-configurer-dhcpv4/
# Redondance

## Protocole STP (Spanning tree protocol)

file:///C:/Users/bapti/OneDrive/Bureau/Le-protocole-STP.pdf

![[Pasted image 20250107110648.png]]

**Les BPDUs sont des messages STP échangés entre les switchs pour détecter les boucles réseau et configurer une topologie sans boucle**

![[Pasted image 20250107111853.png]]

**Le STP ne désactive pas l'interface, il empêche les messages autres que les siens de circuler**

Election du **Root Bridge (RB)** par le **BID (Bridge ID)** codé en binaire sur 64 bits (composé d'un chiffre en 16 bits (priorité) et d'un chiffre en 48 bits (adresse MAC))
- 16 bits : 0 --> 65535, par défaut, 32767 (pas de priorité)
- 48 bits : adresse MAC


Dans le CLI packet tracer : "show version" pour voir l'adresse MAC

**Le switch prioritaire (RB) sera celui avec le BID le plus faible**
Sur le RB, toutes les interfaces sont des DP (Designated Ports)
![[Pasted image 20250107113846.png]]
![[Pasted image 20250107114402.png]]

![[Pasted image 20250107114942.png]]
# FHRPs

![[Pasted image 20250204135130.png]]

## HSRP 

![[Pasted image 20250204135509.png]]

![[Pasted image 20250204162615.png]]

## VRRP

![[Pasted image 20250204140050.png]]

## GLBP

![[Pasted image 20250204140258.png]]

## Tableau de comparaison des FHRPs

![[Pasted image 20250204140344.png]]

