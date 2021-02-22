from graphqlclient import GraphQLClient
from .ext.query_format import Querys as Q
from datetime import datetime


class User:
    def __init__(self, data, token):

        user = data["user"]
        self.json: dict = user
        "The whole given data in Json"

        self.name: str = user["name"]
        """The student name"""

        self.has_unread_discussions: bool = user["userSettings"]["unreadDiscussions"]
        """Return True if the client has unread messages. Else, return False"""

        self.student_class: str = user["studentClass"]["name"]
        """The class of the student"""

        informations = []
        for info in data["infos"]:
            informations.append(Info(info))
        self.messages: list[Info] = informations
        """Return a list of all messages"""

        self.__token = token
        """You shouldn't see this."""

        self.school = Etablishment(user["establishmentsInfo"][0])
        """Return informations about the school"""

        self.settings = Settings(user["userSettings"])
        """Return informations about the user's settings"""

        self.permissions = Authorizations(user["authorizations"])
        """Return user's permissions."""

    async def fetch_infos(self):
        client = GraphQLClient("http://127.0.0.1:21727/graphql")
        client.inject_token(self.__token, "Token")
        # return client.execute(Q.homework)


class Etablishment:
    def __init__(self, data):
        self.name: str = data["name"]
        self.address: str = data["address"][0]
        self.postal_code: str = data["postalCode"]
        self.city: str = data["city"]
        self.website: str = data["website"]


class Settings:
    def __init__(self, data):
        self.version: float = data["version"]
        self.theme: int = data["theme"]


class Authorizations:
    def __init__(self, data):
        self.create_discussions: bool = data["discussions"]
        self.teachers_discussions: bool = data["teachersDiscussions"]
        self.max_user_file_size: int = data["maxUserWorkFileSize"]
        self.max_school_file_size: int = data["maxEstablishmentFileSize"]
        self.print_file: bool = data["canPrint"]
        self.hice_class_parts: bool = data["hideClassParts"]
        self.edit_lessons: list = data["canEditLessons"]
        self.seeable_weeks: list = data["timetableVisibleWeeks"]


class Info:
    def __init__(self, data):
        self.id: str = data["id"]
        """the id of the information"""
        self.timestamp: int = int(data["date"] / 1000)
        """The timestamp ID when the info has been given"""
        self.date: datetime = datetime.fromtimestamp(self.timestamp)
        """When the info has been posted."""
        self.title: str = data["title"]
        """The title of the info"""
        self.author: str = data["author"]
        """The author name"""
        self.content: str = data["content"]
        """The content of the info"""
        self.html_content: str = data["htmlContent"]
        """The content in HTML"""

        files = []
        for file in data["files"]:
            files.append(File(file))
        self.files: list[File] = files
        """A list of class Files"""


class File:
    def __init__(self, data):
        self.id: str = data["id"]
        """The file ID"""
        self.name: str = data["name"]
        """The file name"""
        self.url: str = data["url"]
        """The URL to the file"""
