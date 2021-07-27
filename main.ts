serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    if (serial.readLine() == "A") {
        pins.digitalWritePin(DigitalPin.P0, 1)
    } else if (serial.readLine() == "a") {
        pins.digitalWritePin(DigitalPin.P0, 0)
    } else if (serial.readLine() == "B") {
        pins.digitalWritePin(DigitalPin.P1, 1)
    } else if (serial.readLine() == "b") {
        pins.digitalWritePin(DigitalPin.P1, 0)
    } else if (serial.readLine() == "C") {
        ch = parseFloat(serial.readLine())
        pins.servoWritePin(AnalogPin.P2, ch)
    } else if (serial.readLine() == "D") {
        ch = parseFloat(serial.readLine())
        pins.servoWritePin(AnalogPin.P3, ch)
    } else if (serial.readLine() == "E") {
        ch = parseFloat(serial.readLine())
        pins.servoWritePin(AnalogPin.P4, ch)
    }
})
let ch = 0
serial.setBaudRate(BaudRate.BaudRate115200)
basic.forever(function () {
	
})
