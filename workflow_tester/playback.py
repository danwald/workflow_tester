from collections import defaultdict
import typing
import dataclasses
import logging
import constants  # noqa F401

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class Cursor:
    recv: str = ''
    resp: str = ''


class Player:
    def __init__(self, filename: str):
        self.tape = self._load_tape(filename)
        self.head = defaultdict(int)

    @staticmethod
    def interaction_key(event, user) -> str:
        return f'{event}:{user}'

    def get_n_advance_interaction(self, event, user) -> typing.Optional[Cursor]:
        interaction = self.interaction_key(event, user)
        pos = self.head[interaction]
        self.head[interaction] += 1
        try:
            return self.tape[interaction][pos]
        except IndexError:
            return None

    def _load_tape(self, filename) -> defaultdict[str, typing.List[Cursor]]:
        spool = defaultdict(list)
        with open(filename) as fp:
            for line in fp:
                record = line.split(',')
                logger.debug('Processing: "%s"', record)
                if record[0].strip() == '#':
                    continue
                event_code, user_phone, *interaction = record
                if len(interaction) % 2:
                    logger.error(
                        'Invalid script. Not paired sequenece (%s:%s %s)',
                        event_code, user_phone, interaction
                    )
                    continue
                cursor = iter(interaction)
                for pos in cursor:
                    spool[self.interaction_key(event_code, user_phone)].append(
                        Cursor(pos.strip(), (next(cursor)).strip())
                    )
        return spool
