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

    def __init__(self, current_user = None):
        self.users = []
        self.videos = []
        self.current_user = current_user

    def register(self, nickname, password, age):
        user = User(nickname, hash(password), age)
        self.current_user = user
        self.users.append(user)
        print(user.nickname, ", Вы зарегистрированы в БД UrTube. Ваша учетная запись :  ",
            user.nickname, user.password, user.age)
    def log_in(self, nickname, password):
        self.nickname = nickname
        self.password = int(password)
        if self.current_user is None:
            for user in self.users:
                if user.nickname == self.nickname and user.password == hash(self.password):
                    self.current_user = user
                    print(self.nickname, "Добро пожаловать в UrTube! ")
                    break
                else :
                    print("К сожалению, Вы отсутствуете в БД. Пожалуйста, зарегистрируйтесь")
            else :
                print("Вы уже зарегистрировались, ", self.nickname )

    def log_out(self, current_user) :
        self.current_user = current_user
        print("До следующей встречи, ", self.current_user.nickname)
        self.current_user = None

    def add(self, videos, *all_videos):
            # Откуда берётся неопределенный список *all_videos,
            # который надо сравнивать с имеющимся списком videos?
        self.videos = videos
        for i in all_videos:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, your_str):
        self.your_str = your_str.lower()
        list_video = []
        for i in self.videos:
            if self.your_str in i.title.lower() :
                list_video.append(i.title)
                flag = True
            else:
                flag = False
        if flag :
            print("Ключевое слово ", your_str , " найдено в следующих видео: ")
            for i in list_vid :
                print(i.title)
        else :
            print("Названия видео в videos не содержат ключевого слова ", your_str)

    def watch_video(self, wanted_video):
        self.wanted_video = wanted_video
        for i in self.videos:
            if self.wanted_video == i.title:
                if self.current_user.age < i.adult_mode:
                    print(" Это видео имеет ограничение по возрасту: ", i.adult_mode )
                    break
                for j in range(0, i.duration):
                    print("Просмотр видео идет ", j , " секунд. До конца видео осталось ", i.duration - j, " секунд")

ur1 = UrTube()
ur1.register("Me", 1, 70 )
ur1.register("You", 2, 72)
print("Список всех пользователей БД UrTube : ")
for i in ur1.users :
    print(i.nickname, i.password, i.age)
ur1.log_in("He", 3 )
        # he не зарегистрирован, но залогинился
ur1.log_in("Me", 3)
        # Me залогинился под паролем he
print("Список всех пользователей БД UrTube : ")
        # список users не изменился после залогинивания He и Me под чужим паролем
for i in ur1.users:
    print(i.nickname, i.password, i.age)
    # He и Me, под чужим паролем, не зарегистрированы новыми пользователями
#    ur1.log_out("Me", 3)
    # TypeError: UrTube.UrTube.log_out() takes 2 positional arguments but 3 were given
