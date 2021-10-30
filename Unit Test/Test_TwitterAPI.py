import unittest
import TwitterAPI as TAPI
import json
import sys

tweets = TAPI.get_authorization()
class Unit_Test(unittest.TestCase):
    #def test_credentials(self):
    #    with open('my_credentials_info.json','r') as file:
    #        credentials = json.load(file)
    #    self.assertEqual(TAPI.get_my_credentials(tweets),credentials,"Error")
    def test_home_timeline(self):
        with open('my_home_timeline.json','r') as file:
            my_home_timeline = json.load(file)
        self.assertEqual(TAPI.get_home_timeline(tweets),my_home_timeline)
        
if __name__ == '__main__':
    print('Start my test')
    unittest.main()
