import yaml
import os

class Server:
    def __init__(self, config):
        self.config = config

    def start(self):
        if self.config['ServerIPAddress'] == '127.0.0.1':
            print("Server is running on localhost")
        else:
            print("error: Server is not running on localhost")

if __name__ == "__main__":
    config_path = os.path.join(os.path.dirname(__file__), '../config.yaml')
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    server = Server(config)
    server.start()
