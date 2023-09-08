from __future__ import annotations

import boto3

class SomeException(Exception):
    ...


class AException(SomeException):
    ...


class BException(SomeException):
    ...


class Service:
    _repo = []

    @classmethod
    def save(cls, number) -> int | SomeException:
        if number == 1:
            cls._repo.append(number)
            return 200
        return AException() # UnChecked Exception ?


class Controller:
    service = Service()

    def run(self, number: int):
        result = self.service.save(number)
        if isinstance(result, AException):
            raise result


if __name__ == '__main__':
    c = Controller()
    c.run(number=1)
