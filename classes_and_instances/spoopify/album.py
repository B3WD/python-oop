from song import Song

class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def get_song_names(self):
        return [s.name for s in self.songs]

    def get_song_by_name(self, song_name):
        for s in self.songs:
            if s.name == song_name:
                return s

    def add_song(self, song : Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return f"Cannot add songs. Album is published."

        if song in self.songs:
            return f"Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song : str):
        if song not in self.get_song_names():
            return f"Song is not in the album."

        if self.published:
            return f"Cannot remove songs. Album is published."

        song_to_remove = self.get_song_by_name(song)
        self.songs.remove(song_to_remove)
        return f"Removed song {song} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        album_name_msg = f"Album {self.name}\n"
        album_songs_msg = [f"== {s.get_info()}\n" for s in self.songs]

        return album_name_msg + "".join(album_songs_msg)