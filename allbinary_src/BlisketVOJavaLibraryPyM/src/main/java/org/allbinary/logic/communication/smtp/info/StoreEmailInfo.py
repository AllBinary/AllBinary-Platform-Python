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
# package org.allbinary.logic.communication.smtp.info

from __future__ import annotations

from org.allbinary.logic.communication.smtp.info.BasicEmailInfo import BasicEmailInfo


class StoreEmailInfo(BasicEmailInfo):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.storeFrontInterface: StoreFrontInterface = None
    

    def __init__(self, storeFrontInterface: StoreFrontInterface, subject: str, textBody: str) -> None:
        super().__init__(subject, textBody)
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF(commonStrings.START, self, commonStrings.CONSTRUCTOR)
        self.storeFrontInterface = storeFrontInterface
        self.init()
    

    # throws Exception
    def init(self) -> None:
        contextConfigurationInterface: ContextConfigurationInterface = self.storeFrontInterface.getContextConfigurationInterface()
        emailServerConfigurationInterface: EmailServerConfigurationInterface = contextConfigurationInterface.getEmailServerConfigurationInterface()
        self.setEmailServerConfigurationInterface(emailServerConfigurationInterface)
from org.allbinary.business.context.configuration.ContextConfigurationInterface import ContextConfigurationInterface
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationInterface import EmailServerConfigurationInterface
from org.allbinary.string.CommonStrings import CommonStrings


