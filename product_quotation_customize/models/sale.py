# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class sale_order(models.Model):
	_inherit = 'sale.order'
	revision = fields.Char('Revision')
	sale_order_name_id = fields.Many2one('sale.order.name','Order Name')
	manual_sequence = fields.Char('Manual Input',required=True)
	
	@api.model
	def create(self, vals):
		if vals.get('name', 'New') == 'New':
			vals['name'] = self.env['ir.sequence'].next_by_code('sale.quotation.intipresisi') or 'New'
		sale_order_obj = super(sale_order, self).create(vals)
		print "\n\n=======",sale_order_obj.name,sale_order_obj.manual_sequence
		name = sale_order_obj.name
		latest_name = name.replace('XXX',sale_order_obj.manual_sequence)
		sale_order_obj.write({'name':latest_name})
		return sale_order_obj
	


class sale_order_name(models.Model):
	_name = 'sale.order.name'
	name = fields.Char('Name',required=True)
