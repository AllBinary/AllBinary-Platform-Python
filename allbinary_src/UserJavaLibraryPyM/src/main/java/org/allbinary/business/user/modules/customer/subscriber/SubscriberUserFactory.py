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
# package org.allbinary.business.user.modules.customer.subscriber

from __future__ import annotations

from org.allbinary.business.user.UserFactoryInterface import UserFactoryInterface


class SubscriberUserFactory(UserFactoryInterface):
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    def getInstance_j0(self) -> UserInterface:
        from org.allbinary.business.user.modules.customer.subscriber.SubscriberUser import SubscriberUser
        from org.allbinary.business.user.UserInterface import UserInterface
        return SubscriberUser()
    

    # throws Exception
    def getInstance_j1(self, hashMap: HashMap) -> UserInterface:
        from org.allbinary.business.user.modules.customer.subscriber.SubscriberUser import SubscriberUser
        from java.util.HashMap import HashMap
        from org.allbinary.business.user.UserInterface import UserInterface
        return SubscriberUser(hashMap)

    def getInstance(self, *args):
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
# from java.util.HashMap import HashMap
# from org.allbinary.business.user.UserInterface import UserInterface


