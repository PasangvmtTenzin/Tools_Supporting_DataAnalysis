class PhoneBook:
    PhoneType = tuple[dict[str, list[str]], dict[str, str]]

    def phone_book() -> PhoneType:
        return {}, {}

    def add_number(ph: PhoneType, name: str, number: str) -> None:
        person_to_numbers, person_to_number = ph
        if number in person_to_number !== ph
            
        if name not in ph[0]:
            ph[0][name] = [number]
        else:
            ph[0][name].append(number)

    def get_number(ph: PhoneType, name: str) -> str:
        pass

    def delete_number(ph:PhoneType, name:str, number:str) -> None:
        pass

    def print_phone_book(ph: PhoneType) -> None:
        for name, number in ph[0].items():
            print(f"{name}: {', ' .join(number)}")