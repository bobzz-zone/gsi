# Copyright (c) 2013, Bobzz and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cstr, flt
from frappe import _

def execute(filters=None):
	columns = get_columns()
	mutasi = get_production(filters)
	selected = get_selected_spk(mutasi)
	request = get_request_qty(selected)
	saldo_awal = get_begining(filters,selected)
	data = get_result(request,saldo_awal,mutasi)
	return columns, data

def get_columns():
	return ["SPK:Data:100","Request Qty:Int:100","Early qty:Int:100","Early material cost:Currency:150","Early worker cost:Currency:150","Early monthly cost:Currency:150","Early total cost:Currency:150","Current production:Int:100","Current material cost:Currency:150","Current worker cost:Currency:150","Current monthly cost:Currency:150","Current total cost:Currency:150","Total production:Int:100","Total material cost:Currency:150","Total worker cost:Currency:150","Total monthly cost:Currency:150","total cost:Currency:150","HPP:Currency:150"]

def get_production(filters):
	#result = []
	result = frappe.db.sql("""SELECT car.kode_spk,sum(car.aqty),sum(car.ccost+car.scost+car.acost),sum(car.bahan),sum(car.mcost) from `tabProduction Actual Cost Record` car where car.date between %(from_date)s and %(to_date)s group by car.kode_spk order by car.kode_spk""",filters,as_list=1)
	
	return result

def get_request_qty(selected):
	result = frappe.db.sql("""SELECT kode_spk,qty from `tabProduction Order` where kode_spk IN ("{}") order by kode_spk""".format(selected),as_list=1)
	
	return result

def get_selected_spk(data):
	result=""
	for row in data:
		if result==0:
			result=row[0]
		else:
			result+=","+row[0]
	return result

def get_begining(filters,selected):
	#result = []
	result = frappe.db.sql("""SELECT car.kode_spk,sum(car.aqty),sum(car.ccost+car.scost+car.acost),sum(car.bahan),sum(car.mcost) from `tabProduction Actual Cost Record` car where car.date < "{}" and car.kode_spk IN ("{}") group by car.kode_spk order by car.kode_spk""".format(filters.get("from_date"),selected),as_list=1)
	
	return result

def	get_result(request,saldo_awal,mutasi):
	result = []
	creq=0
	cbeg=0
	totalReq=len(request)
	totalBeg=len(saldo_awal)
	for row in mutasi:
		reqQty=0
		if creq<totalReq and row[0]==request[creq][0]:
			reqQty=request[creq][1]
			creq+=1
		begQty=0
		begBahan=0
		begCost=0
		begMonthly=0
		begTotalCost=0
		if cbeg<totalBeg and row[0]==saldo_awal[cbeg][0]:
			begQty=saldo_awal[cbeg][1]
			begBahan=saldo_awal[cbeg][3]
			begCost=saldo_awal[cbeg][2]
			begMonthly=saldo_awal[cbeg][4]
			begTotalCost=begBahan+begCost+begMonthly
			cbeg+=1
		
		total_mutasi = row[2]+row[3]+row[4]
		result.append([row[0],reqQty,begQty,begBahan,begCost,begMonthly,begTotalCost,row[1],row[3],row[2],row[4],total_mutasi,begQty+row[1],begBahan+row[3],begCost+row[2],begMonthly+row[4],total_mutasi+begTotalCost,(total_mutasi+begTotalCost)/(begQty+row[1])])
	return result