let soilMoisture = 0
let setSoilMoisture = AT24CXX.read_byte(1)
// global analogValue, soilMoisture
basic.forever(function () {
    soilMoisture = Math.round(pins.map(
    pins.analogReadPin(AnalogPin.P2),
    0,
    1023,
    100,
    0
    ))
})
basic.forever(function () {
    serial.writeNumbers([soilMoisture, setSoilMoisture])
    // lcd.display_text("Moisture:" + str(soilMoisture) + "%    ", 1, 1)
    // lcd.display_text("Set Moisture:" + str(setSoilMoisture) + "    ", 1, 2)
    if (soilMoisture > setSoilMoisture) {
        // lcd.display_text(" ", 16, 1)
        basic.showIcon(IconNames.Happy)
    } else {
        // lcd.display_text(lcd.display_symbol(lcd.Symbols.SYM10), 16, 1)
        basic.showIcon(IconNames.Sad)
        music.play(music.tonePlayable(880, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    }
    basic.pause(200)
})
// setSoilMoisture = EEPROM.readw(0)
basic.forever(function () {
    if (input.buttonIsPressed(Button.AB)) {
        while (input.buttonIsPressed(Button.AB)) {
            basic.showIcon(IconNames.Yes)
        }
        music.play(music.tonePlayable(880, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        AT24CXX.write_byte(1, setSoilMoisture)
    } else if (input.buttonIsPressed(Button.A)) {
        setSoilMoisture += -1
        if (setSoilMoisture < 0) {
            setSoilMoisture = 100
        }
        basic.showLeds(`
            . . . . .
            . . . . .
            . # # # .
            . . . . .
            . . . . .
            `)
    } else if (input.buttonIsPressed(Button.B)) {
        setSoilMoisture += 1
        if (setSoilMoisture > 100) {
            setSoilMoisture = 0
        }
        basic.showLeds(`
            . . . . .
            . . # . .
            . # # # .
            . . # . .
            . . . . .
            `)
    }
})
basic.forever(function () {
    if (soilMoisture > setSoilMoisture) {
        pins.digitalWritePin(DigitalPin.P13, 0)
        pins.digitalWritePin(DigitalPin.P4, 0)
    } else {
        pins.digitalWritePin(DigitalPin.P13, 0)
        pins.digitalWritePin(DigitalPin.P13, 1)
    }
})
