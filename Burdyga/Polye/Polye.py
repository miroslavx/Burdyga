import tkinter as tk
import random
import json
import os
from tkinter import messagebox, simpledialog

# переменные
current_word = ""
hidden_word = []
used_letters = set()
players = []
current_player_idx = 0
is_spinning = False
current_score = 0
game_round = 1
roulette_values = [100, 200, 300, 400, 500, "БАНК", "ФИГА", 600, 700, 800]

# Словарик
def create_word_bank():
    return {
        "ТЕЛЕВИЗОР": "Когда-то он был роскошью, 'голубым экраном' с мерцающим черно-белым изображением, вокруг которого собирались соседи. Сегодня он плоский, умный, подключен к глобальной сети, но суть осталась – это окно в мир, приносящее в дом движущиеся картинки со звуком. Он показывает далекие страны, рассказывает новости, развлекает фильмами и шоу, формирует мнения и становится центром вечернего отдыха для многих семей, отражая эпоху и культуру.",
        "МИКРОСКОП": "Собрав несколько линз в одну трубу, человек впервые распахнул дверь в невидимую вселенную, кишащую жизнью и поражающую своей сложностью. Он показал клетки, из которых соткано все живое, помог распознать невидимых врагов – микробов, и дал старт революции в медицине и биологии. От простых увеличительных стекол до электронных гигантов, просвечивающих атомы, он – инструмент познания малого, раскрывающий тайны строения материи и чудеса миниатюрных миров.",
        "БИБЛИОТЕКА": "Это не просто хранилище бумажных томов, а тихий порт в океане времени, где на полках дремлют голоса прошлого, мудрость веков и бесконечные вымышленные миры. Пахнет старой бумагой и знанием. Сюда приходят за тишиной, за ответами, за возможностью побыть наедине с мыслями великих или потеряться в захватывающей истории. Хотя цифровые тексты теснят бумагу, она остается святилищем для ищущих знаний и утешения в шелесте страниц.",
        "ФОТОГРАФИЯ": "Сначала это была алхимия света и серебра в темной комнате, долгие выдержки, запечатлевавшие лишь неподвижное. Затем – щелчок затвора, мгновенно останавливающий время. Она способна сохранить улыбку ребенка, ужас войны, красоту заката, став документом эпохи или произведением искусства. Она позволяет нам видеть мир глазами другого, помнить ушедших и делиться важными моментами. Это застывший свет, ставший памятью.",
        "КОМПЬЮТЕР": "Его предками были счеты и арифмометры, но он превзошел их немыслимо, став универсальной машиной для обработки информации. От занимавших целые комнаты гигантов на лампах до тонких ноутбуков и мощных систем в кармане – он изменил все: работу, общение, развлечения, науку. Он считает, пишет, рисует, связывает людей через континенты, хранит гигантские объемы данных и выполняет команды, рожденные человеческой мыслью.",
        "ЯКУБОВИЧ": "Его усы и неизменный фрак стали символом целой телевизионной эпохи в России. Десятилетиями он стоит у вращающегося игрового поля, с улыбкой принимая самые невероятные дары от участников со всей страны и произнося коронные фразы, знакомые каждому. Он – лицо народного капитал-шоу, которое, несмотря на простоту правил, объединяет у экранов разные поколения, являясь уникальным сплавом азарта, фольклора и телевизионного зрелища.",
        "БАРАБАН": "Гладкий, расчерченный на сектора с буквами, цифрами и специальными знаками вроде 'Банкрот' или 'Приз'. Он – сердце популярной телеигры, ось, вокруг которой вращается удача участников. Его тяжелый ход, звук вращения и щелчок стрелки, замирающей на заветном секторе, создают напряжение и волнение. Крутануть его – значит довериться случаю, испытать судьбу и, возможно, получить шанс угадать слово и выиграть подарки.",
        "САМОВАР": "Он стоял в центре стола, сияя начищенными боками, будь то скромный медный или богато украшенный тульский. Внутри него гудели угли, нагревая воду в специальной трубе, а сверху часто располагался заварочный чайник. Вокруг него собиралась семья или гости, велись неспешные беседы под аромат свежезаваренного чая с баранками и вареньем. Это не просто прибор для кипячения воды, а душа русского чаепития, символ домашнего уюта, гостеприимства и добрых традиций.",
        "КОФЕ": "По легенде, его бодрящие свойства открыл эфиопский пастух, заметив резвость своих коз после поедания красных ягод. Из Африки он начал свое триумфальное шествие по миру, став причиной открытия уютных кофеен, источником вдохновения для творцов и незаменимым утренним ритуалом для миллионов. Горький эспрессо, нежный капучино, пряный напиток по-восточному – его готовят сотнями способов, но всегда ценят за глубокий аромат и способность прогнать сонливость.",
        "ОЧКИ": "Изобретенные, возможно, в средневековых монастырях для стареющих монахов, они стали настоящим даром для человечества, позволив людям с плохим зрением продолжать читать, писать и заниматься ремеслами. Сначала неуклюжие, затем – все более изящные, они превратились из медицинской необходимости в модный аксессуар. Сидя на переносице, эти два кусочка стекла в оправе исправляют фокус, возвращая миру четкость, и порой кардинально меняют облик человека.",
        "ИНТЕРНЕТ": "Рожденный в недрах военных разработок как средство связи на случай катастрофы, он окреп и превратился в гигантскую паутину, опутавшую всю планету. Он дал голос миллиардам, стер границы и расстояния, став источником знаний, развлечений, общения и, увы, новых угроз. Сегодня без него немыслима жизнь большинства людей, он в наших карманах, домах, на работе, хранит наши секреты и связывает нас невидимыми нитями информации.",
        "ТЕЛЕСКОП": "Сначала это были лишь две скромные линзы в трубе, но они позволили впервые увидеть горы на Луне и спутники Юпитера, перевернув представление человека о своем месте во Вселенной. Со временем он становился всё больше и сложнее, научился смотреть сквозь пыль и мрак, улавливать невидимый свет, заглядывая в прошлое космоса на миллиарды лет. Его глазами мы видим рождение и смерть звезд, далекие галактики и ищем ответы на вечные вопросы мироздания.",
        "ЭХО": "В древних мифах это была нимфа, наказанная богиней и обреченная повторять лишь последние слова других. В мире физики – это просто отражение звуковой волны от препятствия, возвращающееся к источнику с опозданием. Оно живет в горах, пустых залах, глубоких колодцах, дразнит путников и помогает летучим мышам ориентироваться в темноте. Иногда кажется, что это голос самого пространства, отвечающий нам, передразнивая сказанное.",
        "ЛАБИРИНТ": "Легенды рассказывают, что первый был построен искусным мастером Дедалом для ужасного Минотавра на острове Крит, и выбраться из него смог лишь герой Тесей с помощью путеводной нити Ариадны. Он может быть выложен из камня на полу собора, выстрижен из живой изгороди в парке или начертан на бумаге как головоломка. Это символ сложного пути, испытания, поиска истины или самого себя в хитросплетениях жизни и запутанных коридорах.",
        "ПУСТЫНЯ": "Бескрайние просторы, где властвует знойное солнце, а дождь – редчайший гость, приносящий бурное, но краткое цветение. Кажется, что здесь нет жизни, но присмотрись: колючие кустарники, юркие ящерицы и выносливые верблюды научились выживать в суровых условиях. Ветер здесь вечный скульптор, создающий из песка причудливые волны-барханы. Она манит абсолютной тишиной, пугает обманчивыми миражами и испытывает на прочность тело и дух человека.",
        "ВУЛКАН": "Он дремлет годами, а иногда и столетиями, скрывая под каменной шапкой огненное сердце Земли и огромное давление газов. Но когда просыпается, его гнев ужасает: пепел затмевает солнце, раскаленная лава потоками стекает по склонам, меняя ландшафт и уничтожая все на своем пути. Древние считали его кузницей богов или входом в преисподнюю. Но после его ярости земля часто становится невероятно плодородной. Это гора, дышащая огнем и пеплом.",
        "СНОВИДЕНИЕ": "Это уникальный театр, разыгрывающийся исключительно для одного зрителя в его голове, пока тело отдыхает в объятиях Морфея. Сценарии здесь не подчиняются логике реальности, знакомые лица ведут себя странно, а законы физики зачастую перестают действовать. Древние считали это явление вестями из другого мира или от богов, психоаналитики – ключом к тайнам подсознания. Оно приходит без спроса и почти всегда исчезает с первыми лучами солнца, оставляя лишь смутные обрывки воспоминаний и сильные эмоции.",
        "МУЗЫКА": "Она родилась, возможно, из простого ритмичного стука камней или пения древнего человека у костра, и постепенно развилась в универсальный язык, понятный без слов любой душе на планете. Она может быть простой и незатейливой, как детская песенка, или сложной и многогранной, как симфония, исполняться на сотнях разных инструментов или рождаться лишь вибрацией голосовых связок. Она способна заставить нас плакать, смеяться, танцевать, вспоминать или маршировать строем. Это всего лишь упорядоченные звуковые колебания, но они способны творить настоящие чудеса с нашими эмоциями и состоянием.",
        "КОМПАС": "Сначала это был просто намагниченный кусочек металла, похожий на ложку и вращающийся на гладкой доске, изобретенный в Древнем Китае для гаданий, а не навигации. Но позже его усовершенствовали, и он изменил ход истории, позволив мореплавателям вроде Колумба и Магеллана отважиться на путешествия через безбрежные океаны, не боясь потеряться. Он всегда упрямо указывает своей стрелкой в одном направлении, используя невидимую магнетическую силу нашей планеты. Даже когда вокруг туман или незнакомая местность, он помогает не сбиться с пути.",
        "АЙСБЕРГ": "Он начинает свою долгую жизнь на суше, являясь частью гигантских ледников или ледяных покровов полярных регионов, а затем, достигнув моря, откалывается с оглушительным треском и отправляется в свободное плавание по холодным океанским течениям. Состоящий из пресной воды, он кажется величественным и безмятежным ледяным островом, но таит в себе скрытую угрозу для кораблей. Большая его часть, до 90% массы, прячется под водой, невидимая для глаз, что делает его коварным и порождает известное выражение о видимой лишь малой части большой проблемы или явления.",
         "МАЯК": "Он стоит несокрушимо на опасных берегах или скалах, одинокий страж перед лицом бескрайнего темного моря. Веками его ритмичный свет – сначала огонь, потом масло, теперь мощные электролампы и линзы Френеля – служил путеводной звездой для моряков. Он предупреждает о рифах и мелях, пробиваясь сквозь туман и шторм своим немигающим взором, показывая безопасный путь домой и являясь символом надежды и бдительности в мире мореплавания.",
        "ПИРАМИДА": "Возведенные трудом бесчисленных рабочих под палящим солнцем древних земель, часто как гробницы для правителей, считавших себя богами или их наместниками. Их строгие геометрические формы, устремленные к небесам, веками будоражат умы инженеров и историков. Внутри скрыты сложные коридоры и камеры, предназначенные защитить усопшего в его путешествии в загробный мир. И хотя многие из них разграблены и тронуты временем, они остаются вечными памятниками амбициям, вере и невероятным организационным способностям исчезнувших цивилизаций.",
        "ЗВЕЗДА": "Лишь светящиеся точки на ночном бархате неба, но каждая – колоссальный шар раскаленного газа на невообразимом расстоянии. Питаемая ядерным синтезом в своем ядре, она миллиарды лет излучает энергию, создавая элементы, из которых состоят планеты и мы сами. Древние видели в их узорах созвездия, слагали мифы и ориентировались по ним в пути. Далекие и недоступные, они – космические двигатели, формирующие вселенную и удерживающие галактики.",
        "КАЛЕНДАРЬ": "Это попытка упорядочить неумолимый бег времени, рожденная из наблюдений за небесными циклами: путь Солнца отмечает дни, фазы Луны складываются в месяцы, а оборот Земли вокруг светила определяет годы. От древних каменных кругов и зарубок на костях до сложных папских указов о високосных годах и современных цифровых планировщиков – его цель неизменна: измерять длительность, планировать будущее, помнить прошлое и синхронизировать жизнь людей, будь то сельскохозяйственные работы, религиозные праздники или деловые встречи.",
        "ЧАСЫ": "Сперва для измерения времени использовали капающую воду, горящие свечи с отметками или тень от гномона под солнцем – люди искали способ делить день на отрезки задолго до появления шестеренок. Позже сложные механизмы с маятниками и анкерными спусками стали отсчитывать мгновения с неумолимой точностью. Сегодня точность обеспечивают вибрации кварца или даже атомные осцилляции. Башенные или наручные, старинные напольные или цифровые на экране – это устройство всегда измеряет ход бытия, деля жизнь на секунды, минуты и часы.",
        "ПАМЯТЬ": "Не вещь, которую можно потрогать, а невидимая, сложнейшая сеть в нейронах нашего мозга. Она позволяет хранить опыт, учиться на ошибках, узнавать близких и строить свое «я». Иногда она остра и ярка, как кинопленка, иногда – ускользающая пустота там, где должно быть имя или факт. Она бывает обманчива, искажая воспоминания, но без нее мы бы плыли в вечном «сейчас», не способные связать события или обрести личность. Это хранилище нашей личной истории.",
        "ОГОНЬ": "Человечество приручило его тысячи лет назад, и это стало поворотным моментом, отделившим нас от животных. Он дал тепло в холод, свет во тьме, способ готовить пищу, делая ее безопаснее, и инструмент для обработки металлов. Он может быть уютным пламенем в очаге, разрушительным пожаром в лесу или контролируемым взрывом в двигателе. И созидатель, и разрушитель, почитаемый как святыня и внушающий страх своей мощью, он – символ превращения, энергии, страсти и опасности; фундаментальная сила природы, укрощенная цивилизацией.",
        "ВОДА": "Покрывая большую часть планеты и составляя значительную часть нас самих, это простое на вид вещество из двух элементов – сама суть жизни. Она падает с неба дождем и снегом, течет реками к морю, замерзает льдом и испаряется невидимым паром. Она утоляет жажду, питает урожай, меняет облик земли эрозией и служит универсальным растворителем. Цивилизации рождались и гибли из-за доступа к ней, и ее наличие – главный признак, который ищут астрономы в поисках внеземной жизни.",
        "РАДУГА": "Часто появляясь после дождя, когда солнце пробивается сквозь капли воды, это захватывающее оптическое явление рисует на небе многоцветную дугу. По сути, это солнечный свет, преломленный и отраженный миллионами крошечных призм-капель, которые разлагают белый свет на спектр, всегда в одном и том же порядке цветов. В мифах – это мост между мирами, знак богов или символ надежды. Хоть она и мимолетна, ее яркая красота всегда вызывает трепет и восхищение – идеальный союз физики и поэзии.",
        "СОЛНЦЕ": "Бесспорный центр нашей планетной семьи, гигантский шар огненной плазмы, чья огромная гравитация удерживает Землю и ее соседей на орбитах. Жизнь на нашей планете полностью зависит от его постоянного потока света и тепла, который движет погодой, питает фотосинтез растений и дает энергию почти всем экосистемам. Хотя издали оно кажется спокойным, его поверхность – бурлящий котел взрывов и магнитных бурь. Древние поклонялись ему как божеству, и его восход и закат по-прежнему задают ритм нашим дням."
    }

def select_word():
    global current_word, hidden_word
    words = list(create_word_bank().keys())
    current_word = random.choice(words)
    hint = create_word_bank()[current_word]
    hidden_word = ["_" for _ in current_word]
    return hint

def update_word_display():
    for widget in word_frame.winfo_children():
        widget.destroy()
    
    for char in hidden_word:
        letter_label = tk.Label(
            word_frame, text=char, font=("Arial", 18, "bold"), width=2,
            relief=tk.RAISED, bg="#3A7734" if char != "_" else "#1E2130", fg="white"
        )
        letter_label.pack(side=tk.LEFT, padx=5, pady=10)

def update_player_info():
    for i, player_frame in enumerate(player_frames):
        name_label, score_label = player_frame.grid_slaves()
        score_label.config(text=f"Очки: {players[i]['score']}")
        player_frame.config(bg="#4DDA6E" if i == current_player_idx else "#16213E")
        name_label.config(bg="#4DDA6E" if i == current_player_idx else "#16213E")
        score_label.config(bg="#4DDA6E" if i == current_player_idx else "#16213E")

def create_alphabet():
    russian_alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    row, col = 0, 0
    
    for widget in alphabet_frame.winfo_children():
        widget.destroy()
    for letter in russian_alphabet:
        button = tk.Button(
            alphabet_frame, text=letter, width=3, height=1,
            font=("Arial", 12, "bold"), bg="#0F3460", fg="white",
            command=lambda l=letter: guess_letter(l)
        )
        button.grid(row=row, column=col, padx=3, pady=3)
        col += 1
        if col >= 11:
            col = 0
            row += 1

def guess_letter(letter):
    global current_player_idx, used_letters, hidden_word
    if letter in used_letters:
        return
    used_letters.add(letter)
    for button in alphabet_frame.winfo_children():
        if button["text"] == letter:
            button.config(state=tk.DISABLED, bg="#16213E", fg="gray")

    if letter in current_word:
        letter_count = 0
        for i, char in enumerate(current_word):
            if char == letter:
                hidden_word[i] = letter
                letter_count += 1
        points = letter_count * current_score
        players[current_player_idx]["score"] += points
        
        update_word_display()
        update_player_info()
        if "_" not in hidden_word:
            messagebox.showinfo("Поздравляем!", f"Слово отгадано: {current_word}")
            next_round()
        else:
            status_label.config(text=f"Буква '{letter}' есть в слове! +{points} очков")
            # Проверяем, является ли текущий игрок ИИ, и если да, даем ему сделать еще один ход
            if players[current_player_idx]["is_ai"]:
                root.after(1000, ai_play)
    else:
        status_label.config(text=f"Буквы '{letter}' нет в слове!")
        next_player()
# Переход
def next_player():
    global current_player_idx
    current_player_idx = (current_player_idx + 1) % len(players)
    update_player_info()
    if not players[current_player_idx]["is_ai"]:
        spin_button.config(state=tk.NORMAL)
        solve_button.config(state=tk.NORMAL)
        status_label.config(text=f"Ход игрока: {players[current_player_idx]['name']}. Вращайте барабан!")
    else:
        spin_button.config(state=tk.DISABLED)
        solve_button.config(state=tk.DISABLED)
        status_label.config(text=f"Ход компьютера: {players[current_player_idx]['name']}")
        root.update()
        root.after(500, ai_play)
# Ход компьютера
def ai_play():
    spin_roulette()
    root.update()
    def choose_letter():
        if is_spinning:
            root.after(50, choose_letter)
        else:
            unused = [l for l in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" if l not in used_letters]
            if unused and current_score != "БАНК" and current_score != "ФИГА":
                letter = random.choice(unused)
                status_label.config(text=f"{players[current_player_idx]['name']} выбирает букву: {letter}")
                root.after(300, lambda: guess_letter(letter))
    
    root.after(200, choose_letter)

# раунд
def next_round():
    global game_round, used_letters
    game_round += 1
    
    if game_round > 3:
        game_over()
        return
    round_label.config(text=f"Раунд: {game_round}")
    hint = select_word()
    hint_label.config(text=f"Подсказка: {hint}")
    used_letters = set()
    update_word_display()
    create_alphabet()
    status_label.config(text=f"Начался раунд {game_round}! Ход игрока {players[current_player_idx]['name']}")
    root.update()
    
    if players[current_player_idx]["is_ai"]:
        root.after(500, ai_play)
# сохранение результатов
def save_game_results():
    player_name = players[0]["name"]
    score = players[0]["score"]
    is_winner = True if players[0]["score"] == max(p["score"] for p in players) else False
    
    # результат
    name = simpledialog.askstring("Сохранение результата", 
                                "Введите ваше имя для записи результата:", 
                                initialvalue=player_name)
    if not name:
        name = player_name
    result = {
        "name": name,
        "score": score,
        "winner": is_winner,
        "round": game_round
    }
    # Загружаем 
    if os.path.exists("game_results.json"):
        try:
            with open("game_results.json", "r", encoding="utf-8") as file:
                all_results = json.load(file)
        except:
            all_results = []
    else:
        all_results = []
    all_results.append(result)
    # Сохраняем
    try:
        with open("game_results.json", "w", encoding="utf-8") as file:
            json.dump(all_results, file, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")

# Завершение
def game_over():
    winner = max(players, key=lambda p: p["score"])
    message = "Игра окончена!\n\nФинальные очки:\n"
    for player in players:
        message += f"{player['name']}: {player['score']}\n"
    message += f"\nПобедитель: {winner['name']} с {winner['score']} очками!"
    messagebox.showinfo("Конец игры", message)
    save_game_results()
    
    if messagebox.askyesno("Новая игра", "Хотите начать новую игру?"):
        new_game()

def solve_attempt():
    global hidden_word
    solution = simpledialog.askstring("Отгадать слово", "Введите отгадку:")
    
    if not solution:
        return
    if solution.upper() == current_word:
        hidden_word = list(current_word)
        update_word_display()
        bonus_points = hidden_word.count("_") * 100
        players[current_player_idx]["score"] += bonus_points
        messagebox.showinfo("Поздравляем!", f"Вы правильно отгадали слово!\nБонус: {bonus_points} очков")
        next_round()
    else:
        messagebox.showinfo("Неверно", "К сожалению, это не правильный ответ.")
        next_player()
#БАрабан
def spin_roulette():
    global is_spinning, current_score
    
    if is_spinning:
        return
    is_spinning = True
    spin_button.config(state=tk.DISABLED)
    solve_button.config(state=tk.DISABLED)
    
    for button in alphabet_frame.winfo_children():
        button.config(state=tk.DISABLED)
    spin_count = 0
    max_spins = random.randint(5, 10)
    def update_roulette():
        nonlocal spin_count
        value = random.choice(roulette_values)
        roulette_label.config(text=str(value))
        if value == "БАНК":
            roulette_label.config(bg="#E94560", fg="white")
        elif value == "ФИГА":
            roulette_label.config(bg="#FFC107", fg="black")
        else:
            roulette_label.config(bg="#16213E", fg="#4DDA6E")
        spin_count += 1
        if spin_count < max_spins:
            root.after(100, update_roulette)
        else:
            stop_roulette()
    update_roulette()
# Остановка 
def stop_roulette():
    global is_spinning, current_score
    current_score = random.choice(roulette_values)
    roulette_label.config(text=str(current_score))
    
    if current_score == "БАНК":
        roulette_label.config(bg="#E94560", fg="white")
        players[current_player_idx]["score"] = 0
        update_player_info()
        status_label.config(text=f"Выпало: БАНК! {players[current_player_idx]['name']} теряет все очки!")
        is_spinning = False  
        root.after(1000, next_player)
        
    elif current_score == "ФИГА":
        roulette_label.config(bg="#FFC107", fg="black")
        status_label.config(text=f"Выпало: ФИГА! {players[current_player_idx]['name']} пропускает ход!")
        is_spinning = False 
        root.after(1000, next_player)
        
    else:
        roulette_label.config(bg="#16213E", fg="#4DDA6E")
        status_label.config(text=f"Выпало: {current_score}. Выберите букву!")
        
        for button in alphabet_frame.winfo_children():
            if button["text"] not in used_letters:
                button.config(state=tk.NORMAL)
        is_spinning = False
    if not players[current_player_idx]["is_ai"]:
        spin_button.config(state=tk.NORMAL)
        solve_button.config(state=tk.NORMAL)
    
    root.update()

def new_game():
    global current_player_idx, game_round, used_letters, current_score
    
    current_player_idx = 0
    game_round = 1
    used_letters = set()
    current_score = 0
    for player in players:
        player["score"] = 0
    hint = select_word()
    hint_label.config(text=f"Подсказка: {hint}")
    round_label.config(text=f"Раунд: {game_round}")
    update_word_display()
    update_player_info()
    create_alphabet()
    roulette_label.config(text="???")
    status_label.config(text="Начните игру, вращая барабан!")

# Запуск
def start_game():
    global players
    player_name = player_name_entry.get().strip() or "Игрок"
    players = [
        {"name": player_name, "score": 0, "is_ai": False},
        {"name": "Компьютер 1", "score": 0, "is_ai": True},
        {"name": "Компьютер 2", "score": 0, "is_ai": True}
    ]
    start_frame.pack_forget()
    game_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    new_game()

# интерфейс
def create_gui():
    global root, start_frame, game_frame, word_frame, alphabet_frame
    global hint_label, round_label, status_label, roulette_label
    global player_frames, spin_button, solve_button, player_name_entry
    
    root = tk.Tk()
    root.title("ПОЛЕ ЧУДЕС")
    root.geometry("800x600")
    root.configure(bg="#1A1A2E")
    start_frame = tk.Frame(root, bg="#1A1A2E", padx=20, pady=20)
    start_frame.pack(fill=tk.BOTH, expand=True)
    tk.Label(start_frame, text="ПОЛЕ ЧУДЕС", font=("Arial", 28, "bold"),
             bg="#1A1A2E", fg="white").pack(pady=30)
    
    name_frame = tk.Frame(start_frame, bg="#1A1A2E")
    name_frame.pack(pady=20)
    tk.Label(name_frame, text="Ваше имя:", font=("Arial", 14),
             bg="#1A1A2E", fg="white").pack(side=tk.LEFT, padx=10)
    
    player_name_entry = tk.Entry(name_frame, font=("Arial", 14), width=20)
    player_name_entry.pack(side=tk.LEFT, padx=10)
    player_name_entry.insert(0, "Игрок")
    tk.Button(start_frame, text="НАЧАТЬ ИГРУ", font=("Arial", 16, "bold"),
              bg="#0F3460", fg="white", padx=20, pady=10, 
              command=start_game).pack(pady=30)
    # Игровой экран
    game_frame = tk.Frame(root, bg="#1A1A2E")
    top_frame = tk.Frame(game_frame, bg="#0F3460", height=40)
    top_frame.pack(fill=tk.X, pady=(0, 10))
    tk.Label(top_frame, text="ПОЛЕ ЧУДЕС", font=("Arial", 16, "bold"),
             bg="#0F3460", fg="white").pack(side=tk.LEFT, padx=20, pady=5)
    
    round_label = tk.Label(top_frame, text="Раунд: 1", font=("Arial", 12),
                          bg="#0F3460", fg="white")
    round_label.pack(side=tk.RIGHT, padx=20, pady=5)
    # Фрейм для слова
    word_container = tk.Frame(game_frame, bg="#16213E", padx=10, pady=10)
    word_container.pack(fill=tk.X, pady=10)
    
    tk.Label(word_container, text="ЗАГАДАННОЕ СЛОВО:", font=("Arial", 14, "bold"),
             bg="#16213E", fg="white").pack(anchor=tk.W, pady=(0, 10))
    word_frame = tk.Frame(word_container, bg="#16213E")
    word_frame.pack(pady=5)
    # Фрейм для подсказки
    hint_frame = tk.Frame(word_container, bg="#16213E", padx=5, pady=5)
    hint_frame.pack(fill=tk.X, pady=5, anchor=tk.W)
    tk.Label(hint_frame, text="ПОДСКАЗКА:", font=("Arial", 12, "bold"),
             bg="#16213E", fg="#FFC107").pack(anchor=tk.W)
    hint_label = tk.Label(hint_frame, text="", font=("Arial", 12, "italic"),
                         bg="#16213E", fg="white", wraplength=700, justify=tk.LEFT)
    hint_label.pack(anchor=tk.W, pady=5)
    # Фрейм для барабана
    roulette_frame = tk.Frame(game_frame, bg="#16213E", padx=10, pady=10)
    roulette_frame.pack(fill=tk.X, pady=10)
    tk.Label(roulette_frame, text="БАРАБАН:", font=("Arial", 14, "bold"),
             bg="#16213E", fg="white").pack(side=tk.LEFT, padx=10)
    
    roulette_label = tk.Label(roulette_frame, text="???", font=("Arial", 20, "bold"),
                             bg="#16213E", fg="#4DDA6E", width=4)
    roulette_label.pack(side=tk.LEFT, padx=20)
    # Кнопки управления
    control_frame = tk.Frame(roulette_frame, bg="#16213E")
    control_frame.pack(side=tk.RIGHT, padx=10)
    
    spin_button = tk.Button(control_frame, text="ВРАЩАТЬ БАРАБАН", font=("Arial", 12, "bold"),
                           bg="#0F3460", fg="white", padx=10, pady=5, command=spin_roulette)
    spin_button.pack(side=tk.LEFT, padx=5)
    
    solve_button = tk.Button(control_frame, text="ОТГАДАТЬ СЛОВО", font=("Arial", 12, "bold"),
                            bg="#0F3460", fg="white", padx=10, pady=5, command=solve_attempt)
    solve_button.pack(side=tk.LEFT, padx=5)
    # Фрейм для игроков
    players_frame = tk.Frame(game_frame, bg="#16213E", padx=10, pady=10)
    players_frame.pack(fill=tk.X, pady=10)
    
    tk.Label(players_frame, text="ИГРОКИ:", font=("Arial", 14, "bold"),
             bg="#16213E", fg="white").pack(anchor=tk.W, pady=(0, 10))
    
    players_container = tk.Frame(players_frame, bg="#16213E")
    players_container.pack(fill=tk.X)
    player_frames = []
    for i in range(3):
        player_frame = tk.Frame(players_container, bg="#16213E", padx=10, pady=5,
                               width=200, height=60)
        player_frame.grid(row=0, column=i, padx=10, pady=5)
        player_frame.grid_propagate(False)
        
        name = ["Игрок", "Компьютер 1", "Компьютер 2"][i]
        
        name_label = tk.Label(player_frame, text=name, font=("Arial", 12, "bold"),
                             bg="#16213E", fg="white")
        name_label.grid(row=0, column=0, sticky=tk.W)
        
        score_label = tk.Label(player_frame, text="Очки: 0", font=("Arial", 12),
                              bg="#16213E", fg="white")
        score_label.grid(row=1, column=0, sticky=tk.W)
        
        player_frames.append(player_frame)
    
    # Статус
    status_frame = tk.Frame(game_frame, bg="#16213E", padx=10, pady=10)
    status_frame.pack(fill=tk.X, pady=10)
    
    tk.Label(status_frame, text="СТАТУС:", font=("Arial", 14, "bold"),
             bg="#16213E", fg="white").pack(anchor=tk.W, pady=(0, 5))
    
    status_label = tk.Label(status_frame, text="Добро пожаловать!",
                           font=("Arial", 12, "italic"), bg="#16213E", fg="white",
                           wraplength=700, justify=tk.LEFT)
    status_label.pack(anchor=tk.W, pady=5)
    # Клаватура
    alphabet_container = tk.Frame(game_frame, bg="#16213E", padx=10, pady=10)
    alphabet_container.pack(fill=tk.X, pady=10)
    
    tk.Label(alphabet_container, text="АЛФАВИТ:", font=("Arial", 14, "bold"),
             bg="#16213E", fg="white").pack(anchor=tk.W, pady=(0, 10))
    
    alphabet_frame = tk.Frame(alphabet_container, bg="#16213E")
    alphabet_frame.pack(fill=tk.X, pady=5)
    return root
# основная функция
def main():
    global root
    root = create_gui()
    root.mainloop()
if __name__ == "__main__":
    main() 
