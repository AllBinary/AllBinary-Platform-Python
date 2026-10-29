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



class TransformInfoObjectConfigNoManipulationFactory:
    instance: TransformInfoObjectConfigNoManipulationFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> TransformInfoObjectConfigNoManipulationFactory:
        return TransformInfoObjectConfigNoManipulationFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, transformInfoInterface: TransformInfoInterface, objectConfigFileAbPath: AbPath) -> TransformInfoObjectConfigInterface:
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfig import TransformInfoObjectConfig
        try:
            transformInfoObjectConfigData: TransformInfoObjectConfigData = TransformInfoObjectConfigData.getInstance()
            data: str = CryptFileReader(transformInfoObjectConfigData.UNCRYPTED_EXTENSION, transformInfoObjectConfigData.getInstance().ENCRYPTED_EXTENSION).get(objectConfigFileAbPath)
            return TransformInfoObjectConfig(transformInfoInterface, DomDocumentHelper.create(data))
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Could Not Load Object Config", self, commonStrings.GET_INSTANCE, e)
            raise e
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.string.CommonStrings import CommonStrings


TransformInfoObjectConfigNoManipulationFactory.instance = TransformInfoObjectConfigNoManipulationFactory()

