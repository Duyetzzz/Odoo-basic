from odoo import fields, models, api
from odoo.exceptions import ValidationError


class School(models.Model):  # class school ke thua class Model trong models
	_name = "school"  # duoc yeu cau va xac dinh ten cua model trong he thong Odoo
	_description = "Module School"  # mo ta model
	_rec_name = "name_school"
	name_school = fields.Char(string="Name School", required=True) 
	email_school = fields.Char(string="Email School", help="email nha", index=True) 
	address_school = fields.Char(string="Address School") 
	image_school = fields.Image(string="Image School") 
	student_ids = fields.One2many('student', 'school_id', string="Student in school", store=True)
 
	@api.constrains('student_ids')
	def _limit_student(self):
		for r in self:
			if len(r.student_ids) > 3:
					raise ValidationError("vượt qua số sinh viên")
	
			

				
	