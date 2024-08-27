class InternalServerErrorException(Exception):
    def __init__(self, message: str = "Internal server error."):
        self.message = message

    def __str__(self):
        return self.message
