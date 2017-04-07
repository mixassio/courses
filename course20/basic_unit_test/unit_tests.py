#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import unittest


class TestMyModule(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setting up class')

    @classmethod
    def tearDownClass(cls):
        print('Tearing down class')

    @classmethod
    def setUp(cls):
        print('Setting up: ', cls)

    @classmethod
    def tearDown(cls):
        print('Tearing down')

    def test_some(self):
        self.assertEqual('1', '1')

    def test_module(self):
        self.assertNotEqual('1', 1)


if __name__ == '__main__':
    unittest.main()
