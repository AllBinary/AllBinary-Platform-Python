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
# package org.allbinary.logic.communication.http.request

from __future__ import annotations



class AbeHttpRequestInfoData:
    instance: AbeHttpRequestInfoData = None

    def _init_fields(self) -> None:
        self.HTTP_USER_AGENT: str = "HTTP_USER_AGENT"
        self.REMOTE_ADDRESS: str = "REMOTE_ADDRESS"
        self.REMOTE_HOST: str = "REMOTE_HOST"
        self.REMOTE_HOST_BY_ADDRESS: str = "REMOTE_HOST_BY_ADDRESS"
        self.REMOTE_PORT: str = "REMOTE_PORT"
        self.REQUEST_FILE_PATH: str = "REQUEST_FILE_PATH"
    

    @staticmethod
    def getInstance() -> AbeHttpRequestInfoData:
        return AbeHttpRequestInfoData.instance
    

    def __init__(self) -> None:
        self._init_fields()


AbeHttpRequestInfoData.instance = AbeHttpRequestInfoData()

