from django.db import models
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator

class MainClass(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
        
    class Meta:
        abstract = True

class Header(MainClass):
    subTitle = models.CharField(max_length=100, verbose_name='Малый заголовок', help_text='Малый заголовок, в дефолтной версии Let me Explain it!', default='Let me Explain it')
    mainTitle = models.CharField(max_length=100, verbose_name='Основной заголовок', help_text='Основной заголовок, в дефолтной версии Курсы по подготовке к USMLE', default='Курсы по подготовке к USMLE')
    buttonOne = models.CharField(max_length=100, verbose_name='Белая кнопка', help_text='Текст на белой кнопке, по дефлоту Узнать по больше', default='Узнать по больше')
    buttonTwo = models.CharField(max_length=100, verbose_name='Синия кнопка', help_text='Текст на синей кнопке, по дефолту Записаться на курсы', default='Записаться на курсы')

    class Meta:
        verbose_name = 'Хедер'
        verbose_name_plural = 'Хедеры'
    
    def __str__(self):
        return self.mainTitle
      
class FirstTopCard(MainClass):
    title = models.CharField(max_length=50, verbose_name='Заголовок карточки 1', help_text='Заголовок первой карточки, по дефолту Команда Менторов', default='Команда Менторов')
    description = models.TextField(max_length=300, verbose_name='Описание первой карточки', help_text='Добавтье описание к первой карточке', default='Успешно сдавшие USMLE преподаватели, практикующие резиденты США обучат и покажут вам дорогу')
    button = models.CharField(max_length=50, verbose_name='Кнопка номер 1 под карточкой', help_text='Текст на кнопке под перой карточкой', default='Read more')

    class Meta:
        verbose_name = 'Первая карточка топ блока'
        verbose_name_plural = 'Первая карточка топ блока'

    def __str__(self):
        return self.title
    
class SecondTopCard(MainClass):
    title = models.CharField(max_length=50, verbose_name='Заголовок карточки 2', help_text='Заголовок второй карточки, по дефолту Общество развития Медиков', default='Общество развития Медиков')
    description = models.TextField(max_length=300, verbose_name='Описание второй карточки', help_text='Добавтье описание ко второй карточке', default='Познакомитесь с кругом новых единомышленников, в тяжелом обучении всегда легче с другом, от первокурсников до опытных врачей')
    button = models.CharField(max_length=50, verbose_name='Кнопка номер 2 под карточкой', help_text='Текст на кнопке под второй карточкой', default='Read more')

    class Meta:
        verbose_name = 'Вторая карточка топ блока'
        verbose_name_plural = 'Вторая карточка топ блока'

    def __str__(self):
        return self.title
    
class ThirdTopCard(MainClass):
    title = models.CharField(max_length=50, verbose_name='Заголовок карточки 3', help_text='Заголовок терий карточки, по дефолту Поднимите себя до мирового стандарта', default='Поднимите себя до мирового стандарта')
    description = models.TextField(max_length=300, verbose_name='Описание третьей карточки', help_text='Добавтье описание к третьей карточке', default='Готовьтесь к самому сложному экзамену по медицине в мире чтобы соответствовать высшему уровню профессионализма')
    button = models.CharField(max_length=50, verbose_name='Кнопка номер 3 под карточкой', help_text='Текст на кнопке под третьей карточкой', default='Read more')

    class Meta:
        verbose_name = 'Третья карточка топ блока'
        verbose_name_plural = 'Третья карточка топ блока'

    def __str__(self):
        return self.title

class ScoreBoardMain(MainClass):
    subtitle = models.CharField(max_length=100, verbose_name='Подзаголовок', help_text='Маленький заголовок над основным заголовком', default='Let me Explain it')
    title = models.CharField(max_length=100, verbose_name='Заголовок', help_text='Основной заголовок', default='Растите с нами')
    colOneNum = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99999)], verbose_name='Первое число', help_text='Первый блок, Целое число, максимум 5 знаков', default='150')
    colOneText = models.CharField(max_length=50, verbose_name='Первый текст', help_text='Текст в первой колонке под числом, макимум 50 символов', default='Довольных учеников')
    colTwoNum = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99999)], verbose_name='Второе число', help_text='Второй блок, Целое число, максимум 5 знаков', default='219')
    colTwoText = models.CharField(max_length=50, verbose_name='Второй текст', help_text='Текст во второй колонке под числом, макимум 50 символов', default='Готовятся вместе')
    colThreeNum = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99999)], verbose_name='Третье число', help_text='Третий блок, Целое число, максимум 5 знаков', default='27')
    colThreeText = models.CharField(max_length=50, verbose_name='Третий текст', help_text='Текст в третьей колонке под числом, макимум 50 символов', default='Сдавших с нами')
    colFourNum = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99999)], verbose_name='Четвертое число', help_text='Четвертый блок, Целое число, максимум 5 знаков', default='4')
    colFourText = models.CharField(max_length=50, verbose_name='Четвертый текст', help_text='Текст в четвертой колонке под числом, макимум 50 символов', default='На данный момент резидента США')

    class Meta:
        verbose_name = 'Панель с цифрами'
        verbose_name_plural = 'Панель с цифрами'
    
    def __str__(self):
        return self.title
    
class MentorTitle(MainClass):
    title = models.CharField(max_length=100, verbose_name='Заголовок', help_text='Заголовок блока менторы', default='Наши менторы')

    class Meta:
        verbose_name = 'Заголовок Менторы'
        verbose_name_plural = 'Заголовок Менторы'
    
    def __str__(self):
        return self.title
    
class MentorOne(MainClass):
    photo = models.ImageField(upload_to='firstMentor/', verbose_name='Фотография', help_text='Фотография ментора в первой карточке')
    subtitle = models.CharField(max_length=50, verbose_name='Подзаголовок', help_text='Подзаголовок над именем и фамилией', default='Курсы')
    firstName = models.CharField(max_length=50, verbose_name='Имя', help_text='Поле для ввода имени', default='Аман')
    secondName = models.CharField(max_length=50, verbose_name='Фамилия', help_text='Поле для ввода ффамилии', default='Базаров')
    grade = models.CharField(max_length=50, verbose_name='Ученая степень', help_text='Указывается ученая степень', default='USMLE Step 1, Step 2')
    exp = models.CharField(max_length=50, verbose_name='Опыт', help_text='Указывается опыт', default='стажировка США, Окончил с красным дипломом')

    class Meta:
        verbose_name = 'Первый ментор'
        verbose_name_plural = 'Первый ментор'
    
    def __str__(self):
        return f'{self.firstName} {self.secondName}'
    
class MentorTwo(MainClass):
    photo = models.ImageField(upload_to='secondMentor/', verbose_name='Фотография', help_text='Фотография ментора вd dnjhjq карточке')
    subtitle = models.CharField(max_length=50, verbose_name='Подзаголовок', help_text='Подзаголовок над именем и фамилией', default='Курсы')
    firstName = models.CharField(max_length=50, verbose_name='Имя', help_text='Поле для ввода имени', default='Калым')
    secondName = models.CharField(max_length=50, verbose_name='Фамилия', help_text='Поле для ввода ффамилии', default='Соодонбеков')
    grade = models.CharField(max_length=50, verbose_name='Ученая степень', help_text='Указывается ученая степень', default='USMLE Step 1, Step 2')
    exp = models.CharField(max_length=50, verbose_name='Опыт', help_text='Указывается опыт', default='преподаватель Ала - Тоо университета, марафонец')

    class Meta:
        verbose_name = 'Второй ментор'
        verbose_name_plural = 'Второй ментор'
    
    def __str__(self):
        return f'{self.firstName} {self.secondName}'
    
class PriceTitile(MainClass):
    subtitle = models.CharField(max_length=50, verbose_name='Подзаголовок', help_text='Маленький заголовок над основным заголовком', default='Оффлайн/Онлайн')
    title = models.CharField(max_length=100, verbose_name='Заголовок', help_text='Основной заголовок', default='Опции курсов')

    class Meta:
        verbose_name = 'Заголовок цены курсы'
        verbose_name_plural = 'Заголовки цен курсов'
    
    def __str__(self):
        return self.title
    
class PriceCardOne(MainClass):
    upperButton = models.CharField(max_length=50, verbose_name='Верхний подзаголовок', help_text='Маленький заголовок над основной карточкой в синем поле', default='Популярный')
    price = models.CharField(max_length=50, verbose_name='Цена и срок', help_text='Цена и срок выделенные зеленым цветом', default='4.5к сом/ мес.')
    description = models.CharField(max_length=150, verbose_name='Описание', help_text='Описание над основным заголовком красного цвета', default='Подходит для всех желающих обучаться в большом потоке, особенно для студентов.')
    title = models.CharField(max_length=50, verbose_name='Основной заголовок', help_text='Основной заголовок красного цвета', default='Standard')
    button = models.CharField(max_length=50, verbose_name='Текст на кнопке', help_text='Текст на синей кнопке', default='Buy Now')

    class Meta:
        verbose_name = 'Карточка обучения номер один'
        verbose_name_plural = 'Карточка обучения номер один'
    
    def __str__(self):
        return self.title
    
class PriceCardOneOption(MainClass):
    option = models.CharField(max_length=50, verbose_name='Опция', help_text='Опция в первой карточке обучения')

    class Meta:
        verbose_name = 'Опция обучения номер один'
        verbose_name_plural = 'Опции обучения номер один'
    
    def __str__(self):
        return self.option
    
class PriceCardTwo(MainClass):
    upperButton = models.CharField(max_length=50, verbose_name='Верхний подзаголовок', help_text='Маленький заголовок над основной карточкой в синем поле', default='Быстрый')
    price = models.CharField(max_length=50, verbose_name='Цена и срок', help_text='Цена и срок выделенные зеленым цветом', default='9.8к сом/мес')
    description = models.CharField(max_length=150, verbose_name='Описание', help_text='Описание над основным заголовком красного цвета', default='Только ординаторы, врачи и студенты 6 курса')
    title = models.CharField(max_length=50, verbose_name='Основной заголовок', help_text='Основной заголовок красного цвета', default='Iad`s Method')
    button = models.CharField(max_length=50, verbose_name='Текст на кнопке', help_text='Текст на синей кнопке', default='Buy Now')

    class Meta:
        verbose_name = 'Карточка обучения номер два'
        verbose_name_plural = 'Карточка обучения номер два'
    
    def __str__(self):
        return self.title
    
class PriceCardTwoOption(MainClass):
    option = models.CharField(max_length=50, verbose_name='Опция', help_text='Опция во второй карточке обучения')

    class Meta:
        verbose_name = 'Опция обучения номер два'
        verbose_name_plural = 'Опции обучения номер два'
    
    def __str__(self):
        return self.option
    
class PriceCardThree(MainClass):
    price = models.CharField(max_length=50, verbose_name='Цена и срок', help_text='Цена и срок выделенные зеленым цветом', default='4к сом/мес или 15к сом за 8 месяцев')
    description = models.CharField(max_length=150, verbose_name='Описание', help_text='Описание над основным заголовком красного цвета', default='Для тех кто не может найти время, а на курсы так хочется.')
    title = models.CharField(max_length=50, verbose_name='Основной заголовок', help_text='Основной заголовок красного цвета', default='Онлайн')
    button = models.CharField(max_length=50, verbose_name='Текст на кнопке', help_text='Текст на синей кнопке', default='Buy Now')

    class Meta:
        verbose_name = 'Карточка обучения номер три'
        verbose_name_plural = 'Карточка обучения номер три'
    
    def __str__(self):
        return self.title
    
class PriceCardThreeOption(MainClass):
    option = models.CharField(max_length=50, verbose_name='Опция', help_text='Опция во третей карточке обучения')

    class Meta:
        verbose_name = 'Опция обучения номер три'
        verbose_name_plural = 'Опции обучения номер три'
    
    def __str__(self):
        return self.option
    
class DarkBlock(MainClass):
    subtitle = models.CharField(max_length=50, verbose_name='Подзаголовок', help_text='Правый подзаголовок на тёмном блоке над основым заголовком блока', default='Why not')
    title = models.CharField(max_length=100, verbose_name='Заголовок', help_text='Правый заголовок на тёмном блоке ', default='Choose the Best')
    descrition = models.CharField(max_length=200, verbose_name='Описание', help_text='Опасание под основным заголовком на тёмном блоке ', default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse varius enim in eros elementum tristique.')
    secondTitle = models.CharField(max_length=100, verbose_name='Второй заголовок', help_text='Второй заголовок на светлом блоке', default='Try our freemium theme')
    secondDescription = models.CharField(max_length=200, verbose_name='Второе описание', help_text='Опасание под вторым заголоком на светлом блоке ', default='With advanced features of higher quality than other similar marketplace themes.')
    button = models.CharField(max_length=50, verbose_name='Текст на кнопке', help_text='Текст на синий кнопке на светлом блоке', default='GET STARTED')

    class Meta:
        verbose_name = 'Блок информации на темном фоне'
        verbose_name_plural = 'Блоки информации на темном фоне'
    
    def __str__(self):
        return self.title
    
class HelpBlock(MainClass):
    subtitle = models.CharField(max_length=50, verbose_name='Подзаголовок', help_text='Подзаголовок на над основным заголовком', default='Помощь от')
    title = models.CharField(max_length=100, verbose_name='Заголовок', help_text='Основной заголовок ', default='В благодраность')
    imageOne = models.ImageField(upload_to='helpone/', verbose_name='Первое фото', help_text='Верхнее фото блока с благодарностями')
    imageTwo = models.ImageField(upload_to='helptwo/', verbose_name='Второе фото', help_text='Нижнее фото блока с благодарностями')

    class Meta:
        verbose_name = 'Блок благодарностей'
        verbose_name_plural = 'Блоки благодарностей'
    
    def __str__(self):
        return self.title
    
class LinkTitleBlock(MainClass):
    titleOne = models.CharField(max_length=100, verbose_name='Первый заголовок', help_text='Первый заголовок', default='Pages')
    titleTwo = models.CharField(max_length=100, verbose_name='Второй заголовок', help_text='Второй заголовок', default='Blog')
    titleThree = models.CharField(max_length=100, verbose_name='Третий заголовок', help_text='Третий заголовок', default='Contact')
    
    class Meta:
        verbose_name = 'Названия в блоке ссылок'
        verbose_name_plural = 'Названия в блоке ссылок'
    
    def __str__(self):
        return f'{self.titleOne} {self.titleTwo} {self.titleThree}'
    
    
class LinkOptionBlock(MainClass):   
    optionOne = models.CharField(max_length=100, verbose_name='Ссылки блок 1', help_text='Ссылки под первым заголовком', blank=True)
    optionTwo = models.CharField(max_length=100, verbose_name='Ссылки блок 2', help_text='Ссылки под вторым заголовком', blank=True)
    optionThree = models.CharField(max_length=100, verbose_name='Ссылки блок 3', help_text='Ссылки под третьем заголовком', blank=True)

    class Meta:
        verbose_name = 'Ссылки под заголовком в блоке ссылок'
        verbose_name_plural = 'Ссылки под заголовком в блоке ссылок'
    
    def __str__(self):
        return f'{self.optionOne} {self.optionTwo} {self.optionThree}'