class ForbiddenException(Exception):
    def __init__(self, message = "Forbidden."):
        self.message = message

    def __str__(self):
        return self.message
