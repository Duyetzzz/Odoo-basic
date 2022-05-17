from odoo import fields,models,api
from odoo.exceptions import ValidationError 


class Object(models.Model):
	_name = "object"
	_description = "Module object"

	name = fields.Char(string="id object",required=True)
	name_object = fields.Char(string="name object")
	name_teacher = fields.Char(string="name teacher")
	tin_chi = fields.Integer(string="So tin chi")
	
	students_ids = fields.Many2many('student','student_object_rel','name','name_student',string="Student")
	
	@api.constrains('students_ids')
	def _limit_student(self):
		for r in self:
			if len(r.students_ids) > 3:
				raise ValidationError('da vuot qua so hoc sinh')
