from odoo import fields, models, api
from num2words import num2words


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    text_amount = fields.Char(string="Amount in letter", compute="_compute_text_amount")

    @api.depends('amount')
    def _compute_text_amount(self):
        if self.amount:
            withholding = self.amount - self.amount_withholding
            self.text_amount = num2words(withholding)
            self.text_amount = ' '.join(elem.capitalize() for elem in self.text_amount.split())
            return

