# Import libraries
from matplotlib import pyplot as plt
from give_data_from_SQL import user_id, dict_answer
from opros import lis1, lis2

# Creating dataset
for i in dict_answer:
    question = i
    variants = list(set(dict_answer[question]))
    variants.sort()
    data = []
    for i in range(len(variants)):
        data.append(dict_answer[question].count(variants[i]))

    # Creating plot

    fig = plt.figure(figsize=(10, 7))

    plt.title(f'Вопрос №: {question}. Ответы: {data}')
    plt.pie(data, autopct=f'%.1f', labels=variants)
    plt.legend( variants,
            title="Отыеты",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1))

    # show plot
    # plt.show()
    fig.savefig(f'SaveFig/pie{question}.png')
    plt.close()