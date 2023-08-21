from odoo import fields, models, api
import locale
from num2words import num2words


class AccountMove(models.Model):
    _inherit = 'account.move'

    def total_credit_compute(self):
        for record in self:
            credit_sum = 0
            debit_sum = 0
            for line in record.line_ids:
                credit_sum = credit_sum + line.credit
                debit_sum = debit_sum + line.debit
            record.total_credit = credit_sum
            record.total_debit = debit_sum
            print(record.total_credit)

    total_credit = fields.Monetary(string="Total Debit", store=True, readonly=True)
    total_debit = fields.Monetary(string="Total Credit", store=True, readonly=True)

    def get_credit_total(self):
        self.total_credit_compute()
        formatted_total = '{:,.2f}'.format(self.total_credit)
        return f"{formatted_total}"

    def get_debit_total(self):
        formatted_total = '{:,.2f}'.format(self.total_debit)
        return f"{formatted_total}"

    @api.depends('total_credit')
    def _compute_text_amount(self):
        if self.total_credit:
            self.text_amount_credit = num2words(self.total_credit)
            self.text_amount_credit = ' '.join(elem.capitalize() for elem in self.text_amount_credit.split())
            return

    text_amount_credit = fields.Char(string="Amount in letter", compute="_compute_text_amount")
