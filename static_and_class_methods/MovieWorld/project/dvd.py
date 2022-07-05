import calendar

class DVD:
    def __init__(
        self, 
        name: str, 
        id: int, 
        creation_year: int, 
        creation_month: str, 
        age_restriction: int
        ):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @staticmethod
    def string_date_to_int(date: str):

        d, m, y = map(int, date.split("."))
        return (d, m, y)

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        _, m, y = cls.string_date_to_int(date)
        m_string = calendar.month_name[m]
        return cls(name, id, y, m_string, age_restriction)

    def __repr__(self) -> str:
        status = "rented" if self.is_rented else "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}"