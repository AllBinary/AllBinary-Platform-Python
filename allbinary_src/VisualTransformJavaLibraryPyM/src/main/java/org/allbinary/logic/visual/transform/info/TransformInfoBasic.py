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
# package org.allbinary.logic.visual.transform.info

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.business.context.AbContext import AbContext
from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface


#Hack class should not exist
@java_inherited_overloads
class TransformInfoBasic(*java_bases(AbContext, TransformInfoHttpInterface)):
    def _java_defaults(self):
        vars(self).setdefault("storeFrontInterface", None)

    def _init_fields(self) -> None:
        if "storeFrontInterface" not in vars(self): self.storeFrontInterface: StoreFrontInterface = None
    

    def __init__(self, storeFrontInterface: StoreFrontInterface, propertiesHashMap: HashMap, pageContext: PageContext) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        super().__init__(propertiesHashMap, pageContext)
        __class__._init_fields(self)
        self.storeFrontInterface = storeFrontInterface
    

    def getStoreName(self) -> str:
        return self.storeFrontInterface.getName()
    

    def log(self) -> str:
        return self.commonStrings.NOT_IMPLEMENTED
    

    def override(self, hashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        pass
    

    def getName(self) -> str:
        return None
    

    def getObjectFile(self) -> str:
        return None
    

    def getObject(self) -> object:
        return None
    

    def getObjectConfigInterface(self) -> TransformInfoObjectConfigInterface:
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigInterface import TransformInfoObjectConfigInterface
        return None
    

    def setObjectConfigInterface(self, transformInfoObjectConfigInterface: TransformInfoObjectConfigInterface) -> None:
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigInterface import TransformInfoObjectConfigInterface
        pass
    

    def getTemplateFilePath(self) -> AbPath:
        from org.allbinary.logic.io.path.AbPath import AbPath
        return None
    

    def getTemplateFile(self) -> str:
        return None
    

    def getTemplate(self) -> str:
        return None
    

    def getDataFilePath(self) -> AbPath:
        from org.allbinary.logic.io.path.AbPath import AbPath
        return None
    

    def getDataFile(self) -> str:
        return None
    

    # throws Exception
    def getDataDocument(self) -> Document:
        from org.w3c.dom.Document import Document
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    def setName(self, value: str) -> None:
        pass
    

    def setStoreName(self, value: str) -> None:
        pass
    

    def setObjectFile(self, value: str) -> None:
        pass
    

    def setObject(self, anyType: object) -> None:
        pass
    

    def setObjectConfigFile(self, value: str) -> None:
        pass
    

    def setTemplateFile(self, value: str) -> None:
        pass
    

    def setTemplate(self, value: str) -> None:
        pass
    

    def setDataFile(self, value: str) -> None:
        pass
    

    def setData(self, value: str) -> None:
        pass
    

    def setChild(self) -> None:
        pass
    

    def isChild(self) -> bool:
        return True
    

    def getImportUriPath(self) -> str:
        return None
    

    def setImportUriPath(self, importUriPath: str) -> None:
        pass
    

    # throws Exception
    def getKey(self) -> object:
        return None
    

    # throws Exception
    def toVector(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return None
    

    # throws Exception
    def toHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        return None
    

    def getWeblisketSession(self) -> WeblisketSessionInterface:
        from org.allbinary.logic.communication.http.request.session.WeblisketSessionInterface import WeblisketSessionInterface
        return java_super_call(super(), "getWeblisketSession")
    

    def getPageContext(self) -> PageContext:
        return java_super_call(super(), "getPageContext")
    

    def getPropertiesHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        return java_super_call(super(), "getPropertiesHashMap")
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigInterface import TransformInfoObjectConfigInterface
# from org.w3c.dom.Document import Document
# from org.allbinary.logic.communication.http.request.session.WeblisketSessionInterface import WeblisketSessionInterface


