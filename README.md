# CS396_project

Install R and R studio.

Install [graphviz](https://graphviz.org/download/), probably need to reboot.

Install some require R packages. You can check the installation by running 'main.py' and expected output = 0

```sh
install.packages("BiocManager")
BiocManager::install(c("pcalg", "kpcalg"))
```

Install [RCIT](https://github.com/Diviyan-Kalainathan/RCIT)

```sh
install.packages("devtools")
library(devtools)
install_github("Diviyan-Kalainathan/RCIT")
```

Remember to change local R path and Graphviz path
```sh
# add Graphviz Path
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
# Change to your Rscript path
cdt.SETTINGS.rpath = 'C:/Program Files/R/R-4.1.3/bin/Rscript'
```
