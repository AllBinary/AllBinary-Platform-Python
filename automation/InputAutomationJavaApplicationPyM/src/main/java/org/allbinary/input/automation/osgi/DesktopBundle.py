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
# package org.allbinary.input.automation.osgi

from __future__ import annotations



class DesktopBundle:
    DESKTOP_SYMBOLIC_NAME: str = "org.knopflerfish.bundle.desktop"

    def _init_fields(self) -> None:
        self.bundle: Bundle = None
    

    def __init__(self) -> None:
        self._init_fields()
        bundleContext: BundleContext = InputAutomationBundleActivator.getBundleContext()
        if bundleContext is not None:
            bundleArray: list[Bundle] = bundleContext.getBundles()
            for index in range(0, len(bundleArray)):
                bundle: Bundle = bundleArray[index]
                symbolicName: str = bundle.getSymbolicName()
                if ((symbolicName > DesktopBundle.DESKTOP_SYMBOLIC_NAME) - (symbolicName < DesktopBundle.DESKTOP_SYMBOLIC_NAME)) == 0:
                    self.bundle = bundle
        else:
            textJDialog: JDialog = BasicTextJDialog("BundlContext is Null")
            textJDialog.setVisible(True)
    

    # throws Exception
    def start(self) -> None:
        self.bundle.start()
# from javax.swing import *
from org.osgi.framework.Bundle import Bundle
from org.osgi.framework.BundleContext import BundleContext
from bundle.input.automation.InputAutomationBundleActivator import InputAutomationBundleActivator
from org.allbinary.gui.dialog.BasicTextJDialog import BasicTextJDialog


