define Alina = Character("Алина", color="#82f364", image="Alina", callback=name_callback, cb_name='Alina')
define Ulyana = Character("Ульяна", color="#4ee4ff", image="Ulyana", callback=name_callback, cb_name='Ulyana')
define Diana = Character("Диана", color="#fc4db6", image="Diana", callback=name_callback, cb_name='Diana')
define Yana = Character("Яна", color="#e48942", image="Yana", callback=name_callback, cb_name='Yana')
define Teacher = Character("Учитель", color="#dad4db", image="Teacher", callback=name_callback, cb_name='Teacher')
define Musk = Character("Маск", color="#814e41", image="Musk", callback=name_callback, cb_name='Musk')
define MainHero = Character("Юра", color="#969696")
define Unknown = Character("Неизвестный", color="#c7ffc7", image="Unknow", callback=name_callback, cb_name='Unknown')
define Enemy = Character("Противники", color="#47587e", image="Enemy", callback=name_callback, cb_name='Enemy')
define Girl = Character("Девочка", color="#c7ffc7")


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
image Alina BeforeFight = At("Characters/Alina/before_fight.png", sprite_highlight('Alina'), smaller)
image Alina Fight = At("Characters/Alina/fight.png", sprite_highlight('Alina'), smaller)
image Alina Angry = At("Characters/Alina/angry.png", sprite_highlight('Alina'), smaller)
image Alina Shy = At("Characters/Alina/shy.png", sprite_highlight('Alina'), smaller)
image Alina Smiling = At("Characters/Alina/smile.png", sprite_highlight('Alina'), smaller)
image Alina Confused = At("Characters/Alina/confused.png", sprite_highlight('Alina'), smaller)

#Спрайты Учителя
image Teacher Disappointed = At("Characters/Teacher/disappointed.png", sprite_highlight('Teacher'), smaller)
image Teacher Angry = At("Characters/Teacher/angry.png", sprite_highlight('Teacher'), smaller)

#Спрайты Дианы
image Diana Idle = At("Characters/Diana/idle.png", sprite_highlight('Diana'), smaller)
image Diana Laughing = At("Characters/Diana/laughing.png", sprite_highlight('Diana'), smaller)
image Diana Angry = At("Characters/Diana/angry.png", sprite_highlight('Diana'), smaller)
image Diana Smiling = At("Characters/Diana/smiling.png", sprite_highlight('Diana'), smaller)
image Diana WinnerPose = At("Characters/Diana/winner_pose.png", sprite_highlight('Diana'), smaller)
image Diana Shrug = At("Characters/Diana/shrug.png", sprite_highlight('Diana'), smaller)
image Diana Sad = At("Characters/Diana/Sad.png", sprite_highlight('Diana'), smaller)


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

define FinalChoice = ""

label start:
    show text "{size=+20}ГЛАВА 1\nПролог" with ComposeTransition(Pause(2), after=dissolve)
    scene black with dissolve

    scene image("BG/ClassRoom.png")
    play sound "bell.mp3" volume 0.3
    $ renpy.block_rollback()
    pause 3

    "Эх, когда же они уже отстанут от меня..."
    show Teacher Angry 
    Teacher "Уже май, экзамены через две недели. Ты когда определишься со своим будущим?!"
    "Она снова кричит... Зачем?.."
    Teacher Disappointed "Ты не понимаешь, что это очень важно? Это решение буквально всю твою жизнь определяет."
    "Ну и что? Время ещё есть. Мне же не через неделю документы подавать."
    Teacher Angry "Почему все твои одноклассники уже давно определились, а ты всё тянешь?"

    play music "toska.ogg" 
    scene image("BG/ResidentialAreaCourtyard.png") with dissolve
    "«Почему?». А я что, знаю что-ли?"
    "Может они мега-гении, которые с семи лет знают, чего хотят от жизни."
    "Может им родители сказали, что делать."
    "Может у них есть кто-то, кто может подсказать как поступить..."
    "У меня даже друзей нет, с которыми можно было бы посоветоваться..."
    "Откуда мне знать, куда я хочу поступать?.."
    "Я вообще по жизни ничего не хочу. Хочу чтобы меня никто не трогал и не надоедал бесполезной чушью. Мне бы в компик поиграть и чтоб еда была. Большего не прошу."    


    scene image ("BG/HeroRoom.png")
    "Вот куда мне поступать?"

    "Посмотрим..."

    scene image("BG/MonitorTurnedOn.png")
    "Столько вариантов, а я всё равно ничего не выбрал..."

    scene image("BG/MonitorTurnedOff.png")
    "К чёрту это всё, потом разберусь."

    scene image("BG/HeroRoom.png")
    "Сколько можно мне мозги выносить?"

    scene black with dissolve

    stop music fadeout 2
    "Ладно, чуть-чуть потерпеть осталось..."

    play music "cave.ogg" fadein 2 
    scene image("BG/Cave.png")
    "Что? Я где?"
    "Куда я попал?"
    "Ужас, как тут сыро"
    # Звук шагов
    "Мне не показалось?"
    MainHero "Кто здесь?"
    Unknown "Ой, а ты откуда здесь?"
    MainHero "Сам не знаю. Где я вообще?"    
    show Yana Confused
    Yana "А вот этого не знаю даже я. Судя по всему, ты такой же как мы. Круто! Меня, кстати, Яна зовут."
    show Yana Idle
    MainHero "«Мы»? Значит мы тут не вд..."
    show Yana Scared at midleft
    ## Яна слева противники справа ?
    play sound "monster1.mp3" volume 0.5
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
    scene image("BG/Cave.png"):
        blur 10
    show screen testing_screen
    Yana "Ну-ка! Сейчас подберу правильную последовательность атаки..."
    call screen testing_screen
    $ config.rollback_enabled = True
    $ renpy.suspend_rollback(False)
    $ renpy.save("autosave_slot")

    scene image("BG/Cave.png")
    show Yana Smiling
    MainHero "Это было... {w} Круто..."
    Yana Laughing "Хах, спасибо. А ты забавный. Стоял и смотрел как девушка в одиночку дерётся с монстром."
    MainHero "Я решил не мешать тебе.."
    Yana Idle "Правильно сделал. Боюсь, если бы ты полез, от тебя бы и мокрого места не осталось. Давай двигаться к выходу, он явно тут не один."
    hide Yana

    scene image("BG/CaveWithFork.png") with fade
    Yana Confused "Вот тут направо. Дальше прямо, прямо и снова направо."
    "Какая-то странная она... На неё нападает огромное существо, а она не боится. Никакого инстинкта самосохранения."
    "Ещё двигалась как-то слишком резко. Словно телепортировалась пока не подобрала нужную комбинацию...{w} Может спросить?..." 

    scene image("BG/Cave-Corridor1.png") with fade
    show Yana Confused
    MainHero "Яна, слушай, а почему ты так резко двигалась пока сражалась? Ещё и не царапинки на тебе, хотя он попадал."
    Yana Idle "А это моя сила."
    MainHero "Сила?"
    Yana Smiling "Ну да. Мы все не знаем как тут оказались, но у каждой есть какая-либо сила. Моя, например: возвращать себя и своё состояние на несколько секунд назад."
    MainHero "Фантастика какая-то. Ты что, управляешь временем?"
    Yana Laughing "Ха-ха-ха. Можно и так сказать. Но только своим. Я не могу влиять на мир."
    MainHero "А что значит «мы»? Ты не в первый раз так говоришь."
    Yana Idle "Скоро узнаешь, но сначала нам нужно выбраться отсюда."
    

    scene image("BG/BigCave.png") with fade
    show Yana Confused at midleft
    Yana "Тише..."
    MainHero "Что случилось?"
    "Показалось может..."
    show Enemy Multiple at midright_center, scale(0.7)
    play sound "monsters.ogg"
    play music "chase.ogg"
    show Yana Scared
    Enemy "ААААРРРРРХ!"
    Yana  "БЕЖИМ!"
    MainHero "ПОЧЕМУ ИХ ТАК МНОГО?"
    Yana  "ОНИ ЖИВУТ СТАЯМИ, НО НЕ НАСТОЛЬКО БОЛЬШИМИ!!!"
    

    scene image ("BG/Cave-Corridor2.png")
    MainHero "Это шутка какая-то! Я очнулся в незнакомом мире и на меня тут же нападает стая каких-то монстров!"
    MainHero "Я не уже не могу бежать!"
    show Yana Exhausted
    Yana "Мы почти на месте! Потерпи чуть-чуть"
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
    

    scene image("BG/FlowerGlade.png") with Fade(0.5, 1, 0.5)
    stop music fadeout 1
    show Yana Exhausted at left
    show Enemy Multiple at center, scale(0.7)
    Yana "Алина! Спасай! Их там слишком много!"
    show Alina Shy at right
    Alina "Ты опять в передрягу попала?"
    Yana "Да! Спасай, Линочка!"
    Alina Confused "А это кто с тобой?"
    Yana "Потом расскажу!"
    show Alina Fight
    show Enemy
    Alina "Ну что, поиграем?"
    
    play music [ "<silence 0.5>", "hacking.ogg" ]
    scene black with Fade(0.5, 1.2, 0.1)
    scene image("BG/FlowerGlade.png"):
        blur 10
    ## Мини-игра Алины
    $ renpy.suspend_rollback(True)
    $ config.rollback_enabled = False
    call screen terminal_screen
    $ config.rollback_enabled = True
    $ renpy.suspend_rollback(False)
    $ renpy.force_autosave()
    stop music

    scene image("BG/FlowerGlade.png")
    show Alina BeforeFight
    MainHero "Что ты сделала? Почему они встали как вкопанные?"
    Alina "Я отключила им мозг. Теперь они будут вечно тут стоять."
    MainHero "Но как?.."
    Alina Shy "Сама толком не понимаю. Как я попала сюда, мои очки какими-то новыми свойствами обзавелись."
    "Да куда я, блин, попал?"
    show Alina Shy at midleft
    show Yana Idle at midright
    Yana "Ребят, пошли к Диане. Она, наверное, уже почти закончила."
    Alina Idle "Да. Неплохо было бы вот этого ей показать. Идём?"
    MainHero "Мне деваться некуда. Куда вы - туда и я."
    

    scene image("BG/EmptyField.png") with fade
    show Yana Confused at midright
    show Alina Shy at midleft
    Alina "То есть, ты почти до конца дошла, а там вот этот сидит?"
    Yana Idle "Ну да. Я так удивилась увидеть там человека!"
    Yana Confused "Алина, ну чего ты злая такая? Не похож он на злодея. Зато нам теперь не так скучно будет!"
    Yana Thinking "Ой, смотрите! Диана!"
    show Diana Idle 
    show Yana Idle at right
    show Alina Idle at left
    Diana Smiling "Привет, девочки! Я вот гуляла, сейчас начну делом заниматься. А вы что, уже закончили?"
    Alina Angry "Что? Ты ещё не начала?! Диана. Тебе было поручено важное дело. Почему ты прохлаждалась пока остальные работали?! Уже почти солнце село!"
    Diana Laughing "Лина, ну не сердись! Ты же знаешь, что я быстро закончу. Можете посмотреть, а пока расскажите, кто это с вами."
    

    ## Мини-игра Дианы
    $ renpy.suspend_rollback(True)
    $ config.rollback_enabled = False
    scene image("BG/EmptyField.png"):
        blur 10
    show screen frontend_screen
    Diana "Так-так... Значит, дом построить?{w} Нужно расставить все элементы по местам."
    call screen frontend_screen
    $ config.rollback_enabled = True
    $ renpy.suspend_rollback(False)
    $ renpy.force_autosave()
    

    scene image ("BG/GladeAtHome.png")
    show Diana Idle
    show Alina Idle at right
    show Yana Idle at left
    Diana Smiling "Вуаля! Линочка, я же говорила, что быстро закончу. Сколько это у меня заняло? Минут пять?"
    Alina Angry "Ладно. Живи пока. Сделай ещё костёр, на огонь посмотреть хочется."
    Yana Smiling "Да-да! И мне!"
    Diana Laughing "Учитесь пока я жива"


    scene image("BG/BonfireField.png") with Fade(0.5, 1, 1)
    play music 'bonfire.mp3'
    show Diana Idle
    show Alina Idle at right
    show Yana Laughing at left
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
                show Alina Smiling
                Alina "Кто - как. Я - три недели, Диана - 12 дней, Яна - три месяцa"
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
    stop music fadeout 1

    scene black with fade
    MainHero "... {w} Куда я попал... "
    
    scene image("BG/StarrySkyInTheFores.png") with Dissolve(2)
    "Какие же эти девочки шумные! Наконец-то тишина..."
    "Так ничего я и не понял. Ну и ладно, в целом. Тут не так плохо как могло бы быть. Если не лазить по всяким пещерам, то вообще классно"

    scene image("BG/NightForest.png") with Fade(1.5, 1, 0.5)
    play music 'nightforest.mp3'
    Unknown "Эй! Ты кто?"
    MainHero "Что? Кто здесь?"
    show Ulyana Excited
    Unknown "Не рыпайся, а то больно будет"
    "Девочки же говорили, что тут нет людей кроме нас. Это тогда кто?"
    MainHero "Подожди, успокойся. Тут рядом люди есть, они меня знают"
    show Ulyana Angry
    Unknown "Ясно, так ты не один. Маск, схвати его!"
    show Musk
    "Что? Она злодейка? Блин-блин-блин, я не хочу!"
    MainHero "Не надо!"
    show Ulyana Excited
    Unknown "Ты пойдёшь со мной, и это не обсуждается"
    MainHero "Да подожди, не надо! Что я тебе сделал?"
    Unknown "Шастал тут, этого достаточно"
    menu:
        "Давить на жалость":
            MainHero "Отпусти меня. Пожалуйста, отпусти. Я ничего плохого тебе не сделал и обещаю, что не сделаю!"
            show Ulyana Pout
            Unknown "Конечно не сделаешь. Мы разберёмся с тобой, и больше ты не будешь представлять угрозы"
        "Попытаться вырваться":
            "Мёртвой хваткой держит. Видимо без вариантов, придется смириться" 
            show Ulyana Pout   
            Unknown "Не пытайся. Даже если ты вырвешься, он снова схватит тебя. Он быстрее тебя, прочнее тебя и, скорее всего...{w} умнее."
            MainHero "Отпусти меня. Пожалуйста, отпусти. Я ничего плохого тебе не сделал и обещаю, что не сделаю!"
            MainHero "Как этот комок глины может быть умней живого человека?"
            show Ulyana Proud
            Unknown "Так не человека ведь, а тебя"
            $ PointUlyana += 1
    stop music fadeout 1
    
    scene image("BG/NightVersionHomeAndBonfire.png") with Fade(1.0, 0.1, 1.0)
    show Diana Idle at right, four
    show Ulyana Proud at midright, four
    show Alina Idle at midleft, four
    show Yana Idle at left, four
    Unknown  "Девочки, смотрите кого я поймала!"
    Diana Angry "Ульяна, ты что делаешь! Это наш друг!"
    Ulyana Pout "Что?! Серьёзно?"
    Alina Shy "Как не прискорбно, но да"
    MainHero "Вот видишь! Я же говорил, что я не сделаю ничего плохого"
    Ulyana "Ладно. Маск, отпусти его."
    Diana Pout"Вот почему ты всегда себя так ведёшь?!"
    Ulyana Angry"В этот раз что не так?"
    Diana  Angry "Зачем надо было хватать человека?! Почему нельзя мирно поговорить?!"
    Ulyana Excited "Ух-ты! То есть, я должна жертвовать безопасностью, чтобы один раз из ста не хватить не того?!"
    Diana Idle "Да!"
    menu:
        "Принять сторону Дианы":
            MainHero "Ульяна, просто в следующий раз уточни кто перед тобой"
            $ PointDiana += 1
        "Принять сторону Ульяны":
            MainHero "Девочки, ничего страшного. Мы в довольно необычном месте, осторожность оправдана"
            $ PointUlyana += 1
    Yana Confused "Ты цел хоть?"
    MainHero "Да, вроде, да. Испугался сильнее. Пришла, не представилась и начала тащить куда-то. Я уже думал, злодейка напала"
    Ulyana Angry"Ты кого злодейкой назвал?!"
    Yana Laughing "Ха-ха. Ну да, наша Ульяна в гневе больше на злодейку похожа. Зато когда успокоится такой доброй становится!"
    show Musk
    Alina Idle "Ладно, пошутили и хватит. Ульяна, ты вовремя. Отправь Маска за водой, у нас вся закончилась"
    Ulyana Proud"Хорошо. Маск!"

    # Мини-игра Ульяны
    $ renpy.suspend_rollback(True)
    $ config.rollback_enabled = False
    scene image("BG/NightVersionHomeAndBonfire.png"):
        blur 10
    show screen backend_screen
    Ulyana "Эй, Маск! Иди к колодцу и набери воды."
    "Напиши алгоритм для Маска, чтобы он подошел к колодцу и взял из него воду."
    call screen backend_screen
    pause 1.0
    $ config.rollback_enabled = True
    $ renpy.suspend_rollback(False)
    $ renpy.save("AfterMaskGame")

    scene image("BG/NightVersionHomeAndBonfire.png")
    show Ulyana Idle at right
    show Diana Idle at left
    Ulyana "Ладно, время уже позднее, пойдёмте спать, девочки."
    Ulyana Angry "А с тобой мы завтра поговорим"
    Diana "Вы идите, а я ещё посижу"

    scene image("BG/Bonfire.png") with Fade(1.5, 1, 1)
    show Diana Idle
    Diana  "Как ты думаешь, почему мы здесь оказались?"
    MainHero "Ума не приложу. Я вообще здесь первый день"
    Diana "Не просто же так нас вырвали из привычной жизни, оторвали от семьи и друзей и закинули сюда?"
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
            Diana Shrug "Спасибо, что поддержал. Клятву придётся сдержать"
            MainHero "Я постараюсь"
            Diana Smiling "Ладно, я тоже спать пойду"
            scene image("BG/BlackScreen.png")
            "Они все такие разные. Такие яркие. Интересно, и как же я собрался выполнять обещание? Надо будет что-то придумать"
    hide Diana
    
    scene image("BG/Bonfire.png") with fade
    show Alina Idle
    Alina "Ты всё сидишь?"
    MainHero "Ну да. Пытаюсь переварить то, что за день произошло"
    Alina "Вставай, поможешь мне"
    MainHero "Помогу с чем?"
    Alina Fight "Увидишь"
    hide Alina

    scene image("BG/NightGladeWithHouseAndFire.png") with fade
    show Alina Idle at midleft
    show Enemy Multiple at midright, scale(0.7)
    Alina Idle "Ночью они вообще везде гуляют, иногда и к нам забредают"
    MainHero "Монстры что-ли?"
    Alina Idle "Ага. Если увидим, то отвлечёшь их на себя, пока я мозги им выключу"
    MainHero "Ничего себе заявочка, а моего согласия не надо спросить?"
    Alina Idle "Я уже один раз тебя спасла, так что нет"
    menu:
        "Уйти":
            MainHero "Нет уж, давай без меня"
            Alina Angry"Хорошо. На мою помощь можешь не рассчитывать"
        "Помочь Алине":
            MainHero "Хорошо"
            scene black with Fade(1, 0.5, 1)
            "А сколько мы этим заниматься будем вообще?..."
    
    scene image("BG/MorningField.png") with fade
    "Блин, в итоге всю ночь провозились. Я чуть не помер, а Алина ушла куда-то, даже спасибо не сказала."
    show Ulyana Idle
    Ulyana "О, а вот и ты. Девочки мне рассказали как они тебя нашли."
    MainHero "Всё? Бить не будешь больше?"
    Ulyana Sad "Пойми, я же переживаю за них. А тут какой-то подозрительный мужик в лесу."
    MainHero "Это я подозрительный?"
    Ulyana Thinking "А как тебя описать?"
    MainHero "Справедливо..."
    show Ulyana at midleft    
    show Yana Confused at midright
    Yana "Ребят, смотрите!"
    Ulyana "Там что, Алина?"
    Yana Scared "Да! И за ней кто-то гонится!"
    MainHero "Зачем она убегает? Она же может просто его отключить."
    Ulyana Angry "Совсем дурак? Ей время для этого нужно, а его некому отвлечь"
    hide Ulyana
    hide Yana

    scene image("BG/ForestEdge.png") with fade
    show Alina Fight at midleft
    Alina "Девочки, помогите!"
    show Yana Idle at midright
    Yana "Уже идём!"
    show Alina at left
    show Yana Determined at right
    show Ulyana Sad
    Ulyana "Будьте осторожнее!"
    "Почему у меня сил никаких нет? Почему я просто стою и смотрю как девочки с ним дерутся?"
    "Если я прав, и их силы и правда просто навыки айтишников, то... Надо что-то менять!"
    MainHero "Девочки, пусть на меня бежит!"
    hide Yana
    hide Ulyana
    hide Alina

    show image("BG/MorningField.png") with Fade(1, 1.5, 1)
    show Alina Idle at left, four
    show Yana Idle at midleft, four
    show Ulyana Idle at midright, four
    show Diana Idle at right, four
    Alina "А ты молодец. Не ожидала от тебя."
    Yana Smiling "Да! Ты таким крутым был!"
    Ulyana Angry"Если бы Алина не ушла одна, ему не пришлось бы быть крутым."
    Alina Confused "Не ворчи, я за информацией ходила."
    Diana WinnerPose "Ух-ты! И что ты узнала?"    
    Alina "Во-первых, мы все обладаем силами друг друга. Просто чтобы мне использовать силы Дианы например, надо приложить гораздо больше усилий и результат будет хуже."
    "А я никакой не обладаю..."
    Alina "Во-вторых, если сил вообще нет, то их можно развить. Можно хоть две сразу, главное равные усилия прилагать."
    Yana Thinking"Значит, он тоже сможет силой обладать?!"
    Alina Smiling"В целом, да. Если лениться не будет."
    Diana Smiling "Ух-ты! Классно!"
    "Надо приложить наконец усилия. Я не могу оставаться беспомощным бездельником."
    Alina "В-третьих, скорее всего предводитель этих чудиков знает, как нам домой вернуться. "
    Ulyana Idle "А вот это важная информация."
    Yana "И что делать будем? Он же злыдень!"
    Alina Idle "Надо решать. Если честно, мне уже надоело тут тусоваться."
    MainHero "А ты откуда это узнала?"
    Alina Confused "Дошла до конца пещеры, в которой тебя Яна нашла. Там кто-то всё это на стене написал."
    "То есть, в этом мире самый надежный источник информации буквально надписи на стенах?"
    Ulyana Thinking"Лина, а ты не узнала где этот «злыдень» сидит?"
    Alina "Да, я знаю куда идти, но это не близко."
    Ulyana Idle "Ребята, надо выдвигаться! Чем раньше пойдём, тем раньше окажемся дома."
    Yana Confused "Подождите, мы что, просто поверим в надписи на стене?! Я всю информацию опытным путём добывала! На заборах тоже много чего пишут!"
    Alina "А у тебя есть предложение лучше? Мне кажется, надо поторопиться."
    Yana Thinking "Это опасно! Давайте сначала я одна туда схожу, разузнаю всё, а потом вернусь за вами!"
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
    "Пока мы шли я немного овладел каждой из сил девочек. Конечно, не идеально, но они помогали мне разобраться.
    Я стал не таким бесполезным. Все понимали, что разговаривать злыдень, скорее всего, не станет."
    "На этот случай Ульяна при помощи Алины разработала план действий. И, когда мы уже почти достигли цели, у нас состоялся последний разговор."


    scene image("BG/Bonfire.png") with fade
    show Yana Idle at midleft, four
    show Ulyana Idle at midright, four
    show Diana Idle at left, four
    show Alina Idle at right, four
    Ulyana "Тебе нельзя биться в одиночку, ты далеко не идеально владеешь силами. Лучше, если ты будешь помогать кому-то из нас."
    Alina "Подумай, какая из сил тебе нравится больше, с какой ты лучше управляешься."
    menu:
        "Выбрать Яну":
            MainHero "Я буду помогать Яне."
            Yana Smiling "Супер! Будем вместе отвлекать на себя часть противников!"
            $ PointYana += 1
            $ CastleChoice = "Yana Idle"
        "Выбрать Алину":
            MainHero "Я буду помогать Алине."
            Alina Smiling "Хорошо, тогда вместе будем обезвреживать тех, кого ни Яне, ни Диане не удастся отвлечь."
            $ PointAlina += 1
            $ CastleChoice = "Alina Idle"
        "Выбрать Диану":
            MainHero "Я буду помогать Диане."
            Diana Smiling "Ура! Тогда вместе их заблокируем!"
            $ PointDiana += 1
            $ CastleChoice = "Diana Idle"
        "Выбрать Ульяну":
            MainHero "Я буду помогать Ульяне."
            Ulyana Proud "Ладно, вроде твой голем сможет продержаться некоторое время."
            Ulyana "Время уже позднее, давайте спать ложиться, завтра тяжёлый день."
            $ PointUlyana += 1
            $ CastleChoice = "Ulyana Idle"
    scene black with Fade(1, 0.5, 1)
    hide Ulyana
    hide Diana
    hide Yana
    hide Alina
    "Как я до такого докатился?.."

    
    scene image("BG/Castle.png") with dissolve
    show Ulyana Happy with dissolve
    Ulyana "Мы пришли, пора расходиться."
    show Ulyana at midleft
    show Diana Idle at midright
    Diana "Удачи, девочки! Берегите себя!"
    scene black with fade
    if CastleChoice == "Yana Idle":
        call CastleWithYana
    elif CastleChoice == "Alina Idle":
        call CastleWithAlina
    elif CastleChoice == "Diana Idle":
        call CastleWithDiana
    else:
        call CastleWithUlyana

    scene image("BG/HeroRoom.png")
    MainHero "{sc}ААААААААААА{/sc}"
    MainHero "Что? Я спал?"
    scene black
    "Что это было вообще?.."
    
    scene image("BG/ClassRoom.png")
    show Teacher Angry
    Teacher "Ну? Ты решил куда будешь поступать?"
    MainHero "Да, я буду поступать в РТФ."
    Teacher Disappointed "Наконец-то! Хороший план, осталось немного поработать."
    scene black
    show text "{size=+20}некоторое время спустя" with ComposeTransition(Pause(2), after=dissolve)
    if FinalChoice == "Help":
        jump ThirdEnding
    else:
        jump SecondEnding


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
    scene image("BG/InsideTheCastle.png") with fade
    show Yana Idle
    Yana "Тебе просто надо привлечь их внимание и сделать так, чтобы они побежали за тобой. Главное не дай им себя догнать!"
    MainHero "Я больше о тебе переживаю... За дело."
    Yana Smiling "Постараемся!"
    ## Противники на фоне или как персонажи
    "Так, проще всего закричать, чтобы они обратили на меня внимание. Так и поступлю."
    Yana Determined "Эй! Дурачьё пластилиновое! Дуйте сюда, только не все сразу"
    MainHero "Про меня не забудьте!"
    hide Yana

    scene image("BG/InsideTheCastle2.png")
    "Если честно, мне уже надоело от них бегать...."
    Yana "Помогите!"
    "Видимо не все монстры заинтересовались мной..."
    MainHero "Яна?! Ты где?!"
    
    show Yana Scared
    show Enemy Single at left
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
            $ FinalChoice = "Help"
            return
        "Убежать":
            "Вот чёрт, надо бежать!"
            scene image("BG/InsideTheCastle3.png")
            "У меня чувство, что я когда уже был в такой ситуации..."
            scene black
            $ FinalChoice = "RunAway"
            return


label CastleWithDiana:
    scene image("BG/InsideTheCastle.png")
    show Diana Idle
    Diana "Ну что? Время творить?"
    MainHero "Давай просто начнём."
    Diana "Надеюсь они в одной куче, чтобы проще было их закрыть."
    
    scene image("BG/InsideTheCastle2.png")
    show Diana Idle
    Diana "Повезло, вроде они все вместе! Будет просто!"
    MainHero "Начинай, я подстрахую."    
    Diana "Ой, да не ворчи. Уже почти всё готово."
    "Как легко она это делает..."
    show Enemy
    MainHero "Диана!"
    menu:
        "Помочь Диане":
            MainHero "Алина, бежим!"
            MainHero "Я отвлеку их на себя, а ты уходи!"
            Diana "Стой, нет! Что ты будешь делать если они тебя догонят?"
            MainHero "Я знаю что делать, у меня есть план."
            Diana "Хорошо, верю в тебя!"
            hide Diana
            "Правда в том, что я не знаю что делать..."
            scene black
            $ FinalChoice = "Help"
            return
        "Сбежать":
            "Надо бежать!"
            scene image("BG/InsideTheCastle3.png")
            "У меня чувство, что я когда уже был в такой ситуации..."
            scene black
            $ FinalChoice = "RunAway"
            return

    
label CastleWithAlina:
    scene image("BG/InsideTheCastle.png")
    show Alina
    Alina "Так-с, главное не шуми, мы должны оставаться незаметными."
    MainHero "Знаю я."
    Alina "Надо найти безопасное место, в котором мы будем видеть их, а они не будут видеть нас."
    MainHero "Как насчёт пойти вот туда?"
    Alina "Супер."
    hide Alina

    scene image("BG/InsideTheCastle2.png")
    show Alina 
    Alina "Я приступаю. Ты контролируй ситуацию."
    MainHero "Принято."
    "Какая она сосредоточенная... Не перестаю ими восхищаться..."
    Alina "Так, первый есть, ещё примерно 25 осталось."
    show Enemy
    MainHero "Алина!"
    menu:
        "Помочь Алине":
            MainHero "Алина, бежим!"
            MainHero "Я отвлеку их на себя, а ты уходи!"
            Alina "Стой, нет! Что ты будешь делать если они тебя догонят?"
            MainHero "Я знаю что делать, у меня есть план."
            Alina "Хорошо, верю в тебя!"
            hide Alina
            "Правда в том, что я не знаю что делать..."
            scene black
            $ FinalChoice = "Help"
            return
        "Сбежать":
            "Надо бежать!"
            scene image("BG/InsideTheCastle3.png")
            "У меня чувство, что я когда уже был в такой ситуации..."
            scene black
            $ FinalChoice = "RunAway"
            return
 
        

label CastleWithUlyana:
    scene image("BG/InsideTheCastle.png")
    show Ulyana
    Ulyana "Главное не мешайся под ногами. Я сделаю всё сама."
    MainHero "Постараюсь."
    hide Ulyana

    scene image("BG/InsideTheCastle2.png")
    show Ulyana 
    Ulyana "Маск всё сделает сам, но мне надо контролировать его, так что прикрой спину."
    MainHero "Окей."
    show Mask
    Ulyana "Маск, давай!"
    show Enemy
    "Опять она всё делает за меня... А она справится?"
    hide Enemy
    hide Mask
    hide Ulyana
    scene black
    "Хочется принести пользу..."
    scene image("InsideTheCastle2.png")
    show Ulyana
    Ulyana "Их слишком много! Надо уходить!"
    menu:
        "Помочь Ульяне":
           MainHero "Я отвлеку их на себя, а ты уходи!"
           Ulyana "Стой, нет! Что ты будешь делать?"
           MainHero "У меня есть план."
           Ulyana "Хорошо, верю в тебя!"
           hide Ulyana
           hide Mask
           scene black
           "Правда в том, что я не знаю что делать..."
           $ FinalChoice = "Help"
           return
        "Сбежать":
            "Надо бежать!"
            scene image("BG/InsideTheCastle3.png")
            "У меня чувство, что я когда уже был в такой ситуации..."
            scene black
            $ FinalChoice = "RunAway"
            return

label SecondEnding:
    scene image("BG/Polytech.png")
    "Вот так значит... В шарагу после одиннадцати классов... Да я герой..."
    "В целом я не удивлён... Мне не особо есть разница где чалиться следующие несколько лет..."
    show expression CastleChoice
    "А ОНА ЧТО ТУТ ДЕЛАЕТ?!"
    Girl "Прости, а ты не знаешь как добраться до РТФ? У меня топографический кретинизм. Хе-хе"
    "ЧТО ДЕЛАТЬ? ЧТО ДЕЛАТЬ? ЧТО ДЕЛАТЬ?"
    menu:
        "Убежать":
            hide CastleChoice
            "Каким был, таким и остался.. Какой я жалкий"

label ThirdEnding:
    scene image("BG/RTF.png")
    "Воу... Я правда поступил?"
    "Когда я успел так измениться?..."
    show expression CastleChoice
    Girl "Привет! Ты случайно не с *название направления*?"
    "Что? Это она? Что она тут делает?"
    MainHero "Да..."
    Girl "Супер! Наставники попросили всех собраться, пойдём!"
    MainHero "Слушай, а мы раньше нигде не встречались?..."
    Girl "Хмм... Вроде нет, а что?"
    MainHero "Просто лицо показалось знакомым..."