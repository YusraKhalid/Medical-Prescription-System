#This function asks for the symptoms from the user, then shortlist the diseases which have that symptom.
def symptoms(diseases):
    firstSymptom = input("If yes, enter one of these symptoms: ")
    shortListed = []

    for i in diseases:
        for j in i:
            if j == firstSymptom:
                shortListed.append(i)
    return  shortListed

def main():
    #writing symptoms of diseases
    allergy = ["nasal congestion", "itchy and watery eyes","sneezing", "runny nose", "sore throat", "throat clearing", "cough"]
    anemia = ['feel tired','weakness','fatigue', 'decreased energy', 'paleness', "palpitations", 'rapid heart rate', 'shortness of breath']
    anxiety = ['palpitations', 'sweating', 'irritability', 'stress']
    appendicits = ['abdominal pain', 'abdominal swelling','abdominal tenderness','back Pain','constipation','diarrhea','fever','loss of appetite','nausea','painful urination','rectal pain','vomiting']
    bladderInfection = ['bloody Urine','burning urination','difficulty urinating','abdominal pain','painful urination','pelvic or rectal pain','urinary fequency','urinary urgency']
    bloodClot = ['abdominal pain','chest pain','confusion','diarrhea','dizziness','headache','loss of sensation','neurological changes','numbness','pain','pallor','paralysis','problems with walking','redness','shortness of breath','slurred speech','swelling','vision changes','warmth','weakness']
    brainTumor = ['balance problems','gait disturbances','headache','hearing changes','memory problems','nausea','numbness','personality changes','seizures','speech changes','tingling','trouble concentrating','vision changes','vomiting','weakness']
    cancer = ['fatigue', 'weight loss', 'skin changes', 'change in bowel', 'unusual bleeding', 'persistent cough', 'voice change', 'fever', 'lumps or tissue masses']
    commonCold = ['body aches','cough','fatigue','fever','headache','nasal congestion','runny nose','sore throat','sneezing','watery eyes']
    colonCancer = ['abdominal cramping','abdominal mass','abdominal pain','abdominal tenderness','bloating','blood in stool','change in bowel habits','constipation','dark stool','diarrhea','fatigue','narrow stools','shortness of breath','weakness','weight loss']
    dengue = ['abdominal pain','bleeding gums','bone pain','difficulty breathing','easy bruising','pever','headache','joint pain','low back pain','muscle pain','nosebleeds','pain behind the eyes','rash','skin hemorrhages','swollen lymph nodes','vomiting']
    diabetes = ['blurred vision','dehydration','dry mouth','fatigue','frequent urination','hunger','increased susceptibility to infection','increased thirst','itching skin','nausea','slow-healing sores','weight gain','weight loss','yeast infections']
    scarletFever=['sore throat','fever','rash','red skin in elbow','strawberry tongue','headache' 'body aches','nausea', 'vomiting','abdominal pain','swollen glands']
    highBloodPressure=['shortness of breath','chest pain','blurred vision','dizziness','headache','leg swelling','nosebleeds','pounding sensation in the neck, chest, or ears']
    leukemia=['bleeding gums','bone pain','confusion','easy bruising','enlarged liver','enlarged spleen','fatigue','fever','headache','joint pain','loss of muscle control','nausea']
    lymeDiseases=['chills','dizziness','fever','headache','joint pain','joint swelling','loss of facial muscle tone','memory problems','muscle pains','numbness','palpitations']
    lungCancer=['chest pain','cough','depression','difficulty swallowing',"fatigue","headache","numbness",'seizures','shortness of breath','shoulder pain','tingling sensation','weakness','weight loss']
    ulcer=['indigestion','loss of appetite','abdominal pain','weight loss','heartburn','nausea','vomiting']
    osteoporosis = 	['back pain','fractures','loss of eight','neck pain','stooped posture']
    pancreaticCancer = ['abdominal pain','back pain','decreased appetite','diarrhea','fatigue','itching','jaundice','nausea','vomiting','weight loss']
    yellowFever = ['fever','headache', 'muscle aches']
    zikaVirusInfection = ['fever', 'rash', 'joint pain', 'redness of eyes','chills','fatigue','headache','muscle pain']
    throatCancer = ['bleeding in throat','cough','ear pain','headache','lump in throat','neck pain','painful swallowing','sore throat','swelling','trouble breathing','trouble speaking']
#diseases are written in list whose symptoms are in nested list.
    diseases = [allergy,anemia,anxiety,appendicits,bladderInfection,bloodClot,brainTumor,cancer,commonCold,colonCancer,dengue,diabetes,scarletFever,highBloodPressure,leukemia,lymeDiseases,lungCancer,ulcer,osteoporosis,pancreaticCancer,yellowFever,zikaVirusInfection,throatCancer]
#giving names of diseases the same index as they are in the list with respect to symptoms. So to write the name of the diseas from the list of its symbols program uses the index  of diseases to get name from nameOfDiseases.
    nameOfDiseases = ['Allergy','Anemia','Anxiety','Appendicits','Bladder Infection','Blood Clot','Brain Tumor','Cancer','Common Cold','Colon Cancer','Dengue','Diabetes','Scarlet Fever','High Blood Pressure','Leukemia','Lyme Diseases','Lung Cancer','Ulcer','Osteoporosis','Pancreatic Cancer','Yellow Fever','Zika Virus Infection','Throat Cancer']
    remedy = ['azelastine hydrochloride and fluticasone propionate (Dymista)', 'epoetin alfa, Epogen, Procrit', 'clomipramine (Anafranil)', 'ampicillin/sulbactam - injection, Unasyn','amoxicillin (Amoxil, Moxatag, Larotid)','Lovenox (enoxaparin)','bevacizumab - injection, Avastin','surgery, chemotherapy or radiation therapy.','Nonsteroidal Antiinflammatory Drugs (NSAIDs)','bevacizumab - injection, Avastin','codeine','Amaryl (glimepiride)','amoxicillin (Amoxil, Moxatag, Larotid)','ACE Inhibitors','alemtuzumab (Campath)','bevacizumab - injection, Avastin','Carafate (sucralfate)','alendronate, Fosamax, Binosto','cisplatin - injection, Platinol-AQ','Vaccination','acetaminophen', 'carboplatin - injection, Paraplatin']
#printing some of the symptoms of all diseases.
    print("""Do you have any of these symptoms:
        Running nose, cough, weakness, fatigue, shortness of breath, sweating, stress, abdominal pain, diarrhea, nausea, fever,
        painful urination, headache, vomitting, sore throat, back pain, neck pain?""")
#the user's input is used to shortlist the diseases.
    diseases01 = symptoms(diseases)
#the user's input is again used to shortlist the list of diseases.
    diseases02 = symptoms(diseases01)

#if the number of possible diseases is 1, printing that disease.
    if len(diseases02) == 2:
        for a in diseases02:
            index03 = diseases.index(a)
            print("You might have: ",nameOfDiseases[index03])
            print("All symptoms of this are: ",diseases[index03])#printing all the symptoms of the disease
            print("The cure for this can be: ",remedy[index03])
    else: #otherwise printing three symptoms of the disease for the user to further select.
        for m in diseases02:
            print(m[1])
            print(m[2])
            print(m[3])

        print("Do you have any of the above mentioned symptoms? ")
        diseases03 = symptoms(diseases02)


        for m in diseases02:
            print(m[1])
            print(m[2])
            print(m[3])

        print("Do you have any of the above mentioned symptoms? ")



        if len(diseases03) == 2:
            for a in diseases03:
                index04 = diseases.index(a)
                print("You might have: ",nameOfDiseases[index04])
                print("All symptoms of this are: ",diseases[index04]) #printing all the symptoms of the disease
                print("The cure for this can be: ",remedy[index04])

        else:
            diseases04 = symptoms(diseases03)

            for a in diseases04:
                index05 = diseases.index(a)
                print("You might have: ",nameOfDiseases[index05])
                print("All symptoms of this are: ",diseases[index05])
                print("The cure for this can be: ",remedy[index05])

main()





