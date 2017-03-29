from handler_base import MessageHandler
import json
import random


class Eightball(MessageHandler):
    
    def __init__(self, path_to_file="handlers/data_files/eightball.json"):
        """
            Finish this __init__ method by storing the json in "self.data"
            :param path_to_file: Look at the file to see how the json is stored.
        """
        with open(path_to_file) as json_file:
            self.data = ""
    
    def handle_message(self, raw_msg, user_email, username):
        """
            Checks if the "raw_msg" has the command eightball.
            If so it returns a random prediction from the list of predictions
            in the json file above, "path_to_file".
            Otherwise it returns false.
            HINT: remove "pass", to begin as it's not needed.
            HINT: self.data is a holder for the json.
            HINT: you need to randomly select a prediction.
            HINT: repeater.py will show you an example of how a "handle_message" works.
            HINT: the test_eightball_handler.py will assist you in completing
            this challenge.
            HINT: there is also a fully functional bot that you can use to see how the game works.

            :param raw_msg: The message to preform operations on.
            :param user_email: email of the user.
            :param username: username of user who made the request.
            :return: String or False.
        """
        pass

    def help(self):
        return "**eightball** - Get a prediction"
