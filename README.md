# Simulador de Ransomware - ENTI UB (Projecte Final) - Release Version
Desenvolupat per Marti Oliver i Marc Fernández

Aquest projecte és un simulador educatiu de malware desenvolupat per a l'assignatura de Programació i Tecnologies de la Productivitat. L'objectiu és demostrar els mecanismes de xifratge simètric i la gestió de fitxers en un entorn controlat (sandbox), seguint metodologies àgils de desenvolupament. El programa desenvolupat simula un atac de ransomware on l'usuari estara obligat a passar per les fases que els atacants volen per a poder recuperar els seus arxius.

Gestió i evolució del Projecte:

Aquest projecte desenvolupat entre desembre i gener ha estat dividit en 3 Sprints, sempre seguint la metodologia Scrum:

Sprint 1: Durant el primer sprint els 2 integrants de l'equip ens vam posar d'acord i vam organitzar, en termes generals, tota l'estructura del projecte, aixi com establir els nostres objectius, decidir el projecte i avançar en un desenvolupament precoç per a una versio Alpha. En aquest primer Sprint es van programar funcions bàsiques, aixi com una estructura solida dels arxius necessaris per a poder continuar amb efectivitat.

Sprint 2: En aquest sprint es on vam fer el volum gran de feina de codi. Ens vam centrar en desenvolupar completament tot el programa, evitar i corretgir errors i, sobretot, garantir una bona comunicació entre nosaltres. Al final d'aquest sprint vam començar a implementar el Tkinter per a millorar la interfaç gràfica.

Sprint 3: En aquest ultim Sprint ens hem centrat en treure el codi endavant, cominicant-nos constantment per a garantir que el programa rutllés com volguessim. A més, hem desenvolupat quasi tota la interfaç gràfica aixi com el desenvolupament d'una ultima mecànica que no haviem previst fins ara. Finalment hem tancat amb totes les necessitats Scrum requerides per a entregar el treball en el millor estat possible.

Per a complir amb els requisits de l'activitat i, com que només hem sigut 2 els integrants del treball, hem utilitzat un flux de treball professional dividit en:

  JIRA:
  Gestió del Backlog, Sprint Planning i seguiment de tasques mitjançant el taulell KANBAN. [https://estudiant-team-ehgwiphm.atlassian.net/jira/software/projects/SDR/boards/35]

  Ús de 4 èpiques:
    - INFRA: Èpica relacionada amb les tasques de desenvolupament de l'estructura i configuració inicial/base del projecte.
    - CRYPTO: Èpica dedicada a ser el nucli del programa. Aqui es on es desenvolupa gran part de la logica del malware.
    - RELEASE: Èpica centrada al desenvolupament de l'experiència d'usuari, aixi com el desenvolupament de la UI i altres.
    - DOC: Èpica relacionada a documentar tots els arxius i coses relacionades amb la metodologia SCRUM. 
  
  REPOSITORI GIT HUB - GIT FLOW:  Hem separat estrictament el codi en dues branques:
  
  - Main  (Dedicada a versions definitives o quasi definitives, ja sigui per a l'Alpha o versions finals del projecte (Release))
  - Develop (Branca dedicada al desenvolupament del projecte i la més activa en quant a variables de codi)

  Cada commit en qualsevol branca pot tenir 2 missatges:
  - Update/Actualització --> Actualitzacions de codi relacionats amb solucionar errors de codi, canviar coses o qualsevol millora o modificació de codi però sense completar cap tasca predefinida al Taulell
  - Tasques actualitzades amb un identificador del taulell --> Actualitzacions de codi degudes a la finalització d'alguna tasca (SDR) plantejada al Taulell

Repositori Git-Hub [https://github.com/martioliverlopez/Simulador-de-Ransomware]

------------------------------
GUIA D'INSTALACIÓ I EXECUCIÓ
------------------------------

Per poder executar el simulador correctament, cal configurar l'entorn seguint aquests requeriments tècnics:

Requisits del sistema
  - Python: Versió 3.10 o superior.
  - Sistema Operatiu: Compatible amb Windows, macOS i Linux (provat principalment en Windows).

Instal·lació de Llibreries Externes. Cal instal·lar les següents:

- Cryptography: És la llibreria principal que gestiona l'algoritme de xifratge simètric Fernet (AES-128). S'encarrega de la generació de claus i de la transformació dels fitxers. Cal executar la seguent comanda a la terminal del sistema:

pip install cryptography

- Pillow: Aquesta llibreria és necessària per al processament d'imatges. S'utilitza per carregar els logotips i icones de la interfície gràfica. Cal executar la seguent comanda a la terminal del sistema:

pip install Pillow

- Tkinter: És la llibreria que s'encarrega de la interfície visual. Generalment, ja ve inclosa amb la instal·lació estàndard de Python. Sinó, cal executar la següent comanda a la terminal del sistema:

sudo apt-get install python3-tk

Funcionament (Guia d'Usuari)

Hem dissenyat aquest simulador per ser intuïtiu a través de la seva interfície gràfica. Per seguretat, el programa només actua sobre els fitxers situats a la carpeta específica de proves, anomenada "sandbox". Segueix aquests passos per realitzar una simulació segura:

  1- Un cop descarregat el projecte, cal crear una carpeta anomenada "data" a la mateixa carpeta del projecte.
  2- Dintre d'aquesta carpeta cal crear una subcarpeta anomenada "sandbox". Es aqui dintre on s'haura de posar tot el contingut que volguem xifrar o sobre el que        volguem fer les proves
  3- Un cop creats aquests directoris ja només quedarà executar el programa. El fitxer principal a executar es "new_main.py", que obrirà la primera pantalla             introductoria del programa. Cal presionar la tecla (space) per a continuar.
  4- Un cop dintre ens transportarem a una altre pantalla amb les 5 funcionalitats del programa:
  
      - EXECUTAR INFECCIÓ: En clicar aquest botó, el motor de xifratge buscarà tots els fitxers a la /sandbox, els xifrarà i els canviarà l'extensió a .locked. Això generarà automàticament es un fitxer INSTRUCCIONS_RECUPERACIO.txt dintre de la Sandbox. Caldrà seguir els passos que ens dicta                                 aquesta nota.
      - SIMULAR PAGAMENT (BTC): Cal introduir les dades especificades en les instruccions de recuperació i clicar en "verificar"
      - RECUPERAR DADES: Un cop simulat el pagament nomes caldrà clicar en aquesta funcionalitat per a recuperar els documents. Aquesta part utilitzarà la clau key.txt (generada durant la infecció) per retornar els fitxers al seu estat original i eliminar l'extensió .locked
      - CONSULTAR LOGS: Es pot verificar i mirar tota la informació del que ha passat fins a aquest moment en aquest apartat.
      - TANCAR TERMINAL: Un cop finalitzat la simulació podrem utilitzar aquest botó per a tancar la terminal. Es desplegarà una ultima finestra que ens demanara una confirmació per a tancar el programa.

Advertència de Seguretat: Tot i que el programa té filtres per no sortir de la carpeta sandbox, es recomana no posar-hi fitxers originals importants del sistema  operatiu.

--------------------------------------------------------------------------
Captures del 3r sprint per a justificar un bon ús de la metodologia Scrum:
--------------------------------------------------------------------------
Backlog inicial i final:

<img width="752" height="393" alt="image" src="https://github.com/user-attachments/assets/60347b3d-1fd6-44aa-ad89-099a627aa3c1" />
<img width="1629" height="741" alt="image" src="https://github.com/user-attachments/assets/92f1aa4a-707b-495d-a7c7-08252b3db6a0" />


Diagrama de Gantt del projecte (Timeline de JIRA):

<img width="1664" height="897" alt="image" src="https://github.com/user-attachments/assets/985401ba-bb1e-41ee-a25d-1fda5c72c57d" />
<img width="1663" height="800" alt="image" src="https://github.com/user-attachments/assets/b9e31fa7-4c0a-4a40-8eae-816ef3c1628a" />


Resum final JIRA:

<img width="1661" height="871" alt="image" src="https://github.com/user-attachments/assets/45f72b77-9b62-43ad-beb7-08424c825a7e" />

