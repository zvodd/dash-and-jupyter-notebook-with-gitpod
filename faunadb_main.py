from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
from dotenv import dotenv_values
from munch import AutoMunch
from pprint import pprint

cfg = AutoMunch(dotenv_values())

# pprint(cfg)
# exit()

fdb = FaunaClient(secret=cfg.FAUNASECRET)

if __name__ == "__main__":
    indexes = fdb.query(q.paginate(q.collections()))
    pprint(indexes)