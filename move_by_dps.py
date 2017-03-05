def move_dps(port, dps, target_pos=False):
    """Moves the motor by degrees per second. Moving to a target position is optional. if a target_pos is not provided the 
    motor will just run continuously."""
    dps_inc = dps / 100
    target_deg = 0
    enc = BP.get_motor_encoder(port)[0]
    print(enc)
    print(target_pos)
    while True:
        if target_pos == False:
            pass
        else:
            if abs(dps) == dps and enc < target_pos or abs(dps) != dps and enc > target_pos:
                pass
            else:
                break
        enc = BP.get_motor_encoder(port)[0]
        target_deg += dps_inc
        BP.set_motor_position(port, target_deg)
        print(BP.get_motor_status(port))
        time.sleep(0.0039)
    #breaks motor
    BP.set_motor_position(port, target_pos - 1)
    time.sleep(0.45)
    BP.set_motor_speed(port, -128)
