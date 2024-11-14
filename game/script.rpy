define Alina = Character("Алина", color="c8ffc8", image="Alina", callback=name_callback, cb_name='Alina')
define Ulyana = Character("Ульяна", color="c8ffc8", image="Ulyana", callback=name_callback, cb_name='Ulyana')
define Diana = Character("Диана", color="c8ffc8", image="Diana", callback=name_callback, cb_name='Diana')
define Yana = Character("Яна", color="c8ffc8", image="Yana", callback=name_callback, cb_name='Yana')
define Teacher = Character("Учитель", color="c8ffc8", image="Teacher", callback=name_callback, cb_name='Teacher')
define Musk = Character("Маск", color="c8ffc8", image="Musk", callback=name_callback, cb_name='Musk')
define MainHero = Character("Главный Герой", color="c9ffc9")
define Unknown = Character("Неизвестный", color="c7ffc7", image="Unknow", callback=name_callback, cb_name='Unknow')
define Enemy = Character("Противник", color="c7ffc7", image="Enemy", callback=name_callback, cb_name='Enemy')

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

#Спрайты Ульяны
image Ulyana Idle = At("Characters/Ulyana/idle.png", sprite_highlight('Ulyana'), smaller)

#Спрайты Дианы
image Diana Idle = At("Characters/Diana/idle.png", sprite_highlight('Diana'), smaller)
image Diana Angry = At("Characters/Diana/angry.png", sprite_highlight('Diana'), smaller)
image Diana Excited = At("Characters/Diana/excited.png", sprite_highlight('Diana'), smaller)
image Diana Happy = At("Characters/Diana/happy.png", sprite_highlight('Diana'), smaller)
image Diana Pout = At("Characters/Diana/pout.png", sprite_highlight('Diana'), smaller)
image Diana Proud = At("Characters/Diana/Proud.png", sprite_highlight('Diana'), smaller)
image Diana Sad = At("Characters/Diana/sad.png", sprite_highlight('Diana'), smaller)
image Diana Thinking = At("Characters/Diana/thinking.png", sprite_highlight('Diana'), smaller)

#Спрайты Яны
image Yana Idle = At("Characters/Yana/idle.png", sprite_highlight('Yana'), smaller)
image Yana BeforeFight = At("Characters/Yana/before fight.png", sprite_highlight('Yana'), smaller)
image Yana Confused = At("Characters/Yana/confused.png", sprite_highlight('Yana'), smaller)
image Yana Exausted = At("Characters/Yana/exausted.png", sprite_highlight('Yana'), smaller)
image Yana Proud = At("Characters/Yana/proud.png", sprite_highlight('Yana'), smaller)
image Yana Scared = At("Characters/Yana/scared.png", sprite_highlight('Yana'), smaller)

#Спрайты Маска
image Musk = "Characters/Musk/Normal.png"
image AlinaHappy = "1"


#Очки персонажей
define PointYana = 0
define PointUlyana = 0
define PointDiana = 0

label start:
    scene image("BG/ClassRoom.png")
    MainHero "Эх, когда же они уже отстанут от меня…"
    show Teacher Angry
    Teacher "Уже май, экзамены через две недели. Ты когда определишься со своим будущим?!"
    MainHero "Она снова кричит… Зачем?.."
    Teacher Disappointed "Ты не понимаешь, что это очень важно? Это решение буквально всю твою жизнь определяет."
    MainHero "Ну и что? Время ещё есть. Мне же не через неделю документы подавать."
    Teacher Disappointed "Почему все твои одноклассники уже давно определились, а ты всё тянешь?"

    scene image("BG/ResidentialAreaCourtyard.png") with dissolve
    MainHero "«Почему?». А я что, знаю что-ли?"
    MainHero "Может они мега-гении, которые с семи лет знают, чего хотят от жизни."
    MainHero "Может им родители сказали, что делать."
    MainHero "Может у них есть кто-то, кто может подсказать как поступить…"
    MainHero "Откуда мне знать, куда я хочу поступать?.."

    scene image ("BG/HeroRoom.png")
    MainHero "Вот куда мне поступать?"

    MainHero "Посмотрим…"

    scene image("BG/MonitorTurnedOn.png")
    MainHero "Столько вариантов, а я всё равно ничего не выбрал…"

    scene image("BG/MonitorTurnedOff.png")
    MainHero "К чёрту это всё, потом разберусь."

    scene image("BG/CeilingAboveTheBed.png")
    MainHero "Сколько можно мне мозги выносить?"
    scene image(Solid("#000000"))
    MainHero "Ладно, чуть-чуть потерпеть осталось…"

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
    MainHero "«Мы»? Значит мы тут не вд…"
    ## Яна слева противники справа ?
    Enemy "ВУУАРАР!!"
    MainHero "ЭТО ЧТО ТАКОЕ?!"
    Yana Proud "Не парься, я знаю как его победить. Смотри и учись"
    MainHero "Постой! Это опасно!"
    Yana BeforeFight "В этой жизни опасно почти всё!"
    hide Yana

    # Мини-игра Яны
    # $ renpy.checkpoint()
    $ renpy.suspend_rollback(True)
    $ config.rollback_enabled = False
    call screen testing_screen
    $ config.rollback_enabled = True
    $ renpy.suspend_rollback(False)

    show Yana Proud
    MainHero "Это было…. {w} Круто…"
    Yana "Хах, спасибо. А ты забавный. Стоял и смотрел как девушка в одиночку дерётся с монстром."
    MainHero "Я решил не мешать тебе.."
    Yana "Правильно сделал. Боюсь, если бы ты полез, от тебя бы и мокрого места не осталось. Давай двигаться к выходу, он явно тут не один."
    hide Yana

    scene image("BG/CaveWithFork.png")
    Yana Confused "Вот тут направо. Дальше прямо, прямо и снова направо."
    "Какая-то странная она… На неё нападает огромное существо, а она не боится. Никакого инстинкта самосохранения."
    "Ещё двигалась как-то слишком резко. Словно телепортировалась пока не подобрала нужную комбинацию…{w} Может спросить?..." 

    scene image("BG/Cave-Corridor1.png")
    show Yana Proud
    MainHero "Яна, слушай, а почему ты так резко двигалась пока сражалась? Ещё и не царапинки на тебе, хотя он попадал."
    Yana  "А это моя сила."
    MainHero "Сила?"
    Yana Idle "Ну да. Мы все не знаем как тут оказались, но у каждой есть какая-либо сила. Моя, например: возвращать себя и своё состояние на несколько секунд назад."
    MainHero "Фантастика какая-то. Ты что, управляешь временем?"
    Yana Idle "Ха-ха-ха. Можно и так сказать. Но только своим. Я не могу влиять на мир."
    MainHero "А что значит «мы»? Ты не в первый раз так говоришь."
    Yana Idle "Скоро узнаешь, но сначала нам нужно выбраться отсюда."
    hide Yana

    scene image("BG/BigCave.png")
    show Yana Confused at midleft
    Yana "Тише…"
    MainHero "Что случилось?"
    MainHero "Показалось может…"
    show Enemy at tiny, midright
    Enemy "ААААРРРРРХ!"
    Yana Scared "БЕЖИМ!"
    MainHero "ПОЧЕМУ ИХ ТАК МНОГО?"
    Yana Scared "ОНИ ЖИВУТ СТАЯМИ, НО НЕ НАСТОЛЬКО БОЛЬШИМИ!!!"
    hide Yana Enemy

    scene image ("BG/Cave-Corridor2.png")
    show Yana Exausted
    MainHero "Это шутка какая-то! Я очнулся в незнакомом мире и на меня тут же нападает стая каких-то монстров!"
    MainHero "Я не уже не могу бежать!"
    Yana Exausted "Мы почти на месте! Потерпи чуть-чуть"
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
    Yana BeforeFight "Бежим"
    hide Yana

    scene image("BG/FlowerGlade.png")
    show Yana Scared at left
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
    call screen terminal_screen
    $ config.rollback_enabled = True
    $ renpy.suspend_rollback(False)

    show Alina Idle
    MainHero "Что ты сделала? Почему они встали как вкопанные?"
    Alina "Я отключила им мозг. Теперь они будут вечно тут стоять."
    MainHero "Но как?.."
    Alina "Сама толком не понимаю. Как я попала сюда, мои очки какими-то новыми свойствами обзавелись."
    "Да куда я, блин, попал?"
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
        Alina "Да странно всё это… Вот откуда ты взялся?"
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
    Diana Proud "Привет, девочки! Я вот гуляла, сейчас начну делом заниматься. А вы что, уже закончили?"
    Alina Angry "Что? Ты ещё не начала?! Диана. Тебе было поручено важное дело. Почему ты прохлаждалась пока остальные работали?! Уже почти солнце село!"
    Diana Excited "Лина, ну не сердись! Ты же знаешь, что я быстро закончу. Можете посмотреть, а пока расскажите, кто это с вами."
    
    hide Diana 
    hide Alina 
    hide Yana
    ## Мини-игра Дианы
    "ТУТ МИНИ-ИГРА"
    
    scene image ("BG/GladeAtHome.png")
    show Diana Idle
    show Alina Idle at right
    show Yana Idle at left
    Diana Proud "Вуаля! Линочка, я же говорила, что быстро закончу. Сколько это у меня заняло? Минут пять?"
    Alina "Ладно. Живи пока. Сделай ещё костёр, на огонь посмотреть хочется."
    Yana Proud "Да-да! И мне!"
    Diana Happy "Учитесь пока я жива"
    hide Diana Alina Yana

    ## Звук щелчка
    scene image("BG/GladeAtHomeWithLogs.png")
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
    "Алина ищет лазейку и влияет на разум монстров, а Диана из ничего создаёт окружение…"
    "Они же… Блин, ну не может такого быть… {w} Они же буквально тестировщик, фронтенд разработчик и специалист по информационной безопасности!"

    scene image("BG/BlackScreen.png")
    MainHero "… {w} Куда я попал… "
    
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
    Diana "Ульяна, ты что делаешь! Это наш друг!"
    Ulyana "Что?! Серьёзно?"
    Alina "Как не прискорбно, но да"
    MainHero "Вот видишь! Я же говорил, что я не сделаю ничего плохого"
    Ulyana "Ладно. Маск, отпусти его."
    Diana "Вот почему ты всегда себя так ведёшь?!"
    Ulyana "В этот раз что не так?"
    Diana "Зачем надо было хватать человека?! Почему нельзя мирно поговорить?!"
    Ulyana "Ух-ты! То есть, я должна жертвовать безопасностью, чтобы один раз из ста не хватить не того?!"
    Diana "Да!"
    menu:
        "Принять сторону Дианы":
            MainHero "Ульяна, просто в следующий раз уточни кто перед тобой"
            $ PointDiana += 1
        "Принять сторону Ульяны":
            MainHero "Девочки, ничего страшного. Мы в довольно необычном месте, осторожность оправдана"
            $ PointUlyana += 1
    Yana "Ты цел хоть?"
    MainHero "Да, вроде, да. Испугался сильнее. Пришла, не представилась и начала тащить куда-то. Я уже думал, злодейка напала"
    Ulyana "Ты кого злодейкой назвал?!"
    Yana "Ха-ха. Ну да, наша Ульяна в гневе больше на злодейку похожа. Зато когда успокоится такой доброй становится!"
    show Musk
    Alina "Ладно, пошутили и хватит. Ульяна, ты вовремя. Отправь Маска за водой, у нас вся закончилась"
    Ulyana "Хорошо. Маск!"

    # Мини-игра Ульяны
    "ТУТ МИНИ-ИГРА"

    Ulyana "Ладно, время уже позднее, пойдёмте спать, девочки. А с тобой мы завтра поговорим"
    Diana "Вы идите, а я ещё посижу"

    scene image("BG/Bonfire.png")
    show Diana Idle
    Diana "Как ты думаешь, почему мы здесь оказались?"
    MainHero "Ума не приложу. Я вообще здесь первый день"
    Diana "Не просто же так нас вырвали из привычной жизни, оторвали от семьи и друзей и закинули сюда?"
    MainHero "Вполне возможно, что просто так"
    Diana "Почему именно мы? Как нам домой вернуться?.."
    menu:
        Diana "Почему именно мы? Как нам домой вернуться?.."
        "Сказать правду":
            MainHero "Я не знаю"
            Diana "Что нам делать?"
            MainHero "Я не знаю"
            Diana "«Не знаю», «Не знаю»! Чего заладил! Ну тебя!"
        "Утешить":
            MainHero "Мы скоро узнаем и обязательно вернёмся к своей привычной жизни. Поверь мне"
            Diana "Обещаешь?"
            MainHero "Клянусь"
            Diana "Спасибо, что поддержал. Клятву придётся сдержать"
            MainHero "Я постараюсь"
            Diana "Ладно, я тоже спать пойду"
            scene image("BG/BlackScreen.png")
            "Они все такие разные. Такие яркие. Интересно, и как же я собрался выполнять обещание? Надо будет что-то придумать"
    hide Diana
    
    scene image("BG/Bonfire.png")
    show Alina Idle
    Alina "Ты всё сидишь?"
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
            scene image("BG/BlackScreen.png")
    return
            

label TurnLeft:
    scene image("BG/Cave-corridor2.png")
    show Yana
    "Бежим"
    scene image("BG/CaveDeadEnd.png")
    Yana "Это тупик!"
    "И что делать? Я не знаю что делать. Ха-ха! Это конец!"
    scene image("BG/HeroHiding.png")
    Enemy "ВУААААР!"
    Yana "Прости, я не осилю их…"
    MainHero "Что?! Нет! Не бросай меня!"
    Yana "Я ничего не могу сделать! Их слишком много"
    scene image("BG/CeilingAboveTheBed.png")
    MainHero "АААААААА!"
    MainHero "Что?… Я живой?… Я дома?… Чуть от страха не умер."
    MainHero "И что это было?… Ну, я живой и нормально."
    ## Ожидает продолжения    

