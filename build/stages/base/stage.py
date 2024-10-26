from pathlib import Path
from argparse import ArgumentParser, Namespace

from .state import BuildState


class InterruptBuild(Exception):
    pass


class KeyNotFoundInConfigError(Exception):
    def __init__(self, key_path: str):
        self.key_path = key_path


class BuildStage:
    def __init__(self, state: BuildState, root_dir_path: Path, build_dir_path: Path, arguments: Namespace):
        self._state = state
        self._root_dir_path = root_dir_path
        self._build_dir_path = build_dir_path
        self.arguments = arguments

    @staticmethod
    def setup_args(parser: ArgumentParser):
        pass

    @property
    def state(self) -> BuildState:
        return self._state

    @property
    def root_dir_path(self) -> Path:
        return self._root_dir_path

    @property
    def build_dir_path(self) -> Path:
        return self._build_dir_path

    def task(self):
        raise NotImplementedError
