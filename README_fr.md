Client Applicatif pour ExtensiveAutomation
======================================

Introduction
------------

L'application cliente permet de piloter un serveur ExtensiveAutomation.
Le client est basée sur le framework Qt, il peut être exécuté sur Windows, Linux et MacOS.

Connexion au serveur
------------------------

Télécharger le zip de la dernière (release)[https://github.com/ExtensiveAutomation/extensiveautomation-appclient/releases]
Et suivre le (Guide d'utilisation)[https://extensiveautomation.readthedocs.io/fr/v21.4/user/getting_started.html#connexion-du-client-au-serveur]

Installation depuis les sources
------------------------

Cette procédure explique comment exécuter le client sur Windows avec Python3.

1. Cloner le dépôt sur votre machine

        git clone https://github.com/ExtensiveAutomation/extensiveautomation-appclient.git
   
2. Installer les paquets suivants avec la commande pip

        py -m pip install sip pyinstaller pylint pyqt5 qscintilla PyQtWebEngine

3. Exécuter le client avec Python

        cd extensiveautomation-appclient/
        py Main.py
        
Build de la version portable pour Windows
--------------------------------

Une version portable en mode exécutable sur Windows peut être générée. 
La procédure ci-dessous explique comment.

1. Allez dans le répertoire `Scripts/qt5/` et exécuter le script `MakePortable.bat`

2. L'exécutable est disponible dans le répertoire `dist`

3. Exécuter le fichier `ExtensiveAutomationClient.exe` pour ouvrir le client.



Comment utiliser le client lourd directement avec le serveur (sans reverse proxy) ?
--------------------------------------------------------------------

Fonctionnement par défaut depuis la version 21.0.0

        [Server]
        data-ssl=False
        api-ssl=False
        port-data=8082
        port-api=8081
        rest-path=/
        
/!\ Au moment de la connexion depuis le client lourd, ne pas mettre de numéro de port dans 
l'adresse. Si un port est présent, l'application remodifie automatiquement la configuration en mode reverse proxy.

Comment utiliser le client lourd directement avec le serveur (avec reverse proxy) ?
--------------------------------------------------------------------

Le client peut être configuré pour se connecter sur le serveur à travers un reverse proxy.
Pour cela il faut éditer le fichier de configuration du client `File\settings.ini` comme ci-dessous:

        [Server]
        data-ssl=True
        api-ssl=True
        port-data=8080
        port-api=8080
        rest-path=/rest/

/!\ Au moment de la connexion depuis le client lourd, ne pas mettre de numéro de port dans 
l'adresse. Si un port est présent, l'application remodifie automatiquement la configuration en mode reverse proxy.
