# game-translator

## Установка зависимостей
- python >= 3.11 < 3.12 (установить с установленной галкой на опции **Tcl/Tk**)
- установить https://github.com/UB-Mannheim/tesseract/wiki (нужен для распознавания текста)

## Установка
1. Выполнить клонирование кода и установку зависимостей
```bash
git clone https://github.com/neriper/game-translator.git
cd game-translator
py -m venv .venv
.venv\Scripts\pip install uv
.venv/Scripts/uv pip install -r requirements.txt
```
2. В файле [config.ini](config.ini) в блоке SCREEN указать свое разрешение монитора 
3. В файле [config.ini](config.ini) в блоке SCREENSHOOT указать в параметре TESSERACT_OCR путь до tesseract.exe

## Запуск
Выполнить команду в консоли из папки game-translator

### WINDOWS
```bash
 .venv/Scripts/python main.py
```

## Принцип работы / Использование
- P.S. игра должна быть в **оконном режиме**
- P.S. есть ошибка с первым выделением, со второго раза норм!

### Принцип работы
- жмем shift + 1 (раздел конфига SCREENSHOOT/CREATE)
- выделяем область текста
- появляется перевод выделенной области на белом фоне
- закрываем окно перевода shift + 2 (раздел конфига SCREENSHOOT/CLOSE)

### Использование
- shift + 1 - запускает выбор области перевода
- shift + 2 - закрыть область с переводом либо закрыть по клику на крест в углу

## Описание параметров [config.ini](config.ini)
- SCREEN (разрешение экрана)
  - WIDTH (ширина в пикселях)
  - HEIGHT (высота в пикселях)
- SCREENSHOOT (опции для работы кода)
  - NAME (имя создаваемого скриншота после выделения области)
  - CREATE (комбинация кнопок запуска выбора области с текстом)
    - документация по вариантам кнопок https://pypi.org/project/keyboard/
  - CLOSE (закрытие окна с переводом)
    - документация по вариантам кнопок https://pypi.org/project/keyboard/
- TRANSLATE_SYSTEM (используемая система перевода)
  - SYSTEM (параметр который определяет алгоритм перевода)
    - 1 - translate.googleapis.com
    - 2 - argostranslate
