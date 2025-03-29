class Model():
    def __init__(self, table_name: str):
        self.table_name = table_name

    def __str__(self) -> str:
        raise NotImplementedError

    def parse_from_string(self, string):
        """
            Parse a string into a model object. This method should be overridden in subclasses.

            Args:
                string (str): The string to parse.

            Returns:
                Model: The parsed model object.
        """

        raise NotImplementedError