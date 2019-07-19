Qt application for ExtensiveAutomation
======================================

Introduction
------------

The Qt application client enable to interact with the ExtensiveAutomation server.

Installation from source
------------------------

The Qt application support both Python 2 and 3. Follow this procedure to execute the application
on Windows with Python3.

1. Clone this repository on your machine

        git clone https://github.com/ExtensiveAutomation/extensiveautomation-appclient.git
   
2. Add additional Python packages with the pip command

        py -m pip install pyinstaller pylint pyqt5 qscintilla PyQtWebEngine

3. Execute the client 

        cd extensiveautomation-appclient/
        py Main.py
        
Portable version for Windows
--------------------------------

Portable version can be build on Windows. Follow this procedure if you want to.

1. Go in the folder `Scripts/qt5/` and execute the script `MakePortable.bat`

2. The output is available in the `dist` folder

3. Execute the file `ExtensiveAutomationClient.exe` to open-it


How to use the client without reverse proxy in front of the server ?
--------------------------------------------------------------------

By default, the client is configured to be used with a reverse proxy.
It's possible to change that by update the `File\settings.ini` as follow:

        [Server]
        data-ssl=False
        port-data=8082
        port-api=8081
        rest-path=/
