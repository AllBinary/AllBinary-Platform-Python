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
# package views.admin.storefront.statistics

from __future__ import annotations

from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


class StoreFrontStatisticsComponent(HttpStoreComponentView):

    def _init_fields(self) -> None:
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.newStoreFrontInterface: StoreFrontInterface = None
        self.domNodeInterface: DomNodeInterface = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.allbinary.business.context.modules.storefront.statistics.RealTimeStoreFrontStatistics import RealTimeStoreFrontStatistics
        from org.allbinary.business.context.modules.storefront.statistics.RealTimeStoreFrontStatisticsView import RealTimeStoreFrontStatisticsView
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        super().__init__(transformInfoInterface)
        self._init_fields()
        self.newStoreFrontInterface = StoreFrontFactory.getInstance(transformInfoInterface.getStoreName())
        self.domNodeInterface = RealTimeStoreFrontStatisticsView(RealTimeStoreFrontStatistics(self.newStoreFrontInterface), self.getWeblisketSession().getRole())
    

    def addDomNodeInterfaces(self) -> None:
        from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
        self.addDomNodeInterface(self.domNodeInterface)
    

    # throws Exception
    def view(self) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            self.addDomNodeInterfaces()
            return super().view()
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
# from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.business.context.modules.storefront.statistics.RealTimeStoreFrontStatistics import RealTimeStoreFrontStatistics
# from org.allbinary.business.context.modules.storefront.statistics.RealTimeStoreFrontStatisticsView import RealTimeStoreFrontStatisticsView
# from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


