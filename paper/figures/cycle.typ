#set text(size: 9pt)
#let outgoing = rgb("d5e3ed")
#let incoming = rgb("ececec")
#let block(values, shade) = box(fill: shade, inset: (x: 1.5mm, y: 2.8mm), width: 26mm)[
  #align(center)[#grid(columns: (1fr,) * 4, ..values)]
]
#let zero = block(([], [], [$0$], []), white)
#align(center)[
  #grid(columns: (8mm, 26mm, 26mm, 26mm, 26mm, 37mm), gutter: 1mm, align: center + horizon,
    [], [Block 0], [Block 1], [Block 2], [Block 3], [Rank-one constraint],
    [], block(($L_0$, $R_0$, $X_0$, $Y_0$), white), block(($L_1$, $R_1$, $X_1$, $Y_1$), white), block(($L_2$, $R_2$, $X_2$, $Y_2$), white), block(($L_3$, $R_3$, $X_3$, $Y_3$), white), [],
    [$0$], block(($1$, $r_0$, $1$, $r_0$), outgoing), block(($1$, $1$, $1$, $1$), incoming), zero, zero, [$h_1=r_0^(epsilon_0) h_0$],
    [$1$], zero, block(($1$, $r_1$, $1$, $r_1$), outgoing), block(($1$, $1$, $1$, $1$), incoming), zero, [$h_2=r_1^(epsilon_1) h_1$],
    [$2$], zero, zero, block(($1$, $r_2$, $1$, $r_2$), outgoing), block(($1$, $1$, $1$, $1$), incoming), [$h_3=r_2^(epsilon_2) h_2$],
    [$3$], block(($1$, $T^2$, $T$, $T$), incoming), zero, zero, block(($1$, $r_3$, $1$, $r_3$), outgoing), [$T h_0=r_3^(epsilon_3) h_3$],
  )
  #v(3mm)
  #box(fill: outgoing, inset: 2pt)[Outgoing block] #h(4mm)
  #box(fill: incoming, inset: 2pt)[Incoming / closing block]
  #h(4mm) $⇒ product_(i=0)^3 r_i^(epsilon_i)=T$
]
