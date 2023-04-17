import csv

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#
# def output_method_doc():
#     import csv
#     with open('input.txt','r', encoding='utf8') as inputFile, open('output.csv','w',newline='', encoding='utf8') as outputFile:
#         csvwriter=csv.writer(outputFile)
#
#         for line in inputFile:
#             line=line.strip()
#             print(line)
#
#             method_form=line.split(',')
#             method_name2=method_form[3].split("'");
#             method_name=method_name2[1]
#
#             class_name=method_form[2].replace("'" , '')
#
#
#             with open('android.csv', 'r', encoding='utf8') as csvFile:
#                 csvReader = csv.reader(csvFile)
#
#                 for i,row in enumerate(csvReader):
#                     if(row[3] == method_name):
#                         print('match')
#
#                         # making sentence
#                         sentence2 = 'method ' + row[3] + ' of class ' + row[2]
#                         if (len(row[6]) != 0):
#                             sentence2 = sentence2 + ' has parameter ' + row[6]
#                         if (len(row[7]) != 0):
#                            sentence2 = sentence2 + ' returns ' + row[7]
#                         if (len(row[5]) != 0):
#                            sentence2 = sentence2 + '. ' + row[5]
#                         if (len(row[8]) != 0):
#                            sentence2 = sentence2 + '. ' + row[8]
#                         csvwriter.writerow([sentence2])
#         #outputFile.close()
#


def get_information_type():
    info_type=['Service','Data','ways','Times','Detail','User account','name','Surname','Password','Email','Address','Telephone number','Postal address','Country','Bank information','Date of birth','Personal data','Recipient','Necessary consent','Shipment','Platform','Service','Location','Ip address','Trips','Identification code','Navigation','Dates','Platform','Hardware','Software','Information','Social networks','User','Personal data','Incident','Privacy policy','Personal information','Person','Death certificate','DNI','Photocopy','Valid passport','Relationship','Kinship','Documentation','Deceased person']
    return info_type


def generate_method_signature_combinations(sourceMethodList):
    with open('android.csv','r',encoding='utf8') as csvFile:
        csvReader= csv.reader(csvFile)

        header = next(csvReader)

        row_count=0
        method_signature = [[None]*4 for _ in range(202)]

        for row in csvReader:


            for i in range(len(sourceMethodList)):
                strValue = sourceMethodList[i].split(',')
                if (strValue[3].strip()== row[3].strip() and strValue[1].strip()==row[1].strip()):
                    print(strValue[3])
                    # method_signature_combination_1
                    # Method + Class + Parameter + Return type + Method Description + Class description
                    sentence1= 'method ' + row[3]+ ' of class '+ row[2] + ' has parameters '+row[6] + ' returns '+row[7]+ row[5]+row[8]

                    # method_signature_combination_2
                    # Method + Class + Parameter + Return type + Method Description
                    sentence2 = 'method ' + row[3] + ' of class ' + row[2] + ' has parameters '+row[6] + ' returns '+row[7] + row[5]

                    # method_signature_combination_3
                    # Method + Class + Parameter + Return type
                    sentence3 = 'method ' + row[3]+ ' of class '+ row[2] + ' has parameters '+row[6] + ' returns '+row[7]

                    # method_signature_combination_4
                    # Method + Class + Parameter
                    sentence4 = 'method ' + row[3]+ ' of class '+ row[2] + ' has parameters '+row[6]

                    if(row_count <=200):
                        method_signature[row_count][0] = sentence1
                        method_signature[row_count][1] = sentence2
                        method_signature[row_count][2] = sentence3
                        method_signature[row_count][3] = sentence4
                        row_count = row_count + 1

    for i in range(len(method_signature)):
        #print(method_signature[i][2])
        try_other_models(method_signature[i][1])

    print('ok')



def try_other_models(method_signature):
     with open('method signature combinations.csv', 'a', newline='', encoding='utf8') as outputFile:
        txtWriter = csv.writer(outputFile)

        txtWriter.writerow([method_signature])

        info_types = get_information_type()
        info_types.insert(0, 'Method combinations')
        txtWriter.writerow(info_types)
        info_types.pop(0)

        # for each model, take mothod combination, for each combination, find cosine similarity between several info_types
        # for model all-MiniLM-L6-v2
        #
        txtWriter.writerow(["all-MiniLM-L6-v2"])
        from sentence_transformers import SentenceTransformer
        from sentence_transformers import util

        model1 = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

        # for row in range(len(method_signature)-95):
        #     row_info = [method_signature[row][0]]
        #     embedding1 = model1.encode(method_signature[row][0], convert_to_tensor=True)
        #
        #     for i in range(len(info_types)):
        #         embedding2 = model1.encode(info_types[i], convert_to_tensor=True)
        #         cosine_scores = util.pytorch_cos_sim(embedding1, embedding2)
        #         row_info.append(str(cosine_scores.item()))
        #
        #     txtWriter.writerow(row_info)

        row_info = [method_signature]
        embedding11 = model1.encode(method_signature, convert_to_tensor=True)

        for i in range(len(info_types)):
            embedding12 = model1.encode(info_types[i], convert_to_tensor=True)
            cosine_scores = util.pytorch_cos_sim(embedding11, embedding12)
            row_info.append(str(cosine_scores.item()))

        txtWriter.writerow(row_info)

        # model 2 all-mpnet-base-v2
        txtWriter.writerow(["all-mpnet-base-v2"])
        model2 = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

        row_info.clear()
        row_info = [method_signature]
        embedding21 = model2.encode(method_signature, convert_to_tensor=True)

        for i in range(len(info_types)):
            embedding22 = model2.encode(info_types[i], convert_to_tensor=True)
            cosine_scores = util.pytorch_cos_sim(embedding21, embedding22)
            row_info.append(str(cosine_scores.item()))

        txtWriter.writerow(row_info)

        # model 3 roberta-base
        txtWriter.writerow(["roberta-base"])

        from transformers import AutoModel, AutoTokenizer
        from sentence_transformers import util
        model_name = 'roberta-base'
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model3 = AutoModel.from_pretrained(model_name)

        row_info.clear()
        row_info = [method_signature]
        encoded_input31 = tokenizer(method_signature, return_tensors='pt')
        output1 = model3(**encoded_input31)
        embedding31 = output1.last_hidden_state.mean(dim=1)

        for i in range(len(info_types)):
            encoded_input32 = tokenizer(info_types[i], return_tensors='pt')
            output2 = model3(**encoded_input32)
            embedding32 = output2.last_hidden_state.mean(dim=1)
            cosine_scores = util.pytorch_cos_sim(embedding31, embedding32)
            row_info.append(str(cosine_scores.item()))

        txtWriter.writerow(row_info)

        # model 4 stsb-roberta-base
        txtWriter.writerow(["stsb-roberta-base"])
        from sentence_transformers import CrossEncoder
        model4 = CrossEncoder('cross-encoder/stsb-roberta-base')

        row_info.clear()
        row_info = [method_signature]

        for i in range(len(info_types)):
            scores = model4.predict((method_signature, info_types[i]))
            row_info.append(str(scores))
        txtWriter.writerow(row_info)

        # model 5 multi-qa-mpnet-base-cos-v1
        txtWriter.writerow(["multi-qa-mpnet-base-cos-v1"])
        model5 = SentenceTransformer('sentence-transformers/multi-qa-mpnet-base-cos-v1')

        row_info.clear()
        row_info = [method_signature]
        embedding51 = model5.encode(method_signature, convert_to_tensor=True)

        for i in range(len(info_types)):
            embedding52 = model5.encode(info_types[i], convert_to_tensor=True)
            cosine_scores = util.pytorch_cos_sim(embedding51, embedding52)
            row_info.append(str(cosine_scores.item()))

        txtWriter.writerow(row_info)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    method_combinations=  ['android, os, Bundle, putBoolean',
    'android, location, Location, getLongitude',
    'android, location, Location, getLatitude',
    'android, content, SharedPreferences, putString',
    'android, telephony, TelephonyManager, getDeviceId',
    'android, os, Bundle, putParcelable',
    'java, lang, String, replace',
    'java, net, HttpURLConnection, getInputStream',
    'android, os, Bundle, putFloat',
    'android, util, Log, e',
    'android, database, Cursor, getString',
    'android, os, Bundle, putInt',
    'android, location, LocationManager, getLastKnownLocation',
    'java, util, Locale, getCountry',
    'android, os, Bundle, putString',
    'android, util, Log, d',
    'android, content, ContentResolver, query',
    'android, util, Log, w']

    generate_method_signature_combinations(method_combinations)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
