init -2 python:
    w, h, s = 48, 42, 2

transform sprite(dir, n):
    crop (n*w*s, dir*h*s, w*s, h*s)

transform walking(dir, duration):
    sprite(dir, 1)
    pause duration / 8
    sprite(dir, 2)
    pause duration / 8
    sprite(dir, 3)
    pause duration / 8
    sprite(dir, 4)
    pause duration / 8
    sprite(dir, 5)
    pause duration / 8
    sprite(dir, 6)
    pause duration / 8
    sprite(dir, 7)
    pause duration / 8
    sprite(dir, 8)
    pause duration / 8

image robot = im.FactorScale("UI/backend/robot.png", s, bilinear=False)

define x = 1
define y = 7
define direction = 0
define velocity = 0
define damaged = False
define progress = 0
define has_bucket = 0

init python:
    def should_animate(a, b, c):
        global velocity
        if velocity == 0:
            return 0
        else:
            return None

transform move_pos(dir, x, y, duration):
    sprite(dir, 0)
    parallel:
        linear duration xpos x*96 ypos y*96
    parallel: 
        function should_animate
        walking(dir, duration)
    sprite(dir, 0)

transform damage:
    matrixcolor TintMatrix("#fff0")
    ease 0.3 matrixcolor TintMatrix("#f00")
    ease 0.3 matrixcolor TintMatrix("#fff0")

transform closing:
    alpha 0.0
    on hide:
        linear 1 alpha 1.0
        linear 0.5 alpha 0.0

transform hold:
    on hide:
        pause 1
        alpha 0.0

screen backend_screen:
    frame:
        xysize (1920, 1080)
        background "#2b2b2be0"
        at hold
        frame:
            background "#222222"
            padding (0, 0)
            align (0.5, 0.5)
            xysize (1640, 768)

            vbox:
                hbox:
                    vbox:
                        spacing 0
                        draggroup:
                            ysize 40 * len(commands)
                            for i, command in enumerate(commands):
                                $ command_line = ""
                                if len(command) >= 1:
                                    $ command_line += f"{command[0]}."
                                if len(command) >= 2:
                                    $ command_line += f"{{color=#76c980}}{command[1]}{{/color}}"
                                if len(command) >= 3:
                                    $ command_line += f"{{color=#698089}}({{/color}}{{color=#ef935f}}{command[2]}{{/color}}{{color=#698089}}){{/color}}"
                                elif len(command) >= 2:
                                    $ command_line += f"{{color=#698089}}(){{/color}}"

                                    
                                drag:
                                    droppable True
                                    draggable True
                                    dropped line_moved
                                    dragged line_dragged
                                    drag_name i
                                    xpos 2
                                    ypos 40 * i
                                    hbox:
                                        text "{color=#aaa}[str(i + 1).rjust(2)]|{/color} [command_line]" style "code"
                                        if len(command) > 0:
                                            fixed:
                                                ysize 20
                                                xsize 20
                                                textbutton "x" action Function(clear_command, i):
                                                    text_bold True
                                                    ypos -8
            
            vbox:
                align (0.0, 1.0)
                spacing 5
                if current_step != 0 or len(commands) < max_commands or len(commands[-1]) == 0:
                    hbox:
                        textbutton "робот" action Function(target_selected, "robot") sensitive (current_step == 0)
                        textbutton "колодец" action Function(target_selected, "well") sensitive (current_step == 0)
                    hbox:
                        textbutton "идти" action Function(action_selected, "move") sensitive (current_step == 1)
                        textbutton "поворот" action Function(action_selected, "rotate") sensitive (current_step == 1)
                        textbutton "использовать" action Function(action_selected, "use") sensitive (current_step == 4)
                    hbox:
                        for i in range(1, 10):
                            textbutton "[i]" action Function(value_selected, i) sensitive (current_step == 2)
                        for a, b in [("направо", "right"), ("налево", "left")]:
                            textbutton "[a]" action Function(value_selected, b) sensitive (current_step == 3)         
            
            frame:
                padding (0, 0)
                align (1.0, 0.5)
                xysize (768, 768)
                image "UI/backend/field_bg.png"
                image "UI/backend/shadow.png" at shadow(x, y, velocity)
                fixed at move_pos(direction, x, y, velocity):
                    id "robot"
                    xysize (768/8, 768/8)
                    if damaged:
                        add "robot" at damage
                    else:
                        add "robot"
                image "UI/backend/bucket.png":
                    if has_bucket != 0:
                        if has_bucket == 1:
                            at move_bucket(x, y, velocity)
                        else:
                            at bucket(x, y, velocity)
                        alpha 1.0
                    else:
                        at bucket(x, y, velocity)
                        alpha 0.0
                image "UI/backend/field_fg.png"
            vbox:
                align(0.0, 1.0)
                xsize round(1640.0 * progress)
                ysize 10
                image Solid("#ff0000")
            hbox:
                align (0.45, 0.95)
                spacing 10
                imagebutton:
                    idle "UI/backend/start.png"
                    insensitive "UI/backend/start_inactive.png"
                    action Function(move_robot) sensitive (velocity == 0)
                imagebutton:
                    idle "UI/backend/reset.png"
                    action [SetVariable("commands", [[]]), SetVariable("current_step", 0), SetVariable("x", 1), SetVariable("y", 7)]
        
    image Solid("#000") at closing

transform move_bucket(x, y, velocity):
    pos (96*7+20, 96*3+40)
    linear 1 pos (96*7+20, 96*3)
    pause 0.5
    bucket(x, y, 0.5)


transform shadow(x, y, velocity):
    linear velocity xpos x*96 ypos y*96 + 30
    zoom 2

transform bucket(x, y, velocity):
    linear velocity xpos x*96 + 31 ypos y*96 - 5
    # ypos 20

define current_step = 0
define commands = [[]]
define max_commands = 12

python early:
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    field = [
        ".....#..",
        "........",
        ".##..#..",
        ".#.....O",
        "...###.#",
        ".#..##.#",
        "..#.##.#",
        "....##.#"
    ]

    def line_dragged(who, where):
        who[0].snap(0, who[0].drag_name * 40)

    def line_moved(who, where):
        where = where[0]
        who.snap(0, who.drag_name * 40)
        where.snap(0, where.drag_name * 40)
        if len(commands[who.drag_name]) == 0 or len(commands[where.drag_name]) == 0:
            return

        commands[who.drag_name], commands[where.drag_name] = commands[where.drag_name], commands[who.drag_name]
        renpy.restart_interaction()

    def move_robot():
        global x, y, direction, velocity, damaged, has_bucket, progress
        if velocity != 0:
            return
        damaged = False
        x, y, direction = 1, 7, 0
        renpy.restart_interaction()
        renpy.invoke_in_new_context(renpy.pause, 0.5, _clear_layers=False)
        velocity = 0.5
        progress = 0
        for n, cmd in enumerate(commands):
            if len(cmd) < 1:
                continue
            a, b = directions[direction]
            if cmd[0] == "robot" and len(cmd) == 3:
                if cmd[1] == "rotate":
                    direction = (direction + (-1 if cmd[2] == "left" else 1)) % 4
                    renpy.restart_interaction()
                    renpy.invoke_in_new_context(renpy.pause, 0.1, _clear_layers=False)
                elif cmd[1] == "move":
                    for i in range(cmd[2]):
                        nextX = x + a
                        nextY = y + b
                        if nextX >= 8 or nextY >= 8 or nextX < 0 or nextY < 0 or field[nextY][nextX] != ".":
                            damaged = True
                            velocity = 0
                            renpy.restart_interaction()
                            return
                        x = nextX
                        y = nextY
                        renpy.restart_interaction()
                        renpy.invoke_in_new_context(renpy.pause, 0.45, _clear_layers=False)
            elif cmd[0] == "well" and len(cmd) == 2:
                if field[max(0, min(7, y + b))][max(0, min(7, x + a))] == "O":
                    has_bucket = 1
                    renpy.restart_interaction()
                    renpy.invoke_in_new_context(renpy.pause, 1, _clear_layers=False)
                    has_bucket = 2
                    renpy.restart_interaction()
                    renpy.invoke_in_new_context(renpy.pause, 0.45, _clear_layers=False)
                    x = 6
                    direction = 2
                    renpy.restart_interaction()
                    while y < 8:
                        renpy.invoke_in_new_context(renpy.pause, 0.45, _clear_layers=False)
                        y += 1
                        renpy.restart_interaction()
                    return True
                else:
                    break
        damaged = True
        velocity = 0
        renpy.restart_interaction()

        velocity = 0
            # renpy.restart_interaction()
            # renpy.invoke_in_new_context(renpy.pause, 0.5, _clear_layers=False)
            

    def clear_command(i):
        global commands, current_step, x, y
        if i == len(commands) - 1:
            current_step = 0
            commands.append([])
        elif (len(commands) >= max_commands and len(commands[-1]) > 0):
            commands.append([])
        del commands[i]

    def target_selected(target):
        global current_step
        commands[-1] = [target]
        if target == "robot":
            current_step += 1
        elif target == "well":
            current_step = 4
    
    def action_selected(action):
        global current_step
        commands[-1].append(action)
        if action == "move":
            current_step = 2
        elif action == "rotate":
            current_step = 3
        else:
            current_step = 0
            commands.append([])

    def value_selected(value):
        global current_step
        commands[-1].append(value)
        current_step = 0
        if len(commands) < max_commands:
            commands.append([])


style code:
    font "fonts/Hack-Regular.ttf"