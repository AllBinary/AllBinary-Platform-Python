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
# package org.allbinary.android

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class NullAndroidCanvas:
    NULL_CANVAS: Canvas = None
    NULL_MEDIA_PLAYER: MediaPlayer = None
# from android.graphics.Canvas import Canvas
# from android.media.MediaPlayer import MediaPlayer


def _NullAndroidCanvas_NULL_CANVAS() -> object:
    from android.graphics.Canvas import Canvas
    return Canvas()

lazy_static(NullAndroidCanvas, "NULL_CANVAS", _NullAndroidCanvas_NULL_CANVAS)

def _NullAndroidCanvas_NULL_MEDIA_PLAYER() -> object:
    from android.media.MediaPlayer import MediaPlayer
    return MediaPlayer()

lazy_static(NullAndroidCanvas, "NULL_MEDIA_PLAYER", _NullAndroidCanvas_NULL_MEDIA_PLAYER)

