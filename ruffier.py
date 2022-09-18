''' Модуль для розрахунку результатів проби Руф'є.
 
Сума вимірювань пульсу у трьох спробах (до навантаження, одразу після та після короткого відпочинку)
в ідеалі має бути не більше 200 ударів на хвилину.
Ми пропонуємо дітям вимірювати свій пульс протягом 15 секунд,
і наводимо результат до ударів за хвилину множенням на 4:
   S = 4 * (P1 + P2 + P3)
Що далі цей результат від ідеальних 200 ударів, то гірше.
Традиційно таблиці даються для величини, поділеної на 10.
 
Індекс Руф'є  
   IR = (S - 200) / 10
оцінюється за таблицею відповідно до віку:
            7-8           9-10              11-12               13-14               15+ (тільки для підлітків!)
чуд.    6.4 і менше    4.9 і менше       3.4 і менше         1.9 і менше               0.4 і менше
добр.   6.5 - 11.9     5 - 10.4          3.5 - 8.9           2 - 7.4                   0.5 - 5.9
задов.  12 - 16.9      10.5 - 15.4       9 - 13.9            7.5 - 12.4                6 - 10.9
слабк.  17 - 20.9      15.5 - 19.4       14 - 17.9           12.5 - 16.4               11 - 14.9
незад.  21 і більше    19.5 і більше     18 і більше         16.5 і більше             15 і більше
 
для всіх вікових груп результат "незад." відстає від "слабкого" на 4,
той від "задовільного" на 5, а "добрий" від "чуд" - на 5.5
 
тому напишемо функцію ruffier_result(r_index, level), яка отримуватиме
розрахований індекс Руф'є та рівень "незадовільно" для віку тестованого, і віддавати результат
 
'''
# тут задаються рядки, за допомогою яких викладено результат:
txt_index = "Ваш індекс Руф'є: "
txt_workheart = "Працездатність серця: "
txt_nodata = '''Немає даних для такого віку'''
txt_res = []
txt_res.append('''Низька. Терміново зверніться до лікаря!''')
txt_res.append('''Задовільна. Зверніться до лікаря!''')
txt_res.append('''Середня. Можливо, варто додатково обстежитись у лікаря.''')
txt_res.append('''Вище середнього''')
txt_res.append('''Висока''')



def hertbeats_count(p1: int, p2: int, p3: int):
    """Кількість ударів на хвилину"""
    return 4 * (p1 + p2 + p3)


def ruffier(hb_minute: int):
    """Індекс Руф'є"""
    return (hb_minute - 200) / 10


def get_index(age: int):
    n = (min(15, age) - 7) // 2
    x = 21 - n * 1.5
    return x

def result(ruffier, max_index):
    txt_res = [] 

    if ruffier >= max_index:
        txt_res.append('''низкая. 
        Срочно обратитесь к врачу!''')
    elif ruffier >= max_index - 4.5:
        txt_res.append('''удовлетворительная. 
        Обратитесь к врачу!''')
    elif ruffier >= max_index - 9.5:
        txt_res.append('''средняя. 
        Возможно, стоит дополнительно обследоваться у врача.''')
    elif ruffier >= max_index - 15:
        txt_res.append('''
        выше среднего''')
    else:
        txt_res.append('''
        высокая''')
    return txt_res

def main_ruffier(p1, p2, p3, age):
    ruff = ruffier(hertbeats_count(p1, p2, p3))
    age_type = get_index(age)

    return result(ruff, age_type)

def ruffier_index(P1, P2, P3):
    ''' повертає значення індексу за трьома показниками пульсу для звірки з таблицею'''
    pass

def neud_level(age):
    ''' варіанти з віком менше 7 і дорослим треба обробляти окремо,
     тут підбираємо рівень "незадовільно" тільки всередині таблиці:
     у віці 7 років "незад" - це індекс 21, далі кожні 2 роки він знижується на 1.5 до значення 15 в 15-16 років '''
    pass
    
def ruffier_result(r_index, level):
    ''' функція отримує індекс Руф'є та інтерпретує його,
     повертає рівень готовності: число від 0 до 4
     (що вище рівень готовності, то краще).  '''
    pass

def test(P1, P2, P3, age):
    ''' цю функцію можна використовувати зовні модуля для підрахунків індексу Руф'є.
     Повертає готові тексти, які залишається намалювати у потрібному місці
     Використовує для текстів константи, задані на початку цього модуля. '''
    pass
