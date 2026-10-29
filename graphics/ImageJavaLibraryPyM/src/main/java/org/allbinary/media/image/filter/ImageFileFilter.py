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
# package org.allbinary.media.image.filter

from __future__ import annotations

# from javax.swing.filechooser.FileFilter import FileFilter


#TWB - replace with file visitor version
class ImageFileFilter(FileFilter):

    def __init__(self) -> None:
        super().__init__()
    

    def accept(self, f: File) -> bool:
        if f.isDirectory():
            return True
        s: str = f.getName()
        i: int = s.rfind('.')
        if i > 0 and i < len(s) - 1:
            ext: str = s[i + 1:].lower()
            if (ext == "jpg") or (ext == "jpeg"):
                return True
        return False
    

    def getDescription(self) -> str:
        return "Accepts .jpg and .jpeg files"
# from java.io.File import File


