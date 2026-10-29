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
# package org.allbinary.media.image

from __future__ import annotations



class AndroidImageUtil:
    instance: AndroidImageUtil = None
    

    @staticmethod
    def getInstance() -> AndroidImageUtil:
        return AndroidImageUtil.instance
    

    def paintBitmap(self, bitmap: Bitmap, originalBitmap: Bitmap, paint: Paint) -> None:
        bitmap.eraseColor(Color.TRANSPARENT)
        canvas: Canvas = Canvas()
        canvas.setBitmap(bitmap)
        canvas.drawBitmap(originalBitmap, 0.0, 0.0, paint)
    

    def paint(self, image: Image, originalImage: Image, paint: Paint) -> None:
        androidImage: AndroidImageInterface = image
        androidImage.getBitmap().eraseColor(Color.TRANSPARENT)
        canvas: Canvas = androidImage.getCanvas()
        originalAndroidImage: AndroidImageInterface = originalImage
        canvas.drawBitmap(originalAndroidImage.getBitmap(), 0.0, 0.0, paint)
    

    def rotate(self, image: Image, originalImage: Image, matrix: Matrix, paint: Paint) -> None:
        androidImage: AndroidImageInterface = image
        androidImage.getBitmap().eraseColor(Color.TRANSPARENT)
        canvas: Canvas = androidImage.getCanvas()
        canvas.concat(matrix)
        originalAndroidImage: AndroidImageInterface = originalImage
        canvas.drawBitmap(originalAndroidImage.getBitmap(), 0.0, 0.0, paint)
from android.graphics.Bitmap import Bitmap
from android.graphics.Canvas import Canvas
from android.graphics.Color import Color
from android.graphics.Matrix import Matrix
from android.graphics.Paint import Paint
# from javax.microedition.lcdui.Image import Image
from org.microemu.android.device.AndroidImageInterface import AndroidImageInterface


AndroidImageUtil.instance = AndroidImageUtil()

