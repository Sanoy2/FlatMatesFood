import jsonpickle


def save_decisions(addresses_and_decisions, filename="decisions.json"):
    file = open(filename, "w")
    frozen = jsonpickle.encode(addresses_and_decisions)
    file.write(frozen)
    file.close()


def get_decisions(filename="decisions.json"):
    file = open(filename, "r")
    frozen = file.read()
    addresses_and_decisions = jsonpickle.decode(frozen)
    file.close()
    return addresses_and_decisions
