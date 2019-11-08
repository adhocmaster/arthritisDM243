import pandas as pd


class ColumnFixer:
    
    
    def __init__(self):
        
        self.errors = []
        pass


    def fixDf(self, df: pd.DataFrame):
        
        df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('/', '').str.replace('(', '').str.replace(')', '')
        df.rename(columns=self.getNameMap(), inplace=True)
        self.populateErrors(df)

        return self.errors, df


    def populateErrors(self, df: pd.DataFrame):

        maxFixedSize = 0

        for fixedName in self.getNameMap().values():

            if len(fixedName) > maxFixedSize:
                maxFixedSize = len(fixedName)

            if fixedName not in df.columns:
                self.errors.append(f'{fixedName} not found in the fixed dataset')



        for colName in df.columns:
            if len(colName) > maxFixedSize:
                self.errors.append(f'{colName} was not from new names. It may be new or has invalid utf characters.')


        pass


    def getNameMap(self): 

        newColNames = {
            '[Gender]': 'Gender',
            'BirthdateYear (xxxx)': 'B_Year',
            '[Country]': 'Country',
            '[Onset_Age]': 'Onset_Age',
            '[Initial_Dx]': 'Initial_Dx',
            '[Dx_Change]': 'Dx_Change',
            '[New_Dx]': 'New_Dx',
            '[New_Dx]_If_you_answered_“yes”,_what_is_your_new_diagnosis_and_what_year_was_your_diagnosis_changed?_[other]': 'New_Dx_Year',
            '[Dx]_Diagnosis_Chosen': 'Dx_Chosen',
            '[Dr_Dx]': 'Dr_Dx', '[Dr_Dx_other]': 'Dr_Dx_other',   

            '[Prior_AD]': 'Prior_AD',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:__[Autoimmune_Hepatitis]': 'Prior_AD_Hep',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:__[Behcet’s_disease]': 'Prior_AD_Beh',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Celiac_disease]': 'Prior_AD_Cel',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Crohn’s_disease]': 'Prior_AD_Cro',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Discoid_lupus]': 'Prior_AD_Dis',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Endometriosis]': 'Prior_AD_End',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Evans_syndrome]': 'Prior_AD_Eva',

            
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Graves’_disease]': 'Prior_AD_Gra',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Hashimoto’s_thyroiditis]': 'Prior_AD_Has',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Hughes_Syndrome]': 'Prior_AD_Hug',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Interstitial_cystitis]': 'Prior_AD_Int',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Lyme_disease,_chronic]': 'Prior_AD_Lym',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Multiple_sclerosis]': 'Prior_AD_Mul',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Myocarditis]': 'Prior_AD_Myoc',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[MyositisPolymyositis]': 'Prior_AD_Myos',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Peripheral_neuropathy]': 'Prior_AD_Per',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Polymyalgia_rheumatica]': 'Prior_AD_Pol',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Reactive_ArthritisReiter’s_Syndrome]': 'Prior_AD_Rea',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Sarcoidosis]': 'Prior_AD_Sarcoidosis',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Scleritis]': 'Prior_AD_Scleritis',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Scleroderma]': 'Prior_AD_Scleroderma',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Thyroid_Disease]': 'Prior_AD_Thy',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Type_1_diabetes]': 'Prior_AD_Type_1',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Ulcerative_colitis]': 'Prior_AD_Ulcerative',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Vasculitis]': 'Prior_AD_Vasculitis',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Vitiligo]': 'Prior_AD_Vitiligo',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Other_Autoimmune_Disease_]': 'Prior_AD_Other_AD',

    
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Other_Autoimmune_Disease_]_[text]': 'Prior_AD_Other_AD_Text',
            '[Post_AD]_10._Since_your_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_have_you_ever_been_diagnosed_with_another_Autoimmune_Diseases_that_is_not_1_of_the_6_included_in_this_study_Rheumatoid_Arthritis,_Psoriatic_Arthritis,_Ankylosing_Spondylitis,_Sjögren’s_Syndrome,_Systemic_Lupus_Erythematosus,_and_Adult_Onset_Still’s_Disease?': 'Post_AD_',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Addison’s_disease]': 'Post_AD_Addison',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Autoimmune_Hepatitis]': 'Post_AD_Hep',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:[Autoimmune_myocarditis]': 'Post_AD_Myo',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Autoimmune_pancreatitis]': 'Post_AD_Pan',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Behcet’s_disease]': 'Post_AD_Beh',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Celiac_disease]': 'Post_AD_Cel',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Crohn’s_disease]': 'Post_AD_Cro',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[CREST_disease]': 'Post_AD_CRE',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Dermatomyositis]': 'Post_AD_Derma',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Discoid_lupus]': 'Post_AD_Dis',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Endometriosis]': 'Post_AD_End',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Hashimoto’s_thyroiditis]': 'Post_AD_Has',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Hughes_Syndrome]': 'Post_AD_Hug',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Interstitial_cystitis]': 'Post_AD_Has',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Lyme_disease,_chronic]': 'Post_AD_Lym',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[MyositisPolymyositis]': 'Post_AD_MyoPol',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Palindromic_rheumatism]': 'Post_AD_Pal',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Peripheral_neuropathy]': 'Post_AD_Per',

            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Polymyalgia_rheumatica]': 'Post_AD_Pol',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Reactive_ArthritisReiter’s_Syndrome]': 'Post_AD_Rea',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Relapsing_polychondritis]': 'Post_AD_Rel',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Scleritis]': 'Post_AD_Scleritis',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Scleroderma]': 'Post_AD_Scleroderma',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Thyroid_Disease]': 'Post_AD_Thy',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Type_1_diabetes]': 'Post_AD_Type_1',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Ulcerative_colitis]': 'Post_AD_Ulcerative',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Vasculitis]': 'Post_AD_Vasculitis',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Vitiligo]': 'Post_AD_Vitiligo',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Other_Autoimmune_Disease]': 'Post_AD_Other_AD',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Other_Autoimmune_Disease]_[text]': 'Post_AD_Other_AD_Text',
            '[Add_AAdx]_11._Since_your_original_diagnosis_of_an_Autoimmune_Arthritis_disease,_have_you_been_diagnosed_with_any_additional_or_secondary_Autoimmune_Arthritis_Diseases_Rheumatoid_Arthritis,_Psoriatic_Arthritis,_Ankylosing_Spondylitis,_Sjögren’s_Syndrome,_Systemic_Lupus_Erythematosus,_and_Adult_Onset_Still’s_Disease_in_addition_to_your_initial_diagnosis?': 'Add_AAdx_11',
            '[Add_AAdxRA]': 'Add_AAdxRA', '[Add_AAdxRADate]': 'Add_AAdxRADate',

            '[CFSyndrome]': 'CFSyndrome',
            '[Raynauds]_14._Prior_to_your_original_diagnosis_of_an_Autoimmune_Arthritis_disease,_were_you_diagnosed_with_Raynaud’s_Phenomenon?': 'Raynauds_14',
            '[Relatives_AD]': 'Relatives_AD', '[Mental_Stressors]': 'Mental_Stressors', '[Prior_virus]': 'Prior_virus',
            '[Virus]': 'Virus', '[Infection]': 'Infection', '[Pneumonia]': 'Pneumonia', '[Bronchitis]': 'Bronchitis',
            '[Virus_Uncertain': 'Virus_Uncertain', '[Virus_[Other]': 'Virus_Other', '[Virus_[Other]_[text]': 'Virus_Other_Text',
            
            ############### 100 done ###########################

            '[Give_Birth]': 'Give_Birth', 
            '[First_onset_visit]': 'First_onset_visit',
            '[First_onset_visit]_23.\tWhen_did_you_first_visit_your_primary_care_doctor,_health_specialist,_or_hospital_after_experiencing_your_initial_onset_symptoms?__[other]': 'First_onset_visit_other',
            '[first_dr_response]': 'first_dr_response', 
            '[first_dr_response_young': 'first_dr_response_young', 
            '[first_dr_response_nosymptoms':'first_dr_response_young',
            '[first_dr_response_nothing_wrong': 'first_dr_response_nothing_wrong', 
            '[first_dr_response_Other]': 'first_dr_response_Other',
            '[first_dr_response_Othertext]': 'first_dr_response_Other_Text',
            '[first_dr_response]_24.\tDuring_your_first_visit_to_discuss_your_initial_symptoms,_whether_with_your_primary_care_doctor_or_the_hospital,_were_you_told_any_of_the_statements_below_by_the_doctor_treating_your_case?__[None_of_these_apply]': 'first_dr_response_none',
            '[referral_time_mos': 'referral_time_mos', 
            '[num_specialists_unrelated': 'num_specialists_unrelated',
            '[Num_Rheum_Immun_todx]': 'Num_Rheum_Immun_todx',
            'Lankle_0_12': 'Ex1_1_Lankle_0_12', 
            'Rankle_0_12': 'Ex1_1_Rankle_0_12', 
            'Lknee_0_12': 'Ex1_1_Lknee_0_12',
            'Rknee_0_12': 'Ex1_1_Rknee_0_12',
            'Lelb_0_12': 'Ex1_1_Lelb_0_12', 
            'Relb_0_12': 'Ex1_1_Relb_0_12',
            

        }

        return newColNames
    