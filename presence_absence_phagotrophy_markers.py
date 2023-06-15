# -*- coding: utf-8 -*-

# Aim of this code: drawing a list of presence/absence of markers in genomes of ~ 100 cultivated Dinoflagellate species
# Code is run on ABIMS cluster: http://abims.sb-roscoff.fr/

# Modules
import os
import numpy as np
import pandas as pd
import re # regular expression (to find aliases of proteins' names)

# Directory containing files with reference species, functionally annotated
rep=os.listdir('/shared/projects/darkdino/finalresult/05_annotation/tsv_corrected/file_modif/')

directory='/shared/projects/darkdino/finalresult/05_annotation/tsv_corrected/file_modif/'
# Directory where to store the output file
output_dir='/shared/projects/darkdino/finalresult/05_annotation/tsv_corrected/file_modif/Output_modif/'

### Define tags for the markers of phagotrophy
# Tags I am looking for in the proteins' names
# Ensemble of necessary (not sufficient) proteins required for phagotrophy

# Small GTPases
rab=re.compile('RAB',re.IGNORECASE) #IGNORECASE ==> I don't care if it's lower or uppercase characters
rac=re.compile('RAC.GTP', re.IGNORECASE)
rap=re.compile('RAP.GTP',re.IGNORECASE)
cdc=re.compile('CDC42',re.IGNORECASE)
rho=re.compile('Rho.GTP',re.IGNORECASE)

#Phosphatidylinositol 3 phosphate 4 kinase (required for invagination of large particles)
pho=re.compile('phosphatidylinositol.3.phosphate',re.IGNORECASE) #dot = matches any character (like * in linux)
#kin=re.compile('kinase',re.IGNORECASE)

# WASH complex : Nucleation-promoting factor, interacting with Arp2/3 in actin polymerization process
wash=re.compile('WASH',re.IGNORECASE)
wasp=re.compile('WASP',re.IGNORECASE)

# SNARE: vesicular transport
snare=re.compile('SNARE',re.IGNORECASE)

# Cathepsins : proteases involved in the resolution (digestion) step
cat=re.compile('Cathepsin',re.IGNORECASE)

# Is my organism a phototroph ?
chl=re.compile('cytochrome',re.IGNORECASE)

#mixo=[chl,rab,rac,rap,cdc,rho,pho,wash,wasp,snare,cat] #list storing the phagotrophic markers' aliases (type re.Pattern)
mixo=[cat,cdc,chl,pho,rab,rac,rap,rho,snare,wash,wasp]

df=pd.DataFrame(columns=rep)

### Loop on the files

for filename in rep: # Loop on the files stored in the directory
    print(filename)
    species=filename[:-4] # Keep the species' ID (get rid of the .tsv)
    if str(filename)[-4:]=='.tsv': # il se trouve que ça marche
        file=pd.read_table(directory+str(filename))

        proteins=file['signature_description'] # in this column, I search for the markers' names

        mymarkers={'Cat':False,'Cdc':False,'Chl':False,'Pho':False,'Rab':False,'Rac':False,'Rap':False,'Rho':False,'Snare':False,'Wash':False,'Wasp':False}
        series_markers=pd.Series(mymarkers)

        print(series_markers)

        for index in range(len(proteins)): # Loop on the lines of the file: examine each protein
            prot=str(proteins[index])
            #print(index,prot)
            for i in range(len(mixo)):
                marker=mixo[i]
                #print(marker)
                find=marker.match(prot)
                if find:
                    if series_markers[i]==False:
                        print('Found : ', marker)
                    series_markers[i]=True
        print(series_markers)

        df[filename]=series_markers
    
print(df)

df.to_csv(output_dir+'example.tsv', sep="\t")



