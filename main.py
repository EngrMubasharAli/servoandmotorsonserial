def on_data_received():
    global ch
    if serial.read_line() == "A":
        pins.digital_write_pin(DigitalPin.P0, 1)
    elif serial.read_line() == "a":
        pins.digital_write_pin(DigitalPin.P0, 0)
    elif serial.read_line() == "B":
        pins.digital_write_pin(DigitalPin.P1, 1)
    elif serial.read_line() == "b":
        pins.digital_write_pin(DigitalPin.P1, 0)
    elif serial.read_line() == "C":
        ch = parse_float(serial.read_line())
        pins.servo_write_pin(AnalogPin.P2, ch)
    elif serial.read_line() == "D":
        ch = parse_float(serial.read_line())
        pins.servo_write_pin(AnalogPin.P3, ch)
    elif serial.read_line() == "E":
        ch = parse_float(serial.read_line())
        pins.servo_write_pin(AnalogPin.P4, ch)
serial.on_data_received(serial.delimiters(Delimiters.NEW_LINE), on_data_received)

ch = 0
serial.set_baud_rate(BaudRate.BAUD_RATE115200)

def on_forever():
    pass
basic.forever(on_forever)
