# Copyright (c) 2022, AiBizzHub LLC and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HDCustomer(Document):
    @staticmethod
    def default_list_data():
        columns = [
            {
                "label": "Name",
                "key": "name",
                "width": "17rem",
                "type": "Data",
            },
            {
                "label": "Domain",
                "key": "domain",
                "width": "24rem",
                "type": "Data",
            },
            {
                "label": "Created On",
                "key": "creation",
                "width": "8rem",
                "type": "Datetime",
            },
        ]
        rows = [
            "name",
            "image",
            "domain",
            "modified",
            "creation",
        ]
        return {"columns": columns, "rows": rows}
