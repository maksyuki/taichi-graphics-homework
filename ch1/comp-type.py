import taichi as ti

ti.init(arch=ti.gpu)

@ti.kernel
def foo():
    a = ti.Vector([0.0, 0.0, 1.0])
    d = ti.Vector([0.0, 1.0, 0.0])
    B = ti.Matrix([[1.5, 1.4], [1.3, 1.2]])
    print(a)
    print("B = ", B)
    
    r = ti.Struct(v1=a, v2=d, l=1)
    print("r.v1=", r.v1)
    print("r.v2=", r.v2)

foo()
