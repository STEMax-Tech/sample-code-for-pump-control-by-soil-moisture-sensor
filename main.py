soilMoisture = 0
setSoilMoisture = 50
# global analogValue, soilMoisture

def on_forever():
    global soilMoisture
    soilMoisture = Math.round(pins.map(pins.analog_read_pin(AnalogPin.P0), 0, 1023, 100, 0))
basic.forever(on_forever)

def on_forever2():
    serial.write_line("Soil Moisture: " + ("" + str(soilMoisture)) + " %")
    serial.write_line("Set Soil Moisture: " + ("" + str(setSoilMoisture)))
    # lcd.display_text("Moisture:" + str(soilMoisture) + "%    ", 1, 1)
    # lcd.display_text("Set Moisture:" + str(setSoilMoisture) + "    ", 1, 2)
    if soilMoisture > setSoilMoisture:
        # lcd.display_text(" ", 16, 1)
        basic.show_icon(IconNames.HAPPY)
    else:
        # lcd.display_text(lcd.display_symbol(lcd.Symbols.SYM10), 16, 1)
        basic.show_icon(IconNames.SAD)
        music.play(music.tone_playable(880, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
    basic.pause(200)
basic.forever(on_forever2)

def on_forever3():
    global setSoilMoisture
    if input.button_is_pressed(Button.A):
        setSoilMoisture += -1
        if setSoilMoisture < 0:
            setSoilMoisture = 100
        basic.show_leds("""
            . . . . .
            . . . . .
            . # # # .
            . . . . .
            . . . . .
            """)
    elif input.button_is_pressed(Button.B):
        setSoilMoisture += 1
        if setSoilMoisture > 100:
            setSoilMoisture = 0
        basic.show_leds("""
            . . . . .
            . . # . .
            . # # # .
            . . # . .
            . . . . .
            """)
    if input.logo_is_pressed():
        while input.logo_is_pressed():
            basic.show_icon(IconNames.YES)
        music.play(music.tone_playable(880, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        #setSoilMoisture = EEPROM.readw(0)
basic.forever(on_forever3)



def on_forever4():
    if soilMoisture > setSoilMoisture:
        # l9110.pause_motor(l9110.Motor.MOTOR_A)
        # l9110.pause_motor(l9110.Motor.MOTOR_B)
        basic.show_icon(IconNames.HAPPY)
    else:
        # l9110.control_motor(l9110.Motor.MOTOR_A, l9110.Rotate.FORWARD, 100)
        # l9110.control_motor(l9110.Motor.MOTOR_B, l9110.Rotate.FORWARD, 100)
        basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever4)
