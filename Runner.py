

def runner(size, is_random, base, redis_name):
    session = base(size, is_random, redis_name)

    return session

