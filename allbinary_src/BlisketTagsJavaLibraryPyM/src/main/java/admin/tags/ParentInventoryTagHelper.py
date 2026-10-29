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
# package admin.tags

from __future__ import annotations



class ParentInventoryTagHelper:
    instance: ParentInventoryTagHelper = None
    

    @staticmethod
    def getInstance() -> ParentInventoryTagHelper:
        return ParentInventoryTagHelper.instance
    

    # throws Exception
    def isValid(self, tagClass: object, parentTag: Tag) -> None:
        if parentTag is None:
            raise Exception("Must have parent tag.")
        elif not (isinstance(parentTag, HelperTag)):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Must have at least a ")
            stringBuffer.append("tags.HelperTag")
            stringBuffer.append(" as parent")
            stringBuffer.append("and not: ")
            stringBuffer.append(type(parentTag).__module__ + "." + type(parentTag).__qualname__)
            raise Exception(str(stringBuffer))
# from javax.servlet.jsp.tagext.Tag import Tag
from org.allbinary.logic.string.StringMaker import StringMaker


ParentInventoryTagHelper.instance = ParentInventoryTagHelper()

