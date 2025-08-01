import logging

def say_hello():
    logging.basicConfig(level=logging.INFO)
    logging.info("Hello, world!")

say_hello()