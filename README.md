Qt application for ExtensiveAutomation
======================================

Introduction
------------

The Qt application client enable to interact with the ExtensiveAutomation server.

Connection to the server
------------------------

Download the latest zip of the [release](https://github.com/ExtensiveAutomation/extensiveautomation-appclient/releases)
And then follow the [user guide](https://extensiveautomation.readthedocs.io/en/latest/user/getting_started.html#connection-to-the-server)

Installation from source
------------------------

Follow this procedure to execute the application on Windows with Python3.

1. Clone this repository on your machine

        git clone https://github.com/ExtensiveAutomation/extensiveautomation-appclient.git
   
2. Add additional Python packages with the pip command

        py -m pip install sip pyinstaller pylint pyqt5 qscintilla PyQtWebEngine

3. Execute the client 

        cd extensiveautomation-appclient/
        py Main.py
        
Build portable version for Windows
--------------------------------

Portable version can be build on Windows. Follow this procedure if you want to.

1. Go in the folder `Scripts/qt5/` and execute the script `MakePortable.bat`

2. The output is available in the `dist` folder

3. Execute the file `ExtensiveAutomationClient.exe` to open-it


How to use the client without reverse proxy in front of the server ?
--------------------------------------------------------------------

By default, the client is configured to be used without a reverse proxy in front of the server since the version 21.0.0

        [Server]
        data-ssl=False
        api-ssl=False
        port-data=8082
        port-api=8081
        rest-path=/

/!\ Be careful, do not provide the tcp port on the address bar of the client during the connection.
If the tcp port is present like that `:8081` then the application automatically reconfigure
the client in reverse proxy mode.

How to use the client with a reverse proxy in front of the server ?
--------------------------------------------------------------------

The client can be configured to be used with a reverse proxy.
It's possible to change that by updating the `File\settings.ini` as follow:

        [Server]
        data-ssl=True
        api-ssl=True
        port-data=8080
        port-api=8080
        rest-path=/rest/

/!\ Be careful, do not provide the tcp port on the address bar of the client during the connection.
If the tcp port is present like that `:8081` then the application automatically reconfigure
the client in reverse proxy mode.