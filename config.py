import jsonpickle


class config_data:
    def __init__(self):
        self.host = ""
        self.email_box_username = ""
        self.email_box_password = ""
        self.addresses = []

    @staticmethod
    def load_config(filename="config.json"):
        file = open(filename, "r")
        frozen = file.read()
        config_data_obj = jsonpickle.decode(frozen)
        file.close()
        return config_data_obj

    def save_config(self, filename="config.json"):
        frozen = jsonpickle.encode(self)
        file = open(filename, "w")
        file.write(frozen)
        file.close()

    def __str__(self):
        return """ 
{0}
{1}
{2}
{3}""".format(self.host, self.email_box_username, self.email_box_password, self.addresses.__str__())
