set term svg size 800,600 enhanced font 'Arial, 24'
set output 'gompertz-hazard.svg'

set samples 500
set xrange [0:1]
set yrange [0:50]
set xtics 0.25
set ytics 10
set xzeroaxis lt -1 lc rgb "black" lw 1
set yzeroaxis lt -1 lc rgb "black" lw 1

# Draw the Gompertz distribution's pdf
set key left top

f(x, eta, b) = b*eta*exp(b*x)

plot f(x, 0.1, 1.0) t "eta=0.1, b=1" lc rgb "red" lw 5,\
   f(x, 1.0, 1.0) t "eta=2.0, b=1" lc rgb "black" lw 5,\
   f(x, 2.0, 1.0) t "eta=3.0, b=1" lc rgb "blue" lw 5,\
   f(x,1.0, 2) t "eta=1.0, b=2" lc rgb "green" lw 5,\
   f(x,1.0, 3) t "eta=1.0, b=3" lc rgb "grey" lw 5