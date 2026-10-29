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
# package org.allbinary.data.tables.transform.info

from __future__ import annotations



class TransformInfoEntityFactory:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getInstance(transformInfoObjectConfigGeneratorFactoryInterface: TransformInfoObjectConfigGeneratorFactoryInterface, transformInfoObjectConfigAndManipulatorFactoryInterface: TransformInfoObjectConfigAndManipulatorFactoryBase, transformInfoFactoryInterface: TransformInfoFactoryInterface) -> TransformInfoEntity:
        from org.allbinary.data.tables.transform.info.TransformInfoEntity import TransformInfoEntity
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            return TransformInfoEntity(transformInfoObjectConfigGeneratorFactoryInterface, transformInfoObjectConfigAndManipulatorFactoryInterface, transformInfoFactoryInterface)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                logUtil.put(commonStrings.EXCEPTION, "TransformInfoEntityFactory", commonStrings.GET_INSTANCE, e)
            return None
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.visual.transform.info.TransformInfoFactoryInterface import TransformInfoFactoryInterface
from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigAndManipulatorFactoryBase import TransformInfoObjectConfigAndManipulatorFactoryBase
from org.allbinary.logic.visual.transform.info.objectConfig.generator.TransformInfoObjectConfigGeneratorFactoryInterface import TransformInfoObjectConfigGeneratorFactoryInterface
from org.allbinary.string.CommonStrings import CommonStrings


