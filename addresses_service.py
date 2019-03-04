import jsonpickle


def get_dictionary(filename="decisions.json"):
    try:
        file = open(filename, "r")
        frozen = file.read()
        addresses_and_decisions = jsonpickle.decode(frozen)
        file.close()
        return addresses_and_decisions
    except:
        reset(filename)
        return get_dictionary(filename)


def save_dictionary(dictionary, filename="decisions.json"):
    frozen = jsonpickle.encode(dictionary)
    file = open(filename, "w")
    file.write(frozen)
    file.close()


def reset(filename="decisions.json"):
    save_dictionary([])


def add_decision(email:str, decision:int, filename="decisions.json"):
    dictionary = get_dictionary()
    email = email.strip().lower()
    if not email in dictionary:
        dictionary[email] = decision
        save_dictionary(dictionary)