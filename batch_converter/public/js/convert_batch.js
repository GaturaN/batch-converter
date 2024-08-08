frappe.ui.form.on('Item', {
    refresh: function(frm) {
        frm.add_custom_button(__('Convert to Batch'), function() {
            frappe.prompt([
                {
                    label: 'Item Group',
                    fieldname: 'item_group',
                    fieldtype: 'Link',
                    options: 'Item Group'
                },
                {
                    label: 'Batch Number Series',
                    fieldname: 'batch_number_series',
                    fieldtype: 'Data'
                }
            ], function(values) {
                frappe.call({
                    method: 'batch_converter.batch_converter.doctype.item.convert_to_batch',
                    args: {
                        item_group: values.item_group,
                        batch_number_series: values.batch_number_series
                    },
                    callback: function(r) {
                        if (r.message) {
                            frappe.msgprint(__('Successfully converted items to batch'));
                        }
                    }
                });
            });
        });
    }
});
