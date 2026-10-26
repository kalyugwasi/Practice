from ..storage import usr,streamer

def check_user(user_id):
    return usr.check_user(user_id)

def add_user(user_id,user_name):
    return usr.add_user(user_id,user_name)

def del_user(user_id):
    return usr.del_user(user_id)

def create_stream(user_id):
    return streamer.create_stream(user_id)

def check_stream(video_id):
    return streamer.check_stream(video_id)

def update_stream_status(video_id):
    return streamer.update_stream_status(video_id)

def del_stream(video_id):
    return streamer.del_stream(video_id)