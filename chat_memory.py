memory = {}

def store(user_id, message):
    if user_id not in memory:
        memory[user_id] = []
    
    memory[user_id].append(message)

    # keep last 3 messages
    memory[user_id] = memory[user_id][-3:]


def get_history(user_id):
    return memory.get(user_id, [])