from handler_base import MessageHandler


class MeaningOfLife(MessageHandler):
    def __init__(self):
        pass

    def handle_message(self, raw_msg, user_email, username):
        """
            Checks if the "raw_msg" has the command "meaning of life".
            If so it returns the meaning of life followed by the users name.
            Otherwise it must returns False.
            HINT: remove "pass", to begin as it's not needed.
            HINT: meaning of life for hitchhikers is their guide to the galaxy.
            HINT: repeater.py will show you an example of how a "handle_message" works.
            HINT: the test_meaningoflife_handler.py will assist you in completing
            this challenge, look at the expected output.
            HINT: there is also a fully functional bot that you can use to see how the game works.

            :param raw_msg: The message to preform operations on.
            :param user_email: email of the user who posted the command to the bot.
            :param username: username of user who posted the command to the bot.
            :return: String or False.
        """
        pass

    def help(self):
        return "**meaning of life** - Ask the bot what the meaning of life is"
