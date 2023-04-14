# -*- coding: utf-8 -*-
from odoo import fields, models
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    name = fields.Char(string = "Name",required=True,active=True)
    _description = "Real Estate Property"
    description = fields.Text(active=True)
    _postcode = 21730
    postcode = fields.Char(active=True)
    _date_availability = 16/2/2022
    date_availability = fields.Date(copy=False,default=lambda self: self._default_date_availability(),active=True)
    _expected_price = 5000.00
    expected_price = fields.Float(string="Expected Price",required=True,active=True)
    _selling_price = 6000.00
    selling_price = fields.Float(readonly=True,copy=False,active=True)
    _bedrooms = 3
    bedrooms = fields.Integer(default=2,active=True)
    _living_area = 2
    living_area = fields.Integer(active=True)
    _facades = 2
    facades = fields.Integer(active=True)
    _garage = True
    garage = fields.Boolean(active=True)
    _garden = True
    garden = fields.Boolean(active=True)
    _garden_area = 2
    garden_area = fields.Integer(active=True)
    _garden_orientation = "Garden Orientation"
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('N','North'),('S','South'),
                   ('E','East'),('W','West')],
    help="Orientation of the property garden",active=True)
    
    _state = "State"
    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        string="Status",
        required=True,
        copy=False,
        default="new",
    )

    def _default_date_availability(self):
        return fields.Date.context_today(self) + relativedelta(months=3)