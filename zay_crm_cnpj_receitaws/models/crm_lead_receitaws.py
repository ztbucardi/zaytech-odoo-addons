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

from openerp import models, fields, api, exceptions,_
import requests
import re

import logging
_logger = logging.getLogger(__name__)

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    partner_others_inf =  fields.Text("Outras informações")

    @api.one
    def cnpj_search(self):
        if not self.cnpj:
           raise exceptions.Warning(_('Preencha o CNPJ antes' ))

           return True

        else:
           cnpj_ws = re.sub(r'[.|/|-]',r'',self.cnpj)
           get_url_receitaws = 'http://receitaws.com.br/v1/cnpj/' + cnpj_ws
           obj_receitaws = requests.get(get_url_receitaws)
           data_receitaws = obj_receitaws.json()

           self.partner_name = data_receitaws['fantasia']
           self.legal_name = data_receitaws['nome']
           self.phone = data_receitaws['telefone']

           self.zip = re.sub(r'[.]',r'',data_receitaws['cep'])
           self.street = data_receitaws['logradouro']
           self.number = data_receitaws['numero']

           # adiciona dados de endereço com rel em db
           # TODO: carregar via consulta cep
           self.street2 = data_receitaws['bairro']
           self.street2 += ' - ' + data_receitaws['municipio']
           self.street2 += '/' + data_receitaws['uf']

           self.partner_others_inf = 'Outros dados da empresa: \ '

           return True

        return True


    @api.one
    def partner_add(self):
        return True
