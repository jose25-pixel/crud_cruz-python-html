data = {}
current_id = 1

def get_next_id():
    global current_id
    record_id = str(current_id)
    current_id += 1
    return record_id