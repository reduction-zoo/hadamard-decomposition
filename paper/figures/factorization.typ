#set text(size: 9pt)
#let data = json("supports.json")
#let boundaries = (0, 16, 28, 44, 48)
#let pixels(rows) = grid(
  columns: (1.45mm,) * 16,
  rows: (1.45mm,) * 52,
  ..rows.enumerate().map(((i, row)) => row.enumerate().map(((j, value)) => rect(
    width: 1.45mm, height: 1.45mm,
    fill: if value == 1 { black } else { white },
    stroke: (top: if i in boundaries { 0.45pt } else { 0.08pt + luma(80%) },
      left: if calc.rem(j, 4) == 0 { 0.45pt } else { 0.08pt + luma(80%) },
      right: if j == 15 { 0.45pt } else { none },
      bottom: if i == 51 { 0.45pt } else { none }),
  ))).flatten(),
)
#align(center)[
  #grid(columns: (25mm, 10mm, 25mm, 10mm, 25mm, 34mm), column-gutter: 2mm, row-gutter: 1.5mm,
    align: center + horizon,
    [$U V$], [], [$W Z$], [], [$M$], [],
    pixels(data.a), text(size: 18pt)[$⊙$], pixels(data.b), text(size: 18pt)[$=$], pixels(data.m),
    grid(rows: (23.2mm, 17.4mm, 23.2mm, 5.8mm, 5.8mm), align: left + horizon,
      [Identity · 16 rows], [Anchor pairs · 12], [Neighbors · 16], [Calibration · 4], [Cycle · 4]),
    [$"rank" = 2$], [], [$"rank" = 8$], [], [$52 times 16$], [],
  )
  #v(3mm)
  #grid(columns: (2mm, auto, 5mm, 2mm, auto), gutter: 2mm, align: horizon,
    rect(width: 2mm, height: 2mm, fill: black, stroke: none), [Nonzero entry], [],
    rect(width: 2mm, height: 2mm, stroke: 0.3pt), [Zero entry])
]
