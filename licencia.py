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
from datetime import timedelta
import time


class licencia(osv.Model):
    _name = 'licencia'
    _description = 'clase licencia'
    
    def _check_date(self, cr, uid, ids):                    
        for clase in self.browse(cr, uid, ids):
                    
            if clase.fechaFinValidez < str(datetime.now().date()): 
                return False
        return True 
    
    def _check_anyos(self, cr, uid, ids):                    
        for clase in self.browse(cr, uid, ids):
                    
            if clase.anyosExperiencia < 0: 
                return False
        return True 
    
    def onchange_finValidez (self,cr,uid,ids): 
        fin = datetime.strptime(time.strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S").date() + timedelta(days=365)
        
        return { 'value': { 'fechaFinValidez' : str(fin) } }
    
    _columns = {
            'name': fields.char('ID', size=64, required=True),
            'tipo': fields.selection([
                ('pesado','Transportes Pesados'),
                ('ligero','Transportes Ligeros'),
                ('alta_movilidad','Alta Movilidad'),
                ],'Tipo de licencia',required=True),
            'fechaFinValidez': fields.datetime('Fecha validez', required=True, autodate = True),
            'anyosExperiencia': fields.integer('Anyos Experiencia', size=13),
            
            'transportista_id': fields.many2one('transportista', 'Transportista',required=True),
        }
    
    _constraints = [
                    (_check_date, '¡ La fecha de validez no puede ser anterior a hoy !' , [ 'fechaFinValidez' ]),
                    (_check_anyos, '¡ No puede tener un numero menor que 0 como experiencia !' , [ 'anyosExperiencia' ])
                    ]
    
    _sql_constraints = [ ('id_licencia', 'unique (name)', 'Ya existe una licencia con ese ID'),  ]