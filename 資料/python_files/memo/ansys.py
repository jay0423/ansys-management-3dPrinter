# setup

from ansys.mapdl.core import launch_mapdl
mapdl = launch_mapdl()

mapdl.cwd(r"C:\Users\matlab\ansys_kajimoto\test10")
mapdl.cwd(r"C:\Users\matlab\Documents\ansys\ansys_fujii\test")
mapdl.filname("tset1", key=1)

mapdl.input(r"C:\Users\matlab\Documents\ansys-management\1\CFRP0\correction\C0_cor.ansys")
mapdl.input(r"C:\Users\matlab\Documents\ansys-management\2\CFRP2_lap=20\thickness=1.5\C2_l20_th1.5.ansys")
mapdl.input(r"C:\Users\matlab\Documents\ansys-management\2\CFRP2_lap=20\thickness=2.0\C2_l20_th2.0.ansys")
mapdl.input(r"C:\Users\matlab\Documents\ansys-management\test2\test.ansys")
mapdl.input(r"sample\CFRP2_lap=10\thickness=0.5\C2_l10_th0.5.ansys")
mapdl.input(r"C:\Users\matlab\Documents\ansys\ansys-management\test\cfrp2_lap=10\thickness=1.5\c2_l10_th1.5.ansys")
mapdl.input(r"C:\Users\matlab\Documents\ansys\ansys-management\fuji\PLA2.ansys")
mapdl.input(r"C:\Users\matlab\Documents\ansys\ansys-management\sample\cfrp2_lap=10\thickness=0.5\c2_l10_th0.5.ansys")

mapdl.input(r"C:\Users\matlab\Documents\ansys-management\sample\CFRP2_lap=10\thickness=0.5\C2_l10_th0.5.ansys")
mapdl.input(r"sample\CFRP2_lap=10\thickness=0.5\C2_l10_th0.5.ansys")

mapdl.solve()
mapdl.finish()

mapdl.post26()
mapdl.rforce(2, "NNUM", "F", "X", "FX")
text = mapdl.prvar(2)
with open('test.csv', 'w') as f:
    f.write(text)