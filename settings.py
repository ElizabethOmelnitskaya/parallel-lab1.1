from os import listdir, path

ADDR, PORT, DATADIR, WORD = '127.0.0.1', 8887, 'data', 'да'
FILES = [f'{path.join(DATADIR, f)}\n' for f in listdir(DATADIR)]
