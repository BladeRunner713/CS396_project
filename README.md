# CS396_project

Only for causal_discovery notebook.

Install R and R studio.

Install [graphviz](https://breakdance.github.io/breakdance/), probably need to reboot.

Install some require R packages.
```sh
install.packages("BiocManager")
BiocManager::install(c("CAM", "SID", "bnlearn", "pcalg", "kpcalg", "D2C"))
```

Finally, install [RCIT](https://github.com/Diviyan-Kalainathan/RCIT)

```sh
install.packages("devtools")
install_github("Diviyan-Kalainathan/RCIT")
```
Remember to change this to local R path
```sh
# Change to your Rscript path
cdt.SETTINGS.rpath = 'C:/Program Files/R/R-4.1.3/bin/Rscript'
```
