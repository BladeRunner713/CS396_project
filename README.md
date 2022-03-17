# CS396_project
Install R.

Install [graphviz](https://graphviz.org/download/)

Install some require R packages. You can check the installation by running 'main.py' and expected output = 0.
```sh
#%%R
install.packages("BiocManager")
BiocManager::install(c("CAM", "SID", "bnlearn", "pcalg", "kpcalg", "D2C"))
```

Remember to change local R path and Graphviz path
```sh
# add Graphviz Path
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
# Change to your Rscript path
cdt.SETTINGS.rpath = 'C:/Program Files/R/R-4.1.3/bin/Rscript'
```
