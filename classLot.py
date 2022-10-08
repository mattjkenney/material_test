from classPO import PO

class Lot(PO):

    def __init__(
        self,
        lot_qty = 1,
        lot_uom = 'each',
        received_qty = 1,
        lot_justification = 'standard',
        unit_justification = 'standard',
        po_qty = 1,
        po_uom = 'each',
        po_number = '',
        line_number = '',
        item_description = '',
        ):

        super().__init__(
            po_qty,
            po_uom,
            po_number,
            line_number,
            item_description,
            )
        
        self.lot_qty = lot_qty
        self.lot_uom = lot_uom
        self.received_qty = received_qty
        self.lot_justification = lot_justification
        self.unit_justification = unit_justification

    @property
    def lot_justification(self):
        return self._lot_justification
    
    @lot_justification.setter
    def lot_justification(self, lot_justification):
        t = lot_justification
        if t == 'standard':
            t = 'The quantity ordered is ' +\
                str(self.po_qty) + ' ' + self.po_uom + '.\n' +\
                'The quantity receieved is ' +\
                str(self.received_qty) + ' ' + self.po_uom +\
                ' in ' + str(self.lot_qty) + ' ' + self.lot_uom + '.\n' +\
                'Therefore, the lot quantity is ' +\
                str(self.lot_qty) + ' ' + self.lot_uom + '.'

        self._lot_justification = t

    @property
    def unit_justification(self):
        return self._unit_justification

    @unit_justification.setter
    def unit_justification(self, unit_justification):
        u = unit_justification
        if u == 'standard':
            u = self.lot_uom + ', as it is the smallest indivisible ' +\
                'item in the lot.'
        self._unit_justification = u
