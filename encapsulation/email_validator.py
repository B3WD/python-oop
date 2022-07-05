class EmailParser:
    def __init__(self, mail) -> None:
        self.__mail = mail

    @property
    def username(self):
        return self.__mail.split("@")[0]

    @property
    def mail_name(self):
        tail = self.__mail.split("@")[1]
        return tail.split(".")[0]

    @property
    def domain(self):
        return self.__mail.split(".", maxsplit=1)[1]

    def parse(self):
        return (self.username, self.mail_name, self.domain)


class EmailValidator:
    def __init__(self, min_lenght: int, mails: list, domains: list) -> None:
        self.min_lenght = min_lenght
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name):
        if len(name) < self.min_lenght:
            return False
        return True

    def __validate_mail(self, mail):
        if mail not in self.mails:
            return False
        return True

    def __validate_domain(self, domain):
        if domain not in self.domains:
            return False
        return True

    def validate(self, email):
        name, mail, domain = EmailParser(email).parse()
        return self.__validate_name(name) and self.__validate_mail(mail) and self.__validate_domain(domain)
    

mails = ["gmail", "softuni"]
domains = ["com", "bg", "co.uk.island.com"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("ivanch0@gmail.co.uk.island.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))