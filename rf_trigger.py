import argparse, signal, time
from rpi_rf import RFDevice

def listen(signal)
    parser = argparse.ArgumentParser(description='Receives a decimal code via a 433/315MHz GPIO device') 
    parser.add_argument('-g', dest='gpio', type=int, default=27, 
                       help="GPIO pin (Default: 27)") 
    args = parser.parse_args() 
    signal.signal(signal.SIGINT, exithandler) 
    rfdevice = RFDevice(args.gpio) 
    rfdevice.enable_rx() 
    timestamp = None 
    logging.info("Listening for codes on GPIO " + str(args.gpio)) 
    code_of_interest = singal 
    
    while True: 
       if rfdevice.rx_code_timestamp != timestamp: 
           timestamp = rfdevice.rx_code_timestamp 
           logging.info(str(rfdevice.rx_code)) 
           if str(rfdevice.rx_code) == code_of_interest:
               time.sleep(1) 
               rfdevice.cleanup()
               return False
           