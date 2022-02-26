# AtomicOrbitals
 
Visualization of Hydrogen wave functions given by the equation
<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;\psi_{n,\ell,m}(r,\theta,\varphi)&space;=&space;\sqrt{\left(\frac{2}{n}\right)^3\frac{(n-\ell-1)!}{2n(n&plus;\ell)!}}&space;\&space;\mathrm{e}^{-\rho/2}\rho^\ell&space;L_{n-\ell-1}^{2\ell&plus;1}(\rho)Y_{\ell}^{m}(\theta,&space;\varphi)" title="\bg_white \psi_{n,\ell,m}(r,\theta,\varphi) = \sqrt{\left(\frac{2}{n}\right)^3\frac{(n-\ell-1)!}{2n(n+\ell)!}} \ \mathrm{e}^{-\rho/2}\rho^\ell L_{n-\ell-1}^{2\ell+1}(\rho)Y_{\ell}^{m}(\theta, \varphi)" />


This can lead to some interesting visualizations as seen below, however best viewed in 3D.



<img src="https://github.com/simonchemnitz/AtomicOrbitals/blob/main/Examples/ex1.png" width="400">
<img src="https://github.com/simonchemnitz/AtomicOrbitals/blob/main/Examples/ex2.png" width="400">
<img src="https://github.com/simonchemnitz/AtomicOrbitals/blob/main/Examples/ex3.png" width="400">

Simply run the file  to produce interactive plotly 3D figures.
Required packages
* Numpy 
* Pandas
* Scipy
* Plotly