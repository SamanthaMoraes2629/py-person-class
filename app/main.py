class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def set_spouse(self) -> None:
        if self.wife:
            self.wife = Person.people.get(self.wife)
        else:
            None
        if self.husband:
            self.husband = Person.people.get(self.husband)
        else:
            None


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        person_instance = Person(person["name"], person["age"])
        person_list.append(person_instance)

    for person in people:
        person_instance = Person.people.get(person["name"])
        if "wife" in person and person["wife"]:
            person_instance.wife = Person.people.get(person["wife"])
        else:
            None
        if "husband" in person and person["husband"]:
            person_instance.husband = Person.people.get(person["husband"])
        else:
            None

    return person_list
