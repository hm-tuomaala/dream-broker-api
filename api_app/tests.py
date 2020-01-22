from django.test import TestCase
import requests
import json

class CurlTestCase(TestCase):
    
    def test_given_curl(self):
        url = 'http://localhost:8000/analyze'
        payload1 = {"text": "hello 2 times  "}

        res1 = {
            "textLength":{"withSpaces":15,"withoutSpaces":11},
            "wordCount":3,
            "characterCount":[{"e":2},{"h":1},{"i":1},{"l":2},{"m":1},{"o":1},{"s":1},{"t":1}]
        }

        r1 = requests.post(url, json=payload1)

        self.assertEqual(json.loads(r1.text), res1)



    def test_empty_text(self):
        url = 'http://localhost:8000/analyze'
        payload2 = {"text": ""}

        res2 = {
            "textLength":{"withSpaces":0,"withoutSpaces":0},
            "wordCount":0,
            "characterCount":[]
        }

        r2 = requests.post(url, json=payload2)

        self.assertEqual(json.loads(r2.text), res2)



    def test_only_spaces(self):
        url = 'http://localhost:8000/analyze'
        payload3 = {"text": "   "}

        res3 = {
            "textLength":{"withSpaces":3,"withoutSpaces":0},
            "wordCount":0,
            "characterCount":[]
        }

        r3 = requests.post(url, json=payload3)

        self.assertEqual(json.loads(r3.text), res3)



    def test_text_with_numbers(self):
        url = 'http://localhost:8000/analyze'
        payload4 = {"text": "123 abc 123"}

        res4 = {
            "textLength":{"withSpaces":11,"withoutSpaces":9},
            "wordCount":3,
            "characterCount":[{"a":1},{"b":1},{"c":1}]
        }

        r4 = requests.post(url, json=payload4)

        self.assertEqual(json.loads(r4.text), res4)
