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

from admin.tags.TableTag import TableTag


class DownloadItemsTag(TableTag):
    

    def __init__(self) -> None:
        super().__init__()
        self.setTagHelperFactory(DownloadItemsHelperFactory())
        self.setTagRequestHelperFactory(DownloadItemsRequestHelperFactory())
    

    # throws JspTagException
    def doStartTag(self) -> int:
        from admin.tags.ParentInventoryTagHelper import ParentInventoryTagHelper
        from admin.tags.AbTagData import AbTagData
        try:
            if self.isEnabled():
                if self.getCommand() is not None:
                    if self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.BACKUP) != 0 and self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.RESTORE) != 0 and self.getCommand().compareTo(self.commonStrings.CREATE) != 0 and self.getCommand().compareTo(self.commonStrings.DROP) != 0:
                        parentTag: Tag = self.getParent()
                        ParentInventoryTagHelper.getInstance().isValid(self, parentTag)
                        self.getPropertiesHashMap().put(AbTagData.PARENT, parentTag)
                    return super().doStartTag()
            return self.SKIP_BODY
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from javax.servlet.jsp.JspTagException import JspTagException
# from javax.servlet.jsp.tagext.Tag import Tag
from admin.taghelpers.DownloadItemsHelperFactory import DownloadItemsHelperFactory
from admin.taghelpers.DownloadItemsRequestHelperFactory import DownloadItemsRequestHelperFactory
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler


