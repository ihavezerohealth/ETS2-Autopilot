import time

import logitech_steering_wheel as lsw
import pygetwindow as gw


if __name__ == '__main__':
    # The steering wheel should be connected to a specific window, the first step is to get the window handle and initialize the SDK
    
    window_handle = gw.getActiveWindow()._hWnd
    print(window_handle)
    initialized = lsw.initialize_with_window(ignore_x_input_controllers=False, hwnd=window_handle)

    print("SDK version is: " + str(lsw.get_sdk_version()))

    connected = lsw.is_connected(0)

    lsw.update()

    # Check if setting and Getting of the operating range works 
    operated = lsw.set_operating_range(0, 100)
    print(lsw.get_operating_range(0))

    if connected and operated:
        print('Steering wheel online')
    else:
        print('Connection failed')
        exit()

    # The update function is called to update the current state, the get state function returns a state object representing the current state of the 
    # steering wheel
    lsw.update()
    s = lsw.get_state(0)
    print(s)

    # Test the force feedback by playing the bumpy road effect on 20 percent of its maximal magnitude 
    lsw.play_bumpy_road_effect(0, 20)

    time.sleep(2)

    lsw.stop_bumpy_road_effect(0)

    # close the connection
    lsw.shutdown()