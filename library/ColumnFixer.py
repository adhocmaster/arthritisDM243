import pandas as pd


class ColumnFixer:
    
    
    def __init__(self):
        
        self.errors = []
        pass


    def fixClassColumn(self, df: pd.DataFrame):
        """It depends on column names after fixing the df columns.
        
        Arguments:
            df {pd.DataFrame} -- [description]
        """


    def fixDf(self, df: pd.DataFrame):
        
        df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('+', 'plus').str.replace('/', '').str.replace('(', '').str.replace(')', '').str.replace('[', '').str.replace(']', '')
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
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Endometriosis]': 'Prior_AD_Endo',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Evans_syndrome]': 'Prior_AD_Eva',

            
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Graves’_disease]': 'Prior_AD_Gra',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Hashimoto’s_thyroiditis]': 'Prior_AD_Hashi',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Hughes_Syndrome]': 'Prior_AD_Hug',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Interstitial_cystitis]': 'Prior_AD_Int',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Lyme_disease,_chronic]': 'Prior_AD_Lym',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Multiple_sclerosis]': 'Prior_AD_Mul',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Myocarditis]': 'Prior_AD_Myoc',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[MyositisPolymyositis]': 'Prior_AD_Myos',
            '[Prior_ADs]_Prior_to_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Peripheral_neuropathy]': 'Prior_AD_Peri',
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
            '[Post_AD]_10._Since_your_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_have_you_ever_been_diagnosed_with_another_Autoimmune_Diseases_that_is_not_1_of_the_6_included_in_this_study_Rheumatoid_Arthritis,_Psoriatic_Arthritis,_Ankylosing_Spondylitis,_Sjögren’s_Syndrome,_Systemic_Lupus_Erythematosus,_and_Adult_Onset_Still’s_Disease?': 'Post_AD_AD',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Addison’s_disease]': 'Post_AD_Addison',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Autoimmune_Hepatitis]': 'Post_AD_Hep',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:[Autoimmune_myocarditis]': 'Post_AD_Myo',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Autoimmune_pancreatitis]': 'Post_AD_Pan',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Behcet’s_disease]': 'Post_AD_Beh',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Celiac_disease]': 'Post_AD_Cel',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Crohn’s_disease]': 'Post_AD_Cro',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[CREST_disease]': 'Post_AD_CRE',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Dermatomyositis]': 'Post_AD_Derma',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Discoid_lupus]': 'Post_AD_Disc',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Endometriosis]': 'Post_AD_Endo',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Hashimoto’s_thyroiditis]': 'Post_AD_Hashi',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Hughes_Syndrome]': 'Post_AD_Hug',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Interstitial_cystitis]': 'Post_AD_Inter',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Lyme_disease,_chronic]': 'Post_AD_Lym',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[MyositisPolymyositis]': 'Post_AD_MyoPol',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Palindromic_rheumatism]': 'Post_AD_Pal',
            '[Post_ADs]_Since_my_firstoriginal_diagnosis_of_an_Autoimmune_Arthritis_disease,_I_was_diagnosed_with:_[Peripheral_neuropathy]': 'Post_AD_Peri',

            
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

            '[Give_Birth]': 'Give_Birth', 
            '[First_onset_visit]': 'First_onset_visit',
            '[First_onset_visit]_23.\tWhen_did_you_first_visit_your_primary_care_doctor,_health_specialist,_or_hospital_after_experiencing_your_initial_onset_symptoms?__[other]': 'First_onset_visit_other',
            '[first_dr_response]': 'first_dr_response', 
            '[first_dr_response_young': 'first_dr_response_young', 
            '[first_dr_response_nosymptoms':'first_dr_response_no_symptoms',
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

            'LShd_0_12': 'Ex1_1_LShd_0_12', 
            'RShd_0_12': 'Ex1_1_RShd_0_12', 
            'Lhip_0_12': 'Ex1_1_Lhip_0_12', 
            'Rhip_0_12': 'Ex1_1_Rhip_0_12', 
            '[N_Ex1_0_12': 'Ex1_1_0_12_None', 
            'Ex1_Other': 'Ex1_1_Other', 
            'FS_LAnk': 'Ex1_1_FS_LAnk', 
            'FS_Rank': 'Ex1_1_FS_Rank', 
            '[FS_LKn]': 'Ex1_1_FS_LKn', 
            '[FS_Rknee': 'Ex1_1_FS_Rknee', 
            '[FS_Lelb': 'Ex1_1_FS_Lelb', 
            '[FS_Relb': 'Ex1_1_FS_Relb', 
            '[FS_LShld': 'Ex1_1_FS_LShld', 
            'FS_RShld': 'Ex1_1_FS_RShld', 
            '[FS_Lhip': 'Ex1_1_FS_Lhip', 
            '[FS_Rhip': 'Ex1_1_FS_Rhip', 
            
            '12_24LAnk': 'Ex1_2_12_24LAnk',
            '12_24RAnk': 'Ex1_2_12_24RAnk',
            '12_24LKnee': 'Ex1_2_12_24LKnee',
            '12_24RKnee': 'Ex1_2_12_24RKnee',
            '12_24LElb': 'Ex1_2_12_24LElb',
            '12_24RElb': 'Ex1_2_12_24RElb',
            '12_24LShld': 'Ex1_2_12_24LShld',
            '12_24RShld': 'Ex1_2_12_24RShld',
            '12_24LHip': 'Ex1_2_12_24LHip',
            '12_24RHip': 'Ex1_2_12_24RHip',
            'N_Ex1_12_24': 'Ex1_2_12_24_None',
            
            'Ex1_24_plus': 'Ex1_2_24_plus',
            'LAnk_24plus': 'Ex1_2_LAnk_24plus',
            'RAnk_24plus': 'Ex1_2_RAnk_24plus',    
            
            'LKnee_24plus': 'Ex1_2_LKnee_24plus',
            'RKnee_24plus': 'Ex1_2_RKnee_24plus',
            'LElb_24plus': 'Ex1_2_LElb_24plus',
            'RElb_24plus': 'Ex1_2_RElb_24plus',
            'LShld_24plus': 'Ex1_2_LShld_24plus',
            'RShld_24plus': 'Ex1_2_RShld_24plus',
            'LHip_24plus': 'Ex1_2_LHip_24plus',
            'RHip_24plus': 'Ex1_2_RHip_24plus',
            
            #Ex2_3
            'Lhand_0_12': 'Ex2_3_Lhand_0_12',
            'Rhand_0_12': 'Ex2_3_Rhand_0_12',
            'LWr_0_12': 'Ex2_3_LWr_0_12',
            'RWr_0_12': 'Ex2_3_RWr_0_12',
            'N_Ex2_0_12': 'Ex2_3_0_12_None',
            'FS_Lhand': 'Ex2_3_FS_Lhand',
            'FS_Rhand': 'Ex2_3_FS_Rhand',
            'FS_LWr': 'Ex2_3_FS_LWr',
            'FS_RWr': 'Ex2_3_FS_RWr',
            'LHand_ABCJoint_0_12': 'Ex2_3_LHand_ABCJoint_0_12',
            'RHand_ABCJoint_0_12': 'Ex2_3_RHand_ABCJoint_0_12',
            
            #Ex2_4
            'Lhand_12_24': 'Ex2_4_Lhand_12_24',
            'RHand_12_24': 'Ex2_4_RHand_12_24',
            'LWr_12_24': 'Ex2_4_LWr_12_24',
            'RWr_12_24': 'Ex2_4_RWr_12_24',
            
            'N_Ex2_12_24': 'Ex2_4_12_24_None',
            
            'LHand_24_plus': 'Ex2_4_LHand_24_plus',
            'RHand_24_plus': 'Ex2_4_RHand_24_plus',
            'LWr_24_plus': 'Ex2_4_LWr_24_plus',
            'RWr_24_plus': 'Ex2_4_RWr_24_plus',
            'LHand_ABCJoints_12_24': 'Ex2_4_LHand_ABCJoints_12_24',
            'RHand_ABCJoints_12_24': 'Ex2_4_RHand_ABCJoints_12_24',

            
            #Ex3_5
            'LToes_0_12': 'Ex3_5_LToes_0_12',
            'RToes_0_12': 'Ex3_5_RToes_0_12',
            'LFt_Top_0_12': 'Ex3_5_LFt_Top_0_12',
            'RFt_Top_0_12': 'Ex3_5_RFt_Top_0_12',
            'LFt_BackBtmHeel_0_12': 'Ex3_5_LFt_BackBtmHeel_0_12',
            'RFt_BackBtmHeel_0_12': 'Ex3_5_RFt_BackBtmHeel_0_12',
            'LFt_Achilles_0_12': 'Ex3_5_LFt_Achilles_0_12',
            'RFt_Achilles_0_12': 'Ex3_5_RFt_Achilles_0_12',
            'LFt_Btm_ball_0_12': 'Ex3_5_LFt_Btm_ball_0_12',
            'RFt_Btm_ball_0_12': 'Ex3_5_RFt_Btm_ball_0_12',
            'N_Ex3_0_12': 'Ex3_5_0_12_None',
            
            'FS_LToes': 'Ex3_5_FS_LToes',
            'FS_RToes': 'Ex3_5_FS_RToes',
            'FS_LFt_Top': 'Ex3_5_FS_LFt_Top',
            'FS_RFt_Top': 'Ex3_5_FS_RFt_Top',
            'FS_LFt_BackBtmHeel': 'Ex3_5_FS_LFt_BackBtmHeel',
            'FS_RFt_BackBtmHeel': 'Ex3_5_FS_RFt_BackBtmHeel',
            'FS_LFt_Achilles': 'Ex3_5_FS_LFt_Achilles',
            'FS_RFt_Achilles': 'Ex3_5_FS_RFt_Achilles',
            'FS_LFt_Btm_ball': 'Ex3_5_FS_LFt_Btm_ball',
            'FS_RFt_Btm_ball': 'Ex3_5_FS_RFt_Btm_ball',
            
            #Ex3_6
            'LToes_12_24': 'Ex3_6_LToes_12_24',
            'RToes_12_24': 'Ex3_6_RToes_12_24',
            'LFt_Top_12_24': 'Ex3_6_LFt_Top_12_24',
            'RFt_Top_12_24': 'Ex3_6_RFt_Top_12_24',
            'LFt_BackBtmHeel_12_24': 'Ex3_6_LFt_BackBtmHeel_12_24',
            'RFt_BackBtmHeel_12_24': 'Ex3_6_RFt_BackBtmHeel_12_24',
            'LFt_Achilles_12_24': 'Ex3_6_LFt_Achilles_12_24',
            'RFt_Achilles_12_24': 'Ex3_6_RFt_Achilles_12_24',
            'LFt_Btm_ball_12_24': 'Ex3_6_LFt_Btm_ball_12_24',
            'RFt_Btm_ball_12_24': 'Ex3_6_RFt_Btm_ball_12_24',
            'N_Ex3_12_24': 'Ex3_6_N_Ex3_12_24',
            'LToes_24p': 'Ex3_6_LToes_24p',
            'RToes_24p': 'Ex3_6_RToes_24p',
            'LFt_Top_24p': 'Ex3_6_LFt_Top_24p',
            'RFt_Top_24p': 'Ex3_6_RFt_Top_24p',
            'LFt_BackBtmHeel_24p': 'Ex3_6_LFt_BackBtmHeel_24p',
            'RFt_BackBtmHeel_24p': 'Ex3_6_RFt_BackBtmHeel_24p',
            'LFt_Achilles_24p': 'Ex3_6_LFt_Achilles_24p',
            'RFt_Achilles_24p': 'Ex3_6_RFt_Achilles_24p',
            

            'LFt_Btm_ball_24p': 'Ex3_6_LFt_Btm_ball_24p',
            'RFt_Btm_ball_24p': 'Ex3_6_RFt_Btm_ball_24p',
            
            #Ex4_7
            'RJaw_0_12': 'Ex4_7_RJaw_0_12',
            'LJaw_0_12': 'Ex4_7_LJaw_0_12',
            'Neck_0_12': 'Ex4_7_Neck_0_12',
            'UpBack_0_12': 'Ex4_7_UpBack_0_12',
            'MidBack_0_12': 'Ex4_7_MidBack_0_12',
            'LowBack_0_12': 'Ex4_7_LowBack_0_12',
            'Sac_0_12': 'Ex4_7_Sac_0_12',
            'RSb_0_12': 'Ex4_7_RSb_0_12',
            'LSb_0_12': 'Ex4_7_LSb_0_12',
            'N_Ex4_0_12': 'Ex4_7_N_Ex4_0_12',
            'FS_RJaw': 'Ex4_7_FS_RJaw',
            'FS_LJaw': 'Ex4_7_FS_LJaw',
            'FS_Neck': 'Ex4_7_FS_Neck',
            'FS_UpBack': 'Ex4_7_FS_UpBack',
            'FS_MidBack': 'Ex4_7_FS_MidBack',
            'FS_LBack': 'Ex4_7_FS_LBack',
            'FS_Sac': 'Ex4_7_FS_Sac',
            'FS_RSb': 'Ex4_7_FS_RSb',
            'FS_LSb': 'Ex4_7_FS_LSb',
            
            #Ex4_8

            'RJaw_12_24': 'Ex4_8_RJaw_12_24',
            'LJaw_12_24': 'Ex4_8_LJaw_12_24',
            'Neck_12_24': 'Ex4_8_Neck_12_24',
            'UpBack_12_24': 'Ex4_8_UpBack_12_24',
            'MidBack_12_24': 'Ex4_8_MidBack_12_24',
            'LowBack_12_24': 'Ex4_8_LowBack_12_24',
            'Sac_12_24': 'Ex4_8_Sac_12_24',
            'RSb_12_24': 'Ex4_8_RSb_12_24',
            'LSb_12_24': 'Ex4_8_LSb_12_24',

            

            'N_Ex4_12_24': 'Ex4_8_12_24_None',
            'RJaw_24p': 'Ex4_8_RJaw_24p',
            'LJaw_24p': 'Ex4_8_LJaw_24p',
            'Neck_24p': 'Ex4_8_Neck_24p',
            'UpBack_24p': 'Ex4_8_UpBack_24p',
            'MidBack_24p': 'Ex4_8_MidBack_24p',
            'LBack_24p': 'Ex4_8_LBack_24p',
            'Sac_24p': 'Ex4_8_Sac_24p',
            'RSb_24p': 'Ex4_8_RSb_24p',
            'LSb_24p': 'Ex4_8_LSb_24p',
            
            #Ex5_9
            'Pv_0_12': 'Ex5_9_Pv_0_12',
            'RSJ_0_12': 'Ex5_9_RSJ_0_12',
            'Th_0_12': 'Ex5_9_Th_0_12',
            'N_Ex5_0_12': 'Ex5_9_0_12_None',
            
            'FS_Pv': 'Ex5_9_FS_Pv',
            'FS_RSJ': 'Ex5_9_FS_RSJ',
            'FS_Th': 'Ex5_9_FS_Th',
            
            #Ex5_10
            'Pv_12_24': 'Ex5_10_Pv_12_24',
            'RSJ_12_24': 'Ex5_10_RSJ_12_24',
            'Th_12_24': 'Ex5_10_Th_12_24',
            'N_Ex5_12_24': 'Ex5_10_12_24_None',
            'Pv_24p': 'Ex5_10_Pv_24p',
            'RSJ_24p': 'Ex5_10_RSJ_24p',
            'Th_24p': 'Ex5_10_Th_24p',
            
            #Ex5_11
            
            'Red_Wm_24': 'Ex5_11_Red_Wm_24',
            'FS_Red_Wm': 'Ex5_11_FS_Red_Wm',
            
            #Ex5_12

            'Sw_24': 'Ex5_12_Sw_24',
            'FS_Sw': 'Ex5_12_FS_Sw',
            
            #Ex5_13
            'Jt_2wk_0_12': 'Ex5_13_Jt_2wk_0_12',
            
            #Ex5_14
            
            'Ch_24': 'Ex5_14_Ch_24',
            
            'Ch_Dx_pleurisy': 'Ex5_14_Ch_Dx_pleurisy',
            'Ch_Dx_pericarditis': 'Ex5_14_Ch_Dx_pericarditis',
            'Ch_Dx_pleural_effusion': 'Ex5_14_Ch_Dx_pleural_effusion',
            'Ch_Dx_pericardial_effusion': 'Ex5_14_Ch_Dx_pericardial_effusion',
            'Ch_Dx_heart_infl': 'Ex5_14_Ch_Dx_heart_infl',
            'Ch_Dx_lung_infl': 'Ex5_14_Ch_Dx_lung_infl',
            'Ch_Dx_costo': 'Ex5_14_Ch_Dx_costo',
            'Ch_Dx_enthesitis': 'Ex5_14_Ch_Dx_enthesitis',
            'Ch_Dx_gen_infl': 'Ex5_14_Ch_Dx_gen_infl',
            'Ch_Dx_stress_injury': 'Ex5_14_Ch_Dx_stress_injury',
            'Ch_Y_NoDx': 'Ex5_14_Ch_Y_NoDx',
            'Ch_Dx_IDR': 'Ex5_14_Ch_Dx_IDR',
            'FS_Ch': 'Ex5_14_FS_Ch',
            
            #Ex5_15
            'ShortBr_0_24': 'Ex5_15_ShortBr_0_24',
            'FS_ShortBr': 'Ex5_15_FS_ShortBr',
            
            #Ex5_16
            'Stiff_0_12': 'Ex5_16_Stiff_0_12',
            'FS_Stiff': 'Ex5_16_FS_Stiff',
            'Stiff_duration': 'Ex5_16_Stiff_duration',
            
            #Ex5_17
            'Stiff_Sit_0_12': 'Ex5_17_Stiff_Sit_0_12',
            'FS_Stiff_Sit': 'Ex5_17_FS_Stiff_Sit',
            
            #Ex5_18
            'Furn_0_12': 'Ex5_18_Furn_0_12',
            'FS_Furn': 'Ex5_18_FS_Furn',
            
            #Ex5_19
            'Fv_24': 'Ex5_19_Fv_24',
            'FS_Fv': 'Ex5_19_FS_Fv',
            'Fv_Type': 'Ex5_19_Fv_Type',
            'Fv_Higher_0_12': 'Ex5_19_Fv_Higher_0_12',
            'Fv_Morn_Peak': 'Ex5_19_Fv_Morn_Peak',
            'Fv_Afternoon_Peak': 'Ex5_19_Fv_Afternoon_Peak',
            'Fv_PM_Peak': 'Ex5_19_Fv_PM_Peak',
            'Fv_Sleep_Peak': 'Ex5_19_Fv_Sleep_Peak',
            

            'Fv_1xplus_daily': 'Ex5_19_Fv_1xplus_daily',
            'Fv_1weekp': 'Ex5_19_Fv_1weekp',
            'Fv_2weekp': 'Ex5_19_Fv_2weekp',
            'Fv_wsalmon_rash': 'Ex5_19_Fv_wsalmon_rash',
            'Fv_Typ_NoneApply': 'Ex5_19_Fv_Typ_NoneApply',
            
            #Ex5_20 
            'Fg_24': 'Ex5_20_Fg_24',
            'FS_Fg': 'Ex5_20_FS_Fg',
            #Ex5_21 
            'App_24': 'Ex5_21_App_24',
            'FS_App': 'Ex5_21_FS_App',
            
            
            #Ex5_22 
            'Lb_loss_24': 'Ex5_22_Lb_loss_24',
            'FS_Lb_Loss': 'Ex5_22_FS_Lb_Loss',
            #Ex5_23 
            'Fog_24': 'Ex5_23_Fog_24',
            'FS_Fog': 'Ex5_23_FS_Fog',
            #Ex5_24 
            'Hair_Loss_24': 'Ex5_24_Hair_Loss_24',
            'FS_Hair_Loss': 'Ex5_24_FS_Hair_Loss',
            
            #Ex5_25
            'Flu_24': 'Ex5_25_Flu_24',
            'FS_Flu': 'Ex5_25_FS_Flu',
            #Ex5_26
            'Myalgia_24': 'Ex5_26_Myalgia_24',
            'FS_Myalgia': 'Ex5_26_FS_Myalgia',
            #Ex5_27
            'HBurn_24': 'Ex5_27_HBurn_24',
            'FS_HBurn': 'Ex5_27_FS_HBurn',
            #Ex5_28
            'Gastro_Hist_28.	Do_you_have_a_history_of_any_bowel_inflammation_or_gastrointestinal_infections_that_cannot_be_contributed_to_diet_or_medications?': 'Ex5_28_Gastro_Hist',
            'FS_Gastro': 'Ex5_28_FS_Gastro',
            #Ex5_29
            'AcidReflux_24': 'Ex5_29_AcidReflux_24',
            'FS_AcidReflux': 'Ex5_29_FS_AcidReflux',
            #Ex5_30
            'Rash_24': 'Ex5_30_Rash_24',
            'Rash_butterfly': 'Ex5_30_Rash_butterfly',
            'FS_Rash_Butterfly': 'Ex5_30_FS_Rash_Butterfly',
            'Rash_chest': 'Ex5_30_Rash_chest',
            'FS_Rash_chest': 'Ex5_30_FS_Rash_chest',


            'Rash_Bk_S': 'Ex5_30_Rash_Bk_S',
            'FS_Rash_Bk_S': 'Ex5_30_FS_Rash_Bk_S',
            'Rash_Arms': 'Ex5_30_Rash_Arms',
            'FS_Rash_Arm': 'Ex5_30_FS_Rash_Arm',
            'Rash_Legs': 'Ex5_30_Rash_Legs',
            'FS_Rash_Legs': 'Ex5_30_FS_Rash_Legs',
            'Rash_Hands': 'Ex5_30_Rash_Hands',
            'FS_Rash_Hands': 'Ex5_30_FS_Rash_Hands',
            'Rash_Scalp': 'Ex5_30_Rash_Scalp',
            'FS_Rash_Scalp': 'Ex5_30_FS_Rash_Scalp',
            'Rash_Elb': 'Ex5_30_Rash_Elb',
            'FS_Rash_Elb': 'Ex5_30_FS_Rash_Elb',
            'Rash_Feet': 'Ex5_30_Rash_Feet',
            'FS_Rash_Feet': 'Ex5_30_FS_Rash_Feet',
            'Rash_Other': 'Ex5_30_Rash_Other',
            'FS_Rash_Other': 'Ex5_30_FS_Rash_Other',
            
            #Ex5_30b
            'ID_Rash_b.	Which_of_the_following_statements_best_describes_the_rashes_that_occurred_on_your_body?_Check_all_that_apply.__Bright_red_and_warm_to_the_touch,_mimicking_a_sunburn': 'Ex5_30b_sunburn',
            'ID_Rash_b.	Which_of_the_following_statements_best_describes_the_rashes_that_occurred_on_your_body?_Check_all_that_apply.__Scaly_red_and_white_patches_psoriasis': 'Ex5_30b_psoriasis',
            'ID_Rash_b.	Which_of_the_following_statements_best_describes_the_rashes_that_occurred_on_your_body?_Check_all_that_apply.__Salmon_colored_rash_that_comes_and_goes': 'Ex5_30b_salmon',
            'ID_Rash_b.	Which_of_the_following_statements_best_describes_the_rashes_that_occurred_on_your_body?_Check_all_that_apply.__Cluster_of_reddish_patches,_not_raised,_and_do_not_itch': 'Ex5_30b_cluster',
            'ID_Rash_b.	Which_of_the_following_statements_best_describes_the_rashes_that_occurred_on_your_body?_Check_all_that_apply.__Reddish-purple_discoloration,_not_raised,_with_the_appearance_of_a_web': 'Ex5_30b_web',
            'ID_Rash_other': 'Ex5_30b_other',
            'ID_Rash_Other_text': 'Ex5_30b_Other_Text',
            
            
            #Ex5_30c
            'Ps_Dx': 'Ex5_30c_Ps_Dx',
            
            #Ex5_30d
            'Ps_pre_arthritis': 'Ex5_30d_Ps_pre_arthritis',
            
            #Ex5_31
            'Eye_Dx': 'Ex5_31_Eye_Dx',
            'FS_Eye': 'Ex5_31_FS_Eye',
            
            #Ex5_32
            'PinkEye_24': 'Ex5_32_PinkEye_24',
            'FS_PinkEye': 'Ex5_32_FS_PinkEye',
            
            #Ex5_33
            'Eye_Dry_24': 'Ex5_33_Eye_Dry_24',

            
            'Eye_burn_itch_24': 'Ex5_33_Eye_burn_itch_24',
            'Eye_Blur_24': 'Ex5_33_Eye_Blur_24',
            'Eye_lightsens_24': 'Ex5_33_Eye_lightsens_24',
            'Eye_Sym_24p': 'Ex5_33_Eye_Sym_24p',
            'N_Eye_Sym_24': 'Ex5_33_N_Eye_Sym_24',
            'Eye_Sym_24_IDK': 'Ex5_33_Eye_Sym_24_IDK',
            'FS_Dry_Eye': 'Ex5_33_FS_Dry_Eye',
            'FS_Burn_Itch': 'Ex5_33_FS_Burn_Itch',
            'FS_Blur': 'Ex5_33_FS_Blur',
            'FS_LightSens': 'Ex5_33_FS_LightSens',
            
            #Ex5_34
            
            'M_Thr_Nk_Ns_24_34.	Did_you_have_any_of_the_following_issues_with_your_mouththroatnecknose_region_during_the_first_24_months_after_initial_onset?_	_Painful_swollen_and_tender_lymph_nodes_andor_saliva_glands_in_areas_around_the_face_andor_neck?': 'Ex5_34_face_andor_neck?',
            'M_Thr_Nk_Ns_24_34.	Did_you_have_any_of_the_following_issues_with_your_mouththroatnecknose_region_during_the_first_24_months_after_initial_onset?_	_Painful_swollen_and_tender_lymph_nodes_in_areas_of_the_body_not_including_the_face_andor_neck?': 'Ex5_34_body',
            'Swallow_24': 'Ex5_34_Swallow_24',
            'Thirst_24': 'Ex5_34_Thirst_24',
            'CSores_Mouth_24': 'Ex5_34_CSores_Mouth_24',
            'Csores_Nose_24': 'Ex5_34_Csores_Nose_24',
            'No_M_Thr_Nk_Ns_24': 'Ex5_34_No_24',
            'M_Thr_Nk_Ns_24_IDK': 'Ex5_34_24_IDK',
            'FS_M_Thr_Nk_Ns.0_Painful_swollen_and_tender_lymph_nodes_andor_saliva_glands_in_areas_around_the_face_andor_neck?_First_symptom?': 'Ex5_34_FS_face_andor_neck',
            'FS_M_Thr_Nk_Ns.1_Painful_swollen_and_tender_lymph_nodes_in_areas_of_the_body_not_including_the_face_andor_neck?_First_symptom?': 'Ex5_34_FS_body',
            'FS_Sore_Throat': 'Ex5_34_FS_Sore_Throat',
            'FS_Swallow': 'Ex5_34_FS_Swallow',
            'FS_Thirst': 'Ex5_34_FS_Thirst',
            'FS_Csores_Mouth': 'Ex5_34_FS_Csores_Mouth',
            'FS_Csores_Nose': 'Ex5_34_FS_Csores_Nose',
            
            #Ex5_35
            
            'Dental_Cavities_24': 'Ex5_35_Dental_Cavities_24',
            'Dental_Gingivitis_24': 'Ex5_35_Dental_Gingivitis_24',
            'Dental_Breaking_teeth_24': 'Ex5_35_Dental_Breaking_teeth_24',
            'Dental_Thrush_24': 'Ex5_35_Dental_Thrush_24',

            
            'Dental_24_Other': 'Ex5_35_Dental_24_Other',
            'Dental_24_Other_text': 'Ex5_35_Dental_24_Other_text',
            'N_Dental_24': 'Ex5_35_N_Dental_24',
            'Dental_24_IDK': 'Ex5_35_Dental_24_IDK',
            'FS_cavities': 'Ex5_35_FS_cavities',
            'FS_Gingivitis': 'Ex5_35_FS_Gingivitis',
            'FS__Breaking_teeth': 'Ex5_35_FS__Breaking_teeth',
            'FS_thrush': 'Ex5_35_FS_thrush',
            
            #Ex5_36    

            'Nodules_0_12': 'Ex5_36_Nodules_0_12',
            'ID_Nodules_Arms': 'Ex5_36_ID_Nodules_Arms',
            'ID_Nodules_Elb': 'Ex5_36_ID_Nodules_Elb',
            'ID_Nodules_hands': 'Ex5_36_ID_Nodules_hands',
            'ID_Nodules_wrists': 'Ex5_36_ID_Nodules_wrists',
            'ID_Nodules_other': 'Ex5_36_ID_Nodules_other',
            'ID_Nodules_othertext': 'Ex5_36_ID_Nodules_othertext',
            'FS_Nodules': 'Ex5_36_FS_Nodules',
            
            #Ex5_37    
            'Numb_24?': 'Ex5_37_Numb_24',
            'FS_Numb': 'Ex5_37_FS_Numb',
            
            #Ex5_38    
            'Nail_Change_24': 'Ex5_38_Nail_Change_24',
            'FS_Nail_Change': 'Ex5_38_FS_Nail_Change',
            'Nailbed_separation': 'Ex5_38_Nailbed_separation',
            'Pitted_nails': 'Ex5_38_Pitted_nails',
            'Nail_fungus': 'Ex5_38_Nail_fungus',
            'Nail_other': 'Ex5_38_Nail_other',
            'Nail_other_text': 'Ex5_38_Nail_other_ext',
            
            #Ex5_39   
            'Raynauds_24': 'Ex5_39_Raynauds_24',
            'FS_Raynauds': 'Ex5_39_FS_Raynauds',
            
            #Ex5_40   
            'Hepatomegaly': 'Ex5_40_Hepatomegaly',
            'FS_Hepatomegaly': 'Ex5_40_FS_Hepatomegaly',
            
            #Ex5_41   
            'Splenomegaly': 'Ex5_41_Splenomegaly',
            'FS_Splenomegaly': 'Ex5_41_FS_Splenomegaly',
            
            #Ex5_42
            'Anemic_Dx': 'Ex5_42_Anemic_Dx',
            
            # Part 3
            'rheu_1.__Rheumatoid_Arthritis_Is_there_any_other_symptom_not_mentioned_in_this_study_that_you_feel_was_a_part_of_your_Rheumatoid_Arthritis_in_the_first_0_to_<_24_months_from_onset?': 'Part3_1_rheu',
            'psor_2._Psoriatic_Arthritis_Is_there_any_other_symptom_not_mentioned_in_this_study_that_you_feel_was_a_part_of_your_Psoriatic_Arthritis_in_the_first_0_to_<_24_months_from_onset?': 'Part3_2_psor',
            'sys_3._Systemic_Lupus_Erythematosus__At_any_time_prior_to_or_at_the_time_of_diagnosis_did_your_blood_test_positive_for_antinuclear_antibodies_ANA?': 'Part3_3_sys',
            'sys_1_Is_there_any_other_symptom_not_mentioned_in_this_study_that_you_feel_was_a_part_of_your_Systemic_Lupus_Erythematosus_disease_in_the_first_0_to_<24_months_from_onset?': 'Part3_3_sys_other_Text',
            'sjo_4.__Sjögren’s_Syndrome_Is_there_any_other_symptom_not_mentioned_in_this_study_that_you_feel_was_a_part_of_your_Sjögren’s_Syndrome_in_the_first_0_to_<_24_months_from_onset?': 'Part3_4_sjo',
            'still_5._Adult_Onset_Still’s_Disease_Were_you_ever_diagnosed_with_acute_respiratory_distress_syndrome_ARDS_or_chronic_restrictive_lung_disease_prior_to_or_during_the_first_24_months_after_onset_of_your_disease?_Yes,_was_diagnosed_with_acute_respiratory_distress_syndrome_ARDS_prior_to_initial_onset_of_my_symptoms': 'Part3_5_still_ARDS_onset',
            'still_5._Adult_Onset_Still’s_Disease_Were_you_ever_diagnosed_with_acute_respiratory_distress_syndrome_ARDS_or_chronic_restrictive_lung_disease_prior_to_or_during_the_first_24_months_after_onset_of_your_disease?_Yes,_was_diagnosed_with_acute_respiratory_distress_syndrome_ARDS_between_0_and_<_24_months_from_initial_onset_of_my_symptoms': 'Part3_5_still_ARDS_0_24',
            'still_5._Adult_Onset_Still’s_Disease_Were_you_ever_diagnosed_with_acute_respiratory_distress_syndrome_ARDS_or_chronic_restrictive_lung_disease_prior_to_or_during_the_first_24_months_after_onset_of_your_disease?_Yes,_was_diagnosed_with_chronic_restrictive_lung_disease_prior_to_initial_onset_of_my_symptoms': 'Part3_5_still_lung_onset',
            'still_5._Adult_Onset_Still’s_Disease_Were_you_ever_diagnosed_with_acute_respiratory_distress_syndrome_ARDS_or_chronic_restrictive_lung_disease_prior_to_or_during_the_first_24_months_after_onset_of_your_disease?_Yes,_was_diagnosed_with_chronic_restrictive_lung_disease_between_0_and_<_24_months_from_initial_onset_of_my_symptoms': 'Part3_5_still_lung_0_24',
            'still_5._Adult_Onset_Still’s_Disease_Were_you_ever_diagnosed_with_acute_respiratory_distress_syndrome_ARDS_or_chronic_restrictive_lung_disease_prior_to_or_during_the_first_24_months_after_onset_of_your_disease?_I_was_diagnosed_with_acute_respiratory_distress_syndrome_ARDS_but_only_sometime_after_the_first_24_months_after_onset': 'Part3_5_still_ARDS_24p',
            'still_5._Adult_Onset_Still’s_Disease_Were_you_ever_diagnosed_with_acute_respiratory_distress_syndrome_ARDS_or_chronic_restrictive_lung_disease_prior_to_or_during_the_first_24_months_after_onset_of_your_disease?_I_was_diagnosed_with_chronic_restrictive_lung_disease_but_only_sometime_after_the_first_24_months_after_onset': 'Part3_5_still_lung_24p',
            'still_5._Adult_Onset_Still’s_Disease_Were_you_ever_diagnosed_with_acute_respiratory_distress_syndrome_ARDS_or_chronic_restrictive_lung_disease_prior_to_or_during_the_first_24_months_after_onset_of_your_disease?_I_do_not_remember': 'Part3_15_still_No_Remember',
            'aosd.0_Acute_respiratory_distress_syndrome_ARDS_First_symptom?': 'Part3_5_FS_ARDS',
            'aosd.1_chronic_restrictive_lung_disease_First_symptom?': 'Part3_5_FS_lung',
            'still_1_Is_there_any_other_symptom_not_mentioned_in_this_study_that_you_feel_was_a_part_of_your_Adult_Onset_Still’s_Disease_in_the_first_0_to_<24_months_from_onset?': 'Part3_5_still_other_Text',
            'ank_6.__Ankylosing_Spondylitis_At_any_time_prior_to_or_at_the_time_of,_or_after_diagnosis_did_your_blood_test_positive_for_the_HLA-B27_gene?': 'Part3_6_Ank',
            'ank_1_Is_there_any_other_symptom_not_mentioned_in_this_study_that_you_feel_was_a_part_of_your_Ankylosing_Spondylitis_in_the_first_0_to_<24_months_from_onset?': 'Part3_6_Ank_other_Text',
            
            

        }

        return newColNames
    