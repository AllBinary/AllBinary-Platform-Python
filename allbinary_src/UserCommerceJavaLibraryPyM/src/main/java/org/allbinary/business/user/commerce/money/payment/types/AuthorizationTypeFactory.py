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
# package org.allbinary.business.user.commerce.money.payment.types

from __future__ import annotations



class AuthorizationTypeFactory:
    instance: AuthorizationTypeFactory = None

    def _init_fields(self) -> None:
        self.NONE: AuthorizationType = AuthorizationType("None")
        self.VOICE: AuthorizationType = AuthorizationType("Voice")
        self.RETINAL: AuthorizationType = AuthorizationType("Retinal")
        self.IMAGE: AuthorizationType = AuthorizationType("Image")
        self.DNA: AuthorizationType = AuthorizationType("DNA")
        self.PRINT: AuthorizationType = AuthorizationType("Print")
        self.CHIP: AuthorizationType = AuthorizationType("Chip")

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> AuthorizationTypeFactory:
        return AuthorizationTypeFactory.instance
from org.allbinary.business.user.commerce.money.payment.types.AuthorizationType import AuthorizationType


AuthorizationTypeFactory.instance = AuthorizationTypeFactory()

