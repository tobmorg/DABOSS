pflag = 1

thck = 0.5	

!p.font = -1
!p.charthick = thck
!x.thick = thck
!y.thick = thck
!p.thick = thck
!p.charsize = 0.75



data = READ_ASCII("data/kbos_mpc.csv", DELIMITER=",", $
                  DATA_START=1)
data = data.field01

print, data[1,0]

a = data[1,*]
ecc = data[2,*] 
inc = data[3,*]
peri = data[4,*]
node = data[5,*]
mag = data[6,*] 



init_plot, pflag, $
        file_name="kbos", $
        x_plot=20, $
        y_plot=15


positions = cglayout([2,2], xgap=8, ygap=2)

norm_font = '!6'

omega_str = '!7x' + norm_font ;TeXtoIDL('\omega')
node_str = '!7X' + norm_font ;TeXtoIDL('\Omega')

x_range = [20,60]
sym_size = 0.1 

xyouts, 0,0, norm_font

cgplot, a, ecc, xrange=x_range, psym='filled circle', symsize=sym_size, position=positions[*,0], xtickformat='(A1)', /noerase, ytitle='eccentricity', thick=thck

cgplot, a, inc, yrange=[0,30], xrange=x_range, psym='filled circle',symsize=sym_size, position=positions[*,1], xtickformat='(A1)', /noerase, ytitle='inclination i [deg]', thick=thck

cgplot, a, peri, xrange=x_range, psym='filled circle',symsize=sym_size, position=positions[*,2], /noerase, ytitle='arg. of pericentre ' + omega_str + ' [deg]', xtitle='semi-major axis a [au]', thick=thck

cgplot, a, node ,xrange=x_range, psym='filled circle',symsize=sym_size, position=positions[*,3], /noerase, ytitle='long. of the asc. node ' + node_str + ' [deg]', xtitle='semi-major axis a [au]', thick=thck




if (pflag eq 1) then begin $
save_plot, file_name="kbos" & $ 
;spawn, "open " + "kbos.pdf" & $ 
endif

