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

Une version portable sur Windows peut être disponible. 
La procédure ci-dessous explique comment.

1. Allez dans le répertoire `Scripts/qt5/` et exécuter le script `MakePortable.bat`

2. L'exécutable est disponible dans le répertoire `dist`