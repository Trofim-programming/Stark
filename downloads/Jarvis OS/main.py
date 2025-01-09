import tkinter as tkfrom tkinter import filedialog, messagebox, simpledialogimport osimport subprocessimport webbrowserimport sqlite3from PIL import Image, ImageDrawimport ioclass MegaOS:    def __init__(self, root):        self.root = root        self.root.title("MegaOS - Рабочий стол для программиста")        self.root.geometry("1200x800")                # Рабочий стол        self.desktop_frame = tk.Frame(self.root, bg="black", width=1200, height=750)        self.desktop_frame.pack(fill="both", expand=True)        self.files_on_desktop = []  # Список файлов на рабочем столе        # Панель в стиле дока        self.dock_frame = tk.Frame(self.root, bg="gray", height=50)        self.dock_frame.pack(fill="x", side="bottom")        self.create_desktop()  # Создание рабочего стола        self.create_dock()     # Создание док-панели    def create_desktop(self):        # Обои рабочего стола чёрного цвета        self.desktop_frame.config(bg="black")        # Пример файлов на рабочем столе (метки, которые можно перетаскивать)        self.create_file_icon("Файл 1", 100, 100)        self.create_file_icon("Файл 2", 100, 200)        self.create_file_icon("Файл 3", 100, 300)    def create_file_icon(self, name, x, y):        # Создание иконки файла        file_icon = tk.Label(self.desktop_frame, text=name, bg="gray", fg="white", width=10, height=2)        file_icon.place(x=x, y=y)        file_icon.bind("<Button-1>", self.on_file_click)        file_icon.bind("<B1-Motion>", self.on_file_drag)        self.files_on_desktop.append(file_icon)    def on_file_click(self, event):        # При клике на файл, выбираем его для перетаскивания        self.selected_file = event.widget        self.dragging = False    def on_file_drag(self, event):        # Перетаскивание файла        if self.selected_file:            self.dragging = True            self.selected_file.place(x=event.x - 50, y=event.y - 25)    def create_dock(self):        # Кнопки для всех программ на док-панели        programs = [            ("Терминал", self.open_terminal),            ("IDE", self.open_ide),            ("Файловый менеджер", self.open_file_manager),            ("Браузер", self.open_browser),            ("Магазин приложений", self.open_app_store),            ("Мониторинг", self.open_process_monitoring),            ("Git", self.open_git_interface),            ("Базы данных", self.open_db_interface),            ("Граф. редактор", self.open_graphic_editor),        ]        for name, command in programs:            button = tk.Button(self.dock_frame, text=name, command=command, width=12, height=2)            button.pack(side="left", padx=5, pady=5)    def open_terminal(self):        terminal_window = tk.Toplevel(self.root)        terminal_window.title("Командная строка")        terminal_window.geometry("800x600")                terminal_text = tk.Text(terminal_window, height=30, width=100)        terminal_text.pack()        def execute_command():            command = terminal_input.get()            result = subprocess.run(command, shell=True, capture_output=True, text=True)            terminal_text.insert(tk.END, result.stdout + "\n")            terminal_text.insert(tk.END, result.stderr + "\n")        terminal_input = tk.Entry(terminal_window, width=100)        terminal_input.pack()        terminal_input.bind("<Return>", lambda event: execute_command())    def open_ide(self):        ide_window = tk.Toplevel(self.root)        ide_window.title("Среда разработки (IDE)")        ide_window.geometry("800x600")                text_area = tk.Text(ide_window, wrap=tk.WORD)        text_area.pack(fill=tk.BOTH, expand=True)        def run_code():            code = text_area.get("1.0", tk.END)            try:                exec(code)            except Exception as e:                messagebox.showerror("Ошибка выполнения", str(e))        run_button = tk.Button(ide_window, text="Запустить код", command=run_code)        run_button.pack(pady=10)    def open_file_manager(self):        file_manager_window = tk.Toplevel(self.root)        file_manager_window.title("Файловый менеджер")        file_manager_window.geometry("800x600")        file_listbox = tk.Listbox(file_manager_window, width=80, height=20)        file_listbox.pack()        def open_directory():            path = filedialog.askdirectory()            if path:                file_listbox.delete(0, tk.END)                for filename in os.listdir(path):                    file_listbox.insert(tk.END, filename)        open_button = tk.Button(file_manager_window, text="Открыть каталог", command=open_directory)        open_button.pack(pady=10)    def open_browser(self):        url = simpledialog.askstring("Введите URL", "Введите URL для открытия:")        if url:            webbrowser.open(url)    def open_app_store(self):        app_store_window = tk.Toplevel(self.root)        app_store_window.title("Магазин приложений")        app_store_window.geometry("600x400")        install_button_1 = tk.Button(app_store_window, text="Установить IDE", command=self.install_ide)        install_button_1.pack(pady=20)        install_button_2 = tk.Button(app_store_window, text="Установить Браузер", command=self.install_browser)        install_button_2.pack(pady=20)    def install_ide(self):        messagebox.showinfo("Установка", "IDE успешно установлено!")    def install_browser(self):        messagebox.showinfo("Установка", "Браузер успешно установлен!")    def open_process_monitoring(self):        monitoring_window = tk.Toplevel(self.root)        monitoring_window.title("Мониторинг процессов")        monitoring_window.geometry("800x600")        process_listbox = tk.Listbox(monitoring_window, width=80, height=20)        process_listbox.pack()        def refresh_processes():            process_listbox.delete(0, tk.END)            processes = os.popen('ps aux').readlines()            for process in processes:                process_listbox.insert(tk.END, process)        refresh_button = tk.Button(monitoring_window, text="Обновить процессы", command=refresh_processes)        refresh_button.pack(pady=10)    def open_git_interface(self):        git_window = tk.Toplevel(self.root)        git_window.title("Работа с Git")        git_window.geometry("800x600")        git_text = tk.Text(git_window, height=30, width=100)        git_text.pack()        def execute_git_command():            command = git_input.get()            result = subprocess.run(command, shell=True, capture_output=True, text=True)            git_text.insert(tk.END, result.stdout + "\n")            git_text.insert(tk.END, result.stderr + "\n")        git_input = tk.Entry(git_window, width=100)        git_input.pack()        git_input.bind("<Return>", lambda event: execute_git_command())    def open_db_interface(self):        db_window = tk.Toplevel(self.root)        db_window.title("Работа с базами данных")        db_window.geometry("800x600")        db_text = tk.Text(db_window, height=30, width=100)        db_text.pack()        def open_db():            db_file = filedialog.askopenfilename(title="Выберите базу данных", filetypes=(("SQLite files", "*.db"),))            if db_file:                conn = sqlite3.connect(db_file)                cursor = conn.cursor()                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")                tables = cursor.fetchall()                db_text.insert(tk.END, f"Таблицы в базе данных: {tables}\n")                conn.close()        open_db_button = tk.Button(db_window, text="Открыть базу данных", command=open_db)        open_db_button.pack(pady=10)    def open_graphic_editor(self):        editor_window = tk.Toplevel(self.root)        editor_window.title("Графический редактор")        editor_window.geometry("800x600")        canvas = tk.Canvas(editor_window, bg="white", width=700, height=500)        canvas.pack(pady=10)        self.last_x, self.last_y = None, None        self.pen_color = "black"        def set_color(color):            self.pen_color = color        def start_draw(event):            self.last_x, self.last_y = event.x, event.y        def draw(event):            if self.last_x and self.last_y:                canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill=self.pen_color, width=2)            self.last_x, self.last_y = event.x, event.y        def clear_canvas():            canvas.delete("all")        def save_drawing():            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG файлы", "*.png"), ("Все файлы", "*.*")])            if file_path:                ps = canvas.postscript(colormode="color")                img = Image.open(io.BytesIO(ps.encode('utf-8')))                img.save(file_path)                messagebox.showinfo("Сохранено", "Рисунок успешно сохранён!")        control_frame = tk.Frame(editor_window)        control_frame.pack(pady=10)        colors = ["black", "red", "green", "blue", "yellow", "purple", "orange", "brown"]        for color in colors:            color_button = tk.Button(control_frame, bg=color, width=2, command=lambda c=color: set_color(c))            color_button.pack(side="left", padx=5)        clear_button = tk.Button(editor_window, text="Очистить", command=clear_canvas)        clear_button.pack(side="left", padx=10)        save_button = tk.Button(editor_window, text="Сохранить", command=save_drawing)        save_button.pack(side="left", padx=10)        canvas.bind("<Button-1>", start_draw)        canvas.bind("<B1-Motion>", draw)if __name__ == "__main__":    root = tk.Tk()    megaos = MegaOS(root)    root.mainloop()