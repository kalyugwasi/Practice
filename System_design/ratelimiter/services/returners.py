from limiter import rep_storage

def repo(client_name):
    return rep_storage.add_client(client_name)
