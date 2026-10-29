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
# package views.generic.advertisement.area

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


class AdvertisementAreaView(HttpStoreComponentView, DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.advertisementAreaName: str = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        self.advertisementAreaName = self.getPropertiesHashMap().get(AdvertisementAreaData.getInstance().NAME)
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        try:
            advertisementAreasEntityInterface: AdvertisementAreasEntityInterface = AdvertisementAreasEntityFactory.getInstance()
            advertisementAreaInterface: AdvertisementAreaInterface = advertisementAreasEntityInterface.get(self.getTransformInfoInterface().getStoreName(), self.advertisementAreaName)
            return None
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().XSLLOGGINGERROR):
                self.logUtil.put(self.commonStrings.FAILURE, self, "toXmlNode", e)
            raise e
    

    def addDomNodeInterfaces(self) -> None:
        self.addDomNodeInterface(self)
    

    # throws Exception
    def view(self) -> str:
        try:
            self.addDomNodeInterfaces()
            return super().view()
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
from org.allbinary.business.advertisement.area.AdvertisementAreaData import AdvertisementAreaData
from org.allbinary.business.advertisement.area.AdvertisementAreaInterface import AdvertisementAreaInterface
from org.allbinary.data.tables.advertisement.areas.AdvertisementAreasEntityFactory import AdvertisementAreasEntityFactory
from org.allbinary.data.tables.advertisement.areas.AdvertisementAreasEntityInterface import AdvertisementAreasEntityInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


