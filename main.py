from classes.ITDashboardGovReader import ITDashboardGovReader as Reader
from classes.Parser import Parser
from classes.Writer import Writer

reader = Reader()
writer = Writer()
parser = Parser()
reader_data = reader.read()
print(reader_data)
parsed_data = parser.parse(reader_data)
print(parsed_data)
writer.write(parsed_data)
