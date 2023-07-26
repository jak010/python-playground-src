from __future__ import annotations

from typing import Final, final


@final
class Thing:
    def __init__(self, version: int):
        self.version = version


class Thing2:
    def __init__(self, version: int):
        self.version: Final = version


if __name__ == '__main__':
    t = Thing2(1)

    t.version = 2  # Not Occur Error
