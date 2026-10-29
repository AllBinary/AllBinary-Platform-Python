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
# package views.business.context.modules.storefront.generator

from __future__ import annotations

from views.business.context.modules.storefront.generator.GeneratorStoreFrontContextView import GeneratorStoreFrontContextView


class PreviewGeneratorStoreFrontContextView(GeneratorStoreFrontContextView):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
    

    # throws Exception
    def view(self) -> str:
        try:
            httpTransformInfoInterface: TransformInfoHttpInterface = self.getTransformInfoInterface()
            httpTransformInfoInterface.getPropertiesHashMap().put(TransformInfoData.getInstance().PARTIAL, CommonSeps.getInstance().SPACE + TransformInfosData.getInstance().PREVIEW)
            return self.view(TransformInfosData.getInstance().PREVIEW)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.logic.visual.transform.info.TransformInfosData import TransformInfosData
from org.allbinary.string.CommonSeps import CommonSeps


