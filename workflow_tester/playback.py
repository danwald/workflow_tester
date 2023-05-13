from collections import defaultdict
import typing
import dataclasses
import content
import logging

logger = logging.getLogger(__name__)

@dataclasses.dataclass
class Cursor:
    recv: str = ''
    resp: str = ''


class Player:
    def __init__(self, filename: str):
        self.tape = self._load_tape(filename)
        self.head = {}

    def _load_tape(filename) -> typing.Dict(str, typing.List(Cursor)):
        spool = defaultdict(list)
        with open(filename) as fp:
            for line in fp:
                record = line.split(',')
                if record[0].strip() == '#':
                    continue
                event_code, user_phone, *interaction = *record
                cursor = iter(interaction)
                for pos in cursor:
                    spool['f{event_code:user_phone}'].append(
                        Cursor(pos, next(cursor))
                    )
