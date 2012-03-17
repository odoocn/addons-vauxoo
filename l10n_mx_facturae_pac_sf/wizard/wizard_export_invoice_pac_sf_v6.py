# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2011 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
############################################################################
#    Coded by: moylop260 (moylop260@vauxoo.com)
#    Coded by: isaac (isaac@vauxoo.com)
#    Financed by: http://www.sfsoluciones.com (aef@sfsoluciones.com)
############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import fields, osv
import wizard
import netsvc
import pooler
import time
import base64
import StringIO
import csv
import tempfile
import os
import sys
import codecs
import xml.dom.minidom
from datetime import datetime, timedelta
from tools.misc import ustr
import time


class wizard_export_invoice_pac_sf_v6(osv.osv_memory):
    _name='wizard.export.invoice.pac.sf.v6'

    def _get_invoice_id(self, cr, uid, data, context = {}):
        res = {}
        invoice_obj = self.pool.get('account.invoice')
        res = invoice_obj._get_file(cr, uid, data['active_ids']) 
        file_xml = res['file']
        return file_xml
        
    def upload_to_pac(self, cr, uid, ids, context ={}):
        res = {}
        invoice_obj = self.pool.get('account.invoice')
        res = invoice_obj._upload_ws_file(cr, uid, context['active_ids'])
        self.write(cr, uid, ids, {'message': res['msg'] }, context=None)
        return True
  
    _columns = {
        'file': fields.binary('File', readonly=True),
        'message': fields.text('text'),
    }

    _defaults= {
        'message': 'Seleccione el botón Subir Factura para exportar al PAC',
        'file': _get_invoice_id,
    }

wizard_export_invoice_pac_sf_v6()

