# Simulador-de-Ransomware // Alpha-Version

L'objectiu principal de l'Sprint 1 (de l'1 al 21 de desembre de 2025) ha estat establir les bases organitzatives i tècniques del projecte. En aquesta etapa, ens hem centrat a definir els objectius del grup i a utilitzar eines com JIRA per garantir una gestió eficient de les tasques, aixi com elaborar una part funcional que ens funcioni a mode de base sòlida per al projecte. El resultat d'aquest esforç és aquesta versió Alpha, que serveix com a prova de concepte funcional.

Per aconseguir una base sòlida, hem estructurat el treball en tres eixos. Primer, hem preparat tota la infraestructura del repositori a GitHub amb una organització neta de carpetes (src/, data/, logs/) i una configuració de GitFlow que ens permet treballar de forma eficient. A més, hem implementat un motor de xifratge real mitjançant la llibreria cryptography, que permet generar claus simètriques i transformar fitxers de text pla en fitxers xifrats recuperables. Finalment, hem prioritzat la claredat d'ús amb un menú interactiu per terminal i un sistema de logs que registra tota l'activitat, assegurant que el programa només actuï dins la carpeta /sandbox per evitar qualsevol risc accidental.

Guia d'execució:

Per posar en marxa aquesta versió Alpha, segueix aquests passos:

1. Instal·lació de dependències: És necessari instal·lar la llibreria de xifratge externa. Cal executar la següent comanda al terminal:
   
pip install cryptography

2. Preparació de l'entorn: Crea una carpeta anomenada sandbox/ a l'arrel del projecte i col·loca-hi els fitxers que vulguis provar (incloent-hi subcarpetes si vols testar la recursivitat).
   
3. Llançament del programa: Executa el fitxer principal main.py

4. Funcionament del menú:
   - Opció 1 (Infectar): El programa buscarà tots els fitxers a la sandbox, aplicarà el filtre de seguretat i xifrarà els permesos afegint l'extensió .locked.
   - Opció 2 (Recuperar): Utilitzarà la clau generada (gestor_claus.key) per tornar els fitxers al seu estat original.
   - Opció 3 (Logs): Mostra l'historial d'accions realitzades pel programa.
