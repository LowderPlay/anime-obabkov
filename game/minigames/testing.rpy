style title_text:
    font "fonts/NineteenEightySeven.ttf"
    color "#dfe8e2"
    size 35
    
style text_style:
    font "fonts/NineteenEightySeven.ttf"
    color "#dfe8e2"
    size 25

style button_style is text_style:
    idle_color "#616161"
    hover_color "#ffffff"

style button:
    size 30

screen testing_screen:
    frame:
        align (0.5, 0.5)
        xysize (1000, 500)
        text "Последовательность действий:" style "title_text":
            align (0.5, 0.1)

        vbox:
            spacing 50
            align (0.5, 0.5)

            hbox:
                align (0.5, 0.5)
                spacing 10
                for i in range(max_sequence_length):
                    fixed:
                        xysize (50, 50)
                        if len(current_sequence) > i:
                            text current_sequence[i] style "title_text"
                        else:
                            text "_" style "title_text"
                imagebutton:
                    idle "UI/backspace.png"
                    hover "UI/backspace_inactive.png"
                    action Function(erase_last)
      
            hbox:
                align (0.5, 0.5)
                text "Действия: " style "title_text"
                spacing 10
                for char, sound in zip(allowed_chars, sounds):
                    fixed:
                        xysize (50, 50)
                        textbutton char:
                            style "button"
                            idle_background "UI/button.png"
                            hover_background "UI/button_active.png"
                            if len(current_sequence) < max_sequence_length:
                                action [IncrementVariable("current_sequence", amount=char), Play("sound", f"audio/games/yana/{sound}")]

            if error != "":
                hbox:
                    text "Ошибка: " color "#ff0000" style "text_style"
                    text error style "text_style"

        hbox:
            ypos 430
            spacing 10
            textbutton "очистить" text_style "button_style":
                action [SetVariable("current_sequence", ""), SetVariable("error", "")]
            textbutton "проверить" text_style "button_style":
                action Function(check_sequence)
                # button:
                    # child Text("123")

default max_sequence_length = 10
default current_sequence = ""
default allowed_chars = "🏹🔪🤜🦶🍔"
default sounds = ["bow.wav", "knife.wav", "hit.wav", "kick.wav", "food.wav"]
default error = ""

python early:
    def erase_last():
        global current_sequence
        current_sequence = current_sequence[:-1]

    def check_sequence():
        global current_sequence, error
        if len(current_sequence) < 7:
            error = "должно быть не меньше семи действий"
        elif current_sequence.count(current_sequence[0]) == len(current_sequence):
            error = "действия должны быть разными"
        elif "🤜" not in current_sequence:
            error = "должно быть хотя бы 1 действие 🤜"
        elif "🤜🤜" in current_sequence:
            error = "нельзя использовать 🤜 два раза подряд - устанешь"
        elif current_sequence.count("🏹") > 3:
            error = "нельзя использовать 🏹 больше трех раз - стрелы закончатся"
        elif current_sequence[0] != "🍔":
            error = "перед битвой нужно перекусить 🍔"
        elif current_sequence.count("🍔") > 1:
            error = "нельзя использовать 🍔 больше одного раза - объешься"
        elif "🏹🔪" in current_sequence or "🔪🏹" in current_sequence:
            error = "нельзя использовать 🔪 и 🏹 рядом - слишком долго менять оружие"
        elif "🤜🦶" in current_sequence or "🦶🤜" in current_sequence:
            error = "нельзя использовать 🦶 и 🤜 рядом - можно потерять равновесие"
        elif "🦶" not in current_sequence:
            error = "должно быть хотя бы 1 действие 🦶 - нужно размять ноги"
        elif current_sequence.count("🤜") > 2:
            error = "нельзя использовать 🤜 больше двух раз - руки устанут"
        elif current_sequence.count("🦶") > 3:
            error = "нельзя использовать 🦶 больше трех раз - ноги устанут"
        elif "🔪" in current_sequence and (current_sequence[0] == "🔪" or not all([x != "🔪" or current_sequence[i] == "🤜" for i, x in enumerate(current_sequence[1:])])):
            error = "перед использованием 🔪 нужно использовать 🤜"
        elif current_sequence.count("🔪") > 2:
            error = "нельзя использовать 🔪 больше двух раз - можно порезаться"
        else:
            renpy.end_interaction("")