# Complete Report
[CSE_243_Project_Report](resources/CSE_243_Project_Report.pdf)
# Motivation
We would like to increase the accuracy and shorten the
time to diagnosis of sufferers with the following Autoimmune
diseases: Ankylosing Spondylitis (AS), Psoriatic
Arthritis (PsA), Systemic Lupus Erythematosus
(SLE), Sjögren’s Syndrome (SS), Adult-Onset Still’s Disease
(AOSD), and Rheumatoid Arthritis (RA). We hope
to accomplish this by identifying the common early
symptoms for each disease as reported by the patient.

Autoimmune Arthritis diseases are difficult to diagnose.
This difficulty is exacerbated by discrepancies between
the symptoms given for each disease in medical
journals and the symptoms that patients report experiencing
prior to diagnosis. These discrepancies prolong
the time to disease diagnosis. It is common for sufferers
of the six diseases in the study to go years without an accurate
diagnoses. Since these diseases are autoimmune
diseases, during this time, the body is literally attaching
itself. The more time that lapses between disease
onset and disease diagnosis, the more damage occurs.
Damage which is irreversible and which reduces the patient’s
mobility, longevity, and quality of life. Any work
in this area that either confirms early symptoms commonly
associated with one of these diseases or identifies
new ones, aides in the diagnosis process and possibly
shortens time to diagnosis resulting in better long term
prognosis.

![Motivation](resources/motivation.PNG)

# Challenges with Dataset
The dataset is built against a set of questions organized
as a survey. The accompanying questionnaire has 59
pages. While the meaning of the data may seem obvious
to appropriate medical practitioners, the data was far
from ready to be analyzed systematically. Here we list
some of the major challenges which we tackled with a
great effort:

1. Not all the questions are about earlier symptoms.
Some of the questions are related to posterior symptoms
or diseases. So, they surface after a person already
has developed an autoimmune disease. And as
the data-set holds data for those questions, too, it led
us to filter those posterior attributes from the dataset.
So, first challenge was to confirm which were in fact
early symptoms.

2. Mapping from questions to data object attributes
were not obvious. For this reason, we couldn’t readily
tell which column refers to which question. This made
our first challenge even more difficult. In the early experiments,
we inadvertently included some posterior
attributes for prediction models and ended up very high
accuracy rates but unfortunately wrong. To make the
mapping clear, we renamed all the columns in such a
way that we could find the associated question fast. But
that was not enough as many of the questions didn’t
have question numbers. So, for some questions, we created
unique prefixes which can group related questions.
We also made the prefixes to hold some semantics. For
example, we use the prefix Post_AD_, for all the attributes
which relates to diseases happening after the
first autoimmune disease. Smart prefixing also helped
us to filter out attributes automatically. So, for first disease
prediction, we matched the column names with
Post_AD_ and AAD_AD_ prefixes and dropped them.
Without renaming columns it would be a tiresome work
for us to manipulate columns for transformations and
clean-up.

3. Inconsistent attribute values. When it comes to
attribute values for a real-life survey, all kinds of surprises
are common. Here are some that we experienced
and how we handled it:
<p align='center'>
  <img style='width:200px' src="resources/p1.PNG">
  <img style='width:400px' src="resources/p2.PNG">
  <img style='width:100px' src="resources/p3.PNG">
</p>

# Final pipeline:
This is a final pipeline of our whole process. It was developed
through process iterations in our experiements.
![Final pipeline](resources/methods.PNG)
Final process pipeline. The bluebordered
methods requires manual interventions
and optionally some automated processes.

# Data mapping & Attribute Renaming
The pivotal element of a smart mapping between the
questions and dataset attribute is the Prefixing mechanism
we employed. The prefixed we created served
several purposes:
- To denote which section, group, or question the
attribute belongs to. For example, AAD_AD prefix
denotes the group of the chosen 6 autoimmune
diseases which can develop after the first autoimmune
disease.
- Some questions has multiple choice options. Each
of the option becomes a attribute in the dataset.
So, they were prefixed with the same string. This
helps to filter out the whole question from dataset.
- Prefixes also help us to segment data. Though, we
did not conduct any experiment with segmentation
in this project, it will be helpful for future
work.
In addition to help us to build effective mapping, renaming
also helped us to create transformers easily. For
example:
**“[M_Thr_Nk_Ns_24] 34. Did you have
any of the following issues with your mouth/ throat/
neck/ nose region during the first 24 months after
initial onset? [Painful swollen and tender lymph
nodes in areas of the body not including the face
and/or neck?]”**
is an actual attribute name in the raw dataset. If we
want to refer to the column in our automated cleaning
and transformation scripts, that would be cumbersome
to work with. But our new name for the column,
**Ex5_34_body**, was easy to refer. Here Ex5 denotes section
of "Exhibit 5", 34 denotes "Question no 34", and
body denotes the option with body excluding face and
neck.

# Data Cleaning & Transformations
We call automated transformation algorithms by transformers.
Before transforming values of an attribute,
we need to make sure they are clean and consistent
enough for the transformer to work. Each transformer
can apply a set of ordered basic transformers.
For continuous values like age, we automated detection
of non-numeric values and manually fixed them
in Microsoft Excel. For categorical valueswe followed
the following steps:
1. Figure out definitions of missing values for the
attribute
2. Replace missing values with string "NA2". "NA2"
was chosen instead of "NA" as some analytic and
machine learning libraries automatically processed
"NA" as missing values. We wanted full control
on our processes.
3. Figure out unique values. This itself is two step
process. First step is automatically extract unique
string values. Then manually detect "duplicates"
and map duplicates to a single value.
4. Create a transformer to transform all the values
for the attribute.
For mixed attributes having data from both pre and
post symptoms, we needed to extract new attributes
before applying the transformations.

# Experimental pipeline
Our final process pipeline 6 emerged from experimental
pipeline in 7. We revised the cleaning and transformation
processes several times which resulted in a
sequence of revisions in and execution of other processes.

![Experimental pipeline](resources/process_actual.PNG)

# Results
<p align="center">
  <img style='width:400px' src="resources/result_RF.PNG">
  <img style='width:400px'  src="resources/result_NN.PNG">
  <img style='width:400px'  src="resources/result_SVM.PNG">
</p>

# Feature Importance
<p align="center">
  <img style='width:400px' src="resources/feature_imp.PNG">
</p>

# Future Work
Possible future work includes:
1. Create survey that lends itself to analysis and
that also includes questions that will help us answer
questions raised during analysis. Identifying
patterns of symptoms over time for different diseases/
segments.
2. Segmentation Analysis
3. More experiments with models
4. Predicting a sequence of Autoimmune diseases
5. Identifying relevant symptoms