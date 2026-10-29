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
# package org.allbinary.gui.dialog

from __future__ import annotations

import sys
from org.allbinary.gui.dialog.CloseJDialogListenerInterface import CloseJDialogListenerInterface


class ExitCloseListener(CloseJDialogListenerInterface):
    

    def __init__(self) -> None:
        pass
    

    def onClose(self) -> None:
        sys.exit(-1)


