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
# package tags

from __future__ import annotations

from tags.CustomTagSupport import CustomTagSupport


class CommandTag(CustomTagSupport):

    def _init_fields(self) -> None:
        self.tagStrings: TagStrings = TagStrings.getInstance()
        self.command: str = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def setCommand(self, command: str) -> None:
        self.command = command
    

    def getCommand(self) -> str:
        return self.command
from tags.TagStrings import TagStrings


