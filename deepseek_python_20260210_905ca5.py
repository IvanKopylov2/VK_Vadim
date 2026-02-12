from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageOps
import os

root = Tk()
root.title("ВКонтакте")
root.geometry("1100x650")
root.configure(bg="#f0f0f0")

# ========================= АВТО-ОПРЕДЕЛЕНИЕ ПУТИ =========================

# Используем текущую рабочую директорию вместо __file__
BASE_DIR = os.getcwd()  # Получаем текущую рабочую директорию

bed_path = os.path.join(BASE_DIR, "bedhead.png")
hul_path = os.path.join(BASE_DIR, "huligan.png")
logo_path = os.path.join(BASE_DIR, "logo.png")  # Путь к логотипу
avatar_path = os.path.join(BASE_DIR, "avatar.png")  # Путь к аватарке
bell_path = os.path.join(BASE_DIR, "bell.png")  # Путь к иконке колокольчика

# Пути к иконкам для вкладок
profile_icon_path = os.path.join(BASE_DIR, "profile_icon.png")
feed_icon_path = os.path.join(BASE_DIR, "feed_icon.png")
friends_icon_path = os.path.join(BASE_DIR, "friends_icon.png")
messenger_icon_path = os.path.join(BASE_DIR, "messenger_icon.png")

# Проверяем существование файлов
print(f"Текущая директория: {BASE_DIR}")
print(f"Файл bedhead.png существует: {os.path.exists(bed_path)}")
print(f"Файл huligan.png существует: {os.path.exists(hul_path)}")
print(f"Файл logo.png существует: {os.path.exists(logo_path)}")
print(f"Файл avatar.png существует: {os.path.exists(avatar_path)}")
print(f"Файл bell.png существует: {os.path.exists(bell_path)}")
print(f"Файл profile_icon.png существует: {os.path.exists(profile_icon_path)}")
print(f"Файл feed_icon.png существует: {os.path.exists(feed_icon_path)}")
print(f"Файл friends_icon.png существует: {os.path.exists(friends_icon_path)}")
print(f"Файл messenger_icon.png существует: {os.path.exists(messenger_icon_path)}")

# ========================= ФУНКЦИИ =========================

def make_circle_avatar(image_path, size):
    """Создает круглую аватарку из изображения"""
    try:
        # Открываем изображение
        img = Image.open(image_path)
        
        # Масштабируем до квадрата
        img = img.resize((size, size), Image.Resampling.LANCZOS)
        
        # Создаем маску для круглой обрезки
        mask = Image.new('L', (size, size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size, size), fill=255)
        
        # Применяем маску
        output = ImageOps.fit(img, (size, size))
        output.putalpha(mask)
        
        # Конвертируем в формат для tkinter
        return ImageTk.PhotoImage(output)
    except Exception as e:
        print(f"Ошибка создания круглой аватарки: {e}")
        # Создаем простую круглую аватарку с цветом
        img = Image.new('RGBA', (size, size), (100, 100, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.ellipse((0, 0, size, size), fill=(100, 100, 255))
        return ImageTk.PhotoImage(img)

def load_bell_icon(size=30):
    """Загружает или создает иконку колокольчика"""
    try:
        # Пробуем загрузить из файла
        if os.path.exists(bell_path):
            bell_img_raw = Image.open(bell_path)
            # Преобразуем в RGBA если нужно
            if bell_img_raw.mode != 'RGBA':
                bell_img_raw = bell_img_raw.convert('RGBA')
            
            # Масштабируем
            bell_img_raw = bell_img_raw.resize((size, size), Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(bell_img_raw)
        else:
            # Создаем иконку программно
            img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)
            
            # Рисуем простой колокольчик
            # Основная часть
            bell_points = [
                (size*0.3, size*0.2),
                (size*0.7, size*0.2),
                (size*0.75, size*0.5),
                (size*0.7, size*0.6),
                (size*0.3, size*0.6),
                (size*0.25, size*0.5)
            ]
            
            # Заливаем
            draw.polygon(bell_points, fill=(150, 150, 150, 255))
            
            # Язычок
            draw.ellipse([size*0.45, size*0.65, size*0.55, size*0.75], 
                        fill=(220, 100, 100, 255))
            
            # Красная точка для уведомлений
            draw.ellipse([size*0.65, size*0.15, size*0.8, size*0.3], 
                        fill=(255, 50, 50, 255))
            
            return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Ошибка создания иконки колокольчика: {e}")
        return None

def create_tab_icon(icon_path, icon_name, size=20):
    """Создает иконку для вкладки"""
    try:
        # Пробуем загрузить из файла
        if os.path.exists(icon_path):
            icon_img_raw = Image.open(icon_path)
            # Преобразуем в RGBA если нужно
            if icon_img_raw.mode != 'RGBA':
                icon_img_raw = icon_img_raw.convert('RGBA')
            
            # Масштабируем
            icon_img_raw = icon_img_raw.resize((size, size), Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(icon_img_raw)
        else:
            # Создаем простую иконку программно
            img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)
            
            # Создаем иконку в зависимости от названия
            if "profile" in icon_name.lower():
                # Иконка профиля - человек
                draw.ellipse([size*0.2, size*0.1, size*0.8, size*0.5], 
                           fill=(70, 130, 180, 255))  # Голова
                draw.rectangle([size*0.35, size*0.5, size*0.65, size*0.85], 
                              fill=(70, 130, 180, 255))  # Тело
            elif "feed" in icon_name.lower():
                # Иконка ленты - квадрат с линиями
                draw.rectangle([size*0.15, size*0.15, size*0.85, size*0.85], 
                              fill=(60, 179, 113, 255))
                # Линии как текст
                draw.line([size*0.25, size*0.35, size*0.75, size*0.35], 
                         fill=(255, 255, 255, 255), width=2)
                draw.line([size*0.25, size*0.5, size*0.6, size*0.5], 
                         fill=(255, 255, 255, 255), width=2)
                draw.line([size*0.25, size*0.65, size*0.55, size*0.65], 
                         fill=(255, 255, 255, 255), width=2)
            elif "friend" in icon_name.lower():
                # Иконка друзей - два человека
                # Первый человек
                draw.ellipse([size*0.1, size*0.2, size*0.4, size*0.6], 
                           fill=(255, 140, 0, 255))
                draw.rectangle([size*0.2, size*0.6, size*0.3, size*0.85], 
                              fill=(255, 140, 0, 255))
                # Второй человек
                draw.ellipse([size*0.6, size*0.2, size*0.9, size*0.6], 
                           fill=(255, 140, 0, 255))
                draw.rectangle([size*0.7, size*0.6, size*0.8, size*0.85], 
                              fill=(255, 140, 0, 255))
                # Соединяющая линия
                draw.line([size*0.4, size*0.4, size*0.6, size*0.4], 
                         fill=(255, 140, 0, 255), width=2)
            elif "messenger" in icon_name.lower():
                # Иконка мессенджера - облачко
                draw.ellipse([size*0.2, size*0.2, size*0.8, size*0.8], 
                           fill=(138, 43, 226, 255))
                # Текст сообщения
                draw.line([size*0.35, size*0.4, size*0.65, size*0.4], 
                         fill=(255, 255, 255, 255), width=2)
                draw.line([size*0.35, size*0.55, size*0.5, size*0.55], 
                         fill=(255, 255, 255, 255), width=2)
            else:
                # Простой кружок по умолчанию
                draw.ellipse([size*0.2, size*0.2, size*0.8, size*0.8], 
                           fill=(100, 100, 100, 255))
            
            return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Ошибка создания иконки {icon_name}: {e}")
        # Создаем простую иконку-кружок
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.ellipse([size*0.2, size*0.2, size*0.8, size*0.8], 
                    fill=(150, 150, 150, 255))
        return ImageTk.PhotoImage(img)

# ========================= ПРОСТАЯ ВЕРХНЯЯ ПАНЕЛЬ =========================

header = Frame(root, bg="#eafff0", height=60)
header.pack(fill="x", side="top")
header.pack_propagate(False)

# ---- ЛЕВАЯ ЧАСТЬ: ЛОГОТИП (теперь картинка) ----
left = Frame(header, bg="#eafff0")
left.pack(side="left", padx=20)

# Пробуем загрузить логотип
logo_img = None
try:
    if os.path.exists(logo_path):
        logo_img_raw = Image.open(logo_path)
        # Автоматически подбираем размер - можно настроить
        logo_width = 250
        logo_height = int(logo_img_raw.height * (logo_width / logo_img_raw.width))
        logo_img_raw = logo_img_raw.resize((logo_width, logo_height))
        logo_img = ImageTk.PhotoImage(logo_img_raw)
        
        # Создаем Label с изображением вместо текста
        logo_label = Label(left, image=logo_img, bg="#eafff0")
        logo_label.pack()
    else:
        print(f"Файл логотипа не найден: {logo_path}")
        # Показываем текст как запасной вариант
        Label(left, text="вконтакте",
              font=("Arial", 18, "bold"),
              bg="#eafff0", fg="#000000").pack()
except Exception as e:
    print(f"Ошибка загрузки логотипа: {e}")
    # Запасной вариант - текст
    Label(left, text="вконтакте",
          font=("Arial", 18, "bold"),
          bg="#eafff0", fg="#000000").pack()

# ---- ЦЕНТР: ПОИСК ----
center_top = Frame(header, bg="#eafff0")
center_top.pack(side="left", expand=True)

search_frame = Frame(center_top, bg="#f2f3f5", bd=0)
search_frame.pack(fill="x", padx=100)

search_field = Entry(search_frame,
                     font=("Arial", 14),
                     bg="#f2f3f5",
                     fg="#000000",
                     bd=0,
                     relief="flat")
search_field.insert(0, "Поиск")
search_field.pack(ipady=6, fill="x")

# ---- ПРАВАЯ ЧАСТЬ: Профиль и уведомления ----
right = Frame(header, bg="#eafff0")
right.pack(side="right", padx=20)

# Грузим изображения
avatar_img = make_circle_avatar(avatar_path if os.path.exists(avatar_path) else None, 40)
bell_img = load_bell_icon(30)

# Контейнер для правой части
right_container = Frame(right, bg="#eafff0")
right_container.pack(side="right")

# 1. КОЛОКОЛЬЧИК (САМЫЙ ПРАВЫЙ ЭЛЕМЕНТ) - Просто Label, а не кнопка
if bell_img:
    bell_label = Label(right_container, 
                      image=bell_img,
                      bg="#eafff0")
    bell_label.pack(side="right", padx=(10, 0))
else:
    # Запасной вариант
    bell_label = Label(right_container, 
                      text="🔔",
                      font=("Arial", 16),
                      bg="#eafff0",
                      fg="#666666")
    bell_label.pack(side="right", padx=(10, 0))

# 2. АВАТАРКА (слева от колокольчика) - Просто Label
if avatar_img:
    avatar_label = Label(right_container, image=avatar_img, bg="#eafff0")
    avatar_label.pack(side="right", padx=(10, 10))
else:
    # Запасной вариант для аватарки
    avatar_label = Label(right_container, text="👤", 
                        font=("Arial", 20),
                        bg="#eafff0")
    avatar_label.pack(side="right", padx=(10, 10))

# 3. ТЕКСТ "ПРОФИЛЬ" (самый левый элемент в контейнере) - Просто Label
profile_label = Label(right_container, text="Профиль",
                     font=("Arial", 14),
                     bg="#eafff0", fg="#000000")
profile_label.pack(side="right", padx=(0, 10))

# ========================= ОСНОВНАЯ ОБЛАСТЬ =========================

main = Frame(root, bg="#ffffff")
main.pack(fill="both", expand=True)

# ========================= ЛЕВАЯ ПАНЕЛЬ =========================

nav_frame = Frame(main, bg="#eeeeee", width=200)
nav_frame.pack(side="left", fill="y")
nav_frame.pack_propagate(False)

# Создаем иконки для вкладок
tab_items = [
    ("ПРОФИЛЬ", "profile_icon.png", "profile"),
    ("ЛЕНТА", "feed_icon.png", "feed"),
    ("ДРУЗЬЯ", "friends_icon.png", "friends"),
    ("МЕССЕНДЖЕР", "messenger_icon.png", "messenger")
]

# Сохраняем иконки в списке
tab_icons = []

for item_text, icon_file, icon_name in tab_items:
    # Создаем фрейм для каждой вкладки
    tab_frame = Frame(nav_frame, bg="#eeeeee")
    tab_frame.pack(fill="x", padx=5, pady=5)
    
    # Создаем иконку
    icon_path = os.path.join(BASE_DIR, icon_file)
    icon_img = create_tab_icon(icon_path, icon_name, 20)
    
    # Сохраняем ссылку на иконку
    if icon_img:
        tab_icons.append(icon_img)
    
    # Добавляем иконку слева
    if icon_img:
        icon_label = Label(tab_frame, image=icon_img, bg="#eeeeee")
        icon_label.pack(side="left", padx=(15, 10))
    else:
        # Запасной вариант - маленький кружок
        icon_label = Label(tab_frame, text="●", 
                          font=("Arial", 10),
                          bg="#eeeeee", fg="#666666")
        icon_label.pack(side="left", padx=(15, 10))
    
    # Добавляем текст вкладки
    text_label = Label(tab_frame, text=item_text, font=("Arial", 11),
                      bg="#eeeeee", fg="#000000",
                      anchor="w")
    text_label.pack(side="left", fill="x", expand=True)
    
    # Добавляем отступ снизу между вкладками
    Label(nav_frame, bg="#eeeeee", height=1).pack()

# ========================= ЦЕНТР =========================

center = Frame(main, bg="#ffffff")
center.pack(side="left", fill="both", expand=True, padx=20, pady=20)

header_feed = Frame(center, bg="#306eff", height=45)
header_feed.pack(fill="x")
header_feed.pack_propagate(False)

Label(header_feed, text="ЛЕНТА НОВОСТЕЙ",
      font=("Arial", 16, "bold"),
      bg="#306eff", fg="#ffffff").pack(expand=True)

white_box = Frame(center, bg="white", highlightbackground="#dddddd", highlightthickness=1)
white_box.pack(fill="both", expand=True, pady=10)

# ========================= ПРАВАЯ КОЛОНКА (РЕКЛАМА) =========================

right_ads = Frame(main, bg="#f0f0f0", width=260)
right_ads.pack(side="right", fill="y")
right_ads.pack_propagate(False)

# === Загружаем изображения рекламы ===
bed_img = None
hul_img = None

try:
    if os.path.exists(bed_path):
        bed_img_raw = Image.open(bed_path).resize((240, 300))
        bed_img = ImageTk.PhotoImage(bed_img_raw)
    else:
        print(f"Файл bedhead.png не найден")
        bed_img = None
except Exception as e:
    print(f"Ошибка загрузки bedhead.png: {e}")
    bed_img = None

try:
    if os.path.exists(hul_path):
        hul_img_raw = Image.open(hul_path).resize((240, 300))
        hul_img = ImageTk.PhotoImage(hul_img_raw)
    else:
        print(f"Файл huligan.png не найден")
        hul_img = None
except Exception as e:
    print(f"Ошибка загрузки huligan.png: {e}")
    hul_img = None

# === Верхняя реклама ===
ad1 = Frame(right_ads, bg="white", highlightbackground="#cccccc", highlightthickness=1)
ad1.pack(fill="x", padx=10, pady=10)

if bed_img:
    Label(ad1, image=bed_img, bg="white").pack()
else:
    Label(ad1, text="Реклама 1\n(изображение не найдено)", 
          bg="white", height=10, width=30).pack()

# === Нижняя реклама ===
ad2 = Frame(right_ads, bg="white", highlightbackground="#cccccc", highlightthickness=1)
ad2.pack(fill="x", padx=10, pady=10)

if hul_img:
    Label(ad2, image=hul_img, bg="white").pack()
else:
    Label(ad2, text="Реклама 2\n(изображение не найдено)", 
          bg="white", height=10, width=30).pack()

# ========================= СОХРАНЕНИЕ ИЗОБРАЖЕНИЙ =========================

# Сохраняем ссылки на изображения, чтобы не удалились сборщиком мусора
if logo_img:
    root.logo_img = logo_img
if bed_img:
    root.bed_img = bed_img
if hul_img:
    root.hul_img = hul_img
if avatar_img:
    root.avatar_img = avatar_img
if bell_img:
    root.bell_img = bell_img

# Сохраняем иконки вкладок
root.tab_icons = tab_icons

root.mainloop()