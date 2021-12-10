from .HTTPReader import HTTPReader


class ITDashboardGovReader(HTTPReader):

    def __init__(self):
        super().__init__("https://itdashboard.gov/")
