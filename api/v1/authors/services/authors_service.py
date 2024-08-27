class AuthorsService:
    @staticmethod
    def get_authors():
        """
        Returns a list of dictionaries representing authors.

        :return: A list of dictionaries, where each dictionary represents an author.
                 Each dictionary has two keys: "id" and "name", both with corresponding values.
        :rtype: list
        """
        return [
            {
                "id": 1,
                "name": "Author 1",
            },
            {
                "id": 2,
                "name": "Author 2",
            },
            {
                "id": 3,
                "name": "Author 3",
            },
        ]