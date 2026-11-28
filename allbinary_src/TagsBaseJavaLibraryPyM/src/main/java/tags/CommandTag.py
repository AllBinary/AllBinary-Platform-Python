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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from tags.CustomTagSupport import CustomTagSupport


@java_inherited_overloads
class CommandTag(CustomTagSupport):
    def _java_defaults(self):
        vars(self).setdefault("tagStrings", None)
        vars(self).setdefault("command", None)

    def _init_fields(self) -> None:
        self.tagStrings: TagStrings = TagStrings.getInstance()
        if "command" not in vars(self): self.command: str = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def setCommand(self, command: str) -> None:
        self.command = command
    

    def getCommand(self) -> str:
        return self.command
from tags.TagStrings import TagStrings


