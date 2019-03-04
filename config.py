import jsonpickle

class config_data:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.addresses = []


    @staticmethod
    def load_config(filename = "config.json"):
        file = open(filename, "r")
        frozen = file.read()
        to_return = jsonpickle.decode(frozen)
        file.close()
        return to_return


    def save_config(self, filename = "config.json"):
        frozen = jsonpickle.encode(self)
        file = open(filename, "w")
        file.write(frozen)
        file.close()


    def __str__(self):
        first_line = "username: {0}".format(self.username)
        second_line = "password: {0}".format(self.password)
        third_line = "addresses: {0}".format(self.addresses.__str__())
        return first_line + "\n" + second_line + "\n" + third_line


    def print_as_html(self):
        return """
<div>
<p> username: {0} </p>
<p> password: {1} </p>
<p> addresses: {2} </p>
</div>
         """.format(self.username, self.password, self.addresses)
