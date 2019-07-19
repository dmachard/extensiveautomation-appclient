#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
# Copyright (c) 2010-2019 Denis Machard
# This file is part of the extensive automation project
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA
# -------------------------------------------------------------------

"""
Repositories manager module
"""

import sys

# unicode = str with python3
if sys.version_info > (3,):
    unicode = str
    
try:
    from PyQt4.QtGui import (QWidget, QFrame, QTabWidget, QIcon, QLabel, QFont, QVBoxLayout)
    from PyQt4.QtCore import (QRect)
except ImportError:
    from PyQt5.QtGui import (QIcon, QFont)
    from PyQt5.QtWidgets import (QWidget, QFrame, QTabWidget, QLabel, QVBoxLayout)
    from PyQt5.QtCore import (QRect)
    
from Libs import QtHelper, Logger

try:
    import LocalRepository
    import RemoteTests
    import RemoteAdapters
    import RemoteLibraries
except ImportError: # support python3
    from . import LocalRepository
    from . import RemoteTests
    from . import RemoteAdapters
    from . import RemoteLibraries
    
import Settings
import UserClientInterface as UCI
import RestClientInterface as RCI

import os.path
import base64
import json
import zlib

# TAB_LOCAL_POS       =   0
# TAB_REMOTE_POS      =   1
# TAB_ADAPTER_POS     =   0
# TAB_LIBRARY_POS     =   1

MAIN_TAB_TEST       = 0
MAIN_TAB_DEV        = 1

class WRepositories(QWidget, Logger.ClassLogger):
    """
    Repositories widget
    """
    def __init__(self, parent=None):
        """
        Constructs WRepositories widget

        @param parent: 
        @type parent:
        """
        QWidget.__init__(self, parent)

        self.remoteRepository = None
        self.adaptersRemoteRepository = None
        
        self.createWidgets()
        self.createConnections()
        self.onResetRemote()

    def createWidgets(self):
        """
        Create qt widgets

        QTabWidget:
          ________  ________
         /        \/        \___________
        |                               |
        |                               |
        |                               |
        |_______________________________|
        """

        # remote repo
        self.remoteRepo = RemoteTests.Repository( parent = self, projectSupport=True )
        if not RCI.instance().isAuthenticated():
            self.remoteRepo.setNotConnected() 
            self.remoteRepo.setEnabled( False ) 

        # adapters remote repo
        self.adaptersRemoteRepository = RemoteAdapters.Repository( parent = self )
        if not RCI.instance().isAuthenticated():
            self.adaptersRemoteRepository.setNotConnected() 
            self.adaptersRemoteRepository.setEnabled( False ) 

        self.layout = QVBoxLayout()

        self.mainTab2 = QTabWidget()
        self.mainTab2.setEnabled(False)
        self.mainTab2.setTabPosition(QTabWidget.North)
        self.mainTab2.setMinimumWidth( 300 )
        self.mainTab2.addTab(self.remoteRepo, QIcon(":/repository-tests.png"), "Tests")

        
        self.mainTab3 = QTabWidget()
        self.mainTab3.setEnabled(False)
        self.mainTab3.setTabPosition(QTabWidget.North)
        self.mainTab3.setMinimumWidth( 300 )
        
        self.mainTab3.addTab(self.adaptersRemoteRepository, QIcon(":/repository-adapters.png"), "Adapters")

        self.layout.addWidget( self.mainTab2 )
        self.layout.addWidget( self.mainTab3 )

        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)

    def createConnections(self):
        """
        Create qt connections
        """
        pass

    def remote(self):
        """
        Returns the remote repository widget

        @return: RemoteRepository.Repository
        @rtype: QWidget
        """
        return self.remoteRepo
    
    def remoteAdapter (self):
        """
        Returns the remote repository widget

        @return: RemoteRepository.Repository
        @rtype: QWidget
        """
        return self.adaptersRemoteRepository

    # functions for remote repository
    def onLoadRemote(self, data):
        """
        Called on load remote actions
        """
        self.mainTab2.setEnabled(True)
        self.mainTab3.setEnabled(True)
        
        self.remoteRepo.setConnected() 
        self.remoteRepo.setEnabled(True)

        self.remoteRepo.defaultActions()
        if self.remoteRepo.initializeProjects( projects=data['projects'], 
                                               defaultProject=data['default-project']  ) :
            self.remoteRepo.initialize(listing= data['repo'])

        self.adaptersRemoteRepository.setConnected() 
        self.adaptersRemoteRepository.setEnabled(True)
        self.adaptersRemoteRepository.defaultActions()
        self.adaptersRemoteRepository.initialize(listing=data['repo-adp'] )

    def onResetRemote(self):
        """
        Called on reset remote actions
        """
        self.mainTab2.setEnabled(False)
        self.mainTab3.setEnabled(False)

        self.remoteRepo.setNotConnected() 
        self.remoteRepo.wrepository.clear()
        self.remoteRepo.setEnabled(False)

        self.adaptersRemoteRepository.setNotConnected() 
        self.adaptersRemoteRepository.wrepository.clear()
        self.adaptersRemoteRepository.setEnabled(False)

        self.mainTab2.setCurrentIndex(MAIN_TAB_TEST)  

    def onRefreshRemoteTests(self, data, projectId, forSaveAs=False):
        """
        """
        self.remoteRepo.defaultActions()
        
        if forSaveAs:
            self.remoteRepo.initializeSaveAs(listing=data, 
                                                   reloadItems=True )
        else:
            # update default project
            projectName = self.remoteRepo.getProjectName(projectId)
            self.remoteRepo.setDefaultProject(projectName=projectName)
            
            # reconstruct
            self.remoteRepo.initialize(listing=data )

    def onRefreshRemoteAdapters(self, data):
        """
        """
        self.adaptersRemoteRepository.defaultActions()
        self.adaptersRemoteRepository.initialize(listing=data )
 
WR = None # Singleton
def instance ():
    """
    Returns Singleton
    """
    return WR

def initialize (parent):
    """
    Initialize WRepositories widget
    """
    global WR
    WR = WRepositories(parent)

def finalize ():
    """
    Destroy Singleton
    """
    global WR
    if WR:
        WR = None