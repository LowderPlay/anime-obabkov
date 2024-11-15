define Alina = Character("Alina", color="#fff0f0")

init python:
    yadjValue = float("inf")
    yadj = ui.adjustment()


# Экран терминала
screen terminal_screen:
    python:
        yadj.value = yadjValue

    frame:
        style_prefix "terminal"
        align (0.5, 0.5)
        xysize (1640, 920)

        vbox:
            spacing 10

            viewport yadjustment yadj:
                id "terminal_viewport"
                draggable True
                mousewheel True
                scrollbars "vertical"

                vbox:
                    id "terminal_output_box"
                    spacing 5

                    for line in terminal_lines:
                        text line style "terminal_history" language "anywhere"
            
                    if prompt_visible:
                        python:
                            if console_state.startswith("login"):
                                prefix = "Введите пароль: "
                            elif console_state.startswith("monster"):
                                host, ip = console_state.split()
                                prefix = f"{host}@{ip} > "
                            else:
                                prefix = "alina@glasses > "
                        input:
                            id "command_input"
                            default ""
                            prefix prefix
                            style "input_field"
                            caret Fixed(At(Text("_", style="input_field"), blink_cursor), xsize=0)
                            value VariableInputValue("command_text")
                            language "anywhere"
                            action [
                                SetVariable("prompt_visible", False), 
                                SetVariable("command_text", ""), 
                                Function(terminal_command_handler, command_text), 
                                SetVariable("prompt_visible", True)
                            ]


default terminal_lines = ["Добро пожаловать в Alinux 14.88 LTS\nGNU/Linux 6.0-generic x86_64", "", "Напишите 'help', чтобы получить список доступных команд"] 
default command_text = ""
define prompt_visible = True
default console_state = ""
default is_first = True

python early:
    import random
    network = {
        "6.4.1.9": ["известный IP (alina)", "Имя хоста: Alina\nЭтот хост является доверенным, поиск уязвимостей запрещён", True],
        "42.5.4.2": ["", "Имя хоста: stone\nК данному хосту невозможно подключиться", True],
        "2.4.84.4": ["", "Имя хоста: monster_2\nУ данного хоста обнаружена уязвимость\n- SQL-инъекция (использовать sqlmap)", True],
        "42.5.5.76": ["известный IP (diana)", "Имя хоста: Diana\nЭтот хост является доверенным, поиск уязвимостей запрещён", True],
        "4.9.6.7": ["известный IP (yana)", "Имя хоста: Yana\nЭтот хост является доверенным, поиск уязвимостей запрещён", True],
        "4.2.2.8": ["", "Имя хоста: tree\nК данному хосту невозможно подключиться", True],
        "9.11.3.8": ["", "Имя хоста: monster_1\nУ данного хоста обнаружена уязвамость\n - слабый пароль (использовать hydra)",True],
        "7.7.7.7": ["известный IP (ulyana)", "Имя хоста: Ulyana\nЭтот хост является доверенным, поиск уязвимостей запрещён", True],
        "14.8.5.8": ["", "Имя хоста: monster_3\nУ данного хоста обнаружена уязвимость:\n- слабый алгоритм хеширования пароля (использовать hashcat)", True],
        "11.11.11.11": ["", "Невозможно просканировать данный IP.\nДанный адрес появился в сети недавно", True]
    }

    passwords = ["admin", "12345678", "password", "qwerty", "123123123", "321321321", "qwerty123", "StrongPassword", "pA$$w0rd", "root", "password123", "Admin", "asdfasdf", "gsdgdskw3"]

    monsters = {
        "2.4.84.4": "amogus228",
        "9.11.3.8": passwords[6],
        "14.8.5.8": "kurwabober1488"
    }

    def is_offline():
        return all([not network[i][2] for i in monsters.keys()])
    
    def help():
        commands = [
            "Список доступных команд:",
            " - help              список доступных команд",
            " - scan <ip/network> просканировать сеть/хост",
            " - connect <ip>      подключение к заданному IP-адресу" ,
            " - hashcat           мощный взламыватель алгоритмов хеширования и шифрования",
            " - sqlmap            утилита для поиска и эксплуатации SQL-инъекций",
            " - hydra             утилита для перебора паролей по различным протоколам",
            " - ls                список всех файлов",
            " - cat <filename>    чтение файла",
            " - exit              выход из системы",
            "Чтобы узнать как использовать команду, введите её название без параметров"
        ]
        for command in commands:
            terminal_lines.append(command)

    def scan_network():
        terminal_lines.append("Сканирование сети...")
        renpy.pause(1)
        for ip, info in network.items():
            renpy.pause(random.randint(1, 10)/10)
            if info[2] == False:
                terminal_lines.append(f"{ip.ljust(15)}(offline)   {info[0]}")
                continue
            terminal_lines.append(f"{ip.ljust(15)}{info[0]}")
        terminal_lines.append(f"Сканирование завершено! Найдено {len(network)} адресов.")
        
    def scan_ip(ip):
        if ip not in network:
            terminal_lines.append("ОШИБКА: Данный IP-адрес не найден")
        elif not network[ip][2]:
            terminal_lines.append("ОШИБКА: Хост недоступен")
        else:
            terminal_lines.append(network[ip][1])

    def hashcat(ip):
        terminal_lines.append("Запрос заголовков сервера...")
        renpy.pause(2)
        if ip == "14.8.5.8":
            messages = [
                "Получение публичных ключей...",
                "Найден ключ пользователя root!",
                "Перебор хешей...",
                "Поиск коллизий...",       
            ]
            for message in messages:
                terminal_lines.append(message)
                renpy.pause(1)
            renpy.pause(2)
            terminal_lines.append("\nПароль найден: kurwabober1488")
        elif ip in ["2.4.84.4", "9.11.3.8"]:
            terminal_lines.append("ОШИБКА: На данном сервере не найдена уязвимость")    
        else:
            terminal_lines.append("ОШИБКА: Не удалось установить связь с сервером")
        
    def sqlmap_host(ip):
        messages = [
                "Проверка time-based инъекций...",
                "Проверка обхода экранирования...",
                "Поиск таблиц...",
                "Обнаружена таблица \"users\"! Используйте 'sqlmap dump' для чтения.",
            ]    
        if ip == "2.4.84.4":
            for i in range(4):
                renpy.pause(random.randint(1, 15)/10)
                terminal_lines.append(messages[i])
        else:
            terminal_lines.append("ОШИБКА: Невозможно подключиться к серверу")

    def sqlmap_dump(ip, table):
        if ip != "2.4.84.4":
            terminal_lines.append("ОШИБКА: Невозможно подключиться к серверу")
            return
        if table != "users":
            terminal_lines.append(f"ОШИБКА: Таблица \"{table}\" не найдена")
            return
        messages = [
            "Выгрузка таблицы \"users\"...",
            "Получение колонок..."
        ]
        for message in messages:
            terminal_lines.append(message)
            renpy.pause(1)
        terminal_lines.append(f"+---------------------+\n| user |   password   |\n+---------------------+\n| root | {monsters[ip].center(12)} |\n+---------------------+")
        
    def hydra(ip, file_name):
        if ip == "9.11.3.8" and file_name == "passwords.txt":
            for password in passwords[:5]:
                terminal_lines.append(f"Проверка связки 'root:{password}'")
                renpy.pause(0.5)
            terminal_lines.append("Найдено совпадение!")
            terminal_lines.append(f"Пароль {monsters[ip]}")
        elif ip == "9.11.3.8" and file_name != "passwords.txt":
            terminal_lines.append("ОШИБКА: Указанный файл не найден")
        elif ip in ["2.4.84.4", "14.8.5.8"]: 
            terminal_lines.append("ОШИБКА: У данного монстра нет такой уязвимости")
        else:
            terminal_lines.append("ОШИБКА: Данный IP адрес не является монстром")

    def connect(ip):
        if ip not in monsters:
            terminal_lines.append("ОШИБКА: Невозможно подключиться к IP-адресу")
        elif not network[ip][2]:
            terminal_lines.append("ОШИБКА: Хост недоступен")
        else:
            global console_state
            console_state = f"login {ip}"

    def cat(file):
        files = {
            "notes.txt":["""Известные мне айпишники:
6.4.1.9, 42.5.5.76, 4.9.6.7, 7.7.7.7
Это Alina, Diana, Yana, Ulyana.""",
"""Недавно на днях встретила какого-то незнакомого парня... 
Надо бы найти его уязвимости >:)"""],
            "passwords.txt": passwords
        }
        if file in files:
            for i in files[file]:
                terminal_lines.append(i)
        else:
            terminal_lines.append("ОШИБКА: Указанный файл не найден")
        

    def terminal_command_handler(command: str):
        global terminal_lines, console_state, is_first
        if console_state.startswith("login"):
            terminal_lines.append(f"Введите пароль: {command}")
            renpy.invoke_in_new_context(renpy.pause, 2, _clear_layers=False)
            ip = console_state.split()[1]
            if monsters[ip] == command:
                terminal_lines.clear()
                terminal_lines.append("Добро пожаловать в EvilOS!\nFreeBSD 14.1-RELEASE-p5")
                terminal_lines.append("Напишите 'help', чтобы получить список доступных команд")
                console_state = f"monster {ip}"
            else:
                console_state = ""
                terminal_lines.append("ОШИБКА: Неверный пароль")
            return

        if console_state.startswith("monster"):
            monter_command_handler(command)
            return 

        command = command.replace("[", "").replace("{", "")
        terminal_lines.append(f"{{b}}{{color=#8f9491}}alina@glasses > {command}{{/color}}{{/b}}")

        command = command.strip().lower().strip('\n')
        if command == "exit":
            if is_offline():
                renpy.end_interaction("")
            else:
                renpy.invoke_in_new_context(Alina, "Нет! Так не пойдет, нужно завалить всех троих.", _clear_layers=False)

        elif command == "help":
            renpy.invoke_in_new_context(help, _clear_layers=False)       
            
            if is_first:
                is_first = False
                renpy.invoke_in_new_context(Alina, "Так... Для начала нужно просканировать сеть", _clear_layers=False)

        elif command.startswith("scan"):
            args = command.split()
            if len(args) != 2:
                terminal_lines.append(" - scan network   сканирование всех IP-адресов поблизости\n - scan <ip>      получение информации о хосте")
            elif args[1] == "network":   
                renpy.invoke_in_new_context(scan_network, _clear_layers=False)
            elif len(args) == 2:
                renpy.invoke_in_new_context(scan_ip, args[1], _clear_layers=False)
                
        elif command.startswith("hashcat"):
            args = command.split()
            if len(args) == 3 and args[1] == "crack":
                renpy.invoke_in_new_context(hashcat, args[2], _clear_layers=False)
            else:
                terminal_lines.append(" - hashcat crack <ip>    подбирает пароль из публичного ключа сервера")
                

        elif command.startswith("sqlmap"):
            args = command.split()
            if len(args) == 4 and args[1] == "dump":
                renpy.invoke_in_new_context(sqlmap_dump, args[2], args[3], _clear_layers=False)
            elif len(args) == 3 and args[1] == "host":
                renpy.invoke_in_new_context(sqlmap_host, args[2], _clear_layers=False)
            else:
                terminal_lines.append(" - sqlmap host <ip>            находит уязвимости хоста\n - sqlmap dump <ip> <table>    выводит содержимое таблицы <table>")
                

        elif command.startswith("hydra"):
            args = command.split()
            if len(args) == 4:
                renpy.invoke_in_new_context(hydra, ip=args[2], file_name=args[3], _clear_layers=False)
            else:
                terminal_lines.append("перебирает пароли из словаря\n - hydra crack <ip> <file.txt>\n <ip>          адрес хоста \n<file.txt>    список паролей")
                

        elif command.startswith("connect"):
            args = command.split()
            if len(args) == 2:
                renpy.invoke_in_new_context(connect, command.split()[1], _clear_layers=False)
            else:
                terminal_lines.append(" - connect <ip>    подключение к заданному IP-адресу")
            
        elif command == "ls":
            terminal_lines.append("notes.txt\npasswords.txt")
        elif command.startswith("cat"):
            args = command.split()
            if len(args) == 2:
                renpy.invoke_in_new_context(cat, args[1], _clear_layers=False)
            else:
                terminal_lines.append("- cat <filename>    чтение файла")            
        else:
            terminal_lines.append(f"Неизвестная команда: '{command}'")

    dead_count = 0
    def monter_command_handler(command):
        command = command.replace("[", "").replace("{", "").strip().lower().strip('\n')
        host, ip = console_state.split()
        terminal_lines.append(f"{{b}}{{color=#8f9491}}{host}@{ip} > {command}{{/color}}{{/b}}")
        if command == "help":
            terminal_lines.append(" - shutdown    выключает хост")
        elif command == "shutdown":
            network[ip][2] = False
            global dead_count
            dead_count += 1
            terminal_lines.append("Завершение работы...")
            renpy.invoke_in_new_context(renpy.pause, 2, _clear_layers=False)
            terminal_lines.clear()
            global console_state
            console_state = ""
            
            if dead_count == 1:
                renpy.invoke_in_new_context(Alina, "Ура! Первый готов.", _clear_layers=False)
            elif dead_count == 2:
                renpy.invoke_in_new_context(Alina, "СОСАТЬ РАКИ!!!", _clear_layers=False) #Минус два, дело за малым.
            else:
                renpy.invoke_in_new_context(Alina, "ЕСС! МИНУС ТРИ!! ЮХУУ", _clear_layers=False)
                renpy.invoke_in_new_context(Alina, "Все готово! Можно выходить из системы", _clear_layers=False)
        else:
            terminal_lines.append(f"Неизвестная команда: '{command}'")



style terminal_frame:
    background "#000000d0"
    padding (20, 20)

style terminal_vbox:
    spacing 10

style terminal_history:
    font "fonts/Hack-Regular.ttf"
    color "#dfe8e2"
    size 25

style input_field is terminal_history:
    #color "#8f9491"
    bold True



transform blink_cursor:
    alpha 1.0
    pause 0.5
    alpha 0.0
    pause 0.5
    repeat