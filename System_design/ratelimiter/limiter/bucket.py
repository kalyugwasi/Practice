import time
pool = {}

def check_client(client_name,rpm):
    refill_rate = rpm/60
    if client_name not in pool:
        pool[client_name] = {
            'token':rpm,
            'last_check':time.monotonic()
            }
    print(pool)
    now = time.monotonic()
    elapsed = now - pool[client_name]["last_check"]
    toa = elapsed * refill_rate
    pool[client_name]['token'] += toa
    pool[client_name]['token'] = min(rpm, pool[client_name]['token'])
    pool[client_name]["last_check"] = now
    if pool[client_name]["token"] < 1:
        return None
    pool[client_name]["token"] -= 1
    
    return True
