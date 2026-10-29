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
# package org.allbinary.logic.system.security.licensing

from __future__ import annotations



class PartnerIdentifierFileUtil:
    instance: PartnerIdentifierFileUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.FILE_NAME: str = "partner.txt"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> PartnerIdentifierFileUtil:
        return PartnerIdentifierFileUtil.instance
    

    def get(self) -> str:
        try:
            resourceUtil: ResourceUtil = ResourceUtil.getInstance()
            inputStream: InputStream = resourceUtil.getResourceAsStream(self.FILE_NAME)
            inputStreamReader: InputStreamReader = InputStreamReader(inputStream)
            chars: list[str] = ['\0'] * (30)
            size: int = inputStreamReader.read(chars)
            partnerString: str = StringUtil.getInstance().EMPTY_STRING
            if size > 0:
                partnerString = "".join(chars[0:0 + size])
            inputStreamReader.close()
            return partnerString
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET, e)
            return StringUtil.getInstance().NULL_STRING
# from java.io.InputStream import InputStream
# from java.io.InputStreamReader import InputStreamReader
from org.allbinary.data.resource.ResourceUtil import ResourceUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings


PartnerIdentifierFileUtil.instance = PartnerIdentifierFileUtil()

