# Задача "Рассылка писем":
def domain_true(adress) :
    res = False
    if ".com" in adress and "@" in adress:
        res = True
    elif ".ru" in adress and "@" in adress:
        res = True
    elif ".net" in adress and "@" in adress:
        res = True
    return res
message = "Добрый день!"
recipient = "BelovPA@yandex.ru"
recipient_sender = "university.help@gmail.com"
recipient_a = "BelovPA_yandex.ru"
recipient_b = "BelovPA@yandex_ru"
recipient_c = "BelovPA_yandex_ru"
sender_new = "u.info@gmail.com"
def send_email(message, recipient, sender = "university.help@gmail.com" ) :
    if domain_true(recipient) and domain_true(sender):
        if  recipient == sender :
            print("Нельзя отправить письмо самому себе!")
        elif sender != "university.help@gmail.com" :
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ", sender, " на адрес ", recipient)
        else :
            print("Письмо успешно отправлено с адреса ", sender, " на адрес ", recipient)
    else :
        print("Невозможно отправить письмо с адреса ", sender, " на адрес ", recipient)

send_email(message, recipient, sender = "university.help@gmail.com")
send_email(message, recipient_sender, sender = "university.help@gmail.com")
send_email(message, recipient, sender_new )
send_email(message, recipient_a, sender = "university.help@gmail.com")
send_email(message, recipient_b, sender = "university.help@gmail.com")
send_email(message, recipient_c, sender = "university.help@gmail.com")

