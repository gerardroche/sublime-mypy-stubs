g_clipboard_history = ...  # type: ClipboardHistory


class ClipboardHistory:
    def __init__(self) -> None: ...
    def push_text(self, text: str) -> None: ...