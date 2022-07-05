import math


class PhotoAlbum:
    MAX_PHOTO_COUNT = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]
        self.current_free_spot = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = math.ceil(photos_count / cls.MAX_PHOTO_COUNT)
        return cls(pages)

    def get_free_spot(self):
        i = self.current_free_spot // PhotoAlbum.MAX_PHOTO_COUNT
        j = i % PhotoAlbum.MAX_PHOTO_COUNT

        return (i, j)

    def add_photo(self, label: str):
        i, j = self.get_free_spot()
        
        if i >= self.pages:
            return f"No more free slots"

        self.photos[i].append(label)
        self.current_free_spot += 1
        return f"{label} photo added successfully on page {i + 1} slot {(j + 1)}"

    def display(self):
        pic = "[] "
        emp = "  "
        sep = "-" * 11
        rep = "" + sep

        for page in self.photos:
            msg = "\n"
            if page:
                q = len(page)
                e = PhotoAlbum.MAX_PHOTO_COUNT - q
                msg += (pic * q).strip() + (emp * e).strip()
            rep += msg + "\n" + sep

        return rep


# album = PhotoAlbum(2)

# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))

# print(album.display())

# album2 = PhotoAlbum(3)
# print(album2.display())