#include <stdio.h>
#include <stdbool.h>
#include "LogitechSteeringWheelEnginesWrapper.dll"

void main() {
    bool a;
    a = LogiSteeringInitialize();
    return 0;
}