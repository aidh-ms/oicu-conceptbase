
## Vital Parameters
If no table and schema is specified, all are found under mimiciv_icu.chartevents with the specified itemid.
Currently: 11
* *heart rate*
	* SNOMED ID: 364075005
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=364075005&edition=MAIN&release=&languages=en
		* MIMIC ID: 220045
			* linksto: chartevents
		- eICU: eicu_crd.vitalperiodic, heartrate
* *systolic blood pressure invasive*
	* SNOMED ID: 251071003
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=251071003&edition=MAIN&release=&languages=en
	* MIMIC: 220050
		* linksto: chartevents
	* eICU: eicu_crd.vitalperiodic, systemicsystolic
* *diastolic blood pressure invasive*
	* SNOMED ID: 251073000
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=251073000&edition=MAIN&release=&languages=en
	* MIMIC: 220051
		* linksto: chartevents
	* eICU: eicu_crd.vitalperiodic, systemicdiastolic
* *mean arterial blood pressure invasive*
	* SNOMED ID: 251074006
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=251074006&edition=MAIN&release=&languages=en
	* MIMIC: 220052
		* linksto: chartevents
	* eICU: eicu_crd.vitalperiodic, systemicmean
* *systolic blood pressure non-invasive*
	* SNOMED ID: 251070002
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=251070002&edition=MAIN&release=&languages=en
	* MIMIC: 220179
		* linksto: chartevents
	* eICU: eicu_crd.vitalaperiodic, noninvasivesystolic
* *diastolic blood pressure non-invasive*
	* SNOMED ID: 174255007
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=174255007&edition=MAIN&release=&languages=en
	* MIMIC: 220180
		* linksto: chartevents
	* eICU: eicu_crd.vitalaperiodic, noninvasivediasystolic
* *mean arterial blood pressure non-invasive*
	* SNOMED ID: 251074006
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=251074006&edition=MAIN&release=&languages=en
	* MIMIC: 220181
		* linksto: chartevents
	* eICU: eicu_crd.vitalaperiodic, noninvasivemean
* *urine output*
	* SNOMED ID: 404231008
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=404231008&edition=MAIN&release=&languages=en
	* MIMIC: mimiciv_derived.urineoutput
		* just for now, hotfix because urine is a little complicated....

		```sql
		SELECT * FROM mimiciv_derived.urineoutput; 
		```
	- eicu: https://github.com/MIT-LCP/eicu-code/blob/main/concepts/pivoted/pivoted-uo.sql
* Temperature (irrespective of site) in Celsius
	* SNOMED ID: 386725007
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=386725007&edition=MAIN&release=&languages=en
	* MIMIC ID: 226329, 223762, 223761
		* recalculation of Fahrenheit values necessary!
	* eICU: eicu_crd.vitalperiodic, temperature
* FiO2
	* SNOMED ID: 250774007
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=250774007&edition=MAIN&release=&languages=en
	- MIMIC: mimiciv_derived.bg fiO2
* *oxygen saturation*
	* SNOMED ID: 431314004
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=431314004&edition=MAIN&release=&languages=en
	* MIMIC: 220277
		* linksto: chartevents
	* eICU: eicu_crd.vitalperiodic, saO2
## Respiratory parameters
* PEEP
* Plateau Pressure
* Breath Frequency
* Tidal Volume
## Medications
If non other specified, can be found under mimiciv_icu.inputevents
Currently: 8
- eICU
	- continuous infusion drugs can be found in `eicu_crd.infusionDrug` and queried by `drugname`
		```sql
		SELECT * FROM eicu_crd.infusiondrug WHERE drugname = '{label}';
		```
	- intermittent drugs can be found in `eicu_crd.medication`
* *norepinephrine*
	* SNOMED ID: 45555007
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=45555007&edition=MAIN&release=&languages=en
	* MIMIC: 221906
		* linksto: inputevents
* adrenaline
	* SNOMED ID: 387362001
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=387362001&edition=MAIN&release=&languages=en
	* MIMIC ID:
		* 221289, 229617
* vasopressine
	* SNOMED ID: 77671006
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=77671006&edition=MAIN&release=&languages=en
	* MIMIC ID: 222315
* dobutamine
	* SNOMED ID: 387145002
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=387145002&edition=MAIN&release=&languages=en
	* MIMIC ID: 221653
* Dextrose 5%
	* SNOMED ID: 100347000
	- MIMIC ID: 220949
* NaCl 0.9%
	* SNOMED ID: 101664001
	* MIMIC: 225158
- Albumine 20%
	- SNOMED ID: 347435009
	- MIMIC: 220861
* *Vancomycine*
	* SNOMED ID: 372735009
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=372735009&edition=MAIN&release=&languages=en
	* MIMIC: 225798
		* linksto: inputevents
	* 
## Lab Tests
If no table and schema is specified, all are found under mimiciv_hosp.labevents with the specified itemid
- eICU consideration:
	- Lab values are in eicu_crd.lab and can be filtered by `labname` , results are displayed in `labresult`
	- Queries can look like this:
		- `SELECT * FROM eicu_crd.lab WHERE labname = '{label}'`
Currently: 18
* Leukocyte Count
* Platelet Count
* CRP
* Glucose
* Magnesium
* Calcium
* Phosphate
* *Serum Creatinine*
	* SNOMED ID: 113075003
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=113075003&edition=MAIN&release=&languages=en
	* MIMIC: 50912, 52546
		* linksto: labevents
	* eICU: creatinine
* Urea
	* SNOMED ID: 250623007
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=250623007&edition=MAIN&release=&languages=en
	* MIMIC: 52647, 51006
* Hb
	* SNOMED: 104141003
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=104141003&edition=MAIN&release=&languages=en
		* have a look into this again, it says semiquantitative measuring
	* MIMIC: 50811, 51222, 51640
	* eICU: Hgb
* Arterial blood Lactate
	* SNOMED ID: 372451000119107
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=372451000119107&edition=MAIN&release=&languages=en
	* MIMIC: 50813, 52442
		* linksto: labevents
* Arterial paO2
	- SNOMED ID: 25579001
		-  https://browser.ihtsdotools.org/?perspective=full&conceptId1=25579001&edition=MAIN&release=&languages=en
		* MIMIC: mimic_derived.bg, po2 IF specimen = ART.
* Arterial paCO2
	* SNOMED ID: 167028004
	* MIMIC: mimic_derived.bg, pco2 IF specimen = ART.
* Arterial pH
	* SNOMED ID: 27051004
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=27051004&edition=MAIN&release=&languages=en
	* MIMIC: mimic_derived.bg, pH IF specimen = ART.
* Arterial Bicarbonate
	* SNOMED ID: 443685006
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=443685006&edition=MAIN&release=&languages=en
	* MIMIC ID: mimic_derived.bg, bicarbonate IF specimen = ART. 
* Arterial Base Excess 
	* SNOMED ID: 67487000
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=67487000&edition=MAIN&release=&languages=en
	- MIMIC: mimiciv_derived.bg, baseexcess IF specimen = ART.
* Blood Sodium
	* SNOMED ID: 312469006
	* MIMIC ID:
		* 50824, 50983, 52455, 52623
* Potassium
	* SNOMED ID: 312468003
	* MIMIC ID:
		* 50822, 50971, 52452, 52610
* Chloride
	* SNOMED ID: 104589004
	* MIMIC ID
		* 50902, 50806, 52434, 52535
* *Bilirubine*
	* SNOMED ID: 359986008
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=313840000&edition=MAIN&release=&languages=en
	* MIMIC: 53089, 50885
		* linksto: labevents
- GOT/AST
	- SNOMED ID: 45896001
		- https://browser.ihtsdotools.org/?perspective=full&conceptId1=45896001&edition=MAIN&release=&languages=en
	- MIMIC: 50878
- GPT/APT
	- SNOMED ID: 250637003
		- https://browser.ihtsdotools.org/?perspective=full&conceptId1=250637003&edition=MAIN&release=&languages=en
	- MIMIC: 50861
- gGT
	- SNOMED ID: 60153001
		- https://browser.ihtsdotools.org/?perspective=full&conceptId1=60153001&edition=MAIN&release=&languages=en
	- MIMIC ID: 50927
- Serum LDH
	- SNOMED ID: 273974004
		- https://browser.ihtsdotools.org/?perspective=full&conceptId1=273974004&edition=MAIN&release=&languages=en
	- MIMIC: 50954
- INR
	- SNOMED ID: 440685005
		- https://browser.ihtsdotools.org/?perspective=full&conceptId1=440685005&edition=MAIN&release=&languages=en
	- MIMIC: 51237, 51675
## Demographic Data
Currently: 4
* *Age*
	* SNOMED ID: 424144002
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=424144002&edition=MAIN&release=&languages=en
	* MIMIC: anchor_age in mimiciv_hosp.patients
	* eICU: eicu_crd.patient, age
* *Gender*
	* SNOMED ID: 263495000
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=263495000&edition=MAIN&release=&languages=en
	* MIMIC: gender in mimiciv_hosp.patients
	* eICU: eicu_crd.patient, gender
* *Height*
	* SNOMED ID: 1153637007
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=1153637007&edition=MAIN&release=&languages=en
	* MIMIC: 226730
		* linksto: chartevents
	* eICU: eicu_crd.patient, admissionheight
* *Weight*
	* SNOMED ID: 726527001
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=726527001&edition=MAIN&release=&languages=en
	- MIMIC: 226512
		- linksto: chartevents
	- eICU: eicu_crd.patient, admissionweight
## Procedure Data
Currently: 1
* Dialysis
	* SNOMED ID: 108241001
		* https://browser.ihtsdotools.org/?perspective=full&conceptId1=108241001&edition=MAIN&release=&languages=en
	- MIMIC: mimic_derived.rrt dialysis_present
	- eICU
		 ```sql
		 SELECT * FROM eicu_crd.treatment WHERE treatmentstring LIKE '%dialysis%'
  AND treatmentstring NOT LIKE '%radiology%';
		```
