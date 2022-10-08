from classLot import Lot

class SamplingPlan(Lot):
    global boolToBox
    
    from usefulTools import boolToBox

    def __init__(
        self,
        sampling_plan = '100%',
        reduce_for_destructive = False,
        sampling_justification = 'standard',
        sampling_method = 'Random Number Generator',
        lot_qty = 1,
        lot_uom = 'each',
        received_qty = 1,
        _lot_justification = 'standard',
        _unit_justification = 'standard',
        po_qty = 1,
        po_uom = 'each',
        po_number = '',
        line_number = '',
        item_description = '',
        ):

        super().__init__(
            lot_qty,
            lot_uom,
            received_qty,
            _lot_justification,
            _unit_justification,
            po_qty,
            po_uom,
            po_number,
            line_number,
            item_description,
            )
        
        self.sampling_plan = sampling_plan
        self.reduce_for_destructive = reduce_for_destructive
        self.sampling_justification = sampling_justification
        self.sampling_method = sampling_method

    def sampling_plan_boxes(self):
        # Parameter 'sampling_plan' must be an integer 1 - 3

        s = self.sampling_plan
        if s == '100%':
            bs = (True, False, False)
    
        elif s == 'normal':
            bs = (False, True, False)
        
        elif s == 'reduced':
            bs = (False, False, True)

        # 'boxes' is a tuple for (100%, Normal, Reduced)
        # sampling plan check boxes
        boxes = (boolToBox(bs[0]),
                 boolToBox(bs[1]),
                 boolToBox(bs[2]))

        return boxes
    
    def reduced_destructive_boxes(self):
        # Parameter 'is_reduced_destructive' must be a boolean input

        b = self.reduce_for_destructive
        if b == True:
            bs = (True, False)

        else:
            bs = (False, True)

        # 'boxes' is a tuple for Reduced Destructive: ("Yes", "No")
        # check boxes
        boxes = (boolToBox(bs[0]), boolToBox(bs[1]))

        return boxes

    def calculate_sampleQTY(self):
        # Determines sample quantity based on sampling plan
        
        from math import ceil

        sp = self.sampling_plan
        if sp == '100%':
            sq = self.lot_qty
        elif sp == 'normal':
            sq = ceil(round(self.lot_qty * 0.4,0))
        elif sp == 'reduced':
            sq = ceil(round(self.lot_qty * 0.1,0))
        elif type(sp) == float:
            sq = ceil(round(self.lot_qty * sp,0))

        return sq

    def get_samples(self):
        # Returns a list of random sample IDs based on the number of samples

        from random import randint

        n = self.lot_qty
        ls = [i for i in range(1, n + 1)]
        ss = []
        for i in range(self.calculate_sampleQTY()):
            t = ls.pop(randint(0, len(ls) -1))
            ss.append(t)
        ss.sort()

        return ss

    @property
    def sampling_justification(self):
        return self._sampling_justification

    @sampling_justification.setter
    def sampling_justification(self, sampling_justification):

        s = sampling_justification
        if s == 'standard':
            s = 'Reduced sampling plan is needed for the long time required ' +\
                'for dedication testing. Justification is based on the long ' +\
                'history of this vendor providing conforming and ' +\
                'homogenuous lots of this product.'

        self._sampling_justification = s
