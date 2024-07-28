# Задача "Однокоренные":
# Напишите функцию single_root_words, которая принимает одно обязательное слово в параметр root_word, а далее неограниченную последовательность в параметр *other_words.
# Функция должна составить новый список same_words только из тех слов списка other_words, которые содержат root_word или наоборот root_word содержит одно из этих слов. После вернуть список same_words в качестве результата своей работы.
#
# Пункты задачи:
# Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
def single_root_words(root_word , *other_words) :
    flag = False
    same_words = []
    for i in other_words :
        if root_word in i :
            same_words.append(i)
            flag = True
    if flag == True :
        print("Список однокоренных слов с ", root_word, " : ", same_words )
    else :
        print("Нет однокоренных слов в списке ", other_words )
    return

single_root_words("qwe" , "qwert", "werty", "asqwer" )
single_root_words("qwe" , "wert", "werty", "aswer" )