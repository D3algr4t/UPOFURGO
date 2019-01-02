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

class proveedor(osv.Model):
    
    _name = 'proveedor'
    _description = 'clase proveedor'
    def _enviosTotal(self, cr, uid, ids, field, arg, context=None):
        res = {}

        for prov in self.browse(cr,uid,ids):
            res[prov.id] = len(prov.envio_id)
        return res  
 
    _columns = {
           'name': fields.char('Nombre', size=50),
           'direccion': fields.char('Direccion', size=128),
           'cif': fields.char('CIF', size=50, required=True),
           'telefono': fields.integer('Telefono', size=13),
           'envios_totales': fields.function(_enviosTotal, type='integer', string='Envios_totales', store = True),
           
           'envio_id': fields.one2many('envio','proveedor_id', 'Envios'),
        }
    
    _sql_constraints = [ ('id_proveedor', 'unique (cif)', 'Ya existe un proveedor con ese CIF'),  ]
    
    
    
    
    
    
