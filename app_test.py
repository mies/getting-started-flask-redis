from app import app

import redis
import os
import unittest
import json

class CloudTestCase(unittest.TestCase):

  def setUp(self):
    r = redis.StrictRedis(host=os.getenv('WERCKER_REDIS_HOST', 'localhost'), port=6379, db=0)
    r.rpush('clouds','Altocumulus')
    r.rpush('clouds','Altostratus')
    r.rpush('clouds','Cumulonimbus')
    r.rpush('clouds','Nimbostratus')

  def tearDown(self):
    r = redis.StrictRedis(host=os.getenv('WERCKER_REDIS_HOST', 'localhost'), port=6379, db=0)
    r.flushdb()

  def test_index(self):
    tester = app.test_client(self)

    response = tester.get('/clouds.json', content_type='application/json')

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data, json.dumps(['Altocumulus', 'Altostratus',
      'Cumulonimbus', 'Nimbostratus']))


if __name__ == '__main__':
  unittest.main()
