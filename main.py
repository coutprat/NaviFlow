import pyray as rl
rl.init_window(800, 450, "Hello")
while not rl.window_should_close():
    rl.begin_drawing()
    rl.clear_background(rl.WHITE)
    rl.draw_text("Hello world", 190, 200, 20, rl.VIOLET)
    rl.end_drawing()
rl.close_window()