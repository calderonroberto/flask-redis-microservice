import app
import unittest
import json
from random import randint

mocked_value = randint(0,255)

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    #not needed now
    #def tearDown(self):

    def test_01_put_wrong_data(self):
        headers = [('Content-Type', 'application/json')]
        data ="{'wrong'}"
        headers.append( ('Content-Length', len(data)) )
        rv = self.app.put( '/sensor', headers=headers, data=data)
        self.assertEqual(rv.status_code, 400)

    def test_02_put_good_data(self):
        headers = [('Content-Type', 'application/json')]
        data = json.dumps({"value":mocked_value})
        headers.append( ('Content-Length', len(data)) )
        rv = self.app.put( '/sensor', headers=headers, data=data)
        rv_object = json.loads(rv.data)
        self.assertEqual(rv.status_code, 201)
        self.assertEqual(rv_object["value"], mocked_value )
        assert "last_updated" in rv_object
        assert "ttl" in rv_object
        self.assertEqual(rv_object["ttl"], 31104000)

    def test_03_get_put_value(self):
        rv = self.app.get('/sensor')
        rv_object = json.loads(rv.data)
        self.assertEqual(rv_object["value"], mocked_value )
        assert "last_updated" in rv_object
        assert "ttl" in rv_object
        self.assertEqual(rv.status_code, 200)


if __name__ == '__main__':
    unittest.main()
