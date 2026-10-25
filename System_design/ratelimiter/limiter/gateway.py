from . import auth_storage
from ..services import returners
from . import bucket


def handle_request(client_name):
    client = auth_storage.get_client(client_name)

    if client is None:
        auth_storage.add_client(client_name)
        client = auth_storage.get_client(client_name)
    
    if client is None:
        return "Unable to register guest"

    if not client["is_authorized"]:
        return "Unauthorized"
    
    allowed = bucket.check_client(client_name,client["rpm"])

    if not allowed:
        return "Rate limit exceeded"

    return returners.repo(client_name)
