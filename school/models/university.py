from odoo import fields,models

class University(models.Model):
	_name = "school"
	_inherit = "school"
	_description = "Module University"

	main_major = fields.Char(string="Main Major")
	