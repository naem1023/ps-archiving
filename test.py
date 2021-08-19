# Based on Kaggle kernel by Scirpus

import xlearn as xl


def convert_to_ffm(df, type, numerics, categories, features):

    currentcode = len(numerics)

    catdict = {}

    catcodes = {}

    # Flagging categorical and numerical fields

    for x in numerics:

        catdict[x] = 0

    for x in categories:

        catdict[x] = 1

    nrows = df.shape[0]

    ncolumns = len(features)

    with open(str(type) + "_ffm.txt", "w") as text_file:

        # Looping over rows to convert each row to libffm format

    for n, r in enumerate(range(nrows)):

        datastring = ""

        datarow = df.iloc[r].to_dict()

        datastring += str(int(datarow['Label']))

        # For numerical fields, we are creating a dummy field here

        for i, x in enumerate(catdict.keys()):

            if(catdict[x] == 0):

                datastring = datastring + " " + \
                    str(i)+":" + str(i)+":" + str(datarow[x])

            else:

                # For a new field appearing in a training example

                if(x not in catcodes):

                    catcodes[x] = {}

                    currentcode += 1

                    # encoding the feature
                    catcodes[x][datarow[x]] = currentcode

        # For already encoded fields

                elif(datarow[x] not in catcodes[x]):

                    currentcode += 1

                    # encoding the feature
                    catcodes[x][datarow[x]] = currentcode

                code = catcodes[x][datarow[x]]

                datastring = datastring + " "+str(i)+":" + str(int(code))+":1"

        datastring += '\n'

        text_file.write(datastring)


ffm_model = xl.create_ffm()

ffm_model.setTrain("criteo.tr.r100.gbdt0.ffm")

ffm_model.setValidate("criteo.va.r100.gbdt0.ffm")


param = {'task': 'binary',  # ‘binary’ for classification, ‘reg’ for Regression

         'k': 2,           # Size of latent factor

         'lr': 0.1,        # Learning rate for GD

         'lambda': 0.0002,  # L2 Regularization Parameter

         'Metric': 'auc',  # Metric for monitoring validation set performance

         'epoch': 25       # Maximum number of Epochs

         }


ffm_model.fit(param, "model.out")
