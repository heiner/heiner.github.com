set term svg size 971,600 enhanced font 'Helvetica, 24'
set output 'afapprox.svg'

set samples 500
set xrange [0:10]
set yrange [0:3]
set xtics 1
set ytics 1
set xzeroaxis lt -1 lc rgb "black" lw 1
set yzeroaxis lt -1 lc rgb "black" lw 1

# Add light grid to plot. gnuplotting.org/code/grid.cfg
set style line 102 lc rgb '#b6b7b9' lt 0 lw 1
set grid back ls 102

set border 0

# unset xzeroaxis
# unset yzeroaxis

set xtics nomirror
set ytics nomirror

set format x "%1.0f%%"
set format y "%1.0f%%"

set key right top

af(p, n) = \
      p * (1 + p) ** n / ((1 + p) ** n - 1)

afapprox(p, n) = \
      (1 + n * p / 2) / n

afm(p, n) = \
      100 * af((1 + p / 100) ** (1.0 / 12) - 1, 12 * n)

afapproxm(p, n) = \
      100 * afapprox(p / 100.0 / 12.0, 12 * n)

plot \
     afapproxm(x, 5) t "n=5" lc rgb "#edb120" lw 2,\
     afm(x, 5) notitle lc rgb "#77edb120" lw 1 dt 4,\
     \
     afapproxm(x, 7) t "n=7" lc rgb "#7e2f8e" lw 2,\
     afm(x, 7) notitle lc rgb "#777e2f8e" lw 1 dt 4,\
     \
     afapproxm(x, 10) t "n=10" lc rgb "#a2142f" lw 2,\
     afm(x, 10) notitle lc rgb "#77a2142f" lw 1 dt 4,\
     \
     afapproxm(x, 15) t "n=15" lc rgb "#d95319" lw 2,\
     afm(x, 15) notitle lc rgb "#77d95319" lw 1 dt 4,\
     \
     afapproxm(x, 20) t "n=20" lc rgb "#7e2f8e" lw 2,\
     afm(x, 20) notitle lc rgb "#777e2f8e" lw 1 dt 4,\
     \
     afapproxm(x, 25) t "n=25" lc rgb "#0072bd" lw 2,\
     afm(x, 25) notitle lc rgb "#770072bd" lw 1 dt 4,\
     \
     afapproxm(x, 30) t "n=30" lc rgb "#77ac30" lw 2,\
     afm(x, 30) notitle lc rgb "#7777ac30" lw 1 dt 4,\
     \
     afapproxm(x, 35) t "n=35" lc rgb "#666666" lw 2,\
     afm(x, 35) notitle lc rgb "#77666666" lw 1 dt 4


# pause -1