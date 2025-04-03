from datetime import datetime
import json
import math
import os
import random
import tkinter as tk
from tkinter import messagebox, font, simpledialog, ttk

class GameData:
    def __init__(self):
        self.save_file = "pole_chudes_saves.json"

    def save_game_state(self, players, current_round, current_player):
        save_data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "players": players,
            "current_round": current_round,
            "current_player": current_player
        }
        all_saves = []
        if os.path.exists(self.save_file):
            try:
                with open(self.save_file, "r", encoding="utf-8") as file:
                    all_saves = json.load(file)
            except:
                pass
        all_saves.append(save_data)
        try:
            with open(self.save_file, "w", encoding="utf-8") as file:
                json.dump(all_saves, file, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")
            return False

    def load_game_state(self):
        if not os.path.exists(self.save_file):
            return None

        try:
            with open(self.save_file, "r", encoding="utf-8") as file:
                all_saves = json.load(file)
                if all_saves:
                    return all_saves[-1]
        except Exception as e:
            print(f"Ошибка при загрузке: {e}")

        return None

class PoleChudes:
    def __init__(self, root):
        self.root = root
        self.root.title("ПОЛЕ ЧУДЕС")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)

        self.current_theme = {
            "bg_main": "#1A1A2E",
            "bg_secondary": "#16213E",
            "bg_accent": "#0F3460",
            "fg_main": "#E2E2E2",
            "fg_secondary": "#AEAEAE",
            "accent1": "#E94560",
            "accent2": "#4DDA6E",
            "accent3": "#FFC107",
            "button_bg": "#0F3460",
            "button_fg": "#FFFFFF",
            "header_bg": "#0F3460",
            "cell_bg": "#16213E",
            "cell_revealed": "#4DDA6E",
            "border": "#333333"
        }

        self.root.configure(bg=self.current_theme["bg_main"])
        self.setup_fonts()
        self.setup_styles()
        self.game_data = GameData()
        self.setup_game_variables()
        self.create_interface()
        self.create_word_bank()
        self.new_game()

    def setup_fonts(self):
        default_family = "Helvetica"

        self.title_font = font.Font(family=default_family, size=22, weight="bold")
        self.subtitle_font = font.Font(family=default_family, size=16, weight="bold")
        self.word_font = font.Font(family=default_family, size=18, weight="bold")
        self.score_font = font.Font(family=default_family, size=12)
        self.button_font = font.Font(family=default_family, size=11)
        self.wheel_font = font.Font(family=default_family, size=14, weight="bold")
        self.status_font = font.Font(family=default_family, size=12, slant="italic")
        self.hint_font = font.Font(family=default_family, size=11, slant="italic")

    def setup_styles(self):
        self.style = ttk.Style()
        self.style.configure("TNotebook", background=self.current_theme["bg_main"])
        self.style.configure("TNotebook.Tab",
                            background=self.current_theme["bg_secondary"],
                            foreground="black",
                            padding=[10, 5],
                            font=('Helvetica', 11))

        self.style.map("TNotebook.Tab",
                      background=[("selected", self.current_theme["bg_accent"])],
                      foreground=[("selected", "black")])
        self.style.configure("Treeview",
                            background=self.current_theme["bg_secondary"],
                            foreground=self.current_theme["fg_main"],
                            fieldbackground=self.current_theme["bg_secondary"],
                            font=('Helvetica', 10))
        self.style.map("Treeview",
                      background=[("selected", self.current_theme["bg_accent"])],
                      foreground=[("selected", self.current_theme["fg_main"])])
        self.style.configure("Treeview.Heading",
                            background=self.current_theme["header_bg"],
                            foreground="black",
                            font=('Helvetica', 11, 'bold'))

    def setup_game_variables(self):
        self.wheel_segments = [
            100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
            "БАНКРОТ", "ПРИЗ", "+", "x2", "x3", "ФИГА", 100, 200, 300, 400
        ]

        self.wrong_letter_phrases = [
            "Увы, такой буквы нет в слове!",
            "Нет, не угадали!",
            "Эта буква отсутствует!",
            "Буква хорошая, но её нет!",
            "Не повезло!",
            "Сожалею, но такой буквы нет!",
            "Нет, не сегодня!",
            "Зал аплодирует вашей смелости, но буквы нет!",
            "Ваш энтузиазм достоин восхищения, но буквы мы не находим!",
            "Ваша буква решила сегодня отдохнуть!",
            "Такой буквы тут точно нет!",
            "Мимо!",
            "Промах!",
            "И снова нет!",
            "А вот и не угадали!",
            "Увы и ах, мимо кассы!",
            "Эта буква есть... но не в этом слове!",
            "Какая жалость, буквы нет!",
            "Вы были так близки... к тому, чтобы ошибиться!",
            "Буква сказала решительное НЕТ!",
            "Табло молчит... значит, буквы нет!",
            "Может, в другом слове? В этом - точно нет!",
            "Мы искали-искали... и не нашли!",
            "Пусто!",
            "Эта буква сегодня не пришла на программу!",
            "Как бы нам ни хотелось, но НЕТ!",
            "Попробуйте другую, эта не подошла!",
            "Мне тут шепнули на ухо... Нет такой буквы!",
            "Режиссер в аппаратной качает головой - нету!",
            "Наш суперкомпьютер, отвечающий за буквы, говорит 'Ошибка 404: Буква не найдена'!",
            "Это слово такое загадочное... даже такой хорошей буквы в нем нет!",
            "Автор этого слова явно экономил на буквах! Вашей - нет.",
            "По правилам нашей игры... вы не угадали!",
            "Даже если бы и была, приз всё равно бы спрятался!",
            "Нет, и даже не просите! Бюджет на буквы сегодня ограничен.",
            "Весь зал затаил дыхание... и выдохнул. Не угадали!",
            "Я бы и рад открыть, но в сценарии этой буквы нет!",
            "Я бы с радостью, честное слово! Но увы, пусто.",
            "Хм, смелый выбор буквы! Но, к сожалению, неверный.",
            "Ваши соперники мысленно вам аплодируют... буквы-то нет!",
            "Табло отказывается показывать вашу букву. Сопротивляется!",
            "Эта буква есть в алфавите, но создатели слова решили её проигнорировать!",
            "Игра говорит 'НЕТ'. А с игрой не поспоришь... или поспоришь?",
            "Может, буква появится в рекламной паузе? Сейчас – точно нет!",
            "Шкатулку хотите? А вот буквы нет!"
        ]

        self.prizes = [
            "Чайный сервиз", "Микроволновка", "Стиральная машина",
            "Мультиварка", "Пылесос", "Телевизор", "Смартфон", "Планшет",
            "Поездка в Сочи", "Домашний кинотеатр"
        ]

        self.studio_gifts = [
            {"name": "Бутылка водки", "cost": 200},
            {"name": "Домашние соленья", "cost": 150},
            {"name": "Самодельная матрёшка", "cost": 300},
            {"name": "Торт", "cost": 250},
            {"name": "Сомбреро", "cost": 350},
            {"name": "Шарф болельщика", "cost": 180},
            {"name": "Банка мёда", "cost": 220},
            {"name": "Шкатулка с украшениями", "cost": 400},
            {"name": "Национальный костюм", "cost": 500},
            {"name": "Музыкальный инструмент", "cost": 450}
        ]

        self.current_word_data = None
        self.hidden_word = []
        self.used_letters = set()
        self.players = [
            {"name": "Игрок", "score": 0, "is_human": True, "consecutive_correct": 0, "multiplier": 1},
            {"name": "ИИ 1", "score": 0, "is_human": False, "consecutive_correct": 0, "multiplier": 1},
            {"name": "ИИ 2", "score": 0, "is_human": False, "consecutive_correct": 0, "multiplier": 1}
        ]
        self.current_player_idx = 0
        self.current_wheel_value = 0
        self.is_spinning = False
        self.game_round = 1
        self.wheel_angle = 0

    def create_interface(self):
        main_bg_frame = tk.Frame(self.root, bg=self.current_theme["bg_main"])
        main_bg_frame.pack(fill=tk.BOTH, expand=True)

        header_frame = tk.Frame(main_bg_frame, bg=self.current_theme["header_bg"],
                               height=60, padx=10, pady=5)
        header_frame.pack(fill=tk.X, padx=0, pady=0)

        game_title = tk.Label(header_frame, text="ПОЛЕ ЧУДЕС",
                             font=self.title_font,
                             bg=self.current_theme["header_bg"],
                             fg=self.current_theme["fg_main"])
        game_title.pack(side=tk.LEFT, padx=15)

        info_frame = tk.Frame(header_frame, bg=self.current_theme["header_bg"])
        info_frame.pack(side=tk.RIGHT, padx=10)

        self.round_label = tk.Label(info_frame, text="Раунд: 1",
                                   font=self.score_font,
                                   bg=self.current_theme["header_bg"],
                                   fg=self.current_theme["fg_main"])
        self.round_label.pack(side=tk.RIGHT, padx=10)

        notebook_frame = tk.Frame(main_bg_frame, bg=self.current_theme["bg_main"], padx=5, pady=5)
        notebook_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.notebook = ttk.Notebook(notebook_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.game_frame = tk.Frame(self.notebook, bg=self.current_theme["bg_main"])
        self.notebook.add(self.game_frame, text="Игра")

        self.stats_frame = tk.Frame(self.notebook, bg=self.current_theme["bg_main"])
        self.notebook.add(self.stats_frame, text="Статистика")

        self.settings_frame = tk.Frame(self.notebook, bg=self.current_theme["bg_main"])
        self.notebook.add(self.settings_frame, text="Настройки")

        self.help_frame = tk.Frame(self.notebook, bg=self.current_theme["bg_main"])
        self.notebook.add(self.help_frame, text="Помощь")

        self.setup_game_screen()

        self.setup_stats_screen()

        self.setup_settings_screen()

        self.setup_help_screen()

        footer_frame = tk.Frame(main_bg_frame, bg=self.current_theme["bg_secondary"],
                               height=25)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

        version_label = tk.Label(footer_frame, text="Поле Чудес v1.0 © 2025",
                                font=("Helvetica", 9),
                                bg=self.current_theme["bg_secondary"],
                                fg=self.current_theme["fg_secondary"])
        version_label.pack(side=tk.RIGHT, padx=10)

    def setup_help_screen(self):
        help_header = tk.Label(self.help_frame, text="ПРАВИЛА ИГРЫ",
                              font=self.title_font, bg=self.current_theme["bg_main"],
                              fg=self.current_theme["fg_main"])
        help_header.pack(pady=15)

        help_scroll = tk.Frame(self.help_frame, bg=self.current_theme["bg_main"])
        help_scroll.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        scrollbar = tk.Scrollbar(help_scroll)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        help_text = tk.Text(help_scroll, wrap=tk.WORD,
                           bg=self.current_theme["bg_secondary"],
                           fg=self.current_theme["fg_main"],
                           font=("Helvetica", 11),
                           padx=10, pady=10,
                           width=70, height=20,
                           yscrollcommand=scrollbar.set)
        help_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=help_text.yview)

        help_content = """
ПОЛЕ ЧУДЕС - ПРАВИЛА ИГРЫ

ЦЕЛЬ ИГРЫ:
Цель игры - отгадать загаданное слово, вращая барабан и предлагая буквы.
Игрок, который наберет больше всего очков, станет победителем.

КАК ИГРАТЬ:

1. ВРАЩЕНИЕ БАРАБАНА:
   Нажмите кнопку "ВРАЩАТЬ БАРАБАН", чтобы определить стоимость хода.
   Барабан может показать следующее:
   - Очки (100-1000): Если угаданная буква есть в слове, вы получаете соответствующие очки за каждое появление.
   - БАНКРОТ: Вы теряете все свои очки, и ход переходит дальше.
   - ПРИЗ: Вы можете выбрать между призом и большей суммой очков.
   - +: Вы получаете дополнительный ход.
   - x2, x3: Множитель очков применяется к вашим будущим ходам.
   - ФИГА: Вы пропускаете ход.

2. ПРЕДЛОЖЕНИЕ БУКВЫ:
   После вращения барабана выберите букву, которая, по вашему мнению, есть в слове.
   Если буква есть в слове, она открывается, и вы получаете очки.
   Если буквы нет в слове, ход переходит к следующему игроку.

3. ОТГАДЫВАНИЕ СЛОВА:
   Если вы думаете, что знаете слово, вы можете нажать кнопку "ОТГАДАТЬ СЛОВО".
   При правильном ответе вы получаете бонусные очки за каждую неоткрытую букву.
   При неправильном ответе ход переходит дальше.

4. ШКАТУЛКИ:
   Если вы угадываете 3 буквы подряд, вы получаете шкатулку с призом.

5. ПОДАРКИ В СТУДИЮ:
   Вы можете потратить очки, чтобы сделать подарок ведущему.

6. ИСПОЛЬЗОВАНИЕ ПОДСКАЗКИ:
   Если у вас есть как минимум 500 очков, вы можете использовать подсказку.
   Это откроет случайную букву в слове.

ПЕРСОНАЖИ:

ВЕДУЩИЙ:
Ведет игру и комментирует ходы игроков.

КОМПЬЮТЕРНЫЕ ИГРОКИ:
Если вы играете с компьютером, у вас есть два противника:
- ИИ 1: Фокусируется на наиболее распространенных буквах
- ИИ 2: Фокусируется на согласных

ОЧКИ И ПОБЕДА:
Игра обычно состоит из трех раундов.
В конце каждого раунда начинается новое слово.
В конце игры побеждает тот, у кого больше всего очков.

СОВЕТЫ:
- Вращайте барабан в начале каждого хода
- Следите за буквами, которые уже были названы
- Читайте подсказку - она дает намеки на слово
- Если вы знаете слово, рекомендуется сразу его отгадать

УДАЧИ В ИГРЕ!
"""

        help_text.insert(tk.END, help_content)
        help_text.config(state=tk.DISABLED)

    def setup_game_screen(self):
        game_container = tk.Frame(self.game_frame,
                                 bg=self.current_theme["bg_main"],
                                 padx=10, pady=5)
        game_container.pack(fill=tk.BOTH, expand=True)

        top_frame = tk.Frame(game_container, bg=self.current_theme["bg_main"])
        top_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        top_frame.columnconfigure(0, weight=2)
        top_frame.columnconfigure(1, weight=2)
        top_frame.columnconfigure(2, weight=1)

        left_frame = tk.Frame(top_frame, bg=self.current_theme["bg_main"])
        left_frame.grid(row=0, column=0, sticky="nsew", padx=5)

        word_container = tk.Frame(left_frame,
                                 bg=self.current_theme["bg_secondary"],
                                 bd=2, relief=tk.RIDGE,
                                 padx=15, pady=15)
        word_container.pack(fill=tk.BOTH, expand=True, pady=5)

        word_label = tk.Label(word_container,
                             text="ЗАГАДАННОЕ СЛОВО:",
                             font=self.subtitle_font,
                             bg=self.current_theme["bg_secondary"],
                             fg=self.current_theme["fg_main"])
        word_label.pack(anchor=tk.W, pady=(0, 10))

        self.word_frame = tk.Frame(word_container, bg=self.current_theme["bg_secondary"])
        self.word_frame.pack(pady=5, fill=tk.X)

        hint_frame = tk.Frame(word_container,
                             bg=self.current_theme["bg_secondary"],
                             padx=5, pady=5)
        hint_frame.pack(fill=tk.X, pady=10, anchor=tk.W)

        hint_label = tk.Label(hint_frame,
                             text="ПОДСКАЗКА:",
                             font=self.score_font,
                             bg=self.current_theme["bg_secondary"],
                             fg=self.current_theme["accent3"])
        hint_label.pack(anchor=tk.W)

        self.hint_text = tk.Label(hint_frame,
                                 text="",
                                 font=self.hint_font,
                                 bg=self.current_theme["bg_secondary"],
                                 fg=self.current_theme["fg_main"],
                                 wraplength=400,
                                 justify=tk.LEFT)
        self.hint_text.pack(anchor=tk.W, pady=5)

        middle_frame = tk.Frame(top_frame, bg=self.current_theme["bg_main"])
        middle_frame.grid(row=0, column=1, sticky="nsew", padx=5)

        wheel_container = tk.Frame(middle_frame,
                                  bg=self.current_theme["bg_secondary"],
                                  bd=2, relief=tk.RIDGE,
                                  padx=10, pady=10)
        wheel_container.pack(fill=tk.BOTH, expand=True, pady=5)

        self.wheel_canvas = tk.Canvas(wheel_container,
                                     width=220, height=220,
                                     bg=self.current_theme["bg_secondary"],
                                     highlightthickness=1,
                                     highlightbackground=self.current_theme["border"])
        self.wheel_canvas.pack(pady=10)

        self.draw_wheel()

        right_frame = tk.Frame(top_frame, bg=self.current_theme["bg_main"])
        right_frame.grid(row=0, column=2, sticky="nsew", padx=5)

        results_container = tk.Frame(right_frame,
                                   bg=self.current_theme["bg_secondary"],
                                   bd=2, relief=tk.RIDGE,
                                   padx=10, pady=10)
        results_container.pack(fill=tk.X, pady=5)

        result_frame = tk.Frame(results_container,
                               bg=self.current_theme["bg_accent"],
                               bd=1, relief=tk.GROOVE,
                               padx=10, pady=5)
        result_frame.pack(fill=tk.X)

        self.wheel_result_label = tk.Label(result_frame,
                                         text="РЕЗУЛЬТАТ ВРАЩЕНИЯ",
                                         font=self.score_font,
                                         bg=self.current_theme["bg_accent"],
                                         fg=self.current_theme["fg_main"])
        self.wheel_result_label.pack(pady=2)

        value_frame = tk.Frame(results_container,
                              bg=self.current_theme["bg_secondary"],
                              bd=1, relief=tk.SUNKEN,
                              padx=5, pady=5)
        value_frame.pack(fill=tk.X, pady=5)

        self.wheel_value_label = tk.Label(value_frame,
                                        text="ВРАЩАЙТЕ БАРАБАН",
                                        font=self.wheel_font,
                                        bg=self.current_theme["bg_secondary"],
                                        fg=self.current_theme["fg_main"])
        self.wheel_value_label.pack(pady=2)

        controls_container = tk.Frame(right_frame,
                                     bg=self.current_theme["bg_secondary"],
                                     bd=2, relief=tk.RIDGE,
                                     padx=10, pady=5)
        controls_container.pack(fill=tk.X, pady=5)

        controls_header = tk.Label(controls_container,
                                  text="УПРАВЛЕНИЕ ИГРОЙ",
                                  font=self.subtitle_font,
                                  bg=self.current_theme["bg_secondary"],
                                  fg="black")
        controls_header.pack(pady=(0, 5))

        controls_frame = tk.Frame(controls_container, bg=self.current_theme["bg_secondary"])
        controls_frame.pack(fill=tk.X)

        self.spin_button = tk.Button(controls_frame,
                                    text="ВРАЩАТЬ БАРАБАН",
                                    command=self.spin_wheel,
                                    font=self.button_font,
                                    bg=self.current_theme["button_bg"],
                                    fg="white",
                                    activebackground=self.current_theme["bg_accent"],
                                    activeforeground="black",
                                    relief=tk.RAISED,
                                    bd=2,
                                    padx=5, pady=3,
                                    width=18)
        self.spin_button.pack(pady=3, fill=tk.X)

        self.solve_button = tk.Button(controls_frame,
                                     text="ОТГАДАТЬ СЛОВО",
                                     command=self.solve_attempt,
                                     font=self.button_font,
                                     bg=self.current_theme["button_bg"],
                                     fg="white",
                                     activebackground=self.current_theme["bg_accent"],
                                     activeforeground="black",
                                     relief=tk.RAISED,
                                     bd=2,
                                     padx=5, pady=3,
                                     width=18)
        self.solve_button.pack(pady=3, fill=tk.X)

        self.gift_button = tk.Button(controls_frame,
                                    text="ПОДАРОК В СТУДИЮ",
                                    command=self.show_gift_dialog,
                                    font=self.button_font,
                                    bg=self.current_theme["bg_accent"],
                                    fg="white",
                                    activebackground=self.current_theme["bg_secondary"],
                                    activeforeground="black",
                                    relief=tk.RAISED,
                                    bd=2,
                                    padx=5, pady=3,
                                    width=18)
        self.gift_button.pack(pady=3, fill=tk.X)

        self.hint_button = tk.Button(controls_frame,
                                    text="ПОДСКАЗКА (500 очков)",
                                    command=self.use_hint,
                                    font=self.button_font,
                                    bg=self.current_theme["bg_accent"],
                                    fg="white",
                                    activebackground=self.current_theme["bg_secondary"],
                                    activeforeground="black",
                                    relief=tk.RAISED,
                                    bd=2,
                                    padx=5, pady=3,
                                    width=18)
        self.hint_button.pack(pady=3, fill=tk.X)

        status_container = tk.Frame(right_frame,
                                   bg=self.current_theme["bg_accent"],
                                   bd=2, relief=tk.RIDGE,
                                   padx=10, pady=10)
        status_container.pack(fill=tk.X, pady=5)

        status_header = tk.Label(status_container,
                                text="КОММЕНТАРИЙ ВЕДУЩЕГО:",
                                font=self.subtitle_font,
                                bg=self.current_theme["bg_accent"],
                                fg="white")
        status_header.pack(anchor=tk.W, pady=(0, 5))

        status_frame = tk.Frame(status_container,
                               bg=self.current_theme["bg_secondary"],
                               bd=1, relief=tk.GROOVE,
                               padx=10, pady=10)
        status_frame.pack(fill=tk.X)

        self.status_text = tk.Label(status_frame,
                                   text="Добро пожаловать в игру Поле Чудес!",
                                   font=self.status_font,
                                   bg=self.current_theme["bg_secondary"],
                                   fg=self.current_theme["fg_main"],
                                   wraplength=270,
                                   justify=tk.LEFT)
        self.status_text.pack(fill=tk.X)

        middle_frame = tk.Frame(game_container, bg=self.current_theme["bg_main"])
        middle_frame.pack(fill=tk.X, pady=5)

        players_container = tk.Frame(middle_frame,
                                    bg=self.current_theme["bg_secondary"],
                                    bd=2, relief=tk.RIDGE,
                                    padx=10, pady=5)
        players_container.pack(fill=tk.X)

        players_header = tk.Label(players_container,
                                 text="ИГРОКИ",
                                 font=self.subtitle_font,
                                 bg=self.current_theme["bg_secondary"],
                                 fg="white")
        players_header.pack(pady=(0, 5))

        player_frame = tk.Frame(players_container, bg=self.current_theme["bg_secondary"])
        player_frame.pack(fill=tk.X, pady=5)

        self.player_labels = []

        player_width_pct = 100 // len(self.players)

        for i, player in enumerate(self.players):
            player_column = tk.Frame(player_frame,
                                    bg=self.current_theme["bg_secondary"])
            player_column.grid(row=0, column=i, padx=5, pady=3, sticky="nsew")

            player_frame.columnconfigure(i, weight=1)

            p_frame = tk.Frame(player_column,
                              bg=self.current_theme["bg_main"],
                              bd=1, relief=tk.RAISED,
                              padx=5, pady=5)
            p_frame.pack(fill=tk.X, expand=True)

            name_label = tk.Label(p_frame,
                                 text=player["name"],
                                 font=self.score_font,
                                 bg=self.current_theme["bg_main"],
                                 fg=self.current_theme["fg_main"])
            name_label.pack(pady=(0, 2))

            score_label = tk.Label(p_frame,
                                  text=f"Счет: {player['score']}",
                                  font=self.score_font,
                                  bg=self.current_theme["bg_main"],
                                  fg=self.current_theme["fg_main"])
            score_label.pack(pady=2)

            multiplier_label = tk.Label(p_frame,
                                      text=f"Множитель: x{player['multiplier']}",
                                      font=self.score_font,
                                      bg=self.current_theme["bg_main"],
                                      fg=self.current_theme["fg_main"])
            multiplier_label.pack(pady=2)

            consecutive_label = tk.Label(p_frame,
                                      text=f"Подряд: {player['consecutive_correct']}/3",
                                      font=self.score_font,
                                      bg=self.current_theme["bg_main"],
                                      fg=self.current_theme["fg_main"])
            consecutive_label.pack(pady=2)

            active_marker = tk.Label(p_frame,
                                    text="▶ ХОД ▶",
                                    font=("Helvetica", 9, "bold"),
                                    bg=self.current_theme["accent2"],
                                    fg=self.current_theme["fg_main"],
                                    padx=5, pady=1)
            active_marker.pack(pady=2)
            active_marker.pack_forget()

            self.player_labels.append({
                "name": name_label,
                "score": score_label,
                "active": active_marker,
                "multiplier": multiplier_label,
                "consecutive": consecutive_label
            })

        bottom_frame = tk.Frame(game_container, bg=self.current_theme["bg_main"])
        bottom_frame.pack(fill=tk.X, side=tk.BOTTOM, pady=5)

        alphabet_container = tk.Frame(bottom_frame,
                                     bg=self.current_theme["bg_secondary"],
                                     bd=2, relief=tk.RIDGE,
                                     padx=10, pady=5)
        alphabet_container.pack(fill=tk.X)

        alphabet_header = tk.Label(alphabet_container,
                                  text="АЛФАВИТ",
                                  font=self.subtitle_font,
                                  bg=self.current_theme["bg_secondary"],
                                  fg="white")
        alphabet_header.pack(pady=(0, 5))

        self.letters_frame = tk.Frame(alphabet_container,
                                     bg=self.current_theme["bg_secondary"],
                                     padx=5, pady=5)
        self.letters_frame.pack(fill=tk.X, expand=True)

        self.create_alphabet()

    def show_gift_dialog(self):
        """Показывает диалог выбора подарка для ведущего"""
        current_player = self.players[self.current_player_idx]

        if not current_player["is_human"]:
            messagebox.showinfo("Подарок", "Только человек-игрок может сделать подарок.")
            return

        dialog = tk.Toplevel(self.root)
        dialog.title("ПОДАРОК В СТУДИЮ")
        dialog.geometry("400x400")
        dialog.config(bg=self.current_theme["bg_main"])

        header_label = tk.Label(dialog, text="ВЫБЕРИТЕ ПОДАРОК",
                              font=self.title_font,
                              bg=self.current_theme["bg_main"],
                              fg=self.current_theme["fg_main"])
        header_label.pack(pady=10)

        score_label = tk.Label(dialog, text=f"Ваши очки: {current_player['score']}",
                             font=self.score_font,
                             bg=self.current_theme["bg_main"],
                             fg=self.current_theme["fg_main"])
        score_label.pack(pady=5)

        gifts_frame = tk.Frame(dialog, bg=self.current_theme["bg_main"])
        gifts_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        scrollbar = tk.Scrollbar(gifts_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        gifts_listbox = tk.Listbox(gifts_frame,
                                 bg=self.current_theme["bg_secondary"],
                                 fg=self.current_theme["fg_main"],
                                 selectbackground=self.current_theme["bg_accent"],
                                 font=("Helvetica", 12),
                                 height=10,
                                 yscrollcommand=scrollbar.set)
        gifts_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=gifts_listbox.yview)

        for gift in self.studio_gifts:
            gifts_listbox.insert(tk.END, f"{gift['name']} ({gift['cost']} очков)")

        def select_gift():
            selection = gifts_listbox.curselection()
            if not selection:
                messagebox.showinfo("Выбор подарка", "Пожалуйста, выберите подарок из списка.")
                return

            selected_gift = self.studio_gifts[selection[0]]
            gift_cost = selected_gift["cost"]

            if current_player["score"] < gift_cost:
                messagebox.showinfo("Недостаточно очков",
                                  f"Для этого подарка нужно {gift_cost} очков. У вас {current_player['score']}.")
                return

            confirm = messagebox.askyesno("Подтверждение",
                                        f"Вы хотите подарить '{selected_gift['name']}' за {gift_cost} очков?")
            if confirm:
                current_player["score"] -= gift_cost
                self.update_player_indicators()

                messagebox.showinfo("Подарок отправлен",
                                  f"Ведущий получил ваш подарок: {selected_gift['name']}!\n"
                                  f"Зал аплодирует вашей щедрости!")

                message = f"Игрок дарит ведущему {selected_gift['name']}! Аплодисменты!"
                self.status_text.config(text=message)

                dialog.destroy()

        select_button = tk.Button(dialog, text="ПОДАРИТЬ",
                                command=select_gift,
                                font=self.button_font,
                                bg=self.current_theme["button_bg"],
                                fg="white",
                                width=15)
        select_button.pack(pady=10)

        cancel_button = tk.Button(dialog, text="ОТМЕНА",
                                command=dialog.destroy,
                                font=self.button_font,
                                bg=self.current_theme["bg_accent"],
                                fg="white",
                                width=15)
        cancel_button.pack(pady=5)

    def use_hint(self):
        current_player = self.players[self.current_player_idx]

        if not current_player["is_human"]:
            messagebox.showinfo("Подсказка", "Только человек-игрок может использовать подсказку.")
            return

        if current_player["score"] < 500:
            messagebox.showinfo("Недостаточно очков",
                               f"Для использования подсказки нужно минимум 500 очков. У вас {current_player['score']}.")
            return

        confirm = messagebox.askyesno("Использование подсказки",
                                     "Вы хотите потратить 500 очков, чтобы открыть одну случайную букву?")

        if not confirm:
            return

        current_player["score"] -= 500
        self.update_player_indicators()

        hidden_indices = [i for i, char in enumerate(self.hidden_word) if char == "_"]

        if not hidden_indices:
            messagebox.showinfo("Подсказка", "Все буквы уже открыты!")
            return

        random_index = random.choice(hidden_indices)
        reveal_letter = self.current_word[random_index]

        self.used_letters.add(reveal_letter)

        new_hidden_word = list(self.hidden_word)

        for i, char in enumerate(self.current_word):
            if char == reveal_letter:
                new_hidden_word[i] = reveal_letter

        self.hidden_word = new_hidden_word

        self.update_word_display()

        if reveal_letter in self.letter_buttons:
            self.letter_buttons[reveal_letter].config(
                state=tk.DISABLED,
                bg=self.current_theme["bg_secondary"],
                fg=self.current_theme["fg_secondary"])

        messagebox.showinfo("Подсказка", f"Открыта буква: {reveal_letter}")

        if "_" not in self.hidden_word:
            self.word_solved()
            return

    def setup_stats_screen(self):
        stats_header = tk.Label(self.stats_frame, text="СТАТИСТИКА ИГРЫ",
                              font=self.title_font, bg=self.current_theme["bg_main"],
                              fg=self.current_theme["fg_main"])
        stats_header.pack(pady=10)

        stats_content = tk.Frame(self.stats_frame, bg=self.current_theme["bg_main"])
        stats_content.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        columns = ("Время", "Раунд", "Лидирующий игрок", "Очки")
        self.stats_tree = ttk.Treeview(stats_content, columns=columns, show="headings")

        for col in columns:
            self.stats_tree.heading(col, text=col)
            self.stats_tree.column(col, width=100)

        self.stats_tree.pack(fill=tk.BOTH, expand=True, pady=5)

        refresh_button = tk.Button(stats_content, text="ОБНОВИТЬ",
                                 command=self.update_stats_display,
                                 font=self.button_font,
                                 bg=self.current_theme["button_bg"],
                                 fg="black")
        refresh_button.pack(pady=10)

        save_button = tk.Button(stats_content, text="СОХРАНИТЬ ИГРУ",
                              command=self.save_current_game,
                              font=self.button_font,
                              bg=self.current_theme["button_bg"],
                              fg="black")
        save_button.pack(pady=5)

    def setup_settings_screen(self):
        settings_header = tk.Label(self.settings_frame, text="НАСТРОЙКИ ИГРЫ",
                                  font=self.title_font,
                                  bg=self.current_theme["bg_main"],
                                  fg=self.current_theme["fg_main"])
        settings_header.pack(pady=10)

        settings_content = tk.Frame(self.settings_frame, bg=self.current_theme["bg_main"])
        settings_content.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        theme_frame = tk.Frame(settings_content, bg=self.current_theme["bg_main"])
        theme_frame.pack(fill=tk.X, pady=10)

        theme_label = tk.Label(theme_frame, text="Тема:",
                             font=self.score_font,
                             bg=self.current_theme["bg_main"],
                             fg=self.current_theme["fg_main"])
        theme_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        self.theme_var = tk.StringVar(value="dark")
        dark_radio = tk.Radiobutton(theme_frame, text="Тёмная", variable=self.theme_var, value="dark",
                                  command=self.change_theme,
                                  bg=self.current_theme["bg_main"],
                                  fg=self.current_theme["fg_main"],
                                  selectcolor=self.current_theme["bg_accent"])
        dark_radio.grid(row=0, column=1, padx=5, pady=5)

        light_radio = tk.Radiobutton(theme_frame, text="Светлая", variable=self.theme_var, value="light",
                                   command=self.change_theme,
                                   bg=self.current_theme["bg_main"],
                                   fg=self.current_theme["fg_main"],
                                   selectcolor=self.current_theme["bg_accent"])
        light_radio.grid(row=0, column=2, padx=5, pady=5)

        font_frame = tk.Frame(settings_content, bg=self.current_theme["bg_main"])
        font_frame.pack(fill=tk.X, pady=10)

        font_label = tk.Label(font_frame, text="Размер шрифта:",
                            font=self.score_font,
                            bg=self.current_theme["bg_main"],
                            fg=self.current_theme["fg_main"])
        font_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        self.font_scale = tk.Scale(font_frame, from_=8, to=18, orient=tk.HORIZONTAL,
                                 command=self.change_font_size,
                                 bg=self.current_theme["bg_secondary"],
                                 fg=self.current_theme["fg_main"],
                                 troughcolor=self.current_theme["bg_accent"], length=200)
        self.font_scale.set(12)
        self.font_scale.grid(row=0, column=1, padx=5, pady=5)

        rounds_frame = tk.Frame(settings_content, bg=self.current_theme["bg_main"])
        rounds_frame.pack(fill=tk.X, pady=10)

        rounds_label = tk.Label(rounds_frame, text="Количество раундов:",
                              font=self.score_font,
                              bg=self.current_theme["bg_main"],
                              fg=self.current_theme["fg_main"])
        rounds_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        self.rounds_var = tk.IntVar(value=3)
        for i, r in enumerate([3, 5, 7]):
            round_radio = tk.Radiobutton(rounds_frame, text=str(r), variable=self.rounds_var, value=r,
                                       bg=self.current_theme["bg_main"],
                                       fg=self.current_theme["fg_main"],
                                       selectcolor=self.current_theme["bg_accent"])
            round_radio.grid(row=0, column=i+1, padx=5, pady=5)

        reset_button = tk.Button(settings_content, text="СБРОСИТЬ НАСТРОЙКИ",
                               command=self.reset_settings,
                               font=self.button_font,
                               bg=self.current_theme["button_bg"],
                               fg="black")
        reset_button.pack(pady=20)

    def create_word_bank(self):
        self.word_bank = [
            {"word": "ПРОГРАММИРОВАНИЕ", "hint": "Процесс создания компьютерных программ"},
            {"word": "ТЕЛЕВИЗОР", "hint": "Устройство для просмотра передач"},
            {"word": "МИКРОСКОП", "hint": "Прибор для наблюдения очень маленьких объектов"},
            {"word": "БИБЛИОТЕКА", "hint": "Учреждение, где хранятся книги"},
            {"word": "ФОТОГРАФИЯ", "hint": "Изображение, полученное с помощью специальной камеры"},
            {"word": "КОМПЬЮТЕР", "hint": "Электронное устройство для обработки информации"},
            {"word": "ПУТЕШЕСТВИЕ", "hint": "Перемещение из одного места в другое"},
            {"word": "ВЕЛОСИПЕД", "hint": "Двухколесное транспортное средство"},
            {"word": "ШАХМАТЫ", "hint": "Настольная логическая игра"},
            {"word": "ПИРАМИДА", "hint": "Древнее сооружение в форме геометрической фигуры"},
            {"word": "АССИСТЕНТКА", "hint": "Девушка, помогающая в телешоу"},
            {"word": "ЯКУБОВИЧ", "hint": "Фамилия известного ведущего программы 'Поле Чудес'"},
            {"word": "АЛГОРИТМ", "hint": "Чёткая последовательность действий для решения задачи"},
            {"word": "ШИФРОВАНИЕ", "hint": "Процесс превращения информации в секретный код"},
            {"word": "ЭЛЕКТРИЧЕСТВО", "hint": "Направленное движение заряженных частиц"},
            {"word": "КАЛЕЙДОСКОП", "hint": "Оптический прибор-игрушка с цветными узорами"},
            {"word": "ТЕЛЕСКОП", "hint": "Прибор для наблюдения за далекими небесными телами"},
            {"word": "АККУМУЛЯТОР", "hint": "Устройство для накопления энергии (часто электрической)"},
            {"word": "ИНТЕРФЕЙС", "hint": "Средство взаимодействия человека и машины"},
            {"word": "ЭКВАТОР", "hint": "Воображаемая линия, делящая Землю на два полушария"},
            {"word": "МЕРИДИАН", "hint": "Условная линия, соединяющая Северный и Южный полюсы"},
            {"word": "АРХИПЕЛАГ", "hint": "Группа близко расположенных островов"},
            {"word": "ФОТОСИНТЕЗ", "hint": "Процесс, с помощью которого растения 'едят' солнечный свет"},
            {"word": "ВУЛКАН", "hint": "Геологическое образование, извергающее лаву и пепел"},
            {"word": "МЕТАМОРФОЗА", "hint": "Превращение, например, гусеницы в бабочку"},
            {"word": "МИМИКРИЯ", "hint": "Подражание одного живого существа другому или неживому объекту"},
            {"word": "АРХИТЕКТУРА", "hint": "Искусство и наука строить, проектировать здания"},
            {"word": "СКУЛЬПТУРА", "hint": "Вид искусства, произведения которого имеют объёмную форму"},
            {"word": "ДИРИЖЁР", "hint": "Руководитель оркестра или хора"},
            {"word": "РЕНЕССАНС", "hint": "Эпоха Возрождения в европейской культуре"},
            {"word": "ПАПИРУС", "hint": "Писчий материал, распространённый в Древнем Египте"},
            {"word": "МЕЦЕНАТ", "hint": "Богатый покровитель наук и искусств"},
            {"word": "СЕРЕНАДА", "hint": "Вечерняя песня влюблённого под окном возлюбленной"},
            {"word": "ПСЕВДОНИМ", "hint": "Вымышленное имя писателя или артиста"},
            {"word": "ВДОХНОВЕНИЕ", "hint": "Особое состояние, прилив творческих сил"},
            {"word": "ЭРУДИЦИЯ", "hint": "Глубокие и обширные познания во многих областях"},
            {"word": "КОМПРОМИСС", "hint": "Соглашение на основе взаимных уступок"},
            {"word": "АБРАКАДАБРА", "hint": "Бессмысленный набор слов или древнее заклинание"},
            {"word": "ПАЛИНДРОМ", "hint": "Слово или фраза, читающаяся одинаково слева направо и справа налево"},
            {"word": "НОСТАЛЬГИЯ", "hint": "Тоска по прошлому или родине"},
            {"word": "ДИЛЕММА", "hint": "Затруднительный выбор между двумя неприятными возможностями"},
            {"word": "ИНТУИЦИЯ", "hint": "Способность понимать что-то без логического анализа, 'шестое чувство'"},
            {"word": "ЗВЕЗДОЧЁТ", "hint": "Старинное название астронома, часто предсказывавшего судьбу"},
            {"word": "ШАРЛАТАН", "hint": "Обманщик, выдающий себя за специалиста"},
            {"word": "КОЛЛЕКЦИЯ", "hint": "Систематизированное собрание однородных предметов"},
            {"word": "МАРМЕЛАД", "hint": "Кондитерское изделие из фруктового пюре и сахара"},
            {"word": "ОРАНЖЕРЕЯ", "hint": "Застеклённое помещение для выращивания теплолюбивых растений"},
            {"word": "ТРОЛЛЕЙБУС", "hint": "Безрельсовый 'рогатый' городской транспорт"},
            {"word": "ДЕГУСТАЦИЯ", "hint": "Проба какого-либо продукта (часто вина или еды) для оценки вкуса"},
            {"word": "БАРАБАН", "hint": "Самый важный предмет в этом телешоу"},
            {"word": "ШАШЛЫК", "hint": "Мясное блюдо, приготовленное на гриле"},
            {"word": "ЛАМПОЧКА", "hint": "Загорается над буквами в студии"},
            {"word": "ВОДКА", "hint": "Крепкий алкогольный напиток"},
            {"word": "ПОДАРОК", "hint": "То, что приносят в студию"},
            {"word": "СУПЕРИГРА", "hint": "Финальный этап 'Поле Чудес'"}
        ]

    def create_alphabet(self):
        for widget in self.letters_frame.winfo_children():
            widget.destroy()

        russian_alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

        letter_count = len(russian_alphabet)

        max_cols = 11

        alphabet_grid = tk.Frame(self.letters_frame, bg=self.current_theme["bg_secondary"])
        alphabet_grid.pack(pady=5)

        self.letter_buttons = {}
        row_count = 0
        col_count = 0

        for letter in russian_alphabet:
            button_frame = tk.Frame(alphabet_grid,
                                   bg=self.current_theme["bg_secondary"],
                                   padx=2, pady=2)
            button_frame.grid(row=row_count, column=col_count, padx=3, pady=3)

            button = tk.Button(button_frame,
                              text=letter,
                              width=3, height=1,
                              bg=self.current_theme["button_bg"],
                              fg="white",
                              font=("Helvetica", 11, "bold"),
                              activebackground=self.current_theme["bg_accent"],
                              activeforeground="white",
                              relief=tk.RAISED,
                              bd=2,
                              command=lambda l=letter: self.guess_letter(l))
            button.pack(padx=1, pady=1)

            self.letter_buttons[letter] = button

            col_count += 1
            if col_count >= max_cols:
                col_count = 0
                row_count += 1

        for i in range(max_cols):
            alphabet_grid.columnconfigure(i, weight=1)
        for i in range(row_count + 1):
            alphabet_grid.rowconfigure(i, weight=1)

    def draw_wheel(self):
        self.wheel_canvas.delete("all")

        center_x = 110
        center_y = 110
        radius = 100

        self.wheel_canvas.create_oval(
            center_x - radius, center_y - radius,
            center_x + radius, center_y + radius,
            fill=self.current_theme["bg_secondary"],
            outline=self.current_theme["fg_main"],
            width=2)

        num_segments = len(self.wheel_segments)
        angle_per_segment = 360 / num_segments

        color_schemes = {
            "number": [(15, 82, 186), (20, 108, 214)],
            "БАНКРОТ": [(186, 15, 42), (214, 20, 35)],
            "ПРИЗ": [(186, 149, 15), (214, 171, 20)],
            "+": [(145, 15, 186), (166, 20, 214)],
            "x2": [(15, 186, 70), (20, 214, 80)],
            "x3": [(15, 186, 130), (20, 214, 150)],
            "ФИГА": [(186, 70, 15), (214, 80, 20)]
        }

        for i, segment in enumerate(self.wheel_segments):
            if isinstance(segment, int):
                segment_type = "number"
            else:
                segment_type = segment

            if segment_type in color_schemes:
                colors = color_schemes[segment_type]
            else:
                colors = color_schemes["number"]

            color_idx = i % 2
            color = colors[color_idx]

            color_hex = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'

            start_angle = self.wheel_angle + i * angle_per_segment
            tk_start_angle = 90 - start_angle

            self.wheel_canvas.create_arc(
                center_x - radius, center_y - radius,
                center_x + radius, center_y + radius,
                start=tk_start_angle, extent=-angle_per_segment,
                fill=color_hex, outline="white", width=1)

        arrow_size = 15
        arrow_points = [
            center_x, center_y - radius - arrow_size,
            center_x - arrow_size, center_y - radius + arrow_size,
            center_x + arrow_size, center_y - radius + arrow_size
        ]

        self.wheel_canvas.create_polygon(
            arrow_points,
            fill=self.current_theme["accent1"],
            outline="white",
            width=2)

        inner_radius = 25
        self.wheel_canvas.create_oval(
            center_x - inner_radius, center_y - inner_radius,
            center_x + inner_radius, center_y + inner_radius,
            fill=self.current_theme["bg_accent"],
            outline="white",
            width=2)

        self.wheel_canvas.create_oval(
            center_x - 3, center_y - 3,
            center_x + 3, center_y + 3,
            fill="white", outline="white")

    def spin_wheel(self):
        if self.is_spinning:
            return

        self.is_spinning = True

        player_name = self.players[self.current_player_idx]["name"]
        message = f"{player_name} вращает барабан..."

        def animate_text(text, index=0):
            if index < len(text):
                self.status_text.config(text=text[:index+1])
                self.root.after(40, animate_text, text, index+1)

        animate_text(message)

        self.spin_button.config(state=tk.DISABLED,
                              bg=self.current_theme["bg_secondary"],
                              fg=self.current_theme["fg_secondary"])
        self.solve_button.config(state=tk.DISABLED,
                               bg=self.current_theme["bg_secondary"],
                               fg=self.current_theme["fg_secondary"])
        self.hint_button.config(state=tk.DISABLED,
                              bg=self.current_theme["bg_secondary"],
                              fg=self.current_theme["fg_secondary"])
        self.gift_button.config(state=tk.DISABLED,
                              bg=self.current_theme["bg_secondary"],
                              fg=self.current_theme["fg_secondary"])

        for button in self.letter_buttons.values():
            if button['state'] == tk.NORMAL:
                button.config(state=tk.DISABLED,
                            bg=self.current_theme["bg_secondary"],
                            fg=self.current_theme["fg_secondary"])

        total_frames = 70 + random.randint(10, 30)
        frames_left = total_frames

        def ease_out_cubic(x):
            return 1 - pow(1 - x, 3)

        final_segment_idx = random.randint(0, len(self.wheel_segments) - 1)
        self.current_wheel_value = self.wheel_segments[final_segment_idx]
        angle_per_segment = 360 / len(self.wheel_segments)

        target_angle = final_segment_idx * angle_per_segment
        target_angle += 360 * 3

        start_angle = self.wheel_angle

        def animate_spin():
            nonlocal frames_left

            if frames_left > 0:
                progress = 1 - frames_left / total_frames

                eased_progress = ease_out_cubic(progress)

                current_angle = start_angle + eased_progress * (target_angle - start_angle)

                self.wheel_angle = current_angle % 360
                self.draw_wheel()

                if frames_left > total_frames * 0.7:
                    shake = 3 if random.random() > 0.5 else -3
                    self.wheel_canvas.place(x=shake, y=shake)
                elif frames_left > total_frames * 0.4:
                    shake = 2 if random.random() > 0.5 else -2
                    self.wheel_canvas.place(x=shake, y=shake)
                elif frames_left > total_frames * 0.1:
                    shake = 1 if random.random() > 0.5 else -1
                    self.wheel_canvas.place(x=shake, y=shake)
                else:
                    self.wheel_canvas.place(x=0, y=0)

                delay = int(50 + eased_progress * 70)
                frames_left -= 1
                self.root.after(delay, animate_spin)
            else:
                self.wheel_canvas.place(x=0, y=0)

                flash_count = 0
                max_flashes = 5

                def flash_result():
                    nonlocal flash_count
                    if flash_count < max_flashes:
                        if flash_count % 2 == 0:
                            color = self.current_theme["accent3"]
                            fg_color = self.current_theme["bg_main"]
                        else:
                            color = self.current_theme["accent1"]
                            fg_color = "white"

                        self.wheel_result_label.config(
                            text="ВЫПАЛО ➤",
                            bg=color,
                            fg=fg_color,
                            font=("Helvetica", 12, "bold"))

                        if isinstance(self.current_wheel_value, str):
                            self.wheel_value_label.config(
                                text=self.current_wheel_value,
                                bg=color,
                                fg=fg_color,
                                font=("Helvetica", 16, "bold"))
                        else:
                            self.wheel_value_label.config(
                                text=f"{self.current_wheel_value} ОЧКОВ",
                                bg=color,
                                fg=fg_color,
                                font=("Helvetica", 16, "bold"))

                        flash_count += 1
                        self.root.after(450, flash_result)
                    else:
                        self.wheel_result_label.config(
                            text="РЕЗУЛЬТАТ ВРАЩЕНИЯ",
                            bg=self.current_theme["bg_accent"],
                            fg=self.current_theme["fg_main"],
                            font=self.score_font)

                        self.wheel_value_label.config(
                            text=str(self.current_wheel_value),
                            bg=self.current_theme["bg_secondary"],
                            fg=self.current_theme["fg_main"],
                            font=self.wheel_font)

                        self.spin_button.config(
                            state=tk.NORMAL,
                            bg=self.current_theme["button_bg"],
                            fg="white")

                        self.solve_button.config(
                            state=tk.NORMAL,
                            bg=self.current_theme["button_bg"],
                            fg="white")

                        self.hint_button.config(
                            state=tk.NORMAL,
                            bg=self.current_theme["bg_accent"],
                            fg="white")

                        self.gift_button.config(
                            state=tk.NORMAL,
                            bg=self.current_theme["bg_accent"],
                            fg="white")

                        for letter, button in self.letter_buttons.items():
                            if letter not in self.used_letters:
                                button.config(
                                    state=tk.NORMAL,
                                    bg=self.current_theme["button_bg"],
                                    fg="white")

                        self.is_spinning = False
                        self.process_wheel_result()

                flash_result()

        animate_spin()

    def process_wheel_result(self):
        wheel_value = self.current_wheel_value
        player_name = self.players[self.current_player_idx]["name"]

        self.wheel_value_label.config(font=(self.wheel_font.cget("family"), self.wheel_font.cget("size"), "bold"))

        if wheel_value == "БАНКРОТ":
            self.wheel_value_label.config(text="БАНКРОТ!", fg="white")
            message = f"О нет! {player_name} теряет все очки!"
            self.status_text.config(text=message)
            self.players[self.current_player_idx]["score"] = 0
            self.players[self.current_player_idx]["multiplier"] = 1
            self.update_player_indicators()
            self.next_player()

        elif wheel_value == "ФИГА":
            self.wheel_value_label.config(text="ФИГА!", fg="white")
            message = f"Ух ты! {player_name} показывает 'фигу' и пропускает ход!"
            self.status_text.config(text=message)
            self.next_player()

        elif wheel_value == "ПРИЗ":
            self.wheel_value_label.config(text="ПРИЗ!", fg="white")
            message = f"{player_name} выпал сектор ПРИЗ!"
            self.status_text.config(text=message)
            self.show_prize_dialog()

        elif wheel_value == "x2":
            self.wheel_value_label.config(text="x2", fg="white")
            message = f"{player_name} получает двойной множитель очков!"
            self.status_text.config(text=message)
            self.players[self.current_player_idx]["multiplier"] = 2
            self.update_player_indicators()
            if not self.players[self.current_player_idx]["is_human"]:
                self.root.after(1500, self.ai_play)

        elif wheel_value == "x3":
            self.wheel_value_label.config(text="x3", fg="white")
            message = f"{player_name} получает тройной множитель очков!"
            self.status_text.config(text=message)
            self.players[self.current_player_idx]["multiplier"] = 3
            self.update_player_indicators()
            if not self.players[self.current_player_idx]["is_human"]:
                self.root.after(1500, self.ai_play)

        elif wheel_value == "+":
            self.wheel_value_label.config(text="ПЛЮС", fg="white")
            message = f"{player_name} получает дополнительный ход!"
            self.status_text.config(text=message)
            if not self.players[self.current_player_idx]["is_human"]:
                self.root.after(1500, self.ai_play)

        else:
            self.wheel_value_label.config(text=str(wheel_value), fg="white")
            message = f"{player_name} выбирает букву (стоимость {wheel_value})"
            self.status_text.config(text=message)

            if not self.players[self.current_player_idx]["is_human"]:
                self.root.after(1500, self.ai_guess_letter)

    def show_prize_dialog(self):
        current_player = self.players[self.current_player_idx]

        if not current_player["is_human"]:
            ai_name = current_player["name"]

            if random.random() < 0.7:
                prize = random.choice(self.prizes)
                bonus = 100

                message = f"{ai_name} выбирает ПРИЗ: {prize} и {bonus} очков!"
                self.status_text.config(text=message)

                current_player["score"] += bonus
                self.update_player_indicators()

                self.next_player()
                return
            else:
                message = f"{ai_name} вращает барабан снова!"
                self.status_text.config(text=message)
                self.root.after(1500, self.ai_play)
                return

        dialog = tk.Toplevel(self.root)
        dialog.title("СЕКТОР ПРИЗ")
        dialog.geometry("400x250")
        dialog.config(bg=self.current_theme["bg_main"])

        header_label = tk.Label(dialog, text="ВЫБЕРИТЕ: ПРИЗ ИЛИ ОЧКИ",
                               font=self.title_font,
                               bg=self.current_theme["bg_main"],
                               fg=self.current_theme["fg_main"])
        header_label.pack(pady=10)

        self.current_money = 100
        money_label = tk.Label(dialog, text=f"ОЧКИ: {self.current_money}",
                              font=self.title_font,
                              bg=self.current_theme["bg_main"],
                              fg=self.current_theme["fg_main"])
        money_label.pack(pady=10)

        self.prize_choices_left = 3
        choices_label = tk.Label(dialog, text=f"ОСТАЛОСЬ ВЫБОРОВ: {self.prize_choices_left}",
                                font=self.score_font,
                                bg=self.current_theme["bg_main"],
                                fg=self.current_theme["fg_main"])
        choices_label.pack(pady=5)

        def choose_money():
            nonlocal money_label, choices_label
            self.prize_choices_left -= 1

            if self.current_money == 100:
                self.current_money = 1000
            elif self.current_money == 1000:
                self.current_money = 5000

            money_label.config(text=f"ОЧКИ: {self.current_money}")
            choices_label.config(text=f"ОСТАЛОСЬ ВЫБОРОВ: {self.prize_choices_left}")

            if self.prize_choices_left == 0:
                messagebox.showinfo("Поздравляем!", f"Вы выиграли {self.current_money} очков!")
                self.players[self.current_player_idx]["score"] += self.current_money
                self.update_player_indicators()
                dialog.destroy()
                self.next_player()

        def choose_prize():
            prize = random.choice(self.prizes)
            messagebox.showinfo("Поздравляем!", f"Вы выиграли: {prize}!\nДополнительно {self.current_money} очков!")

            self.players[self.current_player_idx]["score"] += self.current_money
            self.update_player_indicators()

            dialog.destroy()
            self.next_player()

        button_frame = tk.Frame(dialog, bg=self.current_theme["bg_main"])
        button_frame.pack(pady=15)

        money_button = tk.Button(button_frame, text="ОЧКИ", command=choose_money,
                                font=self.button_font,
                                bg=self.current_theme["button_bg"],
                                fg="white",
                                width=10)
        money_button.grid(row=0, column=0, padx=10)

        prize_button = tk.Button(button_frame, text="ПРИЗ", command=choose_prize,
                                font=self.button_font,
                                bg=self.current_theme["button_bg"],
                                fg="white",
                                width=10)
        prize_button.grid(row=0, column=1, padx=10)

    def show_treasure_box(self):
        """Показывает диалог с шкатулкой за 3 правильные буквы подряд"""
        current_player = self.players[self.current_player_idx]

        if not current_player["is_human"]:
            ai_name = current_player["name"]

            bonus_options = [
                {"name": "Удвоение очков за ход", "value": current_player["score"] * 0.2},
                {"name": "500 дополнительных очков", "value": 500},
                {"name": "Открыть случайную букву", "value": "reveal"}
            ]

            bonus = random.choice(bonus_options)

            if bonus["name"] == "Открыть случайную букву":
                hidden_indices = [i for i, char in enumerate(self.hidden_word) if char == "_"]

                if hidden_indices:
                    random_index = random.choice(hidden_indices)
                    reveal_letter = self.current_word[random_index]

                    self.used_letters.add(reveal_letter)

                    new_hidden_word = list(self.hidden_word)

                    for i, char in enumerate(self.current_word):
                        if char == reveal_letter:
                            new_hidden_word[i] = reveal_letter

                    self.hidden_word = new_hidden_word
                    self.update_word_display()

                    if reveal_letter in self.letter_buttons:
                        self.letter_buttons[reveal_letter].config(
                            state=tk.DISABLED,
                            bg=self.current_theme["bg_secondary"],
                            fg=self.current_theme["fg_secondary"])

                    message = f"{ai_name} открывает шкатулку и находит там букву {reveal_letter}!"
                else:
                    message = f"{ai_name} открывает шкатулку, но не находит полезной буквы!"
            else:
                bonus_value = int(bonus["value"])
                current_player["score"] += bonus_value
                message = f"{ai_name} открывает шкатулку и получает {bonus['name']}!"

            self.status_text.config(text=message)
            self.update_player_indicators()

            if "_" not in self.hidden_word:
                self.word_solved()
                return

            return

        dialog = tk.Toplevel(self.root)
        dialog.title("ШКАТУЛКА")
        dialog.geometry("400x300")
        dialog.config(bg=self.current_theme["bg_main"])

        header_label = tk.Label(dialog, text="ПОЗДРАВЛЯЕМ!",
                               font=self.title_font,
                               bg=self.current_theme["bg_main"],
                               fg=self.current_theme["fg_main"])
        header_label.pack(pady=10)

        info_label = tk.Label(dialog,
                             text="Вы угадали 3 буквы подряд и получаете шкатулку!",
                             font=self.score_font,
                             bg=self.current_theme["bg_main"],
                             fg=self.current_theme["fg_main"],
                             wraplength=350)
        info_label.pack(pady=10)

        box_image = tk.Label(dialog, text="[ШКАТУЛКА]",
                           font=self.title_font,
                           bg=self.current_theme["accent3"],
                           fg="black",
                           width=15, height=2)
        box_image.pack(pady=15)

        options_frame = tk.Frame(dialog, bg=self.current_theme["bg_main"])
        options_frame.pack(pady=10)

        def choose_double_points():
            current_points = self.players[self.current_player_idx]["score"]
            bonus = int(current_points * 0.5)
            self.players[self.current_player_idx]["score"] += bonus
            self.update_player_indicators()
            messagebox.showinfo("Бонус", f"Вы получили дополнительно {bonus} очков!")
            dialog.destroy()

            if "_" not in self.hidden_word:
                self.word_solved()

        def choose_reveal_letter():
            hidden_indices = [i for i, char in enumerate(self.hidden_word) if char == "_"]

            if not hidden_indices:
                messagebox.showinfo("Шкатулка", "Все буквы уже открыты!")
                dialog.destroy()
                return

            random_index = random.choice(hidden_indices)
            reveal_letter = self.current_word[random_index]

            self.used_letters.add(reveal_letter)

            new_hidden_word = list(self.hidden_word)

            for i, char in enumerate(self.current_word):
                if char == reveal_letter:
                    new_hidden_word[i] = reveal_letter

            self.hidden_word = new_hidden_word
            self.update_word_display()

            if reveal_letter in self.letter_buttons:
                self.letter_buttons[reveal_letter].config(
                    state=tk.DISABLED,
                    bg=self.current_theme["bg_secondary"],
                    fg=self.current_theme["fg_secondary"])

            messagebox.showinfo("Шкатулка", f"Открыта буква: {reveal_letter}")
            dialog.destroy()

            if "_" not in self.hidden_word:
                self.word_solved()

        def choose_extra_turn():
            messagebox.showinfo("Бонус", "Вы получаете дополнительный ход!")
            dialog.destroy()

        option1 = tk.Button(options_frame, text="50% БОНУС К ОЧКАМ",
                          command=choose_double_points,
                          font=self.button_font,
                          bg=self.current_theme["button_bg"],
                          fg="white",
                          width=20)
        option1.pack(pady=5)

        option2 = tk.Button(options_frame, text="ОТКРЫТЬ СЛУЧАЙНУЮ БУКВУ",
                          command=choose_reveal_letter,
                          font=self.button_font,
                          bg=self.current_theme["button_bg"],
                          fg="white",
                          width=20)
        option2.pack(pady=5)

        option3 = tk.Button(options_frame, text="ДОПОЛНИТЕЛЬНЫЙ ХОД",
                          command=choose_extra_turn,
                          font=self.button_font,
                          bg=self.current_theme["button_bg"],
                          fg="white",
                          width=20)
        option3.pack(pady=5)

    def guess_letter(self, letter):
        if letter in self.used_letters:
            return

        self.used_letters.add(letter)

        if letter in self.letter_buttons:
            self.letter_buttons[letter].config(state=tk.DISABLED,
                                            bg=self.current_theme["bg_secondary"],
                                            fg=self.current_theme["fg_secondary"])

        current_player = self.players[self.current_player_idx]

        if letter in self.current_word:
            letter_found = 0
            new_hidden_word = list(self.hidden_word)
            for i, char in enumerate(self.current_word):
                if char == letter:
                    new_hidden_word[i] = letter
                    letter_found += 1
            self.hidden_word = new_hidden_word

            self.update_word_display()

            points_earned = 0
            if isinstance(self.current_wheel_value, int):
                points_earned = letter_found * self.current_wheel_value * current_player["multiplier"]
                current_player["score"] += points_earned

            current_player["consecutive_correct"] += 1

            if current_player["consecutive_correct"] >= 3:
                current_player["consecutive_correct"] = 0
                self.update_player_indicators()

                self.root.after(1000, self.show_treasure_box)
                return

            self.update_player_indicators()

            player_name = current_player["name"]
            points_text = f"+{points_earned} очков" if points_earned > 0 else ""
            message = f"{player_name} угадал букву {letter}! {points_text}"
            self.status_text.config(text=message.strip())

            if "_" not in self.hidden_word:
                self.word_solved()
                return
            elif not current_player["is_human"]:
                self.root.after(1500, self.ai_play)

        else:
            current_player["consecutive_correct"] = 0
            self.update_player_indicators()

            player_name = current_player["name"]

            wrong_phrase = random.choice(self.wrong_letter_phrases)
            message = f"{player_name}: буква '{letter}'. {wrong_phrase}"
            self.status_text.config(text=message)

            self.next_player()

    def solve_attempt(self):
        if not self.players[self.current_player_idx]["is_human"]:
            return

        solution = simpledialog.askstring("Отгадать слово", "Введите отгадку:")

        if not solution:
            return

        solution = solution.upper()

        if solution == self.current_word:
            self.hidden_word = list(self.current_word)
            self.update_word_display()

            hidden_count = self.hidden_word.count("_")
            bonus_points = hidden_count * 100
            self.players[self.current_player_idx]["score"] += bonus_points

            messagebox.showinfo("Поздравляем!", f"Вы правильно отгадали слово!\nБонус: {bonus_points} очков")

            self.word_solved()
        else:
            messagebox.showinfo("Неверно", "К сожалению, это не правильный ответ.")
            self.next_player()

    def word_solved(self):
        self.hidden_word = list(self.current_word)
        self.update_word_display()

        player_name = self.players[self.current_player_idx]["name"]
        message = f"Слово отгадано! {player_name} получает дополнительные очки!"
        self.status_text.config(text=message)

        self.root.after(2000, self.next_round)

    def next_round(self):
        max_rounds = self.rounds_var.get()

        if self.game_round < max_rounds:
            self.game_round += 1
            self.round_label.config(text=f"Раунд: {self.game_round}")

            self.current_player_idx = (self.current_player_idx + 1) % len(self.players)

            self.select_word()

            self.used_letters = set()

            for player in self.players:
                player["multiplier"] = 1
                player["consecutive_correct"] = 0

            self.update_player_indicators()
            self.update_word_display()

            self.create_alphabet()

            message = f"Начинается раунд {self.game_round}! Первым играет {self.players[self.current_player_idx]['name']}."
            self.status_text.config(text=message)

            if not self.players[self.current_player_idx]["is_human"]:
                self.root.after(1500, self.ai_play)
        else:
            self.game_over()

    def game_over(self):
        winner = max(self.players, key=lambda p: p["score"])

        messagebox.showinfo("Игра окончена",
                           f"Игра завершена!\n\nПобедитель: {winner['name']}\nСчет: {winner['score']} очков")

        if messagebox.askyesno("Новая игра", "Хотите начать новую игру?"):
            self.new_game()

    def next_player(self):
        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)
        self.update_player_indicators()

        if not self.players[self.current_player_idx]["is_human"]:
            self.root.after(3000, self.ai_play)

    def ai_play(self):
        self.root.after(2000, self.spin_wheel)

    def ai_guess_letter(self):
        ai_player = self.players[self.current_player_idx]
        ai_name = ai_player["name"]

        russian_alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        unused_letters = [letter for letter in russian_alphabet if letter not in self.used_letters]

        if not unused_letters:
            message = f"{ai_name} пропускает ход - все буквы уже названы."
            self.status_text.config(text=message)
            self.next_player()
            return

        if ai_name == "ИИ 1":
            letter_frequency = "ОЕАИНТСРВЛКМДПУЯЫЬГЗБЧЙХЖШЮЦЩЭФЪЁ"
            for letter in letter_frequency:
                if letter in unused_letters:
                    chosen_letter = letter
                    break
            else:
                chosen_letter = random.choice(unused_letters)

        else: # ИИ 2
            consonants = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
            unused_consonants = [letter for letter in consonants if letter in unused_letters]
            if unused_consonants:
                chosen_letter = random.choice(unused_consonants)
            else:
                chosen_letter = random.choice(unused_letters)

        message = f"{ai_name} выбирает букву: {chosen_letter}"
        self.status_text.config(text=message)

        self.root.after(2500, lambda: self.guess_letter(chosen_letter))

    def select_word(self):
        if not self.word_bank:
            messagebox.showerror("Ошибка", "Банк слов пуст!")
            return

        self.current_word_data = random.choice(self.word_bank)
        self.current_word = self.current_word_data["word"]

        self.hidden_word = ["_"] * len(self.current_word)

        self.hint_text.config(text=self.current_word_data["hint"])

    def new_game(self):
        self.game_round = 1
        self.round_label.config(text=f"Раунд: {self.game_round}")

        for player in self.players:
            player["score"] = 0
            player["multiplier"] = 1
            player["consecutive_correct"] = 0

        self.current_player_idx = 0

        self.select_word()

        self.used_letters = set()

        self.update_player_indicators()
        self.update_word_display()
        self.create_alphabet()

        welcome_message = "Добро пожаловать в игру ПОЛЕ ЧУДЕС! Отгадайте загаданное слово, вращая барабан и называя буквы."
        self.status_text.config(text=welcome_message)

    def update_word_display(self):
        for widget in self.word_frame.winfo_children():
            widget.destroy()

        for char in self.hidden_word:
            if char == "_":
                cell_bg = "#1E2130"
                cell_fg = "#555555"
                cell_text = "_"
                cell_relief = tk.GROOVE
            else:
                cell_bg = "#3A7734"
                cell_fg = "#FFFFFF"
                cell_text = char
                cell_relief = tk.RAISED

            char_frame = tk.Frame(self.word_frame, bg="#333333", bd=2,
                                 relief=tk.SUNKEN, width=40, height=50,
                                 highlightbackground="#444", highlightthickness=1)
            char_frame.pack_propagate(False)
            char_frame.pack(side=tk.LEFT, padx=3, pady=5)

            inner_frame = tk.Frame(char_frame, bg=cell_bg, bd=1,
                                  relief=cell_relief, width=36, height=46)
            inner_frame.pack_propagate(False)
            inner_frame.pack(padx=1, pady=1, fill=tk.BOTH, expand=True)

            char_label = tk.Label(inner_frame, text=cell_text,
                                 font=self.word_font, bg=cell_bg, fg=cell_fg)
            char_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def update_player_indicators(self):
        for i, player_labels in enumerate(self.player_labels):
            if i == self.current_player_idx:
                player_labels["active"].pack()
                player_labels["name"].config(fg="white", font=(self.score_font.cget("family"), self.score_font.cget("size"), "bold"))
            else:
                player_labels["active"].pack_forget()
                player_labels["name"].config(fg="grey", font=self.score_font)
                player_labels["score"].config(fg="grey")
                player_labels["multiplier"].config(fg="grey")
                player_labels["consecutive"].config(fg="grey")

            score_color = "white" if i == self.current_player_idx else "grey"
            player_labels["score"].config(text=f"Счет: {self.players[i]['score']}", fg=score_color)
            player_labels["multiplier"].config(text=f"Множитель: x{self.players[i]['multiplier']}", fg=score_color)
            player_labels["consecutive"].config(text=f"Подряд: {self.players[i]['consecutive_correct']}/3", fg=score_color)

    def update_stats_display(self):
        for item in self.stats_tree.get_children():
            self.stats_tree.delete(item)

        saved_games = []
        if os.path.exists(self.game_data.save_file):
            try:
                with open(self.game_data.save_file, "r", encoding="utf-8") as file:
                    saved_games = json.load(file)
            except:
                pass

        for i, game in enumerate(saved_games):
            timestamp = game.get("timestamp", "Неизвестно")
            current_round = game.get("current_round", 0)

            players = game.get("players", [])
            leader_name = "Нет данных"
            leader_score = 0

            if players:
                leader = max(players, key=lambda p: p.get("score", 0))
                leader_name = leader.get("name", "Неизвестно")
                leader_score = leader.get("score", 0)

            self.stats_tree.insert("", "end", values=(timestamp, current_round, leader_name, leader_score))

    def save_current_game(self):
        success = self.game_data.save_game_state(self.players, self.game_round, self.current_player_idx)
        if success:
            messagebox.showinfo("Сохранение", "Игра успешно сохранена!")
            self.update_stats_display()
        else:
            messagebox.showerror("Ошибка", "Не удалось сохранить игру.")

    def change_theme(self):
        theme = self.theme_var.get()
        if theme == "dark":
            self.current_theme["bg_main"] = "#1A1A2E"
            self.current_theme["fg_main"] = "#E2E2E2"
        else:
            self.current_theme["bg_main"] = "#FFFFFF"
            self.current_theme["fg_main"] = "#000000"

        for frame in [self.game_frame, self.stats_frame, self.settings_frame, self.help_frame]:
            frame.config(bg=self.current_theme["bg_main"])

        messagebox.showinfo("Тема", "Для полного изменения темы требуется перезапуск игры.")

    def change_font_size(self, size):
        size = int(float(size))

        self.score_font.configure(size=size)
        self.button_font.configure(size=size)

        messagebox.showinfo("Шрифт", "Для полного изменения размера шрифта требуется перезапуск игры.")

    def reset_settings(self):
        self.theme_var.set("dark")
        self.font_scale.set(12)
        self.rounds_var.set(3)

        messagebox.showinfo("Настройки", "Настройки сброшены к значениям по умолчанию.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PoleChudes(root)
    root.mainloop()
