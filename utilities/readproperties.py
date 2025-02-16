import configparser
import os

from xdist.remote import config


class Read_Commondata:
    config = configparser.RawConfigParser()
    config.read(os.path.abspath(os.curdir)+"\\configurations\\config.ini")
    @staticmethod
    def get_App_url():
        url = config.get('commonData','baseUrl')
        return  url

    @staticmethod
    def get_useremail():
        email = config.get('commonData','email')

    @staticmethod
    def get_userpassword():
        password = config.get('commonDtata','password')
