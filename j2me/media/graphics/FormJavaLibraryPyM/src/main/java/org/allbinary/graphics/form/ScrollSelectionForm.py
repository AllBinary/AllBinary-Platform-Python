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

from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.graphics.form.PaintableForm import PaintableForm


class ScrollSelectionForm(PaintableForm):
    NULL_SCROLL_SELECTION_FORM: object = NullUtil.getInstance().NULL_OBJECT
    NULL_SCROLL_SELECTION_HORIZONTAL_FORM: object = NullUtil.getInstance().NULL_OBJECT
    INSIDE_FORM: str = " inside form"
    IS_IN_FORM: str = "isInForm"
    GET_SELECTED_INDEX: str = "getSelectedIndexForPoint"
    class ScrollSelectionFormHorizontalPaintable(ItemIndexPaintable):

        def _init_fields(self) -> None:
            self.scrollSelectionForm: ScrollSelectionForm = None
        

        def __init__(self, scrollSelectionForm: ScrollSelectionForm) -> None:
            super().__init__()
            self._init_fields()
            self.scrollSelectionForm = scrollSelectionForm
        

        # throws Exception
        def paint(self, graphics: Graphics, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
            return self.scrollSelectionForm.paintItemHorizontal(graphics, index, item, dx, dy)
    class ScrollSelectionFormVerticalPaintable(ItemIndexPaintable):

        def _init_fields(self) -> None:
            self.scrollSelectionForm: ScrollSelectionForm = None
        

        def __init__(self, scrollSelectionForm: ScrollSelectionForm) -> None:
            super().__init__()
            self._init_fields()
            self.scrollSelectionForm = scrollSelectionForm
        

        # throws Exception
        def paint(self, graphics: Graphics, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
            return self.scrollSelectionForm.paintItemVertical(graphics, index, item, dx, dy)
    class ScrollSelectionFormTempHorizontalPaintable(ItemIndexPaintable):

        def _init_fields(self) -> None:
            self.scrollSelectionForm: ScrollSelectionForm = None
        

        def __init__(self, scrollSelectionForm: ScrollSelectionForm) -> None:
            super().__init__()
            self._init_fields()
            self.scrollSelectionForm = scrollSelectionForm
        

        # throws Exception
        def paint(self, graphics: Graphics, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
            return self.scrollSelectionForm.paintItemTempHorizontal(graphics, index, item, dx, dy)
    class ScrollSelectionFormHorizontalDx(ItemIndexDx):

        def _init_fields(self) -> None:
            self.scrollSelectionForm: ScrollSelectionForm = None
        

        def __init__(self, multipleScrollSelectionForm: ScrollSelectionForm) -> None:
            super().__init__()
            self._init_fields()
            self.scrollSelectionForm = multipleScrollSelectionForm
        

        # throws Exception
        def getDx(self, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
            return self.scrollSelectionForm.getSelectedIndexForPointHorizontalDx(index, item, dx, dy)
    class ScrollSelectionFormVericalDx(ItemIndexDx):

        def _init_fields(self) -> None:
            self.scrollSelectionForm: ScrollSelectionForm = None
        

        def __init__(self, multipleScrollSelectionForm: ScrollSelectionForm) -> None:
            super().__init__()
            self._init_fields()
            self.scrollSelectionForm = multipleScrollSelectionForm
        

        # throws Exception
        def getDx(self, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
            return self.scrollSelectionForm.getSelectedIndexForPointVerticalDx(index, item, dx, dy)
    class ScrollSelectionFormTempHorizontalDx(ItemIndexDx):

        def _init_fields(self) -> None:
            self.scrollSelectionForm: ScrollSelectionForm = None
        

        def __init__(self, multipleScrollSelectionForm: ScrollSelectionForm) -> None:
            super().__init__()
            self._init_fields()
            self.scrollSelectionForm = multipleScrollSelectionForm
        

        # throws Exception
        def getDx(self, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
            return self.scrollSelectionForm.getSelectedIndexForPointTempHorizontalDx(index, item, dx, dy)

    def _init_fields(self) -> None:
        self.rectangleCollisionUtil: RectangleCollisionUtil = RectangleCollisionUtil.getInstance()
        self.border: int = None
        self.halfBorder: int = None
        self.buttonBasicColor: BasicColor = None
        self.scrollSelectionFormFormTypeItemIndexPaintable: ItemIndexPaintable = ItemIndexPaintable.getInstance()
        self.formTypeItemIndexDx: ItemIndexDx = ItemIndexDx.getInstance()
        self.paintable: ItemPaintable = ItemPaintableFactory.getInstance()
        self.adjustedExtraBorder: int = None
    

    @staticmethod
    def createForm(title: str, items: list[ABCustomItem], formPaintableFactory: ItemPaintableFactory, border: int, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> PaintableForm:
        from org.allbinary.graphics.form.ItemPaintableFactory import ItemPaintableFactory
        from org.allbinary.graphics.form.PaintableForm import PaintableForm
        from org.allbinary.graphics.form.PaintableForm import PaintableForm
        try:
            if formPaintableFactory == ItemPaintableFactory.getInstance():
                return ScrollSelectionForm(title, items, formPaintableFactory, border, -3, backgroundBasicColor, foregroundBasicColor)
            else:
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil: LogUtil = LogUtil.getInstance()
                logUtil.putF(commonStrings.EXCEPTION, logUtil, commonStrings.EXCEPTION)
                return PaintableForm.getNullPaintableForm()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            logUtil: LogUtil = LogUtil.getInstance()
            logUtil.put(commonStrings.EXCEPTION, logUtil, commonStrings.EXCEPTION, e)
            return PaintableForm.getNullPaintableForm()
    

    @staticmethod
    def getNullScrollSelectionForm() -> ScrollSelectionForm:
        from org.allbinary.graphics.form.ItemPaintableFactory import ItemPaintableFactory
        if ScrollSelectionForm.NULL_SCROLL_SELECTION_FORM == NullUtil.getInstance().NULL_OBJECT:
            ScrollSelectionForm.NULL_SCROLL_SELECTION_FORM = ScrollSelectionForm.createForm(StringUtil.getInstance().EMPTY_STRING, [None] * (0), ItemPaintableFactory.getInstance(), 0, BasicColorFactory.getInstance().BLACK, BasicColorFactory.getInstance().WHITE)
        return ScrollSelectionForm.NULL_SCROLL_SELECTION_FORM
    

    @staticmethod
    def getNullScrollSelectionFormHorizontal() -> ScrollSelectionForm:
        from org.allbinary.graphics.form.ItemPaintableFactory import ItemPaintableFactory
        if ScrollSelectionForm.NULL_SCROLL_SELECTION_HORIZONTAL_FORM == NullUtil.getInstance().NULL_OBJECT:
            ScrollSelectionForm.NULL_SCROLL_SELECTION_HORIZONTAL_FORM = ScrollSelectionForm.createForm(StringUtil.getInstance().EMPTY_STRING, [None] * (0), ItemPaintableFactory.getInstance(), 0, BasicColorFactory.getInstance().BLACK, BasicColorFactory.getInstance().WHITE)
        return ScrollSelectionForm.NULL_SCROLL_SELECTION_HORIZONTAL_FORM
    

    def __init__(self, title: str, items: list[ABCustomItem], formPaintableFactory: ItemPaintableFactory, border: int, adjustedExtraBorder: int, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__(title, items, backgroundBasicColor, foregroundBasicColor)
        self._init_fields()
        self.adjustedExtraBorder = adjustedExtraBorder
        self.buttonBasicColor = foregroundBasicColor
        self.border = border
        self.halfBorder = (border >> 1)
        self.paintable = formPaintableFactory.getInstanceItemPaintable(self)
    

    # throws Exception
    def init(self, rectangle: Rectangle, formType: FormType) -> None:
        from org.allbinary.graphics.form.FormTypeFactory import FormTypeFactory
        from org.allbinary.graphics.form.ScrollSelectionFormTempHorizontalPaintable import ScrollSelectionFormTempHorizontalPaintable
        from org.allbinary.graphics.form.ScrollSelectionFormTempHorizontalDx import ScrollSelectionFormTempHorizontalDx
        from org.allbinary.graphics.form.ScrollSelectionFormVerticalPaintable import ScrollSelectionFormVerticalPaintable
        from org.allbinary.graphics.form.ScrollSelectionFormVericalDx import ScrollSelectionFormVericalDx
        from org.allbinary.graphics.form.ScrollSelectionFormHorizontalPaintable import ScrollSelectionFormHorizontalPaintable
        from org.allbinary.graphics.form.ScrollSelectionFormHorizontalDx import ScrollSelectionFormHorizontalDx
        super().init(rectangle, formType)
        formTypeFactory: FormTypeFactory = FormTypeFactory.getInstance()
        if formType == formTypeFactory.HORIZONTAL_FORM:
            self.scrollSelectionFormFormTypeItemIndexPaintable = ScrollSelectionFormHorizontalPaintable(self)
            self.formTypeItemIndexDx = ScrollSelectionFormHorizontalDx(self)
        elif formType == formTypeFactory.VERTICAL_CENTER_FORM:
            self.scrollSelectionFormFormTypeItemIndexPaintable = ScrollSelectionFormVerticalPaintable(self)
            self.formTypeItemIndexDx = ScrollSelectionFormVericalDx(self)
        elif formType == formTypeFactory.TEMP_HORIZONTAL_FORM:
            self.scrollSelectionFormFormTypeItemIndexPaintable = ScrollSelectionFormTempHorizontalPaintable(self)
            self.formTypeItemIndexDx = ScrollSelectionFormTempHorizontalDx(self)
        elif formType == formTypeFactory.NULL_FORM_TYPE:
            pass
        else:
            raise Exception(formTypeFactory.UNK)
    

    def paintItemHorizontal(self, graphics: Graphics, index: int, item: ABCustomItem, x: int, y: int) -> int:
        width: int = item.getMinimumWidth()
        return x + width + self.border
    

    def paintItemVertical(self, graphics: Graphics, index: int, item: ABCustomItem, x: int, y: int) -> int:
        height: int = item.getMinimumHeight()
        return y + height + self.border
    

    def paintItemTempHorizontal(self, graphics: Graphics, index: int, item: ABCustomItem, x: int, y: int) -> int:
        return 0
    

    def getSelectedIndexForPointHorizontalDx(self, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
        return dx - self.halfBorder
    

    def getSelectedIndexForPointVerticalDx(self, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
        return dx + self.getDiffX(item)
    

    def getSelectedIndexForPointTempHorizontalDx(self, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
        return dx + self.getDiffX(item)
    

    def append(self, item: ABCustomItem) -> int:
        return super().append(item)
    

    # throws Exception
    def getSelectedItem(self, point: GPoint) -> ABCustomItem:
        index: int = self.getSelectedIndexForPoint(point)
        if index != -1:
            return self.get(index)
        else:
            return ABCustomItem.getNullInstance()
    

    # throws Exception
    def getItemIndex(self, item: ABCustomItem) -> int:
        nextItem: ABCustomItem = None
        size: int = self.size()
        for index in range(0, size):
            nextItem = self.get(index)
            if nextItem == item:
                return index
        return -1
    

    def getStartIndex(self) -> int:
        return 0
    

    # throws Exception
    def getSelectedIndexForPoint(self, point: GPoint) -> int:
        from org.allbinary.graphics.form.FormTypeFactory import FormTypeFactory
        start: int = self.getStartIndex()
        size: int = self.size()
        dx: int = self.getDx()
        dy: int = self.getDy()
        formTypeFactory: FormTypeFactory = FormTypeFactory.getInstance()
        commonLabels: CommonLabels = CommonLabels.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(commonLabels.START_LABEL)
        stringBuffer.appendint(start)
        stringBuffer.append(CommonSeps.getInstance().SPACE)
        stringBuffer.append(commonLabels.TOTAL_LABEL)
        stringBuffer.appendint(size)
        self.logUtil.putF(str(stringBuffer), self, ScrollSelectionForm.GET_SELECTED_INDEX)
        item: ABCustomItem = None
        width: int = 0
        height: int = 0
        diffX: int = 0
        for index in range(start, size):
            item = self.get(index)
            width = item.getMinimumWidth()
            height = item.getMinimumHeight()
            diffX = self.formTypeItemIndexDx.getDx(index, item, dx, dy)
            if self.rectangleCollisionUtil.isInside(diffX, dy - self.halfBorder, diffX + width + self.border, dy + height + self.halfBorder + 1, point.getX(), point.getY()):
                stringBuffer.delete(0, stringBuffer.length())
                stringBuffer.append(commonLabels.ITEM_LABEL)
                stringBuffer.append(item.getLabel())
                stringBuffer.append(CommonSeps.getInstance().SPACE)
                stringBuffer.append(commonLabels.INDEX_LABEL)
                stringBuffer.appendint(index)
                self.logUtil.putF(str(stringBuffer), self, ScrollSelectionForm.GET_SELECTED_INDEX)
                return index
            if self.formType == formTypeFactory.HORIZONTAL_FORM:
                dx = dx + width + self.border
                if dx > self.rectangle.getMaxX():
                    break
            elif self.formType == formTypeFactory.VERTICAL_CENTER_FORM:
                dy = dy + height + self.border
                if dy > self.rectangle.getMaxY():
                    break
            elif self.formType == formTypeFactory.NULL_FORM_TYPE:
                pass
            else:
                raise Exception(formTypeFactory.UNK)
        return -1
    

    # throws Exception
    def processInputKey(self, gameKeyCode: int) -> int:
        from org.allbinary.graphics.form.FormTypeFactory import FormTypeFactory
        formTypeFactory: FormTypeFactory = FormTypeFactory.getInstance()
        if self.size() == 0:
            return -1
        index: int = self.getSelectedIndex()
        if self.formType == formTypeFactory.HORIZONTAL_FORM or self.formType == formTypeFactory.TEMP_HORIZONTAL_FORM:
            if gameKeyCode == Canvas.RIGHT:
                index += 1
            elif gameKeyCode == Canvas.LEFT:
                index -= 1
        elif self.formType == formTypeFactory.VERTICAL_CENTER_FORM:
            if gameKeyCode == Canvas.DOWN:
                index += 1
            elif gameKeyCode == Canvas.UP:
                index -= 1
        elif self.formType == formTypeFactory.NULL_FORM_TYPE:
            pass
        else:
            raise Exception(formTypeFactory.UNK)
        max: int = self.size() - 1
        if index < 0:
            self.setSelectedIndex(0)
        elif index > max:
            self.setSelectedIndex(max)
        else:
            self.setSelectedIndex(index)
        return -1
    

    def isInForm(self, point: GPoint) -> bool:
        if self.rectangleCollisionUtil.isInside(self.x, self.y - self.halfBorder, self.rectangle.getMaxX() + self.border, self.rectangle.getMaxY() + self.border, point.getX(), point.getY()):
            self.logUtil.putF(str(StringMaker().append(StringUtil.getInstance().toString(point)).append(ScrollSelectionForm.INSIDE_FORM)), self, ScrollSelectionForm.IS_IN_FORM)
            return True
        return False
    

    # throws Exception
    def paintItem(self, graphics: Graphics, index: int, item: ABCustomItem, x: int, y: int) -> int:
        item.paintXY(graphics, x, y)
        width: int = item.getMinimumWidth()
        height: int = item.getMinimumHeight()
        graphics.setColor(int(self.getButtonBasicColor()))
        adjustedBorder: int = 3
        graphics.drawRect(x - self.halfBorder - adjustedBorder, y - self.halfBorder - adjustedBorder, width + self.border + self.adjustedExtraBorder, height + self.border + self.adjustedExtraBorder)
        return self.scrollSelectionFormFormTypeItemIndexPaintable.paint(graphics, index, item, x, y)
    

    # throws Exception
    def paintUnselectedItem(self, graphics: Graphics, index: int, item: ABCustomItem, x: int, y: int) -> int:
        graphics.setColor(int(self.getButtonBasicColor()))
        item.paintUnselected(graphics, x, y)
        return self.scrollSelectionFormFormTypeItemIndexPaintable.paint(graphics, index, item, x, y)
    

    def getDiffX(self, item: ABCustomItem) -> int:
        return 0
    

    def getDx(self) -> int:
        return self.x
    

    def getDy(self) -> int:
        return self.y
    

    def setButtonBasicColor(self, buttonBasicColor: BasicColor) -> None:
        self.buttonBasicColor = buttonBasicColor
    

    def getButtonBasicColor(self) -> BasicColor:
        return self.buttonBasicColor
# from javax.microedition.lcdui.Canvas import Canvas
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.math.RectangleCollisionUtil import RectangleCollisionUtil
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.graphics.form.ItemPaintableFactory import ItemPaintableFactory
from org.allbinary.graphics.form.ItemIndexPaintable import ItemIndexPaintable
from org.allbinary.graphics.form.ItemIndexDx import ItemIndexDx


