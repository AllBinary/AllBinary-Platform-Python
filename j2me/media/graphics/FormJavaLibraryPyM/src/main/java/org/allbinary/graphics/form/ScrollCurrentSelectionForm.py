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
# package org.allbinary.graphics.form

from __future__ import annotations

from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.graphics.form.ScrollSelectionForm import ScrollSelectionForm


class ScrollCurrentSelectionForm(ScrollSelectionForm, UpdateMyFontInterface):
    class TempHorizontalFormProcessor(Processor):

        def _init_fields(self) -> None:
            self.scrollCurrentSelectionForm: ScrollCurrentSelectionForm = None
        

        def __init__(self, scrollCurrentSelectionForm: ScrollCurrentSelectionForm) -> None:
            super().__init__()
            self._init_fields()
            self.scrollCurrentSelectionForm = scrollCurrentSelectionForm
        

        # throws Exception
        def process(self) -> None:
            self.scrollCurrentSelectionForm.processTempHorizontalForm()
            self.scrollCurrentSelectionForm.processor = Processor.getInstance()
    class HorizontalFormProcessor(Processor):

        def _init_fields(self) -> None:
            self.scrollCurrentSelectionForm: ScrollCurrentSelectionForm = None
        

        def __init__(self, scrollCurrentSelectionForm: ScrollCurrentSelectionForm) -> None:
            super().__init__()
            self._init_fields()
            self.scrollCurrentSelectionForm = scrollCurrentSelectionForm
        

        # throws Exception
        def process(self) -> None:
            self.scrollCurrentSelectionForm.processHorizontalForm()
            self.scrollCurrentSelectionForm.processor = Processor.getInstance()
    class VerticalFormProcessor(Processor):

        def _init_fields(self) -> None:
            self.scrollCurrentSelectionForm: ScrollCurrentSelectionForm = None
        

        def __init__(self, scrollCurrentSelectionForm: ScrollCurrentSelectionForm) -> None:
            super().__init__()
            self._init_fields()
            self.scrollCurrentSelectionForm = scrollCurrentSelectionForm
        

        # throws Exception
        def process(self) -> None:
            self.scrollCurrentSelectionForm.processVerticalForm()
            self.scrollCurrentSelectionForm.processor = Processor.getInstance()
    class TempHorizontalItemIndexDx(ItemIndexDx):

        def _init_fields(self) -> None:
            self.scrollCurrentSelectionForm: ScrollCurrentSelectionForm = None
        

        def __init__(self, scrollCurrentSelectionForm: ScrollCurrentSelectionForm) -> None:
            super().__init__()
            self._init_fields()
            self.scrollCurrentSelectionForm = scrollCurrentSelectionForm
        

        # throws Exception
        def getDx(self, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
            return self.scrollCurrentSelectionForm.getXTempHorizontalForm(index, item, dx, dy)
    class HorizontalItemIndexDx(ItemIndexDx):

        def _init_fields(self) -> None:
            self.scrollCurrentSelectionForm: ScrollCurrentSelectionForm = None
        

        def __init__(self, scrollCurrentSelectionForm: ScrollCurrentSelectionForm) -> None:
            super().__init__()
            self._init_fields()
            self.scrollCurrentSelectionForm = scrollCurrentSelectionForm
        

        # throws Exception
        def getDx(self, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
            return self.scrollCurrentSelectionForm.getXHorizontalForm(index, item, dx, dy)
    class VerticalItemIndexDx(ItemIndexDx):

        def _init_fields(self) -> None:
            self.scrollCurrentSelectionForm: ScrollCurrentSelectionForm = None
        

        def __init__(self, scrollCurrentSelectionForm: ScrollCurrentSelectionForm) -> None:
            super().__init__()
            self._init_fields()
            self.scrollCurrentSelectionForm = scrollCurrentSelectionForm
        

        # throws Exception
        def getDx(self, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
            return self.scrollCurrentSelectionForm.getXVerticalForm(index, item, dx, dy)

    def _init_fields(self) -> None:
        self.moveForSmallScreen: bool = None
        self.updateMyFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.myFontProcessor: MyFontProcessor = self.updateMyFontProcessor
        self.processor: Processor = Processor.getInstance()
        self.preItemIndexDx: ItemIndexDx = ItemIndexDx.getInstance()
        self.dx: int = 0
        self.dy: int = 0
        self.maxWidth: int = 0
    

    def __init__(self, title: str, items: list[ABCustomItem], formPaintableFactory: ItemPaintableFactory, border: int, adjustedExtraBorder: int, moveForSmallScreen: bool, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__(title, items, formPaintableFactory, border, adjustedExtraBorder, backgroundBasicColor, foregroundBasicColor)
        self._init_fields()
        self.moveForSmallScreen = moveForSmallScreen
    

    # throws Exception
    def init(self, rectangle: Rectangle, formType: FormType) -> None:
        from org.allbinary.graphics.form.FormTypeFactory import FormTypeFactory
        from org.allbinary.graphics.form.VerticalFormProcessor import VerticalFormProcessor
        from org.allbinary.graphics.form.VerticalItemIndexDx import VerticalItemIndexDx
        from org.allbinary.graphics.form.HorizontalFormProcessor import HorizontalFormProcessor
        from org.allbinary.graphics.form.HorizontalItemIndexDx import HorizontalItemIndexDx
        from org.allbinary.graphics.form.TempHorizontalFormProcessor import TempHorizontalFormProcessor
        from org.allbinary.graphics.form.TempHorizontalItemIndexDx import TempHorizontalItemIndexDx
        super().init(rectangle, formType)
        formTypeFactory: FormTypeFactory = FormTypeFactory.getInstance()
        if formType == formTypeFactory.TEMP_HORIZONTAL_FORM:
            self.processor = TempHorizontalFormProcessor(self)
            self.preItemIndexDx = TempHorizontalItemIndexDx(self)
        elif formType == formTypeFactory.HORIZONTAL_FORM:
            self.processor = HorizontalFormProcessor(self)
            self.preItemIndexDx = HorizontalItemIndexDx(self)
        elif formType == formTypeFactory.VERTICAL_CENTER_FORM:
            self.processor = VerticalFormProcessor(self)
            self.preItemIndexDx = VerticalItemIndexDx(self)
        elif formType == formTypeFactory.NULL_FORM_TYPE:
            pass
        else:
            self.logUtil.putF(formTypeFactory.UNK, self, self.commonStrings.INIT)
        self.myFontProcessor = self.updateMyFontProcessor
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def processTempHorizontalForm(self) -> None:
        self.dx = self.x - 30 + (self.rectangle.getWidth() >> 1)
        self.dy = self.y
    

    def processHorizontalForm(self) -> None:
        size: int = self.size()
        totalWidth: int = 0
        item: ABCustomItem = None
        for index in range(0, size):
            item = self.get(index)
            totalWidth += item.getMinimumWidth() + self.border
        self.dx = self.x + (self.rectangle.getWidth() >> 1) - (totalWidth >> 1)
        self.dy = self.y + (self.rectangle.getHeight() >> 1)
        if self.moveForSmallScreen:
            maxTitleHeight: int = 175
            if self.dy < maxTitleHeight:
                self.dy = maxTitleHeight
    

    def processVerticalForm(self) -> None:
        totalHeight: int = 0
        size: int = self.size()
        item2: ABCustomItem = None
        for index in range(0, size):
            item2 = self.get(index)
            if self.maxWidth < item2.getMinimumWidth():
                self.maxWidth = item2.getMinimumWidth()
            totalHeight += item2.getMinimumHeight() + self.border
        self.dx = ((self.rectangle.getWidth() - self.maxWidth) / 2)
        if self.size() > 0:
            self.dy = self.y + ((self.rectangle.getHeight() - totalHeight) / 2)
            if self.moveForSmallScreen:
                maxTitleHeight: int = 175
                if self.dy < maxTitleHeight:
                    self.dy = maxTitleHeight
        else:
            self.dy = self.y
    

    def getXTempHorizontalForm(self, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
        return self.getDiffX(item)
    

    def getXHorizontalForm(self, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
        return 0
    

    def getXVerticalForm(self, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
        return self.getDiffX(item) + self.halfBorder
    

    def getDiffX(self, item: ABCustomItem) -> int:
        return ((self.maxWidth - item.getMinimumWidth()) >> 1)
    

    def getDx(self) -> int:
        return self.dx
    

    def getDy(self) -> int:
        return self.dy
    

    def paint(self, graphics: Graphics) -> None:
        from org.allbinary.graphics.form.FormTypeFactory import FormTypeFactory
        try:
            self.processor.process()
            delta: int = 0
            deltaX: int = self.getDx()
            deltaY: int = self.getDy()
            size: int = self.size()
            formTypeFactory: FormTypeFactory = FormTypeFactory.getInstance()
            item: ABCustomItem = None
            for index in range(0, size):
                item = self.get(index)
                diffX: int = self.preItemIndexDx.getDx(index, item, self.dx, self.dy)
                if index == self.getSelectedIndex():
                    delta = self.paintItem(graphics, index, item, deltaX + diffX, deltaY)
                    self.paintable.paint(graphics, index, deltaX + diffX, deltaY)
                else:
                    delta = self.paintUnselectedItem(graphics, index, item, deltaX + diffX, deltaY)
                    self.paintable.paint(graphics, index, deltaX + diffX, deltaY)
                if self.formType == formTypeFactory.TEMP_HORIZONTAL_FORM:
                    pass
                elif self.formType == formTypeFactory.HORIZONTAL_FORM:
                    deltaX = delta
                elif self.formType == formTypeFactory.VERTICAL_CENTER_FORM:
                    deltaY = delta
                else:
                    raise Exception(formTypeFactory.UNK)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.canvasStrings.PAINT, e)
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.canvas.Processor import Processor
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
from org.allbinary.graphics.form.ItemIndexDx import ItemIndexDx


