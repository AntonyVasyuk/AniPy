from PIL import (Image, ImageFont,
                ImageGrab, ImageDraw)
import time

# сделаем скриншот
# задержка в 2 секунды, для того,
# чтобы переключиться на рабочий стол
time.sleep(2)
# создание скриншота
tmp = ImageGrab.grab()
# конвертируем скриншот из 'RGB' в 'RGBA'
scr1 = tmp.convert('RGBA')
# сохраним, понадобится для следующего примера
scr1.save('scr1.png')

# изображение, которое будем накладывать
# создадим прозрачную подложку, размером со скриншот
scr2 = Image.new("RGBA", scr1.size , (0, 0, 0, 0))
# получаем контекст рисования
d = ImageDraw.Draw(scr2)
# подключим шрифт
fnt = ImageFont.load_default()
# координаты привязки текста
xy = (scr1.size[0]//2, scr1.size[1]//2)
# накладываем текст с прозрачностью 80 на прозрачную подложку
d.text(xy, "DOCS-PYTHON.RU", anchor="ms", fill=(0, 0, 0, 100))
# сохраним, понадобится для следующего примера
scr2.save('scr2.png')

##########################
# накладываем изображения #
##########################
img = Image.alpha_composite(scr1, scr2)
# сохраняем и смотрим что получилось
img.save('test.png')