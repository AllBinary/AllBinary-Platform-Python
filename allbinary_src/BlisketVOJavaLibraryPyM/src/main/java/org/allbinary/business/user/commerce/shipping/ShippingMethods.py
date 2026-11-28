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
# package org.allbinary.business.user.commerce.shipping

from __future__ import annotations

from org.allbinary.business.user.commerce.shipping.ShippingMethodsInterface import ShippingMethodsInterface


class ShippingMethods(ShippingMethodsInterface):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "shippingVector" not in vars(self): self.shippingVector: BasicArrayList = None
        if "defaultShippingMethodInterface" not in vars(self): self.defaultShippingMethodInterface: ShippingInterface = None
    

    def __init__(self, abeClientInformation: AbeClientInformationInterface, storeFrontInterface: StoreFrontInterface) -> None:
        from org.allbinary.business.user.commerce.shipping.ShippingMethodsFactory import ShippingMethodsFactory
        from org.allbinary.business.user.commerce.shipping.ShippingMethodsFactory import ShippingMethodsFactory
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        __class__._init_fields(self)
        self.defaultShippingMethodInterface = ShippingMethodsFactory(abeClientInformation, storeFrontInterface).getDefaultInstance()
        self.shippingVector = ShippingMethodsFactory(abeClientInformation, storeFrontInterface).getInstance()
    

    def get(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.shippingVector
    

    # throws Exception
    def getShippingInterface(self, name: str) -> ShippingInterface:
        from org.allbinary.business.user.commerce.shipping.modules.ShippingInterface import ShippingInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        shipping: ShippingInterface = None
        size: int = self.shippingVector.size()
        for index in range(0, size):
            shipping = self.shippingVector.get(index)
            if ((name > shipping.getName()) - (name < shipping.getName())) == 0:
                return shipping
        error: str = "Error Finding Shipping: " + name
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SHIPPINGERROR):
            self.logUtil.putF(self.commonStrings.EXCEPTION, self, "getShippingInterface(String name)")
        raise Exception(error)
    

    # throws Exception
    def getDefault(self) -> ShippingInterface:
        from org.allbinary.business.user.commerce.shipping.modules.ShippingInterface import ShippingInterface
        return self.defaultShippingMethodInterface
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.business.user.commerce.shipping.modules.ShippingInterface import ShippingInterface
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


