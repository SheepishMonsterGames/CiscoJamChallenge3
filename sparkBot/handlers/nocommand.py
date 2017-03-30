from handler_base import MessageHandler
import random


class NoCommand(MessageHandler):
    def __init__(self):
        self.responses = ["**WHAT** %s?", "Huh, did you say something %s?",
                          "Look, please stop with the silence %s!",
                          "Love when people call out my name and then say nothing.",
                          "%s"]

    def handle_message(self, raw_msg, user_email, username):
        if "No Command" in raw_msg:
            return random.choice(self.responses) % str(username)
        return False

    def help(self):
        return ""
