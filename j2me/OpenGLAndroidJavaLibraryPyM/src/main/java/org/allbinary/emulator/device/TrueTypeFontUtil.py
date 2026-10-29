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
# package org.allbinary.emulator.device

from __future__ import annotations

from org.allbinary.emulator.device.TrueTypeFontUtilBase import TrueTypeFontUtilBase


#TTF
class TrueTypeFontUtil(TrueTypeFontUtilBase):
    instance: TrueTypeFontUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.preResourceImageUtil: PreResourceImageUtil = PreResourceImageUtil.getInstance()
        self.realFontSize: int = 18
        self.fontImage: OpenGLESImage = OpenGLESImage.NULL_OPENGL_IMAGE
    

    @staticmethod
    def getInstance() -> TrueTypeFontUtil:
        return TrueTypeFontUtil.instance
    

    def __init__(self) -> None:
        super().__init__(1)
        self._init_fields()
    

    def saveFontAtlasAsFile(self) -> None:
        try:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            file: File = ResourceUtil.getInstance().getContext().getFilesDir()
            path: str = file.getAbsolutePath() + CanvasStrings.getInstance().FONT_ATLAS
            self.logUtil.putF(path, self, commonStrings.CONSTRUCTOR)
            fos: FileOutputStream = FileOutputStream(path)
            bitmap: Bitmap = (self.fontImage.openGLBitmap.getImage()).getBitmap()
            bitmap.compress(Bitmap.CompressFormat.PNG, 100, fos)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            PreLogUtil.putOE(commonStrings.EXCEPTION, self, commonStrings.EXCEPTION, e)
    

    def getFontBitmapGL(self, gl: GL10, filename: str, cellSize: int, basicColor: BasicColor) -> Image:
        if self.fontImage == OpenGLESImage.NULL_OPENGL_IMAGE:
            cellsPerRow2: int = self.CELLS_PER_ROW * 2
            cellsPerRow3: int = self.CELLS_PER_ROW * 3
            cellsPerRow4: int = self.CELLS_PER_ROW * 4
            cellsPerRow5: int = self.CELLS_PER_ROW * 5
            cellsPerRow6: int = self.CELLS_PER_ROW * 6
            cellsPerRow7: int = self.CELLS_PER_ROW * 7
            typeface: Typeface = Typeface.DEFAULT
            textureSize: int = self.getAsTextureSize(self.CELLS_PER_ROW * cellSize)
            bitmap: Bitmap = Bitmap.createBitmap(textureSize, textureSize, Bitmap.Config.ARGB_8888)
            canvas: Canvas = Canvas(bitmap)
            paint: Paint = Paint()
            paint.setTypeface(typeface)
            paint.setTextSize(float(self.realFontSize))
            paint.setAlpha(int(basicColor.alpha))
            paint.setColor(int(basicColor))
            biggestHeight: int = 0
            bounds: Rect = Rect()
            x: int = 0
            y: int = 0
            for index in range(0, self.size):
                self.characterArray[0] = self.pattern.charAt(index)
                paint.getTextBounds(self.characterArray, 0, 1, bounds)
                self._characterWidth[index] = bounds.right
                if bounds.bottom - bounds.top > biggestHeight:
                    biggestHeight = bounds.bottom - bounds.top
                x = (index % self.CELLS_PER_ROW) * cellSize
                x += (cellSize >> 1)
                x -= (self._characterWidth[index] >> 1)
                y = 0
                if index >= self.CELLS_PER_ROW:
                    y += cellSize
                if index >= cellsPerRow2:
                    y += cellSize
                if index >= cellsPerRow3:
                    y += cellSize
                if index >= cellsPerRow4:
                    y += cellSize
                if index >= cellsPerRow5:
                    y += cellSize
                if index >= cellsPerRow6:
                    y += cellSize
                if index >= cellsPerRow7:
                    y += cellSize
                y += cellSize
                y -= (cellSize >> 2)
                canvas.drawText(self.characterArray, 0, 1, float(x) - 3.0, float(y) - 6.0, paint)
            canvas.save()
            image: Image = AndroidImmutableImage.create(bitmap)
            self.fontImage = self.preResourceImageUtil.encapsulate(image)
            return self.fontImage
        else:
            return self.fontImage
    

    def getFontWidths(self, filename: str, fontSize: int) -> list[int]:
        typeface: Typeface = Typeface.DEFAULT
        paint: Paint = Paint()
        paint.setTypeface(typeface)
        paint.setTextSize(float(fontSize))
        paint.setARGB(255, 255, 255, 255)
        bounds: Rect = Rect()
        for index in range(0, self.size):
            self.characterArray[0] = self.pattern.charAt(index)
            paint.getTextBounds(self.characterArray, 0, 1, bounds)
            if index < self.lastCapIndex:
                if self.characterArray[0] == '1':
                    self._characterWidth[index] = bounds.right + 3
                elif self.characterArray[0] == 'J' or self.characterArray[0] == 'V' or self.characterArray[0] == '2' or self.characterArray[0] == '9' or self.characterArray[0] == 'I' or self.characterArray[0] == 'N' or self.characterArray[0] == 'U':
                    self._characterWidth[index] = bounds.right + 1
                elif self.characterArray[0] == '4' or self.characterArray[0] == 'C' or self.characterArray[0] == 'E' or self.characterArray[0] == 'O':
                    self._characterWidth[index] = bounds.right - 2
                elif self.characterArray[0] == 'B' or self.characterArray[0] == 'D' or self.characterArray[0] == 'G' or self.characterArray[0] == 'H' or self.characterArray[0] == 'T' or self.characterArray[0] == 'W':
                    self._characterWidth[index] = bounds.right - 3
                elif self.characterArray[0] == 'A' or self.characterArray[0] == 'Q' or self.characterArray[0] == 'R':
                    self._characterWidth[index] = bounds.right - 5
                elif self.characterArray[0] == 'M':
                    self._characterWidth[index] = bounds.right - 6
                elif self.characterArray[0] == 'm':
                    self._characterWidth[index] = bounds.right - 8
                else:
                    self._characterWidth[index] = bounds.right
            else:
                if self.characterArray[0] == ' ':
                    self._characterWidth[index] = bounds.right + 10
                elif self.characterArray[0] == 'l' or self.characterArray[0] == 'i' or self.characterArray[0] == 'j' or self.characterArray[0] == '.' or self.characterArray[0] == '!' or self.characterArray[0] == '|':
                    self._characterWidth[index] = bounds.right + 6
                elif self.characterArray[0] == 'f' or self.characterArray[0] == 't' or self.characterArray[0] == 'u' or self.characterArray[0] == 'v':
                    self._characterWidth[index] = bounds.right + 1
                elif self.characterArray[0] == 'r':
                    self._characterWidth[index] = bounds.right + 2
                elif self.characterArray[0] == 'a' or self.characterArray[0] == 'b' or self.characterArray[0] == 'g' or self.characterArray[0] == 'u':
                    self._characterWidth[index] = bounds.right - 1
                elif self.characterArray[0] == 'o' or self.characterArray[0] == 'e':
                    self._characterWidth[index] = bounds.right - 2
                elif self.characterArray[0] == 'm':
                    self._characterWidth[index] = bounds.right - 7
                else:
                    self._characterWidth[index] = bounds.right
        self._characterWidth[0] = (fontSize >> 1) - 2
        return self._characterWidth
# from java.io.File import File
# from java.io.FileOutputStream import FileOutputStream
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.lcdui.Image import Image
from android.graphics.Bitmap import Bitmap
from android.graphics.Canvas import Canvas
from android.graphics.Paint import Paint
from android.graphics.Rect import Rect
from android.graphics.Typeface import Typeface
from org.allbinary.data.resource.ResourceUtil import ResourceUtil
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
from org.allbinary.image.PreResourceImageUtil import PreResourceImageUtil
from org.allbinary.image.opengles.OpenGLESImage import OpenGLESImage
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.microemu.android.device.AndroidImageInterface import AndroidImageInterface
from org.microemu.android.device.AndroidImmutableImage import AndroidImmutableImage


TrueTypeFontUtil.instance = TrueTypeFontUtil()

