import pygame

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

dic = unpickle(r'C:\Users\pedro\Downloads\cifar-10-batches-py\data_batch_1')
data = dic[b'data']
surface = pygame.Surface((32, 32))

dicio = {}
dicio['media'] = []
dicio['imagem'] = []

for im in range(10000):

    foto = data[im]

    ri = 0
    gi = 0
    bi = 0

    for i in range(32):
        for j in range(32):
            ri += foto[i + j*32]
            gi += foto[i + j*32 + 1024]
            bi += foto[i + j*32 + 2048]
    
    ri /= 32**2
    gi /= 32**2
    bi /= 32**2

    dicio['media'].append((ri, gi, bi))
    dicio['imagem'].append((foto))
