from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = "res.partner"

    has_phone = fields.Boolean(string=_("Has Phone"))

    @api.onchange("phone")
    def on_change_has_phone(self):
        for record in self:
            if record.phone:
                record.has_phone = True
            else:
                record.has_phone = False

            self.env["res.partner"].create(
                {"name": "Testing Create", "has_phone": True}
            )

            has_phone_contacts = self.env["res.partner"].search(
                [("has_phone", "=", False)]
            )