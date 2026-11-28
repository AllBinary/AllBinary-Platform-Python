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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigAndManipulatorFactoryBase import TransformInfoObjectConfigAndManipulatorFactoryBase


@java_inherited_overloads
class TransformInfoObjectConfigAndManipulatorFactory(TransformInfoObjectConfigAndManipulatorFactoryBase):
    instance: TransformInfoObjectConfigAndManipulatorFactory = None
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance_j0() -> TransformInfoObjectConfigAndManipulatorFactory:
        return TransformInfoObjectConfigAndManipulatorFactory.instance
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j3_1(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface, objectConfigFileAbPath: AbPath) -> TransformInfoObjectConfigInterface:
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
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
                self.logUtil.put("Could Not Load Object Config", TransformInfoObjectConfigAndManipulatorFactory.getInstance_j0()
            , self.commonStrings.GET_INSTANCE, e)
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
            if transformInfoInterface is not None and not (stringValidationUtil.isEmpty(transformInfoInterface.getStoreName())):
                return GenericStoreTransformInfoObjectConfig(abeClientInformation, transformInfoInterface)
            else:
                return TransformInfoObjectConfig(transformInfoInterface)
        except Exception as e:
            error: str = "Failed To Get Instance: "
            if transformInfoInterface is not None:
                error = error + transformInfoInterface.getName()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, TransformInfoObjectConfigAndManipulatorFactory.getInstance_j0()
            , self.commonStrings.GET_INSTANCE, e)
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
            if transformInfoInterface is not None and not (stringValidationUtil.isEmpty(transformInfoInterface.getStoreName())):
                return GenericStoreTransformInfoObjectConfig(abeClientInformation, transformInfoInterface, document)
            else:
                return TransformInfoObjectConfig(transformInfoInterface, document)
        except Exception as e:
            error: str = "Failed To Get Instance: "
            if transformInfoInterface is not None:
                error = error + transformInfoInterface.getName()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, TransformInfoObjectConfigAndManipulatorFactory.getInstance_j0()
            , "getInstance(document)", e)
            raise e

    def getInstance(self=None, *args):
        if self is None and not args: return __class__.getInstance_j0()
        if len(args) == 3 and True and (args[0] is None or any(base.__name__ == "AbeClientInformationInterface" for base in type(args[0]).__mro__)) and (args[1] is None or any(base.__name__ == "TransformInfoInterface" for base in type(args[1]).__mro__)) and (args[2] is None or any(base.__name__ == "AbPath" for base in type(args[2]).__mro__)):
            return __class__.__dict__["getInstance_j3_1"].__get__(self, __class__)(*args)
        if len(args) == 3:
            return __class__.__dict__["getInstance_j3_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("getInstance_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getInstance(*args)
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

