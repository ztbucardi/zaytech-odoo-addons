# -*- coding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2016 - Leandro Augusto  <leandro@leandroaugusto.eti.br>       #
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

{
    'name': "Zaytech / CRM - Webservice receitaws.com.br",

    'category': 'Custom',
    'version': '0.4',
    "license": "AGPL-3",
    'website': "http://www.leandroaugusto.eti.br",
    'author': "Leandro Augusto <leandro@leandroaugusto.eti.br>",
    'contributors': ['Leandro Augusto <leandro@leandroaugusto.eti.br>'],
    'summary': """Modulo que adiciona a funcao de consulta CNPJ""",
    'description': """
        Este modulo adiciona a funcao de consultar os dados da empresa via
        ReceitaWS.com.br no formulario de Oportunidade 
        """,

    'depends': ['zay_crm_base' ],
    'data': [
        'view/crm_oppor_receitaws.xml',
    ],

    'installable': True,
    'auto_install': True,
}
