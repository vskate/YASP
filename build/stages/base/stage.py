from pathlib import Path

from .state import BuildState


class BuildConfigError(Exception):
    def __init__(self, message: str):
        self.message = message


class BuildStage:
    def __init__(self, state: BuildState, build_dir_path: Path):
        self._state = state
        self._build_dir_path = build_dir_path

    @property
    def state(self) -> BuildState:
        return self._state

    @property
    def build_dir_path(self) -> Path:
        return self._build_dir_path

    def task(self) -> bool:
        """
        :returns: a boolean which indicates whether the task completed successfully and the next stage can be run.
        """
        raise NotImplementedError
