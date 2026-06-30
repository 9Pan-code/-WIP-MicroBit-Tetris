def on_button_pressed_a():
    sprite.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    sprite.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

current_y = 0
current_x = 0
sprite: game.LedSprite = None
sprite = game.create_sprite(2, 1)

def on_forever():
    global current_x, current_y
    basic.pause(650)
    current_x = sprite.get(LedSpriteProperty.X)
    current_y = sprite.get(LedSpriteProperty.Y)

    if current_y == 4:
        gurt = game.create_sprite(current_x, current_y)
        sprite.set(LedSpriteProperty.X, 2)
        sprite.set(LedSpriteProperty.Y, 1)
    else:
        sprite.change(LedSpriteProperty.Y, 1)

    if current_y == 0:
        pass

basic.forever(on_forever)

def on_in_background():
    while True:
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.play_tone(247, music.beat(BeatFraction.HALF))
        music.play_tone(262, music.beat(BeatFraction.HALF))
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.HALF))
        music.play_tone(247, music.beat(BeatFraction.HALF))
        music.play_tone(220, music.beat(BeatFraction.WHOLE))
        music.play_tone(220, music.beat(BeatFraction.HALF))
        music.play_tone(262, music.beat(BeatFraction.HALF))
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.play_tone(294, music.beat(BeatFraction.HALF))
        music.play_tone(262, music.beat(BeatFraction.HALF))
        music.play_tone(247, music.beat(BeatFraction.WHOLE))
        music.play_tone(247, music.beat(BeatFraction.HALF))
        music.play_tone(262, music.beat(BeatFraction.HALF))
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(220, music.beat(BeatFraction.WHOLE))
        music.play_tone(220, music.beat(BeatFraction.WHOLE))
        basic.pause(400)

control.in_background(on_in_background)