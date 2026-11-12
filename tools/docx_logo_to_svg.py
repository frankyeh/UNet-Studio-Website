#!/usr/bin/env python3
"""Convert the native DrawingML vector logo in 'unet studio.docx' to an icon-only SVG.

Reads word/document.xml and word/theme/theme1.xml directly from the DOCX archive:
- Resolves schemeClr (tx2 -> dk2) + lumMod/lumOff in HLS space (#1F497D -> #558ED5).
- Transforms all 8 wps:wsp custom-geometry open Bezier paths (moveTo + cubicBezTo)
  using wp:positionH/V posOffset, a:xfrm ext (cx/cy), and center rotation (rot/60000 deg).
- Preserves each shape's exact stroke width (a:ln/@w in EMU -> pt, round linecaps)
  and renders Office 'diamond' (w='sm', len='sm') headEnd/tailEnd markers as explicit
  <polygon> elements centered at each path endpoint with half-diagonal = stroke_width,
  oriented along the curve chord at Euclidean distance = stroke_width.
"""

import argparse
import colorsys
import math
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

EMU_PER_PT = 12700.0
NS = {
    "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "wps": "http://schemas.microsoft.com/office/word/2010/wordprocessingShape",
}


def resolve_scheme_color(theme_xml: str, scheme_name: str, lum_mod: int, lum_off: int) -> str:
    alias = {"tx1": "dk1", "tx2": "dk2", "bg1": "lt1", "bg2": "lt2"}.get(scheme_name, scheme_name)
    root = ET.fromstring(theme_xml)
    node = root.find(f".//a:clrScheme/a:{alias}", NS)
    if node is None:
        raise ValueError(f"Missing scheme color {alias} in theme1.xml")
    srgb = node.find("a:srgbClr", NS)
    hex_rgb = srgb.attrib["val"] if srgb is not None else node.find("a:sysClr", NS).attrib["lastClr"]
    r, g, b = (int(hex_rgb[i : i + 2], 16) / 255.0 for i in (0, 2, 4))
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    l = max(0.0, min(1.0, l * (lum_mod / 100000.0) + (lum_off / 100000.0)))
    r2, g2, b2 = colorsys.hls_to_rgb(h, l, s)
    return "#{:02X}{:02X}{:02X}".format(round(r2 * 255), round(g2 * 255), round(b2 * 255))


def cubic_point(p0, p1, p2, p3, t: float):
    u = 1.0 - t
    return (
        u**3 * p0[0] + 3 * u**2 * t * p1[0] + 3 * u * t**2 * p2[0] + t**3 * p3[0],
        u**3 * p0[1] + 3 * u**2 * t * p1[1] + 3 * u * t**2 * p2[1] + t**3 * p3[1],
    )


def sample_curve(segments, steps_per_seg: int = 400):
    pts = [segments[0][0]]
    for seg in segments:
        for step in range(1, steps_per_seg + 1):
            pts.append(cubic_point(*seg, step / steps_per_seg))
    return pts


def office_diamond_end(end_pt, sampled_pts, is_head: bool, half_diag: float):
    seq = sampled_pts if is_head else list(reversed(sampled_pts))
    ref_pt = seq[-1]
    for pt in seq[1:]:
        if math.hypot(pt[0] - end_pt[0], pt[1] - end_pt[1]) >= half_diag:
            ref_pt = pt
            break
    dx, dy = ref_pt[0] - end_pt[0], ref_pt[1] - end_pt[1]
    norm = math.hypot(dx, dy) or 1.0
    ux, uy = dx / norm, dy / norm
    nx, ny = -uy, ux
    return [
        (end_pt[0] + ux * half_diag, end_pt[1] + uy * half_diag),
        (end_pt[0] + nx * half_diag, end_pt[1] + ny * half_diag),
        (end_pt[0] - ux * half_diag, end_pt[1] - uy * half_diag),
        (end_pt[0] - nx * half_diag, end_pt[1] - ny * half_diag),
    ]


def convert_docx_to_svg(docx_path: Path, out_svg_path: Path) -> dict:
    with zipfile.ZipFile(docx_path, "r") as zf:
        doc_xml = zf.read("word/document.xml").decode("utf-8")
        theme_xml = zf.read("word/theme/theme1.xml").decode("utf-8")

    root = ET.fromstring(doc_xml)
    shapes = []
    bound_pts = []

    for anc in root.findall(".//wp:anchor", NS):
        pos_x = int(anc.find("wp:positionH/wp:posOffset", NS).text) / EMU_PER_PT
        pos_y = int(anc.find("wp:positionV/wp:posOffset", NS).text) / EMU_PER_PT
        wsp = anc.find(".//wps:wsp", NS)
        xfrm = wsp.find(".//a:xfrm", NS)
        rot_deg = int(xfrm.attrib.get("rot", "0")) / 60000.0
        cx = int(xfrm.find("a:ext", NS).attrib["cx"]) / EMU_PER_PT
        cy = int(xfrm.find("a:ext", NS).attrib["cy"]) / EMU_PER_PT

        path_el = wsp.find(".//a:path", NS)
        pw = int(path_el.attrib["w"])
        ph = int(path_el.attrib["h"])

        ln = wsp.find(".//a:ln", NS)
        stroke_w = int(ln.attrib["w"]) / EMU_PER_PT
        scheme = ln.find(".//a:gs/a:schemeClr", NS)
        color = resolve_scheme_color(
            theme_xml,
            scheme.attrib["val"],
            int(scheme.find("a:lumMod", NS).attrib["val"]),
            int(scheme.find("a:lumOff", NS).attrib["val"]),
        )

        center_x = pos_x + cx / 2.0
        center_y = pos_y + cy / 2.0
        rad = math.radians(rot_deg)
        cos_a, sin_a = math.cos(rad), math.sin(rad)

        def transform_pt(px: int, py: int):
            lx = pos_x + (px / pw) * cx
            ly = pos_y + (py / ph) * cy
            dx, dy = lx - center_x, ly - center_y
            return (
                center_x + dx * cos_a - dy * sin_a,
                center_y + dx * sin_a + dy * cos_a,
            )

        segments = []
        cur = None
        for cmd in path_el:
            tag = cmd.tag.split("}")[-1]
            pts = [transform_pt(int(p.attrib["x"]), int(p.attrib["y"])) for p in cmd.findall("a:pt", NS)]
            if tag == "moveTo":
                cur = pts[0]
            elif tag == "cubicBezTo":
                segments.append((cur, pts[0], pts[1], pts[2]))
                cur = pts[2]
            else:
                raise ValueError(f"Unexpected path command: {tag}")

        sampled = sample_curve(segments)
        polys = []
        head = ln.find("a:headEnd", NS)
        tail = ln.find("a:tailEnd", NS)
        if head is not None and head.attrib.get("type") == "diamond":
            polys.append(office_diamond_end(segments[0][0], sampled, True, stroke_w))
        if tail is not None and tail.attrib.get("type") == "diamond":
            polys.append(office_diamond_end(segments[-1][3], sampled, False, stroke_w))

        half_w = stroke_w / 2.0
        for sx, sy in sampled:
            bound_pts.extend([(sx - half_w, sy - half_w), (sx + half_w, sy + half_w)])
        for poly in polys:
            bound_pts.extend(poly)

        shapes.append((segments, stroke_w, color, polys))

    min_x = min(p[0] for p in bound_pts)
    min_y = min(p[1] for p in bound_pts)
    vb_w = max(p[0] for p in bound_pts) - min_x
    vb_h = max(p[1] for p in bound_pts) - min_y

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w:.2f} {vb_h:.2f}">'
    ]
    for segments, stroke_w, color, polys in shapes:
        d_cmds = [f"M {segments[0][0][0] - min_x:.2f} {segments[0][0][1] - min_y:.2f}"]
        for _, p1, p2, p3 in segments:
            d_cmds.append(
                f"C {p1[0] - min_x:.2f} {p1[1] - min_y:.2f}, "
                f"{p2[0] - min_x:.2f} {p2[1] - min_y:.2f}, "
                f"{p3[0] - min_x:.2f} {p3[1] - min_y:.2f}"
            )
        svg_lines.append(
            f'  <path d="{" ".join(d_cmds)}" fill="none" stroke="{color}" '
            f'stroke-width="{stroke_w:.2f}" stroke-linecap="round" stroke-linejoin="round"/>'
        )
        for poly in polys:
            pts_attr = " ".join(f"{px - min_x:.2f},{py - min_y:.2f}" for px, py in poly)
            svg_lines.append(f'  <polygon points="{pts_attr}" fill="{color}"/>')
    svg_lines.append("</svg>\n")

    out_svg_path.parent.mkdir(parents=True, exist_ok=True)
    out_svg_path.write_text("\n".join(svg_lines), encoding="utf-8")
    return {"paths": len(shapes), "viewBox": (round(vb_w, 2), round(vb_h, 2)), "color": shapes[0][2]}


def main():
    parser = argparse.ArgumentParser(description="Convert unet studio.docx vector logo to SVG.")
    parser.add_argument("--docx", required=True, type=Path, help="Path to 'unet studio.docx'")
    parser.add_argument("--out", required=True, type=Path, help="Output SVG path")
    args = parser.parse_args()
    info = convert_docx_to_svg(args.docx, args.out)
    print(f"Wrote {args.out}: {info}")


if __name__ == "__main__":
    main()
