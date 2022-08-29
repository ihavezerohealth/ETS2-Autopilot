import ctypes

libraryPath = r"C:\Users\Michal jr. K\OneDrive\Dokumenty\aaaaProgramming\ETS2-Autopilot\LogitechSteeringWheelSDK_8.75.30\Include\LogitechSteeringWheelLib.h"
sdk = ctypes.CDLL(libraryPath)

testing = sdk.LogiUpdate()
print(testing)