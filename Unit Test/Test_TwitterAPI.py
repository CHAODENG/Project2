import unittest
import TwitterAPI as TAPI
import json
import sys

api = TAPI.get_authorization()
class Unit_Test(unittest.TestCase):
    def test_credentials(self):
        with open('my_credentials_info.json','r') as file:
            credentials = json.load(file)
        self.assertEqual(TAPI.get_my_credentials(tweets),credentials,"Error")
