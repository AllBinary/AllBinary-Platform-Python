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
# package org.allbinary.animation

from __future__ import annotations

import math
import traceback


class SVGAsJSONSimpleLoader:
    instance: SVGAsJSONSimpleLoader = None

    def _init_fields(self) -> None:
        self.graphicsStrings: GraphicsStrings = GraphicsStrings.getInstance()
        self.shapeTypeFactory: ShapeTypeFactory = ShapeTypeFactory.getInstance()
        self.KEY_SVG: str = "svg"
        self.KEY_X1: str = "x1"
        self.KEY_Y1: str = "y1"
        self.KEY_X2: str = "x2"
        self.KEY_Y2: str = "y2"
        self.KEY_CX: str = "cx"
        self.KEY_CY: str = "cy"
        self.KEY_R: str = "r"
        self.KEY_X: str = PositionStrings.getInstance().X
        self.KEY_Y: str = PositionStrings.getInstance().Y
        self.ERROR_PARSE_SVG_JSON: str = "Unable to parse SVG JSON"
        self.ERROR_MISSING_KEY_PREFIX: str = "Missing key: "
        self.ERROR_INVALID_NUMBER_PREFIX: str = "Invalid number for key: "
        self.ERROR_EXPECTED_OBJECT_PREFIX: str = "Expected object for: "
        self.EMPTY_POINTS: list[list[int]] = PrimitiveIntUtil.getTwoDimensionalArrayInstance()
        self.SHAPE_SEPARATOR: list[int] = [1000, 1000]
        self.CIRCLE_SEGMENTS: int = 16

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> SVGAsJSONSimpleLoader:
        return SVGAsJSONSimpleLoader.instance
    

    # throws Exception
    def load(self, svgAsJson: str) -> list[list[int]]:
        if svgAsJson is None:
            return self.EMPTY_POINTS
        try:
            root: JSONObject = JSONObject(svgAsJson)
            svgValue: object = root.opt(self.KEY_SVG)
            svg: JSONObject = (root if svgValue is None else self.asObject(svgValue, self.KEY_SVG))
            pointVector: BasicArrayList = BasicArrayListD()
            keys: Enumeration = svg.keys()
            while keys.hasMoreElements():
                key: str = keys.nextElement()
                value: object = svg.opt(key)
                if self.shapeTypeFactory.KEY_LINE.equals(key):
                    self.addShapes(pointVector, value, self.shapeTypeFactory.LINE)
                elif self.shapeTypeFactory.equals(key):
                    self.addShapes(pointVector, value, self.shapeTypeFactory.CIRCLE)
                elif self.shapeTypeFactory.KEY_RECT.equals(key) or self.shapeTypeFactory.KEY_RECTANGLE.equals(key):
                    self.addShapes(pointVector, value, self.shapeTypeFactory.RECTANGLE)
            return self.toPoints(pointVector)
        except JSONException as e:
            raise ValueError(self.ERROR_PARSE_SVG_JSON, e)
    

    # throws Exception
    def addShapes(self, pointVector: BasicArrayList, value: object, shapeType: ShapeType) -> None:
        if isinstance(value, JSONArray):
            array: JSONArray = value
            size: int = array.length()
            for index in range(0, size):
                self.addShape(pointVector, array.opt(index), shapeType)
        else:
            self.addShape(pointVector, value, shapeType)
    

    # throws Exception
    def addShape(self, pointVector: BasicArrayList, value: object, shapeType: ShapeType) -> None:
        shape: JSONObject = self.asObject(value, shapeType.getName())
        if shapeType == self.shapeTypeFactory.LINE:
            self.addLine(pointVector, shape)
        elif shapeType == self.shapeTypeFactory.CIRCLE:
            self.addCircle(pointVector, shape)
        else:
            self.addRectangle(pointVector, shape)
    

    # throws Exception
    def addLine(self, pointVector: BasicArrayList, line: JSONObject) -> None:
        self.addPoint(pointVector, self.readInt(line, self.KEY_X1), self.readInt(line, self.KEY_Y1))
        self.addPoint(pointVector, self.readInt(line, self.KEY_X2), self.readInt(line, self.KEY_Y2))
        self.addSeparator(pointVector)
    

    # throws Exception
    def addCircle(self, pointVector: BasicArrayList, circle: JSONObject) -> None:
        cx: int = self.readInt(circle, self.KEY_CX)
        cy: int = self.readInt(circle, self.KEY_CY)
        radius: int = self.readInt(circle, self.KEY_R)
        for index in range(0, self.CIRCLE_SEGMENTS + 1):
            angle: float = (Math.PI * 2.0 * index) / self.CIRCLE_SEGMENTS
            x: int = int(int(math.floor(cx + (math.cos(angle) * radius) + 0.5)))
            y: int = int(int(math.floor(cy + (math.sin(angle) * radius) + 0.5)))
            self.addPoint(pointVector, x, y)
        self.addSeparator(pointVector)
    

    # throws Exception
    def addRectangle(self, pointVector: BasicArrayList, rectangle: JSONObject) -> None:
        x: int = self.readInt(rectangle, self.KEY_X, 0)
        y: int = self.readInt(rectangle, self.KEY_Y, 0)
        width: int = self.readInt(rectangle, self.graphicsStrings.WIDTH)
        height: int = self.readInt(rectangle, self.graphicsStrings.HEIGHT)
        self.addPoint(pointVector, x, y)
        self.addPoint(pointVector, x + width, y)
        self.addPoint(pointVector, x + width, y + height)
        self.addPoint(pointVector, x, y + height)
        self.addPoint(pointVector, x, y)
        self.addSeparator(pointVector)
    

    def addPoint(self, pointVector: BasicArrayList, x: int, y: int) -> None:
        pointVector.add([x, y])
    

    def addSeparator(self, pointVector: BasicArrayList) -> None:
        pointVector.add([self.SHAPE_SEPARATOR[0], self.SHAPE_SEPARATOR[1]])
    

    # throws Exception
    def readInt(self, anyType: JSONObject, key: str) -> int:
        value: object = anyType.get(key)
        if value is None:
            raise ValueError(self.ERROR_MISSING_KEY_PREFIX + key)
        return self.toInt(value, key)
    

    # Java overloaded method: Python keeps the last definition
    def readInt(self, anyType: JSONObject, key: str, defaultValue: int) -> int:
        try:
            if anyType.has(key):
                value: object = anyType.get(key)
                return self.toInt(value, key)
        except Exception as e:
            traceback.print_exception(e)
        return defaultValue
    

    def toInt(self, value: object, key: str) -> int:
        if isinstance(value, Number):
            return int(int(math.floor(float((value)) + 0.5)))
        if isinstance(value, str):
            return int(int(math.floor(float(value) + 0.5)))
        raise ValueError(self.ERROR_INVALID_NUMBER_PREFIX + key)
    

    def asObject(self, value: object, name: str) -> JSONObject:
        if isinstance(value, JSONObject):
            return value
        raise ValueError(self.ERROR_EXPECTED_OBJECT_PREFIX + name)
    

    def toPoints(self, pointVector: BasicArrayList) -> list[list[int]]:
        if pointVector.size() == 0:
            return self.EMPTY_POINTS
        points: list[list[int]] = [[0] * (2) for _ in range(pointVector.size())]
        for index in range(0, pointVector.size()):
            point: list[int] = pointVector.get(index)
            points[index] = point
        return points
    

    # throws Exception
    @staticmethod
    def main(args: list[str]) -> None:
        svgAsJson: str = "{\"svg\": {\n" + "    \"rect\": {\n" + "        \"width\": 20,\n" + "        \"fill\": \"#008c00\",\n" + "        \"height\": 20\n" + "    },\n" + "    \"xmlns\": \"http://www.w3.org/2000/svg\",\n" + "    \"width\": 20,\n" + "    \"height\": 20\n" + "}}\n"
        points: list[list[int]] = SVGAsJSONSimpleLoader.getInstance().load(svgAsJson)
        stringBuilder: StringMaker = StringMaker()
        size: int = len(points)
        for index in range(0, size):
            size2: int = len(points[index])
            for index2 in range(0, size2):
                stringBuilder.appendint(int(points[index][index2]))
                stringBuilder.append(CommonSeps.getInstance().COMMA)
        print(str(stringBuilder))
# from java.util.Enumeration import Enumeration
from org.allbinary.graphics.GraphicsStrings import GraphicsStrings
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.math.PositionStrings import PositionStrings
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.json.me.JSONArray import JSONArray
from org.json.me.JSONException import JSONException
from org.json.me.JSONObject import JSONObject
from org.allbinary.animation.ShapeTypeFactory import ShapeTypeFactory


SVGAsJSONSimpleLoader.instance = SVGAsJSONSimpleLoader()

