# Generated Code Do Not Modify
# package org.allbinary.animation

from __future__ import annotations



class PolygonRasterizer:
    instance: PolygonRasterizer = None
    

    @staticmethod
    def getInstance() -> PolygonRasterizer:
        return PolygonRasterizer.instance
    

    def getPixelBuffer(self, svgPath: str, pathX: list[int], pathY: list[int], pixelBuffer: list[int], width: int, height: int) -> list[int]:
        from org.allbinary.animation.PathParser import PathParser
        pointCount: int = PathParser.parsePath(svgPath, pathX, pathY, len(pathX))
        for i in range(0, len(pixelBuffer)):
            pixelBuffer[i] = 0xFFFFFFFF
        PolygonRasterizer.getInstance().fillPolygon(pathX, pathY, pointCount, pixelBuffer, width, height, 0xFFFF00FF)
        return pixelBuffer
    

    def fillPolygon(self, polyX: list[int], polyY: list[int], numPoints: int, buffer: list[int], width: int, height: int, colorRGB: int) -> None:
        from org.allbinary.animation.FixedPoint import FixedPoint
        if numPoints < 3:
            return
        fixedPoint: FixedPoint = FixedPoint.getInstance()
        x: list[int] = [0] * (numPoints)
        y: list[int] = [0] * (numPoints)
        minY: int = height
        maxY: int = 0
        for i in range(0, numPoints):
            x[i] = fixedPoint.toInt(polyX[i])
            y[i] = fixedPoint.toInt(polyY[i])
            if y[i] < minY:
                minY = y[i]
            if y[i] > maxY:
                maxY = y[i]
        if minY < 0:
            minY = 0
        if maxY >= height:
            maxY = height - 1
        scanlineX: list[int] = [0] * (numPoints)
        for scanY in range(minY, maxY + 1):
            intersectCount: int = 0
            for i in range(0, numPoints):
                next: int = (i + 1) % numPoints
                x1: int = x[i]
                y1: int = y[i]
                x2: int = x[next]
                y2: int = y[next]
                if (y1 < scanY and y2 >= scanY) or (y2 < scanY and y1 >= scanY):
                    if y2 != y1:
                        interX: int = x1 + int((scanY - y1) * (x2 - x1) / (y2 - y1))
                        scanlineX[((intersectCount := intersectCount + 1) - 1)] = interX
            for i in range(0, intersectCount - 1):
                for j in range(i + 1, intersectCount):
                    if scanlineX[i] > scanlineX[j]:
                        temp: int = scanlineX[i]
                        scanlineX[i] = scanlineX[j]
                        scanlineX[j] = temp
            for i in range(0, intersectCount, 2):
                if i + 1 >= intersectCount:
                    break
                startX: int = scanlineX[i]
                endX: int = scanlineX[i + 1]
                if startX < 0:
                    startX = 0
                if endX >= width:
                    endX = width - 1
                rowOffset: int = scanY * width
                for pixelX in range(startX, endX + 1):
                    buffer[rowOffset + pixelX] = colorRGB
    

    def main(self, args: list[str]) -> None:
        width: int = 100
        height: int = 100
        pathX: list[int] = [0] * (200)
        pathY: list[int] = [0] * (200)
        pixelBuffer: list[int] = [0] * (width * height)
        svgPath: str = "M 32.139812,81.554575 14.450128,74.294372 V 50.000034 25.705697 l 17.73231,-7.268329 C 41.935209,14.439788 49.953112,11.168898 50,11.168723 c 0.04689,-1.74e-4 8.064791,3.270238 17.817562,7.267583 l 17.73231,7.267899 V 50 74.295795 l -17.73231,7.2679 c -9.752771,3.997344 -17.789855,7.264116 -17.860188,7.259492 -0.07033,-0.0046 -8.088235,-3.275499 -17.817562,-7.268612 z"
        PolygonRasterizer.getInstance().getPixelBuffer(svgPath, pathX, pathY, pixelBuffer, width, height)


PolygonRasterizer.instance = PolygonRasterizer()

