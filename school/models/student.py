from odoo import fields,models,api
from odoo.exceptions import ValidationError


class Student(models.Model):
	_name = 'student'

	_description = "Student Information"

	_rec_name ="name_student"

	name_student = fields.Char(string="Student Name",required=True)

	address_student = fields.Char(string="Address Student")

	age_student = fields.Integer(string="Age Student")

	gender_student = fields.Selection([('male','Male'),('female','Female')],string="Gender",default= 'male')

	class_student = fields.Char(string="Class student")

	email_student = fields.Char(string="Email Student")

	phone_number = fields.Char(string="Phone Number")

	image_student = fields.Binary(string="Image's Student")

	school_id = fields.Many2one('school',string='School Student')

	object_ids = fields.Many2many('object','object_school_rel','name_student','name')

	tien_hoc = fields.Char("tien hoc",compute='_tinh_hoc_phi')

	hien_thi = fields.Char("hello")

	len_mon_hoc = fields.Integer("So mon hoc",compute="_len_hoc_sinh")

	dem_tin_chi = fields.Integer("So tin chi",compute="_dem_tin_chi")

	year_of_bird = fields.Integer("Năm sinh",compute="_tinh_nam_sinh")

	curent_year = fields.Integer(default=fields.Datetime.today().year)

	tinder = fields.Text("Co the ket ban voi",compute="_ham_tinder")
	
 # sport_faverious = fields.Selection([('football','Football'),('voolayball','Voolayball')],string='Mon the thao ua thich')
	
	@api.depends('object_ids')
	def _tinh_hoc_phi(self):
		for r in self:
			r.tien_hoc = sum(r.object_ids.mapped('tin_chi'))*500

	@api.depends('object_ids')
	def _dem_tin_chi(self):
		for r in self:
			r.dem_tin_chi = sum(r.object_ids.mapped('tin_chi'))
	
	@api.constrains('object_ids')
	def _limit_object(self):
		for r in self: 
			if sum(r.object_ids.mapped('tin_chi')) > 5:
				raise ValidationError('da vuot qua so tin chi')
		
	@api.depends('object_ids')
	def _len_hoc_sinh(self):
		for r in self:
			r.len_mon_hoc = len(r.object_ids)

	@api.onchange('school_id')
	def _onchane_ahaha(self):
		if self.school_id:
			self.hien_thi = self.school_id.email_school

	@api.depends('age_student')
	def _tinh_nam_sinh(self):
		for r in self:
		 	r.year_of_bird = (r.curent_year) - (r.age_student)

	@api.constrains('age_student')
	def _check_year_of_bird(self):
		for r in self:
			if r.age_student < 10:
				raise ValidationError('ko hợp lệ ')
	

	