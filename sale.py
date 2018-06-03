# This file is part of the sale_reference module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval, Not, Equal

__all__ = ['Sale']


class Sale:
    __metaclass__ = PoolMeta
    __name__ = 'sale.sale'

    def create_shipment(self, shipment_type):
        shipments = super(Sale, self).create_shipment(shipment_type)
        if not shipments:
            return
        to_write = []
        for shipment in shipments:
            shipment.customer_reference = self.reference
            shipment.save()
        return shipments
