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
# package org.allbinary.midlet

from __future__ import annotations

from org.allbinary.midlet.AllBinaryMidlet import AllBinaryMidlet


class ProgressMidlet(AllBinaryMidlet):

    def _init_fields(self) -> None:
        self.abeClientInformation: AbeClientInformationInterface = None
    

    def __init__(self, clientInformationFactory: ClientInformationFactory) -> None:
        super().__init__()
        self._init_fields()
        self.preInit()
        self.abeClientInformation = clientInformationFactory.getInstance()
    

    def preInit(self) -> None:
        pass
    

    def exitProgress(self, isProgress: bool) -> None:
        from org.allbinary.midlet.MidletExitProcessorFactory import MidletExitProcessorFactory
        from org.allbinary.midlet.ExitRunnable import ExitRunnable
        processor: Processor = MidletExitProcessorFactory.getInstance().getExitInstance(self)
        try:
            primaryThreadPool: ThreadPool = PrimaryThreadPool.getInstance()
            runnable: object = ExitRunnable(self, processor, isProgress)
            primaryThreadPool.runTask(runnable)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "exit", e)
            try:
                processor.process()
            except Exception as e2:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "exit", e)
from org.allbinary.canvas.Processor import Processor
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.ClientInformationFactory import ClientInformationFactory
from org.allbinary.thread.PrimaryThreadPool import PrimaryThreadPool
from org.allbinary.thread.ThreadPool import ThreadPool


