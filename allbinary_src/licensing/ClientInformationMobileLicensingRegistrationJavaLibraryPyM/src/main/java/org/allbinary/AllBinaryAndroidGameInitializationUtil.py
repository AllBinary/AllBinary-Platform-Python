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
# package org.allbinary

from __future__ import annotations



class AllBinaryAndroidGameInitializationUtil:
    

    @staticmethod
    def init() -> None:
        from org.allbinary.AndroidResources import AndroidResources
        resourceUtil: ResourceUtil = ResourceUtil.getInstance()
        androidResources: AndroidResources = AndroidResources.getInstance()
        licenseInitInfoUtil: LicenseInitInfoUtil = LicenseInitInfoUtil.getInstance()
        resourceUtil.addResource(licenseInitInfoUtil.INITFILENAME, str(androidResources.raw.licenseinitdata))
        resourceUtil.addResource(PartnerIdentifierFileUtil.getInstance().FILE_NAME, str(androidResources.raw.partner))
from org.allbinary.business.init.LicenseInitInfoUtil import LicenseInitInfoUtil
from org.allbinary.data.resource.ResourceUtil import ResourceUtil
from org.allbinary.logic.system.security.licensing.PartnerIdentifierFileUtil import PartnerIdentifierFileUtil


