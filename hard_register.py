# Задание "Свой YouTube"

class User :
    """
    Атрибуты:
    nickname(имя пользователя, строка),
    password(в хэшированном виде, число),
    age(возраст, число)
    """
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = str(password)
        self.age = int(age)

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

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    def register(self, nickname, password, age):
        new_user = User(nickname, hash(password), age)
        for current_user in self.users:
            if current_user.nickname == nickname and current_user.password == hash(password) :
                print(f"{current_user.nickname}, Вы уже были зарегистрированы в БД UrTube. "
                    f"Ваша учетная запись - Никнейм:, {current_user.nickname}, "
                    f"Пароль:, {current_user.password}, Возраст:, {current_user.age}")
                break
            break
        self.users.append(new_user)
        self.current_user = new_user
        print(f"{new_user.nickname}, Вы успешно зарегистрированы в БД UrTube. "
              f"Ваша учетная запись - Никнейм:, {new_user.nickname}, "
              f"Пароль:, {new_user.password}, Возраст:, {new_user.age}")


    def log_in(self, nickname, password):
        hashed_password = hash(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"{nickname}, добро пожаловать в UrTube!")
                return
        print(f"{nickname}, к сожалению, Вы отсутствуете в БД. Пожалуйста, зарегистрируйтесь.")

    def log_out(self):
        if self.current_user is not None:
            print("До следующей встречи, ", self.current_user.nickname)
            self.current_user = None
        else:
            print(f"Нет пользователя, желающего выйти: current_user = { self.current_user}")

# Тест метода register

print("    Тест метода register")
urt = UrTube()
urt.register("Me", "1", 70)
urt.register("Me", "2", 70)
urt.register("Anybody", 1, 72)
urt.register("You", "1", 72)
print("Список всех пользователей БД UrTube:")
for user in urt.users:
    print(" ",user.nickname, user.password, user.age)

# Тест метода log_in

print("     Тест метода log_in")
urt.log_in("Me", "1")
urt.log_in("Anybody", 1)
urt.log_in("You", "C3")
urt.log_in("New", "C3")




