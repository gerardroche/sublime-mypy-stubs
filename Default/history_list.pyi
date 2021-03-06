from typing import List, Tuple

import sublime


class JumpHistory:
    def __init__(self) -> None:
        ...

    def push_selection(self, view: sublime.View) -> None:
        ...

    def jump_back(self, active_view: sublime.View) -> Tuple[sublime.View, List[sublime.Region]]:
        ...

    def jump_forward(self, active_view: sublime.View) -> Tuple[sublime.View, List[sublime.Region]]:
        ...

    def remove_view(self, view_id: int) -> None:
        ...

    def generate_key(self) -> str:
        ...

    def clear_history_after_current(self) -> None:
        ...

    def trim_selections(self) -> None:
        ...

    def len(self) -> int:
        ...


def get_jump_history(window_id: int) -> JumpHistory:
    ...
