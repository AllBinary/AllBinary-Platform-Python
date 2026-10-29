# Generated Code Do Not Modify
# package org.allbinary.animation

from __future__ import annotations



class PathParser:
    

    @staticmethod
    def tokenize(d: str) -> list[str]:
        from org.allbinary.animation.StringBuffer import StringBuffer
        tokens: BasicArrayList = BasicArrayListD()
        sb: StringBuffer = StringBuffer()
        for i in range(0, len(d)):
            c: str = d[i]
            if c == ' ' or c == ',' or c == '\t' or c == '\n' or c == '\r':
                if sb.length() > 0:
                    tokens.add(str(sb))
                    sb.setLength(0)
            elif c == 'M' or c == 'm' or c == 'L' or c == 'l' or c == 'V' or c == 'v' or c == 'C' or c == 'c' or c == 'Z' or c == 'z':
                if sb.length() > 0:
                    tokens.add(str(sb))
                    sb.setLength(0)
                tokens.add(str(c))
            else:
                sb.append(c)
        if sb.length() > 0:
            tokens.add(str(sb))
        res: list[str] = [None] * (tokens.size())
        tokens.toArrayType(res)
        return res
    

    @staticmethod
    def parsePath(d: str, outX: list[int], outY: list[int], maxPoints: int) -> int:
        from org.allbinary.animation.FixedPoint import FixedPoint
        from org.allbinary.animation.PGUtil import PGUtil
        tokens: list[str] = PathParser.tokenize(d)
        count: list[int] = [0]
        fixedPoint: FixedPoint = FixedPoint.getInstance()
        curX: int = 0
        curY: int = 0
        startX: int = 0
        startY: int = 0
        idx: int = 0
        while idx < len(tokens):
            tok: str = tokens[((idx := idx + 1) - 1)]
            cmd: str = tok[0]
            if cmd == 'M' or cmd == 'm':
                x: int = fixedPoint.toFixed(float(tokens[((idx := idx + 1) - 1)]))
                y: int = fixedPoint.toFixed(float(tokens[((idx := idx + 1) - 1)]))
                if cmd == 'm':
                    x += curX
                    y += curY
                curX = x
                curY = y
                startX = x
                startY = y
                outX[count[0]] = curX
                outY[count[0]] = curY
                count[0] += 1
            elif cmd == 'L' or cmd == 'l':
                x: int = fixedPoint.toFixed(float(tokens[((idx := idx + 1) - 1)]))
                y: int = fixedPoint.toFixed(float(tokens[((idx := idx + 1) - 1)]))
                if cmd == 'l':
                    x += curX
                    y += curY
                curX = x
                curY = y
                outX[count[0]] = curX
                outY[count[0]] = curY
                count[0] += 1
            elif cmd == 'V' or cmd == 'v':
                y: int = fixedPoint.toFixed(float(tokens[((idx := idx + 1) - 1)]))
                if cmd == 'v':
                    y += curY
                curY = y
                outX[count[0]] = curX
                outY[count[0]] = curY
                count[0] += 1
            elif cmd == 'C' or cmd == 'c':
                x1: int = fixedPoint.toFixed(float(tokens[((idx := idx + 1) - 1)]))
                y1: int = fixedPoint.toFixed(float(tokens[((idx := idx + 1) - 1)]))
                x2: int = fixedPoint.toFixed(float(tokens[((idx := idx + 1) - 1)]))
                y2: int = fixedPoint.toFixed(float(tokens[((idx := idx + 1) - 1)]))
                x3: int = fixedPoint.toFixed(float(tokens[((idx := idx + 1) - 1)]))
                y3: int = fixedPoint.toFixed(float(tokens[((idx := idx + 1) - 1)]))
                if cmd == 'c':
                    x1 += curX
                    y1 += curY
                    x2 += curX
                    y2 += curY
                    x3 += curX
                    y3 += curY
                PGUtil.getInstance().flattenCubicBezier(curX, curY, x1, y1, x2, y2, x3, y3, outX, outY, count, maxPoints)
                curX = x3
                curY = y3
            elif cmd == 'Z' or cmd == 'z':
                curX = startX
                curY = startY
                outX[count[0]] = curX
                outY[count[0]] = curY
                count[0] += 1
            while idx < len(tokens) and not PathParser.isCommand(tokens[idx]):
                if cmd == 'M' or cmd == 'm' or cmd == 'L' or cmd == 'l':
                    x: int = fixedPoint.toFixed(float(tokens[((idx := idx + 1) - 1)]))
                    y: int = fixedPoint.toFixed(float(tokens[((idx := idx + 1) - 1)]))
                    if cmd == 'm' or cmd == 'l':
                        x += curX
                        y += curY
                    curX = x
                    curY = y
                    outX[count[0]] = curX
                    outY[count[0]] = curY
                    count[0] += 1
                elif cmd == 'V' or cmd == 'v':
                    y: int = fixedPoint.toFixed(float(tokens[((idx := idx + 1) - 1)]))
                    if cmd == 'v':
                        y += curY
                    curY = y
                    outX[count[0]] = curX
                    outY[count[0]] = curY
                    count[0] += 1
        return count[0]
    

    @staticmethod
    def isCommand(tok: str) -> bool:
        c: str = tok[0]
        return "MmLlVvCcZz".find(c) >= 0
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil


