import os
from time import gmtime, strftime
import shutil

shutil.copytree('Master/XXXX_Master','Master/temp/XXXX_Master')

# - Get the info
projectNb = raw_input("Numero de projet..: ");
client = raw_input("Nom de client..: ");
Description = raw_input("Description..: ");

mainFolder = projectNb + '_' + client + '__' + Description

folderArray = [
                projectNb + '_' + '1Document',
                projectNb + '_' + '1Document/Images',
                projectNb + '_' + '1Document/Logos',
                projectNb + '_' + 'Collect',
                projectNb + '_' + 'Gestion_projet',
                projectNb + '_' + 'Gestion_projet/Client',
                projectNb + '_' + 'Gestion_projet/Documentation',
                projectNb + '_' + 'Gestion_projet/Fournisseur',
                projectNb + '_' + 'Gestion_projet/Planification',
                projectNb + '_' + 'Gestion_projet/Presentation',
                projectNb + '_' + 'Gestion_projet/Production',
                projectNb + '_' + 'Gestion_projet/Recherche',
                projectNb + '_' + 'Inter',
                projectNb + '_' + 'Inter/Maquette',
                projectNb + '_' + 'Inter/Maquette/Developpement',
                projectNb + '_' + 'Inter/Maquette/Developpement/Images',
                projectNb + '_' + 'Inter/Maquette/PDF',
                projectNb + '_' + 'Original_client',
                projectNb + '_' + 'Original_client/' + strftime("%Y-%M-%d"),
                projectNb + '_' + 'PDF',
                projectNb + '_' + 'PDF/PDF_LowRes',
                projectNb + '_' + 'PDF/PDF_X1',
                projectNb + '_' + 'Photos',
                projectNb + '_' + 'PSD',
                projectNb + '_' + 'Retreive_jeter',
                projectNb + '_' + 'WWW',
                projectNb + '_' + 'zTrash'
]

if not os.path.exists(mainFolder):
    os.rename('Master/temp/XXXX_Master', 'Master/temp/' + mainFolder)
    listFolder = os.listdir('Master/temp/' + mainFolder)
    print listFolder
    #for i in range(len(folderArray)):
     #   print "Creation de.." + mainFolder + '/' + folderArray[i]
      #  os.makedirs(mainFolder + '/' + folderArray[i])
else:
    print "Le projet existe deja :("


