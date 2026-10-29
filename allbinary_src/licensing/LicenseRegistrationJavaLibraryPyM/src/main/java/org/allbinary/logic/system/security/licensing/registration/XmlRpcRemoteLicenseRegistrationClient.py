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
# package org.allbinary.logic.system.security.licensing.registration

from __future__ import annotations

from org.allbinary.logic.communication.xmlrpc.XmlRpcAbeClient import XmlRpcAbeClient


class XmlRpcRemoteLicenseRegistrationClient(XmlRpcAbeClient):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.PAGE: str = "licenseregistrationserverssl.php"
    

    def __init__(self, clientInfo: AbeClientInformationInterface) -> None:
        super().__init__(clientInfo, "LicenseRegistrationServer.process")
        self._init_fields()
        self.setServer(0)
    

    # throws Exception
    def get(self, anyType: object, cryptInterface: CryptInterface) -> object:
        try:
            server: str = self.getClientInfo().getLicenseServer(self.getServer())
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(self.TRYING)
            stringBuffer.appendint(int(self.getServer()))
            stringBuffer.append(SEP)
            stringBuffer.append(server)
            self.logUtil.putF(str(CommonLabels.getInstance().START_LABEL) + str(stringBuffer), self, self.commonStrings.GET)
            param: BasicArrayList = BasicArrayListD()
            serverUrl: str = self.getClientInfo().getLicenseServer(self.getServer())
            index: int = serverUrl.rfind("/")
            serverUrl = serverUrl[0:index + 1] + self.PAGE
            xmlRpcClient: XmlRpcClient = XmlRpcClient(serverUrl)
            self.setClient(xmlRpcClient)
            xmlRpcClient.setBasicAuthentication(None, None)
            hashtable: ABHashtable[object, object] = anyType
            self.logUtil.putF(str(self.CLIENT_INFO) + str(hashtable), self, self.commonStrings.GET)
            param.add(hashtable)
            result: object = xmlRpcClient.execute(self.getRemoteMethod(), param, cryptInterface)
            self.logUtil.putF(str(self.RESULT) + str(result), self, self.commonStrings.GET)
            self.isOnline = True
            return result
        except OSError as e:
            self.logUtil.putF(self.TRYING_OTHER_SERVERS + ExceptionUtil.getInstance().getStackTrace(e), self, self.commonStrings.GET)
            if not str(e).startsWith(self.HOST_NOT_RESOLVED):
                return self.tryAnother(anyType)
            else:
                raise Exception(self.HOST_NOT_RESOLVED_MSG)
        except XmlRpcException as e:
            self.logUtil.put(self.SERVER_REPORTED_ERROR, self, self.commonStrings.GET, e)
            return self.tryAnother(anyType)
        except Exception as e:
            self.logUtil.put(self.UNKNOWN_ERROR, self, self.commonStrings.GET, e)
            return self.tryAnother(anyType)
# from java.io.IOException import IOException
from org.apache.xmlrpc.XmlRpcClient import XmlRpcClient
from org.apache.xmlrpc.XmlRpcException import XmlRpcException
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.init.crypt.jcehelper.CryptInterface import CryptInterface
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.java.exception.ExceptionUtil import ExceptionUtil
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.util.ABHashtable import ABHashtable


