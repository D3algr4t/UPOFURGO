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

class vehiculo(osv.Model):
    
    _name = 'vehiculo'
    _description = 'clase vehiculo'
    
    def _check_date_revision(self, cr, uid, ids):                    
        for clase in self.browse(cr, uid, ids):
                    
            if clase.fechaProximaRevision < str(datetime.now().date()): 
                return False
        return True  
    
    def _check_date_compra_revision(self, cr, uid, ids):                    
        for clase in self.browse(cr, uid, ids):        
            if clase.fechaAdquisicion > clase.fechaProximaRevision: 
                return False
        return True
 
    _columns = {
           'modelo': fields.char('Modelo', size=50,required=True),
           'name': fields.char('Matricula', size=128,required=True),
           'fechaAdquisicion': fields.datetime('Fecha adquisicion', required=True, autodate = True),
           'fechaProximaRevision': fields.datetime('Fecha Proxima Revision', required=True, autodate = True),
           
           'transportista_id': fields.many2many('transportista','transp_vehic_rel','dni','matricula','Transportistas'),
        }
    
    _constraints = [
                (_check_date_revision, '¡ La fecha de revision no puede ser anterior a hoy !' , [ 'fechaProximaRevision' ]),
                (_check_date_compra_revision, '¡ La fecha de revision no puede ser anterior a la de compra !' , [ 'fechaProximaRevision' ])
                ]
    
    _sql_constraints = [ ('id_vehiculo', 'unique (name)', 'Ya existe un vehiculo con esa matricula'),  ]