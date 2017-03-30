from handler_base import MessageHandler
import random


class Numbers(MessageHandler):
    def __init__(self):
        self.large_nums = [25, 50, 75, 100]
        self.small_nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
        self.numbers = list()
        self.target = 0

    def handle_message(self, raw_msg, user_email, username):
        """
            You don't need to modify any code in this method.
        """
        if "numbers" in str(raw_msg).lower():
            return self.get_numbers(raw_msg[8::].strip())
        return False

    def help(self):
        return "**numbers s:<number> l:<number>** - Returns numbers countdown game"

    def get_numbers(self, raw_msg):
        """
            This method should check if "raw_msg" contains the next parts of the numbers command.
            "raw_msg" should contain an "l:<number>" and "s:<number>", if it's missing one or both
            of them this method should return a failing string.
            The "l:<number>" can be before or after the "s:<number>"

            If "l:" is greater than 4, a fail string should be returned.
            If "s:" is greater than 6, a fail string should be returned.
            If the combined numbers of "l:" and "s:" are less than six,
            a fail string should be returned.
            If the combined numbers of "l:" and "s:" are greater than six,
            a fail string should be returned.

            If all is correct, this method should,
            choose "s:" random numbers from the "self.small_nums" list
            and "l:" random numbers from the self.large_nums" list.
            The numbers chosen from the lists can not be select more than then appear in the list,
            i.e. in "self.small" you can't choose 1 three times as it only appears twice.
            i.e. in "self.large" you can't choose any number twice as they only appear once.
            It should also return a "Target" 3 digit number to be reached.

            HINT: remove "pass" it's not needed.
            HINT: a lot of string manipulation in this one.
            HINT: this is the countdown numbers game.
            HINT: repeater.py will show you an example of how a the basic structure works.
            HINT: test_numbers_handler.py will assist you in this challenge, look at the "expected_response"
            strings for the fail strings to return.
            HINT: there is also a fully functional bot that you can use to see how the game works.
            HINT: there are methods that will help you below.

            :param raw_msg: Message containing the command and s: and l:
            :return: a string which is either a fail or a numbers game.
        """
        self.target = 0
        self.numbers = []
        pass

    def get_a_target(self):
        """ Returns a random number between 100 and 999. """
        return random.randint(100, 999)

    def get_num_from_string(self, string):
        """ Parses out the number from this string "s:<number>". """
        return int(string[2::])

    def choose_num_from_list(self, num, item_list):
        """ Will randomly choose "x" numbers from the list passed in, "item_list". """
        for i in range(num):
            random.shuffle(item_list)
            self.numbers.append(item_list.pop())
