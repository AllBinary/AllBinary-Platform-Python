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
# package org.allbinary.logic.math.permutations

from __future__ import annotations



class OrderedObjectArrayPermutationUtil:
    instance: OrderedObjectArrayPermutationUtil = None

    def _init_fields(self) -> None:
        self.TOTAL_ITERATIONS_TABLE: str = "Total Iterations: "
        self.FINISHED: str = "\nFINISHED"
    

    @staticmethod
    def getInstance() -> OrderedObjectArrayPermutationUtil:
        return OrderedObjectArrayPermutationUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getNext(self, data: list[object]) -> None:
        length: int = len(data)
        i: int = length - 1
        tsUtil: TsUtil = TsUtil.getInstance()
        while tsUtil.hashCode(data[i - 1]) >= tsUtil.hashCode(data[i]):
            i = i - 1
        j: int = length
        while tsUtil.hashCode(data[j - 1]) <= tsUtil.hashCode(data[i - 1]):
            j = j - 1
        self.swap(data, i - 1, j - 1)
        i += 1
        j = length
        while i < j:
            self.swap(data, i - 1, j - 1)
            i += 1
            j -= 1
    

    def swap(self, data: list[object], a: int, b: int) -> None:
        temp: object = data[a]
        data[a] = data[b]
        data[b] = temp
    

    def factorial(self, dataLength: int) -> int:
        temp: int = 1
        if dataLength > 1:
            for i in range(1, dataLength + 1):
                temp *= i
        return temp
    

    def generate(self, data: list[object], visitor: Visitor) -> None:
        iterations: int = self.factorial(len(data))
        print(self.TOTAL_ITERATIONS_TABLE, end="")
        print(iterations)
        for count in range(0, iterations - 1):
            self.getNext(data)
            visitor.visit(self)
        print(self.FINISHED)
    

    @staticmethod
    def main(args: list[str]) -> None:
        from org.allbinary.logic.math.permutations.ComparableObject import ComparableObject
        from org.allbinary.logic.math.permutations.ObjectPermutationVisitor import ObjectPermutationVisitor
        TOTAL: int = 7
        data: list[object] = [None] * (TOTAL)
        for i in range(0, TOTAL):
            data[i] = ComparableObject()
        Arrays.sort(data)
        permutationVisitor: ObjectPermutationVisitor = ObjectPermutationVisitor(data)
        ORIGINAL_DATA_LABEL: str = "Original Data: "
        print(ORIGINAL_DATA_LABEL, end="")
        permutationVisitor.visit(data)
        OrderedObjectArrayPermutationUtil.getInstance().generate(data, permutationVisitor)
# from java.util.Arrays import Arrays
from org.allbinary.TsUtil import TsUtil
from org.allbinary.logic.util.visitor.Visitor import Visitor


OrderedObjectArrayPermutationUtil.instance = OrderedObjectArrayPermutationUtil()

