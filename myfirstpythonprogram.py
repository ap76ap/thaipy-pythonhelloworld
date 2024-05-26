
# Function to help build message
def hello_world_message(name=None):

    if not name:
        name = 'World'

    msg = f'Hello {name}!'

    return msg

# Use function to write Hello messages
print(hello_world_message())
print(hello_world_message('ThaiPy'))

