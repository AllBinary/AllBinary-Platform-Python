# Generated Code Do Not Modify
# package org.allbinary.android

from __future__ import annotations

from android.view.View import View


class ViewSwapper:
    NULL_VIEW_ARRAY: list[View] = [None] * (0)

    def _init_fields(self) -> None:
        self.rootViewId: int = None
        self.activity: Activity = None
        self.currentMainViewId: int = -1
        self.mainViewArray: list[View] = ViewSwapper.NULL_VIEW_ARRAY
        self.topViewArray: list[View] = ViewSwapper.NULL_VIEW_ARRAY
    

    def __init__(self, activity: Activity, rootViewId: int) -> None:
        self._init_fields()
        self.activity = activity
        self.rootViewId = rootViewId
    

    def setMainViews(self, viewArray: list[View]) -> None:
        self.mainViewArray = viewArray
    

    def setTopViewArray(self, topViewArray: list[View]) -> None:
        self.topViewArray = topViewArray
    

    def setMainView(self, id: int) -> None:
        viewGroup: ViewGroup = self.activity.findViewById(self.rootViewId)
        if id != self.currentMainViewId:
            for index in range(0, len(self.topViewArray)):
                viewGroup.removeView(self.topViewArray[index])
            for index in range(0, len(self.mainViewArray)):
                if id != self.mainViewArray[index].getId():
                    viewGroup.removeView(self.mainViewArray[index])
            for index in range(0, len(self.mainViewArray)):
                if id == self.mainViewArray[index].getId():
                    viewGroup.addView(self.mainViewArray[index])
                    self.currentMainViewId = id
            for index in range(0, len(self.topViewArray)):
                viewGroup.addView(self.topViewArray[index])
from android.app.Activity import Activity
from android.view.ViewGroup import ViewGroup


