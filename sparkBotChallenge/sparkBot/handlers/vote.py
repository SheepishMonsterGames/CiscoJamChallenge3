# -*- coding: utf-8 -*-
import json
from handler_base import MessageHandler


class Vote(MessageHandler):
    def __init__(self, path_to_file="handlers/data_files/votes.json"):
        # load the json votes.
        self.path = path_to_file
        with open(self.path) as json_votes:
            self.data = json.load(json_votes)

    def handle_message(self, raw_msg, user_email, username):
        if "start_vote" in raw_msg.lower():
            raw_msg = raw_msg.lower().replace("start_vote", "", 1)
            return self.start_vote(raw_msg)
        if "end_vote" in raw_msg.lower():
            return self.end_vote()
        if "vote" in raw_msg.lower():
            raw_msg = raw_msg.lower().replace("vote", "", 1)
            return self.vote(raw_msg, user_email)
        return False

    def help(self):
        return "**Vote** - the voting command:<br>" \
               "1. start_vote - Defaulted to \"yes\" or \"no\", adding choices, \"maybe, hell no, ok\".<br>" \
               "2. vote <choice> - vote for your choice, can only vot once.<br>" \
               "3. end_vote - tallies the votes and retruns the results."

    def write_json(self):
        with open(self.path, 'w') as output:
            json.dump(self.data, output)

    def start_vote(self, options):
        """
            This method should start a vote, if a vote is not already in progress.
            If there is a vote in progress return a fail string
            If the user passes voting options use those and return a vote string with the options
            If the user passes 0 voting options use the default yes or no, and return a vote string with the options
            If the user passes 1 voting option, cancel the vote and return the correct fail string
            Remember to write the voting options to a json file.
            Users should be able to pass camelcase voting options, but they should be stored in lower case.
            example of how the json should look when a vote is in progress:
            {
                'options': ['yes', 'no'],
                'test_email@email.mail': 'yes',
                'email_test2@email.mail': 'no'
            }

            HINT: remove "pass", it's a keyword that is not needed.
            HINT: repeater.py will show you an example of how a the basic structure works.
            HINT: test_vote_handler.py will assist you in this challenge, look at the "expected_response"
            strings for the fail strings to return.
            HINT: there is also a fully functional bot that you can use to see how the game works.
            HINT: there are methods that will help you below.

            :return: voting options or a fail string.
            :param options: the voting options
        """
        pass

    def vote(self, vote, user_email):
        """
            This method should take a users vote.
            If the vote is one of the options list, record the vote and return a string saying so.
            If the vote is not one of the stored options return a fail string.
            If the user passes a blank vote i.e. "<bot_name> vote " return a fail string.
            If the user tries to vote and there is no vote in progress, return a fail string.
            If a user who has already voted tries to vote again, return a fail string.
            Users should be able to vote with camelcase valid options. i.e. YeS or nO
            example of how the json should look when a vote is in progress:
            {
                'options': ['yes', 'no'],
                'test_email@email.mail': 'yes',
                'email_test2@email.mail': 'no'
            }

            HINT: remove "pass", it's a keyword that is not needed.
            HINT: repeater.py will show you an example of how the basic structure works.
            HINT: test_vote_handler.py will assist you in this challenge, look at the "expected_response"
            strings for the fail strings to return.
            HINT: there is also a fully functional bot that you can use to see how the game works.
            HINT: there are methods that will help you below.

            :return: a fail string or a successful vote.
            :param vote: the users vote.
            :param user_email: email of the user.
        """
        pass

    def end_vote(self):
        """
            This method should end a vote that is in progress, it should count all the votes and
            list them out in a string. The string should also show which voting option won.
            If there is no vote in progress then a fail string is returned.
            If a vote is in progress and no votes are cast a fail string is returned.
            example of how the json should look when a vote is ended:
            {
                'options': []
            }

            HINT: remove "pass", it's a keyword that is not needed.
            HINT: repeater.py will show you an example of how the basic structure works.
            HINT: test_vote_handler.py will assist you in this challenge, look at the "expected_response"
            strings for the fail strings to return.
            HINT: there is also a fully functional bot that you can use to see how the game works.
            HINT: there are methods that will help you below.

            :return: a count of all the votes thus far or a fail string.
        """
        pass
