class song:
    total_songs = 0
    def __init__(self, name, writer, singer, language, genre, pub_year):
        self.name = name
        self.writer = writer
        self.singer = singer
        self.language = language
        self.genre = genre
        self.pub_year = pub_year

    def display(self):
        print(self.name + "\t" + self.singer + "\t" + self.writer + "\t" + self.pub_year + "\t" + self.language + "\t" + self.genre)

    def pack(self):
        buffer = self.name + "|" + self.singer + "|" + self.writer + "|" + self.pub_year + "|" + self.language + "|" + self.genre + "|"

n = input("Enter number of songs ")
song_list = list()
for i in range(n):
    name = raw_input("Enter the name of the song ")
    singer = raw_input("Enter the name of the singer ")
    writer = raw_input("Enter the name of the song writer ")
    pub_year = raw_input("Enter the year of release ")
    genre = raw_input("Enter the genre of the song ")
    lang = raw_input("Enter the language of the song ")
    s = song(name,writer,singer,lang, genre, pub_year)
    s.total_songs += 1
    song_list.append(s)

for i in song_list:
    i.display()
