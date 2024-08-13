# Задание "Свой YouTube"
# Всего будет 3 класса: User, Video, UrTube.


class User :
    """
    Атрибуты:
    nickname(имя пользователя, строка),
    password(в хэшированном виде, число),
    age(возраст, число)
    """
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(int(password))
        self.age = int(age)

class Video :
    """
    Атрибуты:
    title(заголовок, строка),
    duration(продолжительность, секунды),
    time_now(секунда остановки (изначально 0)),
    adult_mode(ограничение по возрасту,
    bool (False по умолчанию)
    """
    def __init__(self, title, duration, time_now, adult_mode, bool):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = 0
        self.adult_mode = int(adult_mode)
        self.bool = False

class UrTube :
    """
    Атриубты:
    users(список объектов User),
    videos(список объектов Video),
    current_user(текущий пользователь, User)

    Методы:
    register,   который принимает три аргумента: nickname, password, age, и
                добавляет пользователя в список, если пользователя не существует (с таким же nickname).
                если существует, выводит на экран: "Пользователь {nickname} уже существует".
                После регистрации, вход выполняется автоматически.
    log_in,     который принимает на вход аргументы: nickname, password и пытается найти пользователя в users
    log_out     для сброса текущего пользователя на None.
    add,        который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
                если с таким же названием видео ещё не существует.
                В противном случае ничего не происходит.
    get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово.
                Регистр не учитывает.
    watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
                то ничего не воспроизводится,
                если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
                После текущее время просмотра данного видео сбрасывается.
    """
    def __init__(self, users, videos, current_user = None):
        self.users = users
        self.videos = videos
        self.current_user = current_user
    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        for user in self.users :
            if user.nickname == self.nickname :
                print("Пользователь ", self.nickname, " уже зарегистрирован ")
                break
            else :
                user = User(self.nickname, hash(self.password), self.age)
                self.current_user = user
                self.users.append(user)
        print(self.nickname, ", Вы зарегистрированы в БД UrTube. Ваша учетная запись :  ", self.current_user )
        print("Список всех пользователей БД UrTube : ", users)
        # print(self.nickname, ", Добро пожаловать в UrTube! ")
    def log_in(self,nickname, password ):
        if self.current_user is None :
            self.nickname = input("Введите Ваш логин : " )
            self.password = int(input("Введите Ваш пароль : " ))
            for user in self.users :
                if user.nickname == self.nickname and user.password == hash(self.password) :
                    self.current_user = user
                    print(self.nickname, "Добро пожаловать в UrTube! ")
                    break
users = []
videos = []
user = User("Я", 1, 10)
print(user.nickname, user.password, user.age )
ur1 = UrTube(users, videos)
ur1.register("Me", 1, 70)











