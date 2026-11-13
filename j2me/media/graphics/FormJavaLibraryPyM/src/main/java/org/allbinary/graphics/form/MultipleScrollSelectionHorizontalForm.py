# Generated Code Do Not Modify
# package org.allbinary.graphics.form

from __future__ import annotations

from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.graphics.paint.Paintable import Paintable
from org.allbinary.graphics.form.ScrollSelectionForm import ScrollSelectionForm
from org.allbinary.graphics.form.ItemIndexPaintable import ItemIndexPaintable
from org.allbinary.graphics.form.ItemIndexPaintable import ItemIndexPaintable


class MultipleScrollSelectionHorizontalForm(ScrollSelectionForm, UpdateMyFontInterface):
    class MultipleScrollSelectionFormHorizontalPaintable(ItemIndexPaintable):

        def _init_fields(self) -> None:
            self.multipleScrollSelectionForm: MultipleScrollSelectionHorizontalForm = None
        

        def __init__(self, multipleScrollSelectionForm: MultipleScrollSelectionHorizontalForm) -> None:
            super().__init__()
            self._init_fields()
            self.multipleScrollSelectionForm = multipleScrollSelectionForm
        

        # throws Exception
        def paint(self, graphics: Graphics, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
            from javax.microedition.lcdui.Graphics import Graphics
            from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
            return self.multipleScrollSelectionForm.paintHorizontal(graphics, index, item, dx, dy)
    class MultipleScrollSelectionFormVerticalPaintable(ItemIndexPaintable):

        def _init_fields(self) -> None:
            self.multipleScrollSelectionForm: MultipleScrollSelectionHorizontalForm = None
        

        def __init__(self, multipleScrollSelectionForm: MultipleScrollSelectionHorizontalForm) -> None:
            super().__init__()
            self._init_fields()
            self.multipleScrollSelectionForm = multipleScrollSelectionForm
        

        # throws Exception
        def paint(self, graphics: Graphics, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
            from javax.microedition.lcdui.Graphics import Graphics
            from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
            return self.multipleScrollSelectionForm.paintVertical(graphics, index, item, dx, dy)
    class MultipleScrollSelectionFormRectPaintable(Paintable):

        def _init_fields(self) -> None:
            self.multipleScrollSelectionForm: MultipleScrollSelectionHorizontalForm = None
        

        def __init__(self, multipleScrollSelectionForm: MultipleScrollSelectionHorizontalForm) -> None:
            super().__init__()
            self._init_fields()
            self.multipleScrollSelectionForm = multipleScrollSelectionForm
        

        def paint(self, graphics: Graphics) -> None:
            from javax.microedition.lcdui.Graphics import Graphics
            self.multipleScrollSelectionForm.fillRect(graphics)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
        from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
        from org.allbinary.graphics.paint.NullPaintable import NullPaintable
        self.rectPaintable: Paintable = NullPaintable.getInstance()
        self.multipleScrollSelectionHorizontalFormTypeItemIndexPaintable: ItemIndexPaintable = ItemIndexPaintable.getInstance()
        self.backgroundColor: int = int(BasicColorFactory.getInstance().TRANSPARENT_GREY)
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.logged: bool = False
        self.fontHeight: int = 0
    

    # throws Exception
    @staticmethod
    def createForm(title: str, items: list[ABCustomItem], rectangle: Rectangle, formType: FormType, border: int, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> ScrollSelectionForm:
        from org.allbinary.graphics.form.ItemPaintableFactory import ItemPaintableFactory
        from org.allbinary.graphics.Rectangle import Rectangle
        from org.allbinary.graphics.color.BasicColor import BasicColor
        from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
        scrollSelectionForm: ScrollSelectionForm = MultipleScrollSelectionHorizontalForm(title, items, ItemPaintableFactory.getInstance(), border, backgroundBasicColor, foregroundBasicColor)
        scrollSelectionForm.init(rectangle, formType)
        return scrollSelectionForm
    

    def __init__(self, title: str, items: list[ABCustomItem], formPaintableFactory: ItemPaintableFactory, border: int, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        from org.allbinary.J2MEUtil import J2MEUtil
        from org.allbinary.graphics.color.BasicColor import BasicColor
        from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
        super().__init__(title, items, formPaintableFactory, border, 3, backgroundBasicColor, foregroundBasicColor)
        self._init_fields()
        if J2MEUtil.isJ2ME() or J2MEUtil.isHTML():
            pass
        else:
            self.rectPaintable = MultipleScrollSelectionFormRectPaintable(self)
    

    def fillRect(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        graphics.setColor(self.backgroundColor)
        graphics.fillRect(self.x, self.y, self.rectangle.getWidth(), self.rectangle.getHeight())
    

    # throws Exception
    def init(self, rectangle: Rectangle, formType: FormType) -> None:
        from org.allbinary.graphics.form.FormTypeFactory import FormTypeFactory
        from org.allbinary.graphics.Rectangle import Rectangle
        super().init(rectangle, formType)
        formTypeFactory: FormTypeFactory = FormTypeFactory.getInstance()
        if formType == formTypeFactory.HORIZONTAL_FORM:
            self.multipleScrollSelectionHorizontalFormTypeItemIndexPaintable = MultipleScrollSelectionFormHorizontalPaintable(self)
        elif formType == formTypeFactory.VERTICAL_CENTER_FORM:
            self.multipleScrollSelectionHorizontalFormTypeItemIndexPaintable = MultipleScrollSelectionFormVerticalPaintable(self)
        elif formType == formTypeFactory.NULL_FORM_TYPE:
            pass
        else:
            raise Exception(formTypeFactory.UNK)
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Font import Font
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
        font: Font = graphics.getFont()
        self.fontHeight = font.getHeight()
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    # throws Exception
    def paintHorizontal(self, graphics: Graphics, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
        dx2: int = self.paintItem(graphics, index, item, dx, dy) + self.border
        self.paintable.paint(graphics, index, dx, dy)
        dx = dx2
        return dx
    

    # throws Exception
    def paintVertical(self, graphics: Graphics, index: int, item: ABCustomItem, dx: int, dy: int) -> int:
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
        self.paintItem(graphics, index, item, dx, dy)
        self.paintable.paint(graphics, index, dx, dy)
        return dx
    

    def getStartIndex(self) -> int:
        return self.getSelectedIndex()
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        try:
            self.myFontProcessor.process(graphics)
            start: int = self.getStartIndex()
            size: int = self.size()
            dx: int = self.x
            dy: int = self.y
            self.rectPaintable.paint(graphics)
            graphics.drawString(self.getTitle(), self.x, self.y - self.fontHeight, 0)
            item: ABCustomItem = None
            for index in range(start, size):
                item = self.get(index)
                if dx >= self.rectangle.getMaxX():
                    if self.logged:
                        pass
                    else:
                        self.logged = True
                        PreLogUtil.put(str(StringMaker().append("painting beyond maxx: ").appendint(int(self.rectangle.getMaxX()))), self, self.canvasStrings.PAINT)
                dx = self.multipleScrollSelectionHorizontalFormTypeItemIndexPaintable.paint(graphics, index, item, dx, dy)
        except Exception as e:
            PreLogUtil.put(self.commonStrings.EXCEPTION, self, self.canvasStrings.PAINT)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.J2MEUtil import J2MEUtil
# from org.allbinary.graphics.Rectangle import Rectangle
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
# from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
# from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
# from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
# from org.allbinary.graphics.paint.NullPaintable import NullPaintable
# from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.graphics.form.ItemIndexPaintable import ItemIndexPaintable


