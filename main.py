from Runner import runner
from algorithms.sort.select_sort import SelectSearch
from algorithms.manage import Manage


def search_starter(
    size: int = 0,
    is_random: bool = False,
    redis_name: str = None
):
    with runner(
        size,
        is_random,
        base=SelectSearch,
        redis_name=redis_name
    ) as session:
        yield session


if __name__ == '__main__':
    end = False
    while not end:
        check_db = input("Hello user, do you want to check"
                         " your previous journeys? (y/Y or n/N)")
        if check_db in ["y", "Y"]:
            print(Manage().show_dbs_list())
        algorithm_name = input("Input the name of your this magic journey: ")
        select = input("Do you want to generate the list or generate"
                       " random one for you? (g/G or r/R)")
        if select in ["g", "G"]:
            pass
        elif select in ["r", "R"]:
            list_size = input("What size of list you want?"
                              " (must greater than 0)")
            print("Generating the list for you...")
            starter = search_starter(int(list_size),
                                     is_random=True, redis_name=algorithm_name)
            res = next(starter)
            print(f"Before select sort is {res[0]}")
            print(f"After select sort is  {res[1]}")
            print(res[2])
            is_check = input("Do you want to check the status? (y/Y or n/N)")
            if is_check in ["y", "Y"]:
                print(res[3])
                print(f"cost total {len(res[3])} steps.")
            is_continue = input("Do you want to continue? (y/Y or n/N)")
            end = True if is_continue in ["n", "N"] else False
        else:
            print("invalided input, please try again.")

