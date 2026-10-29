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
# package org.allbinary.business.user.address

from __future__ import annotations



class StreetAddress:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.id: str = None
        self.name: str = None
        self.street: str = None
        self.city: str = None
        self.state: str = None
        self.code: str = None
        self.country: str = None
        self.isDefault: bool = False

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 6:
            self._constructor6(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        self._init_fields()
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        self._init_fields()
        nameNode: Node = DomSearchHelper.getNode(StreetAddressData.NAME, node.getChildNodes())
        self.name = DomNodeHelper.getTextNodeValue(nameNode)
        streetNode: Node = DomSearchHelper.getNode(StreetAddressData.STREET, node.getChildNodes())
        self.street = DomNodeHelper.getTextNodeValue(streetNode)
        cityNode: Node = DomSearchHelper.getNode(StreetAddressData.CITY, node.getChildNodes())
        self.city = DomNodeHelper.getTextNodeValue(cityNode)
        stateNode: Node = DomSearchHelper.getNode(StreetAddressData.STATE, node.getChildNodes())
        self.state = DomNodeHelper.getTextNodeValue(stateNode)
        codeNode: Node = DomSearchHelper.getNode(StreetAddressData.CODE, node.getChildNodes())
        self.code = DomNodeHelper.getTextNodeValue(codeNode)
        countryNode: Node = DomSearchHelper.getNode(StreetAddressData.COUNTRY, node.getChildNodes())
        self.country = DomNodeHelper.getTextNodeValue(countryNode)
        self.log()
    

    def _constructor1(self, streetAddress: StreetAddress) -> None:
        self._init_fields()
        self.id = streetAddress.getId()
        self.name = streetAddress.getName()
        self.street = streetAddress.getStreet()
        self.city = streetAddress.getCity()
        self.state = streetAddress.getState()
        self.code = streetAddress.getCode()
        self.country = streetAddress.getCountry()
        self.isDefault = streetAddress.isDefault()
        self.log()
    

    def _constructor1(self, request: HttpServletRequest) -> None:
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        self._init_fields()
        self.setId(request.getParameter(StreetAddressData.ID))
        self.setName(request.getParameter(StreetAddressData.NAME))
        self.setStreet(request.getParameter(StreetAddressData.STREET))
        self.setCity(request.getParameter(StreetAddressData.CITY))
        self.setState(request.getParameter(StreetAddressData.STATE))
        self.setCode(request.getParameter(StreetAddressData.CODE))
        self.setCountry(request.getParameter(StreetAddressData.COUNTRY))
        self.log()
    

    def _constructor6(self, name: str, street: str, city: str, state: str, code: str, country: str) -> None:
        self._init_fields()
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.code = code
        self.country = country
        self.log()
    

    def _constructor1(self, address: dict) -> None:
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        self._init_fields()
        self.id = address.get(StreetAddressData.ID)
        self.name = address.get(StreetAddressData.NAME)
        self.street = address.get(StreetAddressData.STREET)
        self.city = address.get(StreetAddressData.CITY)
        self.state = address.get(StreetAddressData.STATE)
        self.code = address.get(StreetAddressData.CODE)
        self.country = address.get(StreetAddressData.COUNTRY)
        def_: str = address.get(StreetAddressData.DEFAULT)
        if def_ is not None and ((def_ > StreetAddressData.DEFAULT) - (def_ < StreetAddressData.DEFAULT)) == 0:
            self.isDefault = True
        else:
            self.isDefault = False
        self.log()
    

    def log(self) -> None:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
            self.logUtil.putF("Created Address: \n" + str(self.toHashMap()), self, "log")
    

    def setId(self, id: str) -> None:
        self.id = id
    

    def setName(self, name: str) -> None:
        self.name = name
    

    def setStreet(self, value: str) -> None:
        self.street = value
    

    def setCity(self, value: str) -> None:
        self.city = value
    

    def setState(self, value: str) -> None:
        self.state = value
    

    def setCode(self, value: str) -> None:
        self.code = value
    

    def setCountry(self, value: str) -> None:
        self.country = value
    

    def getName(self) -> str:
        return self.name
    

    def getStreet(self) -> str:
        return self.street
    

    def getCity(self) -> str:
        return self.city
    

    def getState(self) -> str:
        return self.state
    

    def getCode(self) -> str:
        return self.code
    

    def getCountry(self) -> str:
        return self.country
    

    def getId(self) -> str:
        return self.id
    

    def isDefault(self) -> bool:
        return self.isDefault
    

    def isEmpty(self) -> bool:
        EMPTY_STRING: str = StringUtil.getInstance().EMPTY_STRING
        if self.getName() is None and self.getName().compareTo(EMPTY_STRING) == 0 and self.getStreet() is None and self.getStreet().compareTo(EMPTY_STRING) == 0 and self.getCity() is None and self.getCity().compareTo(EMPTY_STRING) == 0 and self.getState() is None and self.getState().compareTo(EMPTY_STRING) == 0 and self.getCode() is None and self.getCode().compareTo(EMPTY_STRING) == 0 and self.getCountry() is None and self.getCountry().compareTo(EMPTY_STRING) == 0:
            return True
        return False
    

    def isValid(self) -> bool:
        EMPTY_STRING: str = StringUtil.getInstance().EMPTY_STRING
        if self.getName() is None or self.getName().compareTo(EMPTY_STRING) == 0 or self.getStreet() is None or self.getStreet().compareTo(EMPTY_STRING) == 0 or self.getCity() is None or self.getCity().compareTo(EMPTY_STRING) == 0 or self.getState() is None or self.getState().compareTo(EMPTY_STRING) == 0 or self.getCode() is None or self.getCode().compareTo(EMPTY_STRING) == 0 or self.getCountry() is None or self.getCountry().compareTo(EMPTY_STRING) == 0:
            return False
        return True
    

    def validationInfo(self) -> str:
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("Address Failed To Validate - All fields must contain data.<br></br>")
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        if not stringValidationUtil.isValidRequired(self.getName(), StreetAddressData.MIN, StreetAddressData.MAX):
            stringBuffer.append("Please enter a valid name")
            stringBuffer.append("<br></br>")
        if not stringValidationUtil.isValidRequired(self.getStreet(), StreetAddressData.MIN, StreetAddressData.MAX):
            stringBuffer.append("Please enter a valid street")
            stringBuffer.append("<br></br>")
        if not stringValidationUtil.isValidRequired(self.getCity(), StreetAddressData.MIN, StreetAddressData.MAX):
            stringBuffer.append("Please enter a valid city")
            stringBuffer.append("<br></br>")
        if not stringValidationUtil.isValidRequired(self.getState(), StreetAddressData.MIN, StreetAddressData.MAX):
            stringBuffer.append("Please enter a valid state")
            stringBuffer.append("<br></br>")
        if not stringValidationUtil.isValidRequired(self.getCode(), StreetAddressData.MIN, StreetAddressData.MAX):
            stringBuffer.append("Please enter a valid zipcode")
            stringBuffer.append("<br></br>")
        if not stringValidationUtil.isValidRequired(self.getCountry(), StreetAddressData.MIN, StreetAddressData.MAX):
            stringBuffer.append("Please enter a valid country")
            stringBuffer.append("<br></br>")
        return str(stringBuffer)
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        try:
            node: Node = document.createElement(StreetAddressData.FORM)
            node.appendChild(self.toXmlNode(document))
            return node
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, "toValidationInfoNode", e)
            return None
    

    def toHashMap(self) -> dict:
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put(StreetAddressData.ID, self.id)
        hashMap.put(StreetAddressData.NAME, self.name)
        hashMap.put(StreetAddressData.STREET, self.street)
        hashMap.put(StreetAddressData.CITY, self.city)
        hashMap.put(StreetAddressData.STATE, self.state)
        hashMap.put(StreetAddressData.CODE, self.code)
        hashMap.put(StreetAddressData.COUNTRY, self.country)
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        stringUtil: StringUtil = StringUtil.getInstance()
        hashMap: dict = self.toHashMap()
        keySet: Set = hashMap.keySet()
        keyArray: list[object] = keySet.toArray()
        size: int = len(keyArray)
        node: Node = document.createElement(StreetAddressData.ADDRESS)
        for i in range(0, size):
            name: str = keyArray[i]
            value: str = stringUtil.getNonNull(hashMap.get(name))
            node.appendChild(ModDomHelper.createNameValueNodes(document, name, value))
        return node
# from java.util.HashMap import HashMap
# from java.util.Set import Set
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


