import os
from typing import List
import interface.routine as Routines

from io import TextIOWrapper
from .llm import LargeLangueModelInterface, init_llm
from .db import VectorDatabaseInterface
from .db.constants import VectorTable
from .neutral_file import set_interface
from .prompt import PromptInterface, PromptRepository, PromptTag
from structure import TomatoProject, TomatoSettings
from structure.error import FileLoadError
from result import Result, Ok, Err


class TomatoInterface:
    project: TomatoProject

    database: VectorDatabaseInterface
    llm: LargeLangueModelInterface
    _last_prompter: PromptTag = None
    prompters: dict[PromptTag, PromptInterface]

    def __init__(
        self,
        project: TomatoProject,
        database: VectorDatabaseInterface,
        llm: LargeLangueModelInterface,
    ):

        self.project = project
        self.database = database
        self.llm = llm
        # Register a global Embedding Function
        Routines.register_llm(self.llm)
        # Build the Database tables with Global Function
        Routines.init_database(self.database)
        # Build Prompt Objects
        self.rebuild_prompts()
        # Set Global Reference
        set_interface(self)

    def save(self):
        self.project.save()
        return self

    def chapter(self):
        return Routines.ChapterRoutine(
            self.project.book,
            self.project.metadata.path,
            self.database,
            self.llm,
        )

    def character(self):
        return Routines.EntityRoutine(
            self.project.book,
            VectorTable.CHARACTER,
            Routines.EntityRoutine.CRUD(
                lambda: [x[1] for x in self.project.book.characters.items()],
                self.project.book.add_character,
                self.project.book.update_character,
                self.project.book.delete_character,
            ),
            self.database,
            self.llm,
        )

    def location(self):
        return Routines.EntityRoutine(
            self.project.book,
            VectorTable.LOCATION,
            Routines.EntityRoutine.CRUD(
                lambda: [x[1] for x in self.project.book.locations.items()],
                self.project.book.add_location,
                self.project.book.update_location,
                self.project.book.delete_location,
            ),
            self.database,
            self.llm,
        )

    def rebuild_prompts(self):
        self.prompters = {}
        for tag, config in PromptRepository.prompts.items():
            self.prompters[tag] = config.builder(config.template, self.database)

    def prompter(self, tag: PromptTag) -> PromptInterface:
        self._last_prompter = tag
        return self.prompters[tag]

    def last_references(self) -> Result[PromptInterface.PriorContext, str]:
        if self._last_prompter is None or self._last_prompter not in self.prompters:
            return Err("Mismatch, empty LLM History")
        return Ok(self.prompters[self._last_prompter].context)

    @staticmethod
    def new(config: TomatoProject.InitializationParameters, settings: TomatoSettings):
        if os.path.exists(config.path.string):
            raise FileLoadError(
                config.path.string,
                "TomatoInterface.new()",
                f"Project {config.title} already exists under {config.path}",
            )
        os.makedirs(config.path.string)
        project = TomatoProject.new(config, settings)
        database = VectorDatabaseInterface.init(project.metadata)
        llm = init_llm(project.metadata)
        return TomatoInterface(project, database, llm).save()

    @staticmethod
    def open(f: TextIOWrapper):
        project: TomatoProject = TomatoProject.open(f)
        project.book.align()
        database = VectorDatabaseInterface.init(project.metadata)
        llm = init_llm(project.metadata)
        return TomatoInterface(
            project=project,
            database=database,
            llm=llm,
        )
