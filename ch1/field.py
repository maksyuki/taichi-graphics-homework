import taichi as ti

ti.init(arch=ti.gpu)

pix = tifield(dtype=float, shape=(16,18))
pix[1,2] = 42.23
