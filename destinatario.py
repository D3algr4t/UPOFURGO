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

class destinatario(osv.Model):
    
    _name = 'destinatario'
    _description = 'clase destinatario'
 
    _columns = {
           'dni': fields.char('DNI', size=50,required=True),
           'name': fields.char('Nombre', size=128),
           'direccion': fields.char('Direccion',size=128),
           'codigoPostal': fields.integer('Codigo postal'),
           'telefonoContacto': fields.char('Telefono contacto', size=13),
           
           'envio_id': fields.one2many('envio','destinatario_id', 'Envios'),
        }
    
    _sql_constraints = [ ('id_destinatario', 'unique (dni)', 'No puede haber dos destinatarios que tengan el mismo DNI'),  ]