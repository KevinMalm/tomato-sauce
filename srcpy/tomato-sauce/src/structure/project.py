import os
import pickle
from io import TextIOWrapper
from dataclasses import dataclass
from structure.control.settings import TomatoSettings
from structure.story.book import Book
from shared.types import String
from shared.util import into_file, from_file, strip_string


@dataclass
class TomatoProject:
    @dataclass
    class InitializationParameters:
        path: String
        title: String
        author: String

    @dataclass
    class ProjectMetaData:
        path: String
        file_name: String
        settings: TomatoSettings

    metadata: ProjectMetaData
    book: Book

    @staticmethod
    def new(config: InitializationParameters, settings: TomatoSettings):
        project = TomatoProject(
            metadata=TomatoProject.ProjectMetaData(
                path=config.path,
                file_name=String(strip_string(config.title.string)),
                settings=settings,
            ),
            book=Book.empty(title=config.title, author=config.author),
        )

        return project

    @staticmethod
    def init(metadata: ProjectMetaData, book: Book):
        return TomatoProject(metadata=metadata, book=book)

    @staticmethod
    def open(f: TextIOWrapper):
        return pickle.load(f)

    def save(self):
        with open(
            os.path.join(
                self.metadata.path.string,
                self.metadata.file_name.string,  # store it inside the lance-db folder :)
                self.metadata.file_name.string + ".tomato",
            ),
            "wb",
        ) as f:
            pickle.dump(self, f)

        with open(
            os.path.join(
                self.metadata.path.string,
                self.metadata.file_name.string,  # store it inside the lance-db folder :)
                self.metadata.file_name.string + ".yaml",
            ),
            "w",
        ) as f:
            into_file(f, self.metadata)
