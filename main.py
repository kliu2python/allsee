from Runner import runner
from algorithems.search.search_base import SearchBase


def search_starter():
    with runner(
            base=SearchBase
    ) as session:
        yield session


if __name__ == '__main__':
    pass
