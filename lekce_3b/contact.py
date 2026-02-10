class Contact:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: str,
        phone: str,
        tags: list[str] | None = None
    ):
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.email = email.strip()
        self.phone = phone.strip()
        self.tags = tags if tags is not None else []

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def has_tag(self, tag: str) -> bool:
        return tag in self.tags

    def __str__(self) -> str:
        tags_text = ", ".join(self.tags) if self.tags else "-"
        return (
            f"{self.full_name()}\n"
            f" e-mail: {self.email}\n"
            f" telefon: {self.phone}\n"
            f" tagy: {tags_text}"
        )
