# Copyright (c) 2022, Saiyyam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MyErpDoc(Document):
		def validate(self):
			
					# Fetch Sales Invoice Item item through db.sql()
			# sqlData = frappe.db.sql(
			#    "select itemSale.item_code from `tabSales Invoice Item` itemSale inner join `tabSales Invoice` sales on itemSale.parent = sales.name where sales.posting_date between '2022-08-01' and '2022-12-19'",
			#                     as_dict=True)
			

					#/* Fetch Customer data*/
			# # sqlData = frappe.db.sql("""select customer.customer_name, customer.customer_group, customer.territory
			# 							from `tabCustomer` customer 
			# 							inner join
			# 							`tabSales Order` saleOrder on customer.name = saleOrder.customer where customer.customer_type = 'Company'""");


					#Use of DB API below
			#/* Set value in  valuation_rate through DB API*/
			# frappe.db.set_value("Item","001",{
			# 	"valuation_rate":21 
			# })

			# itemGroupList = frappe.db.get_list("Item", 
            #                 fields=['item_group']
            #     )
			# print(f'\n \n data : \n \n{itemGroupList}')
			#Use conditional operators in filter
			sqlData = frappe.db.get_list("MyErpDoc",filters = {'name':['!=', self.name]	
			}, fields=["name1", "number"])
			print(f'\n \n data : \n \n{sqlData}')

		# def before_insert(self):
		# 	frappe.msgprint(f'{self.name1} is successfully added.')
		
		# def on_update(self):
		# 	frappe.msgprint(f'Doc {self.name} is successfully updated.')
