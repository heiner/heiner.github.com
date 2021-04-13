set term svg size 971,600 enhanced font 'Helvetica, 24'
set output 'af.svg'

set samples 500
set xrange [0:10]
set yrange [0:40]
set xtics 1
set ytics 5
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

# Draw the Gompertz distribution's pdf
set key right top

b = 1 / 9.5
t_m = 87.25

eta(t_0) = exp(b * (t_0 - t_m))

af(r, t_0) = \
      100 * (1 - exp(eta(t_0)) * eta(t_0) ** (r / 100 / b) * gamma(1 - r / 100 / b) * (1 - igamma(1 - r / 100 / b, eta(t_0)))) / r

plot \
     af(x, 35) t "t_0=35" lc rgb "#edb120" lw 5,\
     af(x, 45) t "t_0=45" lc rgb "#7e2f8e" lw 5,\
     af(x, 55) t "t_0=55" lc rgb "#a2142f" lw 5,\
     af(x, 65) t "t_0=65" lc rgb "#d95319" lw 5,\
     af(x, 75) t "t_0=75" lc rgb "#0072bd" lw 5,\
     af(x, 85) t "t_0=85" lc rgb "#77ac30" lw 5,\
     af(x, 95) t "t_0=95" lc rgb "#666666" lw 5
