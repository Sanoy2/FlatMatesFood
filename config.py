import jsonpickle

class config_data:
    def __init__(self):
        self.email_box_username = ""
        self.email_box_password = ""
        self.addresses = []


    @staticmethod
    def load_config(filename = "config.json"):
        file = open(filename, "r")
        frozen = file.read()
        config_data_obj = jsonpickle.decode(frozen)
        file.close()
        return config_data_obj


    def save_config(self, filename = "config.json"):
        frozen = jsonpickle.encode(self)
        file = open(filename, "w")
        file.write(frozen)
        file.close()


    def __str__(self):
        first_line = "username: {0}".format(self.email_box_username)
        second_line = "password: {0}".format(self.email_box_password)
        third_line = "addresses: {0}".format(self.addresses.__str__())
        return first_line + "\n" + second_line + "\n" + third_line


    def print_as_html(self):
        return """
<div>
<p> username: {0} </p>
<p> password: {1} </p>
<p> addresses: {2} </p>
</div>
         """.format(self.email_box_username, self.email_box_password, self.addresses)
