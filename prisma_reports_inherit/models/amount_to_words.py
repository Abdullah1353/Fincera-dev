from odoo import fields, models, api
from num2words import num2words


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    text_amount = fields.Char(string="Amount in letter", compute="_compute_text_amount")

    @api.depends('amount')
    def _compute_text_amount(self):
        if self.amount and self.amount_withholding:
            total = self.amount + self.amount_withholding
            amount_total = total - self.amount_withholding
        elif self.amount:
            amount_total = self.amount
        else:
            amount_total = 0

        self.text_amount = num2words(amount_total)
        self.text_amount = ' '.join(elem.capitalize() for elem in self.text_amount.split())
        return


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def number_to_words(self, number):
        return num2words(number, lang='en').title()
