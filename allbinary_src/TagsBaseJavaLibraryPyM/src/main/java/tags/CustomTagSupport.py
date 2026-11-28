# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# from javax.servlet.jsp.tagext.TagSupport import TagSupport


@java_inherited_overloads
class CustomTagSupport(TagSupport):
    def _java_defaults(self):
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("tagStrings", None)

    def _init_fields(self) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.tagStrings: TagStrings = TagStrings.getInstance()

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
# from org.allbinary.string.CommonStrings import CommonStrings
from tags.TagStrings import TagStrings


