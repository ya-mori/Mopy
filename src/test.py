from table import Table
from seed.rand_int_seed import RandIntSeed
from seed.pk_int_seed import PkIntSeed
from seed.enum_seed import EnumSeed 
from seed.rand_string_seed import RandStrSeed
from seed.rand_boolean_seed import RandBoolSeed
from seed.rand_date_seed import RandDateSeed

if __name__ == "__main__":

    users = Table(
        "users",
        id=PkIntSeed(),
        age=RandIntSeed(min=0, max=10),
        name=RandStrSeed(size=5),
        birth=RandDateSeed()
    )

    items = Table(
        "items",
        id=PkIntSeed(),
        price=RandIntSeed(min=0, max=100),
        user_id=users("id"),
        type=EnumSeed(["ONE", "TWO", "THERE"]),
        isActive=RandBoolSeed()
    )

    for query in users.create(10).to_sql():
        print(query)

    for query in items.create(10).to_sql():
        print(query)