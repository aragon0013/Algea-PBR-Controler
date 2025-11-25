import time
import sys
import signal
import select
import ADC_code.ADS1263 as ADS1263

def handle_sigterm(signum, frame):
    print("SIGTERM erhalten, sauber beenden...")
    measure["running"] = False

measure = {"running":True}
counter = 0

# müssen wir noch messen
REF = 5.08

signal.signal(signal.SIGTERM, handle_sigterm)
sys.stdout.write("initialize sensor program...\n")
sys.stdout.flush()
time.sleep(2)

try:
    ADC = ADS1263.ADS1263()

    if (ADC.ADS1263_init_ADC1('ADS1263_400SPS') == -1):
        exit()
    ADC.ADS1263_SetMode(0)
    channel2read = [0]

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
        print(f"Durchlauf {counter}")
        
        ADC_Value = ADC.ADS1263_GetAll(channel2read)
        for channel in channel2read:
            if(ADC_Value[channel]>>31 == 1):
                sys.stdout.write(f"ADC1 IN{channel},{REF*2 - ADC_Value[channel]*REF/ 0x80000000}\n")
            else:
                sys.stdout.write(f"ADC1 IN{channel},{ADC_Value[channel]*REF/ 0x7fffffff}\n")
            sys.stdout.flush()
        

        
        counter += 1
        time.sleep(5)
    ADC.ADS1263_Exit()
    
except IOError as e:
    print("Fehler:")
    print(e)

   