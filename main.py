
# import subprocess
# output = subprocess.call("{} --vanilla {}".format("C:/Program Files/R/R-4.1.3/bin/Rscript", "testlib.R"), shell=True)
# print(output)

import subprocess
# path to your R installation
command = "C:/Program Files/R/R-4.1.3/bin/Rscript"
arg = '--vanilla'
# path of repo
path2script = "C:/LE/Class/2022winter/396 Causual Inference/project/CS396_project/testlib.R"
output = subprocess.call([command, arg, path2script], shell=True)
print (output)