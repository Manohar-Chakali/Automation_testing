import configparser
import os

class Read_Commondata:
    config_path = os.path.join(os.path.abspath(os.curdir)+"\\configurations\\config.ini")
    config = configparser.RawConfigParser()
    config.read(config_path)
    @staticmethod
    def get_App_url():
        url = Read_Commondata.config.get('commonData','baseUrl')
        return  url

    @staticmethod
    def get_useremail():
        email = Read_Commondata.config.get('commonData','email')
        return  email

    @staticmethod
    def get_userpassword():
        password = Read_Commondata.config.get('commonData','password')
        return password
