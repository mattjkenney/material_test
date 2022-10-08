def boolToBox(self, T_or_F):
    
    # Parameter 'T_or_F' must be a boolean input
    
    b = T_or_F
    if b == True:
        b = u'\U0001F5F9'
    elif b == False:
        b = u'\u2610'

    return b
