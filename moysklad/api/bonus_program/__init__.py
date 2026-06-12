from moysklad.api.base import AsyncEndpoint, SyncEndpoint
from moysklad.models.bonus_program.transaction import BonusTransaction
from moysklad.models.bonus_program.program import BonusProgram

class AsyncBonusProgramAPI:
    def __init__(self, client):
        self.transaction = AsyncEndpoint[BonusTransaction](client, "entity/bonustransaction", BonusTransaction)
        self.program = AsyncEndpoint[BonusProgram](client, "entity/bonusprogram", BonusProgram)

class SyncBonusProgramAPI:
    def __init__(self, client):
        self.transaction = SyncEndpoint[BonusTransaction](client, "entity/bonustransaction", BonusTransaction)
        self.program = SyncEndpoint[BonusProgram](client, "entity/bonusprogram", BonusProgram)
