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

class envio(osv.Model):
    _name = 'envio'
    _description = 'clase envio'
    
    def _check_date_envio(self, cr, uid, ids):                    
        for clase in self.browse(cr, uid, ids):
                    
            if clase.fechaEnvio < str(datetime.now().date()): 
                return False
        return True  
    
    def _check_date_entrega(self, cr, uid, ids):                    
        for clase in self.browse(cr, uid, ids):        
            if clase.fechaEstimadaEntrega < str(datetime.now().date()): 
                return False
        return True
    
    def _check_date_envio_entrega(self, cr, uid, ids):                    
        for clase in self.browse(cr, uid, ids):        
            if clase.fechaEnvio > clase.fechaEstimadaEntrega: 
                return False
        return True
    
    def onchange_fechaEnvio (self,cr,uid,ids,fechaEnvio): 
        entrega = datetime.strptime(fechaEnvio,"%Y-%m-%d %H:%M:%S").date() + timedelta(days=3)
        
        return { 'value': { 'fechaEstimadaEntrega' : str(entrega) } }
    
    _columns = {
            'id_envio': fields.integer('ID',required=True),
            'tipoDeEnvio': fields.selection([
                ('express','Express'),
                ('lowCost','Lowcost'),
                ('largaDistancia','LargaDistancia'),
                ('especial','Especial'),
                ],'Tipo de Envio',required=True),
            'state': fields.selection([
                ('preparado','Preparado'),
                ('camino','En camino'),
                ('reparto','En reparto'),
                ('recibido','Recibido'),
                ],'Estado de Envio',required=True),
            'fechaEnvio': fields.datetime('Fecha Envio', required=True, autodate = True),
            'fechaEstimadaEntrega': fields.datetime('Fecha Estimada de  Entrega', required=True, autodate = True),
           
            'destinatario_id': fields.many2one('destinatario', 'Destinatario',required=True),
            'transportista_id': fields.many2one('transportista', 'Transportista',required=True),
            'proveedor_id': fields.many2one('proveedor', 'Proveedor'),
            'bulto_id': fields.one2many('bulto','envio_id', 'Bultos'),
            'parteIncidencia_id': fields.one2many('parte_incidencia','envio_id', 'Partes de Incidencia'),
        }
    
    _defaults = {'state':'preparado'}
    
    _constraints = [
                    (_check_date_envio, '¡ La fecha de envio no puede ser anterior a hoy !' , [ 'fechaEnvio' ]),
                    (_check_date_entrega, '¡ La fecha estimada de entrega no puede ser anterior a hoy !' , [ 'fechaEstimadaEntrega' ]),
                    (_check_date_envio_entrega, '¡ La fecha de entrega no puede ser anterior a la de envio !' , [ 'fechaEstimadaEntrega' ])
                    ]
    
    _sql_constraints = [ ('id_uniq', 'unique (id_envio)', 'Ya existe ese id'),  ]
