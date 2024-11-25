define Alina = Character("Алина", color="#82f364", image="Alina", callback=name_callback, cb_name='Alina')
define Ulyana = Character("Ульяна", color="#532d49", image="Ulyana", callback=name_callback, cb_name='Ulyana')
define Diana = Character("Диана", color="#fc4db6", image="Diana", callback=name_callback, cb_name='Diana')
define Yana = Character("Яна", color="#e48942", image="Yana", callback=name_callback, cb_name='Yana')
define Teacher = Character("Учитель", color="#dad4db", image="Teacher", callback=name_callback, cb_name='Teacher')
define Musk = Character("Маск", color="#814e41", image="Musk", callback=name_callback, cb_name='Musk')
define MainHero = Character("Главный Герой", color="#969696")
define Unknown = Character("Неизвестный", color="#c7ffc7", image="Unknow", callback=name_callback, cb_name='Unknown')
define Enemy = Character("Противники", color="#47587e", image="Enemy", callback=name_callback, cb_name='Enemy')

transform smaller: 
    zoom 0.89
transform tiny: 
    zoom 0.5
transform midleft:
    xalign 0.3 yalign 1.0
transform midright:
    xalign 0.7 yalign 1.0
transform four: 
    zoom 0.8
transform scale(x):
    zoom x
transform midright_center:
    xalign 0.8 yalign 0.6

#Спрайты Алины
image Alina Idle = At("Characters/Alina/idle.png", sprite_highlight('Alina'), smaller)
image Alina InGlasses = At("Characters/Alina/in glasses.png", sprite_highlight('Alina'), smaller)
image Alina Angry = At("Characters/Alina/angry.png", sprite_highlight('Alina'), smaller)
image Alina Blush1 = At("Characters/Alina/blushing 1.png", sprite_highlight('Alina'), smaller)
image Alina Blush2 = At("Characters/Alina/blushing 2.png", sprite_highlight('Alina'), smaller)
image Alina Confused = At("Characters/Alina/confused.png", sprite_highlight('Alina'), smaller)

#Спрайты Учителя
image Teacher Disappointed = At("Characters/Teacher/disappointed.png", sprite_highlight('Teacher'), smaller)
image Teacher Angry = At("Characters/Teacher/angry.png", sprite_highlight('Teacher'), smaller)

#Спрайты Дианы
image Diana Idle = At("Characters/Diana/idle.png", sprite_highlight('Diana'), smaller)
image Diana Laughing = At("Characters/Diana/laughing.png", sprite_highlight('Diana'), smaller)
image Diana Smiling = At("Characters/Diana/smiling.png", sprite_highlight('Diana'), smaller)
image Diana WinnerPose = At("Characters/Diana/winner_pose.png", sprite_highlight('Diana'), smaller)

#Спрайты Ульяны
image Ulyana Idle = At("Characters/Ulyana/idle.png", sprite_highlight('Ulyana'), smaller)
image Ulyana Angry = At("Characters/Ulyana/angry.png", sprite_highlight('Ulyana'), smaller)
image Ulyana Excited = At("Characters/Ulyana/excited.png", sprite_highlight('Ulyana'), smaller)
image Ulyana Happy = At("Characters/Ulyana/happy.png", sprite_highlight('Ulyana'), smaller)
image Ulyana Pout = At("Characters/Ulyana/pout.png", sprite_highlight('Ulyana'), smaller)
image Ulyana Proud = At("Characters/Ulyana/Proud.png", sprite_highlight('Ulyana'), smaller)
image Ulyana Sad = At("Characters/Ulyana/sad.png", sprite_highlight('Ulyana'), smaller)
image Ulyana Thinking = At("Characters/Ulyana/thinking.png", sprite_highlight('Ulyana'), smaller)

#Спрайты Яны
image Yana Idle = At("Characters/Yana/idle.png", sprite_highlight('Yana'), smaller)
image Yana Determined = At("Characters/Yana/determined.png", sprite_highlight('Yana'), smaller)
image Yana Confused = At("Characters/Yana/confused.png", sprite_highlight('Yana'), smaller)
image Yana Thinking = At("Characters/Yana/thinking.png", sprite_highlight('Yana'), smaller)
image Yana Exhausted = At("Characters/Yana/exhausted.png", sprite_highlight('Yana'), smaller)
image Yana Smiling = At("Characters/Yana/smiling.png", sprite_highlight('Yana'), smaller)
image Yana Laughing = At("Characters/Yana/laughing.png", sprite_highlight('Yana'), smaller)
image Yana Scared = At("Characters/Yana/scared.png", sprite_highlight('Yana'), smaller)

#Спрайты Маска
image Musk = "Characters/Musk/Normal.png"
image Enemy Single = "Characters/Monster/single.png"
image Enemy Multiple = "Characters/Monster/multiple.png"


#Очки персонажей
define PointYana = 0
define PointUlyana = 0
define PointDiana = 0
define PointAlina = 0

# C кем мы пойдём в замок
define CastleChoice = ""

label start:
    show text "{size=+20}ГЛАВА 1\nПролог" with ComposeTransition(Pause(2), after=dissolve)
    scene black with dissolve

    scene image("BG/ClassRoom.png")
    play sound "bell.mp3" volume 0.3
    $ renpy.block_rollback()
    pause 3

    MainHero "Эх, когда же они уже отстанут от меня..."
    show Teacher Angry
    Teacher "Уже май, экзамены через две недели. Ты когда определишься со своим будущим?!"
    MainHero "Она снова кричит... Зачем?.."
    Teacher Disappointed "Ты не понимаешь, что это очень важно? Это решение буквально всю твою жизнь определяет."
    MainHero "Ну и что? Время ещё есть. Мне же не через неделю документы подавать."
    Teacher Disappointed "Почему все твои одноклассники уже давно определились, а ты всё тянешь?"

    play music "toska.ogg"
    scene image("BG/ResidentialAreaCourtyard.png") with dissolve
    MainHero "«Почему?». А я что, знаю что-ли?"
    MainHero "Может они мега-гении, которые с семи лет знают, чего хотят от жизни."
    MainHero "Может им родители сказали, что делать."
    MainHero "Может у них есть кто-то, кто может подсказать как поступить..."
    MainHero "У меня даже друзей нет, с которыми можно было бы посоветоваться..."
    MainHero "Откуда мне знать, куда я хочу поступать?.."
    MainHero "Я вообще по жизни ничего не хочу. Хочу чтобы меня никто не трогал и не надоедал бесполезной чушью. Мне бы в компик поиграть и чтоб еда была. Большего не прошу."    


    scene image ("BG/HeroRoom.png")
    MainHero "Вот куда мне поступать?"

    MainHero "Посмотрим..."

    scene image("BG/MonitorTurnedOn.png")
    MainHero "Столько вариантов, а я всё равно ничего не выбрал..."

    scene image("BG/MonitorTurnedOff.png")
    MainHero "К чёрту это всё, потом разберусь."

    scene image("BG/HeroRoom.png")
    MainHero "Сколько можно мне мозги выносить?"

    scene black with dissolve

    MainHero "Ладно, чуть-чуть потерпеть осталось..."

    play music "cave.ogg" fadein 1.0
    scene image("BG/Cave.png")
    MainHero "Что? Я где?"
    MainHero "Куда я попал?"
    MainHero "Ужас, как тут сыро"
    # Звук шагов
    MainHero "Мне не показалось?"
    MainHero "Кто здесь?"
    Unknown "Ой, а ты откуда здесь?"
    MainHero "Сам не знаю. Где я вообще?"    
    show Yana Confused
    Yana "А вот этого не знаю даже я. Судя по всему, ты такой же как мы. Круто! Меня, кстати, Яна зовут."
    show Yana Idle
    MainHero "«Мы»? Значит мы тут не вд..."
    ## Яна слева противники справа ?
    play sound "monster1.mp3"
    show Enemy Single at midright_center, scale(0.7)
    Enemy "ВУУАРАР!!"
    show Yana Confused
    MainHero "ЭТО ЧТО ТАКОЕ?!"

    Yana Smiling "Не парься, я знаю как его победить. Смотри и учись"
    MainHero "Постой! Это опасно!"
    Yana Determined "В этой жизни опасно почти всё!"
    hide Yana
    hide Enemy

    # Мини-игра Яны
    $ renpy.suspend_rollback(True)
    $ config.rollback_enabled = False
    show screen testing_screen
    Yana "Ну-ка! Сейчас подберу правильную последовательность атаки..."
    call screen testing_screen
    $ config.rollback_enabled = True
    $ renpy.suspend_rollback(False)
    $ renpy.force_autosave()

    show Yana Smiling
    MainHero "Это было... {w} Круто..."
    Yana Laughing "Хах, спасибо. А ты забавный. Стоял и смотрел как девушка в одиночку дерётся с монстром."
    MainHero "Я решил не мешать тебе.."
    Yana Idle "Правильно сделал. Боюсь, если бы ты полез, от тебя бы и мокрого места не осталось. Давай двигаться к выходу, он явно тут не один."
    hide Yana

    scene image("BG/CaveWithFork.png")
    Yana Confused "Вот тут направо. Дальше прямо, прямо и снова направо."
    "Какая-то странная она... На неё нападает огромное существо, а она не боится. Никакого инстинкта самосохранения."
    "Ещё двигалась как-то слишком резко. Словно телепортировалась пока не подобрала нужную комбинацию...{w} Может спросить?..." 

    scene image("BG/Cave-Corridor1.png")
    show Yana Confused
    MainHero "Яна, слушай, а почему ты так резко двигалась пока сражалась? Ещё и не царапинки на тебе, хотя он попадал."
    Yana Idle "А это моя сила."
    MainHero "Сила?"
    Yana Smiling "Ну да. Мы все не знаем как тут оказались, но у каждой есть какая-либо сила. Моя, например: возвращать себя и своё состояние на несколько секунд назад."
    MainHero "Фантастика какая-то. Ты что, управляешь временем?"
    Yana Laughing "Ха-ха-ха. Можно и так сказать. Но только своим. Я не могу влиять на мир."
    MainHero "А что значит «мы»? Ты не в первый раз так говоришь."
    Yana Idle "Скоро узнаешь, но сначала нам нужно выбраться отсюда."
    hide Yana

    scene image("BG/BigCave.png")
    show Yana Confused at midleft
    Yana "Тише..."
    MainHero "Что случилось?"
    MainHero "Показалось может..."
    show Enemy Multiple at midright_center, scale(0.7)
    play sound "monsters.ogg"
    Enemy "ААААРРРРРХ!"
    Yana Scared "БЕЖИМ!"
    MainHero "ПОЧЕМУ ИХ ТАК МНОГО?"
    Yana Scared "ОНИ ЖИВУТ СТАЯМИ, НО НЕ НАСТОЛЬКО БОЛЬШИМИ!!!"
    hide Yana Enemy

    scene image ("BG/Cave-Corridor2.png")
    show Yana Exhausted
    MainHero "Это шутка какая-то! Я очнулся в незнакомом мире и на меня тут же нападает стая каких-то монстров!"
    MainHero "Я не уже не могу бежать!"
    Yana Exhausted "Мы почти на месте! Потерпи чуть-чуть"
    hide Yana

    scene image ("BG/Cave-Corridor3.png")
    show Yana Scared
    Yana "Блин, я не помню куда идти!"
    menu:
        "Налево":
            MainHero "Налево!"
            menu:
                Yana "Ты уверен?"
                "Да":
                    menu:
                        Yana "ТЫ ТОЧНО УВЕРЕН?"
                        "Да":
                            menu:
                                Yana "В любом случае, это только твой выбор, и винить надо будет только тебя. Ещё раз спрошу, ты уверен?"
                                "Да":
                                    jump TurnLeft
                                "Нет":
                                    $ PointYana += 1
                        "Нет":
                            $ PointYana += 1
                "Нет":
                    $ PointYana += 1

        "Направо":
            $ PointYana += 1
    Yana Determined "Бежим"
    hide Yana

    stop music

    scene image("BG/FlowerGlade.png")
    show Yana Exhausted at left
    show Enemy Multiple at center, scale(0.7)
    Yana "Алина! Спасай! Их там слишком много!"
    show Alina Idle at right
    Alina "Ты опять в передрягу попала?"
    Yana "Да! Спасай, Линочка!"
    Alina "А это кто с тобой?"
    Yana "Потом расскажу!"
    show Alina InGlasses
    show Enemy
    Alina "Ну что, поиграем?"
    hide Enemy

    hide Alina 
    hide Yana
    ## Мини-игра Алины
    $ renpy.suspend_rollback(True)
    $ config.rollback_enabled = False
    play music "hacking.ogg"
    call screen terminal_screen
    $ config.rollback_enabled = True
    $ renpy.suspend_rollback(False)
    $ renpy.force_autosave()
    stop music

    show Alina Idle
    MainHero "Что ты сделала? Почему они встали как вкопанные?"
    Alina "Я отключила им мозг. Теперь они будут вечно тут стоять."
    MainHero "Но как?.."
    Alina "Сама толком не понимаю. Как я попала сюда, мои очки какими-то новыми свойствами обзавелись."
    "Да куда я, блин, попал?"
    show Alina Idle at midleft
    show Yana Idle at midright
    Yana "Ребят, пошли к Диане. Она, наверное, уже почти закончила."
    Alina "Да. Неплохо было бы вот этого ей показать. Идём?"
    MainHero "Мне деваться некуда. Куда вы - туда и я."
    hide Yana 
    hide Alina

    scene image("BG/EmptyField.png")
    show Yana Confused at midright
    show Alina Confused at midleft
    Alina "То есть, ты почти до конца дошла, а там вот этот сидит?"
    Yana "Ну да. Я так удивилась увидеть там человека! Алина, ну чего ты злая такая? Не похож он на злодея. Зато нам теперь не так скучно будет!"
    menu:
        Alina "Да странно всё это... Вот откуда ты взялся?"
        "Казахстанский я":
            pass
        "Уральский я":
            ## Былла кому?(балл главному герою)
            pass
        "Сибирский я":
            pass
        "Московский я":
            pass
    Alina "Какой? Что это значит вообще?"
    "Они что, не помнят реальный мир?"
    Yana Idle "Ой, смотрите! Диана!"
    show Diana Idle 
    show Yana Idle at right
    show Alina Idle at left
    Diana Smiling "Привет, девочки! Я вот гуляла, сейчас начну делом заниматься. А вы что, уже закончили?"
    Alina Angry "Что? Ты ещё не начала?! Диана. Тебе было поручено важное дело. Почему ты прохлаждалась пока остальные работали?! Уже почти солнце село!"
    Diana Laughing "Лина, ну не сердись! Ты же знаешь, что я быстро закончу. Можете посмотреть, а пока расскажите, кто это с вами."
    
    hide Diana 
    hide Alina 
    hide Yana
    ## Мини-игра Дианы
    "ТУТ БУДЕТ МИНИ-ИГРА ФРОНТЕНЩИЦЫ, ПОКА ЧТО ТАМ СТОИТ ИГРА БЕКЕНЩИЦЫ, В КОТОРОЙ НУЖНО ЗАСТАВИТЬ РОБОТА ПРИНЕСТИ ВОДЫ"
    $ renpy.suspend_rollback(True)
    $ config.rollback_enabled = False
    show screen backend_screen
    Alina "Эй, Маск! Иди к колодцу и набери воды."
    call screen backend_screen
    pause 1.0
    $ config.rollback_enabled = True
    $ renpy.suspend_rollback(False)
    $ renpy.force_autosave()
    
    scene image("BG/EmptyField.png")
    # scene image ("BG/GladeAtHome.png")
    show Diana Idle
    show Alina Idle at right
    show Yana Idle at left
    Diana Smiling "Вуаля! Линочка, я же говорила, что быстро закончу. Сколько это у меня заняло? Минут пять?"
    Alina "Ладно. Живи пока. Сделай ещё костёр, на огонь посмотреть хочется."
    Yana Smiling "Да-да! И мне!"
    Diana Laughing "Учитесь пока я жива"
    hide Diana Alina Yana

    ## Звук щелчка
    scene image("BG/EmptyField.png")
    # scene image("BG/GladeAtHomeWithLogs.png")
    show Diana Idle
    show Alina Idle at right
    show Yana Idle at left
    scene image("BG/BonfireField.png")
    show Diana Idle
    show Alina Idle at right
    show Yana Idle at left
    Yana "Ура! Сразу в разы уютнее стало!"
    hide Diana 
    hide Alina 
    hide Yana
    
    $ questions = []

    while len(questions) < 5:
        menu:
            "Диана, это твоя сила? Ты можешь на ландшафт и окружение влиять?" if 1 not in questions:
                show Diana Idle
                Diana "Ну да. Мне это особых усилий не представляет. Я буквально из ничего могу предметы создавать"
                hide Diana 
                $ questions.append(1)
                # $ renpy.block_rollback()
            "А как давно вы тут?" if 2 not in questions:
                show Alina Idle
                Alina "Кто — как. Я — три недели, Диана — 12 дней, Яна — три месяцa"
                hide Alina 
                $ questions.append(2)
                # $ renpy.block_rollback()
            "Вы помните откуда сюда попали?" if 3 not in questions:
                show Diana Idle
                Diana "Нет. Мы понимаем, что не отсюда родом, но ничего толком про свой мир не помним. В лучшем случае образы и понимание, что нормально, а что нет"
                hide Diana 
                $ questions.append(3)
                # $ renpy.block_rollback()
            "А что вы знаете об этом месте?" if 4 not in questions:
                show Alina Idle at midright
                show Yana Idle at midleft
                Yana "Людей тут нет. Ну, вернее, кроме нас. Я видела очень много разных монстров, и, насколько я поняла, 
                они воспринимают людей как аномалию, пытаются нас схватить. Если не оказать им сопротивления, они явно тебя утащат"
                MainHero "Утащат куда?"
                Alina "К какому-то их предводителю. Вот про него мы и сами мало что знаем. Но, видимо, только он знает как нам домой вернуться"
                MainHero "А вы знаете где он находится?"
                Yana "Нет. Я сегодня в ту пещеру пошла, чтобы найти его. Думали, может он что-то типо лича или вампира, но, видимо, нет. Зато нашли тебя и тех монстриков. Хорошо, что я Алину с собой взяла"
                hide Yana 
                hide Alina
                $ questions.append(4)
                # $ renpy.block_rollback()
            "Ещё раз, какие у вас силы?" if 5 not in questions:
                show Alina Idle
                Alina "Диана может менять ландшафт, постройки возводить. Яна возвращается на несколько секунд назад во времени, а я мозги монстрам отключаю"
                hide Alina 
                $ questions.append(5)
                # $ renpy.block_rollback()
    "Так. Яна перебирает все варианты, ищет слабое место и использует его, чтобы иметь преимущество, ещё и раньше всех сюда попала"
    "Алина ищет лазейку и влияет на разум монстров, а Диана из ничего создаёт окружение..."
    "Они же... Блин, ну не может такого быть... {w} Они же буквально тестировщик, фронтенд разработчик и безопасник!"

    scene black
    MainHero "... {w} Куда я попал... "

    return
    
    scene image("BG/StarrySkyInTheFores.png")
    "Какие же эти девочки шумные! Наконец-то тишина..."
    "Так ничего я и не понял. Ну и ладно, в целом. Тут не так плохо как могло бы быть. Если не лазить по всяким пещерам, то вообще классно"

    scene image("BG/NightForest.png")
    show Ulyana
    Unknown "Эй! Ты кто?"
    MainHero "Что? Кто здесь?"
    Unknown "Не рыпайся, а то больно будет"
    "Девочки же говорили, что тут нет людей кроме нас. Это тогда кто?"
    MainHero "Подожди, успокойся. Тут рядом люди есть, они меня знают"
    Unknown "Ясно, так ты не один. Маск, схвати его!"
    show Musk
    "Что? Она злодейка? Блин-блин-блин, я не хочу!"
    MainHero "Не надо!"
    Unknown "Ты пойдёшь со мной, и это не обсуждается"
    MainHero "Да подожди, не надо! Что я тебе сделал?"
    Unknown "Шастал тут, этого достаточно"
    menu:
        "Давить на жалость":
            MainHero "Отпусти меня. Пожалуйста, отпусти. Я ничего плохого тебе не сделал и обещаю, что не сделаю!"
            Unknown "Конечно не сделаешь. Мы разберёмся с тобой, и больше ты не будешь представлять угрозы"
        "Попытаться вырваться":
            "Мёртвой хваткой держит. Видимо без вариантов, придется смириться"    
            Unknown "Не пытайся. Даже если ты вырвешься, он снова схватит тебя. Он быстрее тебя, прочнее тебя и, скорее всего...{w} умнее."
            MainHero "Отпусти меня. Пожалуйста, отпусти. Я ничего плохого тебе не сделал и обещаю, что не сделаю!"
            MainHero "Как этот комок глины может быть умней живого человека?"
            Unknown "Так не человека ведь, а тебя"
            $ PointUlyana += 1

    scene image("BG/NightVersionHomeAndBonfire.png")
    show Diana Idle at right, four
    show Ulyana Idle at midright, four
    show Alina Idle at midleft, four
    show Yana Idle at left, four
    Unknown "Девочки, смотрите кого я поймала!"
    Diana Angry "Ульяна, ты что делаешь! Это наш друг!"
    Ulyana "Что?! Серьёзно?"
    Alina Confused "Как не прискорбно, но да"
    MainHero "Вот видишь! Я же говорил, что я не сделаю ничего плохого"
    Ulyana "Ладно. Маск, отпусти его."
    Diana Pout"Вот почему ты всегда себя так ведёшь?!"
    Ulyana "В этот раз что не так?"
    Diana  Angry "Зачем надо было хватать человека?! Почему нельзя мирно поговорить?!"
    Ulyana "Ух-ты! То есть, я должна жертвовать безопасностью, чтобы один раз из ста не хватить не того?!"
    Diana "Да!"
    menu:
        "Принять сторону Дианы":
            MainHero "Ульяна, просто в следующий раз уточни кто перед тобой"
            $ PointDiana += 1
        "Принять сторону Ульяны":
            MainHero "Девочки, ничего страшного. Мы в довольно необычном месте, осторожность оправдана"
            $ PointUlyana += 1
    Yana Confused "Ты цел хоть?"
    MainHero "Да, вроде, да. Испугался сильнее. Пришла, не представилась и начала тащить куда-то. Я уже думал, злодейка напала"
    Ulyana "Ты кого злодейкой назвал?!"
    Yana Laughing "Ха-ха. Ну да, наша Ульяна в гневе больше на злодейку похожа. Зато когда успокоится такой доброй становится!"
    show Musk
    Alina "Ладно, пошутили и хватит. Ульяна, ты вовремя. Отправь Маска за водой, у нас вся закончилась"
    Ulyana "Хорошо. Маск!"

    # Мини-игра Ульяны
    "ТУТ МИНИ-ИГРА"

    Ulyana "Ладно, время уже позднее, пойдёмте спать, девочки. А с тобой мы завтра поговорим"
    Diana Idle"Вы идите, а я ещё посижу"

    scene image("BG/Bonfire.png")
    show Diana Sad
    Diana  "Как ты думаешь, почему мы здесь оказались?"
    MainHero "Ума не приложу. Я вообще здесь первый день"
    Diana Thinking "Не просто же так нас вырвали из привычной жизни, оторвали от семьи и друзей и закинули сюда?"
    MainHero "Вполне возможно, что просто так"
    Diana Sad "Почему именно мы? Как нам домой вернуться?.."
    menu:
        "Сказать правду":
            MainHero "Я не знаю"
            Diana Sad "Что нам делать?"
            MainHero "Я не знаю"
            Diana Angry "«Не знаю», «Не знаю»! Чего заладил! Ну тебя!"
        "Утешить":
            MainHero "Мы скоро узнаем и обязательно вернёмся к своей привычной жизни. Поверь мне"
            Diana Sad "Обещаешь?"
            MainHero "Клянусь"
            Diana Proud"Спасибо, что поддержал. Клятву придётся сдержать"
            MainHero "Я постараюсь"
            Diana Happy "Ладно, я тоже спать пойду"
            scene image("BG/BlackScreen.png")
            "Они все такие разные. Такие яркие. Интересно, и как же я собрался выполнять обещание? Надо будет что-то придумать"
    hide Diana
    
    scene image("BG/Bonfire.png")
    show Alina Idle
    Alina Confused "Ты всё сидишь?"
    MainHero "Ну да. Пытаюсь переварить то, что за день произошло"
    Alina "Вставай, поможешь мне"
    MainHero "Помогу с чем?"
    Alina "Увидишь"

    scene image("BG/NightGladeWithHouseAndFire.png")
    show Alina Idle
    show Enemy
    Alina "Ночью они вообще везде гуляют, иногда и к нам забредают"
    MainHero "Монстры что-ли?"
    Alina "Ага. Если увидим, то отвлечёшь их на себя, пока я мозги им выключу"
    MainHero "Ничего себе заявочка, а моего согласия не надо спросить?"
    Alina "Я уже один раз тебя спасла, так что нет"
    menu:
        "Уйти":
            MainHero "Нет уж, давай без меня"
            Alina "Хорошо. На мою помощь можешь не рассчитывать"
        "Помочь Алине":
            MainHero "Хорошо"
            scene black
            "А сколько мы этим заниматься будем вообще?..."
    
    scene image("BG/MorningField.png")
    "Блин, в итоге всю ночь провозились. Я чуть не помер, а Алина ушла куда-то, даже спасибо не сказала."
    show Ulyana
    Ulyana "О, а вот и ты. Девочки мне рассказали как они тебя нашли."
    MainHero "Всё? Бить не будешь больше?"
    Ulyana "Пойми, я же переживаю за них. А тут какой-то подозрительный мужик в лесу."
    MainHero "Это я подозрительный?"
    Ulyana "А как тебя описать?"
    MainHero "Справедливо..."    
    show Yana Thinking
    Yana "Ребят, смотрите!"
    Ulyana "Там что, Алина?"
    Yana "Да! И за ней кто-то гонится!"
    MainHero "Зачем она убегает? Она же может просто его отключить."
    Ulyana "Совсем дурак? Ей время для этого нужно, а его некому отвлечь"
    hide Ulyana
    hide Yana

    scene image("BG/ForestEdge.png")
    show Alina
    Alina "Девочки, помогите!"
    show Yana
    Yana "Уже идём!"
    show Ulyana
    Ulyana "Будьте осторожнее!"
    "Почему у меня сил никаких нет? Почему я просто стою и смотрю как девочки с ним дерутся?"
    "Если я прав, и их силы и правда просто навыки айтишников, то... Надо что-то менять!"
    MainHero "Девочки, пусть на меня бежит!"
    hide Alina
    hide Yana
    hide Ulyana

    show image("BG/MorningField.png") with Pause(2.0)
    show Alina
    Alina "А ты молодец. Не ожидала от тебя."
    show Yana
    Yana "Да! Ты таким крутым был!"
    show Ulyana
    Ulyana "Если бы Алина не ушла одна, ему не пришлось бы быть крутым."
    Alina "Не ворчи, я за информацией ходила."
    show Diana
    Diana "Ух-ты! И что ты узнала?"    
    Alina "Во-первых, мы все обладаем силами друг друга. Просто чтобы мне использовать силы Дианы например, надо приложить гораздо больше усилий и результат будет хуже."
    "А я никакой не обладаю..."
    Alina "Во-вторых, если сил вообще нет, то их можно развить. Можно хоть две сразу, главное равные усилия прилагать."
    Yana "Значит, он тоже сможет силой обладать?!"
    Alina "В целом, да. Если лениться не будет."
    Diana "Ух-ты! Классно!"
    "Надо приложить наконец усилия. Я не могу оставаться беспомощным бездельником."
    Alina "В-третьих, скорее всего предводитель этих чудиков знает, как нам домой вернуться. "
    Ulyana "А вот это важная информация."
    Yana "И что делать будем? Он же злыдень!"
    Alina "Надо решать. Если честно, мне уже надоело тут тусоваться."
    MainHero "А ты откуда это узнала?"
    Alina "Дошла до конца пещеры, в которой тебя Яна нашла. Там кто-то всё это на стене написал."
    "То есть, в этом мире самый надежный источник информации буквально надписи на стенах?"
    Ulyana "Лина, а ты не узнала где этот «злыдень» сидит?"
    Alina "Да, я знаю куда идти, но это не близко."
    Ulyana "Ребята, надо выдвигаться! Чем раньше пойдём, тем раньше окажемся дома."
    Yana "Подождите, мы что, просто поверим в надписи на стене?! Я всю информацию опытным путём добывала! На заборах тоже много чего пишут!"
    Alina "А у тебя есть предложение лучше? Мне кажется, надо поторопиться."
    Yana "Это опасно! Давайте сначала я одна туда схожу, разузнаю всё, а потом вернусь за вами!"
    menu:
        "Поддержать Яну":
            MainHero "Я думаю, лишний раз перестраховаться будет не лишним."
            $ PointYana += 1
        "Поддержать Алину":
            MainHero "Я думаю, надо поспешить!"
            Diana "Я согласна с Алиной! Очень хочется вернуться домой!"
            Ulyana "Хорошо. Решение принято большинством голосов. Выдвигаемся!"
    hide Yana
    hide Ulyana
    hide Alina
    hide Diana

    scene image("BG/ForestWithLake.png") with dissolve
    "ока мы шли я немного овладел каждой из сил девочек. Конечно, не идеально, но они помогали мне разобраться.
    Я стал не таким бесполезным. Все понимали, что разговаривать злыдень, скорее всего, не станет."
    "На этот случай Ульяна при помощи Алины разработала план действий. И, когда мы уже почти достигли цели, у нас состоялся последний разговор."

    scene image("BG/Bonfire.png")
    show Ulyana
    Ulyana "Тебе нельзя биться в одиночку, ты далеко не идеально владеешь силами. Лучше, если ты будешь помогать кому-то из нас."
    show Alina
    Alina "Подумай, какая из сил тебе нравится больше, с какой ты лучше управляешься."
    show Diana
    show Yana
    menu:
        "Выбрать Яну":
            MainHero "Я буду помогать Яне."
            Yana "Супер! Будем вместе отвлекать на себя часть противников!"
            $ PointYana += 1
            $ CastleChoice = "Yana"
        "Выбрать Алину":
            MainHero "Я буду помогать Алине."
            Alina "Хорошо, тогда вместе будем обезвреживать тех, кого ни Яне, ни Диане не удастся отвлечь."
            $ PointAlina += 1
            $ CastleChoice = "Alina"
        "Выбрать Диану":
            MainHero "Я буду помогать Диане."
            Diana "Ура! Тогда вместе их заблокируем!"
            $ PointDiana += 1
            $ CastleChoice = "Diana"
        "Выбрать Ульяну":
            MainHero "Я буду помогать Ульяне."
            Ulyana "Ладно, вроде твой голем сможет продержаться некоторое время."
            Ulyana "Время уже позднее, давайте спать ложиться, завтра тяжёлый день."
            $ PointUlyana += 1
            $ CastleChoice = "Ulyana"
    hide Ulyana
    hide Diana
    hide Yana
    hide Alina
    scene black
    "Как я до такого докатился?.."

    scene image("BG/Castle.png")
    show Ulyana
    Ulyana "Мы пришли, пора расходиться."
    show Diana
    Diana "Удачи, девочки! Берегите себя!"
    scene black with Pause(2.0)
    if CastleChoice == "Yana":
        call CastleWithYana
    elif CastleChoice == "Alina":
        call CastleWithAlina
    elif CastleChoice == "Diana":
        call CastleWithDiana
    else:
        call CastleWithUlyana
    return
            

label TurnLeft:
    scene image("BG/Cave-corridor2.png")
    show Yana Scared
    "Бежим"
    scene image("BG/CaveDeadEnd.png")
    Yana "Это тупик!"
    "И что делать? Я не знаю что делать. Ха-ха! Это конец!"
    scene image("BG/HeroHiding.png")
    Enemy "ВУААААР!"
    Yana Exhausted "Прости, я не осилю их..."
    MainHero "Что?! Нет! Не бросай меня!"
    Yana "Я ничего не могу сделать! Их слишком много"
    scene image("BG/HeroRoom.png")
    MainHero "АААААААА!"
    MainHero "Что?... Я живой?... Я дома?... Чуть от страха не умер."
    MainHero "И что это было?... Ну, я живой и нормально."
    return
    ## Ожидает продолжения    

label CastleWithYana:
    scene image("BG/InstideTheCastle.png") with fade
    show Yana
    Yana "Тебе просто надо привлечь их внимание и сделать так, чтобы они побежали за тобой. Главное не дай им себя догнать!"
    MainHero "Я больше о тебе переживаю... За дело."
    Yana "Постараемся!"
    ## Противники на фоне или как персонажи
    "Так, проще всего закричать, чтобы они обратили на меня внимание. Так и поступлю."
    Yana "Эй! Дурачьё пластилиновое! Дуйте сюда, только не все сразу"
    MainHero "Про меня не забудьте!"
    hide Yana

    scene image("BG/InsideTheCastle2.png")
    "Если честно, мне уже надоело от них бегать...."
    Yana "Помогите!"
    MainHero "Яна?! Ты где?!"
    show Yana
    "Вот чёрт, что делать-то?"
    menu:
        "Помочь Яне":
            MainHero "Яна, бежим!"
            MainHero "Я отвлеку их на себя, а ты уходи!"
            Yana "Стой, нет! Что ты будешь делать если они тебя догонят?"
            MainHero "Я знаю что делать, я уже сбросил нескольких."
            Yana "Хорошо, верю в тебя!"
            hide Yana
            "Правда в том, что я не знаю что делать..."
            scene black
            # ОЖИДАЕТ ПРОДОЛЖЕНИЕ
        "Убежать":
            "Вот чёрт, надо бежать!"
            scene image("BG/InsideTheCastle3.png")
            "У меня чувство, что я когда уже был в такой ситуации..."
            scene black
    return


label CastleWithDiana:
    
label CastleWithAlina:

label CastleWithUlyana: