# -*- coding: utf-8 -*-
from odoo import models, fields
class TestModel(models.Model):
    _name = "test.model"
    name = fields.Char()