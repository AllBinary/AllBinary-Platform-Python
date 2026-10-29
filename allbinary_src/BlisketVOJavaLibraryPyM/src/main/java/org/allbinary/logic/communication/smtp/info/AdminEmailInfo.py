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


class AdminEmailInfo(BasicEmailInfo):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, subject: str, textBody: str) -> None:
        super().__init__(subject, textBody)
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF(commonStrings.START, self, commonStrings.CONSTRUCTOR)
        self.init()
    

    # throws Exception
    def init(self) -> None:
        adminConfigurationInterface: AdminConfigurationInterface = AdminConfiguration()
        contextConfigurationInterface: ContextConfigurationInterface = adminConfigurationInterface.getContextConfigurationInterface()
        emailServerConfigurationInterface: EmailServerConfigurationInterface = contextConfigurationInterface.getEmailServerConfigurationInterface()
        self.setEmailServerConfigurationInterface(emailServerConfigurationInterface)
from org.allbinary.business.context.configuration.ContextConfigurationInterface import ContextConfigurationInterface
from org.allbinary.business.user.modules.admin.configuration.AdminConfiguration import AdminConfiguration
from org.allbinary.business.user.modules.admin.configuration.AdminConfigurationInterface import AdminConfigurationInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationInterface import EmailServerConfigurationInterface
from org.allbinary.string.CommonStrings import CommonStrings


