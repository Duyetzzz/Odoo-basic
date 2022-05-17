from odoo import models,fields

class University_plus(models.Model):
	_name = "universiy_plus"
	_inherit = "school"
	_description = "Module about University"


	name_school_in = fields.Many2one('school','Original School',required=True)
	
	scholarships = fields.Boolean("Scholaerships",default = False)
	beautifull_campus = fields.Boolean("Beautiful campus",default = True)
	big_library = fields.Boolean("Big Library",default=True)
