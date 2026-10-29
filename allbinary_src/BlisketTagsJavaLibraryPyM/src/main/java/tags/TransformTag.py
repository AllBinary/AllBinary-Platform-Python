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
# package tags

from __future__ import annotations

from tags.transform.info.TransformInfoTag import TransformInfoTag


class TransformTag(TransformInfoTag):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        super().__init__(ViewHelperFactory())
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
    

    def _constructor1(self, tagHelperFactoryInterface: TagHelperFactoryInterface) -> None:
        super().__init__(tagHelperFactoryInterface)
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
    

    # throws Exception
    def view(self) -> str:
        try:
            result: str = type(self.getHelper()).getMethod("view", None).invoke(self.getHelper(), None)
            return result
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                self.logUtil.putF("Creating with: \n" + str(self.getPropertiesHashMap()), self, self.tagStrings.DO_START_TAG)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("ViewTag Start For: ")
                stringBuffer.append(self.getName())
                stringBuffer.append("\nViewFile: ")
                stringBuffer.append(self.getObjectFile())
                self.logUtil.putF(str(stringBuffer), self, self.tagStrings.DO_START_TAG)
            self.setHelper()
            self.pageContext.getOut().print_(self.view())
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                self.logUtil.putF("Tag End", self, self.tagStrings.DO_START_TAG)
            return self.SKIP_BODY
        except LicensingException as e:
            AbResponseHandler.sendJspTagLicensingRedirect(self.pageContext, e)
            return self.SKIP_BODY
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from javax.servlet.jsp.JspTagException import JspTagException
from admin.taghelpers.TagHelperFactoryInterface import TagHelperFactoryInterface
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
from taghelpers.ViewHelperFactory import ViewHelperFactory


