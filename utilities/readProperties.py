import configparser

config = configparser.RawConfigParser()
config.read('./Configurations/config.ini')

class ReadConfig():
#URL's
    @staticmethod
    def getApplicationUrl():
        url = config.get('base setup','baseURl')
        return url

#Users
    @staticmethod
    def getUserName():
        username = config.get('base setup', 'username')
        return username

    @staticmethod
    def getUserLocked():
        userlocked = config.get('base setup', 'userLocked')
        return userlocked

    @staticmethod
    def getUserProblem():
        userproblem = config.get('base setup', 'userProblem')
        return userproblem

    @staticmethod
    def getUserPerformance():
        userperformance = config.get('base setup', 'userPerformance')
        return userperformance

#Passwords
    @staticmethod
    def getWrongPassword():
        wrongpassword = config.get('base setup', 'wrongPassword')
        return wrongpassword

    @staticmethod
    def getPassword():
        password = config.get('base setup', 'password')
        return password