from odoo import fields, models, api
import locale
from num2words import num2words


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    cheque_no = fields.Char(string="Cheque No")

    @api.depends('amount', 'amount_withholding')
    def _compute_total_amount(self):
        for payment in self:
            if payment.amount and payment.amount_withholding:
                total = payment.amount + payment.amount_withholding
                payment.total_amount = total - payment.amount_withholding
            elif payment.amount:
                payment.total_amount = payment.amount
            else:
                payment.total_amount = 0

    total_amount = fields.Monetary(string="Total Amount", compute='_compute_total_amount', store=True)

    def get_formatted_total(self):
        if self.amount and self.amount_withholding:
            total = self.amount + self.amount_withholding
        elif self.amount:
            total = self.amount
        formatted_total = '{:,.2f}'.format(self.total_amount)
        formatted_amount = '{:,.2f}'.format(total)
        formatted_amount_withholding = '{:,.2f}'.format(self.amount_withholding)
        record = {'formatted_total': f"{self.currency_id.symbol} {formatted_total}",
                  'formatted_amount': f"{self.currency_id.symbol} {formatted_amount}",
                  'formatted_amount_withholding': f"{self.currency_id.symbol} {formatted_amount_withholding}",

                  }

        return record

# boolean = fields.Boolean(string='Boolean', compute='cheque_compute', store=True)
#
# @api.depends('date')
# def cheque_compute(self):
#     for rec in self:
#         if 'sale' and 'purchase' and 'cash' and 'general' in rec.journal_id.type:
#             rec.boolean = True
#         else:
#             rec.boolean = False
