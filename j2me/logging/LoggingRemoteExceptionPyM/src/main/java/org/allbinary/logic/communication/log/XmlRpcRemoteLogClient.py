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
# package org.allbinary.logic.communication.log

from __future__ import annotations

from org.allbinary.logic.communication.xmlrpc.XmlRpcAbeClient import XmlRpcAbeClient


class XmlRpcRemoteLogClient(XmlRpcAbeClient):

    def _init_fields(self) -> None:
        self.noCrypt: NoCrypt = NoCrypt()
    

    def __init__(self, clientInfo: AbeClientInformationInterface) -> None:
        super().__init__(clientInfo, "SSLLogServ.logUtil")
        self._init_fields()
    

    # throws Exception
    def get(self, anyType: object) -> object:
        try:
            param: BasicArrayList = BasicArrayListD()
            serverUrl: str = self.getClientInfo().getLicenseServer(self.getServer())
            index: int = serverUrl.rfind("/")
            serverUrl = serverUrl[0:index + 1] + "logservssl.php"
            xmlRpcClient: XmlRpcClient = XmlRpcClient(serverUrl)
            self.setClient(xmlRpcClient)
            xmlRpcClient.setBasicAuthentication(None, None)
            hashtable: ABHashtable[object, object] = anyType
            param.add(hashtable)
            result: object = xmlRpcClient.execute(self.getRemoteMethod(), param, self.noCrypt)
            print(str(CommonLabels.getInstance().RESULT_ + CommonSeps.getInstance().NEW_LINE) + str(result))
            return result
        except OSError as e:
            print("IOException Trying Other Servers")
            if not str(e).startsWith(self.HOST_NOT_RESOLVED):
                return self.tryAnother(anyType)
            else:
                raise Exception(self.HOST_NOT_RESOLVED_MSG)
        except XmlRpcException as e:
            return self.tryAnother(anyType)
        except Exception as e:
            return self.tryAnother(anyType)
# from java.io.IOException import IOException
from org.apache.xmlrpc.XmlRpcClient import XmlRpcClient
from org.apache.xmlrpc.XmlRpcException import XmlRpcException
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.system.security.crypt.jcehelper.NoCrypt import NoCrypt
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.util.ABHashtable import ABHashtable


