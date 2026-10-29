# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.logic.communication.log.config.type

from __future__ import annotations



class LogConfigTypeFactory:
    instance: LogConfigTypeFactory = None

    def _init_fields(self) -> None:
        self.NO_DESCRIPTION: str = "No Description"
        self.AUTHENTICATION: LogConfigType = LogConfigType("Authentication", self.NO_DESCRIPTION)
        self.AUTHENTICATIONERROR: LogConfigType = LogConfigType("Authentication Error", self.NO_DESCRIPTION)
        self.CATEGORY: LogConfigType = LogConfigType("Category", self.NO_DESCRIPTION)
        self.CATEGORYERROR: LogConfigType = LogConfigType("Category Error", self.NO_DESCRIPTION)
        self.CRYPT: LogConfigType = LogConfigType("Crypt", self.NO_DESCRIPTION)
        self.CRYPTERROR: LogConfigType = LogConfigType("Crypt Error", self.NO_DESCRIPTION)
        self.EMAILLOGGING: LogConfigType = LogConfigType("Email", self.NO_DESCRIPTION)
        self.EMAILLOGGINGERROR: LogConfigType = LogConfigType("Email Error", self.NO_DESCRIPTION)
        self.ENTITYFACTORYERROR: LogConfigType = LogConfigType("Entity Factory Error", self.NO_DESCRIPTION)
        self.NETBEANS_MODULE: LogConfigType = LogConfigType("NetBeans Module", self.NO_DESCRIPTION)
        self.NETBEANS_MODULE_ERROR: LogConfigType = LogConfigType("NetBeans Module Error", self.NO_DESCRIPTION)
        self.FACTORYERROR: LogConfigType = LogConfigType("General Factory Error", self.NO_DESCRIPTION)
        self.FILE: LogConfigType = LogConfigType("File", self.NO_DESCRIPTION)
        self.FILEERROR: LogConfigType = LogConfigType("File Error", self.NO_DESCRIPTION)
        self.HTTP: LogConfigType = LogConfigType("HTTP", self.NO_DESCRIPTION)
        self.HTTPERROR: LogConfigType = LogConfigType("HTTP Error", self.NO_DESCRIPTION)
        self.HTTPREQUEST: LogConfigType = LogConfigType("Http Request", self.NO_DESCRIPTION)
        self.HTTPREQUESTERROR: LogConfigType = LogConfigType("Http Request Error", self.NO_DESCRIPTION)
        self.IDLOGGING: LogConfigType = LogConfigType("ID Logging", self.NO_DESCRIPTION)
        self.JSPEXTRAOUTPUT: LogConfigType = LogConfigType("JSP Extra Output", self.NO_DESCRIPTION)
        self.JSPTAGEXTRAOUTPUT: LogConfigType = LogConfigType("JSP Tag Extra Output", self.NO_DESCRIPTION)
        self.JSPTAG: LogConfigType = LogConfigType("JSP Tag", self.NO_DESCRIPTION)
        self.JSPTAGERROR: LogConfigType = LogConfigType("JSP Tag Error", self.NO_DESCRIPTION)
        self.LICENSING: LogConfigType = LogConfigType("Licensing", self.NO_DESCRIPTION)
        self.LICENSINGERROR: LogConfigType = LogConfigType("Licensing Error", self.NO_DESCRIPTION)
        self.LOADER: LogConfigType = LogConfigType("Loader", self.NO_DESCRIPTION)
        self.LOADERERROR: LogConfigType = LogConfigType("Loader Error", self.NO_DESCRIPTION)
        self.OS: LogConfigType = LogConfigType("OS", self.NO_DESCRIPTION)
        self.OSERROR: LogConfigType = LogConfigType("OS Error", self.NO_DESCRIPTION)
        self.PAYMENT: LogConfigType = LogConfigType("Payment", self.NO_DESCRIPTION)
        self.PAYMENTERROR: LogConfigType = LogConfigType("Payment Error", self.NO_DESCRIPTION)
        self.PRELOADER: LogConfigType = LogConfigType("PreLoader", self.NO_DESCRIPTION)
        self.PRELOADERERROR: LogConfigType = LogConfigType("PreLoader Error", self.NO_DESCRIPTION)
        self.PRODUCTSEARCHLOGGING: LogConfigType = LogConfigType("Product Search Logging", self.NO_DESCRIPTION)
        self.PRODUCTSEARCHLOGGINGERROR: LogConfigType = LogConfigType("Product Search Logging Error", self.NO_DESCRIPTION)
        self.SERVLET: LogConfigType = LogConfigType("Servlet", self.NO_DESCRIPTION)
        self.SERVLETERROR: LogConfigType = LogConfigType("Servlet Error", self.NO_DESCRIPTION)
        self.SHIPPINGERROR: LogConfigType = LogConfigType("Shipping Error", self.NO_DESCRIPTION)
        self.SQLLOGGINGERROR: LogConfigType = LogConfigType("SQL Error", self.NO_DESCRIPTION)
        self.SQLLOGGING: LogConfigType = LogConfigType("SQL Logging", self.NO_DESCRIPTION)
        self.SQLTAGS: LogConfigType = LogConfigType("SQL Tag Logging", self.NO_DESCRIPTION)
        self.SQLTAGSERROR: LogConfigType = LogConfigType("SQL Tag Error", self.NO_DESCRIPTION)
        self.STYLE: LogConfigType = LogConfigType("Style", self.NO_DESCRIPTION)
        self.STYLEERROR: LogConfigType = LogConfigType("Style Error", self.NO_DESCRIPTION)
        self.TAGHELPER: LogConfigType = LogConfigType("Tag Helper", self.NO_DESCRIPTION)
        self.TAGHELPERERROR: LogConfigType = LogConfigType("Tag Helper Error", self.NO_DESCRIPTION)
        self.TAGHELPERFACTORY: LogConfigType = LogConfigType("Tag Helper Factory", self.NO_DESCRIPTION)
        self.TAGHELPERFACTORYERROR: LogConfigType = LogConfigType("Tag Helper Factory Error", self.NO_DESCRIPTION)
        self.TAX: LogConfigType = LogConfigType("Tax", self.NO_DESCRIPTION)
        self.TAXERROR: LogConfigType = LogConfigType("Tax Error", self.NO_DESCRIPTION)
        self.VALIDATION: LogConfigType = LogConfigType("Validation", self.NO_DESCRIPTION)
        self.VALIDATIONERROR: LogConfigType = LogConfigType("Validation Error", self.NO_DESCRIPTION)
        self.VIEW: LogConfigType = LogConfigType("View", self.NO_DESCRIPTION)
        self.VIEWERROR: LogConfigType = LogConfigType("View Error", self.NO_DESCRIPTION)
        self.VIEWFACTORYERROR: LogConfigType = LogConfigType("View Factory Error", self.NO_DESCRIPTION)
        self.WORKFLOW: LogConfigType = LogConfigType("Workflow", self.NO_DESCRIPTION)
        self.WORKFLOWERROR: LogConfigType = LogConfigType("Workflow Error", self.NO_DESCRIPTION)
        self.XMLLOGGING: LogConfigType = LogConfigType("XML Logging", self.NO_DESCRIPTION)
        self.XMLLOGGINGERROR: LogConfigType = LogConfigType("XML Logging Error", self.NO_DESCRIPTION)
        self.XSLLOGGING: LogConfigType = LogConfigType("XSL Logging", self.NO_DESCRIPTION)
        self.XSLLOGGINGERROR: LogConfigType = LogConfigType("XSL Logging Error", self.NO_DESCRIPTION)
        self.REPLACE: LogConfigType = LogConfigType("Replace", self.NO_DESCRIPTION)
        self.REPLACE_INFO: LogConfigType = LogConfigType("Replace Info", self.NO_DESCRIPTION)
        self.REPLACEERROR: LogConfigType = LogConfigType("Replace Error", self.NO_DESCRIPTION)
        self.SQLLOGGINGPOOL: LogConfigType = LogConfigType("SQL Pool", self.NO_DESCRIPTION)
        self.SQLLOGGINGPOOLERROR: LogConfigType = LogConfigType("SQL Pool Error", self.NO_DESCRIPTION)
        self.STATICPAGEGENERATIONLOGGING: LogConfigType = LogConfigType("Static Page Generation Logging", self.NO_DESCRIPTION)
        self.STATICPAGEGENERATIONLOGGINGERROR: LogConfigType = LogConfigType("Static Page Generation Logging Error", self.NO_DESCRIPTION)
    

    @staticmethod
    def getInstance() -> LogConfigTypeFactory:
        return LogConfigTypeFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
        PreLogUtil.put("FreeBlisket", self, CommonStrings.getInstance().CONSTRUCTOR)
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.config.type.LogConfigType import LogConfigType


LogConfigTypeFactory.instance = LogConfigTypeFactory()

