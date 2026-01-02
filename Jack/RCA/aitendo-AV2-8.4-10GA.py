import FreeCAD as App
import Part
import math

// https://www.aitendo.com/product/16785

name = "aitendo_AV2-8.4-10GA"
doc = App.newDocument(name)

# --- 定数定義 ---
B_W = 27.0      # 本体幅
B_H = 14.4      # 本体高さ
B_D = 10.3      # 本体奥行
J_SPACE = 14.0  # ジャック中心間距離
J_Z = 7.9       # ジャック中心高さ
PIN_L = 3.0     # ピンの基板下長さ

# 1. 本体
body = Part.makeBox(B_W, B_D, B_H)
body.Placement.Base = App.Vector(-B_W/2, 0, 0)

# 2. RCAジャック（二重円筒）
for side in [-1, 1]:
    out_c = Part.makeCylinder(10.0/2, 7.6, App.Vector(side*J_SPACE/2, 0, J_Z), App.Vector(0, -1, 0))
    in_c = Part.makeCylinder(8.3/2, 7.6, App.Vector(side*J_SPACE/2, 0, J_Z), App.Vector(0, -1, 0))
    jack = out_c.cut(in_c)
    body = body.fuse(jack)

# 3. 上部固定タブ (R3.5, Φ2.5穴)
tab_base = Part.makeBox(7.0, 1.2, 16.9-14.4)
tab_base.translate(App.Vector(-3.5, 1.2, 14.4-2.0))
tab_cyl = Part.makeCylinder(3.5, 1.2, App.Vector(0, 1.2, 16.9), App.Vector(0, 1, 0))
tab_hole = Part.makeCylinder(2.5/2, 1.2, App.Vector(0, 1.2, 16.9), App.Vector(0, 1, 0))
tab = tab_base.fuse(tab_cyl).cut(tab_hole)
body = body.fuse(tab)

# 4. 足（ピン）の部分 - 正確な寸法再現

# (A) 信号ピン (矩形 2.5x1.5) - 底面図「1」
# 間隔 14.0mm, 前面から 5.0mm
for side in [-1, 1]:
    p1 = Part.makeBox(2.5, 1.5, PIN_L)
    p1.translate(App.Vector(side*14.0/2 - 2.5/2, 5.0 - 1.5/2, -PIN_L))
    body = body.fuse(p1)

# (B) アースピン (円柱 Φ1.5) - 底面図「2」
# 間隔 14.0mm Xオフセット4mm, 前面から 10.3mm
for side in [-1, 1]:
    p2 = Part.makeCylinder(1.5/2, PIN_L, App.Vector(side*14.0/2 + 4, 10.3, -PIN_L), App.Vector(0,0,1))
    body = body.fuse(p2)

# (C) サイドのスナップイン脚 (外側 25.5, 内側 22.8)
# 幅方向 1.35mm, 厚み 0.5mm
for side in [-1, 1]:
    p1 = Part.makeBox(1.35, 3.0, PIN_L)
    p1.translate(App.Vector(side*21.0/2 - 1.35/2, 6.0 - 3.0/2, -PIN_L))
    body = body.fuse(p1)

# 表示
obj = doc.addObject("Part::Feature", name)
obj.Shape = body
doc.recompute()
App.Gui.ActiveDocument.ActiveView.viewAxometric()