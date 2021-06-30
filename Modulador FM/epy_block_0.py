"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy
from numpy import float32,complex64,pi,exp
from gnuradio import gr

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, frecuencia_normalizada=0.5):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Modulador FM',   # will show up in GRC
            in_sig=[float32],
            out_sig=[complex64]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.frecuencia_normalizada = frecuencia_normalizada
        self.muestra_anterior = 0

    def work(self, input_items, output_items):
    
        """Integrador y Modulador"""
        for i in range(0,len(input_items[0])):
        	
        	"""Integramos"""
        	ys = self.muestra_anterior + input_items[0][i]
        	self.muestra_anterior = ys
        	"""Modulador"""
        	output_items[0][i] = exp(1j*2*pi*self.frecuencia_normalizada*ys)
        	
        return len(output_items[0])
