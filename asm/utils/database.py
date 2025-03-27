from asm.models import StudentModel

class Database:
    __data = {}

    @classmethod
    def load(cls):
        try:
            with open("database.txt", "r") as file:
                for line in file:
                    line = line.strip()

                    if not line:
                        continue

                    if line.startswith("[") and line.endswith("]"):
                        current_table = line[1:-1]
                        cls.__data[current_table] = []
                    elif current_table:
                        cls.__data[current_table].append(line)
        except Exception as e:
            print(f"An error occurred: {e}")

    @classmethod
    def save(cls):
        try:
            with open("database.txt", "w") as file:
                for table in cls.__data:
                    file.write(f"[{table}]\n")

                    for value in cls.__data[table]:
                        file.write(f"{value}\n")
        except Exception as e:
            print(f"An error occurred: {e}")

    @classmethod
    def create(cls, table_name, value):
        cls.__data[table_name].append(value)
        cls.save()

    @classmethod
    def read_all(cls, table_name) -> list:
        return cls.__data.get(table_name)