#set text(size: 10pt)
#let corner-table(chosen) = grid(
  columns: (11mm, 25mm, 25mm),
  rows: (9mm, 14mm, 14mm),
  align: center + horizon,
  [], $b_i$, $c_i$,
  $alpha$, box(stroke: 0.8pt, inset: 6pt)[$z_(L_i)$],
    box(stroke: 0.8pt, inset: 6pt)[#if chosen [$t_i^(-1) z_(X_i)$] else [$t_i z_(Y_i)$]],
  $beta$, box(stroke: 0.8pt, inset: 6pt)[#if chosen [$t_i z_(Y_i)$] else [$t_i^(-1) z_(X_i)$]],
    box(stroke: 0.8pt, inset: 6pt)[$z_(R_i)$],
)
#grid(columns: (1fr, 1fr), gutter: 10mm,
  align(center)[*Selected: $epsilon_i=1$* #v(2mm) #corner-table(true)],
  align(center)[*Unselected: $epsilon_i=0$* #v(2mm) #corner-table(false)],
)
