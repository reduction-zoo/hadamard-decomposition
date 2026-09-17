#set math.equation(numbering: none)
#set text(size: 10pt)
#let node(body) = box(stroke: 0.8pt, inset: 6pt, body)
#align(center)[
  #grid(columns: (17mm, 24mm, 17mm, 17mm, 27mm, 26mm, 20mm), align: center + horizon,
    [], $r_0^(epsilon_0)$, [], [], [], $r_(K-1)^(epsilon_(K-1))$, [],
    node[$h_0$], $arrow.r.long$, node[$h_1$], $dots.c$, node[$h_(K-1)$], $arrow.r.long$, node[$T h_0$],
  )
  #v(5mm)
  $ product_(i=0)^(K-1) r_i^(epsilon_i) = T, quad h_0 != 0 $
]
