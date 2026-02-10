from contact import Contact
from contact_book import ContactBook



def print_contacts(title: str, contacts: list[Contact]) -> None:
    print("\n" + title)
    print("-" * len(title))
    
    if not contacts:
        print("Žádné výsledky")
        return
    
    for c in contacts:
        print(c)


def main():
    book = ContactBook()
    
    #Přídám kontakty
    book.add(Contact("Jan", "Novák", "jannovak@example.com", "+420 777 125 485", ["klient"]))
    