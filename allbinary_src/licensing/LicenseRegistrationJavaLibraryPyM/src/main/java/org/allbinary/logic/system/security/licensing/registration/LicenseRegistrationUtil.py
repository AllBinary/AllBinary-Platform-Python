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
# package org.allbinary.logic.system.security.licensing.registration

from __future__ import annotations

import threading


class LicenseRegistrationUtil:
    _lock = threading.RLock()
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def process(abeClientInformation: AbeClientInformationInterface, registrationId: str) -> None:
        with LicenseRegistrationUtil._lock:
            return LicenseRegistrationUtil._process_unlocked(abeClientInformation, registrationId)

    @staticmethod
    def _process_unlocked(abeClientInformation: AbeClientInformationInterface, registrationId: str) -> None:
        from org.allbinary.logic.system.security.licensing.registration.RegistrationConfiguration import RegistrationConfiguration
        from org.allbinary.logic.system.security.licensing.registration.RegistrationConfiguration import RegistrationConfiguration
        from org.allbinary.logic.system.security.licensing.registration.XmlRpcRemoteLicenseRegistrationClient import XmlRpcRemoteLicenseRegistrationClient
        try:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            PreLogUtil.put(str(CommonLabels.getInstance().START_LABEL) + "License Registration", "LicenseRegistrationUtil", commonStrings.PROCESS)
            registrationConfiguration: RegistrationConfiguration = RegistrationConfiguration.getInstance()
            registrationConfiguration.setRegistrationCode(registrationId)
            registrationConfiguration.write()
            hashtable: ABHashtable[object, object] = abeClientInformation.toHashtable()
            hashtable.put(RegistrationConfiguration.getInstance().NAME, registrationId)
            hashtable.put("message", SpecialMessageUtil.getInstance().get())
            XmlRpcRemoteLicenseRegistrationClient(abeClientInformation).get(hashtable)
        except Exception as e:
            PreLogUtil.putOE("License Registration Exception", "LicenseRegistrationUtil", "License Registration", e)
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.canvas.SpecialMessageUtil import SpecialMessageUtil
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.util.ABHashtable import ABHashtable


