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

class parteincidencia(osv.Model):
    
    _name = 'parte_incidencia'
    _description = 'clase parte_incidencia'
    
    def _check_date(self, cr, uid, ids):                    
        for clase in self.browse(cr, uid, ids):
                    
            if clase.fecha < str(datetime.now().date()): 
                return False
        return True  
    
    def _check_date_resolucion(self, cr, uid, ids):                    
        for clase in self.browse(cr, uid, ids): 
            if clase.fechaResolucion != None:       
                if clase.fechaResolucion < str(datetime.now().date()): 
                    return False
        return True
    
    def _check_date_notificacion_entrega(self, cr, uid, ids):                    
        for clase in self.browse(cr, uid, ids):   
            
            print(clase.fechaResolucion)
            if clase.fechaResolucion != None:         
                if clase.fecha > clase.fechaResolucion: 
                    return False
        return True
 
    _columns = {
           'name': fields.char('ID', size=64, required=True),
           'fecha': fields.datetime('Fecha', required=True, autodate = True),
           'descripcion': fields.char('Direccion', size=128),
           'fechaResolucion': fields.datetime('Fecha Resolucion'),
           'solucionFacilitada': fields.char('Telefono', size=128),
           
           'envio_id': fields.many2one('envio', 'Envio',required=True),
        }
    
    _constraints = [
                    (_check_date, '¡ La fecha de notificacion no puede ser anterior a hoy !' , [ 'fecha' ]),
                    (_check_date_resolucion, '¡ La fecha de resolucion de entrega no puede ser anterior a hoy !' , [ 'fechaResolucion' ]),
                    (_check_date_notificacion_entrega, '¡ La fecha de resolucion no puede ser anterior a la de notificacion !' , [ 'fechaResolucion' ])
                    ]
    
    _sql_constraints = [ ('id_incidencia', 'unique (name)', 'Ya existe una parte de Incidencia con ese ID'),  ]