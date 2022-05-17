from odoo import models,fields,api

class Tution_university(models.Model):
    _name = "tuition.university"
    _inherits = {'school':'tuition_student_ids'}

  
    tuition_university_ids= fields.Many2one('school','University Origanal',required=True)
    basic_tution = fields.Float('Basic Price',readonly=False)
  
    final_tution = fields.Float('Tiền học cộng thêm:',compute='_compute_final_tution')
    # student_ids_1 = fields.One2many('student','name_student',string="Name")
    
    class_type = fields.Selection([
        ('basic','Basic'),
        ('vip','VIP'),
    ],string='Class Type',default='basic')

    @api.depends('class_type')
    def _compute_final_tution(self):
      for r in self:
        if r.class_type == 'vip':
            r.final_tution = r.basic_tution  + 500
        else:
            r.final_tution = r.basic_tution 
      


   
            