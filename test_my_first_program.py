
from myfirstpythonprogram import hello_world_message

def test_simple():

    assert True

def test_hello_world_message_default():

    # Test default response
    msg = hello_world_message()
    assert msg == 'Hello World!'

def test_hello_world_message_custom():

    # Test custom resp
    msg = hello_world_message('ThaiPy')
    assert msg == 'Hello ThaiPy!'
