##################################################################
#
#   This is the measure loop, which communicates with the external ADC
#   The program measures the every 100ms channel 1 and sends every sec.
#   ...over console "stdout" the value.
#
#   Note:   - This files still contains many unsused variables, that can be deleted.
#           - This file only reads only channel 1, the file has to be adopted to work
#               ...with more than one channels, also the communication with UI has to
#               ...be improved   
#
#   Author: Andreas Müller (Github: aragon0013)
#
# Copyright (C) 2025 Andreas Müller

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
##################################################################


import time
import sys
import signal
import select
import csv
import ADC_code.ADS1263 as ADS1263

def handle_sigterm(signum, frame):
    print("SIGTERM erhalten, sauber beenden...", flush=True)
    measure["running"] = False

measure = {"running":True}
counter = 0
no_of_measurements_p_cycle = 10
cache = {}


y_measure_values = []
x_measure_nr = []

# müssen wir noch messen
REF = 5.21

signal.signal(signal.SIGTERM, handle_sigterm)
sys.stdout.write("initialize sensor program...")
sys.stdout.flush()


try:
    ADC = ADS1263.ADS1263()

    if (ADC.ADS1263_init_ADC1('ADS1263_100SPS') == -1):
        exit()
    ADC.ADS1263_SetMode(0)
    channel2read = [0]
    for channel in channel2read:
        cache[channel] = 0
    time.sleep(2)

    while measure["running"]:
        '''
        sys.stdout.write("__________________\n")
        sys.stdout.write(f"Timestamp:{counter}\n")
        sys.stdout.write("sensor01:pH_data\n")
        sys.stdout.write("sensor02:conductivity_data\n")
        sys.stdout.write("sensor03:temperature_data\n")
        sys.stdout.flush()
        counter += 1
        '''
        """
        sys.stdout.write(f"Durchlauf {counter},\n")
        
        ADC_Value = ADC.ADS1263_GetAll(channel2read)
        for channel in channel2read:
            if(ADC_Value[channel]>>31 == 1):
                sys.stdout.write(f"ADC1,IN{channel},{REF*2 - ADC_Value[channel]*REF/ 0x80000000}\n")
            else:
                sys.stdout.write(f"ADC1,IN{channel},{ADC_Value[channel]*REF/ 0x7fffffff}\n")
                y_value = ADC_Value[channel]*REF/ 0x7fffffff
                x_value = counter
        sys.stdout.flush()
        """
        ADC_Value = ADC.ADS1263_GetAll(channel2read)
        for channel in channel2read:
            value = 0
            if(ADC_Value[channel]>>31 == 1):
                value = REF*2 - ADC_Value[channel]*REF/ 0x80000000
            else:
                value = ADC_Value[channel]*REF/ 0x7fffffff
            cache[channel] += value
        counter += 1
        if counter == 10:
            sys.stdout.write(f"Durchlauf {counter}\n")
            for channel in channel2read:
                sys.stdout.write(f"ADC1,IN{channel},{cache[channel]/10}\n")
                cache[channel] = 0 #Reset Cache für jeden Channel
            sys.stdout.write("Warte auf nächsten Durchlauf!\n\n")
            sys.stdout.flush()
            counter = 0
        
        time.sleep(0.1)
    ADC.ADS1263_Exit()
    
except IOError as e:
    print("Fehler:")
    print(e)

   
