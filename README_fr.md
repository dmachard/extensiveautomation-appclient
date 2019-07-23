Client Applicatif pour ExtensiveAutomation
======================================

Introduction
------------

L'application cliente permet de piloter un serveur ExtensiveAutomation.
Le client est basée sur le framework Qt, il peut être exécuté sur Windows, Linux et MacOS.

Installation depuis les sources
------------------------

L'application cliente supporte Python2 et 3. Cette procédure explique comment exécuter le client.

1. Cloner le dépôt sur votre machine

        git clone https://github.com/ExtensiveAutomation/extensiveautomation-appclient.git
   
2. Installer les paquets suivants avec la commande pip

        py -m pip install pyinstaller pylint pyqt5 qscintilla PyQtWebEngine

3. Exécuter le client avec Python

        cd extensiveautomation-appclient/
        py Main.py
        
Version portable pour Windows
--------------------------------

Une version portable en mode exécutable sur Windows peut être générée. 
La procédure ci-dessous explique comment.

1. Allez dans le répertoire `Scripts/qt5/` et exécuter le script `MakePortable.bat`

2. L'exécutable est disponible dans le répertoire `dist`

3. Exécuter le fichier `ExtensiveAutomationClient.exe` pour ouvrir le client.



Comment utiliser le client lourd directement avec le serveur (sans reverse proxy) ?
--------------------------------------------------------------------

Par défault, le client est configuré pour se connecter sur le serveur à travers un reverse proxy.
Néanmoins, en modifiant manuellement la configuration il est possible de l'utiliser sans RP.

Editer le fichier de configuration du client `File\settings.ini` comme ci-dessous:

        [Server]
        data-ssl=False
        api-ssl=False
        port-data=8082
        port-api=8081
        rest-path=/

/!\ Au moment de la connexion depuis le client lourd, ne pas mettre de numéro de port dans 
l'adresse. Si un port est présent, l'application remodifie automatiquement la configuration en mode reverse proxy.