def main():

    from classSample import SamplingPlan
    from classPO import PO
    from classLot import Lot

    po = PO(40,'bolts','12345','1','Bolt, 1/2"-13 x 1" Gr. 5"')
    lot = Lot(40, 'bolts', 40, **po.__dict__)
    sp = SamplingPlan(0.15,**lot.__dict__)

    return sp

sp = main()
print(sp.get_samples())
