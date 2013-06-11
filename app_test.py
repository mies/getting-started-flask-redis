from app import app

import redis
import os
import unittest
import json

class CloudTestCase(unittest.TestCase):

  def setUp(self):
    app.redis.rpush('clouds','Altocumulus')
    app.redis.rpush('clouds','Altostratus')
    app.redis.rpush('clouds','Cumulonimbus')
    app.redis.rpush('clouds','Nimbostratus')

  def tearDown(self):
    app.redis.flushdb()

  def test_clouds(self):
    tester = app.test_client(self)

    response = tester.get('/clouds.json', content_type='application/json')

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data, json.dumps(['Altocumulus', 'Altostratus',
      'Cumulonimbus', 'Nimbostratus']))

if __name__ == '__main__':
  unittest.main()
