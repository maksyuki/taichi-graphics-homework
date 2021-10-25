import taichi as ti

ti.init(arch=ti.gpu)

@ti.kernel
def foo():
    a = 1.234234
    b = ti.cast(a, ti.i32)
    c = ti.cast(b, ti.i32)
    print("b = ", b)
    print("c = ", c)
    print(a)

foo()
