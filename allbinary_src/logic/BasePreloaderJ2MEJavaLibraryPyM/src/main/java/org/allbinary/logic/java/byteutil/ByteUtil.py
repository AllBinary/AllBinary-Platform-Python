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
# package org.allbinary.logic.java.byteutil

from __future__ import annotations



class ByteUtil:
    instance: ByteUtil = None
    

    @staticmethod
    def getInstance() -> ByteUtil:
        return ByteUtil.instance
    

    def __init__(self) -> None:
        pass
    

    def xor(self, array: list[int], mask: int) -> list[int]:
        bytes: list[int] = [0] * (len(array))
        size: int = len(array)
        index: int = 0
        currentByte: int = 0
        while index < size:
            currentByte = array[index]
            bytes[index] = ((int((currentByte ^ mask)) + 128) % 256 - 128)
            index += 1
        return bytes
    

    def not_(self, array: list[int]) -> list[int]:
        bytes: list[int] = [0] * (len(array))
        size: int = len(array)
        index: int = 0
        while index < size:
            bytes[index] = ((int(~array[index]) + 128) % 256 - 128)
            index += 1
        return bytes
    

    def xorByte(self, array: list[int], index: int) -> list[int]:
        mask: int = 0
        if index == 0:
            mask = 1
        if index == 1:
            mask = 2
        if index == 2:
            mask = 4
        if index == 3:
            mask = 8
        if index == 4:
            mask = 16
        if index == 5:
            mask = 32
        if index == 6:
            mask = 64
        if index == 7:
            mask = ((int(-127) + 128) % 256 - 128)
        return self.xor(array, mask)
    

    def compare(self, newByteArray: list[int], oldByteArray: list[int]) -> bool:
        if len(newByteArray) != len(oldByteArray):
            return False
        else:
            pass
        size: int = len(newByteArray)
        for index in range(0, size):
            if newByteArray[index] != oldByteArray[index]:
                return False
        return True
    

    def compareWithStats(self, newByteArray: list[int], newSize: int, oldByteArray: list[int], stats: list[int]) -> bool:
        if newSize != len(oldByteArray):
            stats[0] = -1
            stats[2] = newSize
            stats[3] = len(oldByteArray)
            return False
        else:
            stats[0] = newSize
        stats[1] = 0
        size: int = newSize
        for index in range(0, size):
            if newByteArray[index] != oldByteArray[index]:
                return False
            stats[1] += 1
        return True


ByteUtil.instance = ByteUtil()

