from song import Song
from album import Album

class Band:
    def __init__(self, name : str):
        self.name = name
        self.albums = []

    def get_album_names(self):
        return [a.name for a in self.albums]

    def get_album_by_name(self, album_name):
        for a in self.albums:
            if a.name == album_name:
                return a

    def add_album(self, album : Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name : str):
        album_to_remove = self.get_album_by_name(album_name)

        if album_to_remove.published:
            return f"Album has been published. It cannot be removed."

        if album_name not in self.get_album_names():
            return f"Album {album_name} is not found."

        self.albums.remove(album_to_remove)
        return f"Album {album_name} has been removed."

    def details(self):
        band_msg = f"Band {self.name}\n"
        band_albums_msg = [f"{a.details()}\n" for a in self.albums]

        return band_msg + "".join(band_albums_msg)


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
