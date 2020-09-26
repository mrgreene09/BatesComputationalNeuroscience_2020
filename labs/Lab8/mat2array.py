def loadmat(filename):
    import scipy.io as sio
        
    # this function calls the function '_check_keys' to cure all entries
    # which are still mat-objects

    data = sio.loadmat(filename, struct_as_record=False, squeeze_me=True)
    return _check_keys(data)

def _check_keys(dict):
    import scipy.io as sio
    # checks if entries in dictionary are mat-objects. If yes, 
    # todict is called to change them to nested dictionaries
    
    for key in dict:
        if isinstance(dict[key], sio.matlab.mio5_params.mat_struct):
            dict[key] = _todict(dict[key])
    return dict        

def _todict(matobj):
    import scipy.io as sio
    #A recursive function which constructs from matobjects nested dictionaries

    dict = {}
    for strg in matobj._fieldnames:
        elem = matobj.__dict__[strg]
        if isinstance(elem, sio.matlab.mio5_params.mat_struct):
            dict[strg] = _todict(elem)
        else:
            dict[strg] = elem
    return dict