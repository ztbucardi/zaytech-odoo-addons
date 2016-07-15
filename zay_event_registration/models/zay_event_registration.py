# -*- coding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2016 - Leandro Augusto  <leandro@leandroaugusto.eti.br>       #
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).               #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU Affero General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU Affero General Public License for more details.                         #
#                                                                             #
# You should have received a copy of the GNU Affero General Public License    #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
###############################################################################

from openerp import models, fields, api

class ZayEventRegistration(models.Model):
  _inherit = 'event.registration'


  external_number = fields.Char(string='Codigo externo', size=8)
  campaign_others_ref = fields.Char(string='Ref',size=64 )
  notes = fields.Text(string='Notas')

  people_inf_cpf = fields.Char(string='CPF', size=12)
  people_inf_rg = fields.Char(string='RG', size=12)
  people_inf_nascimento = fields.Date(string='Data nascimento')

  tags = fields.Many2many(comodel_name='zay.event.registration.tags',
                          relation='zay_event_registration_tags_rel',
                          column1='registration_id',column2='tag_id', string="Tags")
