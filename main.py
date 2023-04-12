import random
from faker import Faker
from datetime import datetime
class Movie():
    def __init__(self, title, publication_date, genre, views):
        self.title = title
        self.publication_date = publication_date
        self.genre = genre
        self.views = views

    def __str__(self):
        return f"{self.title} ({self.publication_date})"

    def play(self):
        self.views += 1

class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super(Series, self).__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f"{self.title} S{self.season:02d}E{self.episode:02d}"

def get_movies(films):
    tmp = []
    for film in films:
        if "(" and ")" in film.__str__().split()[-1]:
            tmp.append(film)
    return sorted(tmp, key=lambda movie:movie.title)

def get_series(films):
    tmp = []
    for film in films:
        if "E" and "S" in film.__str__().split()[-1]:
            tmp.append(film)
    return sorted(tmp, key=lambda movie:movie.title)

def search(title, films):
    for x in range(len(films)):
        if title == films[x].title:
            return True
    else:
        return False

def generate_views(films):
    number_of_film = random.randint(0, len(films) - 1)
    for x in range(0, random.randint(1, 100)):
        films[number_of_film].play()

def ten_times_generate_views(films):
    for x in range(10):
        generate_views(films)

def top_titles(films, numbers_of_videos):
    sorted_by_views = sorted([films[x] for x in range(len(films))], key=lambda movie:movie.views)[::-1]
    if numbers_of_videos <= len(films) and numbers_of_videos > 0:
        for x in range(numbers_of_videos):
            print(sorted_by_views[x])
    else:
        print("Podana liczba filmów jest błęda")

def fill_content():
    genres = ['Akcja', 'Komedia', 'Dramat', 'Horror', 'Thriller', 'Romans', 'Science Fiction']
    fake = Faker()
    films_list = []
    for x in range(random.randint(1, 10)):
        films_list.append(Movie(title=fake.catch_phrase(), publication_date=fake.year(), genre=random.choice(genres), views=random.randint(0, 100)))
    for x in range(random.randint(1, 10)):
        films_list.append(Series(title=fake.catch_phrase(), publication_date=fake.year(), genre=random.choice(genres), views=random.randint(0, 100), episode=random.randint(1, 30), season=random.randint(1, 15)))
    return films_list


if __name__ == "__main__":
    print("Biblioteka filmów.")
    films_list = fill_content()
    generate_views(films_list)
    print(f"Najpopularniejsze filmy i seriale dnia {datetime.today().strftime('%d.%m.%Y')}")
    top_titles(films_list, 3)