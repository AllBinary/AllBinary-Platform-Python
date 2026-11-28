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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


@java_inherited_overloads
class GeneratorStoreFrontContextView(HttpStoreComponentView):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__(transformInfoInterface)
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("View Name: " + transformInfoInterface.getName(), self, self.commonStrings.CONSTRUCTOR)
    

    # throws Exception
    def view_j1(self, group: str) -> str:
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.visual.transform.generator.TransformsGeneratorUtil import TransformsGeneratorUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        result: str = TransformsGeneratorUtil.getInstance().generateComponentsFromObjectConfig(self.abeClientInformation, self.getTransformInfoInterface(), group)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPEXTRAOUTPUT):
            return result
        else:
            return StringUtil.getInstance().EMPTY_STRING
    

    # throws Exception
    def view_j0(self) -> str:
        from org.allbinary.logic.visual.transform.info.TransformInfosData import TransformInfosData
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            return self.view(TransformInfosData.getInstance().ALL)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e

    def view(self, *args):
        implementation = __class__.__dict__.get("view_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().view(*args)
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.visual.transform.generator.TransformsGeneratorUtil import TransformsGeneratorUtil
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.logic.visual.transform.info.TransformInfosData import TransformInfosData
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


