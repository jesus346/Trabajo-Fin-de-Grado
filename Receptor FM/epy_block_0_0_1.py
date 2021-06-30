"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy
from numpy import angle, pi, complex64, float32
from gnuradio import gr

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, Frecuencia_Normalizada=75000):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Demodulador FM',   # will show up in GRC
            in_sig=[complex64],
            out_sig=[float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.frecuencia_normalizada = Frecuencia_Normalizada
        self.muestra_anterior = 1

    def work(self, input_items, output_items):
        
        for i in range(0,len(input_items[0])):
            """Derivador de Fase"""
            y = input_items[0][i]*self.muestra_anterior
            self.muestra_anterior = input_items[0][i].conjugate()
        	
            """Modulador"""
            output_items[0][i] = angle(y)/(2*pi*self.frecuencia_normalizada)
        	
        	
        return len(output_items[0])
