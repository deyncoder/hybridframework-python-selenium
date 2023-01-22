import configparser

# read config.ini
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig():
    @staticmethod  # to directly access using class name without creating any object
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getEmail():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
