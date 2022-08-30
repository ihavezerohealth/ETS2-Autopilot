from ctypes import *
from posixpath import lexists

#libraryPath = r"C:\Users\Michal jr. K\OneDrive\Dokumenty\aaaaProgramming\ETS2-Autopilot\LogitechSteeringWheelSDK_8.75.30\Include\LogitechSteeringWheelLib.h"
#libraryPath = r"C:\Users\Michal jr. K\OneDrive\Dokumenty\aaaaProgramming\ETS2-Autopilot\LogitechSteeringWheelSDK_8.75.30\Include\SDK.so"


libraryPath = r"C:\Users\Michal jr. K\OneDrive\Dokumenty\aaaaProgramming\ETS2-Autopilot\LogitechSteeringWheelSDK_8.75.30\Lib\GameEnginesWrapper\x64\LogitechSteeringWheelEnginesWrapper"
sdk = CDLL(libraryPath)

class DIJOYSTATE2():
    def __init__(self, lX, lY, lZ, lRx, lRy, lRz, rglSlider, rgdwPOV, rgbButtons, lVX, lVY, lVZ, lVRx, lVRy, lVRz, rglVSlider, lAX, lAY, lAZ, lARx, lARy, lARz, rglASlider, lFX, lFY, lFZ, lFRx, lFRy, lFRz, rglFSlider):
        self.lX = lX
        self.lY = lY
        self.Lz = lZ
        self.lRX = lRx
        self.lRy = lRy
        self.lRz = lRz
        self.rglSlider = rglSlider
        self.rgdwPOV = rgdwPOV
        self.rgbButtons = rgbButtons
        self.lVX = lVX
        self.lVY = lVY
        self.lVZ = lVZ
        self.lVRx = lVRx
        self.lVRy = lVRy
        self.lVRz = lVRz
        self.rglVSlider = rglVSlider
        self.lAX = lAX
        self.lAY = lAY
        self.lAZ = lAZ
        self.lARx = lARx
        self.lARy = lARy
        self.lARz = lARz
        self.rglASlider = rglASlider
        self.lFX = lFX
        self.lFY = lFY
        self.lFZ = lFZ
        self.lFRx = lFRx
        self.lFRy = lFRy
        self.lFRz = lFRz
        self.rglFSlider = rglFSlider

LogiSteeringInitialize = sdk.LogiSteeringInitialize
LogiSteeringInitialize.restype = c_bool

LogiUpdate = sdk.LogiUpdate
LogiUpdate.restype = c_bool

LogiGetState = sdk.LogiGetState
LogiGetState.restype = DIJOYSTATE2

print(testing)