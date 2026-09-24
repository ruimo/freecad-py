import FreeCAD as App
import Part

doc = App.newDocument("BNX016_01")

# 寸法 [mm]
body_w = 12.0
body_d = 11.0
body_h = 8.0

lead_d = 0.8
lead_l = 4.0

# KiCadフットプリントのパッド座標を本体中心原点へ変換
leads_spec = (
    (1, 2.5, -2.5),
    (2, 2.5, 2.5),
    (3, -2.5, -2.5),
    (4, -2.5, 2.5),
    (5, 5.0, 0.0),
    (6, 0.0, 0.0),
)

# 原点:
# XY = 本体中心
# Z=0 = 本体下面（基板側）
# リードは-Z方向

# 本体
body_shape = Part.makeBox(
    body_w,
    body_d,
    body_h,
    App.Vector(-body_w / 2, -body_d / 2, 0),
)

body = doc.addObject("PartDesign::Feature", "Body")
body.Label = "BNX016-01 Body"
body.Shape = body_shape
body.ViewObject.ShapeColor = (0.18, 0.18, 0.20)

# リード
leads = []

for number, x, y in leads_spec:
    shape = Part.makeCylinder(
        lead_d / 2,
        lead_l,
        App.Vector(x, y, 0),
        App.Vector(0, 0, -1),
    )

    lead = doc.addObject("PartDesign::Feature", f"Lead{number}")
    lead.Label = f"Lead {number}"
    lead.Shape = shape
    lead.ViewObject.ShapeColor = (0.80, 0.80, 0.82)
    leads.append(lead)

doc.recompute()

# FreeCADマスターファイル
doc.recompute()
