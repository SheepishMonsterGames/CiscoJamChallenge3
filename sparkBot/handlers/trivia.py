import os
import requests
from handler_base import MessageHandler
import json

class Trivia(MessageHandler):

    def __init__(self, path_to_file="handlers/data_files/trivia_answer.json"):
        # Store the path_to_file for later use.
        self.answer_file = path_to_file
        with open(self.answer_file) as json_file:
            self.answer = (json.load(json_file))["text"]

    def handle_message(self, raw_msg, user_email, username):
        if "trivia question" in str(raw_msg).lower():
            return self.get_trivia_question()
        if "trivia answer" in str(raw_msg).lower():
            return self.get_trivia_answer()
        return False

    def help(self):
        return "**Trivia** - Returns a randomly pulled jeoprady question"

    def get_trivia_question(self):
        """
            This method should make a request to "http://jservice.io/api/random"
            for a random trivia question.
            The request comes back with a json object, within the object is a
            question, a title and an answer, the answer needs to be stored in a
            separate json file located at above "path_to_file".
            Before getting a new question this method should check if there is an answer
            in the json file. If there is return a string asking the user to get the answer.
            In the test_trivia_handler.py there is a pattern in test 100, you question string should
            use this pattern, but replace both ".*"

            HINT: remove "pass", it's a keyword that is not needed.
            HINT: request comes back as json.
            HINT: remember to save new answers to the json file.
            HINT: look at the json file to see what it expects.
            HINT: repeater.py will show you an example of how the basic structure works.
            HINT: test_trivia_handler.py will assist you in this challenge, look at the "expected_response"
            strings.
            HINT: there is also a fully functional bot that you can use to see how the game works.

            :return: a trivia question.
        """
        pass

    def get_trivia_answer(self):
        """
            This method should return the answer to the last question asked.
            If no answer exists a question wasn't asked and therefore
            this should be returned a prompt for the user to ask a queston.


            HINT: remove "pass", it's a keyword that is not needed.
            HINT: Return the answer if it's there.
            HINT: don't forget to clear the text from the json.
            HINT: test_trivia_handler.py will assist you in this challenge, look at the "expected_response"
            strings.
            HINT: there is also a fully functional bot that you can use to see how the game works.

            :return: a trivia answer or a string with no question.
        """
        pass

    def store_trivia_answer(self, response_answer):
        with open(self.answer_file, 'w') as json_file:
            json.dump(response_answer, json_file)
