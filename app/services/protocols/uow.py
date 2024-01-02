import typing


class UoW(typing.Protocol):
    def commit(self):
        pass

    def rollback(self):
        pass
