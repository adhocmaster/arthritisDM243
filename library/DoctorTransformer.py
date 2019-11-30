import pandas as pd
import numpy as np

class DoctorTransformer:


    def __init__(self):
        pass

    #### Disease Transformation
    def getDiseasesMap(self):
        

        valMap = {
            'Nurse Practioner specializing in rheumatology': 'Nurse',
            'Internist then confirmed by a rheumatologist': 'Rheumatologist' ,
            'Neurologist thought it was MS': 'Neurologist',
            'Internist, Primary Care Physician': 'Physician',
            'Spine dr ran original blood test': 'Spine',
            'Sicca study': 'Sicca',
            'Internal Medicine': 'Internal Medicine',
            'Autonomic Neurologist': 'Neurologist',
            'Internist': 'Internist',
            'Infectious Disease Dr. & my Primary Dr & a Rheumatologist/internal medicine Dr.': 'Rheumatologist',
            'Infectious Disease': 'Infectious Disease',
            'Hematologist/Oncologist': 'Oncologist',
            'MRI technician, confirmed by Rheum ': 'Rheumatologist',
            'Physical Medicine and Rehab physician': 'Rehab Physician',
            'Infectious Disease Physician': 'Infectious Disease',
            'Internal Medicine Doctor': 'Internal Medicine',
            'Internal medicine': 'Internal Medicine',
            'infectious doctor from Vanderbilt at Williamson County Medical Center when I was in hospital 2013': 'Infectious Disease',
            'infectious Disease Dr & a Rheumatologist ': 'Rheumatologist',
            'physiotherapy clinic': 'clinic',
            'doctor': 'doctor',
            'Pain Management Practitioner': ,
            'Gastroenterologist': ,
            'gynecologist ': ,
            'infectious disease': ,
            'Orthopedist': ,
            'GI Clinic Nurse Practitioner ': ,
            'Mother-in-law found info online, I showed to GP. Tests positive. Rheum confirmed.': ,
            'Nero': ,
            'chiropractor': ,
            'dermatologist': ,
            'eye doctor': ,
            'Radiologist': ,
            'Gastroenterologist ': ,
            'renal consultant': ,
            'Renal Specialist': ,
            'Renal Physician': ,
            'Haematologist': ,
            'Neurologist': ,
            'Dermatologist: Lupus  and then Rheumatologist: Sjrogrens': ,
            
            ​


        }

        return valMap


    def transformDr_Dx(self, df: pd.DataFrame):
        
        return df

    