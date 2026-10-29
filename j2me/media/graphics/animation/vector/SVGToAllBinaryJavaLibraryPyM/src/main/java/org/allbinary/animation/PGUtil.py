# Generated Code Do Not Modify
# package org.allbinary.animation

from __future__ import annotations



class PGUtil:
    instance: PGUtil = None
    

    @staticmethod
    def getInstance() -> PGUtil:
        return PGUtil.instance
    

    def flattenCubicBezier(self, x0: int, y0: int, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, outX: list[int], outY: list[int], count: list[int], maxPoints: int) -> None:
        from org.allbinary.animation.FixedPoint import FixedPoint
        fixedPoint: FixedPoint = FixedPoint.getInstance()
        steps: int = 10
        for i in range(1, steps + 1):
            t: int = fixedPoint.div(fixedPoint.toFixed(float(i)), fixedPoint.toFixed(steps))
            mt: int = fixedPoint.ONE - t
            mt3: int = fixedPoint.mul(fixedPoint.mul(mt, mt), mt)
            mt2t3: int = 3 * fixedPoint.mul(fixedPoint.mul(mt, mt), t)
            mtt23: int = 3 * fixedPoint.mul(fixedPoint.mul(mt, t), t)
            t3: int = fixedPoint.mul(fixedPoint.mul(t, t), t)
            x: int = fixedPoint.mul(mt3, x0) + fixedPoint.mul(mt2t3, x1) + fixedPoint.mul(mtt23, x2) + fixedPoint.mul(t3, x3)
            y: int = fixedPoint.mul(mt3, y0) + fixedPoint.mul(mt2t3, y1) + fixedPoint.mul(mtt23, y2) + fixedPoint.mul(t3, y3)
            if count[0] < maxPoints:
                outX[count[0]] = x
                outY[count[0]] = y
                count[0] += 1


PGUtil.instance = PGUtil()

