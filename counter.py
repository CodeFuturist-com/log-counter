import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

contador = 0

while True:
    contador += 1
    logging.info(f'Contador: {contador}')
    time.sleep(3)