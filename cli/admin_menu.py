from getpass4 import getpass
from dotenv import load_dotenv
import os

load_dotenv()

def adminMenu():
    print('welcome back admin')


def adminLogin():
    password=getpass('Enter your password : ')