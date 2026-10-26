from ..middleware import gateway

def check_user(user_id):
    return gateway.check_usr(user_id)

def add_user(user_id,user_name):
    return gateway.add_user(user_id,user_name)

def del_user(user_id):
    return gateway.del_user(user_id)

def create_stream(user_id):
    return gateway.create_stream(user_id)

def check_stream(user_id):
    return gateway.check_stream(video)

def update_stream_status(video_id):
    return gateway.update_stream_status(video_id)

def del_stream(video_id):
    return gateway.del_stream(video_id)
    