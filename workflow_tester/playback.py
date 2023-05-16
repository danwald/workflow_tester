from collections import defaultdict
import typing
import dataclasses
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level='DEBUG', format='%(asctime)s - %(levelname)s - %(message)s')


@dataclasses.dataclass
class Cursor:
    recv: str = ''
    resp: str = ''


class Player:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.tape = self._load_tape(filename)
        self.head = defaultdict(int)

    def __str__(self) -> str:
        return f'Player loaded `{self.filename}` @ { {k:v for k,v in self.head.items()} }'

    @staticmethod
    def interaction_key(event: str, user: str) -> str:
        return f'{event}:{user}'

    def get_n_advance_interaction(self, event: str, user: str) -> typing.Optional[Cursor]:
        interaction = self.interaction_key(event, user)
        pos = self.head[interaction]
        self.head[interaction] += 1
        try:
            return self.tape[interaction][pos]
        except IndexError:
            return None

    def _load_tape(self, filename: str) -> defaultdict[str, typing.List[Cursor]]:
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
