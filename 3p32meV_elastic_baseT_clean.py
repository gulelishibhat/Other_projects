import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os
import glob

import scipy.optimize as opt

data_directory = '/SNS/CNCS/IPTS-20916/shared/autoreduce/'
nxspe_files = sorted(glob.glob(data_directory + "*.nxspe"))

nxspe_elastic_files = []
for idx, val in enumerate(nxspe_files):
    if 'elastic' in val:
        nxspe_elastic_files.append(nxspe_files.pop(idx))

print(nxspe_elastic_files)
#print(nxspe_files)

run_numbers = range(288826, 288868+1)

print(len(run_numbers))

runs = run_numbers

#print "Low T data"

flag = 0
for r in runs:
    for filename_ in nxspe_files:
    #for filename_ in nxspe_elastic_files:
        if str(r) in filename_:
            filename = filename_

    print(filename)
    raw=LoadNXSPE(Filename=filename)

    #SetUB(raw, UB='-0.0030, 0.0036, 0.1218,0.1211, 0.0049, 0.0027,-0.0068, 0.0850, -0.0054')
    #SetUB(raw,a=7.52,b=4.599,c=7.60,alpha=90, beta=90, gamma=90, u="0,1,0", v="0,0,1")
    #SetUB(raw,a=5.837,b=5import numpy as np
    LoadIsawUB( raw,'/SNS/CNCS/IPTS-20916/shared/ub_matrix/UB_night1_15K.mat')

    md_inelastic_3p32meV_lowT_refinedUB=ConvertToMD(InputWorkspace=raw, 
                                QDimensions='Q3D', 
                                Q3DFrames='HKL', 
                                Uproj='0,1,0', Vproj='0,0,1', Wproj='1,0,0', 
                                QConversionScales='HKL',
                                MinValues="-3.5,-6.0,-3.5,-10",MaxValues="3.5,6.0,3.5,10")
                                
    if flag == 0:
        inelastic_3p32meV_lowT_refinedUB = CloneMDWorkspace(md_inelastic_3p32meV_lowT_refinedUB)
        flag =1
    else:
        inelastic_3p32meV_lowT_refinedUB = inelastic_3p32meV_lowT_refinedUB + md_inelastic_3p32meV_lowT_refinedUB
        
#Binning test IvsQx
MD_inelastic_3p32meV_lowT_refinedUB_histo = BinMD(InputWorkspace='inelastic_3p32meV_lowT_refinedUB', 
            AlignedDim0='[0,K,0],-1.5,0.5,100', 
            AlignedDim1='[0,0,L],-1.02,-0.98,1', 
            AlignedDim2='[H,0,0],-0.2,0.2,1', 
            AlignedDim3='DeltaE,-0.5,0.5,1', 
            OutputWorkspace='MD_inelastic_3p32meV_lowT_refinedUB_histo')
            
plotSlice(MD_inelastic_3p32meV_lowT_refinedUB_histo , normalization = 2)
SaveMD(MD_inelastic_3p32meV_lowT_refinedUB_histo, Filename = '/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/3p32meV_base_T_IvsQ_bin_test_k.nxs')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os
import glob
from mantid import plots
import pandas as pd

import scipy.optimize as opt
#Reduce into 1D plot based on binning information.

MD_in=LoadMD(Filename = '/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/3p32meV_base_T_IvsQ_bin_test_k.nxs',OutputWorkspace='MD_in')

Q, I, dI = mantid.plots.helperfunctions.get_md_data1d(MD_in,mantid.plots.helperfunctions.get_normalization(MD_in)[0])

#f=open('/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/saved_md/elastic_baseT_0meV_night3_refinedUB_histo_100bins.txt','w')
out=[]
for i in range(len(Q)):
    out.append([Q[i],I[i],dI[i]])
    out_np = np.array(out)
df = pd.DataFrame(out_np)
df.to_csv('/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/3p32meV_base_T_IvsQ_bin_test_k.txt', sep = '\t', na_rep = 'np.nan', index = 'False', Header = 'False')
#f.write(df.values)
#f.close()




#Resolution test 3p32
MD_inelastic_3p32meV_lowT_refinedUB_histo = BinMD(InputWorkspace='inelastic_3p32meV_lowT_refinedUB', 
            AlignedDim0='[0,K,0],-0.82,-0.78,1', 
            AlignedDim1='[0,0,L],-1.2,-0.8,1', 
            AlignedDim2='[H,0,0],-0.2,0.2,1', 
            AlignedDim3='DeltaE,-1,2.5,70', 
            OutputWorkspace='MD_inelastic_3p32meV_lowT_refinedUB_histo')
            
plotSlice(MD_inelastic_3p32meV_lowT_refinedUB_histo , normalization = 2)
SaveMD(MD_inelastic_3p32meV_lowT_refinedUB_histo, Filename = '/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/3p32meV_base_T_resolution__-0p8_diff0p02.nxs')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os
import glob
from mantid import plots
import pandas as pd
s
import scipy.optimize as opt

MD_in=LoadMD(Filename = '/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/3p32meV_base_T_resolution__-0p8_diff0p02.nxs',OutputWorkspace='MD_in')

Q, I, dI = mantid.plots.helperfunctions.get_md_data1d(MD_in,mantid.plots.helperfunctions.get_normalization(MD_in)[0])

#f=open('/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/saved_md/elastic_baseT_0meV_night3_refinedUB_histo_100bins.txt','w')
out=[]
for i in range(len(Q)):
    out.append([Q[i],I[i],dI[i]])
    out_np = np.array(out)
df = pd.DataFrame(out_np)
df.to_csv('/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/3p32meV_base_T_resolution__-0p8_diff0p02.txt', sep = '\t', na_rep = 'np.nan', index = 'False', Header = 'False')





 # plot inelastic IvsE
MD_inelastic_3p32meV_lowT_refinedUB_histo = BinMD(InputWorkspace='inelastic_3p32meV_lowT_refinedUB', 
            AlignedDim0='[0,K,0],-0.3,-0.1,1', 
            AlignedDim1='[0,0,L],-1.2,-0.8,1', 
            AlignedDim2='[H,0,0],-0.2,0.2,1', 
            AlignedDim3='DeltaE,-0.5,3.0,70', 
            OutputWorkspace='MD_inelastic_3p32meV_lowT_refinedUB_histo')
            
plotSlice(MD_inelastic_3p32meV_lowT_refinedUB_histo , normalization = 2)
SaveMD(MD_inelastic_3p32meV_lowT_refinedUB_histo, Filename = '/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/3p32meV_base_T_IvsE_0p2.nxs')


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os
import glob
from mantid import plots
import pandas as pd

import scipy.optimize as opt

MD_in=LoadMD(Filename = '/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/3p32meV_base_T_IvsE_0p2.nxs',OutputWorkspace='MD_in')

Q, I, dI = mantid.plots.helperfunctions.get_md_data1d(MD_in,mantid.plots.helperfunctions.get_normalization(MD_in)[0])

#f=open('/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/saved_md/elastic_baseT_0meV_night3_refinedUB_histo_100bins.txt','w')
out=[]
for i in range(len(Q)):
    out.append([Q[i],I[i],dI[i]])
    out_np = np.array(out)
df = pd.DataFrame(out_np)
df.to_csv('/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/3p32meV_base_T_IvsE_0p2.txt', sep = '\t', na_rep = 'np.nan', index = 'False', Header = 'False')
#f.write(df.values)
#f.close()

#IvsQ
MD_inelastic_3p32meV_lowT_refinedUB_histo = BinMD(InputWorkspace='inelastic_3p32meV_lowT_refinedUB', 
            AlignedDim0='[0,K,0],-1.5, 0.5,100', 
            AlignedDim1='[0,0,L],-1.2,-0.8,1', 
            AlignedDim2='[H,0,0],-0.2,0.2,1', 
            AlignedDim3='DeltaE,2.5,2.7,1', 
            OutputWorkspace='MD_inelastic_3p32meV_highT_refinedUB_histo')
            
plotSlice(MD_inelastic_3p32meV_lowT_refinedUB_histo , normalization = 2)
SaveMD(MD_inelastic_3p32meV_lowT_refinedUB_histo, Filename = '/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/3p32meV_base_T_IvsQ_E2p6.nxs')


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os
import glob
from mantid import plots
import pandas as pd

import scipy.optimize as opt

MD_in=LoadMD(Filename = '/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/3p32meV_base_T_IvsQ_E2p6.nxs',OutputWorkspace='MD_in')

Q, I, dI = mantid.plots.helperfunctions.get_md_data1d(MD_in,mantid.plots.helperfunctions.get_normalization(MD_in)[0])

#f=open('/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/saved_md/elastic_baseT_0meV_night3_refinedUB_histo_100bins.txt','w')
out=[]
for i in range(len(Q)):
    out.append([Q[i],I[i],dI[i]])
    out_np = np.array(out)
df = pd.DataFrame(out_np)
df.to_csv('/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/3p32meV_base_T_IvsQ_E2p6.txt', sep = '\t', na_rep = 'np.nan', index = 'False', Header = 'False')
#f.write(df.values)
#f.close()


#IvsE, 0p51
MD_inelastic_3p32meV_lowT_refinedUB_histo = BinMD(InputWorkspace='inelastic_3p32meV_lowT_refinedUB', 
            AlignedDim0='[0,K,0],-0.53, -0.49,1', 
            AlignedDim1='[0,0,L],-1.1,-0.9,1', 
            AlignedDim2='[H,0,0],-0.1,0.1,1', 
            AlignedDim3='DeltaE,-1.5,3,90', 
            OutputWorkspace='MD_inelastic_3p32meV_lowT_refinedUB_histo')
            
plotSlice(MD_inelastic_3p32meV_lowT_refinedUB_histo , normalization = 2)
SaveMD(MD_inelastic_3p32meV_lowT_refinedUB_histo, Filename = '/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/3_IvsE_k0p51_0p02_l0p01h_0p1.nxs')


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os
import glob
from mantid import plots
import pandas as pd

import scipy.optimize as opt

MD_in=LoadMD(Filename = '/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/3_IvsE_k0p51_0p02_l0p01h_0p1.nxs',OutputWorkspace='MD_in')

Q, I, dI = mantid.plots.helperfunctions.get_md_data1d(MD_in,mantid.plots.helperfunctions.get_normalization(MD_in)[0])

#f=open('/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/saved_md/elastic_baseT_0meV_night3_refinedUB_histo_100bins.txt','w')
out=[]
for i in range(len(Q)):
    out.append([Q[i],I[i],dI[i]])
    out_np = np.array(out)
df = pd.DataFrame(out_np)
df.to_csv('/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/3_IvsE_k0p51_0p02_l0p01h_0p1.txt', sep = '\t', na_rep = 'np.nan', index = 'False', Header = 'False')
#f.write(df.values)
#f.close()

#2Dplot

MD_elastic_baseT_3p32meV_night3_refinedUB_histo1 = BinMD(InputWorkspace='inelastic_3p32meV_lowT_refinedUB', 
            AlignedDim0='[0,K,0],-1.5,0.5,41', 
            AlignedDim1='[0,0,L],-3.0,0.5,41', 
            AlignedDim2='[H,0,0],-0.75,0.75,15', 
            AlignedDim3='DeltaE,-1.5,3,90', 
            OutputWorkspace='MD_2D_baseT_3p32meV_night3_refinedUB_histo1')

plotSlice(MD_elastic_baseT_3p32meV_night3_refinedUB_histo1, normalization = 2)

#Background IvsE
MD_inelastic_3p32meV_lowT_refinedUB_histo = BinMD(InputWorkspace='inelastic_3p32meV_lowT_refinedUB', 
            AlignedDim0='[0,K,0],-0.12, -0.08,1', 
            AlignedDim1='[0,0,L],-1.68,-1.48,1', 
            AlignedDim2='[H,0,0],-0.3,-0.1,1', 
            AlignedDim3='DeltaE,-1.5,3,90', 
            OutputWorkspace='MD_inelastic_3p32meV_lowT_refinedUB_histo')
            
plotSlice(MD_inelastic_3p32meV_lowT_refinedUB_histo , normalization = 2)
SaveMD(MD_inelastic_3p32meV_lowT_refinedUB_histo, Filename = '/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/3_IvsE_k-0p1_0p02_l-1p58_0p1h-0p2_0p1.nxs')


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os
import glob
from mantid import plots
import pandas as pd

import scipy.optimize as opt

MD_in=LoadMD(Filename = '/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/3_IvsE_k-0p1_0p02_l-1p58_0p1h-0p2_0p1.nxs',OutputWorkspace='MD_in')

Q, I, dI = mantid.plots.helperfunctions.get_md_data1d(MD_in,mantid.plots.helperfunctions.get_normalization(MD_in)[0])

#f=open('/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/saved_md/elastic_baseT_0meV_night3_refinedUB_histo_100bins.txt','w')
out=[]
for i in range(len(Q)):
    out.append([Q[i],I[i],dI[i]])
    out_np = np.array(out)
df = pd.DataFrame(out_np)
df.to_csv('/SNS/users/sbhatta9/data/SNS/CNCS/IPTS-20916/shared/Shiva/Shiva_2022/3_IvsE_k-0p1_0p02_l-1p58_0p1h-0p2_0p1.txt', sep = '\t', na_rep = 'np.nan', index = 'False', Header = 'False')
#f.write(df.values)
#f.close()
