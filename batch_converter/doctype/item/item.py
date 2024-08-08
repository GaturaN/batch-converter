from __future__ import unicode_literals
import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def convert_to_batch(item_group, batch_number_series):
    if not item_group or not batch_number_series:
        frappe.throw(_("Item Group and Batch Number Series are required"))
    
    items = frappe.get_all('Item', filters={'item_group': item_group, 'has_batch_no': 0}, fields=['name', 'item_name'])
    for item in items:
        frappe.db.set_value('Item', item.name, {
            'has_batch_no': 1,
            'create_new_batch': 1,
            'batch_number_series': batch_number_series
        })
        
        batch_no = frappe.get_doc({
            'doctype': 'Batch',
            'item': item.name
        }).insert().name
        
        stock_entries = frappe.get_all('Stock Ledger Entry', filters={'item_code': item.name}, fields=['name'])
        for entry in stock_entries:
            frappe.db.set_value('Stock Ledger Entry', entry.name, 'batch_no', batch_no)
    
    return True
