from odoo import _, fields
from odoo.exceptions import UserError


def check_date(date):
    """
    Check if the date is in the future and raise a UserError if it is.
    :param date: datetime
    :return: None
    :raise: UserError if date is in the future
    """
    now = fields.Datetime.now()
    if date and date > now:
        raise UserError(_("You can not process an actual movement date in the future."))
