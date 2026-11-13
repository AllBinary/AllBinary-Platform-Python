#
# AllBinary Open License Version 1
# Copyright (c) 2026 AllBinary
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
# package org.allbinary

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


#like microemu-playn, so the languages without overloading can be generated. J2ME uses the MIDP overloads.
class MIDPUtil:
    instance: MIDPUtil = None
    

    @staticmethod
    def getInstance() -> MIDPUtil:
        return MIDPUtil.instance
    

    def createImageWH(self, width: int, height: int) -> Image:
        from javax.microedition.lcdui.Image import Image
        return Image.createImage(width, height)
    

    def createImageFromByteArray(self, imageData: list[int], imageOffset: int, imageLength: int) -> Image:
        from javax.microedition.lcdui.Image import Image
        return Image.createImage(imageData, imageOffset, imageLength)
    

    # throws IOException
    def createImageFromInputStream(self, inputStream: InputStream) -> Image:
        from java.io.InputStream import InputStream
        from javax.microedition.lcdui.Image import Image
        return Image.createImage(inputStream)
    

    # throws IOException, MediaException
    def createPlayerFromInputStream(self, inputStream: InputStream, type_: str) -> Player:
        from java.io.InputStream import InputStream
        from javax.microedition.media.Manager import Manager
        from javax.microedition.media.MediaException import MediaException
        from javax.microedition.media.Player import Player
        return Manager.createPlayer(inputStream, type_)
    

    def appendItem(self, form: Form, item: Item) -> int:
        from javax.microedition.lcdui.Form import Form
        from javax.microedition.lcdui.Item import Item
        return form.append(item)
# from java.io.IOException import IOException
# from java.io.InputStream import InputStream
# from javax.microedition.lcdui.Form import Form
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.Item import Item
# from javax.microedition.media.Manager import Manager
# from javax.microedition.media.MediaException import MediaException
# from javax.microedition.media.Player import Player


def _MIDPUtil_instance() -> object:
    return MIDPUtil()

lazy_static(MIDPUtil, "instance", _MIDPUtil_instance)

