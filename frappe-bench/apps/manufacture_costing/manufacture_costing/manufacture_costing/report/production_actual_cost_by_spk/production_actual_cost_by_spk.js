// Copyright (c) 2013, Bobzz and contributors
// For license information, please see license.txt

frappe.query_reports["Production Actual Cost by SPK"] = {
	"filters": [
		{
			"fieldname":"fiscal_year",
			"label": __("Fiscal Year"),
			"fieldtype": "Link",
			"options": "Fiscal Year",
			"reqd": 1,
			"width": "60px"
		}
	]
}
