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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from admin.tags.TableTag import TableTag


@java_inherited_overloads
class BasicGroupItemsTag(TableTag):
    def _java_defaults(self):
        vars(self).setdefault("propertiesHashMap", None)

    def _init_fields(self) -> None:
        if "propertiesHashMap" not in vars(self): self.propertiesHashMap: HashMap = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from admin.taghelpers.BasicGroupItemsHelperFactory import BasicGroupItemsHelperFactory
        from admin.taghelpers.BasicGroupItemsRequestHelperFactory import BasicGroupItemsRequestHelperFactory
        super().__init__()
        __class__._init_fields(self)
        self.setTagHelperFactory(BasicGroupItemsHelperFactory())
        self.setTagRequestHelperFactory(BasicGroupItemsRequestHelperFactory())
# from java.util.HashMap import HashMap
# from admin.taghelpers.BasicGroupItemsHelperFactory import BasicGroupItemsHelperFactory
# from admin.taghelpers.BasicGroupItemsRequestHelperFactory import BasicGroupItemsRequestHelperFactory


