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
from datetime import datetime

class empresatransportista(osv.Model):
    _name = 'empresa_transportista'
    _description = 'clase empresatransportista'
    
    def _check_date(self, cr, uid, ids):                    
        for clase in self.browse(cr, uid, ids):
                    
            if clase.finContrato < str(datetime.now().date()): 
                return False
        return True  
    
    _columns = {
            'cif': fields.char('CIF', size=50, required=True),
            'name': fields.char('Nombre', size=128),
            'direccion': fields.char('Direccion', size=128),
            'direccionSede': fields.char('Direccion Sede', size=128),
            'finContrato': fields.datetime('Fin Contrato', required=True, autodate=True),
            
            'transportista_id': fields.one2many('transportista', 'empresa_id', 'Empleados'),
        }
    
    _constraints = [
                    (_check_date, '¡ La fecha de fin de contrato no puede ser anterior a hoy !' , [ 'finContrato' ]),
                    ]
    
    _sql_constraints = [ ('id_empresa', 'unique (cif)', 'Ya existe ese CIF'), ]
