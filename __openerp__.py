# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "UPOFURGO",
    "version": "1.0",
    "category": "Empresa",
    "description": "Empresa de transporte",
    "author": "Grupo 1",
    "depends": ["base"],
    "init_xml": [],
    'update_xml': [],
    'data' : [
              'envio_view.xml',
              'empresaTransportista_view.xml',
              'destinatario_view.xml',
              'transportista_view.xml',
              'vehiculo_view.xml',
              'licencia_view.xml',
              'proveedor_view.xml',
              'bulto_view.xml',
              'parteIncidencia_view.xml',
              'envio_workflow.xml'
            ],
    'demo_xml': ['upoFurgo_demo.xml'],
    'installable': True,
    'active': False,
}