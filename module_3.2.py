import re

pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.(?:com|net|ru))\"?"


def email_validation(email):
    if isinstance(email, str):
        emailPattern = re.compile(pattern)
        if re.match(emailPattern, email):
            return True
        else:
            return False
    else:
        return False


def send_email(message, recipient, sender="university.help@gmail.com"):
    if isinstance(recipient, str) and isinstance(sender, str) and isinstance(message, str):
        if sender == recipient:
            print("Нельзя отправить письмо самому себе!")
            return
        if email_validation(recipient) and email_validation(sender):
            if sender == "university.help@gmail.com":
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
                return
            else:
                print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
                return
        else:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
