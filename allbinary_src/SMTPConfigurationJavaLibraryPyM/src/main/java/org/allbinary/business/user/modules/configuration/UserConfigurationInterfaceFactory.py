#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
# 
# By agreeing to this license you and any business entity you represent are
# legally bound to the AllBinary Open License Version 1 legal agreement.
# 
# You may obtain the AllBinary Open License Version 1 legal agreement from
# AllBinary or the root directory of AllBinary's AllBinary Platform repository.
# 
# Created By: Travis Berthelot
#  
# Generated Code Do Not Modify
# package org.allbinary.business.user.modules.configuration

from __future__ import annotations



class UserConfigurationInterfaceFactory:
    configurationName: str = "DefaultUserConfiguration"
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getInstance(document: Document) -> UserConfigurationInterface:
        from org.allbinary.business.user.modules.configuration.UserConfigurationData import UserConfigurationData
        from org.allbinary.business.user.modules.configuration.UserConfigurationView import UserConfigurationView
        configurationNode: Node = DomSearchHelper.getNode(UserConfigurationData.NAME, document.getChildNodes())
        return UserConfigurationView(configurationNode).getUserConfigurationInterface()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def getInstance(userRole: UserRole) -> UserConfigurationInterface:
        from org.allbinary.business.user.modules.configuration.UserConfigurationData import UserConfigurationData
        from org.allbinary.business.user.modules.configuration.UserConfigurationData import UserConfigurationData
        from org.allbinary.business.user.modules.configuration.UserConfigurationData import UserConfigurationData
        abPath: AbPath = AbPath(self.URLGLOBALS.getMainPath() + self.FREEBLISKET_PATH_GLOBALS.getInstance().USERCONFIGURATIONPATH, str(UserConfigurationInterfaceFactory.configurationName) + str(userRole) + str(AbPathData.getInstance().EXTENSION_SEP) + str(UserConfigurationData.UNCRYPTED_EXTENSION))
        documentString: str = CryptFileReader(UserConfigurationData.UNCRYPTED_EXTENSION, UserConfigurationData.ENCRYPTED_EXTENSION).get(abPath)
        document: Document = DomDocumentHelper.create(documentString)
        return UserConfigurationInterfaceFactory.getInstance(document)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def getInstance() -> UserConfigurationInterface:
        from org.allbinary.business.user.modules.configuration.UserConfiguration import UserConfiguration
        return UserConfiguration()
from org.allbinary.business.user.role.UserRole import UserRole
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


