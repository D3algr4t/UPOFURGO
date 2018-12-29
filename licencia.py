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

class licencia(osv.Model):
    _name = 'licencia'
    _description = 'clase licencia'
    _columns = {
            'tipo': fields.selection([
                ('subcontratado','Subcontratado'),
                ('contratado','Contratado'),
                ('indefinido','Indefinido'),
                ],'Tipo de licencia'),
            'fechaFinValidez': fields.datetime('Fecha validez', required=True, autodate = True),
            'anyosExperiencia': fields.integer('Anyos Experiencia', size=13),
            
            'transportista_id': fields.many2one('transportista', 'Transportista'),
        }