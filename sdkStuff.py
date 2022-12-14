from ctypes import *
from ctypes.wintypes import DWORD
from posixpath import lexists
from sre_parse import State
from struct import Struct

#libraryPath = r"C:\Users\Michal jr. K\OneDrive\Dokumenty\aaaaProgramming\ETS2-Autopilot\LogitechSteeringWheelSDK_8.75.30\Include\LogitechSteeringWheelLib.h"
#libraryPath = r"C:\Users\Michal jr. K\OneDrive\Dokumenty\aaaaProgramming\ETS2-Autopilot\LogitechSteeringWheelSDK_8.75.30\Include\SDK.so"


libraryPath = r"C:\Users\Michal jr. K\OneDrive\Dokumenty\aaaaProgramming\ETS2-Autopilot\LogitechSteeringWheelSDK_8.75.30\Lib\GameEnginesWrapper\x64\LogitechSteeringWheelEnginesWrapper"
sdk = CDLL(libraryPath)

class DIJOYSTATE2ENGINES(Structure):
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
        _fields_ = [
            (lX, c_long),
            (lY, c_long),
            (lZ, c_long),
            (lRx, c_long),
            (lRy, c_long),
            (lRz, c_long),
            (rglSlider, c_long),
            #(rgdwPOV, DWORD),
            #(rgbButtons, c_byte),
            (rgdwPOV, c_uint),
            (rgbButtons, c_ubyte),
            (lVX, c_long),
            (lVY, c_long),
            (lVZ, c_long),
            (lVRx, c_long),
            (lVRy, c_long),
            (lVRz, c_long),
            (rglVSlider, c_long),
            (lAX, c_long),
            (lAY, c_long),
            (lAZ, c_long),
            (lARx, c_long),
            (lARy, c_long),
            (lARz, c_long),
            (rglASlider, c_long),
            (lFX, c_long),
            (lFY, c_long),
            (lFZ, c_long),
            (lFRx, c_long),
            (lFRy, c_long),
            (lFRz, c_long),
            (rglFSlider, c_long)
            ]

LogiSteeringInitialize = sdk.LogiSteeringInitialize
LogiSteeringInitialize.restype = c_bool

LogiSteeringInitializeWithWindow = sdk.LogiSteeringInitializeWithWindow
LogiSteeringInitializeWithWindow.restype = c_bool

LogiUpdate = sdk.LogiUpdate
LogiUpdate.restype = c_bool

LogiGetStateENGINES = sdk.LogiGetStateENGINES
LogiGetStateENGINES.restype = POINTER(DIJOYSTATE2ENGINES)

LogiPlayConstantForce = sdk.LogiPlayConstantForce
LogiPlayConstantForce.restype = c_bool

LogiIsConnected = sdk.LogiIsConnected
LogiIsConnected.restype = c_bool

print(f"init {LogiSteeringInitializeWithWindow(False, 133620)}")
print(f"update {LogiUpdate()}")

# x = 0
# while True:
#   results = LogiIsConnected(c_int(x))
#   print(f"x: {x}\nresults: {results}")
#   #if x == False: break
#   x += 1

# p1 = DIJOYSTATE2ENGINES.from_address(LogiGetStateENGINES(c_int(0)))
# print(p1)
# print

if (LogiUpdate()):
    index0 = LogiGetStateENGINES(c_int(0))
    index1 = LogiGetStateENGINES(c_int(1))
    index2 = LogiGetStateENGINES(c_int(2))
    print(f"{index0.contents}")
    print(f"{index1.lX}")
    print(f"{index2}")