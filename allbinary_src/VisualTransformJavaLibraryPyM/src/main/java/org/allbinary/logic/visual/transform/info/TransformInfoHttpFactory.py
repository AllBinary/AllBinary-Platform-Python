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



class TransformInfoHttpFactory:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getInstance(propertiesHashMap: HashMap, pageContext: PageContext) -> TransformInfoInterface:
        from org.allbinary.logic.visual.transform.info.TransformInfoHttpContext import TransformInfoHttpContext
        from org.allbinary.logic.visual.transform.info.TransformInfoHttpStore import TransformInfoHttpStore
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            weblisketSession: WeblisketSession = WeblisketSession(propertiesHashMap, pageContext)
            if not StringValidationUtil.getInstance().isEmpty(weblisketSession.getStoreName()):
                storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(weblisketSession.getStoreName())
                if storeFrontInterface is not None:
                    return TransformInfoHttpStore(storeFrontInterface, propertiesHashMap, pageContext)
                else:
                    raise Exception("No StoreFront with: " + str(weblisketSession.getStoreName()))
            else:
                return TransformInfoHttpContext(propertiesHashMap, pageContext)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil.put(commonStrings.EXCEPTION, "TransformInfoFactory", commonStrings.GET_INSTANCE, e)
            raise e
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


