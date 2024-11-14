screen testing_screen:
    # TODO: сделать красиво
    frame:
        align (0.5, 0.5)
        xysize (980, 350)

        vbox:
            spacing 20

            text "Текущая последовательность:"
            hbox:
                spacing 10
                for i in range(max_sequence_length):
                    fixed:
                        xysize (50, 50)
                        if len(current_sequence) > i:
                            text current_sequence[i]
                        else:
                            text "_"
                textbutton "<-":
                    action Function(erase_last)
      
            hbox:
                spacing 10
                for i in allowed_chars:
                    fixed:
                        xysize (50, 50)
                        textbutton i:
                            if len(current_sequence) < max_sequence_length:
                                action IncrementVariable("current_sequence", amount=i)

            if error != "":
                hbox:
                    text "ошибка: "
                    text error

            hbox:
                spacing 10
                textbutton "очистить":
                    action [SetVariable("current_sequence", ""), SetVariable("error", "")]
                textbutton "проверить":
                    action Function(check_sequence)
                # button:
                    # child Text("123")

default max_sequence_length = 10
default current_sequence = ""
default allowed_chars = "🏹🔪🤜🦶🍔"
default error = ""

python early:
    def erase_last():
        global current_sequence
        current_sequence = current_sequence[:-1]

    def check_sequence():
        global current_sequence, error
        if len(current_sequence) < 7:
            error = "должно быть не меньше 7-х действий"
        elif current_sequence.count(current_sequence[0]) == len(current_sequence):
            error = "действия должны быть разными - будь креативнее"
        elif "🤜" not in current_sequence:
            error = "должно быть хотя бы 1 действие 🤜 - или зассал"
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
            error = "должно быть хотя бы 1 действие 🦶 - нужно размять ноги перед бегом"
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