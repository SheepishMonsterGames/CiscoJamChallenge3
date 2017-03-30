from handler_base import MessageHandler
import random


class Futurama(MessageHandler):
    def __init__(self):
        self.quotes = ["Bite my shiny metal ass!", "Shut up baby, I know it!",
                       "Hahahahaha. Oh wait you're serious. Let me laugh even harder.",
                       "You know what cheers me up? Other people's misfortune.",
                       "Anything less than immortality is a complete waste of time.",
                       "Blackmail is such an ugly word. I prefer extortion. The \"x\" makes it sound cool.",
                       "Have you tried turning off the TV, sitting down with your children, and hitting them?"]

    def handle_message(self, raw_msg, user_email, username):
        """
            Checks if the "raw_msg" has the command futurama.
            If so it returns a random quote from the list of "self.quotes" above
            Otherwise it must return False.
            HINT: remove "pass", to begin as it's not needed.
            HINT: select a quote at random.
            HINT: repeater.py will show you an example of how a "handle_message" works.
            HINT: the test_futurama_handler.py will assist you in completing
            this challenge.
            HINT: there is also a fully functional bot that you can use to see how the game works.

            :param raw_msg: The message to preform operations on.
            :param user_email: email of the user.
            :param username: username of user who made the request.
            :return: String or False.
        """
        pass

    def help(self):
        return "**futurama** - Responds with a futurama quote"
