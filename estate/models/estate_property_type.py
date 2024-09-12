from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type"

    _sql_constraints = [
        (
            "unique_property_type_name",
            "UNIQUE(name)",
            "The property type name must be unique.",
        )
    ]

    name = fields.Char(string="Property Type", required=True)
