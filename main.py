class Reader:

    def read(self):
        raise Exception("Abstract method")


class Writer:

    def write(self, data):
        raise Exception("Abstract method")


class Parser:

    def parse(self, data):
        raise Exception("Abstract method")


reader = Reader()
writer = Writer()
parser = Parser()
reader_data = reader.read()
print(reader_data)
parsed_data = parser.parse(reader_data)
print(parsed_data)
writer.write(parsed_data)

# modules reader, writer, parser