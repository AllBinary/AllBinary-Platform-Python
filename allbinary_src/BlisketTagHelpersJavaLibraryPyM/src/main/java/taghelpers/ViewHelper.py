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
# package taghelpers

from __future__ import annotations

from org.allbinary.logic.visual.transform.TransformInterface import TransformInterface


class ViewHelper(TransformInterface):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
        self.componentInterface: TransformInterface = None
        self.NO_TYPE: int = 0
    

    def __init__(self, hashMap: HashMap, pageContext: PageContext) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.visual.transform.TransformFactory import TransformFactory
        self._init_fields()
        self.componentInterface = TransformFactory.getInstance().getInstance(self.abeClientInformation, hashMap, pageContext)
    

    def getTypeId(self) -> int:
        return self.NO_TYPE
    

    # throws Exception
    def view(self) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            return self.componentInterface.view()
        except Exception as e:
            error: str = "Failed to View: "
            if self.componentInterface is not None:
                error += str(type(self.componentInterface).__module__ + "." + type(self.componentInterface).__qualname__)
            else:
                error += "Unknown"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
    

    # throws Exception
    def toXmlDoc(self) -> Document:
        from org.w3c.dom.Document import Document
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            raise Exception("Hmm: " + str(self.componentInterface.getTransformDocumentInterface().getDoc()))
        except Exception as e:
            error: str = "Failed to View: "
            if self.componentInterface is not None:
                error += str(type(self.componentInterface).__module__ + "." + type(self.componentInterface).__qualname__)
            else:
                error += "Unknown"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
    

    def getViewObject(self) -> TransformInterface:
        return self.componentInterface
    

    # throws Exception
    def getTransformInfoInterface(self) -> TransformInfoInterface:
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        return self.componentInterface.getTransformInfoInterface()
    

    def getTransformDocumentInterface(self) -> TransformDocumentInterface:
        from org.allbinary.logic.visual.transform.data.TransformDocumentInterface import TransformDocumentInterface
        return None
    

    def setTransformDocumentInterface(self, viewDocumentInterface: TransformDocumentInterface) -> None:
        from org.allbinary.logic.visual.transform.data.TransformDocumentInterface import TransformDocumentInterface
        return
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory
# from org.allbinary.logic.visual.transform.TransformFactory import TransformFactory
# from org.allbinary.logic.visual.transform.data.TransformDocumentInterface import TransformDocumentInterface
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Document import Document
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


