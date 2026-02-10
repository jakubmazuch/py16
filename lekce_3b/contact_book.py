from contact import Contact


class ContactBook:
    def __init__(self):
        self.contacts: list[Contact] = []

    def add(self, contact: Contact) -> None:
        if self._email_exists(contact.email):
            raise ValueError(f"E-mail {contact.email} již existuje.")
        self.contacts.append(contact)

    def remove_by_email(self, email: str) -> None:
        email = email.strip()
        for i, c in enumerate(self.contacts):
            if c.email.lower() == email.lower():
                del self.contacts[i]
                return
        raise ValueError(f"Kontakt s e-mailem '{email}' nebyl nalezen.")

    def find(self, query: str) -> list[Contact]:
        q = query.strip().lower()
        vysledky: list[Contact] = []

        for x in self.contacts:
            if (
                q in x.first_name.lower() or
                q in x.last_name.lower() or
                q in x.email.lower() or
                q in x.phone.lower()
            ):
                vysledky.append(x)
        return vysledky

    def filter_by_tag(self, tag: str) -> list[Contact]:
        tag = tag.strip()
        return [c for c in self.contacts if c.has_tag(tag)]

    def list_all(self, sort_by: str = "name") -> list[Contact]:
        sort_by = sort_by.strip().lower()

        if sort_by == "name":
            return sorted(self.contacts, key=lambda c: (c.last_name.lower(), c.first_name.lower()))
        if sort_by == "email":
            return sorted(self.contacts, key=lambda c: c.email.lower())
        raise ValueError("Chyba vstupu.")
