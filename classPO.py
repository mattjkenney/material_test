class PO():

    def __init__(
        self,
        po_qty = 1,
        po_uom = 'each',
        po_number = '',
        line_number = '',
        item_description = '',
        ):

        self.po_qty = po_qty
        self.po_uom = po_uom
        self.po_number = po_number
        self.line_number = line_number
        self.item_description = item_description
