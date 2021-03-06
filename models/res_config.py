# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Business Applications
#    Copyright (C) 2004-2012 OpenERP S.A. (<http://openerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import logging
_logger = logging.getLogger(__name__)

from openerp import api, fields, models


class InsuranceManagementConfiguration(models.TransientModel):
    _name = 'insurance_management.config.settings'
    _inherit = 'res.config.settings'

    module_insurance_management = fields.Boolean(
        string='Manage insurance contract',
        help='Allows to define the insurance contract for your customer')

    module_insurance_broker_management = fields.Boolean(
        string='Manage insurance broker contract',
        help='Allows to define the insurance contract broker')

    @api.onchange('module_insurance_management')
    def onchange_insurance_management(self):
        return {'value': {
            'module_insurance_management': self.module_insurance_management,
        }}

    @api.onchange('module_insurance_broker__management')
    def onchange_insurance_broker_management(self):
        return {'value': {
            'module_insurance_broker_management': self.module_insurance_broker_management,
        }}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
