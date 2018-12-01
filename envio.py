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

from osv import osv
from osv import fields

class envio(osv.Model):
    _name = 'envio'
    _description = 'clase envio'
    _columns = {
            'id_envio': fields.integer('ID'),
            'tipoDeEnvio': fields.selection([
                ('express','Express'),
                ('lowCost','Lowcost'),
                ('largaDistancia','LargaDistancia'),
                ('especial','Especial'),
                ],'Tipo de Envio'),
            'estadoEnvio': fields.char('Estado de Envio',size=128),
            'fechaEnvio': fields.datetime('Fecha Envio', required=True, autodate = True),
            'fechaEstimadaEntrega': fields.datetime('Fecha Estimada de  Entrega', required=True, autodate = True),
           
            'destinatario_id': fields.many2one('destinatario', 'Destinatario'),
            'transportista_id': fields.many2one('transportista', 'Transportista'),
        }