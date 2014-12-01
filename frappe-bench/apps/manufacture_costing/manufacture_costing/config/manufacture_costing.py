from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Production Actual Cost",
					"description": _("Summerize Production report"),
					"label": _("Production Closing Voucher")
				}
			]
		},
		{
			"label": _("Reports"),
			"icon": "icon-list",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Open Production Orders",
					"doctype": "Production Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Production Orders in Progress",
					"doctype": "Production Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Issued Items Against Production Order",
					"doctype": "Production Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Completed Production Orders",
					"doctype": "Production Order"
				},{
					"type": "report",
					"is_query_report": True,
					"name": "Production Actual Report by Closing Voucher",
					"doctype": "Production Actual Cost"
				},{
					"type": "report",
					"is_query_report": True,
					"name": "Production Actual Cost by SPK",
					"doctype": "Production Actual Cost"
				},{
					"type": "report",
					"is_query_report": True,
					"name": "Production Cost Report by Time",
					"doctype": "Production Actual Cost"
				}
				
			]
		}
	]
