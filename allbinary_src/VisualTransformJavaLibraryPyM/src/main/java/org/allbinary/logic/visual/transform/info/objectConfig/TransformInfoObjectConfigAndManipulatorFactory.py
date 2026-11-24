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
# package org.allbinary.logic.visual.transform.info.objectConfig

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigAndManipulatorFactoryBase import TransformInfoObjectConfigAndManipulatorFactoryBase


class TransformInfoObjectConfigAndManipulatorFactory(TransformInfoObjectConfigAndManipulatorFactoryBase):
    instance: TransformInfoObjectConfigAndManipulatorFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance_j0() -> TransformInfoObjectConfigAndManipulatorFactory:
        return TransformInfoObjectConfigAndManipulatorFactory.instance
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j3_1(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface, objectConfigFileAbPath: AbPath) -> TransformInfoObjectConfigInterface:
        from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
        from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            data: str = CryptFileReader(TransformInfoObjectConfigData.getInstance().UNCRYPTED_EXTENSION, TransformInfoObjectConfigData.getInstance().ENCRYPTED_EXTENSION).get(objectConfigFileAbPath)
            return self.getInstance(abeClientInformation, transformInfoInterface, DomDocumentHelper.create(data))
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Could Not Load Object Config", TransformInfoObjectConfigAndManipulatorFactory.getInstance(), self.commonStrings.GET_INSTANCE, e)
            raise e
    

    # throws Exception
    def getInstance_j2(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface) -> TransformInfoObjectConfigInterface:
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfig import TransformInfoObjectConfig
        from org.allbinary.logic.visual.transform.info.objectConfig.GenericStoreTransformInfoObjectConfig import GenericStoreTransformInfoObjectConfig
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
            if transformInfoInterface is not None and not stringValidationUtil.isEmpty(transformInfoInterface.getStoreName()):
                return GenericStoreTransformInfoObjectConfig(abeClientInformation, transformInfoInterface)
            else:
                return TransformInfoObjectConfig(transformInfoInterface)
        except Exception as e:
            error: str = "Failed To Get Instance: "
            if transformInfoInterface is not None:
                error = error + transformInfoInterface.getName()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, TransformInfoObjectConfigAndManipulatorFactory.getInstance(), self.commonStrings.GET_INSTANCE, e)
            raise e
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j3_2(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface, document: Document) -> TransformInfoObjectConfigInterface:
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfig import TransformInfoObjectConfig
        from org.allbinary.logic.visual.transform.info.objectConfig.GenericStoreTransformInfoObjectConfig import GenericStoreTransformInfoObjectConfig
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.w3c.dom.Document import Document
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
            if transformInfoInterface is not None and not stringValidationUtil.isEmpty(transformInfoInterface.getStoreName()):
                return GenericStoreTransformInfoObjectConfig(abeClientInformation, transformInfoInterface, document)
            else:
                return TransformInfoObjectConfig(transformInfoInterface, document)
        except Exception as e:
            error: str = "Failed To Get Instance: "
            if transformInfoInterface is not None:
                error = error + transformInfoInterface.getName()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, TransformInfoObjectConfigAndManipulatorFactory.getInstance(), "getInstance(document)", e)
            raise e

    def getInstance(self, *args):
        if len(args) == 3 and True and not isinstance(args[0], (str, list, int, float)) and not isinstance(args[1], (str, list, int, float)) and not isinstance(args[2], (str, list, int, float)):
            return self.getInstance_j3_1(*args)
        if len(args) == 3:
            return self.getInstance_j3_2(*args)
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
# from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.w3c.dom.Document import Document
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _TransformInfoObjectConfigAndManipulatorFactory_instance() -> object:
    return TransformInfoObjectConfigAndManipulatorFactory()

lazy_static(TransformInfoObjectConfigAndManipulatorFactory, "instance", _TransformInfoObjectConfigAndManipulatorFactory_instance)

