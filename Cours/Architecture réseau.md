
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


## Exercice

