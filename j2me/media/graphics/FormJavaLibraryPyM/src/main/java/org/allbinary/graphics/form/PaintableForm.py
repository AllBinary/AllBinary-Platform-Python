# Generated Code Do Not Modify
# package org.allbinary.graphics.form

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.graphics.form.ABCustomForm import ABCustomForm


class PaintableForm(ABCustomForm):
    NULL_PAINTABLE_FORM: object = None

    def _init_fields(self) -> None:
        from org.allbinary.graphics.Rectangle import Rectangle
        from org.allbinary.graphics.RectangleFactory import RectangleFactory
        from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
        self.canvasStrings: CanvasStrings = CanvasStrings.getInstance()
        self.rectangle: Rectangle = RectangleFactory.SINGLETON
        self.x: int = 0
        self.y: int = 0
        self.formType: FormType = FormTypeFactory.getInstance().NULL_FORM_TYPE
    

    @staticmethod
    def getNullPaintableForm() -> PaintableForm:
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
        from org.allbinary.logic.NullUtil import NullUtil
        from org.allbinary.logic.string.StringUtil import StringUtil
        if PaintableForm.NULL_PAINTABLE_FORM == NullUtil.getInstance().NULL_OBJECT:
            PaintableForm.NULL_PAINTABLE_FORM = PaintableForm(StringUtil.getInstance().EMPTY_STRING, [None] * (0), BasicColorFactory.getInstance().BLACK, BasicColorFactory.getInstance().WHITE)
        return PaintableForm.NULL_PAINTABLE_FORM
    

    def __init__(self, title: str, items: list[ABCustomItem], backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
        super().__init__(title, items, backgroundBasicColor, foregroundBasicColor)
        self._init_fields()
        self.setSelectedIndex(0)
    

    # throws Exception
    def init(self, rectangle: Rectangle, formType: FormType) -> None:
        from org.allbinary.graphics.GPoint import GPoint
        from org.allbinary.graphics.Rectangle import Rectangle
        self.rectangle = rectangle
        point: GPoint = self.rectangle.getPoint()
        self.x = point.getX()
        self.y = point.getY()
        self.formType = formType
    

    def getWidth(self) -> int:
        return self.rectangle.getWidth()
# from org.allbinary.graphics.GPoint import GPoint
# from org.allbinary.graphics.Rectangle import Rectangle
# from org.allbinary.graphics.RectangleFactory import RectangleFactory
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
# from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
# from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.graphics.form.FormTypeFactory import FormTypeFactory


def _PaintableForm_NULL_PAINTABLE_FORM() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(PaintableForm, "NULL_PAINTABLE_FORM", _PaintableForm_NULL_PAINTABLE_FORM)

