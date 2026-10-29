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
# package org.allbinary.business.user

from __future__ import annotations



class NewUserFactory:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getInstance() -> UserInterface:
        return User()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def getInstance(transformInfoInterface: TransformInfoInterface) -> UserInterface:
        from org.allbinary.business.user.CreateUserFactory import CreateUserFactory
        httpTransformInfoInterface: TransformInfoHttpInterface = transformInfoInterface
        httpServletRequest: HttpServletRequest = httpTransformInfoInterface.getPageContext().getRequest()
        hashMap: dict = RequestParams(httpServletRequest).toHashMap()
        role: str = httpTransformInfoInterface.getPropertiesHashMap().get(str(UserRoleData.NAME))
        hashMap.put(str(UserRoleData.NAME), role)
        return CreateUserFactory.getInstance(hashMap)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def getInstance(httpServletRequest: HttpServletRequest, propertiesHashMap: dict) -> UserInterface:
        from org.allbinary.business.user.CreateUserFactory import CreateUserFactory
        if propertiesHashMap is not None:
            requestHashMap: dict = RequestParams(httpServletRequest).toHashMap()
            roleString: str = propertiesHashMap.get(str(UserRoleData.NAME))
            requestHashMap.put(str(UserRoleData.NAME), roleString)
            return CreateUserFactory.getInstance(requestHashMap)
        else:
            raise Exception("Null HashMap")
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.allbinary.business.user.modules.User import User
from org.allbinary.business.user.role.UserRoleData import UserRoleData
from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface


