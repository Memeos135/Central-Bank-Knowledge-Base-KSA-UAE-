# CBUAE_EN_4881_VER1.pdf

## Page 1

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
Model Management
Standards
Version date: November 2022
Central Bank of the U.A.E. 
 
1/56

## Page 2

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
CONTENTS
INTRODUCTION
Section 1 
Context and Objectives
Section 2 
Implementation
PART I – GENERAL STANDARDS
Section 3 
General Standards
PART II – APPLICATION OF THE STANDARDS
Section 4 
Model Governance
Section 5 
Data Management
Section 6 
Development
Section 7 
Model Implementation
Section 8 
Model Usage
Section 9 
Model Monitoring
Section 10 Independent Validation
APPENDIX
Numerical thresholds
Central Bank of the U.A.E. 
 
2/56

## Page 3

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
TABLE OF CONTENTS
Definitions and interpretations .................................................................................................. 5
1 
Context and objectives ...................................................................................................... 11
1.1 
Regulatory context .................................................................................................... 11
1.2 
Objectives ................................................................................................................. 11
1.3 
Document structure ................................................................................................... 12
2 
Implementation ................................................................................................................. 12
2.1 
Scope of application ................................................................................................. 12
2.2 
Requirements and implementation timeframe .......................................................... 13
2.3 
Reporting to the CBUAE .......................................................................................... 14
2.4 
Scope of models ........................................................................................................ 14
3 
General Standards ............................................................................................................ 15
3.1 
Model governance .................................................................................................... 15
3.2 
Data management ..................................................................................................... 17
3.3 
Model development .................................................................................................. 18
3.4 
Model implementation .............................................................................................. 19
3.5 
Model usage .............................................................................................................. 19
3.6 
Model performance monitoring ................................................................................ 20
3.7 
Independent validation .............................................................................................. 21
4 
Model Governance ............................................................................................................ 23
4.1 
Overview................................................................................................................... 23
4.2 
Model objectives and strategy .................................................................................. 23
4.3 
Model life-cycle ........................................................................................................ 24
4.4 
Model inventory and grouping ................................................................................. 24
4.5 
Model ownership ...................................................................................................... 25
4.6 
Stakeholders and decision process ............................................................................ 25
4.7 
Third party provider .................................................................................................. 27
4.8 
Internal skills ............................................................................................................ 28
4.9 
Model documentation ............................................................................................... 29
4.10 Performance Reporting ............................................................................................. 29
4.11 Mergers, acquisitions and disposals .......................................................................... 30
5 
Data Management ............................................................................................................. 31
5.1 
Data governance ....................................................................................................... 31
5.2 
Identification of data sources .................................................................................... 31
5.3 
Data collection .......................................................................................................... 32
5.4 
Data quality review ................................................................................................... 32
5.5 
Data storage and access ............................................................................................ 33
5.6 
System infrastructure ................................................................................................ 33
Central Bank of the U.A.E. 
 
3/56

## Page 4

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
6 
Model Development .......................................................................................................... 34
6.2 
Data preparation and representativeness ................................................................... 34
6.3 
Data exploration ........................................................................................................ 35
6.4 
Data transformation .................................................................................................. 35
6.5 
Sampling ................................................................................................................... 35
6.6 
Choice of methodology ............................................................................................. 36
6.7 
Model construction ................................................................................................... 36
6.8 
Model selection ......................................................................................................... 38
6.9 
Model calibration ...................................................................................................... 39
6.10 Pre-implementation validation .................................................................................. 39
6.11 Impact analysis ......................................................................................................... 39
7 
Model Implementation ..................................................................................................... 40
7.2 
Project Governance ................................................................................................... 40
7.3 
Implementation timing .............................................................................................. 40
7.4 
System infrastructure ................................................................................................ 41
7.5 
User Acceptance Testing .......................................................................................... 41
7.6 
Production testing ..................................................................................................... 42
7.7 
Spreadsheet implementation ..................................................................................... 42
8 
Model Usage ...................................................................................................................... 44
8.2 
Usage definition and control ..................................................................................... 44
8.3 
Responsibilities ......................................................................................................... 44
8.4 
Input and output overrides ........................................................................................ 45
8.5 
User feedback ........................................................................................................... 45
8.6 
Usage of rating models ............................................................................................. 45
9 
Model Performance Monitoring ...................................................................................... 47
9.1 
Objective ................................................................................................................... 47
9.2 
Responsibility ........................................................................................................... 47
9.3 
Frequency ................................................................................................................. 47
9.4 
Metrics and limits ..................................................................................................... 48
9.5 
Reporting and decision-making ................................................................................ 48
10 
Independent Validation .................................................................................................... 49
10.1 Objective and scope .................................................................................................. 49
10.2 Responsibilities ......................................................................................................... 50
10.3 Qualitative validation ................................................................................................ 50
10.4 Quantitative validation .............................................................................................. 51
10.5 Review frequency ..................................................................................................... 52
10.6 Reporting of findings ................................................................................................ 53
10.7 Remediation process ................................................................................................. 54
Numerical thresholds included in the MMS ........................................................................... 56
Central Bank of the U.A.E. 
 
4/56

## Page 5

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
DEFINITIONS AND INTERPRETATIONS
The following terms shall have the meaning assigned to them for the purpose of interpreting these 
Standards and the related Guidance:
1. Board: As defined in the CBUAE’s Corporate Governance Regulation for Banks.
2. Causality (written in lower case as “causality”): Relationship between cause and effect. It is 
the influence of one event on the occurrence of another event.
3. CBUAE: Central Bank of the United Arab Emirates.
4. Correlation (written in lower case as “correlation”): Any statistical relationship between two 
variables, without explicit causality explaining the observed joint behaviours. Several metrics 
exist to capture this relationship. Amongst others, linear correlations are often captured by 
the Pearson coefficient. Linear or non-linear correlation are often captured by the Spearman’s 
rank correlation coefficient.
5. Correlation Analysis (written in lower case as “correlation analysis”): Correlation analysis 
refers to a process by which the relationships between variables are explored. For a given set 
of data and variables, observe (i) the statistical properties of each variable independently, 
(ii) the relationship between the dependent variable and each of the independent variables on 
a bilateral basis, and (iii) the relationship between the independent variables with each other.
6. CI (Credit Index):  In the context of credit modelling, a credit index is a quantity defined over 
(−∞,+∞) derived from observable default rates, for instance through probit transformation. 
CI represents a systemic driver of creditworthiness. While this index is synthetic, (an abstract 
driver), it is often assimilated to the creditworthiness of specific industry or geography.
7. Default (written in lower case as “default”): The definition of default depends on the 
modelling context, either for the development of rating models or for the calibration and 
probabilities of default. For a comprehensive definition, refer to the section on rating models 
in the MMG.
8. Deterministic Model (written in lower case as “deterministic model”): A deterministic model 
is a mathematical construction linking, with certainty, one or several dependent variables, to 
one or several independent variables. Deterministic models are different from statistical 
models. The concept of confidence interval does not apply to deterministic models. Examples 
of deterministic models include NPV models, financial cash flow models or exposure models 
for amortizing facilities.
9. DMF (Data Management Framework): Set of policies, procedures and systems designed to 
organise and structure the management of data employed for modelling.
10. DPD (Days-Past-Due): A payment is considered past due if it has not been made by its 
contractual due date. The days-past-due is the number of days that a payment is past its due 
date, i.e. the number of days for which a payment is late.
11. DSIB (Domestic Systemically Important Banks): These are UAE banks deemed sufficiently 
large and interconnected to warrant the application of additional regulatory requirements. The 
identification of the institutions is based upon a framework defined by the CBUAE.
12. EAD (Exposure At Default): Expected exposure of an institution towards an obligor (or a 
facility) upon a future default of this obligor (or its facility). It also refers to the observed 
exposure upon the realised default of an obligor (or a facility). This amount materialises at 
the default date and can be uncertain at reporting dates prior to the default date. The
Central Bank of the U.A.E. 
 
5/56

## Page 6

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
uncertainty surrounding EAD depends on the type of exposure and the possibility of future 
drawings. In the case of a lending facility with a pre-agreed amortisation schedule, the EAD 
is known. In the case of off-balance sheet exposures such as credit cards, guarantees, working 
capital facilities or derivatives, the EAD is not certain on the date of measurement and should 
be estimated with statistical models.
13. EAR (Earning At Risk): Refer to NII.
14. ECL (Expected Credit Loss): Metric supporting the estimation of provisions under IFRS9 to 
cover credit risk arising from facilities and bonds in the banking book. It is designed as a 
probability-weighted expected loss.
15. Economic Intuition (written in lower case as “economic intuition”): Also referred to as 
economic intuition and business sense. Property of a model and its output to be interpreted in 
terms and metrics that are commonly employed for business and risk decisions. It also refers 
to the property of the model variables and the model outputs to meet the intuition of experts 
and practitioners, in such a way that the model can be explained and used to support decision-
making.
16. Effective Challenge: Characteristic of a validation process. An effective model validation 
ensures that model defects are suitably identified, discussed and addressed in a timely fashion. 
Effectiveness is achieved via certain key features of the validation process such as 
independence, expertise, clear reporting and prompt action from the development team.
17. EVE (Economic Value of Equity): It is defined as the difference between the present value 
of the institution’s assets minus the present value of liabilities. The EVE is sensitive to 
changes in interest rates. It is used in the measurement of interest rate risk in the banking 
book.
18. Expert-Based Models (written in lower case as “expert-based models”): Also referred to as 
judgemental models, these models rely on the subjective judgement of expert individuals 
rather than on quantitative data. In particular, this type of model is used to issue subjective 
scores in order to rank corporate clients.
19. Institutions (written in lower case as “institution(s)”): All banks licenced by the CBUAE. 
Entities that take deposits from individuals and/or corporations, while simultaneously issuing 
loans or capital market securities.
20. LGD (Loss Given Default): Estimation of the potential loss incurred by a lending institution 
upon the default of an obligor (or a facility), measured as a percentage of the EAD. It also 
refers to the actual loss incurred upon past defaults also expressed as a percentage of EAD. 
The observed LGD levels tend to be related to PD levels with various strength of correlation.
21. Limits and limitations (written in lower case as “limits” and “limitations”): Model limits are 
thresholds applied to a model’s outputs and/or its parameters in order to control its 
performance. Model limitations are boundary conditions beyond which the model ceases to 
be accurate.
22. LSI (Large and/or Sophisticated Institutions): This group comprises DSIBs and any other 
institutions that are deemed large and/or with mature processes and skills. This categorisation 
is defined dynamically based on the outcome of regular banking supervision.
23. Macroeconomic Model (written in lower case as “macroeconomic model” or “macro 
model”): Refers to two types of models. (i) A model that links a set of independent macro 
variables to another single dependent macro variable or to several other dependent macro 
variables or (ii) a model that links a set of independent macro variables to a risk metric (or a 
set of risk metrics) such as probabilities of default or any other business metric such as 
revenues.
Central Bank of the U.A.E. 
 
6/56

## Page 7

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
24. Market Data: Refers to the various data attributes of a traded financial instrument reported 
by a trading exchange. It includes the quoted value of the instrument and/or the quoted 
parameters of that instrument that allow the derivation of its value. It also includes transaction 
information including the volume exchanged and the bid-ask spread.
25. Materiality: The materiality of a model represents the financial scope covered by the model 
in the context of a given institution. It can be used to estimate the potential loss arising from 
model uncertainty (see Model Risk). Model materiality can be captured by various metrics 
depending on model types. Typically, total exposure can be used as a metric for credit models.
26. MMG: CBUAE’s Model Management Guidance.
27. MMS: CBUAE’s Model Management Standards.
28. Model (written in lower case as “model”): A quantitative method, system, or approach that 
applies statistical, economic, financial, or mathematical theories, techniques, and assumptions 
to process input data into quantitative estimates. For the purpose of the MMS and MSG, 
models are categorised in to three distinct groups: statistical models, deterministic models 
and expert-based models.
29. Model Calibration (written in lower case as “model calibration”): Key step of the model 
development process. Model calibration means changing the values of the parameters and/or 
the weights of a model, without changing the structure of the model, i.e. without changing the 
nature of the variables and their transformations.
30. Model Complexity (written in lower case as “model complexity”): Overall characteristic of 
a model reflecting the degree of ease (versus difficulty) with which one can understand the 
model conceptual framework, its practical design, calibration and usage. Amongst other 
things, such complexity is driven by, the number of inputs, the interactions between variables, 
the dependency with other models, the model mathematical concepts and their 
implementation.
31. Model Construction (written in lower case as “model construction”): Key step of the model 
development process. The construction of a model depends on its nature, i.e. statistical or 
deterministic. For the purpose of the MMS and the MMG, model construction means the 
following: for statistical models, for a given methodology and a set of data and transformed 
variables, it means estimating and choosing, with a degree of confidence, the number and 
nature of the dependent variables along with their associated weights or coefficients. For 
deterministic models, for a given methodology, it means establishing the relationship between 
a set of input variables and an output variable, without statistical confidence intervals.
32. Model Development (written in lower case as “model development”): Means creating a 
model by making a set of sequential and recursive decisions according to the steps outlined 
in the dedicated sections of the MMS. Model re-development means conducting the model 
development steps again with the intention to replace an existing model. The replacement 
may, or may not, occur upon re-development.
33. Modelling Decision (written in lower case as “modelling decision”): A modelling decision 
is a deliberate choice that determines the core functionality and output of a model. Modelling 
decisions relate to each of the steps of the data acquisition, the development and the 
implementation phase. In particular, modelling decisions relate to (i) the choice of data, 
(ii) the analysis of data and sampling techniques, (iii) the methodology, (iv) the calibration 
and (v) the implementation of models. Some modelling decisions are more material than 
others. Key modelling decisions refer to decisions with strategic implications and/or with 
material consequences on the model outputs.
34. Model Risk: Potential loss faced by institutions from making decisions based on inaccurate 
or erroneous outputs of models due to errors in the development, the implementation or the 
inappropriate usage of such models. Losses incurred from Model Risk should be understood
Central Bank of the U.A.E. 
 
7/56

## Page 8

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
in the broad sense as Model Risk has multiple sources. This definition includes direct 
quantifiable financial loss but also any adverse consequences on the ability of the institution 
to conduct its activities as originally intended, such as reputational damage, opportunity costs 
or underestimation of capital. In the context of the MMS and the MMG, Model Risk for a 
given model should be regarded as the combination of its materiality and the uncertainty 
surrounding its results.
35. Model Selection (written in lower case as “model selection”): This step is part of the 
development process. This means choosing a specific model amongst a pool of available 
models, each with a different set of variables and parameters.
36. Model Uncertainty (written in lower case as “model uncertainty”): This refers to the 
uncertainty surrounding the results generated by a model. Such uncertainty can be quantified 
as a confidence interval around the model output values. It is used as a component to estimate 
Model Risk.
37. Multivariate Analysis (written in lower case as “multivariate analysis”):  For a given set of 
data and variables, this is a process of observing the joint distribution of the dependent and 
independent variables together and drawing conclusions regarding their degree of correlation 
and causality.
38. NII (Net Interest Income): To simplify notations, both Net Interest Income (for conventional 
products) and/or Net Profit Income (for Islamic Products) are referred to as “NII”. In this 
context, ‘profit’ is assimilated as interest. It is defined as the difference between total interest 
income and total interest expense, over a specific time horizon and taking into account 
hedging. The change in NII (“∆NII”) is defined as the difference between the NII estimated 
with stressed interest rates under various scenarios, minus the NII estimated with the interest 
rates as of the portfolio reporting date. ∆NII is also referred to as earnings at risk (“EAR”).
39. NPV (Net Present Value): Present value of future cash flows minus the initial investment, i.e. 
the amount that a rational investor is willing to pay today in exchange for receiving these cash 
flows in the future. NPV is estimated through a discounting method. It is commonly used to 
estimate various metrics for the purpose of financial accounting, risk management and 
business decisions.
40. PD (Probability of Default): Probability that an obligor fails to meet its contractual obligation 
under the terms of an agreed financing contract. Such probability is computed over a given 
horizon, typically 12 months, in which case it is referred to as a 1-year PD. It can also be 
computed over longer horizons. This probability can also be defined at several levels of 
granularity, including, but not limited to, single facility, pool of facilities, obligor, or 
consolidated group level.
41. PD Model (written as “PD model”): This terminology refers to a wide variety of models with 
several objectives. Amongst other things, these models include mapping methods from scores 
generated by rating models onto probability of defaults. They also include models employed 
to estimate the PD or the PD term structure of facilities, clients or pool of clients.
42. PD Term Structure (written as “PD term structure”): Refers to the probability of default 
over several time horizons, for instance 2 years, 5 years or 10 years. A distinction is made 
between the cumulative PD and the marginal PD. The cumulative PD is the total probability 
of default of the obligor over a given horizon. The marginal PD is the probability of default 
between two dates in the future, provided that the obligor has survived until the first date.
43. PIT (Point-In-Time) and TTC (Through-The-Cycle): A point-in-time assessment refers to 
the value of a metric (typically PD or LGD) that incorporates the current economic conditions. 
This contrasts with a through-the-cycle assessment that refers to the value of the same metric 
across a period covering one or several economic cycles.
Central Bank of the U.A.E. 
 
8/56

## Page 9

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
44. Qualitative validation: A review of model conceptual soundness, design, documentation, 
and development and implementation process.
45. Quantitative validation: A review of model numerical output, covering at least its accuracy, 
degree of conservatism, stability, robustness and sensitivity.
46. Rating / Scoring (written in lower case “rating or scoring”): For the purpose of the MMS and 
the MMG, a rating and a score are considered as the same concept, i.e. an ordinal quantity 
representing the relative creditworthiness of an obligor (or a facility) on a predefined scale. 
‘Ratings’ are commonly used in the context of corporate assessments whilst ‘scores’ are used 
for retail client assessments.
47. Restructuring (written in lower case “restructuring”): The definition of restructuring / 
rescheduling used for modelling in the context of the MMS and MMG should be understood 
as the definition provided in the dedicated CBUAE regulation and, in particular, in the 
Circular 28/2010 on the classification of loans, with subsequent amendments to this Circular 
and any new CBUAE regulation on this topic.
48. Rating Model (written in lower case “rating model”): The objective of such model is to 
discriminate ex-ante between performing clients and potentially non-performing clients. Such 
models generally produce a score along an arbitrary scale reflecting client creditworthiness. 
This score can subsequently mapped to a probability of default. However, rating models 
should not be confused with PD models.
49. Retail Clients (written in lower case as “retail clients”): Retail clients refer to individuals to 
whom credit facilities are granted for the following purpose: personal consumer credit 
facilities, auto credit facilities, overdraft and credit cards, refinanced government housing 
credit facilities, other housing credit facilities, credit facilities against shares to individuals. It 
also includes small business credit facilities for which the credit risk is managed using similar 
methods as applied for personal credit facilities.
50. Segment (written in lower case as “segment”): Subsets of an institution’s portfolio obtained 
by splitting the portfolio by the most relevant dimensions which explain its risk profile. 
Typical dimensions include obligor size, industries, geographies, ratings, product types, tenor 
and currency of exposure. Segmentation choices are key drivers of modelling accuracy and 
robustness.
51. Senior Management: As defined in the CBUAE’s Corporate Governance Regulation for 
Banks.
52. Statistical Model (written in lower case as “statistical model”): A statistical model is a 
mathematical construction achieved by the application of statistical techniques to samples of 
data. The model links one or several dependent variables to one or several independent 
variables. The objective of such a model is to predict, with a confidence interval, the values 
of the dependent variables given certain values of the independent variables. Examples of 
statistical models include rating models or value-at-risk (VaR) models. Statistical models are 
different from deterministic models. By construction, statistical models always include a 
degree of Model Risk.
53. Tiers: Models are allocated to different groups, or Tiers, depending on their associated Model 
Risk.
54. Time series analysis (written in lower case as “time series analysis”): For a given set of data 
and variables, this is a process of observing the behaviour of these variables through time. 
This can be done by considering each variable individually or by considering the joint pattern 
of the variables together.
Central Bank of the U.A.E. 
 
9/56

## Page 10

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
55. UAT (User Acceptance Testing): Phase of the implementation process during which users 
rigorously test the functionalities, robustness, accuracy and reliability of a system containing 
a new model before releasing it into production.
56. Variable Transformation (written in lower case as “variable transformation”): Step of the 
modelling process involving a transformation of the model inputs before developing a model. 
Amongst others, common transformations include (i) relative or absolute differencing 
between variables, (ii) logarithmic scaling, (iii) relative or absolute time change, (iv) ranking, 
(v) lagging, and (vi) logistic or probit transformation.
57. Wholesale Clients (written in lower case as “wholesale clients”): Wholesale clients refer to 
any client that is not considered as a retail client as per the definition of these Standards.
Central Bank of the U.A.E. 
 
10/56

## Page 11

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
INTRODUCTION
1 
CONTEXT AND OBJECTIVES
1.1 
Regulatory context
1.1.1 
The Risk Management Regulation (Circular No. 153/2018) issued by the Central Bank 
of the UAE (“CBUAE”) on 27th May 2018, states that banks must have robust systems 
and tools to assess and measure risks. In particular, when models are used, they must be 
managed appropriately to support decision-making.
(i) 
Article 2.1: “A bank must have an appropriate risk governance framework that 
provides a bank-wide view of all material risks. This includes policies, processes, 
procedures, systems and controls to identify, measure, evaluate, monitor, report 
and control or mitigate material sources of risk on a timely basis (…).”
(ii) 
Article 4.1: “A bank must have systems to measure and monitor risks which are 
commensurate with the risk profile, nature, size and complexity of its business and 
structure.”
(iii) 
Article 4.3: “Where a Bank uses models to measure components of risks, it must 
have appropriate internal processes for the development and approval for use of 
such models and must perform regular and independent validation and testing of 
the models (…).”
1.1.2 
Consequently, the Model Management Standards (“MMS”) present modelling practices 
that must be implemented by banks in the UAE, if they decide to employ models for 
decision-making. These standards are based upon practices deemed appropriate within 
the financial industry internationally with consideration of local circumstances. The 
MMS therefore represent the minimum requirements to be met within the UAE.
1.2 
Objectives
1.2.1 
Models are an integral part of decision-making within UAE banks for risk management, 
business decisions and accounting. Banks employ models to comply with several 
regulatory and accounting requirements, including, but not limited to: (i) IFRS9 
accounting requirements, (ii) capital forecasting, (iii) Pillar II capital assessment, 
(iv) regulatory stress testing requirements, (v) risk management of capital market 
activities and (vi) valuation adjustments. In addition, banks employ models to manage 
their business effectively, for instance with pricing models, portfolio management models 
and budgeting models.
1.2.2 
When using models to support decisions, banks are exposed to potential losses occurring 
from making decisions based on inappropriate models or the incorrect usage of models. 
This potential loss and the associated adverse consequences are referred to as Model Risk. 
Further details are provided in the definition section.
1.2.3 
In light of this large and complex landscape, the MMS has three key objectives. The first 
objective is to ensure that models employed by UAE banks meet quality standards to
Central Bank of the U.A.E. 
 
11/56

## Page 12

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
adequately support decision-making and reduce Model Risk. The second objective is to 
improve the homogeneity of model management across UAE banks. The third objective 
is to mitigate the risk of potential underestimation of provisions and capital across UAE 
banks.
1.3 
Document structure
1.3.1 
The MMS are accompanied by the Model Management Guidance (“MMG”), which 
expands on technical aspects by model type. Both the MMS and MMG should be read 
jointly as they constitute a consistent set of requirements and guidance, as follows:
(i) 
Part I of the MMS outlines general standards applicable to all models. They 
represent the key components of the Model Management Standards.
(ii) 
Part II of the MMS outlines specific requirements for the application of the 
standards. Both Part I and Part II constitute the minimum requirements to be met 
by a model and its management process so that the model can be used effectively 
for decision-making.
(iii) 
The MMG expands on technical aspects that are expected to be implemented by 
UAE banks for certain types of models. Given the wide range of models and the 
complexity of some models, the CBUAE recognises that alternative approaches 
can be envisaged on specific technical points. However, deviations from the MMG 
should be clearly justified and will be subject to CBUAE supervisory review.
1.3.2 
The MMS is constructed in such a way that all points are mentioned sequentially and 
each point is a unique reference across the entire MMS. Throughout the document, the 
requirements associated with ‘must’ are mandatory, while those associated with ‘should’ 
are strongly recommended as they are regarded as robust modelling practice. The articles 
of the MMG are all articulated with ‘should’.
1.3.3 
Both the MMS and the MMG contain an appendix summarising the main numerical limits 
included throughout each document, respectively. The summary is expected to ease the 
implementation and monitoring of these limits by institutions and the CBUAE.
2 
IMPLEMENTATION
2.1 
Scope of application
2.1.1 
The MMS and the MMG apply to all licensed banks in the UAE, which are referred to 
herein as “institutions”. This scope covers Islamic institutions.
2.1.2 
All institutions must ensure that their models meet minimum quality standards. Simple 
models must not be confused with poorly designed models. Poorly designed models can 
be misleading and interfere with sound decision-making. Consequently, the MMS and 
the MMG apply to all institutions irrespective of their size or sophistication. Small and/or 
unsophisticated institutions can employ simple models that are properly designed.
Central Bank of the U.A.E. 
 
12/56

## Page 13

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
2.1.3 
At a minimum, UAE branches or subsidiaries of foreign institutions must apply the MMS 
and the MMG. Where certain elements of the requirements of the parent company’s 
regulator are more stringent, then these requirements should be implemented. The degree 
of conservatism must be assessed for each model individually and the associated 
calibration. The compliance of the UAE branch or subsidiary with the MMS / MSG may 
require the operational support of their parent company.
2.1.4 
An institution that is a parent company incorporated in the UAE must ensure that all its 
branches and subsidiaries, that are also institutions, comply with the MMS and the MMG.
2.2 
Requirements and implementation timeframe
2.2.1 
The MMS and the MMG will be effective one day after their publication date.
2.2.2 
All institutions are expected to identify gaps between their practice and the MMS and 
MMG and, if necessary, establish a remediation plan to reach compliance. The outcome 
of this self-assessment and the plan to meet the requirements of the MMS and the MMG 
must be submitted to the CBUAE no later than six (6) months from the effective date of 
the MMS.
2.2.3 
Institutions must work towards compliance in a proactive manner. They must 
demonstrate continuous improvements towards meeting these requirements within a 
reasonable timeframe. This timeframe will be approved by the CBUAE following a 
review of the self-assessments. The CBUAE will take a proportionate view in its 
assessment of the proposed time to reach compliance, taking into consideration the size 
and complexity of each institution. The remediation plan and the associated timing must 
be detailed, transparent, and justified. The plan must address each gap at a suitable level 
of granularity.
2.2.4 
Institutions, which repeatedly fall short of the requirements and/or do not demonstrate 
continuous improvement, will face greater scrutiny and could be subject to formal 
enforcement action by the CBUAE. In particular, continuously structurally deficient 
models must be replaced and must not be used for decision-making and reporting.
2.2.5 
The path to remediation may involve reducing the number and/or complexity of models 
in order to improve the quality of the remaining models. Subsequently, and subject to 
remediation needs, the institution could increase the number of models and/or their 
complexity while maintaining their quality.
2.2.6 
Institutions must achieve and maintain full compliance with respect to the general 
principles described in Part I and Part II of the MMS. For the MMG, whilst alternative 
approaches can be considered, the focus is on the rationale and the thought process behind 
modelling choices. Institutions must avoid material inconsistencies, cherry-picking, 
reverse-engineering and positive bias, i.e. modelling approaches that deliberately favour 
a desired outcome. Evidence of an institution defying the general principles in this way 
will warrant a supervisory response ranging from in-depth scrutiny to formal enforcement 
action.
Central Bank of the U.A.E. 
 
13/56

## Page 14

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
2.2.7 
For statistical models in particular, institutions must focus on the suitability of their 
calibration, whether these models are relying on internal data or external data. Lack of 
data will not be an acceptable reason for material models to fall short of these 
requirements. Instead, institutions must implement temporary solutions to mitigate Model 
Risk until models based on more robust data sets are implemented. Institutions must avoid 
excessive and unreasonable generalisations to compensate for lack of data.
2.3 
Reporting to the CBUAE
2.3.1 
Once a plan to reach full compliance is decided and approved, institutions must report 
their remediation progress to the CBUAE at regular intervals, as agreed upon with the 
CBUAE. The CBUAE expects continued and iterative dialogue on this matter during the 
implementation of the plan and thereafter as modelling requirements evolve.
2.3.2 
From the effective date of the MMS, institutions must comply with all CBUAE reporting 
requirements related to model management. The nature, depth and scope of this reporting 
may evolve with modelling techniques and economic conditions.
2.4 
Scope of models
2.4.1 
The MMS applies to all types of models employed by institutions to support decision-
making.  Therefore it covers, amongst others, risk models, pricing models and valuation 
models. The scope of the MMS includes, at a minimum, the non-exhaustive list in Table 
1 below, that represents the most commonly employed model types in UAE institutions.
Table 1: List of most commonly employed model types in UAE institutions
Field 
Model Type 
 
Field 
Model Type 
Credit risk 
Rating and scorecard models 
 
Stress 
Testing (ST)
Credit risk ST  
Score-to-PD models 
 
Market risk ST  
LGD models 
 
 
Counterparty risk ST 
Provision 
computation 
for credit 
risk
PIT PD term structure models 
 
 
Liquidity risk ST 
PIT LGD models 
 
 
Other types of ST models 
PIT EAD models 
 
Operational 
Ops risk scorecards 
ECL models 
 
risk 
Ops risk capital models 
Macro models 
 
Pricing and 
Derivative pricing models 
Market risk 
VaR and related models 
 
finance 
Bond pricing models 
Valuation models 
 
 
RAROC models 
Counterparty 
risk
Exposure models 
 
 
NPV models 
xVA models 
 
Asset and 
EVE models 
Capital  
Capital forecasting models 
 
Liability 
Management
EAR and NII models 
management 
Concentration models 
 
Liquidity risk models 
 
Funding cost models 
 
Business  
Artificial Intelligence  
 
Economic capital models 
 
management 
Budgeting, forecasting  
AML 
Fraud alert and other models 
 
 
Marketing models
Central Bank of the U.A.E. 
 
14/56

## Page 15

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
PART I – GENERAL STANDARDS
The MMS is constructed in such a way that the numbering of each article is sequential and each article is a unique 
reference across the entire MMS. Therefore the numbering continues from the previous Part.
3 
GENERAL STANDARDS
This Part outlines the general principles of the MMS, that is, the key components of the Standards. 
Part I must be read in conjunction with Part II, which explains how these principles must be 
applied. Both Part I and Part II must be regarded as minimum requirements. The key components 
of model management are as follows: (i) model governance, (ii) data management, (iii) model 
development, (iv) model implementation, (v) model usage, (vi) performance monitoring and 
(vii) independent validation. The timeframes and minimum frequencies of model review are 
addressed in Part II.
3.1 
Model governance
3.1.1 
Model governance must reinforce the continuous improvement of modelling practices in 
order for institutions to comply with the requirements of the MMS. Institutions must 
establish a clear plan to comply.
3.1.2 
Institutions must define a comprehensive model management framework to ensure that 
models are used effectively for decision-making and that Model Risk is appropriately 
understood and mitigated. The scope of the model governance must cover all models used 
to make decisions within the institution.
3.1.3 
Model Risk must be incorporated in institutions’ risk framework alongside other key risks 
faced by institutions, as inherent consequences of conducting their activities. 
Consequently, Model Risk must be managed through a formal process incorporating  the 
institution’s  appetite for model uncertainty. The framework must be designed to identify, 
measure, monitor, report and mitigate this risk. A large appetite for Model Risk should 
be mitigated by counter-measures such as conservative buffers on model results, 
additional provisions and/or potentially a Pillar II capital add-on.
3.1.4 
The model management framework must be structured around key components to be 
effective. First, the responsibilities of the stakeholders must be clearly defined with a 
transparent process for modelling decisions, oversight, escalation and for managing 
relationships with third parties. Second, a limit framework must be established to control 
and mitigate Model Risk. Third, the nature, objective and priorities of the modelling tasks 
must be defined. Fourth, appropriate systems, tools and data must be established to 
support model management. Fifth, the framework must include a granular reporting 
process to support pro-active management of Model Risk.
3.1.5 
Institutions must manage each model according to a defined life-cycle composed of 
specific steps, from model design to re-development. The roles and responsibilities of 
stakeholders must be defined for each step of the life cycle. To facilitate model 
management and prioritisation, models must be grouped according to their associated 
Model Risk, or at least based on their associated materiality, as defined in the MMS.
Central Bank of the U.A.E. 
 
15/56

## Page 16

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
3.1.6 
Institutions must establish a Model Oversight Committee which must be accountable for 
all significant modelling decisions related to each step of the model life-cycle. The 
committee must ensure that these decisions are transparent, justified and documented. 
The committee’s main objective is to optimise the ability of models to support decision-
making throughout the institution, covering all model types. The Model Oversight 
Committee is accountable to Senior Management and to the Board, who must ensure that 
the Model Oversight Committee manages Model Risk appropriately and meets the 
requirements articulated in the MMS.
3.1.7 
The Chief Risk Officer (“CRO”) must ensure that the design and usage of models is 
appropriate to support decision-making throughout the institution, in order to minimise 
Model Risk. Therefore, the scope of the CRO’s responsibility in this matter must cover 
the whole institution and must not be limited to the risk function. The CRO must ensure 
that Model Risk is fully managed with suitable identification, measurement, monitoring, 
reporting and mitigation.
3.1.8 
In accordance with Article 2.2 of the Risk Management Regulation 153/2018, the Board 
bears the responsibility for the suitability of the risk management framework. In addition, 
Article 4.3 states that the Board is ultimately accountable for the appropriate usage and 
management of models, whether the approval for the use of models is provided directly 
by the Board or through authorities delegated to Senior Management. Consequently:
(i) 
The Board bears the responsibility of all modelling decisions with material 
implications for the institution and it must define the appetite of the institution 
for Model Risk. Consequently, the Model Oversight Committee must refer 
decisions with material consequences to the Board (or the Board Risk 
Committee). If a Board decision is not deemed necessary, the Board (or the Board 
Risk Committee) must nonetheless be informed of key decisions taken by the 
Model Oversight Committee, with appropriate rationale.
(ii) 
To support the appropriate management of models, the Board must ensure that 
institutions have a sufficient number of internal employees with robust technical 
expertise. The Board must also ensure that Senior Management possess an 
adequate level of technical knowledge to form a judgement on the suitability of 
material modelling decisions.
3.1.9 
The internal audit function is also a stakeholder in model governance. It must assess the 
regulatory compliance and the overall effectiveness of the model management framework 
as part of its regular auditing process. For this purpose, the internal audit function must 
be familiar with the requirements articulated in the MMS and review the model 
management framework against these requirements. The internal audit function must not 
be involved in the validation of specific models.
3.1.10 Institutions can use third parties to support the design, implementation and management 
of models. However, institutions must take responsibility for all modelling decisions, 
model outputs and related financial consequences, even if third parties are involved.
Central Bank of the U.A.E. 
 
16/56

## Page 17

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
3.1.11 To achieve and maintain the quality of models, institutions must ensure that a sufficient 
number of internal technical resources are hired, trained and retained. Each institutions’ 
designated human resource function is responsible for supporting this requirement, 
operationally and strategically.
3.1.12 One of the key elements to manage Model Risk is a robust process for model review and 
challenge. Such review must be independent to be effective. Consequently, institutions 
must clearly define the roles and responsibilities of the development and the validation 
teams to ensure this independence. The validation team must communicate its findings to 
Senior Management and the Board on a yearly basis. The management and reporting of 
Model Risk must also be independent from the development teams.
3.1.13 Dedicated and consistent documentation must be produced for each step of the model 
life-cycle. Institutions must therefore develop model documentation standards. The 
documentation must be sufficiently comprehensive to ensure that any independent party 
has all the necessary information to assess the suitability of the modelling decisions.
3.1.14 The management of models must be supported by a comprehensive reporting framework 
reviewed and analysed at several levels of the organisation, from the development and 
validation teams, up to the Board. This reporting must be designed to support the 
management of Model Risk, covering the identification, measurement, monitoring and 
mitigation of this risk. Reporting must be clear, comprehensive, specific and actionable.
3.2 
Data management
3.2.1 
Accurate and representative historical data is the backbone of financial models. 
Institutions must implement a rigorous and formal data management framework 
(“DMF”) to support the development and validation of accurate models.
3.2.2 
The management of data sets used for modelling should not be confused with the 
management of data used for the production of regular risk analysis and reporting. While 
these two data sets may overlap, they are governed by two different processes and 
priorities. The construction of data for modelling focuses on consistency through long 
time periods, while risk analysis and reporting relies more on point-in-time data. In 
addition, numerous data points needed for modelling are often not included in the scope 
of reporting.
3.2.3 
The DMF must be constructed to fully support each step of the model life-cycle process. 
The DMF must not be the responsibility of the model development or validation teams. 
The DMF must be organised by a separate dedicated function / team within the institution, 
with its dedicated set of policies and procedures.
3.2.4 
The DMF must be comprehensive to adequately support the scope of models employed 
by the institution. It must be coherent with the breadth and depth of models used in 
production. In particular, sophisticated models with numerous parameters and complex 
calibration requirements must be supported by an equally sophisticated DMF.
Central Bank of the U.A.E. 
 
17/56

## Page 18

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
3.2.5 
At a minimum, the DMF must include the following components: (i) systematic 
identification of sources, (ii) regular and frequent collection, (iii) rigorous data quality 
review and control, (iv) secure storage and controlled access and (v) robust system 
infrastructure.
3.2.6 
The data quality review is a key component of the DMF. It must incorporate standard 
checks to assess the data completeness, accuracy, timeliness, uniqueness and traceability.
3.3 
Model development
3.3.1 
The development process must support the construction of the most appropriate models 
in order to meet the objectives assigned to these models.
3.3.2 
The development process must be structured with sequential logical steps that take into 
consideration multiple factors, including but not limited to, the business and economic 
context, the data available, the development techniques, the implementation options and 
the future usage. Consequently, institutions are expected to employ judgement and critical 
thinking in the execution of this process, rather than run it in a mechanistic fashion.
3.3.3 
Model development requires human judgement at each step of the process to ensure that 
the assumptions, design and data meet the objective of the model. Judgement is also 
required to ensure that development methodology is adequate, given the data available. 
Therefore, institutions must identify where judgment is needed in the development 
process. Suitable  governance must be implemented to support a balanced and controlled 
usage of human judgement.
3.3.4 
Each of these components must be regarded as an essential part to complete the whole 
process because each step involves key modelling decisions that can materially impact 
the model outcome and the financial decisions that follow. The process must be iterative. 
This means that if one step is not satisfactory, some prior steps must be repeated.
3.3.5 
The development process must incorporate a degree of conservatism to mitigate Model 
Risk. Any material degree of uncertainty associated with the development steps, in 
particular related to data, must be compensated by conservative choices. For instance, 
conservatism can be reflected during the model selection process or by the usage of 
buffers at any point during the development process. However, conservatism should not 
be employed to hide defects and deprioritise remediation. When conservatism is applied, 
institutions must justify the reasons for it, identify the uncertainty being addressed and 
define the conditions for model improvement.
3.3.6 
The choice of methodology for model development must be the result of a concerted 
structured process. This choice should be made upon comparing several options derived 
from common industry practice and/or relevant academic literature. Methodologies must 
be consistent across the organisation, transparent and manageable.
3.3.7 
Institutions must pay particular attention to the model selection process for all types of 
models. When several models are available, institutions must put in place a documented 
process to select a model amongst several available options.
Central Bank of the U.A.E. 
 
18/56

## Page 19

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
3.3.8 
The pre-implementation validation must be considered an integral part of the 
development process. This step must ensure that the model is consistent, fit for purpose 
and generates results that can be explained and support decision-making appropriately. 
The depth of the pre-implementation validation should be defined based on model 
materiality.
3.4 
Model implementation
3.4.1 
Institutions must consider model implementation as a separate phase of the model life-
cycle process, with its own set of principles.
3.4.2 
The implementation of a model must be treated as a project with clear governance, 
planning, funding and timing. It must include comprehensive user acceptance testing with 
record keeping and associated documentation. Upon request, these records shall be made 
available to the CBUAE, other regulators and auditors to assess whether a particular 
model has been implemented successfully.
3.4.3 
The system infrastructure supporting the ongoing usage of models must be carefully 
designed and assessed before the model implementation phase, to adequately address the 
needs of model usage. It must cope with the demand of the model sophistication and the 
volume of regular production.
3.4.4 
After the model implementation, institutions must regularly assess the suitability of their 
system infrastructure for their current and future usage of models. This assessment must 
be made in light of (i) evolving model design and methodologies, (ii) rapid technology 
developments and (iii) growing volume of transactions to be processed.
3.4.5 
Institutions should avoid spreadsheets for the implementation of large and complex 
models. Where this is unavoidable, and preferably on a temporary basis, institutions must 
implement rules and rigorous validation to mitigate the risks posed by spreadsheet tools 
which are highly susceptible to operational errors. Institutions must implement internal 
policies and guidelines for the development of spreadsheet tools used in production.
3.5 
Model usage
3.5.1 
The conditions for using models must be defined, monitored and managed. Model usage 
must be treated as an integral part of model management because the appropriate usage 
of a model is independent from the quality of such model.
3.5.2 
Institutions must develop policies to manage model usage. At a minimum, the following 
must be included: (i) the definition of the expected usage, (ii) the process to control this 
usage, (iii) the governance surrounding the override of model inputs and outputs, and (iv) 
the management of user feedback.
3.5.3 
Institutions must pay particular attention to circumstances under which model results are 
overridden. They must establish a clear, approved and controlled policy to govern 
overrides. This requirement is applicable to all models.
Central Bank of the U.A.E. 
 
19/56

## Page 20

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
3.6 
Model performance monitoring
3.6.1 
Institutions must implement a process to and monitor the performance of their models on 
a regular basis, as part of their model life-cycle management. The monitoring frequency 
must depend on model types. The required minimum frequencies are set in Part II of the 
MMS.
3.6.2 
Prior to engaging in performance monitoring, institutions must ensure that models are 
used appropriately. This means that the analysis of model usage must have been 
completed successfully.
3.6.3 
The objective of performance monitoring is to assess whether exogenous changes in the 
economic and business environment have impacted the assumptions of the model and 
therefore its performance. The monitoring process must be organised with specific 
responsibilities, monitoring metrics, limits associated with these metrics and required 
reporting for each model and/or model type. The process must incorporate a clear 
decision-making and escalation mechanism.
3.6.4 
The responsibility for the execution of model monitoring must be clearly defined. This 
can be assigned to the development team, the validation team or any independent third 
party. If model monitoring is not performed by the validation team, then the validation 
team must review the quality and relevance of the monitoring reports during the 
validation cycle. Monitoring reports must be presented to the Model Oversight 
Committee on a regular basis, at least every quarter.
3.6.5 
Metrics and limits must be designed to appropriately track the performance of each model 
based on its specific characteristics and its implementation.
3.6.6 
Monitoring reports must be comprehensive, transparent and contain explanations 
regarding the nature of metrics, their acceptable range and respective interpretation. 
These reports must be designed in such way that non-technical readers can understand 
the implications of the observations. Each monitoring report must contain an explicit 
conclusion on the model performance. The report should also include suggestions for 
defect remediation, when deemed appropriate.
3.6.7 
Upon the production of monitoring reports, a clear process must be followed to decide 
whether to either continue using a model (with further monitoring) or suspend it and work 
on remediation. This decision must be made by the Model Oversight Committee.
3.6.8 
The monitoring process is a key preceding step towards the validation process. The results 
of the monitoring process must be used as inputs to the validation process (when 
available), if the monitoring reports are deemed of sufficient quality and relevance by the 
validator.
Central Bank of the U.A.E. 
 
20/56

## Page 21

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
3.7 
Independent validation
3.7.1 
The independent validation must be established as a key step of the model lifecycle 
management and is the basis upon which Model Risk can be assessed and managed. 
Institutions must implement a process to validate independently all their models on a 
regular basis based on model types, as part of their model life-cycle management. 
Minimum frequencies are mentioned in Part II of the MMS.
3.7.2 
In the context of model management, the model owner acts as the first line of defence, 
the independent validator acts as a the second line of defence and the internal audit 
function acts as the third line of defence.
3.7.3 
The validation process must be organised with specific responsibilities, metrics, limits 
and reporting requirements for each model type. The validation process must be 
constructed to ensure an effective identification and remediation of model defects to 
manage Model Risk appropriately. This is referred to as the Effective Challenge principle.
3.7.4 
Model validation can be performed either by an internal independent team or by a third 
party. In all cases, the validation process must remain independent from the development 
process. If model validation is assigned to a third party, institutions remain the owners of 
validation reports and remain responsible for taking appropriate actions upon the issuance 
of these reports. If the institution has an internal validation team and also uses third party 
validators, the internal validation team must maintain oversight of all validation exercises 
conducted by third parties. If the institution does not have an internal validation team, all 
validation reports produced by third parties should be owned by an appropriate internal 
control function separate from the model owner.
3.7.5 
The validation must be independent by virtue of excluding the development team from 
involvement in the assessment of the model. The development team may be involved in 
the validation process once a set of observations has been produced, in particular for the 
remediation of these observations. Institutions must be able to demonstrate to the Central 
Bank, the appropriate arm’s length independence of the validator. Consequently, if a third 
party provides a methodology to develop a model for an institution, any subsequent 
validation exercise must be performed by a party different from the original provider. 
Validation teams must not report to the business lines.
3.7.6 
The validation team must possess sufficient technical skills and maturity to formally 
express its opinion without the interference of the development team or from the business 
lines. The business lines may be consulted during the validation process, but the 
conclusion of such process must be formed independently from business line interests.
3.7.7 
The validation scope must cover both a qualitative validation and a quantitative 
validation. A qualitative validation alone is not sufficient to be considered as a complete 
validation. If insufficient data is available to perform the quantitative validation of a 
model, the validation process must be flagged as incomplete and the institution must 
recognise and account for the uncertainty and thus the Model Risk related to such model.
Central Bank of the U.A.E. 
 
21/56

## Page 22

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
3.7.8 
A validation exercise must result in a full articulated judgement regarding the suitability 
of the model to support decision-making. The analyses and tests performed during the 
validation of a model must be rigorously documented in a validation report, such that (i) 
management is able to form a view on the performance of the model, and (ii) an 
independent party is able to repeat the process on the basis of the report.
3.7.9 
Institutions must put in place an effective process to manage and remedy findings arising 
from validation exercises. Observations and findings across all models must be 
documented, recorded, tracked and reported to Senior Management and the Board at least 
once a year. Findings must be classified into groups based on their associated severity, in 
order to drive the prioritisation of remediation.
3.7.10 Institutions must ensure that model defects are understood and remedied within an 
appropriate time-frame. They must implement an effective process to prioritise and 
address model defects based on their materiality and/or associated Model Risk. High 
severity findings must be remedied promptly. If necessary, such remediation may rely on 
temporary adjustments and/or manual override. Such adjustments and overrides must not 
become regular practice, in that they must have an expiry horizon and must be coupled 
with a plan to implement more robust remediation. Further requirements and minimum 
remediation timings are mentioned in Part II.
3.7.11 Models employed by institutions must be fit for purpose to support decision-making. 
Therefore, institutions must aim to resolve all model defects associated with high and 
medium severity and aim to minimise the number of defects with low severity. If an 
institution decides not to address some model defects, it must identify, assess and report 
the associated Model Risk to Senior Management and the Board. Such decision may 
result in additional provisions and/or capital buffers and will be subject to review by the 
CBUAE.
3.7.12 The internal audit function is responsible for verifying that the model validation process 
is performed appropriately and meets the MMS requirements. This review must be 
planned as part of regular audit cycles. The audit team must comment on the degree of 
independence of the internal validation process. For technical matters, the audit team may 
decide to be assisted by third party experts. Where third party assistance is utilised, the 
internal audit function remains the sole owner of the conclusions of the audit report.
Central Bank of the U.A.E. 
 
22/56

## Page 23

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
PART II – APPLICATION OF THE STANDARDS
The MMS is constructed in such a way that the numbering of each article is sequential and each article is a unique 
reference across the entire MMS. Therefore the numbering continues from the previous Part.
4 
MODEL GOVERNANCE
4.1 
Overview
4.1.1 
Institutions must develop and maintain policies and procedures that support their model 
management framework. In addition, they must regularly ensure that these policies and 
procedures are correctly implemented.
4.1.2 
In addition to the elements mentioned in Part I, institutions must include the following 
components in their model governance framework, at a minimum: (i) the definition of 
model objectives, (ii) steps of model life-cycle, (iii) model inventory, (iv) model 
ownership, (v) identification of key stakeholders involved in decision-making, (vi) 
relations with third parties, (vii) adequacy of internal skills, (viii) comprehensive model 
documentation, and (ix) reporting.
4.2 
Model objectives and strategy
4.2.1 
Institutions must assign a clearly defined objective to each model and include it in the 
model development documentation.
4.2.2 
If stakeholders disagree on the objective of a model, the model must remain under 
development or be removed from production until the disagreement is resolved.
4.2.3 
Institutions must have a defined strategy to meet the objectives of their models. 
Institutions must distinguish between short term tactical solutions from longer term 
solutions. Such strategies must be documented and approved by the stakeholders involved 
in model management, including Senior Management and the Board.
4.2.4 
The modelling strategy must clearly articulate the potential contribution of third party 
consultants to the development, management and validation of models. The outsourcing 
strategy must be defined and justified, in particular regarding data, systems, calibration 
and methodology design. If a quantity of portion of modelling work is outsourced, 
institutions must implement mechanisms to retain controls  control over the key elements 
of modelling.
Central Bank of the U.A.E. 
 
23/56

## Page 24

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
4.3 
Model life-cycle
4.3.1 
Institutions must manage each model according to a cycle that includes, at a minimum, 
the following steps.
(i) 
Development,  
(ii) 
Pre-implementation validation,  
(iii) 
Implementation, 
(iv) 
Usage and monitoring, 
(v) 
Independent validation, and 
(vi) 
Recalibration, redevelopment or retirement, if deemed necessary.
4.3.2 
The duration and frequency of each step must be specified in advance for each model and 
documented accordingly.
4.3.3 
Upon independent validation and the response from the development team, the following 
decisions must be considered by the Model Oversight Committee, which must all be 
thoroughly justified:
(i) 
Leave the model unchanged, 
(ii) 
Use a temporary adjustment while establishing a remediation plan,  
(iii) 
Recalibrate the model,  
(iv) 
Redevelop or acquire a new model, or  
(v) 
Withdraw the model without further redevelopment.
4.4 
Model inventory and grouping
4.4.1 
Institutions must maintain a comprehensive inventory of all their models employed in 
production to support decision-making. The inventory must cover internal models and 
models provided by third parties. It must contain sufficient relevant information to 
support model management and mitigate Model Risk.
4.4.2 
The inventory must cover models both currently in use and employed in the past for 
production (starting from the implementation of this MMS). Institutions must ensure that 
they can refer and/or roll back to previously employed models, if necessary. 
Consequently, institutions must have a model archiving mechanism in place supported 
by appropriate documentation and IT system infrastructure.
4.4.3 
Each model must have a unique nomenclature and identification number that must be 
explicitly mentioned in any related model documentation. A model with a new calibration 
must carry a different identification number. Any variation of a model requiring a 
separate validation or approval should be identified as a separate model.
4.4.4 
The model inventory must include, for each model, all the references and documents 
pertaining to each step of the life-cycle. Amongst others: (i) the dates of each step, 
including past and planned steps, (ii) the internal party responsible for each step, and (iii) 
previous validation exercises and audit reviews plus any reference to their respective 
outcome. Third-party consultants must not be considered as responsible for any step but 
only considered as supporting their execution. Where consultants have been involved, the 
details of the consultants must be recorded.
Central Bank of the U.A.E. 
 
24/56

## Page 25

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
4.4.5 
Models must be grouped based on their associated Model Risk.
(i) 
At a minimum, institutions must create two groups referred to as Tier 1 and Tier 2 
models, with Tier 1 models being more critical than Tier 2 models. If institutions 
already employ more than two groups, those can be retained for internal purpose. 
In the context of the MMS and for regulatory purpose, the models deemed less 
material than Tier 2, must be regarded Tier 2.
(ii) 
Whilst the grouping decisions are left to the discretion of each institution, they will 
be reviewed by the CBUAE as part of its supervisory duty. At a minimum, IFRS9 
models for large portfolios (measured by exposure) and capital forecasting models 
must be classified as Tier 1.
(iii) 
Institutions may prioritise model management by tier once they have established a 
clear grouping framework based on Model Risk. In the MMS, in the absence of 
specific reference to model tiers, the requirements apply to all models irrespective 
of their materiality, as these requirements must be regarded as fundamental 
building blocks of model management. Where needed, the MMS explicitly refers 
to model Tier 1 and Tier 2.
4.5 
Model ownership
4.5.1 
The concept of model ownership is fundamental to model management.  Institutions must 
ensure that an internal owner with a sufficient level of seniority is assigned to each model 
at all times.
4.5.2 
The owner of a model is accountable for all modelling decisions and for ensuring that the 
model goes through all the steps of its life-cycle in a timely fashion. In other words, a 
model owner is not responsible for executing all the steps; however, a model owner must 
ensure that the steps are performed.
4.5.3 
Risk models involving statistical calibration must be owned by the risk department and 
must not be owned by the business lines to avoid conflicts of interest. Pricing and 
valuation models used for commercial decisions can be owned by the business lines. 
Other financial models with no statistical calibration can be owned by the finance 
department, at the discretion of each institution.
4.6 
Stakeholders and decision process
4.6.1 
A modelling decision is defined as a deliberate choice that relates to each step of the 
model life-cycle. In particular, key modelling decisions relate to (i) the model strategy, 
(ii) the choice of data, (iii) the analysis of data, (iv) the methodology and the development 
process, (v) the calibration, and (vi) the implementation of models. Such decision have 
material impacts on model outcomes and have financial implications. Consequently, 
institutions must implement a clear governance process around these decisions.
Central Bank of the U.A.E. 
 
25/56

## Page 26

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
4.6.2 
All parties involved in making decisions required at any step of the model life-cycle must 
be identified and recorded in the model documentation. Within an institution, individuals 
may hold several of these roles (i.e. several responsibilities), with the exception of model 
validation which must remain independent from the other roles. At a minimum, the 
following roles must be identified for each model:
(i) 
Model owner, 
(ii) 
Model developer, 
(iii) 
Model validator,  
(iv) 
Model user, 
(v) 
Modelling data owner, and  
(vi) 
Model Oversight Committee members.
4.6.3 
Institutions must establish a Model Oversight Committee, to whom the stakeholders 
mentioned at 4.6.2 are accountable. This committee must be established separately from 
existing risk management committees. Its scope must cover all models across the 
institution, with the view to manage Model Risk in its entirety. The committee must 
convene regularly and at a minimum every quarter.
4.6.4 
The Model Oversight Committee must provide substantiated decisions related to each 
step of the model life-cycle and in particular, strategic modelling options. Consequently, 
the committee members must have a minimum level of technical understanding to be able 
to contribute to those decisions.
4.6.5 
The Model Oversight Committee must be accountable to Senior Management and the 
Board. The committee must provide an impartial view of the best modelling approach for 
the institution. It must remain independent from actual, potential or perceived interests of 
business lines. Therefore, the majority of the Committee members must not be from the 
business lines. If business views and risk management views related to modelling choices 
are irreconcilable, Senior Management must make a decision, be accountable for it and 
provide a clear rationale for it. The final decision must be in compliance with the 
requirements outlined in the MMS.
4.6.6 
At a minimum, the Model Oversight Committee must hold the following responsibilities.
(i) 
Design the institution’s appetite for Model Risk to be approved by the Board, 
(ii) 
Ensure that Model Risk is managed appropriately across the institution, 
(iii) 
Escalate modelling decisions when necessary,  
(iv) 
Oversee the objective and strategy of each model, 
(v) 
Approve the development of new models, 
(vi) 
Request the development of new models when necessary, 
(vii) Approve material modelling decisions throughout the model life-cycle,  
(viii) At the end of each cycle, review the validation results and make a choice amongst
the options presented in the section 4.3 on model life-cycle.
Whilst some technical aspects of these responsibilities can be delegated to sub-
committees, working groups and/or individuals, the Model Oversight Committee must 
remain the centralised forum where modelling decisions for the whole institution are 
discussed, made or proposed for escalation. Material modelling decisions must be 
ultimately approved by the Board.
Central Bank of the U.A.E. 
 
26/56

## Page 27

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
4.6.7 
Other subject matter experts across the institution and third party experts can contribute 
to each step of the model life-cycle depending on their field of expertise. They can be 
involved in model design, development and testing. However, their involvement must be 
viewed as consultative only.
4.6.8 
The CRO is responsible for ensuring that Model Risk is managed appropriately. 
Consequently, as part of his/her duty, the CRO must ensure that:
(i) 
Model Risk is appropriately identified, understood, estimated, reported and 
mitigated across the institution. 
(ii) 
The governance for model management is efficient and appropriate to the size and 
complexity of the institution.  
(iii) 
The Model Oversight Committee is functioning appropriately and meets the 
responsibilities outlined in article 4.6.6. 
(iv) 
Material modelling decisions are approved by the Board (or the Board Risk 
Committee). The Board is adequately informed of Model Risk, the status of model 
management and the performance of models.  
(v) 
A suitable escalation process is in place through the institution and up to the Board. 
(vi) 
The institution employs adequate resources to meet the demands of model 
management and, where required, escalate identified gaps to Senior Management 
and /or the Board. 
(vii) He/she is fully familiar with the requirements articulated in the MMS. 
(viii) He/she has sufficient technical understanding to form an opinion about the
modelling decisions with material financial implications. 
(ix) 
He/she is sufficiently informed of material modelling decisions, in such a way that 
he/she can articulate a view about the suitability of these decisions. 
(x) 
Particular attention is given to the quality, completeness and accuracy of the data 
used to make decisions based on models.
4.7 
Third party provider
4.7.1 
Institutions must remain the owners of their models at all times, under all circumstances.  
They must remain accountable for all modelling choices, even in the case of support from 
a third party consultant for any of the steps in the life-cycle.
4.7.2 
If modelling support is provided by a third party, institutions must take the necessary 
steps to transfer knowledge from that third party to internal employees within a given 
time frame. This requirement applies to any of the steps of the model life-cycle.
4.7.3 
Third party providers may offer a range of modelling contributions covering, amongst 
others, methodological support, system infrastructure, validation services and ready-
made calibrations based on external data. Institutions must take the necessary action to 
fully understand the contributions provided by third parties. This requirement applies to 
all models and to all risk types.
4.7.4 
In the case of methodological support, whilst institutions must operate within the 
constraints of the acquired model, they must demonstrate that the method is adequate to 
their portfolios. If a methodology acquired from a third party is not fully understood by
Central Bank of the U.A.E. 
 
27/56

## Page 28

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
the institution, then it must not be considered fit for purpose. If a third party provides a 
methodology to an institution, any subsequent validation exercise must be performed by 
an internal or external party independent from the original provider.
4.7.5 
If a third party provides a ready-made calibrated model based on external data, such a 
solution must be justified, based on the following specific circumstances:
(i) 
For portfolios and metrics for which an institution is not able to collect sufficient 
internal data, then externally calibrated models are acceptable. For instance, this 
applies in the case of low default portfolios or small portfolios for which data 
collection may not lead to statistically representative samples.
(ii) 
For portfolios and metrics for which an institution is in a position to collect internal 
data, then externally calibrated models must not be used. Externally calibrated 
models are acceptable, only temporarily over the short term until sufficient data is 
collected. In this case, immediately after the model implementation, institutions 
must take the necessary actions to (i) collect historical internal data from internal 
systems and (ii) collect future internal data in order to develop a model internally.
4.8 
Internal skills
4.8.1 
Institutions must ensure that they acquire and retain adequate internal knowledge and 
core competences about modelling techniques. Full model ownership requires that 
institutions must have an appropriate number of internal employees with technical skills 
to understand and own models, even with the contribution of third parties. The 
contribution of external consultants cannot justify a lack of internal technical employees.
4.8.2 
All institutions must ensure that they have a minimum number of technical employees to 
manage models independently of third parties. The skills of these employees must 
sufficient to cope with the complexity of the models implemented at the institution. If an 
institution does not have the required internal skills to manage complex models, these 
models should be simplified or replaced.
4.8.3 
For branches or subsidiaries of foreign institutions, the internal technical expertise may 
reside at the parent group level, which are responsible for the oversight of the local 
implementation and/or usage of models. The technical experts from the parent entity must 
also oversee any third parties employed to deliver models for the local entity. The local 
branches or subsidiaries must nonetheless have employees with sufficient skills to ensure 
that models are suitably calibrated to the UAE context and meet the CBUAE requirements 
in this regard.
4.8.4 
Knowledge about a model must not be restricted to a single individual in the organisation.  
Instead, knowledge must be shared amongst several staff members. This is necessary for 
the purpose of sound decision-making related to modelling choices and to minimise the 
impact of staff departure on the smooth continuation of model life-cycle execution.
4.8.5 
Institutions are expected to recognise the scarcity of technical staff able to genuinely 
understand and own models. Therefore, they must put in place development plans and 
initiatives to retain and manage their technical employees appropriately. The strategic
Central Bank of the U.A.E. 
 
28/56

## Page 29

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
management of technical resources must include full and adequate cooperation of the 
institutions’ human resources function.
4.9 
Model documentation
4.9.1 
Dedicated and consistent documentation must be produced for each step of the  model 
life-cycle. The documentation must be sufficiently comprehensive to ensure that an 
independent party has all the necessary information to assess the suitability of the 
modelling decisions. In particular, the documentation must make a clear distinction 
between theoretical considerations, calibration choices and practical implementation 
considerations.
4.9.2 
All model documentation, model management policies and procedures must be an 
accurate reflection of the institution’s practice and usage. In other words, institutions must 
ensure that the model attributes described in a modelling document are actually 
implemented. Any gaps and partial implementation must be recorded, tracked and 
reported to Senior Management and the Board by the modelling stakeholders. Institutions 
must have a remediation plan in place to address each of these gaps within an appropriate 
timeframe.
4.9.3 
Institutions must develop internal standards for model documentation across all model 
types, with rigorous document control. This requirement is particularly relevant for the 
development and the validation steps. The documentation must be adapted to the type of 
model, the business context and the step of the life-cycle. At a minimum, all model 
development documentation must include the following information:
(i) 
Document control including the model reference, owners, contributors and key 
dates of each life-cycle step,   
(ii) 
Model materiality in relation to the institution’s risk profile, 
(iii) 
Overview of the model strategy, structure and expected usage, 
(iv) 
Data set description, when applicable, 
(v) 
Methodology and modelling choices related to all the key modelling decisions, 
(vi) 
Modelling assumptions, weaknesses and limitations, 
(vii) Expert judgement inputs if any, 
(viii) Impact analysis of the new modelling decisions, and 
(ix) 
Implementation process and timing of the new modelling decisions.
4.10 Performance Reporting
4.10.1 Institutions must implement a comprehensive reporting framework to ensure that Model 
Risk is analysed and assessed for the purpose of implementing risk mitigating measures.
4.10.2 Reporting must be implemented at several levels of the organisation, including to the 
Model Oversight Committee, the institution’s Risk Committee and the Board. Reporting 
must be specific and adapted to the nature of the stakeholders. The status of model 
management and Model Risk across the entire organisation must be presented to the 
Model Oversight Committee and the institution’s Risk Committee at a minimum on a 
quarterly basis, and to the Board or a specialised sub-committee of the Board at least on 
a yearly basis.
Central Bank of the U.A.E. 
 
29/56

## Page 30

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
4.10.3 Reporting must be designed to support Model Risk management covering the 
identification, measurement, monitoring and mitigation of these risks. In particular, 
reporting must cover (i) the status of the model lifecycle for each model, (ii) the results 
of model performance assessment, (iii) the risks arising from the uncertainty surrounding 
certain modelling decisions, and (iv) the status and estimation of Model Risk throughout 
the organisation.
4.10.4 Institutions must comply with model reporting requirements from the CBUAE, as they 
evolve through time.
4.11 Mergers, acquisitions and disposals
4.11.1 If an institution merges with or acquires another institution, it must re-visit all the 
elements of the model management framework, as part of the integration process. The 
modelling framework and all the principles of model life-cycle management must be 
applied consistently across the newly formed institution. In particular, model ownership 
must be clearly defined. The newly formed institution must have sufficient resources to 
fully manage the new scope of models.
4.11.2 The scope of models must be re-visited to assess whether there is a degree of overlap 
between models. Depending on circumstances, models may need to be recalibrated or 
redeveloped. Models must be representative of the risk profile of the newly formed 
institution. In the case of overlap between two similar models, a new single model must 
be developed based on a larger data sample. This new development must occur promptly 
after the completion of the merger or the acquisition.
4.11.3 Institutions must pay particular attention to the integration of historical data, and future 
data collection, subsequent to the merger or the acquisition. This requirement applies to 
all data fields used as inputs to the existing models and to the future models to be 
developed, in particular, default rates and recovery information. Historical data time 
series must be reconstructed to reflect the characteristics and risk profile of the newly 
formed institution. Upon the implementation of the MMS, this requirement applies 
retroactively to cover, at a minimum, a full economic cycle in the UAE, and where 
possible covering the 2008 global financial crisis. Future data collection must be 
performed for the entire scope of the newly formed institution.
4.11.4 In the case of the disposal of an entity, a subsidiary, a branch and/or a large portfolio, 
institutions must ensure that the modelling framework and all the principles of model 
life-cycle management are adjusted to fit the needs of the reduced scope of portfolios, 
products, obligors and/or exposures.
Central Bank of the U.A.E. 
 
30/56

## Page 31

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
5 
DATA MANAGEMENT
5.1 
Data governance
5.1.1 
For the avoidance of doubt, the scope under consideration in this section includes the data 
employed for modelling and validation purposes, not the data employed for regular risk 
analysis and reporting. This section focuses on the construction of historical data sets for 
the purpose of modelling.
5.1.2 
Accurate and representative historical data is the backbone of financial models.  
Institutions must implement rigorous and a comprehensive formal data management 
framework (“DMF”) to ensure the development of accurate models. Institutions must 
consider DMF as a structured process within the institution, with dedicated policies and 
procedures, and with the adequate amount of resources and funding. The DMF core 
principles are as follows:
(i) 
It must be approved by Senior Management and the Board, 
(ii) 
It must be thoroughly documented with indication of limitations and assumptions, 
(iii) 
Its coverage must include the whole institution and all material risk types, and 
(iv) 
It must be independently validated.
5.1.3 
The DMF must include, at a minimum, the following steps:
(i) 
Identification of sources, 
(ii) 
Regular and frequent collection, 
(iii) 
Rigorous data quality review and control,  
(iv) 
Secure storage and controlled access, and 
(v) 
Robust system infrastructure.
5.1.4 
The roles and responsibilities of the parties involved or contributing to the DMF must be 
defined and documented. Each data set or data type must have an identified owner. The 
owner is accountable for the timely and effective execution of the DMF steps for its data 
set or data type. The owner may not be responsible for performing each of the DMF steps, 
but she/he must remain accountable for ensuring that those are performed by other parties 
with high quality standards.
5.2 
Identification of data sources
5.2.1 
The DMF must include a process to identify and select relevant data sources within the 
institution for each type of data and model. If an institution recently merged or acquired 
another entity, it must carry out the necessary steps to retrieve historical data from these 
entities.
5.2.2 
If internal sources are lacking in data quality or quantity, institutions may rely on external 
sources. However, if an institution decides to rely on external data for modelling, it must 
demonstrate that the data is relevant and suitably representative of its risk profile and its 
business model. External data sources must be subject to an identification and selection 
process. The DMF governance and quality control also apply to external data employed 
for modelling.
Central Bank of the U.A.E. 
 
31/56

## Page 32

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
5.2.3 
Once a source has been selected, institutions are expected to retain this source long 
enough to build consistent time series.  Any change of data source for the construction of 
a given data set must be rigorously documented.
5.3 
Data collection
5.3.1 
Each institution must collect data for the estimation of all risks arising from instruments 
and portfolios where it has material exposures. The data collection must be sufficiently 
granular to support adequate modelling. This means that data collection must be (i) 
sufficiently specific to be attributed to risk types and instrument types, and (ii) sufficiently 
frequent to allow the construction of historical time series.
5.3.2 
The data collection process must cover, amongst others, credit risk, market risk (in both 
the trading and banking books), concentration risk, liquidity risk, operational risk, fraud 
risk and financial data for capital modelling. A justifiable and appropriate collection 
frequency must be defined for each risk type.
5.3.3 
The data must be organised such that the drivers and dimensions of these risks can be 
fully analysed. Typical dimensions include obligor size, industries, geographies, ratings, 
product types, tenor and currency of exposure. For credit risk in particular, the data set 
must include default events and recovery events by obligor segments on a monthly basis.
5.3.4 
The data collection must be documented. The data collection procedure must include 
clear roles and responsibilities with a maker-checker review process, when appropriate.
5.3.5 
Institutions must seek to maximise automated collections and reduce manual 
interventions. Manual interventions must be avoided as much as possible and rigorously 
documented to avoid operational errors.
5.3.6 
The data collection process must ensure the accuracy of metadata such as units, 
currencies, and date/time-stamping.
5.4 
Data quality review
5.4.1 
Prior to being used for modelling purposes, the extracted data must go through a cleaning 
process to ensure that data meets a required quality standard.  This process must consider, 
at a minimum, the following data characteristics:
(i) 
Completeness: values are available, where needed,  
(ii) 
Accuracy: values are correct and error-free, 
(iii) 
Consistency: several sources across the institution lead to matching data,  
(iv) 
Timeliness: values are accurate as of the reporting date, 
(v) 
Uniqueness: values are not incorrectly duplicated in the same data set, and 
(vi) 
Traceability: the origin of the data can be traced.
5.4.2 
Institutions must put in place process to accomplish a comprehensive data quality review. 
In particular, the quality of data can be improved by, amongst others, replacing missing 
data points, removing errors, correcting the unit basis (thousands vs. millions, wrong 
currency, etc.) and reconciling against several sources.
Central Bank of the U.A.E. 
 
32/56

## Page 33

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
5.4.3 
Institutions must put in place tolerance levels and indicators of data quality. These 
indicators must be mentioned in all model documentation. Data quality reports must be 
prepared regularly and presented to Senior Management and the Board as part of the DMF 
governance, with the objective to monitor and continuously improve the quality of data 
over time. Considering the essential role of data quality in supporting risk management 
and business decisions, institutions must also consider including data quality measures in 
their risk appetite framework.
5.5 
Data storage and access
5.5.1 
Once a data set has been reviewed and is deemed fit for usage, it must be stored in a 
defined and shared location.  Final data sets must not be solely stored on the computers 
of individual employees.
5.5.2 
The access to a final data set must be controlled and restricted to avoid unwarranted 
modifications.
5.5.3 
Appropriate measures must be taken to ensure that data is stored securely to mitigate  
operational risks such as cyber-attacks and physical damage.
5.6 
System infrastructure
5.6.1 
Institutions must ensure that an appropriate IT system infrastructure is in place to support 
all the steps required by the DMF.
5.6.2 
The system infrastructure must be sufficiently scalable to support the DMF requirements.
5.6.3 
The system infrastructure must be in the form of strategic long-term solutions, not tactical 
solutions. Spreadsheet solutions must be not considered as acceptable long term solutions 
for data storage.
5.6.4 
Employment of staff with data science knowledge and expertise is encouraged in order 
to undertake appropriate data management oversight.
5.6.5 
Institutions must minimise key person risk related to the management of modelling data. 
They must ensure that several members of staff have the suitable technical expertise to 
fully manage data for modelling purposes.
Central Bank of the U.A.E. 
 
33/56

## Page 34

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
6 
MODEL DEVELOPMENT
6.1.1 
The development of internal models must follow a documented and structured process 
with sequential and logical steps, supporting the construction of the most appropriate 
models to meet the objectives assigned to these models. At a minimum, institutions must 
consider the following components. More components can be added depending on the 
type of model. If a component is not addressed, then clear justification must be provided.
(i) 
Data preparation, 
(ii) 
Data exploration (for statistical models), 
(iii) 
Data transformation, 
(iv) 
Sampling (for statistical models), 
(v) 
Choice of methodology, 
(vi) 
Model construction, 
(vii) 
Model selection, 
(viii) 
Model calibration (for statistical models), 
(ix) 
Pre-implementation validation, and 
(x) 
Impact analysis.
6.1.2 
This process must be iterative, in that, if  one step is not satisfactory, some prior steps 
must be repeated. For instance, if no model can be successfully constructed, additional 
data may be needed or another methodology should be explored.
6.1.3 
Each of these steps must be fully documented to enable an independent assessment of the 
modelling choices and their execution. This requirement is essential to support an 
adequate, independent model validation. Mathematical expressions must be documented 
rigorously to enable replication if needed.
6.1.4 
For the purpose of risk models, a sufficient degree of conservatism must be incorporated 
in each of the development step to compensate for uncertainties. This is particularly 
relevant in the choice of data and the choice of methodology.
6.2 
Data preparation and representativeness
6.2.1 
Institutions must demonstrate that the data chosen for modelling is representative of the 
key attributes of the variables to be modelled. In particular, the time period, product types, 
obligor segments and geographies must be carefully chosen. The development should not 
proceed further if the data is deemed not representative of the variable being modelled. 
The institution should use a conservative buffer instead of a model, until a robust model 
can be built.
6.2.2 
For the purpose of preparation and accurate representation, the data may need to be 
filtered. For instance, specific obligors, portfolios, products or time periods could be 
excluded in order to focus on the relevant data. Such filtering must be supported by robust 
documentation and governance, such that the institution is in a position to measure the 
impact of data filtering on model outputs. The tools and codes employed to apply filters 
must be fully transparent and replicable by an independent party.
Central Bank of the U.A.E. 
 
34/56

## Page 35

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
6.3 
Data exploration
6.3.1 
The data exploration phase must be used to confirm whether the data set is suitable for 
modelling purposes. The objective is to understand the nature and composition of the data 
set at hand and to identify expected or unusual patterns in the data. In this process, critical 
thinking and judgement is expected from the modelling team.
6.3.2 
Descriptive statistics should be produced across both the dependent and independent 
variables. For instance, for credit risk modelling, such exploration is relevant to identify 
whether obligors have homogeneous features per segment and or market risk modelling, 
such exploration is relevant to assess whether the market liquidity of the underlying 
product is sufficient to ensure a minimum reliability of the market factor time series.
6.3.3 
Institutions must clearly state the outcome of the data exploration step, that is, whether 
the data is fit for modelling or not. In the latter case, the development process must stop 
and additional suitable data must be sourced. Consequently, data unavailability must not 
excuse unreliable and inaccurate model output.
6.3.4 
The exploration of data can lead to unusual, counterintuitive or even illogical patterns. 
Such features should not be immediately accepted as a mere consequence of the data. 
Instead, the modelling team is expected to analyse further these patterns at a lower level 
of granularity to understand their origin. Subsequently, either (i) the pattern should be 
accepted as a matter of fact, or (ii) the data should be adjusted, or (iii) the data set should 
be replaced. This investigation must be fully documented because it has material 
consequences on model calibration.
6.4 
Data transformation
6.4.1 
Institutions must search for the most appropriate transformation of the dependent and the 
independent variables, in order to maximise the explanatory power of models. If some 
variables do not need to be transformed, such conclusion must be clearly stated and 
justified in the model development documentation.
6.4.2 
The choice of variable transformation must neither be random nor coincidental.  
Transformations must be justified by an economic rationale.  Amongst others, common 
transformations include (i) relative or absolute differencing between variables, (ii) 
logarithmic scaling, (iii) relative or absolute time change, (iv) ranking and binning, (v) 
lagging, and (vi) logistic or probit transformation. Quadratic and cubic transformations 
are possible but should be used with caution,  backed by  robust economic rationale, and 
should be used with a clear purpose in mind.
6.5 
Sampling
6.5.1 
For all types of statistical models, institutions must ensure that samples used for 
modelling are representative of the target variable to be modelled. Samples must meet 
minimum statistical properties to be eligible for modelling including, amongst others, a 
minimum size and a minimum number of data points.
Central Bank of the U.A.E. 
 
35/56

## Page 36

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
6.5.2 
Once a modelling data set has been identified, institutions should use sampling techniques 
to increase the likelihood of model stability, when possible. The sampling technique must 
be appropriate to the data set and a justification must be provided. Amongst others, 
common techniques include dividing data sets into a development sample and a validation 
sample.
6.6 
Choice of methodology
6.6.1 
Each methodology employed for modelling must be based upon a conscious, rigorous 
and documented choice made under the model governance framework, and guided by the 
model objective. Methodology options can be suggested by third parties, however, the 
choice of a specific methodology remains a decision made within each institution. The 
ownership of a methodology must be assigned to a specific team or function within the 
institution, with sufficient level of seniority. The choice of methodology must be clearly 
stated and justified in the model development documentation.
6.6.2 
The choice of methodology must be made upon comparing several options derived from 
common industry practice and/or relevant academic literature. Institutions must explicitly 
list and document the benefits and limitations of each methodology.
6.6.3 
The choice of methodology must follow the following principles, which must be included 
in the model documentation:
(i) 
Consistency: Methodologies must be consistent and comparable across the 
institution, across risk metrics and risk types. For instance, two similar portfolios 
should be subject to similar modelling approaches, unless properly justified.
(ii) 
Transparency: Methodologies must be clear and well-articulated to all 
stakeholders, including management, internal audit and the CBUAE. Mathematical 
formulation must be documented with all parameters clearly mentioned.
(iii) 
Manageability: A methodology must be chosen only if all the steps of the model 
life-cycle can support it. Complex methodologies must be avoided if any step of 
the model life-cycle cannot be performed.  The choice of methodology must be 
based upon its ability to be implemented and successfully maintained.
6.6.4 
When choosing the most suitable methodology, institutions must avoid excessive and 
unreasonable generalisations to compensate for a lack of data.
6.7 
Model construction
6.7.1 
Statistical models:
(i) 
The construction of statistical models must be based upon robust statistical 
techniques to reach a robust assessment of the coefficients. The statistical 
techniques should be chosen amongst those commonly employed in the industry 
for financial modelling and/or those supported by academic scientific literature.
(ii) 
Institutions must demonstrate that they have undertaken best efforts to understand 
the characteristics of the data and the nature of the relationships between the
Central Bank of the U.A.E. 
 
36/56

## Page 37

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
dependent and independent variables. In particular, institutions should analyse and 
discuss the observed correlations between variables and expected economic 
causations between them. Institutions should discuss the possibility of non-linear 
relationships and second order effects. Upon this set of analysis, a clear conclusion 
must be drawn in order to choose the best-suited approach for the model at hand.  
The analyses, reasoning and conclusions must be all documented.
(iii) 
Statistical indicators must be computed and reported in order to support the choice 
of a model. Thresholds should be explicitly chosen upfront for each statistical 
indicator. The indicators and associated thresholds should be justified and 
documented.
(iv) 
The implementation of statistical techniques is expected to lead to several potential 
candidate models. Consequently, institutions should identify candidates and rank 
them by their statistical performance as shown by the performance  indicators. The 
pool of candidate models should form part of the modelling documentation. All 
model parameters must be clearly documented.
6.7.2 
Deterministic models:
(i) 
Deterministic models, such as financial forecasting models or valuation models, 
do not have statistical confidence intervals. Instead, the quality of their 
construction should be tested through (a) a set of internal consistency and logical 
checks and (b) comparison of the model outputs against analytically derived 
values.
(ii) 
Amongst other checks, one form of verification consists of computing the same 
quantity by different approaches. For instance, cash flows can be computed with a 
financial model through the direct or the indirect methods, which should both lead 
to the same results. Institutions must demonstrate and document that they have put 
in place a set of consistency checks as part of the development process of 
deterministic models.
(iii) 
Several deterministic models can be constructed based on a different set of 
assumptions. These models should constitute the pool of candidate models to be 
considered as part of the selection process.
6.7.3 
Expert-based models:
(i) 
Expert-based models, also referred to as ‘judgemental models’, must be managed 
according to a comprehensive life-cycle as for any other model. The construction 
of such models must follow a structured process, irrespective of the subjective 
nature of their inputs. The documentation must be sufficiently comprehensive to 
enable subsequent independent validations. In particular, the relationship between 
variables, the model logic and the rationale for modelling choices should all be 
documented and approved by the Model Oversight Committee.
(ii) 
The collection of subjective inputs must be treated as a formal data collection 
process. This means that the input data must be part of the DMF, with suitable 
quality control. Expert-based models provided by third parties must be supported 
by an appropriate involvement of internal subject matter experts.
Central Bank of the U.A.E. 
 
37/56

## Page 38

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
(iii) 
Institutions are expected to develop several candidate models based on different 
assumptions. For all candidates, they should assess the uncertainty of the outputs, 
which will be a key driver of the model selection.
(iv) 
Institutions must be mindful of the high Model Risk associated with expert-based 
models. They must be in a position to justify that appropriate actions have been 
taken to manage such Model Risk. An additional degree of conservatism should be 
employed for the design, calibration and usage of expert-based models. The usage 
of such models for material portfolios could result into additional provisions and/or 
capital upon reviews from the CBAUE.
6.8 
Model selection
6.8.1 
For statistical models, institutions must choose a final model amongst a pool of 
constructed models. Institutions must implement an explicit mechanism to filter out 
models and select a final model amongst several available options. It is recommended to 
select a main model and a challenger model up to the pre-implementation validation step. 
The selection of a model should include, at a minimum, the criteria outlined below. 
Institutions should consider all criteria together. Statistical performance should not be the 
only decisive factor to choose a model.
(i) 
The chosen model must demonstrate adequate performance, statistical stability and 
robustness as shown by the statistical indicators and their thresholds.
(ii) 
The chosen model must be based on appropriate causal relationships, i.e. it should 
be constructed with variables and relationships that meet economic intuition and 
make logical business sense, as per the definition section of the MMS. For that 
purpose, causal diagrams are encouraged.
(iii) 
The chosen model must also lead to outcomes that meet economic intuition, can 
be explained easily and can support decision-making appropriately.
(iv) 
The chosen model must be implementable.
6.8.2 
For deterministic and expert-based models, institutions must choose a final model 
amongst the pool of constructed models based on various assumptions. Institutions must 
put in place an explicit mechanism to prioritise certain assumptions and therefore choose 
a model amongst several candidates. In particular, the selection process should 
incorporate the following criteria:
(i) 
The relationships between variables should be based on established causal links. 
The assumptions and limitations of these links should be assessed thoroughly.
(ii) 
The chosen model should lead to outcomes that make meet economic intuition as 
defined in the MMS, can be explained easily and can support decision-making 
appropriately.
(iii) 
The chosen model should be implementable.
Central Bank of the U.A.E. 
 
38/56

## Page 39

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
6.9 
Model calibration
6.9.1 
Model calibration is necessary to ensure that models are suitable to support business and 
risk decisions. Institutions must ensure that model calibration is based on relevant data 
that represents appropriately the characteristics and the drivers of the portfolio subject to 
modelling. This also applies to decisions to override or adjust inputs, coefficients and/or 
variables. Calibration choices must be fully documented and their assessment must also 
form part of the validation process. Models should be re-calibrated when deemed 
necessary, based on explicit numerical indicators and pre-established limits.
6.9.2 
The choice of calibration requires judgement and must be closely linked to the objective 
of each model. In particular, the time period employed for calibration must be carefully 
justified depending on model types. Pricing models should be accurate. Provision models 
should be accurate with a degree of conservatism and should reflect the current and future 
economic conditions. Capital models should be conservative and reflect long term trends. 
Stress testing models should focus on extreme economic conditions.
6.10 Pre-implementation validation
6.10.1 The pre-implementation validation of a model is the first independent validation that 
takes place after the model development. The objective of such validation must ensure 
that the model is fit for purpose, meets economic intuition as defined in the MMS and 
generates results that are assessed as reasonable by expert judgement. The depth of such 
validation must be defined based on model materiality and follow the institution’s model 
management framework. Tier 1 models must be subject to comprehensive pre-
implementation validation.
6.10.2 For the qualitative review, the pre-implementation validation must cover the elements 
presented in Article 10.3 pertaining to the scope of the independent post-implementation 
validation. For the quantitative review, the pre-implementation validation must assess the 
model accuracy, stability and sensitivity as explained in Article 10.4.3 also pertaining to 
the scope of the independent post-implementation validation.
6.10.3 Institutions must document the scope, limitations and assumptions of models as part of 
the pre-implementation validation.
6.11 Impact analysis
6.11.1 The objective of the impact analysis is to quantify the impact of using a newly-developed 
model or a newly-recalibrated model on the production of financial estimates. Where 
applicable, the impact analysis should be documented as part of the model development 
phase and reported to the Model Oversight Committee.
Central Bank of the U.A.E. 
 
39/56

## Page 40

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
7 
MODEL IMPLEMENTATION
7.1.1 
Institutions must consider model implementation as a separate phase within the model 
life-cycle process. The model development phase must take into account the potential 
constraints of model implementation. However, successful model development does not 
guarantee a successful implementation. Consequently, the implementation phase must 
have its own set of documented and approved principles.
7.2 
Project Governance
7.2.1 
The implementation of a model must be treated as a project with clear governance, 
planning, funding, resources, reporting and accountabilities.
7.2.2 
The implementation of a model must be approved by Senior Management and must only 
occur after the model development phase is complete and the model is fully approved.
7.2.3 
The implementation project must be fully documented and, at a minimum, must include 
the following components:
(i) 
Implementation scope, 
(ii) 
Implementation plan, 
(iii) 
Roles and responsibilities of each party, 
(iv) 
Roll-back plan, and 
(v) 
User Acceptance Testing with test cases.
7.2.4 
The roles and responsibilities of the parties involved in the model implementation must 
be defined and documented. At a minimum, the following parties must be identified: (i) 
the system owner, (ii) the system users, and (iii) the project manager.  All parties must be 
jointly responsible for the timely and effective implementation.
7.2.5 
For model implementation, institutions should produce the following key documents, at 
a minimum:
(i) 
User specification documentation: this document should specify requirements 
regarding the system functionalities from the perspective of users.
(ii) 
Functional and technical specification documentation: this document should specify 
the technological requirements based on the user specifications.
(iii) 
A roll back plan: this document should specify the process by which the 
implementation can be reversed, if necessary, so that the institution can rely on its 
previous model.
7.3 
Implementation timing
7.3.1 
Institutions must be conscious that models are valid for a limited period of time. Any 
material delay in implementation diminishes the period during which the model can be 
used. Newly developed models must be implemented within a reasonable timeframe after 
the completion of the development phase. This timeframe must be decided upfront and 
fully documented in the implementation plan.
Central Bank of the U.A.E. 
 
40/56

## Page 41

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
7.4 
System infrastructure
7.4.1 
The IT system infrastructure must be designed to cope with the demand of the model 
sophistication and the volume of regular production. Institutions must assess that demand 
during the planning phase. Institutions should be in a position to demonstrate that the 
technological constraints have been assessed.
7.4.2 
The IT system infrastructure should include, at a minimum, three environments: (i) 
development, (ii) testing, and (iii) production.
7.4.3 
Institutions must have a management plan for systems failure. A system that does not 
comply with the business requirements must be replaced.
7.4.4 
In the case of systems provided by a third party, institutions must have a contingency plan 
to address the risks that may arise if the third party is no longer available to support the 
institution.
7.4.5 
If a system is designed to produce a given set of metrics, then institutions must use that 
system for the production and reporting of those metrics. If a system is not fit for purpose 
despite being implemented, institutions must not use a shadow system or a parallel system 
to produce the metrics that the original system was meant to produce, while maintaining 
the deficient original system. Instead, institutions must decommission any deficient 
system and fully replace it by a functioning system.
7.5 
User Acceptance Testing
7.5.1 
Institutions must ensure that a User Acceptance Testing (“UAT”) phase is performed as 
part of the system implementation plan. The objective of this phase is to ensure that the 
models are suitably implemented according to the agreed specifications.
7.5.2 
The model implementation team must define a test plan and test cases to assess the full 
scope of the system functionalities, both from a technical perspective and modelling 
perspective. The test cases should be constructed with gradually increasing complexity. 
In particular, the test cases should be designed in order to assess each functionality, first 
independently and then jointly. The test cases should also capture extreme and erroneous 
inputs. Partial model replication must be used as much as possible.
7.5.3 
There must be at least two (2) rounds of UAT to guarantee the correct implementation of 
the model. Generally, the first round is used to identify issues, while the second round is 
used to verify that the issues have been remediated.
7.5.4 
The UAT test cases and results must be fully documented as part of the model 
implementation documentation. The test case inputs, results and computation replications 
must be stored and must be available for as long as the model is used in production.
Central Bank of the U.A.E. 
 
41/56

## Page 42

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
7.5.5 
Institutions must ensure that UAT tests and results are recorded and can be presented to 
the CBUAE, other regulators and/or auditors to assess whether a model has been 
implemented successfully. In particular, all rounds of UAT test cases and results must be 
available upon request from the CBUAE, as long as a model is used in production.
7.5.6 
The UAT must be considered successful only upon the sign-off from all identified 
stakeholders on the UAT results. The UAT plan and results must be approved by the 
Model Oversight Committee.
7.5.7 
Institutions must ensure that the model being implemented remains unchanged during the 
testing phase.
7.6 
Production testing
7.6.1 
Institutions must ensure that a production testing phase is performed as part of the system 
implementation plan. The objective of this phase is to guarantee the robustness of the 
system from a technology perspective according to the functional and technical 
specification documentation.
7.6.2 
In particular, the production testing phase must ensure that systems can cope with the 
volume of data in production and can run within an appropriate execution time.
7.7 
Spreadsheet implementation
7.7.1 
It is not recommended that institutions use spreadsheet tools for the usage of material 
models and the production of metrics used for regular decision-making. More robust 
systems are preferred. Nevertheless, if spreadsheets are the only possible modelling 
environment available initially, the standards in 7.7.2 must apply, at a minimum.
7.7.2 
Spreadsheet implementation should follow a quality standard as follows:
(i) 
The spreadsheet should be constructed with a logical flow,  
(ii) 
Formulae should be easily traceable, 
(iii) 
Formulae should be short and constructed in a way that they are easily 
interpreted. It is recommended to split long formula into separate components, 
(iv) 
Tables should include titles, units and comments, 
(v) 
Inputs should not be scattered across the sheets but they should be grouped in one 
worksheet/table, 
(vi) 
Hardcoded entries (i.e. fixed inputs) should be clearly identified, 
(vii) 
Tabs should be clean, i.e. when the implementation is completed, all work in 
progress should be removed, 
(viii) 
Instructions should be included in one or several tabs, and 
(ix) 
Wherever suitable, cells should be locked and worksheets protected, preferably 
by password.
7.7.3 
Models implemented in spreadsheets that deviate from the above criteria must not be 
employed for regular production.
Central Bank of the U.A.E. 
 
42/56

## Page 43

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
7.7.4 
To ensure their robust implementation, spreadsheet tools must include consistency 
checks. Common consistency checks include: (i) computing the same results through 
different methods, (ii) ensuring that a specific set of inputs leads to the correct expected 
output values, and (iii) ensuring that the sensitivities of outputs to changes in inputs are 
matching expected values.
7.7.5 
If an institution employ spreadsheets for regular production, a rigorous maker-checker 
process must be implemented and documented. The review of spreadsheet tools must be 
included in the scope of the independent validation process. In addition, a clear version 
control should be implemented.
Central Bank of the U.A.E. 
 
43/56

## Page 44

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
8 
MODEL USAGE
8.1.1 
Model usage is an integral part of model management. Model usage must be defined, 
documented, monitored and managed according to the following principles.
8.2 
Usage definition and control
8.2.1 
As part of the definition of model strategy and objectives, institutions must articulate and 
document upfront the expected usage of each model. Model usage must cover, at a 
minimum, the following components:
(i) 
The users identified either as individuals or teams,  
(ii) 
The expected frequency of model utilisation, 
(iii) 
The specific source and nature of the inputs in the production environment,  
(iv) 
The destination of the outputs in terms of IT system and operational processes,  
(v) 
The interpretation of the outputs, that is a clear guidance on how the outputs should 
be used, their meaning and the decisions that they can support, 
(vi) 
The limits of the outputs, associated uncertainty and the decisions that can be 
supported by the model versus those that should be supported, and 
(vii) The governance of output overrides.
8.2.2 
Institutions must produce indicators to actively monitor the realisation of the components 
in 8.2.1 and compare them against initial expectations. These must be documented and 
reported as part of the monitoring and validation steps of the model life-cycle.
8.2.3 
Any deviation between the real usage of a model and the expected usage of a model must 
be documented in the monitoring and validation phases and remedied promptly, by 
reverting to the intended usage of the model.
8.3 
Responsibilities
8.3.1 
The management of model usage is shared between several parties. The model owner is 
responsible to define the usage of his/her models. The usage of each model should then 
be approved by the Model Oversight Committee. If the model owner and model user are 
different parties, the owner is responsible to provide documentation and training to the 
user. The model user must therefore follow appropriately the guidance provided by the 
owner.
8.3.2 
The monitoring of model usage can be performed by the model owner, by the validator, 
or both, depending on the institution’s circumstances. Irrespective of the party performing 
the monitoring process, the validator must conduct an independent assessment of the 
appropriate usage of models as part of the validation process. For this purpose, the 
validator should refer to the monitoring reports, when available.
8.3.3 
It may happen that the model owner has limited control over the usage of a model by 
other parties. In this case, the model owner is responsible to report to the Model Oversight 
Committee any model misuse or usage without his consent.
Central Bank of the U.A.E. 
 
44/56

## Page 45

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
8.4 
Input and output overrides
8.4.1 
This section refers to all model types including, but not limited to, rating models. Manual 
overrides of model inputs and outputs are possible and permitted but within limits. For 
this purpose,  institutions must put in place robust governance to manage these overrides. 
Such governance must be reviewed by the internal audit function. Institutions must 
implement limits and controls on the frequency and magnitude of overrides. Models 
whose input and/or outputs that are frequently and materially overridden must not be 
considered fit for purpose and must be recalibrated or replaced.
8.4.2 
During the execution phase, input and/or output overrides must be documented, justified 
and approved at the appropriate authority level. When necessary, an opinion from 
technical subject matter experts should be produced. Overrides used by the business lines 
must be subject of review by the risk management function before being implemented.
8.4.3 
The development and validation teams must analyse and understand the reasons for input 
and/or output overrides and assess whether they are caused by model weaknesses. 
Overrides must be tracked and reported to the Model Oversight Committee, Senior 
Management and the Board as part of the monitoring and validation processes.
8.4.4 
If a model has been approved and is deemed suitable for production, its outputs must not 
be ignored. This also applies when model outputs are not meeting commercial 
expectations. Model outputs must be considered objectively and independently from 
actual, potential or perceived business line interests.
8.5 
User feedback
8.5.1 
Institutions must have a process in place to ensure that model functionalities are working 
as expected during ongoing utilisation.  The objective is to ensure that models have been 
designed, calibrated and implemented successfully.
8.5.2 
The user feedback must cover the model functionalities, stability and consistency of 
output against economic and business expectations. The user feedback must be 
documented and reported as part of the monitoring and validation steps of the model life-
cycle. If model users are different from model developers, institutions must have a 
process in place to collect feedback from the identified model users.
8.6 
Usage of rating models
8.6.1 
Institutions must pay particular attention to the usage of rating models due to their 
material impacts on financial reporting, provisions, risk decisions and business decisions. 
Specific policies and procedures must be designed to govern overrides, including the 
scope of usage, the responsibilities and the conditions of output overrides.
8.6.2 
At a minimum, a rating must be assigned to each obligor on a yearly cycle. In the case of 
exceptional circumstances related to the obligor, the industry or the wider economy, 
ratings may need to be assigned more frequently.
Central Bank of the U.A.E. 
 
45/56

## Page 46

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
8.6.3 
Consistently with Article 8.6.2, upon the roll-out of a new rating model and/or a newly 
recalibrated (optimised) rating model, institutions must update client ratings as soon as 
possible and within a period no longer than twelve (12) months. Further details are 
provided in the MMG on this matter.
Central Bank of the U.A.E. 
 
46/56

## Page 47

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
9 
MODEL PERFORMANCE MONITORING
9.1 
Objective
9.1.1 
Institutions must implement a process to monitor the performance of their models on a 
regular basis, as part of their model life-cycle management. The relationship between 
model performance and usage is asymmetric. A robust model does not guarantee relevant 
usage. However, an improper usage is likely to impact the model performance. 
Consequently, institutions must ensure that models are used appropriately prior to 
engaging in performance monitoring.
9.1.2 
The objective of the monitoring process is to assess whether changes in the economic 
environment, market conditions and/or business environment have impacted the 
performance, stability, key assumptions and/or reliability of models.
9.1.3 
Institutions must implement a documented process with defined responsibilities, metrics, 
limits and reports in order to assess whether models are fit for purpose, on an ongoing 
basis. Upon this assessment, there must be a clear decision-making process to either (i) 
continue monitoring or (ii) escalate for further actions.
9.2 
Responsibility
9.2.1 
The responsibility for the execution of model monitoring must be clearly defined. 
Institutions have the flexibility to assign this task to the development team, the validation 
team or to a third party. If model monitoring is assigned to the development team, the 
monitoring reports must be included in the scope of review of the independent validation 
process. If model monitoring is assigned to a third party, institutions remain the owners 
of monitoring reports and remain responsible to take appropriate actions upon the 
issuance of these reports. Institutions are expected to fully understand and control the 
content of monitoring reports produced by third party providers.
9.2.2 
Monitoring reports must be presented regularly to the Model Oversight Committee. All 
reports containing limit breaches of monitoring metrics must be discussed by the 
committee.
9.2.3 
The internal audit function must verify that model monitoring is performed appropriately 
by the assigned party. In particular, the internal audit function must review the relevance, 
frequency and usability of the monitoring reports.
9.3 
Frequency
9.3.1 
Model monitoring must be undertaken on a frequent basis and documented as part of the 
model life-cycle management. Institutions must demonstrate that the monitoring 
frequency is appropriate for each model. The minimum frequency is indicated in the 
Article (10) of the MMS, which covers the independent validation process.
Central Bank of the U.A.E. 
 
47/56

## Page 48

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
9.4 
Metrics and limits
9.4.1 
Institutions must develop metrics and limits to appropriately track model performance. 
The metrics must be carefully designed to capture the model performance based on its 
specific characteristics and its implementation. At a minimum, the monitoring metrics 
must capture the model accuracy and stability as explained in Article 10.4.3 pertaining to 
the scope of the post-implementation validation. In addition, the monitoring metrics must 
track the model usage to assess whether the model is used as intended.
9.5 
Reporting and decision-making
9.5.1 
Institutions must implement a regular process to report the results of model monitoring 
to the Model Oversight Committee, the CRO and to the model users.
9.5.2 
Reports must be clear and consistent through time. For each model, monitoring metrics 
must be included along with their respective limits. Times series of the metrics should be 
provided in order to appreciate their volatility and/or stability through time and therefore 
help make a view on the severity of limit breaches. Explanations on the nature and 
meaning of each metric must be provided, in such a way that the report can be understood 
by the members of the Model Oversight Committee and by auditors.
9.5.3 
Regardless of the party responsible for model monitoring, all reports must be circulated 
to both the development team and the independent validation team, as soon as they are 
produced. For some models, monitoring reports can also be shared with the model users.
9.5.4 
In each report, explanations on the significance of limit breaches must be provided. 
Sudden material deterioration of model performance must be discussed promptly between 
the development team and the validation team. If necessary, such deterioration must be 
escalated to the Model Oversight Committee and the CRO outside of the scheduled steps 
of the model life-cycle. The Committee and/or the CRO may decide to suspend the usage 
of a model or accelerate the model review upon the results of the monitoring process.
9.5.5 
Institutions must define the boundaries of model usage. These are the limits and 
conditions upon which a model is immediately subject to adjustments, increased margins 
of conservatism, exceptional validation and/or suspension. Specific triggers must be 
clearly employed to identify abnormalities in model outputs.
Central Bank of the U.A.E. 
 
48/56

## Page 49

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
10 INDEPENDENT VALIDATION
10.1 Objective and scope
10.1.1 The independent validation of models is a key step of their life-cycle management. The 
objective is to undertake a comprehensive review of models in order to assess whether 
they are performing as expected and in line with their designed objective. While 
monitoring and validation are different processes run at different frequencies, the content 
of the monitoring process forms a subset of the broader scope covered by the validation 
process. Therefore, when available, the results of the monitoring process must be used as 
inputs into the validation process.
10.1.2 Institutions must put in place a rigorous process with defined responsibilities, metrics, 
limits and reporting in order to meet the requirements of independent model validation.  
Part of the metrics must be common between the monitoring process and the validation 
process. Independent validation must be applied to all models including statistical 
models, deterministic models and expert-based models whether they have been developed 
internally or acquired from a third party provider.
10.1.3 The validation scope must cover both a qualitative validation and a quantitative 
validation. Both validation approaches complement each other and must not be 
considered separately. A qualitative validation alone is not sufficient to be considered as 
a complete validation since it does not constitute an appropriate basis on which modelling 
decisions can be made. If insufficient data is available to perform the quantitative 
validation, the validation process should be flagged as incomplete to the Model Oversight 
Committee, which should then make a decision regarding the usage of the model in light 
of the uncertainty and the Model Risk associated with such partially validated model.
10.1.4 The scope of the validation must be comprehensive and clearly stated. The scope must 
include all relevant model features that are necessary to assess whether the model 
produces reliable outputs to meet its objectives. If a validation is performed by a third 
party, institutions must ensure that the validation scope is comprehensive. It may happen 
that an external validator cannot fully assess all relevant aspects of a model for valid 
reasons. In this case, institutions are responsible to perform the rest of the validation and 
to ensure that the scope is complete.
10.1.5 A validation exercise must result in an independent judgement with a clear conclusion 
regarding the suitability of the model. A mere description of the model features and 
performance does not constitute a validation. Observations must be graded according to 
an explicit scale including, but not limited to, ‘high severity’, ‘medium severity’ and ‘low 
severity’. The severity of model findings must reflect the degree of uncertainty 
surrounding the model outputs, independently of the model materiality, size or scope. As 
a second step, this degree of uncertainty should be used to estimate Model Risk, since the 
latter is defined as the combination of model uncertainty and materiality.
10.1.6 In addition to the finding severity, institutions must create internal rating scales to assess 
the overall performance of each model. This performance rating should be a key input in 
the decision process in each model step of the model life-cycle.
Central Bank of the U.A.E. 
 
49/56

## Page 50

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
10.2 Responsibilities
10.2.1 Institutions must put in place a rigorous process to ensure that models are independently 
validated either by an internal dedicated team or by a third party provider, or both. If 
model validation is assigned to a third party, institutions remain the owners of validation 
reports and must take appropriate action upon the issuance of these reports.
10.2.2 In order to ensure its independence and efficiency, the party responsible for model 
validation (“validator”) must be able to demonstrate all the following characteristics. If 
the validator does not possess all of those, the validation reports must not be considered 
independent and/or robust enough and therefore must not be used for decision-making.
(i) 
Advanced understanding of model methodologies and validation techniques, that 
is sufficiently mature to allow the formulation of independent judgement.
(ii) 
The expertise and freedom to express, hold and defend views that are different 
from the development team and from management. The ability to present those 
views to the Model Oversight Committee, Senior Management and the Board.
(iii) 
The ability to perform independent research and articulate alternative proposals.
10.2.3 The internal audit function is responsible to verify that model validation is performed 
appropriately by the assigned party, following a regular audit cycle. At a minimum, the 
audit function must cover the following scope:
(i) 
Review the governance surrounding the internal validation process and assess its 
independence in light of the MMS.
(ii) 
Form a view regarding the suitability of the depth and scope of the work performed 
by the validation team, also in light of the MMS.
(iii) 
Review the relevance, frequency and effectiveness of the validation process. At a 
minimum, the auditor must review the list of findings issued by the validator and 
assess if the timing necessary for remediation is appropriate.
10.2.4 The internal audit function should employ third party experts to assist on technical matters 
until it can demonstrate that it can perform an adequate review of the model validation 
process without technical support. If the audit team employs supporting experts, it 
remains the sole owner of the conclusions of the audit report.
10.3 Qualitative validation
10.3.1 The independent validation process must include a review of the model conceptual 
soundness, design and suitability of the development process. The scope of the qualitative 
validation varies depending on the statistical or deterministic nature of the model. This 
must include, at a minimum, a review of the following elements:
(i) 
The model governance and decision process,  
(ii) 
The model conceptual soundness, purpose and scope, 
(iii) 
The methodology including the mathematical construction,  
(iv) 
The suitability of the output in terms of economic intuition and business sense as 
defined in the MMS, and 
(v) 
The suitability of the implementation (when the model is implemented).
In addition, for statistical models:
Central Bank of the U.A.E. 
 
50/56

## Page 51

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
(vi) 
The choice of variables and their respective transformation, 
(vii) The suitability of the data in terms of sources, filters and time period, and 
(viii) The suitability of the sampling techniques, if any.
10.4 Quantitative validation
10.4.1 The quantitative validation must assess the suitability of the model output with respect to 
the objective initially assigned to the model. This process must rely on numerical analyses 
to derive its conclusions. Such validation should include a set of dedicated research to 
arrive at an independent judgement. Under certain circumstances, partial model 
replication and/or a challenger model may be necessary to form a judgement.
10.4.2 The set of metrics employed for model validation must at least include those employed 
for monitoring. As a first step, the validator must make a review of the monitoring reports 
and their observations. In addition, institutions should employ a broader spectrum of 
performance metrics to fully assess model performance, since the scope of the validation 
process is larger than that of monitoring.
10.4.3 The assessment of model performance must cover, at a minimum, the following 
components, applicable to both statistical and deterministic models:
(i) 
Accuracy and conservatism: The ability of a model to generate predictions that are 
close to the realised values, observed before and after the model development 
phase. For models whose results are subject to material uncertainty, the validator 
should assess if sufficient conservatism included in the model calibration.
(ii) 
Stability and robustness: Whilst there are theoretical differences between stability 
and robustness, for the purpose of this MMS, this refers to the ability of a model 
to withstand perturbations, i.e. maintain its accuracy despite variability in its inputs 
or when the modelling assumptions are not fully satisfied. In particular, this means 
the ability of a model to generate consistent and comparable results through time.
(iii) 
Controlled sensitivity: This relates to the model construction. Model sensitivity 
refers to the relationship between a change in the model inputs and the observed 
change in the model results. The sensitivity of the output to a change in inputs must 
be logical, fully understood and controlled.
10.4.4 The quantitative validation process should include a review of the suitability, relevance 
and accuracy of following components.
For both statistical and deterministic models: 
(i) 
The implementation, 
(ii) 
The adjustments and scaling factors, if any, 
(iii) 
The ‘hard-coded’ rules and mappings, 
(iv) 
The extrapolations and interpolations, if any, and 
(v) 
The sensitivities to changes in inputs,
In addition for statistical models only:  
(vi) 
The model coefficients,  
(vii) The statistical accuracy of the outputs,  
(viii) The raw data as per the DMF requirements, and 
(ix) 
The historical time series,
Central Bank of the U.A.E. 
 
51/56

## Page 52

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
In addition, for deterministic models only:  
(x) 
A decomposition of the model drivers and their associated sensitivity, and 
(xi) 
A partial replication, when possible.
10.5 Review frequency
10.5.1 All models must be validated at regular frequencies appropriate to model types and tiers. 
The review periods should not be longer than the ones presented in Table 2 below. More 
frequent reviews can be implemented at the discretion of institutions, depending on model 
types and complexity. More frequent reviews may also be necessary in the case of 
unforeseen circumstances, for instance related to changes in model usage and/or changes 
in the economic environment. Less frequent reviews are possible in certain 
circumstances, but they should be justified and will be subject to assessment from the 
CBUAE.
10.5.2 The dates corresponding to the last monitoring and validation exercises must be tracked 
rigorously, included in the model inventory and reported to the Model Oversight 
Committee at least every quarter. The internal audit function must ensure that this 
process is implemented effectively by the model owner and the validator.
Table 2: Minimum monitoring and validation frequencies for most common models
Tier 1 models 
Tier 2 models 
Portfolio 
Model Type 
Monitoring 
Validation 
Monitoring 
Validation 
Wholesale 
Rating 
1 year 
3 years 
2 years 
5 years 
Wholesale 
PD term structure 
1 year 
3 years 
2 years 
5 years
Wholesale 
Macro-PD 
1 year 
2 years 
2 years 
3 years 
Wholesale 
LGD 
1 year 
3 years 
2 years 
5 years 
Wholesale 
Macro-LGD 
1 year 
2 years 
2 years 
3 years 
Wholesale 
EAD 
1 year 
3 years 
2 years 
5 years 
Retail 
Scorecard 
3 months 
1 year 
6 months 
3 years 
Retail 
PD term structure 
1 year 
2 years 
2 years 
3 years
Retail 
Macro-PD 
1 year 
2 years 
2 years 
3 years 
Retail 
LGD 
1 year 
2 years 
2 years 
3 years 
Retail 
Macro-LGD 
1 year 
2 years 
2 years 
3 years 
Retail 
EAD 
1 year 
3 years 
2 years 
5 years 
Trading Book 
VaR and related models  
1 month 
3 years* 
6 months 
4 years* 
Trading Book 
Exposure and xVA 
3 months 
3 years* 
6 months 
4 years*
Multiple 
Valuation 
1 year 
3 years* 
n/a 
4 years* 
Multiple 
Concentration  
1 year 
3 year** 
n/a 
n/a 
Multiple  
IRRBB 
1 year 
3 year** 
n/a 
n/a 
Multiple  
Other Pillar II models 
1 year 
3 year** 
n/a 
n/a 
Multiple 
Capital forecasting 
1 year 
3 year** 
n/a 
n/a 
Multiple 
Liquidity 
1 year 
3 year** 
n/a 
n/a
Central Bank of the U.A.E. 
 
52/56

## Page 53

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
10.5.3 Where [*] is indicated in table 2 above: For pricing and traded risk models such as VaR, 
exposure and xVA models, a distinction should be made between (i) the model 
mechanics, (ii) the calibration and (iii) the associated market data. The mechanics should 
be reviewed at least every 3 to 4 years ; however the suitability of the calibration and the 
market data should be reviewed more frequently as part of the model monitoring process. 
In addition to these frequencies, any exceptional market volatility should trigger a 
revision of all model decisions.
10.5.4 Where [**] is indicated in table 2 above: For deterministic models such as capital 
forecasting, concentration and IRRBB models, a distinction should also be made between 
(i) the model mechanics and (ii) the input data. Whilst the mechanics (methodology and 
system) can be assessed every 3 years, the calibration must be reviewed yearly in order 
to assess the appropriate usage of the model with a new set of inputs. This yearly 
frequency is motivated by the strategic usage of such models in the ICAAP.
10.5.5 For models other than those mentioned in table 2 above, institutions must establish a 
schedule for monitoring and validation that is coherent with their nature and their 
associated Model Risk.
10.6 Reporting of findings
10.6.1 The analyses and tests performed during the validation of a model must be rigorously 
documented in a validation report.  Validation reports must be practical, action orientated, 
focused on findings and avoid unnecessary theoretical digressions. A validation report 
should include, at a minimum, the following components:
(i) 
The model reference number, nomenclature, materiality and classification, 
(ii) 
The implementation date, the monitoring dates and the last validation date, if any, 
(iii) 
A clear list of findings with their associated severity, 
(iv) 
Suggestions for remediation, when appropriate, 
(v) 
The value of each performance indicator with its associated limit, 
(vi) 
The results of the qualitative review as explained above, 
(vii) The results of the quantitative review as explained above, 
(viii) The model risk rating, and 
(ix) 
A conclusion regarding the overall performance.
10.6.2 The model validation report must refer to the steps of the model life-cycle.  Its conclusion 
should be one of the following possible outcomes, as mentioned in the model governance 
section:
(i) 
Leave the model unchanged, 
(ii) 
Use a temporary adjustment while establishing a remediation plan, 
(iii) 
Recalibrate the model, 
(iv) 
Redevelop a new model, or  
(v) 
Withdraw the model without further redevelopment.
Central Bank of the U.A.E. 
 
53/56

## Page 54

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
10.7 Remediation process
10.7.1 Institutions must put in place effective processes to manage observations and findings 
arising from independent validation exercises. The remediation process must be 
structured and fully documented in the institution’s policy. The findings need to be clearly 
recorded and communicated to all model stakeholders including, at least, the development 
team, the members of the Model Oversight Committee and Senior Management. The 
members of the committee must agree on a plan to translate the findings into actionable 
items which  must  be addressed in a timely fashion.
10.7.2 If an institution decides not to address some model defects, it must identify, assess and 
report the associated Model Risk. It must also consider retiring and/or replacing the model 
or implement some other remediation plan. Such decision may result in additional 
provisions and/or capital buffers and will be subject to review by the CBUAE.
10.7.3 Upon completion, the validation report must be discussed between the validator and the 
development team, with the objective to reach a common understanding of the model 
weaknesses and their associated remediation. Both parties are expected to reach a 
conclusion on the validation exercise, its outcomes and its remediation plan. The 
following must be considered:
(i) 
The views expressed by both parties must be technical, substantiated and 
documented. The development team and/or the model owner should provide a 
response to all the observations and findings raised by the validator.
(ii) 
The views expressed by both parties must aim towards a practical resolution, with 
the right balance between theoretical requirements vs. practical constraints.
(iii) 
The resolution of modelling defects must be based on minimising the estimated  
Model Risk implicit in each remediation option.
(iv) 
Outstanding divergent views between both parties should be resolved by the Model 
Oversight Committee.
10.7.4 For each finding raised by the validator, the following must be submitted to the Model 
Oversight Committee for consideration: (i) substantiated evidence from the validator, (ii) 
the opinion of the development team, (iii) a suggested remediation, if deemed necessary, 
and (iv) a remediation date, if applicable. The Model Oversight Committee must decide 
to proceed with one of the options listed in the Article 10.6.2 above. When making a 
choice amongst the various options, the Committee must consider their respective Model 
Risk and associated financial implications.
10.7.5 The validator must keep track of the findings and remediating actions and report them to 
the Model Oversight Committee and Senior Management on a quarterly basis, and to 
the Board (or to a specialised body of the Board) on a yearly basis. Such status reports 
must cover all models and present the outstanding Model Risk. The reports must be 
reviewed by the internal audit function as part of their audit review. Particular attention 
should be given to repeated findings from one validation to the next.
Central Bank of the U.A.E. 
 
54/56

## Page 55

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
10.7.6 If the institution does not have an internal validation team, then reporting of model 
findings and remediation can be performed by another function within the institution. 
However, the internal audit function must regularly review the reporting process to ensure 
that such reporting is an accurate representation of the status of model performance.
10.7.7 Institutions must aim to resolve model findings promptly in order to mitigate Model Risk. 
For that purpose, institutions must develop a process to manage defect remediation 
effectively. This process must include the following principles:
(i) 
High severity findings must be addressed immediately with tactical solutions, 
irrespective of the model Tier. Such solutions can take the form of temporary 
adjustment, overlay and/or scaling in order to reduce the risk of inaccurate model 
outputs and introduce a degree of conservatism. Tactical solutions must not 
become permanent, must be associated with an expiration date and must cease after 
the implementation of permanent remediation.
(ii) 
Institutions must establish maximum remediation periods per finding severity, per 
model Tier and per model type. The remediation period must start from the date at 
which the Model Oversight Committee reaches an agreement on the nature and 
severity of the finding. For findings requiring urgent attention, an accelerated 
approval process must be put in place to start remediation work.
(iii) 
Tactical solutions must only be temporary in nature and institutions should aim to 
fully resolve high severity findings within six (6) months. At a maximum, high 
severity findings must be resolved no later than twelve (12) months after their 
identification. High severity findings, not resolved within 6 months must be 
reported to the Board and to the CBUAE.
(iv) 
When establishing maximum remediation periods, institutions must take into 
account  model types in order to mitigate Model Risk appropriately. For instance, 
defects related to market risk / pricing models should be remedied within weeks, 
while defect remediation for rating models could take longer.
(v) 
For each defect, a clear plan must be produced in order to reach timely remediation. 
Priority should be given to models with greater financial impacts. The validator 
should express its view on the timing and content of the plan, and the remediation 
plan should be approved by the Model Oversight Committee.
10.7.8 At the level of the institution, the timing for finding resolution is a reflection of the 
effectiveness of the validation process and the ability of the institution to manage Model 
Risk. This will be subject to particular attention from the CBUAE. Exceptions to the time 
frame defined by institutions must be formally approved by Senior Management upon 
robust justification and will be reviewed by the CBUAE as part of regular supervision.
Central Bank of the U.A.E. 
 
55/56

## Page 56

CBUAE Classification: Public
Model Management Standards 
Central Bank of the UAE
APPENDIX
NUMERICAL THRESHOLDS INCLUDED IN THE MMS
The MMS contains several numerical thresholds.
The following table indicates the relevant Articles to facilitate their implementation.
Table 3: Numerical thresholds included in the MMS
Article 
Topic 
Threshold 
Strength
6 months from the 
effective date of 
the MMS
2.2.2 
Self-assessment and plan to meet 
the MMS and MMG requirements
Mandatory
4.6.3 
Model Oversight Committee 
meeting 
Quarterly 
Mandatory
Reporting model life-cycle and 
associated Model Risk to the Model 
Oversight Committee and to the 
Board
Quarterly and 
yearly,  
respectively
Mandatory
4.10.2
8.6.2 and 
8.6.3 
Rating frequency 
Annually 
Mandatory
10.5.2 
Reporting of monitoring & 
validation results to the Model 
Oversight Committee
Quarterly 
Mandatory
See table in the 
corresponding 
section
10.5.2 
Maximum periods of model 
validation and monitoring
Strongly recommended
Quarterly and 
yearly,  
respectively
10.7.5 
Reporting of findings and 
remediation to Senior Management
Mandatory
10.7.7 
Maximum remediation period for 
high severity findings 
12 months 
Mandatory
Central Bank of the U.A.E. 
 
56/56
