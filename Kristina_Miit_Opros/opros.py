from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from work_SQL import add_answer, conn, cur


class Answer_Callback(CallbackData, prefix="ans"):
    question: int
    answer: str
    id_user: int


dictionary_answer = {}
dictionary_question = {''}
lis1 = ['',
    'Вспомните, когда вы последний раз дарили подарок. Это было по какому-то поводу или просто так?',
    'Вы дарили подарок лично или от компании людей?',
    'Вы знали, что человек хочет получить или придумали сами?',
    'За сколько времени до торжества вы выбирали подарок?',
    'Сложно ли было выбрать этот подарок?',
    'Какие возникли сложности при выборе подарка?',
    'Вы покупали этот подарок лично или заказали в интернет-магазине?',
    'Упаковываете ли вы подарки, которые дарите?',
    'Вы делаете это самостоятельно или обращаетесь в специальные организации?',
    'Угадали в итоге с подарком?',
    'Чем обусловлено отсутствие сложности в выборе подарка?',
    'Обычно вы являетесь организатором сборов на подарки?',
    'Почему вы выбрали такой подарок?',
    'Если вы дарите не деньги, то где вы покупаете подарок?',
    'За сколько времени до торжества вы выбираете подарок?',
    'Упаковываете ли вы подарок, который дарите?',
    'Вы делаете это самостоятельно или обращаетесь в специальные организации?',
	'Всегда ли вы помните дни рождения друзей и близких, коллег?',
	'Вы любите в основном сами выбирать и придумывать подарки или вам нужна четкая инструкция, что конкретно хочет человек?',
	'Что важнее для вас при дарении подарка?',
	'Кому чаще всего вы дарите подарки?',
    'Ведете ли вы список подарков, которые можно подарить друзьям?',
    'Вы знали, что человек хочет получить или придумали сами?'
]

lis2 = ['',
    ['был повод', 'без повода'],
    ['лично', 'от компании'],
    ['сам/а придумал/а', 'точно знал/а, что человек хочет получить', 'подарил/а деньги'],
    ['за месяц', 'за неделю', 'от недели до месяца', 'в последний момент'],
    ['да', 'нет'],
    ['не укладывался в бюджет', 'товара не было в наличии', 'не укладываюсь в сроки'],
    ['лично', 'заказал/а в интернет-магазине'],
    ['да', 'нет'],
    ['люблю сам/а', 'иду, чтобы упаковали за меня'],
    ['да', 'нет'],
    ['я заранее знал/а, что подарю', 'увидел/а в интернете, понравилось, купил/а', 'увидел/а в магазине, понравилось, купил/а'],
    ['да, я люблю быть организатором', 'нет, просто скидываю деньги'],
    ['не знал/а, что подарить', 'считаю, что деньги лучший подарок', 'знал/а, что человек копит на что-то', 'это был коллективный подарок'],
    ['хожу сам/а в магазин', 'заказываю в интернет-магазине'],
    ['за месяц', 'за неделю', 'от недели до месяца', 'в последний момент'],
    ['да', 'нет'],
    ['люблю сам/а', 'иду, чтобы упаковали за меня'],
    ['да, помню', 'нет, мне нужны напоминания'],
    ['люблю сам/а выбирать', 'мне нужно знать, что хочет человек'],
    ['эмоции получателя', 'мнение о вас получателя', 'удовлетворенность получателя подарком', 'мнения присутствующих людей при процессе дарения'],
    ['родственникам', 'друзьям', 'коллегам', 'детям'],
    ['да, записываю идеи', 'такого списка у меня нет'],
    ['сами придумали', 'точно знали, что человек хочет получить', 'подарили деньги']
]

lis = [i for i in range(len(lis1))]


def history_answer(number_question:int, answer:str) -> int:
    print(number_question, answer)
    if number_question == 0:
        return 18
    if number_question == 21 or number_question == 20 or number_question == 19 or number_question == 18:
        return number_question + 1
    if number_question == 22:
        return 1
    if number_question == 1 or (number_question == 3 and answer[-1] != 'в') or number_question == 7:
        return number_question + 1
    if number_question == 3 and answer[-1] == 'в':
        return 13
    if number_question == 2 and answer[-1] == 'а':
        return 3
    if number_question == 2 and answer[-1] == 'б':
        return 12
    if number_question == 12:
        return 23
    if number_question == 23 and answer[-1] == 'в':
        return 13
    if number_question == 23:
        return 4
    if number_question == 4 and answer[-2] == 'а':
        return 5
    if number_question == 4 and answer[-2] == 'б':
        return 7
    if number_question == 5 and answer[-1] == 'а':
        return 6
    if number_question == 5 and answer[-1] == 'б':
        return 11
    if number_question == 6 or number_question == 11:
        return 7
    if number_question == 8 and answer[-1] == 'а':
        return 9
    if number_question == 8 and answer[-1] == 'б' and len(answer.split('_')[-1]) > 12:
        return 10
    if number_question == 8 and answer[-1] == 'б' and len(answer.split('_')[-1]) < 13:
        return 0
    if number_question == 9 and len(answer.split('_')[-1]) > 13:
        return 10
    if number_question == 9 and len(answer.split('_')[-1]) <= 13:
        return 0
    if number_question == 10:
        return 0
    if number_question == 13 or number_question == 14 or number_question == 15:
        return number_question + 1
    if number_question == 16 and answer[-1] == 'а':
        return 17
    if number_question == 16 and answer[-1] == 'б':
        return 0
    if number_question == 17:
        return 0


def make_question(number_question:int, answer:str) -> tuple:
    alfa = ['а', 'б', 'в', 'г', 'д', 'е']
    question = []
    number = history_answer(number_question, answer)
    if number == 0:
        post = 'Спасибо большое за участие в опросе!'
        return (post, number, 0)
    question.append(lis[number])
    question.append(lis1[number])
    temp = []
    for i in range(len(lis2[number])):
        temp.append(f'{alfa[i]}) {lis2[number][i]}\n')
    n = len(temp)
    question.append(''.join(temp))
    post = f'''<b>{question[1]}</b>\n{question[2]}
    '''
    return (post, number, n)


def get_keyboard_fab(n:int, call_back_info:Answer_Callback, number:int):
    alfa = ['а', 'б', 'в', 'г', 'д', 'е']
    builder = InlineKeyboardBuilder()
    if number == 0:
        builder.button(
            text="Пройти еще раз?",
            callback_data=Answer_Callback(question=0, answer="Ответы_", id_user=call_back_info.id_user))
        return builder.as_markup()
    for i in range(n):
        builder.button(
            text=f"{alfa[i]})",
            callback_data=Answer_Callback(
                question=number,
                answer=f"{call_back_info.answer}{alfa[i]}",
                id_user=call_back_info.id_user))
    builder.adjust(n)
    return builder.as_markup()


def zapomni_otvet(id:int, answer:str) -> None:
    global dictionary_answer
    if id not in dictionary_answer:
        dictionary_answer[id] = [answer[-1]]
    else:
        dictionary_answer[id].append(answer[-1])


# def what_text_message(mess:str, id:int) -> str:
#     parser_mess = mess.split('.')
#     vopros = make_question(int(parser_mess[0]))
#     zapomni_otvet(id, parser_mess)
#     return vopros

def what_answer(otv: Answer_Callback):
    zapomni_otvet(otv.id_user, otv.answer)
    mess, number, n = make_question(otv.question, otv.answer)
    mess_keyboard = get_keyboard_fab(n, otv, number)
    add_answer(otv.id_user, otv.question, otv.answer[-1], conn, cur)
    return mess, mess_keyboard



# Первая версия вопросов

# lis1 = ['',
#     'Любите ли вы дарить подарки?',
#     'Тяжело ли вам выбрать подарок?',
#     'Что важнее для вас при дарении подарка?',
#     'Какой тип подарка вы выбираете?',
#     'Учитываете ли вы вкусы получателя?',
#     'За сколько времени до торжества вы выбираете подарок?',
#     'Где предпочитаете выбирать подарки?',
#     'Часто ли вы дарите подарки?',
#     'Упаковываете ли вы подарок в упаковочную бумагу?',
#     'Кому, в большинстве случаев, вы дарите подарки?',
#     'Делаете ли вы подарки незнакомым людям?',
#     'Любите ли вы получать подарки?',
#     'Какие подарки вы больше всего любите?',
#     'Важно ли для вас, чтобы подарок был упакован в подарочную бумагу?',
#     'Вы предпочтете готовый подарок или подарок-действие?'
# ]
#
# lis2 = ['',
#     ['Да', 'Нет'],
#     ['Да', 'Нет'],
#     ['Эмоции получателя', 'Мнение о вас получателя', 'Удовлетворенность получателя подарком', 'Мнения присутствующих людей при процессе дарения', 'Ничего из выше перечисленного'],
#     ['Нужные товары получателю', 'Веселые товары', 'Лишь бы было', 'Деньги', 'То что найду', 'Оригинальные подарки'],
#     ['Да', 'Нет'],
#     ['За месяц', 'За неделю', 'От недели до месяца', 'В последний момент'],
#     ['Сами идете в магазин', 'Заказываю в Интернет-магазине'],
#     ['Только по какому-то поводу', 'Мне нравится дарить подарки, поэтому дарю и без повода', 'Редко'],
#     ['Да', 'Нет'],
#     ['Родным', 'Друзьям', 'Коллегам'],
#     ['Да, делаю такие вещи', 'Это не про меня'],
#     ['Да', 'Нет', 'Мне все равно'],
#     ['Нужные', 'Оригинальные', 'Сделанные собственными руками'],
#     ['Да', 'Нет'],
#     ['Готовый - вещи, нематериальное творчество.', 'Подарок-действие - сертификаты, обучение, платные подписки и т.д.']
# ]
#
# lis = [i for i in range(len(lis1))]