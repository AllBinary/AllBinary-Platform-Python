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



class OrderedIntArrayPermutationUtil:
    instance: OrderedIntArrayPermutationUtil = None

    def _init_fields(self) -> None:
        self.TOTAL_ITERATIONS_TABLE: str = "Total Iterations: "
        self.FINISHED: str = "\nFINISHED"
    

    @staticmethod
    def getInstance() -> OrderedIntArrayPermutationUtil:
        return OrderedIntArrayPermutationUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getNext(self, data: list[int]) -> None:
        length: int = len(data)
        i: int = length - 1
        while data[i - 1] >= data[i]:
            i = i - 1
        j: int = length
        while data[j - 1] <= data[i - 1]:
            j = j - 1
        self.swap(data, i - 1, j - 1)
        i += 1
        j = length
        while i < j:
            self.swap(data, i - 1, j - 1)
            i += 1
            j -= 1
    

    def swap(self, data: list[int], a: int, b: int) -> None:
        temp: int = data[a]
        data[a] = data[b]
        data[b] = temp
    

    def factorial(self, dataLength: int) -> int:
        temp: int = 1
        if dataLength > 1:
            for i in range(1, dataLength + 1):
                temp *= i
        return temp
    

    def generate(self, data: list[int], visitor: Visitor) -> None:
        iterations: int = self.factorial(len(data))
        print(self.TOTAL_ITERATIONS_TABLE, end="")
        print(iterations)
        for count in range(0, iterations - 1):
            self.getNext(data)
            visitor.visit(self)
        print(self.FINISHED)
    

    @staticmethod
    def main(args: list[str]) -> None:
        from org.allbinary.logic.math.permutations.IntPermutationVisitor import IntPermutationVisitor
        TOTAL: int = 3
        data: list[int] = [0] * (TOTAL)
        for i in range(0, TOTAL):
            data[i] = i
        permutationVisitor: IntPermutationVisitor = IntPermutationVisitor(data)
        ORIGINAL_DATA_LABEL: str = "Original Data: "
        print(ORIGINAL_DATA_LABEL, end="")
        permutationVisitor.print_(data)
        OrderedIntArrayPermutationUtil.getInstance().generate(data, permutationVisitor)
from org.allbinary.logic.util.visitor.Visitor import Visitor


OrderedIntArrayPermutationUtil.instance = OrderedIntArrayPermutationUtil()

