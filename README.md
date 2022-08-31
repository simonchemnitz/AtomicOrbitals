# AtomicOrbitals
 
Visualization of Hydrogen wave functions given by the equation
<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;\psi_{n,\ell,m}(r,\theta,\varphi)&space;=&space;\sqrt{\left(\frac{2}{n}\right)^3\frac{(n-\ell-1)!}{2n(n&plus;\ell)!}}&space;\&space;\mathrm{e}^{-\rho/2}\rho^\ell&space;L_{n-\ell-1}^{2\ell&plus;1}(\rho)Y_{\ell}^{m}(\theta,&space;\varphi)" title="\bg_white \psi_{n,\ell,m}(r,\theta,\varphi) = \sqrt{\left(\frac{2}{n}\right)^3\frac{(n-\ell-1)!}{2n(n+\ell)!}} \ \mathrm{e}^{-\rho/2}\rho^\ell L_{n-\ell-1}^{2\ell+1}(\rho)Y_{\ell}^{m}(\theta, \varphi)" />


This can lead to some interesting visualizations as seen below, however best viewed in 3D.



<img src="https://github.com/simonchemnitz/AtomicOrbitals/blob/main/Examples/ex1.png" width="400">
<img src="https://github.com/simonchemnitz/AtomicOrbitals/blob/main/Examples/ex2.png" width="400">
<img src="https://github.com/simonchemnitz/AtomicOrbitals/blob/main/Examples/ex3.png" width="400">

To download packages
```
pip install pipenv

pipenv install
```
```
plot_kwargs = {
        "opacity": 1,
        "colorscale": "plasma",
        "marker_size": 2,
        "theme": "plotly_dark",
    }

wave = Hydrogen_Wave()
wave.set_quantum_number(n=4, l=2, m=2)
wave.generate_data(n_points=600000, low=-35, high=35)
wave.vizualise_wave(threshold=0.01, plot_kwargs=plot_kwargs)
```
