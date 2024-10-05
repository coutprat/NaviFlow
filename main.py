import pyray as rl
rl.init_window(660, 450, "NaviFlow")
car1 = rl.Vector2(320,0)
car2 = rl.Vector2(0,220)
car1d = 1
car2d =1
rl.set_target_fps(60)
while not rl.window_should_close():
    rl.begin_drawing()
    rl.clear_background(rl.WHITE)
    car1.y = car1.y + rl.get_frame_time()*60*car1d
    rl.draw_rectangle_lines_ex(rl.Rectangle(0,0,660,450),3,rl.BLACK)
    car2.x = car2.x + rl.get_frame_time()*45*car2d
    rl.draw_rectangle_lines_ex(rl.Rectangle(0,0,300,200),3,rl.BLACK)
    rl.draw_rectangle_lines_ex(rl.Rectangle(360,0,300,200),3,rl.BLACK)
    rl.draw_rectangle_lines_ex(rl.Rectangle(0,240,300,200),3,rl.BLACK)
    rl.draw_rectangle_lines_ex(rl.Rectangle(360,240,300,200),3,rl.BLACK)

    rl.draw_circle(int(car1.x),int(car1.y),10,rl.BLUE)
    rl.draw_circle(int(car2.x),int(car2.y),10,rl.RED)

    if car1.y > 450:
        car1.y = 449
        car1d = -1
    elif car1.y < 0:
        car1.y = 1
        car1d = 1

    if car2.x > 660:
        car2.x = 659
        car2d = -1
    elif car2.x < 0:
        car2.x = 1
        car2d = 1

    rl.draw_line_ex((280,180),(380,180),5,rl.GREEN)

    for i in range(-100,100):
        for j in range(-100,100):
            rl.draw_circle(i*20,j*20,2,rl.GRAY)

    rl.end_drawing()
rl.close_window()