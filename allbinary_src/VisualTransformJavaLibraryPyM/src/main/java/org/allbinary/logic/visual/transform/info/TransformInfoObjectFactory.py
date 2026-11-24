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

from java.lang.JavaRuntimeStatic import lazy_static


class TransformInfoObjectFactory:
    instance: TransformInfoObjectFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance_j0() -> TransformInfoObjectFactory:
        return TransformInfoObjectFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def getInstance_j2(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface) -> TransformInterface:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.system.loader.AbeFactory import AbeFactory
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.visual.transform.TransformInterface import TransformInterface
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.putF("Creating View: " + transformInfoInterface.getName(), self, commonStrings.GET_INSTANCE)
            params: list[object] = [None] * (1)
            classes: list[type] = [None] * (1)
            classes[0] = TransformInfoInterface
            params[0] = transformInfoInterface
            anyType: TransformInterface = AbeFactory.getInstance().getInstance(abeClientInformation, transformInfoInterface.getObjectFile(), classes, params)
            if anyType is None:
                if transformInfoInterface is not None:
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append("\nNo Such View Name: ")
                    stringBuffer.append(transformInfoInterface.getName())
                    stringBuffer.append("\nNo Such View Object: ")
                    stringBuffer.append(transformInfoInterface.getObjectFile())
                    raise Exception(str(stringBuffer))
                else:
                    raise Exception("No Such View Object since transformInfo is null")
            return anyType
        except LicensingException as e:
            error: str = "Failed To Get Instance: "
            if transformInfoInterface is not None:
                error = error + transformInfoInterface.getName()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(error, self, commonStrings.GET_INSTANCE, e)
            raise e
        except Exception as e:
            error: str = "Failed To Get Instance: "
            if transformInfoInterface is not None:
                error = error + transformInfoInterface.getName()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(error, self, commonStrings.GET_INSTANCE, e)
            raise e

    def getInstance(self, *args):
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.system.loader.AbeFactory import AbeFactory
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
# from org.allbinary.logic.visual.transform.TransformInterface import TransformInterface
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _TransformInfoObjectFactory_instance() -> object:
    return TransformInfoObjectFactory()

lazy_static(TransformInfoObjectFactory, "instance", _TransformInfoObjectFactory_instance)

