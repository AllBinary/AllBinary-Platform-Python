# Generated Code Do Not Modify
# package org.apache.xmlrpc

from __future__ import annotations

from org.apache.xmlrpc.XmlRpcHandler import XmlRpcHandler


class XmlRpcClient(XmlRpcHandler):

    def _init_fields(self) -> None:
        self.url: URL = None
    

    def __init__(self, url: str) -> None:
        self._init_fields()
        self.url = URL(url)
    

    def getURL(self) -> URL:
        return self.url
    

    def setBasicAuthentication(self, user: str, password: str) -> None:
        pass
    

    # throws XmlRpcException, IOException
    def execute(self, method: str, params: BasicArrayList) -> object:
        return NullUtil.getInstance().NULL_OBJECT
    

    # throws XmlRpcException, IOException
    # Java overloaded method: Python keeps the last definition
    def execute(self, method: str, params: BasicArrayList, cryptInterface: CryptInterface) -> object:
        return NullUtil.getInstance().NULL_OBJECT
# from java.io.IOException import IOException
# from java.net.MalformedURLException import MalformedURLException
# from java.net.URL import URL
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.init.crypt.jcehelper.CryptInterface import CryptInterface
from org.allbinary.logic.NullUtil import NullUtil


