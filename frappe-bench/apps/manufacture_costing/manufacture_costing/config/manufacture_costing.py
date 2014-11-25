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
		}
	]
