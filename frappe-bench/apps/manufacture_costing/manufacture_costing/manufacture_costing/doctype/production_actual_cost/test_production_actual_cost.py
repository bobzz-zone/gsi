# Copyright (c) 2013, Bobzz and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Production Actual Cost')

class TestProductionActualCost(unittest.TestCase):
	pass
