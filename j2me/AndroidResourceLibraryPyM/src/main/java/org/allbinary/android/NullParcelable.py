# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.android

from __future__ import annotations

from android.os.Parcelable import Parcelable


class NullParcelable(Parcelable):
    NULL_PARCELABLE: NullParcelable = None
    

    def describeContents(self) -> int:
        raise RuntimeError()
    

    def writeToParcel(self, dest: Parcel, flags: int) -> None:
        pass
from android.os.Parcel import Parcel


NullParcelable.NULL_PARCELABLE = NullParcelable()

