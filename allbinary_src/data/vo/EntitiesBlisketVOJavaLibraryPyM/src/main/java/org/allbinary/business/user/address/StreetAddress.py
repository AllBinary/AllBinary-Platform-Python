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

from java.lang.JavaRuntimeStatic import java_predicate


class StreetAddress:

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "id" not in vars(self): self.id: str = None
        if "name" not in vars(self): self.name: str = None
        if "street" not in vars(self): self.street: str = None
        if "city" not in vars(self): self.city: str = None
        if "state" not in vars(self): self.state: str = None
        if "code" not in vars(self): self.code: str = None
        if "country" not in vars(self): self.country: str = None
        self.isDefault_field: bool = False

    def __init__(self, *args) -> None:
        if len(args) == 0:
            __class__._constructor0(self, *args)
        elif len(args) == 1:
            __class__.__jconstructor1(self, *args)
        elif len(args) == 6:
            __class__._constructor6(self, *args)

    def __jconstructor1(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "Node" for base in type(args[0]).__mro__)):
            __class__._constructor1_1(self, *args)
        elif True and (args[0] is None or any(base.__name__ == "StreetAddress" for base in type(args[0]).__mro__)):
            __class__._constructor1_2(self, *args)
        elif True and (args[0] is None or any(base.__name__ == "HttpServletRequest" for base in type(args[0]).__mro__)):
            __class__._constructor1_3(self, *args)
        else:
            __class__._constructor1_4(self, *args)
    

    def _constructor0(self) -> None:
        __class__._init_fields(self)
    

    def _constructor1_1(self, node: Node) -> None:
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.w3c.dom.Node import Node
        __class__._init_fields(self)
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
    

    def _constructor1_2(self, streetAddress: StreetAddress) -> None:
        __class__._init_fields(self)
        self.id = streetAddress.getId()
        self.name = streetAddress.getName()
        self.street = streetAddress.getStreet()
        self.city = streetAddress.getCity()
        self.state = streetAddress.getState()
        self.code = streetAddress.getCode()
        self.country = streetAddress.getCountry()
        self.isDefault_field = java_predicate(streetAddress, "isDefault")
        self.log()
    

    def _constructor1_3(self, request: HttpServletRequest) -> None:
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        __class__._init_fields(self)
        self.setId(request.getParameter(StreetAddressData.ID))
        self.setName(request.getParameter(StreetAddressData.NAME))
        self.setStreet(request.getParameter(StreetAddressData.STREET))
        self.setCity(request.getParameter(StreetAddressData.CITY))
        self.setState(request.getParameter(StreetAddressData.STATE))
        self.setCode(request.getParameter(StreetAddressData.CODE))
        self.setCountry(request.getParameter(StreetAddressData.COUNTRY))
        self.log()
    

    def _constructor6(self, name: str, street: str, city: str, state: str, code: str, country: str) -> None:
        __class__._init_fields(self)
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.code = code
        self.country = country
        self.log()
    

    def _constructor1_4(self, address: HashMap) -> None:
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from java.util.HashMap import HashMap
        __class__._init_fields(self)
        self.id = address.get(StreetAddressData.ID)
        self.name = address.get(StreetAddressData.NAME)
        self.street = address.get(StreetAddressData.STREET)
        self.city = address.get(StreetAddressData.CITY)
        self.state = address.get(StreetAddressData.STATE)
        self.code = address.get(StreetAddressData.CODE)
        self.country = address.get(StreetAddressData.COUNTRY)
        def_: str = address.get(StreetAddressData.DEFAULT)
        if def_ is not None and ((def_ > StreetAddressData.DEFAULT) - (def_ < StreetAddressData.DEFAULT)) == 0:
            self.isDefault_field = True
        else:
            self.isDefault_field = False
        self.log()
    

    def log(self) -> None:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
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
        return self.isDefault_field
    

    def isEmpty(self) -> bool:
        from org.allbinary.logic.string.StringUtil import StringUtil
        EMPTY_STRING: str = StringUtil.getInstance().EMPTY_STRING
        if self.getName() is None and self.getName().compareTo(EMPTY_STRING) == 0 and self.getStreet() is None and self.getStreet().compareTo(EMPTY_STRING) == 0 and self.getCity() is None and self.getCity().compareTo(EMPTY_STRING) == 0 and self.getState() is None and self.getState().compareTo(EMPTY_STRING) == 0 and self.getCode() is None and self.getCode().compareTo(EMPTY_STRING) == 0 and self.getCountry() is None and self.getCountry().compareTo(EMPTY_STRING) == 0:
            return True
        return False
    

    def isValid(self) -> bool:
        from org.allbinary.logic.string.StringUtil import StringUtil
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
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("Address Failed To Validate - All fields must contain data.<br></br>")
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        if not (stringValidationUtil.isValidRequired(self.getName(), StreetAddressData.MIN, StreetAddressData.MAX)):
            stringBuffer.append("Please enter a valid name")
            stringBuffer.append("<br></br>")
        if not (stringValidationUtil.isValidRequired(self.getStreet(), StreetAddressData.MIN, StreetAddressData.MAX)):
            stringBuffer.append("Please enter a valid street")
            stringBuffer.append("<br></br>")
        if not (stringValidationUtil.isValidRequired(self.getCity(), StreetAddressData.MIN, StreetAddressData.MAX)):
            stringBuffer.append("Please enter a valid city")
            stringBuffer.append("<br></br>")
        if not (stringValidationUtil.isValidRequired(self.getState(), StreetAddressData.MIN, StreetAddressData.MAX)):
            stringBuffer.append("Please enter a valid state")
            stringBuffer.append("<br></br>")
        if not (stringValidationUtil.isValidRequired(self.getCode(), StreetAddressData.MIN, StreetAddressData.MAX)):
            stringBuffer.append("Please enter a valid zipcode")
            stringBuffer.append("<br></br>")
        if not (stringValidationUtil.isValidRequired(self.getCountry(), StreetAddressData.MIN, StreetAddressData.MAX)):
            stringBuffer.append("Please enter a valid country")
            stringBuffer.append("<br></br>")
        return str(stringBuffer)
    

    def toValidationInfoDoc(self) -> Document:
        from org.w3c.dom.Document import Document
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            node: Node = document.createElement(StreetAddressData.FORM)
            node.appendChild(self.toXmlNode(document))
            return node
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, "toValidationInfoNode", e)
            return None
    

    def toHashMap(self) -> HashMap:
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from java.util.HashMap import HashMap
        from org.allbinary.logic.StdUtil import StdUtil
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
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
        from java.util.HashMap import HashMap
        from java.util.Set import Set
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        stringUtil: StringUtil = StringUtil.getInstance()
        hashMap: HashMap = self.toHashMap()
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
# from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


