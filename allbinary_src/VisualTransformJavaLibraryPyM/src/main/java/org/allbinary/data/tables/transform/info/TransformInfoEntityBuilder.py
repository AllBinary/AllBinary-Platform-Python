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



class TransformInfoEntityBuilder:
    

    @staticmethod
    def getInstance() -> TransformInfoEntity:
        from org.allbinary.data.tables.transform.info.TransformInfoEntityFactory import TransformInfoEntityFactory
        return TransformInfoEntityFactory.getInstance(TransformInfoObjectConfigGeneratorFactory.getInstance(), TransformInfoObjectConfigAndManipulatorFactory.getInstance(), TransformInfoHttpStoreFactory.getInstance())
from org.allbinary.logic.visual.transform.info.TransformInfoHttpStoreFactory import TransformInfoHttpStoreFactory
from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigAndManipulatorFactory import TransformInfoObjectConfigAndManipulatorFactory
from org.allbinary.logic.visual.transform.info.objectConfig.generator.TransformInfoObjectConfigGeneratorFactory import TransformInfoObjectConfigGeneratorFactory


