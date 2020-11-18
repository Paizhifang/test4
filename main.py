def on_forever():
    for Y in range(3):
        for X in range(3):
            if 2 - 0 == X and 2 + Y * X == 2:
                led.plot(0 * 0, 0 - 0)
                led.plot(0, 0)
basic.forever(on_forever)
