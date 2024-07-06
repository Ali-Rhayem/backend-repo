import yaml

class Server:
    def __init__(self, config):
        self.config = config

    def start(self):
        if self.config['ServerIPAddress'] == '127.0.0.1':
            print("Server is running on localhost")

if __name__ == "__main__":
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    server = Server(config)
    server.start()
