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
# package views.compound

from __future__ import annotations

from org.allbinary.logic.visual.transform.AbTransformer import AbTransformer


class CompoundTransform(AbTransformer):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        self.setURIResolver(StoreUriResolver(self.getTransformInfoInterface(), self.getURIResolver()))
        objectConfig: CompoundContextTransformInfoObjectConfig = CompoundContextTransformInfoObjectConfig(self.abeClientInformation, self.getTransformInfoInterface(), self.getTransformInfoInterface().getObjectConfigInterface().toXmlDoc())
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("\nObjectConfig: \n" + str(objectConfig), self, self.commonStrings.CONSTRUCTOR)
        templateInputStream: InputStream = objectConfig.createInputStream()
        self.setInputStream(templateInputStream)
# from java.io.InputStream import InputStream
# from javax.xml.transform.URIResolver import URIResolver
from org.allbinary.data.tree.dom.BasicUriResolver import BasicUriResolver
from org.allbinary.data.tree.dom.StoreUriResolver import StoreUriResolver
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from views.compound.objectConfig.CompoundContextTransformInfoObjectConfig import CompoundContextTransformInfoObjectConfig


