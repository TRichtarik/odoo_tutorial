from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    # Basic Information
    name = fields.Char(string="Property Name", required=True)
    description = fields.Text(string="Description")
    active = fields.Boolean(string="Active", default=True)
    
    # Location Details
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(
        string="Available From", copy=False,
        default=lambda self: fields.Date.add(fields.Date.today(), months=3)
    )
    
    # Pricing Details
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price", readonly=True, copy=False)
    
    # Property Features
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        string="Garden Orientation"
    )
    
    # Sales Information
    buyer_id = fields.Many2one('res.partner', string="Buyer", copy=False)
    salesperson_id = fields.Many2one(
        'res.users', string="Salesperson", default=lambda self: self.env.user
    )
    
    # Tags and Offers
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offers")
    
    # Property Type
    property_type_id = fields.Many2one('estate.property.type', string="Property Type")
    
    # State Management
    state = fields.Selection(
        [
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled')
        ], 
        string="State", required=True, copy=False, default='new'
    )
