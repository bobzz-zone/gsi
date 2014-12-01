# Copyright (c) 2013, Bobzz and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cstr, flt
from frappe import _

def execute(filters=None):
	columns = get_columns()
	data = get_data_result(filters)
	return columns, data

def get_columns():
	return ["SPK:Data:100","Cutting Qty:Int:100","Cutting Total hours:Float:100","Cutting Cost:Float:200","Cutting Cost Average:Float:100","Stitching Qty:Int:100","Stitching Total hours:Float:100","Stitching Cost:Float:200","Stitching Cost Average:Float:100","Assembly Qty:Int:100","Assembly Total hours:Float:100","Assembly Cost:Float:200","Assembly Cost Average:Float:100","Monthly Cost:Float:100"]

def get_data_result(filters):
	#result = []
	result = frappe.db.sql("""SELECT car.kode_spk,sum(car.cqty),sum(car.ctime),sum(car.ccost),avg(car.ccost/car.cqty) as "cavg",sum(car.sqty),sum(car.stime),sum(car.scost),avg(car.scost/car.sqty) as "savg",sum(car.aqty),sum(car.atime),sum(car.acost),avg(car.acost/car.aqty) as "aavg",sum(car.mcost) from `tabProduction Actual Cost Record` car join `tabProduction Actual Cost` ca on car.parent=ca.name where ca.fiscal_year=%(fiscal_year)s group by car.kode_spk""",filters,as_list=1)
	
	return result
