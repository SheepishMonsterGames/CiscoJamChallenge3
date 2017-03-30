from abc import ABCMeta, abstractmethod


class MessageHandler(object):
    """
    An abstract class for message handlers
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def handle_message(self, raw_msg, user_email, username):
        """Decide if the message is meant for you, and handle it."""
        pass

    @abstractmethod
    def help(self):
        """Return a string that describes how the handler works."""
        pass
