# Treatment Planning & Optimization

Dose-rate-aware planning, optimization algorithms and delivery strategies for FLASH.

*55 records. Newest first.*

---

### Enabling time-aware treatment plan evaluation for clinical proton pencil beam scanning systems.

*Meijers A, Reimold MN, Pisciotta P, Zou W, Burguete J, Knopf AC et al.* — Physica medica : PM : an international journal devoted to the applications of physics to medicine and biology : official journal of the Italian Association of Biomedical Physics (AIFB) (2026)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Beam Delivery &amp; Technology</span> <span class="badge tag">Modeling &amp; Mechanisms</span>


**TL;DR.** Clinical Treatment Planning Systems (TPS) for proton pencil beam scanning (PBS) typically do not consider treatment delivery time, limiting advanced applications like FLASH therapy, 4D dose calculation, and in vivo verification that depend on accurate temporal modeling. We developed a machine-learning framework to predict machine-specific delivery timing using only standard DICOM-RT plan data.


??? note "Abstract"
    INTRODUCTION: Clinical Treatment Planning Systems (TPS) for proton pencil beam scanning (PBS) typically do not consider treatment delivery time, limiting advanced applications like FLASH therapy, 4D dose calculation, and in vivo verification that depend on accurate temporal modeling. We developed a machine-learning framework to predict machine-specific delivery timing using only standard DICOM-RT plan data. METHODS: A component-based model (predicting spot delivery, spot transition, and layer switch times) was developed using Random Forest regressors. The framework was trained on machine log files and validated on two distinct systems: an IBA ProteusPlus and a Varian ProBeam, incorporating machine-specific pre-processing to handle proprietary logic like spot reordering. RESULTS: The models achieved high accuracy for spot delivery (R2 &gt; 0.98) and spot transition (R2 &gt; 0.95) time prediction on both systems. Energy layer switching time was the primary source of error, leading to an underestimation of total field time (∼3-5%). Despite this, Gamma analysis for predicted dose rate maps against log-file-based maps showed excellent agreement, with pass rates consistently meeting or exceeding 97% (0.5%/2mm criteria). CONCLUSIONS: This work validates a robust, adaptable framework for predicting PBS delivery timing. By enabling time-aware plan evaluation, this model provides the foundation for optimizing treatment efficiency and enabling next-generation, dose-rate-dependent treatment modalities.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/41905127/) · [DOI](https://doi.org/10.1016/j.ejmp.2026.105787)


---

### Single-field-uniform-dose-per-fraction simultaneous dose and dose rate optimization (SFUDPF-SDDRO) method for proton FLASH therapy.

*Luo Y, Zhu YN, Setianegara J, Hong X, Zhang W, Wang C et al.* — Medical physics (2026)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Modeling &amp; Mechanisms</span>


**TL;DR.** The FLASH effect can significantly reduce radiation-induced normal tissue damage while maintaining tumour control, but requires ultra-high dose rates and high doses. PURPOSE: This work proposes a single-field-uniform-dose-per-fraction simultaneous dose and dose rate optimization (SFUDPF-SDDRO) method for proton FLASH radiotherapy to ensure both dose rate and dose meet FLASH effect thresholds.


??? note "Abstract"
    BACKGROUND: The FLASH effect can significantly reduce radiation-induced normal tissue damage while maintaining tumour control, but requires ultra-high dose rates and high doses. PURPOSE: This work proposes a single-field-uniform-dose-per-fraction simultaneous dose and dose rate optimization (SFUDPF-SDDRO) method for proton FLASH radiotherapy to ensure both dose rate and dose meet FLASH effect thresholds. METHODS: The SFUDPF method focuses on delivering the prescription dose for each fraction from only a single field instead of multiple fields, which inherently supports the ultra-high dose rate and high dose necessary for the FLASH effect. We performed retrospective FLASH treatment planning utilizing SFUDPF-SDDRO on four clinical head-and-neck (HN) cases for this study. SFUDPF planning involves delivering each prescription fraction (8 Gy x 5 fx) in 1 beam angle as opposed to multiple beam angles per fraction for IMPT. For each beam delivery, we maximized the FLASH effect in a 1 cm expansion of the HN CTV (CTV+1 cm) by enforcing FLASH dose-rate and dose thresholds of 40 Gy/s and 5 Gy, respectively, in this region. The pencil-beam-scanning dose rate (PBSDR) was calculated voxel-wise by modeling the raster-scanning spot trajectory, while neglecting energy switching times under the assumption of a range modulator capable of expanding a single-energy beam into a spread-out Bragg peak (SOBP). Robust optimization at 3 mm/3.5% was performed to address setup and range uncertainties. We employed iterative convex relaxation and alternating direction method of multipliers algorithms to solve the non-convex optimization problem posed by the SFUDPF-SDDRO model. The FLASH effect was modelled within this work by multiplying the proton dose with a constant 0.7 dose modification factor for voxels fulfilling the dose-rate and dose thresholds to obtain the FLASH effective dose (FED). Effects of FLASH sparing maximization via SFUDPF-SDDRO are verified by comparing with IMPT and VMAT on plan qualities such as (i) high-dose area sparing, (ii) conformity index (CI), and (iii) OAR doses. RESULTS: FLASH RT via SFUDPF-SDDRO compared with IMPT and VMAT was evaluated for four clinical HN cases with different tumor geometries. When compared with their VMAT counterparts, SFUD-SDDRO achieved a considerable reduction of FED for OAR directly adjacent to the CTV. Specifically in case 1, the brainstem D1% decreased from 87.57% to 62.26%, and the spinal cord D10% decreased from 87.36% to 60.74%; in case 2, the D10% of the carotid decreased from 102.46% to 63.30%; in case 3, the D10%of the oral cavity decreased from 94.72% to 62.66%, and the D10% of the oropharynx decreased from 102.5% to 69.09%; in case 4, the D10% of the oral cavity decreased from 88.56% to 59.81%. The SFUDPF-SDDRO achieved a satisfactory CI in terms of FED, indicating that conformity was not sacrificed to achieve the FLASH effect. CONCLUSION: The proposed SFUDPF-SDDRO method is feasible and shows potential clinical benefits for FLASH treatment planning. Maximizing the FLASH effect within a 1 cm ring around the target substantially limits high-dose spillage and enhances OAR sparing compared with conventional approaches.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/41833534/) · [DOI](https://doi.org/10.1002/mp.70291)


---

### Treatment planning comparison of focused very high energy electron and volumetric modulated arc therapy.

*Amstutz F, Zhu C, Volken W, Loebner HA, Mueller S, Frei S et al.* — Physics and imaging in radiation oncology (2026)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Beam Delivery &amp; Technology</span> <span class="badge tag">Modeling &amp; Mechanisms</span> <span class="badge tag">Radiobiology</span>


**TL;DR.** Very high energy electron (VHEE) radiotherapy gained interest owing to technical advances and its potential for FLASH radiotherapy. Magnetically focused VHEE (fVHEE) beams showed promises in preliminary investigations in water phantoms.


??? note "Abstract"
    BACKGROUND AND PURPOSE: Very high energy electron (VHEE) radiotherapy gained interest owing to technical advances and its potential for FLASH radiotherapy. Magnetically focused VHEE (fVHEE) beams showed promises in preliminary investigations in water phantoms. However, inverse treatment planning for fVHEE remains unexplored in clinically motivated scenarios. This study presented first inverse-optimized fVHEE treatment planning, permitting comparison to the current clinical benchmark, volumetric modulated arc therapy (VMAT), independent of FLASH considerations. MATERIAL AND METHODS: Seven cases across five sites (brain, head and neck, lung, prostate, and femoral head) were investigated. fVHEE plans were generated using Monte Carlo-based beamlet dose calculations and in-house inverse optimization. Plans employed 250 MeV electrons focused via idealized magnetic lenses. Plan quality was compared regarding target coverage and organ-at-risk (OAR) sparing. RESULTS: fVHEE achieved equivalent or improved target coverage in four sites, with V95% increasing by up to 4.5% in lung cases. Notable OAR sparing occurred, including D2% reductions of 0.2-7.6 Gy for the spinal canal and esophagus versus VMAT. The femoral head case&#x27;s D2% to the rectum/bladder decreased by 1.3 Gy/2.6 Gy. Compared to VMAT, fVHEE enabled dose deposition via limited beam angles, reducing OAR dose at selected angles and to contralateral structures in lateralized tumors. Prostate cases showed less benefit due to target-OAR proximity in multiple directions, limiting directional selectivity. CONCLUSIONS: First results on inverse-optimized fVHEE planning are encouraging, particularly for lateralized targets or directionally isolated OARs. fVHEE demonstrates potential for selective dose sculpting, further comparison to VHEE is required to isolate fVHEE-specific benefits.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/41783835/) · [DOI](https://doi.org/10.1016/j.phro.2026.100934) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12955155/)


---

### Spread-Out Bragg Peak FLASH Radiotherapy for Head and Neck Reirradiation: A Treatment Planning Study.

*Alomar M, Pin A, Nilsson R, Traneus E, Gan GN, Gao H et al.* — International journal of particle therapy (2026)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Physics &amp; Dosimetry</span>


**TL;DR.** Proton FLASH radiotherapy offers the potential to enhance normal tissue sparing while maintaining tumor control. This study investigates the dosimetric advantages of spread-out Bragg peak (SOBP) FLASH compared to standard intensity modulated proton therapy (IMPT) for re-irradiation in recurrent head-and-neck (HN) cancer.


??? note "Abstract"
    PURPOSE: Proton FLASH radiotherapy offers the potential to enhance normal tissue sparing while maintaining tumor control. This study investigates the dosimetric advantages of spread-out Bragg peak (SOBP) FLASH compared to standard intensity modulated proton therapy (IMPT) for re-irradiation in recurrent head-and-neck (HN) cancer. METHODS: Eight recurrent HN cancer cases were retrospectively analyzed using hypofractionated proton therapy plans (5 × 8 Gy fractions). FLASH plans were designed using a single energy layer and patient-specific modulation devices implemented in the RayStation. Robust optimizations accounted for setup (±3 mm) and range (±3.5%) uncertainties. A biologically effective dose model incorporating a FLASH-modifying factor (FMF) of 0.7 for normal tissues meeting dose (≥5 Gy) and dose rate (≥40 Gy/s) thresholds was used to assess the therapeutic potential of FLASH. Dosimetric parameters such as target coverage, homogeneity index (HI), conformity index (CI), and organ-at-risk (OAR) sparing were compared between FLASH and standard IMPT plans. RESULTS: Compared to standard IMPT, SOBP-based FLASH plans demonstrated reduced target homogeneity (p &lt; .05) and slightly lower dose conformity, with the effects more pronounced for targets near the neck region due to larger center-to-axis distances to avoid collisions. Despite these limitations, FLASH plans maintained robust target coverage (D95% &gt; 96.6% ± 1.2%) in robustness scenarios. The FLASH effective dose model indicated a reduction in the maximum dose to OARs within 2 cm of the target volume; for instance, the maximum dose to the larynx decreased from 29.9 Gy (IMPT) to 25.4 Gy (FLASH). CONCLUSIONS: SOBP-based FLASH plans preserved the dosimetric advantages of IMPT for sparing distal normal tissues while offering potential reductions in high-dose exposure to OARs near the target volume. Incorporating an FMF of 0.7, these plans showed comparable dosimetric profiles to IMPT with the added benefit of enhanced normal tissue protection under uncertainty, a unique advantage over conventional radiotherapy.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/41716727/) · [DOI](https://doi.org/10.1016/j.ijpt.2026.101302) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12914863/)


---

### 3D range modulators for fast, conformal carbon ion therapy: anthropomorphic phantom validation and robustness analysis.

*Hailey Ahn SH, Lysakovski P, Brons S, Karle C, Longarino F, Abdollahi A et al.* — Physics in medicine and biology (2026)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Physics &amp; Dosimetry</span> <span class="badge tag">Beam Delivery &amp; Technology</span> <span class="badge tag">Modeling &amp; Mechanisms</span>


**TL;DR.** Objective. Fast and precise delivery of ion-beam therapy is essential for improving clinical throughput and intrafractional motion management, yet synchrotron-based systems require multiple energy layers for depth dose coverage, resulting in delays on the order of minutes.


??? note "Abstract"
    Objective. Fast and precise delivery of ion-beam therapy is essential for improving clinical throughput and intrafractional motion management, yet synchrotron-based systems require multiple energy layers for depth dose coverage, resulting in delays on the order of minutes. To eliminate energy layer switching times, a fast Monte Carlo (MC)-based workflow for patient-specific 3D range modulators was developed to enable monoenergetic, conformal carbon irradiation at clinically viable speeds. To mirror realistic clinical use, the dosimetric impact of setup and RM geometry deviations from simulated models were assessed.Approach. The workflow begins with spot extraction from clinical intensity modulated particle therapy (IMPT) plans, followed by RM geometry optimization, fast MC dose verification using MonteRay, and 3D printing final geometries. Experimental validations were performed for spread-out Bragg peaks (SOBPs) in water, and two targets in an anthropomorphic head phantom: (1) in a homogeneous brain region and (2) across a heterogeneous bone-soft tissue interface. Robustness against realistic setup and printing errors were assessed in the heterogeneous case.Main results. Each RM geometry was optimized in under one minute and the RM-based plans achieved dose distributions comparable to IMPT with similar target coverage and homogeneity. Simulated and measured depth dose profiles for SOBP plans agreed within 1.2% local deviation in the target. In the head phantom, measured 2D dose maps achieved local gamma pass rates &gt;99% (2%/2 mm, 10% threshold) in both uniform and anatomically complex settings. Plans were robust to setup deviations up to 1 mm, and manufacturing deviations up to 100µm.Significance. This rapid, clinically feasible workflow enables conformal, monoenergetic carbon ion delivery with dosimetric quality comparable to IMPT even in heterogenous scenarios. The substantially reduced treatment delivery time facilitates motion mitigation and higher patient throughput, and may also provide a technical basis for exploring FLASH regimes in synchrotron-based ion beam facilities.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/41525717/) · [DOI](https://doi.org/10.1088/1361-6560/ae36e5)


---

### Novel Treatment Planning Strategy using Single Switching of Universal Range Shifters in Bragg Peak Proton FLASH Radiotherapy.

*Zhang Q, Quan H, Zeng Y, Pang B, Liu M, Chen S et al.* — Medical physics (2026)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span>


**TL;DR.** Bragg peak (BP) proton FLASH radiotherapy (FLASH-RT) holds promise for achieving conformal dose distributions while maintaining ultra-high dose rates (UHDR). However, achieving dose conformality may necessitate patient or beam specific modulation devices.


??? note "Abstract"
    BACKGROUND: Bragg peak (BP) proton FLASH radiotherapy (FLASH-RT) holds promise for achieving conformal dose distributions while maintaining ultra-high dose rates (UHDR). However, achieving dose conformality may necessitate patient or beam specific modulation devices. Moreover, the FLASH effect is substantially diminished during energy layer switching in multi-energy BP FLASH-RT. PURPOSE: This study presents a novel optimization framework that enables single-energy BP FLASH-RT using a single switching of universal range shifters (URS). The proposed approach offers a more generalizable method for conformal FLASH-RT and addresses the impact of energy layer switching on treatment efficacy. METHODS AND MATERIALS: In single-energy BP FLASH-RT planning with a URS (URS plan), both the dose and URS thickness were simultaneously optimized. To emulate an equivalent lower energy layer without switching the proton beam energy, a switchable URS was implemented, thereby generating a treatment plan (sURS plan) that features a single switching of URS event. Subsequently, gradient-based optimization was applied to adjust spot placement within the beam to obtain the final plan, further improving the conformality index. For 10 brain cancer cases and 10 lung cancer cases, both plan types were designed and compared against conventional multi-energy IMPT plans. Additionally, their delivery parameters, dose metrics, and dose rate indicators were analyzed and compared. RESULTS: Both URS and sURS plans met clinical dose criteria and robustness requirements, with significantly fewer energy layers and shorter delivery times compared to IMPT. The treatment times for the URS and sURS plans were 0.8 s and 0.9 s for brain cases and 0.7 s and 0.8 s for lung cases, respectively, compared to 42.3 s for brain and 21.4 s for lung in the IMPT plans. After adding an additional URS thickness, the conformality indexes improved from 0.63 to 0.72 for brain cases and from 0.68 to 0.77 for lung cases, bringing them closer to the high conformity of intensity-modulated proton therapy (IMPT) plans that achieved CI of 0.82 and 0.85. Additionally, the volume of normal tissues exposed to the ADR-based V40Gy/s in the URS plan was 57.8% in brain cases and 49.1% in lung cases. After adding a single switching of URS, these volumes changed to 55.2% and 44.6%, respectively, while IMPT plans showed negligible UHDR coverage. CONCLUSION: The optimization framework enables URS-based plans with a single switching of URS to achieve ultra-high dose rate coverage for normal tissues and enhances conformality.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/41521619/) · [DOI](https://doi.org/10.1002/mp.70275)


---

### Deliverable proton conformal FLASH radiotherapy treatment planning for head and neck re-irradiation patients.

*Zou W, Dong L, Pin A, Nilsson R, Kim M, Apinorasethkul O et al.* — Radiotherapy and oncology : journal of the European Society for Therapeutic Radiology and Oncology (2026)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Beam Delivery &amp; Technology</span> <span class="badge tag">Clinical &amp; Translational</span> <span class="badge tag">Radiobiology</span>


**TL;DR.** Clinical translation of ultra-high dose rate (UHDR) delivery to harness potential FLASH effect requires a treatment planning system (TPS) to optimize and calculate dose and dose rate in patients. Proton conformal FLASH treatment aims to deliver pencil beam scanning (PBS) Bragg Peaks to the tumor region with UHDR.


??? note "Abstract"
    PURPOSE: Clinical translation of ultra-high dose rate (UHDR) delivery to harness potential FLASH effect requires a treatment planning system (TPS) to optimize and calculate dose and dose rate in patients. Proton conformal FLASH treatment aims to deliver pencil beam scanning (PBS) Bragg Peaks to the tumor region with UHDR. In this work, we conducted a treatment planning study for head and neck (H&amp;N) re-irradiation patients using a research-version of a commercial TPS paired with conformal FLASH hardware integrated into a nozzle of a clinical cyclotron-based system. METHODS: Fifteen H&amp;N patients were planned for re-irradiation of 40 GyRBE in 5 fractions to the area of intact tumor. The TPS was configured with validated UHDR beam measurement to generate optimized patient FLASH plans with one or two beams, delivered as single-beam-per-fraction (SBPF). Each beam consists of a deliverable mono-energetic PBS map, a 3D-printable conformal energy modulator design, a selection of aluminum range shifter plates, and a brass aperture. Python scripts with machine-specific delivery timing parameters were used for Monte Carlo dose and dose rate calculations. Clinical VMAT and IMPT plans were also generated for dosimetric comparison. RESULTS: All plans met the tumor target and OAR planning objectives. Conformal FLASH plans showed very similar dose distributions to the clinical IMPT plans. Compared to VMAT plans, both IMPT and FLASH plans have reduced low dose region, maximum cord dose D0.03 cc (8.37 ± 0.94 vs. 3.19 ± 3.81 and 4.32 ± 3.12 GyRBE, respectively), contra-lateral parotid mean dose (1.88 ± 0.99 vs. 0.00 ± 0.01 and 0.00 ± 0.00 GyRBE, respectively) and contra-lateral submandibular gland mean dose (2.49 ± 1.06 vs. 0.14 ± 0.13 and 0.19 ± 0.19 GyRBE, respectively). With 500 nA quasi-continuous nozzle beam current, the mean dose-averaged dose rate in CTVs of these 15 patients achieved 95.75 ± 22.78 Gy/s. CONCLUSIONS: We report the deliverable proton conformal FLASH treatment plans for H&amp;N re-irradiation patients using the innovative hardware configuration and measured beam data in our institution. The FLASH plans have very similar plan qualities to clinical IMPT proton plans and were deliverable with our proton machine. The machine specific 3D dose rate distribution can be calculated and displayed in the TPS.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/41423134/) · [DOI](https://doi.org/10.1016/j.radonc.2025.111349) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13151878/)


---

### Mitigating the impact of FLASH-model uncertainties through personalized FLASH optimization functions for delivery pattern optimization for lung IMPT.

*van Zon MC, Breedveld S, Hoogeman MS, Habraken SJM* — Physics in medicine and biology (2026)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span>


**TL;DR.** Objective.It is generally assumed that the FLASH effect is triggered at dose rates (DRs) of at least 40 Gy s-1, while recent studies indicate that this threshold is not binary but follows a sigmoid across samples. Some patients may thus already experience the FLASH effect at lower DRs, while the current FLASH models do not account for this.


??? note "Abstract"
    Objective.It is generally assumed that the FLASH effect is triggered at dose rates (DRs) of at least 40 Gy s-1, while recent studies indicate that this threshold is not binary but follows a sigmoid across samples. Some patients may thus already experience the FLASH effect at lower DRs, while the current FLASH models do not account for this. We propose a method that aims to maximally exploit the FLASH effect over a wider dose-rate range through dose-rate-dependent FLASH delivery pattern optimization (DPO) functions while maintaining the FLASH effect at the currently accepted binary dose-rate threshold of 40 Gy s-1.Approach.We optimized and evaluated FLASH-weighted dose (FWD) distributions for 1397 FLASH optimization functions. All FLASH optimization functions were used to optimize the FWD distribution using DPO. The generated FWD distributions were evaluated in case FLASH is triggered at DRs ranging from 10 to 60 Gy s-1and compared to the FWD distribution that was optimized under the assumption that FLASH is only and maximally triggered at 40 Gy s-1.Main results.(i) Substantial improvements in FWD distributions were obtained using FLASH optimization functions. (ii) The optimal FLASH optimization function differs both per patient and per beam. (iii) FLASH optimization function class solutions can also lead to an overall improvement of FWD distributions.Significance.We demonstrated that substantial improvements in FWD distributions can be achieved by using FLASH optimization functions that exploit the FLASH effect over a wider dose-rate range.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/41411757/) · [DOI](https://doi.org/10.1088/1361-6560/ae2f16)


---

### Assessing the potential and pitfalls of spot sequence optimization for OAR-specific dose rate control in proton PBS Bragg peak FLASH radiotherapy.

*Diao L, Zhao X, Cheng C, Zhang T, Wei S, Meng D et al.* — Radiotherapy and oncology : journal of the European Society for Therapeutic Radiology and Oncology (2026)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Physics &amp; Dosimetry</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Beam Delivery &amp; Technology</span>


**TL;DR.** To evaluate the impact of key treatment planning parameters-including beam arrangement, minimum monitor unit (MMU) settings, and anatomical site variability-on the ability to achieve ultra-high dose rate (UHDR) delivery in Bragg peak FLASH radiotherapy. METHODS: FLASH dose rate coverage can be assessed by dose-rate volume histogram (DRVH), thus objective functions based on DRVH can be constructed …


??? note "Abstract"
    PURPOSE: To evaluate the impact of key treatment planning parameters-including beam arrangement, minimum monitor unit (MMU) settings, and anatomical site variability-on the ability to achieve ultra-high dose rate (UHDR) delivery in Bragg peak FLASH radiotherapy. METHODS: FLASH dose rate coverage can be assessed by dose-rate volume histogram (DRVH), thus objective functions based on DRVH can be constructed to optimize the dose rate distribution for individual regions of interest (ROIs). The optimization of each ROI, as part of the final objective function, is integrated into a multi-objective optimization problem that can be solved using a heuristic algorithm. A phantom-based study was conducted to investigate the effect of beam number on optimization performance in proton therapy planning. Treatment plans of 8 consecutive node-negative non-small cell lung cancer and 5 consecutive liver cancer patients were initially optimized, followed by optimizing the spot delivery sequence to enhance dose rate ratios without compromising dose performance. A thorough evaluation was conducted to assess the optimization of the scanning pattern in improving the FLASH ratio of critical OARs in Bragg peak FLASH-RT, considering beam currents, beam arrangement, MMU constraints, and anatomical sites in lung and liver cases. RESULTS: The phantom study demonstrated that the effectiveness of the spot pattern in dose rate depends on the number of beams and beam arrangement, and the 3-field arrangement can achieve better optimization effects. In lung cases, using a MMU of 600 (nozzle current of 252nA), scanning pattern optimization increased the average dose rate (V40Gy/s) for the esophagus, heart, spinal cord, and lung-GTV from 38.3 %, 62.8 %, 59.6 % and 61.9 % to 74.4 %, 85.5 %, 83.3 % and 78.6 %, respectively (all p-values &lt; 0.001). When a higher MMU of 1200 (nozzle current of 504nA) was used, the benefits brought by optimization are not as obvious as the previous situation. For all liver cases with an MMU of 600, the average FLASH dose rate (V40Gy/s) for the esophagus, heart, spinal cord, and liver-GTV increased from 60.5 %, 52.7 %, 60.3 %, and 59.1 % to 75.1 %, 69.4 %, 80.2 %, and 75.9 %, respectively, after optimization (all p-values &lt; 0.001). However, when a higher MMU of 1200 was used, the V40Gy/s for all four OARs increased from approximately 93.3 % to 97.0 %, showing only limited additional improvement. CONCLUSION: This approach successfully optimized FLASH dose rate coverage for specific OARs, enhancing BP-FLASH effectiveness by improving OAR protection while maintaining dosimetric quality. However, the impact of spot pattern optimization is influenced by factors such as the number of beams, MMU constraints, and spot distribution, with limited effectiveness in significantly increasing the FLASH ratio.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/41271173/) · [DOI](https://doi.org/10.1016/j.radonc.2025.111291)


---

### The impact of dose rate optimisation and robust optimisation on FLASH proton therapy treatment plan quality and dose rates.

*Lövgren N, Nilsson R, Traneus E, Petersson K* — Frontiers in oncology (2025)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span>


**TL;DR.** Bragg peak FLASH proton therapy (FLASH-PT) relies on fast dose delivery (≥ 40 Gy/s) to elicit a normal tissue sparing effect. FLASH-PT beam delivery modifications lead to inferior margin-based FLASH-PT treatment plan quality compared to intensity modulated proton therapy (IMPT).


??? note "Abstract"
    BACKGROUND AND PURPOSE: Bragg peak FLASH proton therapy (FLASH-PT) relies on fast dose delivery (≥ 40 Gy/s) to elicit a normal tissue sparing effect. FLASH-PT beam delivery modifications lead to inferior margin-based FLASH-PT treatment plan quality compared to intensity modulated proton therapy (IMPT). To achieve ultra-high dose rates to regions of interest, dose rate optimisation may need to be utilised as part of the treatment planning process. This study aims to determine the impact of dose rate optimisation and robust optimisation on FLASH-PT treatment plan quality and achievable dose rates. All FLASH-PT plans are also compared to IMPT plans to determine the clinical applicability of the technique. MATERIALS AND METHODS: FLASH-PT and IMPT treatment plans were generated for bone (n = 3), brain (n = 4) and lung (n = 3) targets for a one-beam-per-fraction and multi-beam-per fraction delivery, respectively. The open-source MIROpt treatment planning system (TPS) was used to generate dose rate optimised FLASH-PT plans, while a research version of the RayStation TPS was used to generate non-dose rate optimised, margin-based, and robust FLASH-PT plans. Dose rate coverage was evaluated for different dose and dose rate thresholds. RESULTS AND CONCLUSION: Dose rate optimised FLASH-PT plans were associated with significantly worse target dose coverage, whilst significantly improving dose rate coverages to organs at risk, compared to non-dose rate optimised plans. The use of dose rate optimisation should be used with caution as it may lead to degraded plan quality. Robust optimisation improved target coverage compared to margin-based plans, without compromising dose rate coverage. FLASH-PT plans struggle to achieve IMPT-equivalent D95% and is associated with non-significant increases in organ at risk doses compared to IMPT, regardless of TPSs and treatment planning techniques (margin and robust). Future work will focus on improving D95%, reducing organ at risk doses, and optimising MU/spot delivery to improve plan quality, while further increasing the dose rates.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/41487594/) · [DOI](https://doi.org/10.3389/fonc.2025.1638319) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12757242/)


---

### Proton pencil beam scanning ultra-high dose rate 3D lattice radiotherapy: A proof-of-concept FLASH SFRT study.

*Wei S, Qi H, Xu L, Selvaraj B, Zhao X, Zheng A et al.* — Medical physics (2025)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Physics &amp; Dosimetry</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Beam Delivery &amp; Technology</span>


**TL;DR.** 3D lattice radiation therapy (3D-LRT) is an effective treatment solution that can offer excellent local tumor control with limited morbidity. Pencil beam scanning (PBS) proton therapy achieves excellent dose conformity and eliminates exit doses to normal tissue, making it a great candidate to implement 3D-LRT.


??? note "Abstract"
    BACKGROUND: 3D lattice radiation therapy (3D-LRT) is an effective treatment solution that can offer excellent local tumor control with limited morbidity. Pencil beam scanning (PBS) proton therapy achieves excellent dose conformity and eliminates exit doses to normal tissue, making it a great candidate to implement 3D-LRT. But it may also introduce high entrance doses to normal tissues. Ultra-high dose rate (UHDR) beams may offset this disadvantage by triggering the FLASH normal tissue protection effect. PURPOSE: We conducted the first-ever feasibility study of applying proton PBS UHDR beams to 3D-LRT. This study aims to evaluate the dosimetric feasibility and potential benefits of integrating ultra-high dose rate proton beams with spatially fractionated lattice treatment techniques. METHODS: Two-field and single-field approaches targeting individual vertex were developed to achieve proton PBS UHDR 3D-LRT, in combination to conventional intensity-modulated proton therapy (IMPT) that targets the entire gross tumor volume (GTV). In a two-field technique, beam-modifying devices, including a universal range shifter and beam-specific range compensator, were used to implement distal edge tracking (DET) of single-energy Bragg peak beams to achieve conformal dose to the target volume. Apertures were employed to sharpen the lateral dose fall-off and enhance the peak-to-valley dose ratio (PVDR) for effective 3D-LRT. In a single-field technique, a universal ridge filter was added upstream to broaden Bragg peak beams for uniform and conformal vertex coverage. 3D-LRT treatment plans were designed following published guidelines and evaluated in nine diverse representative cases of three treatment sites: head and neck (H&amp;N), liver, and lung. The prescription dose was 18 GyRBE to vertices and 3 GyRBE to the GTV. These were assessed in terms of nominal plan quality, UHDR coverage to normal tissues, and plan robustness. End-to-end validation was performed on a head-and-neck phantom; dose and dose rate were measured with EBT-XD radiochromic films and a GRID ionization-chamber array and compared against the treatment plan. RESULTS: The two-field technique achieved an average PVDR1 (D2%/D50%) and PVDR2 (D10%/D90%) of 4.4 ± 0.4 and 4.2 ± 0.2, compared to 4.9 ± 0.6 and 4.7 ± 0.3 with the single-field technique. Vertex D90% was higher in the two-field plans (19.7 ± 0.5 GyRBE) than in the single-field plans (19.2 ± 0.6 GyRBE). The two-field technique significantly reduced skin doses, with a D1cc of 9.2 ± 0.9 GyRBE vs. 15.1 ± 0.5 GyRBE in the single-field technique. Both techniques achieved high UHDR coverage, with an average V40GyRBE/s to the skin of 100% for both two-field plans and single-field plans, for doses above 5 GyRBE. Relatively small differences in plan robustness were observed regarding PVDR, D90%, and skin D1cc between the two techniques. End-to-end study achieved consistent dose distribution between measurements and plans with gamma passing rates between 93.4% and 96.7% for two-field and single-field approaches, respectively. The measured dose-rate exceeded 40GyRBE/s for both single-field and two-field plans with average error of 5% compared to plans. CONCLUSION: Proton PBS UHDR 3D-LRT is achievable with the proposed two-field and single-field techniques, leveraging advanced inverse treatment planning and beam modifiers such as universal range shifters, beam-specific range compensators, apertures, and ridge filters. Planning study and end-to-end validation demonstrated that both techniques provided UHDR coverage to entrance normal tissues, favorable for triggering the FLASH effect, while maintaining high PVDR and plan robustness.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/41330730/) · [DOI](https://doi.org/10.1002/mp.70187)


---

### Joint range-modulator and spot optimization for Bragg-peak proton FLASH radiotherapy.

*Han J, Wang A, Zhu YN, Li W, Lin Y, Gao H* — Medical physics (2025)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Physics &amp; Dosimetry</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Clinical &amp; Translational</span>


**TL;DR.** Ultra-high-dose-rate (UHDR) radiation therapy has demonstrated promising potential in reducing toxicity to organs-at-risk (OARs). Proton therapy is uniquely positioned to deliver UHDR by leveraging the Bragg peak in conjunction with patient-specific range modulators (PSRMs) to generate a spread-out Bragg peak (SOBP).


??? note "Abstract"
    BACKGROUND: Ultra-high-dose-rate (UHDR) radiation therapy has demonstrated promising potential in reducing toxicity to organs-at-risk (OARs). Proton therapy is uniquely positioned to deliver UHDR by leveraging the Bragg peak in conjunction with patient-specific range modulators (PSRMs) to generate a spread-out Bragg peak (SOBP). Existing proton FLASH (pFLASH) treatment planning workflows typically follow a two-step process: 1) generating a multi-energy intensity-modulated proton therapy (IMPT) plan to determine spot weights and 2) subsequently converting this plan into a single-energy pFLASH delivery using PSRM optimization. However, the intrinsic coupling between spot weight distribution and PSRM design has not been fully investigated, which may limit the achievable dosimetric and radiobiological advantages of pFLASH therapy. PURPOSE: This work proposes a novel alternating optimization framework-Joint Range-Modulator and Spot Optimization (JRSO)-that simultaneously optimizes the PSRM and spot weights to improve the plan quality of conformal pFLASH therapy. METHODS: Compared to the conventional method, JRSO does not require a one-to-one correspondence between beam spots and PSRM pins. Proton beam diffusion from the delivery system to the PSRM is modeled by Gaussian function. To achieve better plan quality, starting from an initial solution derived from a conventional IMPT plan, JRSO iteratively updates the PSRM design and spot weights in an alternating manner. This process progressively refines both parameters while ensuring compliance with practical delivery constraints, such as the minimum monitor-unit (MMU) requirement. RESULTS: JRSO obtained improved plan quality compared to the conventional method. For example, in a head-and-neck (HN) case, JRSO reduced the objective function value from 0.46 to 0.26, lowered the maximum target dose from 117.6% to 107.1%, improved the conformity index from 0.74 to 0.87, and decreased the region-of-interest (ROI) effective dose from 6.50  to 6.10 Gy. CONCLUSION: A new optimization method JRSO is proposed for conformal pFLASH radiotherapy. It outperforms the conventional approach and may extend the applicability of PSRM to more complex clinical scenarios, particularly those involving misalignments between beam spots and pins. Numerical results demonstrate the robustness and efficiency of the new method.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/41316733/) · [DOI](https://doi.org/10.1002/mp.70171)


---

### Monoenergetic Bragg peak FLASH proton therapy with universal range shifter in multi-field optimization.

*Zhang Q, Zeng Y, Pang B, Liu M, Chen S, Wang H et al.* — Physics in medicine and biology (2025)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span>


**TL;DR.** Objective.Monoenergetic high-energy Bragg peak (monoBP) proton therapy has emerged as promising candidates for conformal FLASH radiotherapy (FLASH-RT). However, the beam-specific proton modulation devices are needed for dose conformality.


??? note "Abstract"
    Objective.Monoenergetic high-energy Bragg peak (monoBP) proton therapy has emerged as promising candidates for conformal FLASH radiotherapy (FLASH-RT). However, the beam-specific proton modulation devices are needed for dose conformality. Meanwhile, the beam switching time could disrupt ultra-high dose rate (UHDR), thereby compromising the FLASH effect. This study aims to propose a novel monoBP conformal FLASH-RT methodology with the only utilization of universal range shifter (URS).Approach.An optimization algorithm, which optimized both URS thickness and dose distribution, was implemented based on multi-field optimization. Two proton FLASH techniques with 218 MeV proton beams were investigated for 10 brain and 10 lung cancer cases: (1) URS-modulated monoBP FLASH plan, and (2) transmission beam (TB) FLASH plan. All plans were optimized under the same optimization constraints with robust scenarios. Delivery parameters, dose, and dose rate metrics of the two plans were analyzed and compared.Main Results.Both modalities achieved similar dose coverage, withD98%of target meeting the clinical requirement for brain (BP: 98.2 ± 0.7%, TB: 98.6 ± 0.5%) and lung (BP: 97.8 ± 0.3%, TB: 98.7 ± 0.5%) cancer cases. However, compared to TB strategy, the BP FLASH plans reduced theDmeanof normal tissue for brain (BP: 16.6 ± 3.1 Gy, TB: 19.7 ± 5.4 Gy, p &lt; 0.05) and lung (BP: 3.3 ± 1.7 Gy, TB: 4.2 ± 1.8 Gy,p&lt; 0.05) cases. For dose-averaged dose rate, theV40Gy/s_DADRof both modalities reached 100% in brain and lung cancer cases; while for averaged dose rate, theV40Gy/s_ADRwas 37.4%and 26.6%for BP plans in brain and lung cancer cases, respectively, and was 61.5% and 61.3% for TB plans in brain and lung cancer cases, respectively.Significance.A monoBP conformal FLASH-RT methodology was proposed, utilizing only a fixed URS. The proposed monoBP FLASH-RT reached the requirement of FLASH effect, while demonstrating better dose protection, compared to the TB FLASH-RT.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/41125106/) · [DOI](https://doi.org/10.1088/1361-6560/ae1650)


---

### A methodology for optimizing treatment head angle arrangement for multi-angle FLASH intensity modulated radiation therapy platforms.

*Cui W, Guo C, Hu Z, Wang Y, Men K, Dai J* — Frontiers in oncology (2025)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span>


**TL;DR.** Flash therapy technology has been introduced, and several systems have been developed for its implementation. One such FLASH radiotherapy platform employs multiple treatment heads that deliver radiation to a target simultaneously.


??? note "Abstract"
    PURPOSE: Flash therapy technology has been introduced, and several systems have been developed for its implementation. One such FLASH radiotherapy platform employs multiple treatment heads that deliver radiation to a target simultaneously. However, the optimal number of treatment heads and their precise angular configuration needed to best meet clinical requirements remain to be determined. METHODS AND MATERIALS: In this study, each treatment head angle is treated as an independent variable, and the total angular discrepancy between a set of beam directions from clinically used plans and those generated by a virtual FLASH radiotherapy platform is defined as the objective function. This problem is solved using an optimization technique known as Adaptive Simulated Annealing (ASA). The performance of the proposed optimization model was evaluated using a dataset of 69,928 beams from 8,866 intensity-modulated radiation therapy (IMRT) plans collected over a two-year period in our department. These plans represent various types of common tumors, including nasopharyngeal, breast, esophageal, lung, and rectal cancers. The total angular discrepancy was compared between the beam directions obtained through the optimized treatment head arrangement and the directions used in clinical practice. RESULTS: For a virtual FLASH therapy platform equipped with five treatment heads, we obtained the optimized treatment head angle arrangements both with and without the constraint of an imaging system. Under the imaging system constraint, the optimized angles were 0°, 40.4°, 169.4°, 201.2°, and 239.8°, resulting in an average discrepancy of 38.9°compared to the beam directions used in the reference treatment plan cohort. Without the imaging system constraint, the optimized angles were 0°, 155.4°, 234.4°, 266.2°, and 304.8°, yielding an average discrepancy of 37.8°. In contrast, equally spaced treatment head angles produced an average discrepancy of 78.4°. CONCLUSION: A methodology for optimizing the treatment head angle arrangement for multi-angle FLASH radiotherapy platforms is proposed. The optimized configuration provides an effective solution for clinical applications, balancing performance with practical feasibility.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/41040529/) · [DOI](https://doi.org/10.3389/fonc.2025.1628281) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12483917/)


---

### Bragg-peak FLASH biological optimization enables enhanced normal tissue sparing and dose escalation for ocular stereotactic body radiation therapy.

*Hamza M, Selvaraj B, Cheng C, Zhao X, Kaulfers T, Lattery G et al.* — Physics in medicine and biology (2025)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Physics &amp; Dosimetry</span> <span class="badge tag">Modeling &amp; Mechanisms</span>


**TL;DR.** Objective.To evaluate proton Bragg peak FLASH for ocular treatments to enhance normal tissue sparing and enable dose escalation via FLASH biological optimization (FBO).Approach.The FLASH-sparing factors for normal tissues were derived from the literature in modeling the phenomenological FLASH normal tissue sparing effect. Using the single-energy BP-FLASH technique (SEBP-FLASH), an in-house treatme…


??? note "Abstract"
    Objective.To evaluate proton Bragg peak FLASH for ocular treatments to enhance normal tissue sparing and enable dose escalation via FLASH biological optimization (FBO).Approach.The FLASH-sparing factors for normal tissues were derived from the literature in modeling the phenomenological FLASH normal tissue sparing effect. Using the single-energy BP-FLASH technique (SEBP-FLASH), an in-house treatment planning system was implemented with the FLASH FBO module. Ten consecutive ocular patients who were treated using conventional dose rate intensity-modulated proton therapy (CONV-IMPT) to 50 Gy in 5 fractions were replanned using the FLASH technique. The dose metrics for the OARs were compared using the two different techniques. The fraction dose was then intentionally escalated from 10 to 12 Gy through FBO to assess whether the plans still met clinical constraints.Main results.In the FLASH regimen without FBO (50 Gy/5 fractions), all ipsilateral OAR dosimetric metrics met clinical objectives with safe margins. While the clinical CONV-IMPT approach demonstrated slightly better dosimetric performance than SEBP-FLASH plans, the incorporation of FBO improved all OAR dose metrics beyond those of CONV- IMPT, except for the mean dose to the cornea (no difference). When the target dose was increased from 50 to 60 Gy using FBO, all OARs remained within clinical limits. The mean and maximum doses to the cornea increased from 11.7 to 15.4 Gy and from 22.8 to 23.6 Gy, respectively, when transitioning from 50 Gy CONV-IMPT to 60 Gy FBO. However, in the 60 Gy FBO plans, the maximum doses were reduced for the eye (102.0%-87.0%), optic nerves (98.7%-74.0%), retina (100.5%-81.8%), lacrimal gland (84.9%-73.2%), and conjunctiva (91%-72.3%).Significance.SEBP-FLASH achieves plan quality comparable to CONV-IMPT using 50 Gy/5 fractions and enables dose escalation via FLASH FBO while meeting clinical standards, potentially improving tumor control with acceptable toxicity.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/41038240/) · [DOI](https://doi.org/10.1088/1361-6560/ae0ef7)


---

### An adaptive proton FLASH therapy using modularized pin ridge filter.

*Zafar AJ, Yang X, Diamond Z, Sibo T, Yu D, Patel PR et al.* — Medical physics (2025)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Physics &amp; Dosimetry</span> <span class="badge tag">Radiobiology</span>


**TL;DR.** In our previous study, we developed a modular pin ridge filter (pRF) design framework to streamline assembly, enabling the fast manufacture of custom filters optimized for single-energy proton FLASH planning. PURPOSE: In this paper, we propose a method to optimize adaptive proton FLASH therapy (ADP-FLASH) using modularized pRFs by recycling module pins from the initial plan while reducing pRF adju…


??? note "Abstract"
    BACKGROUND: In our previous study, we developed a modular pin ridge filter (pRF) design framework to streamline assembly, enabling the fast manufacture of custom filters optimized for single-energy proton FLASH planning. PURPOSE: In this paper, we propose a method to optimize adaptive proton FLASH therapy (ADP-FLASH) using modularized pRFs by recycling module pins from the initial plan while reducing pRF adjustments in adaptive FLASH planning. METHODS: Initially, single energy (250 MeV) FLASH-pRF plans were created using pencil beam directions (PBDs) from initial IMPT plans on the planning CT (pCT). PBDs are classified as new/changed (ΔE &gt; 5 MeV) or unchanged by comparing spot maps for targets between pCT and re-CT. We used an iterative least-square regression model to identify recyclable PBDs with minimal relative changes to spot MU weighting. Two PBDs with the least square error were retrieved per iteration and added to the background plan, and the remaining PBDs were reoptimized for the adaptive plan in subsequent iterations. The method was validated on three liver SBRT cases (50 Gy in five fractions) by comparing various dosimetric parameters across initial pRF plans on pCT, re-CT, and the ADP-FLASH-pRF plans on re-CT. RESULTS: V100 for initial-pRF plans on pCT, re-CT, and ADP-FLASH-pRF plans for the three cases were as follows: (93.7%, 89.2%, 91.4%), (93.5%, 60.2%, 91.7%), and (97.3%, 69.9%, 98.8%). We observe a decline in plan quality when applying the initial pRF to the re-CT, whereas the ADP-FLASH-pRF approach restores quality comparable to the initial pRF on the pCT. FLASH effect of the initial pRF and ADP pRF plans were evaluated with a dose and dose rate threshold of 1 and 40 Gy/s, respectively, using the FLASH effectiveness model. The proposed method recycled 91.2%, 71%, and 64.7% of PBDs from initial pRF plans for the three cases while maintaining all clinical goals and preserving FLASH effects. CONCLUSION: This study validated a method for recycling the pRFs in single-energy proton FLASH planning for SBRT cases. This framework offers a scalable solution for adaptive proton therapy, balancing clinical effectiveness and practicality.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/40940290/) · [DOI](https://doi.org/10.1002/mp.18109)


---

### FLASH-enabled proton SBRT for a challenging case of spine metastasis.

*Wuyckens S, Vera MC, Nilsson R, Wase V, Di Perri D, Geets X et al.* — Physics in medicine and biology (2025)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Clinical &amp; Translational</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Beam Delivery &amp; Technology</span>


**TL;DR.** Objective. The FLASH effect, characterized by potential sparing of organs at risk (OARs) through ultra-high dose rate (DR) irradiation, has garnered significant attention for its capability to address indications previously untreatable at conventional DRs with hypofractionated schemes.


??? note "Abstract"
    Objective. The FLASH effect, characterized by potential sparing of organs at risk (OARs) through ultra-high dose rate (DR) irradiation, has garnered significant attention for its capability to address indications previously untreatable at conventional DRs with hypofractionated schemes. While considerable biological research is needed to understand the FLASH effect and determine the FLASH modifying factors (FMF) for individual OARs, treatment planning studies have also emerged. This study evaluates the feasibility of achieving FLASH conditions in proton stereotactic body radiotherapy for spine metastases and establishes the required FMFs under different fractionation regimens.Approach. A conformal FLASH Proton SBRT plan was generated for a patient with spine metastasis in a research version of RayStation11B (RaySearch laboratories AB, Stockholm) on an IBA Proteus Plus system. Two oblique posterior beams were used in the plan. The prescribed dose to the CTV was set according to 3 different fractionation regimens: 5 fractions (fx) of 7 Gy, 8 fx of 5 Gy, and 10 fx of 4.2 Gy. Spot filtering and sorting techniques were applied to maximize the 5% pencil beam scanning DR in the spinal cord (SC). The FLASH effect was assumed to be observed within irradiated regions above 40 Gy s-1and 4 Gy per fraction.Main results. The generated plans successfully ensure robust target coverage in each fraction. The volume of SC that does not comply with the clinical goal adheres to the FLASH effect conditions in each fraction. Depending on the aforementioned fractionation schemes used, a FMF of approximately 0.6 to 0.8 is necessary to enable such treatment in FLASH conditions.Significance. This study indicates that treating challenging spine metastases with protons using FLASH delivery is technically feasible. However, clinical viability depends on optimistic parameters to trigger the FLASH effect and FMF values below 0.8, which are not yet guaranteed given current research.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/40897368/) · [DOI](https://doi.org/10.1088/1361-6560/ae023c)


---

### FLASH Stereotactic Body Radiation Therapy for Spine Tumors Using a Single-Energy Proton Pristine Bragg Peak Delivery Technique.

*Selvaraj B, Zhao X, Lin H, Shen J, Cheng C, Bookbinder A et al.* — Advances in radiation oncology (2025)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Physics &amp; Dosimetry</span>


**TL;DR.** To investigate the dosimetric performance and dose rate of Bragg peak FLASH (BP-FLASH) for spinal cord stereotactic body radiation therapy (SBRT). METHODS AND MATERIALS: Ten consecutive patients with spinal tumors treated with conventional intensity modulated proton therapy (CONV-IMPT) SBRT (40 Gy in 5 fractions) were selected for this study.


??? note "Abstract"
    PURPOSE: To investigate the dosimetric performance and dose rate of Bragg peak FLASH (BP-FLASH) for spinal cord stereotactic body radiation therapy (SBRT). METHODS AND MATERIALS: Ten consecutive patients with spinal tumors treated with conventional intensity modulated proton therapy (CONV-IMPT) SBRT (40 Gy in 5 fractions) were selected for this study. These patients were reoptimized using an in-house FLASH algorithm and a single-energy Bragg peak approach. The dose distributions and dose metrics for target coverage and critical organs-at-risk (OARs) were compared. BP-FLASH plans dose rates were calculated using an average-dose-rate. The FLASH ratios (V40Gy/s) were assessed with dose thresholds at 0.2, 2, and 5 Gy. The doses and dose rates for the 10 patients were averaged, and a t test was performed comparing CONV-IMPT and BP-FLASH. RESULTS: Dosimetric analysis revealed that the BP-FLASH plans deliver a similar dose as CONV-IMPT plans to critical OARs. However, in BP-FLASH, the clinical target volume received a higher maximum dose than CONV-IMPT (115.1% versus 108.9%, P = .001). No notable differences were observed in the maximum doses to the spinal cord (P = .122) or esophagus (P = .327). FLASH dose rates for all the OARs exceeded 80% with 2 Gy dose threshold. When increased to 5 Gy, V40Gy/s increased to &gt;95% for composite plan doses. CONCLUSIONS: BP-FLASH SBRT is a promising treatment for challenging spinal cord cancers, which achieved ultra-high-dose rates for FLASH effect and maintained the same dosimetry quality as the CONV-IMPT plans.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/40416512/) · [DOI](https://doi.org/10.1016/j.adro.2025.101776) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12098142/)


---

### Implementation of a novel pencil beam scanning Bragg peak FLASH technique to a commercial treatment planning system.

*Bookbinder A, Krieger M, Lansonneur P, Magliari A, Zhao X, Choi JI et al.* — Medical physics (2025)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Beam Delivery &amp; Technology</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Physics &amp; Dosimetry</span>


**TL;DR.** Ultra-high dose rate, or FLASH, radiotherapy has shown promise in preclinical experiments of sparing healthy tissue without compromising tumor control. This &quot;FLASH effect&quot; can compound with dosimetric sparing of the proton Bragg peak (BP) using a method called Single Energy Pristine Bragg Peak (SEPBP) FLASH.


??? note "Abstract"
    BACKGROUND: Ultra-high dose rate, or FLASH, radiotherapy has shown promise in preclinical experiments of sparing healthy tissue without compromising tumor control. This &quot;FLASH effect&quot; can compound with dosimetric sparing of the proton Bragg peak (BP) using a method called Single Energy Pristine Bragg Peak (SEPBP) FLASH. However, this and other proposed FLASH techniques are constrained by lack of familiar treatment planning systems (TPSs). Creating modules to implement SEPBP FLASH into a commercial TPS opens up the possibility of more widespread investigation of FLASH and lays the groundwork for future clinical translation. PURPOSE: To implement, investigate, and benchmark the capacity of a commercial TPS research extension for BP FLASH SBRT treatment planning by studying the dosimetric properties and FLASH ratio for critical organs-at-risk (OARs) at several sites. METHODS: A 250 MeV clinical proton beam model was commissioned in the Eclipse TPS (Varian Medical Systems, Palo Alto, USA). BP FLASH fields were single-layer maximum-energy beams with a universal range shifter (URS) and field-specific range compensators (RCs). RCs for each beam angle were included as contours within the structure set, while the URS was modeled in the PBS beamline. Spotmaps were created using Lloyd&#x27;s algorithm with minimum monitor units (MU)-based spacing to ensure plan quality and preserve FLASH coverage for critical OARs. Inverse optimization while preserving minimum MU constraints was done with scorecard-based optimization. Fifteen SBRT cases from three anatomical sites (liver, lung, base-of-skull \[BOS\]) previously treated at the New York Proton Center were re-optimized using this method, and dosimetric characteristics of BP plans were compared to clinically treated plans. FLASH ratios for critical OARs were evaluated for BP FLASH plans. RESULTS: The dose distributions, including target uniformity, conformity index (CI), and DVHs, showed no significant difference in clinically-used metrics between BP FLASH and clinically delivered plans across all anatomical sites. Mean 40 Gy/s FLASH ratios for critical OARs were above 84% for all but one OAR with 2 Gy threshold and above 98% for all OARs with 5 Gy threshold. Dmax for liver and BOS cases was 111.3 ± 2.68 and 112.88 ± 1.29, respectively, and D2% for lung cases was 112.04 ± 1.09. All Dmax remained below 115%. CONCLUSIONS: Inverse planning using a single-energy BP FLASH technique based on sparse spots and ultra-high minimum MU/spot can achieve intensity-modulated proton therapy (IMPT)-equivalent quality and sufficient FLASH coverage. This successful prototype brings us closer to commercial implementation and may increase the availability of proton FLASH dosimetry studies.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/40344192/) · [DOI](https://doi.org/10.1002/mp.17876) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12257904/)


---

### Fast spot order optimization to increase dose rates in scanned particle therapy FLASH treatments.

*Wase V, Widenfalk O, Nilsson R, Fälth C, Fredriksson A* — Physics in medicine and biology (2025)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Clinical &amp; Translational</span> <span class="badge tag">Radiobiology</span>


**TL;DR.** The advent of ultra-high dose rate irradiation, known as FLASH radiation therapy, has shown promising potential in reducing toxicity while maintaining tumor control. However, the clinical translation of these benefits necessitates efficient treatment planning strategies.


??? note "Abstract"
    The advent of ultra-high dose rate irradiation, known as FLASH radiation therapy, has shown promising potential in reducing toxicity while maintaining tumor control. However, the clinical translation of these benefits necessitates efficient treatment planning strategies. This study introduces a novel approach to optimize proton therapy for FLASH effects using traveling salesperson problem (TSP) heuristics. We applied these heuristics to optimize the arrangement of proton spots in treatment plans for 26 prostate cancer patients, comparing the performance against conventional sorting methods and global optimization techniques. Our results demonstrate that TSP-based heuristics significantly enhance FLASH coverage to the same extent as the global optimization technique, but with computation times reduced from hours to a few seconds. This approach offers a practical and scalable solution for enhancing the effectiveness of FLASH therapy, paving the way for more effective and personalized cancer treatments. Future work will focus on further optimizing run times and validating these methods in clinical settings.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/39774312/) · [DOI](https://doi.org/10.1088/1361-6560/ada715)


---

### The Radiosurgery Society Working Groups on GRID, LATTICE, Microbeam, and FLASH Radiotherapies: Advancements Symposium and Subsequent Progress Made.

*Snider JW, Mayr NA, Molitoris J, Chhabra AM, Mossahebi S, Griffin R et al.* — Practical radiation oncology (2025)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Clinical &amp; Translational</span> <span class="badge tag">Radiobiology</span>


**TL;DR.** Since the inaugural workshop &quot;Understanding High-Dose, Ultra-High Dose Rate and Spatially Fractionated Radiotherapy.&quot; hosted by the National Cancer Institute and sponsored by the Radiosurgery Society (RSS), growing collaborations and investigations have ensued among experts, practitioners, and researchers. The RSS GRID, LATTICE, Microbeam and FLASH (GLMF) Working Groups were formed as a framework …


??? note "Abstract"
    PURPOSE: Since the inaugural workshop &quot;Understanding High-Dose, Ultra-High Dose Rate and Spatially Fractionated Radiotherapy.&quot; hosted by the National Cancer Institute and sponsored by the Radiosurgery Society (RSS), growing collaborations and investigations have ensued among experts, practitioners, and researchers. The RSS GRID, LATTICE, Microbeam and FLASH (GLMF) Working Groups were formed as a framework for these efforts and have focused on advancing the understanding of the biology, technical/physical parameters, trial design, and clinical practice of these new radiation therapy modalities. METHODS AND MATERIALS: In view of the steadily increasing clinical interest in Spatially Fractionated Radiotherapy (SFRT) and FLASH, a full-day symposium entitled &quot;Advancements in GRID, LATTICE, and FLASH Radiotherapy Symposium&quot; was established in 2022 that immediately preceded the RSS scientific meeting. This well-attended symposium focused on clinical, technical, and physics approaches for SFRT, and closely examining relevant radiobiological underpinnings. Practical clinical trial development was a highlighted discussion. An additional section reviewed proton therapy and other particle-based techniques for the delivery of GRID and LATTICE therapy. A treatment planning and delivery tutorial for GRID, LATTICE, and proton GRID/LATTICE was directed toward the real-world considerations for the development of new clinical GRID or LATTICE programs. An overall similar approach was applied to the discussion of FLASH. This report summarizes the content of the first GLMF Symposium and related work of the RSS GLMF Working Groups in the field of heterogeneous and ultrahigh dose rate irradiation, over approximately 2 years. RESULTS: The GLMF Working Groups have continued to expand in membership and attendance, and several resultant trial concepts, research efforts, academic discussions, and peer-reviewed publications have followed as the number of institutions and practitioners using SFRT and FLASH continues to grow. CONCLUSIONS: The GLMF Working Groups and the RSS continue to demonstrate excellent progress in proliferating use of and improving understanding of SFRT and ultrahigh dose rate radiation therapy techniques.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/39447865/) · [DOI](https://doi.org/10.1016/j.prro.2024.09.015) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12128894/)


---

### Hybrid ultra-high and conventional dose rate treatments with electrons and photons for the clinical transfer of FLASH-RT to deep-seated targets: A treatment planning study.

*Böhlen TT, Zeverino M, Germond JF, Kinj R, Schiappacasse L, Bochud F et al.* — Radiotherapy and oncology : journal of the European Society for Therapeutic Radiology and Oncology (2024)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Physics &amp; Dosimetry</span> <span class="badge tag">Clinical &amp; Translational</span> <span class="badge tag">Radiobiology</span>


**TL;DR.** This study explores the dosimetric feasibility and plan quality of hybrid ultra-high dose rate (UHDR) electron and conventional dose rate (CDR) photon (HUC) radiotherapy for treating deep-seated tumours with FLASH-RT. METHODS: HUC treatment planning was conducted optimizing a broad UHDR electron beam (between 20-250 MeV) combined with a CDR VMAT for a glioblastoma, a pancreatic cancer, and a prost…


??? note "Abstract"
    PURPOSE: This study explores the dosimetric feasibility and plan quality of hybrid ultra-high dose rate (UHDR) electron and conventional dose rate (CDR) photon (HUC) radiotherapy for treating deep-seated tumours with FLASH-RT. METHODS: HUC treatment planning was conducted optimizing a broad UHDR electron beam (between 20-250 MeV) combined with a CDR VMAT for a glioblastoma, a pancreatic cancer, and a prostate cancer case. HUC plans were based on clinical prescription and fractionation schemes and compared against clinically delivered plans. Considering a HUC boost treatment for the glioblastoma consisting of a 15-Gy-single-fraction UHDR electron boost supplemented with VMAT, two scenarios for FLASH sparing were assessed using FLASH-modifying-factor-weighted doses. RESULTS: For all three patient cases, HUC treatment plans demonstrated comparable dosimetric quality to clinical plans, with similar PTV coverage (V95% within 0.5 %), homogeneity, and critical OAR-sparing. At the same time, HUC plans delivered a substantial portion of the dose to the PTV (Dmedian of 50-69 %) and surrounding tissues at UHDR. For the HUC boost treatment of the glioblastoma, the first FLASH sparing scenario showed a moderate FLASH sparing magnitude (10 % for D2%,PTV) for the 15-Gy UHDR electron boost, while the second scenario indicated a more substantial sparing of brain tissues inside and outside the PTV (32 % for D2%,PTV, 31 % for D2%,Brain). CONCLUSIONS: From a planning perspective, HUC treatments represent a feasible approach for delivering dosimetrically conformal UHDR treatments, potentially mitigating technical challenges associated with delivering conformal FLASH-RT for deep-seated tumours. While further research is needed to optimize HUC fractionation and delivery schemes for specific patient cohorts, HUC treatments offer a promising avenue for the clinical transfer of FLASH-RT.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/39395673/) · [DOI](https://doi.org/10.1016/j.radonc.2024.110576)


---

### A Novel Dose Rate Optimization Method to Maximize Ultrahigh-Dose-Rate Coverage of Critical Organs at Risk Without Compromising Dosimetry Metrics in Proton Pencil Beam Scanning FLASH Radiation Therapy.

*Zhao X, Huang S, Lin H, Choi JI, Zhu K, Simone CB et al.* — International journal of radiation oncology, biology, physics (2024)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Beam Delivery &amp; Technology</span> <span class="badge tag">Physics &amp; Dosimetry</span> <span class="badge tag">Radiobiology</span>


**TL;DR.** This study aimed to investigate a dose rate optimization framework based on the spot-scanning patterns to improve ultrahigh-dose-rate coverage of critical organs at risk (OARs) for proton pencil beam scanning (PBS) FLASH radiation therapy (ultrahigh dose-rate (often referred to as &gt;40 Gy per second) delivery) and present implementation of a genetic algorithm (GA) method for spot sequence optimizat…


??? note "Abstract"
    PURPOSE: This study aimed to investigate a dose rate optimization framework based on the spot-scanning patterns to improve ultrahigh-dose-rate coverage of critical organs at risk (OARs) for proton pencil beam scanning (PBS) FLASH radiation therapy (ultrahigh dose-rate (often referred to as &gt;40 Gy per second) delivery) and present implementation of a genetic algorithm (GA) method for spot sequence optimization to achieve PBS FLASH dose rate optimization under relatively low nozzle beam currents. METHODS AND MATERIALS: First, a multifield FLASH plan was developed to meet all the dosimetric goals and optimal FLASH dose rate coverage by considering the deliverable minimum monitor unit constraint. Then, a GA method was implemented into the in-house treatment platform to maximize the dose rate by exploring the best spot delivery sequence. A phantom study was performed to evaluate the effectiveness of the dose rate optimization. Then, 10 consecutive plans for patients with lung cancer previously treated using PBS intensity-modulated proton therapy were optimized using 45 GyRBE in 3 fractions for both transmission and Bragg peak FLASH radiation therapy for further validation. The spot delivery sequence of each treatment field was optimized using this GA. The ultrahigh-dose-rate-volume histogram and dose rate coverage V40GyRBE/s were investigated to assess the efficacy of dose rate optimization quantitatively. RESULTS: Using a relatively low monitor unit/spot of 150, corresponding to a nozzle beam current of 65 nA, the FLASH dose rate ratio V40GyRBE/s of the OAR contour of the core was increased from 0% to ∼60% in the phantom study. In the patients with lung cancer, the ultrahigh-dose-rate coverage V40GyRBE/s was improved from 15.2%, 15.5%, 17.6%, and 16.0% before the delivery sequence optimization to 31.8%, 43.5%, 47.6%, and 30.5% after delivery sequence optimization in the lungs-GTV (gross tumor volume), spinal cord, esophagus, and heart (for all, P &lt; .001). When the beam current increased to 130 nA, V40GyRBE/s was improved from 45.1%, 47.1%, 51.2%, and 51.4% to 65.3%, 83.5%, 88.1%, and 69.4% (P &lt; .05). The averaged V40GyRBE/s for the target and OARs increased from 12.9% to 41.6% and 46.3% to 77.5% for 65 and 130 nA, respectively, showing significant improvements based on a clinical proton system. After optimizing the dose rate for the Bragg peak FLASH technique with a beam current of 340 nA, the V40GyRBE/s values for the lung GTV, spinal cord, esophagus, and heart were increased by 8.9%, 15.8%, 22%, and 20.8%, respectively. CONCLUSIONS: An optimal plan quality can be maintained as the spot delivery sequence optimization is a separate independent process after the plan optimization. Both the phantom and patient results demonstrated that novel spot delivery sequence optimization can effectively improve the ultrahigh-dose-rate coverage for critical OARs, which can potentially be applied in clinical practice for better OARs-sparing efficacy.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/38879087/) · [DOI](https://doi.org/10.1016/j.ijrobp.2024.06.002)


---

### Simultaneous dose and dose rate optimization via dose modifying factor modeling for FLASH effective dose.

*Ma J, Lin Y, Tang M, Zhu YN, Gan GN, Rotondo RL et al.* — Medical physics (2024)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Modeling &amp; Mechanisms</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Beam Delivery &amp; Technology</span>


**TL;DR.** Although the FLASH radiotherapy (FLASH) can improve the sparing of organs-at-risk (OAR) via the FLASH effect, it is generally a tradeoff between the physical dose coverage and the biological FLASH coverage, for which the concept of FLASH effective dose (FED) is needed to quantify the net improvement of FLASH, compared to the conventional radiotherapy (CONV). PURPOSE: This work will develop the fir…


??? note "Abstract"
    BACKGROUND: Although the FLASH radiotherapy (FLASH) can improve the sparing of organs-at-risk (OAR) via the FLASH effect, it is generally a tradeoff between the physical dose coverage and the biological FLASH coverage, for which the concept of FLASH effective dose (FED) is needed to quantify the net improvement of FLASH, compared to the conventional radiotherapy (CONV). PURPOSE: This work will develop the first-of-its-kind treatment planning method called simultaneous dose and dose rate optimization via dose modifying factor modeling (SDDRO-DMF) for proton FLASH that directly optimizes FED. METHODS: SDDRO-DMF models and optimizes FED using FLASH dose modifying factor (DMF) models, which can be classified into two categories: (1) the phenomenological model of the FLASH effect, such as the FLASH effectiveness model (FEM); (2) the mechanistic model of the FLASH radiobiology, such as the radiolytic oxygen depletion (ROD) model. The general framework of SDDRO-DMF will be developed, with specific DMF models using FEM and ROD, as a demonstration of general applicability of SDDRO-DMF for proton FLASH via transmission beams (TB) or Bragg peaks (BP) with single-field or multi-field irradiation. The FLASH dose rate is modeled as pencil beam scanning dose rate. The solution algorithm for solving the inverse optimization problem of SDDRO-DMF is based on iterative convex relaxation method. RESULTS: SDDRO-DMF is validated in comparison with IMPT and a state-of-the-art method called SDDRO, with demonstrated efficacy and improvement for reducing the high dose and the high-dose volume for OAR in terms of FED. For example, in a SBRT lung case of the dose-limiting factor that the max dose of brachial plexus should be no more than 26 Gy, only SDDRO-DMF met this max dose constraint; moreover, SDDRO-DMF completely eliminated the high-dose (V70%) volume to zero for CTV10mm (a high-dose region as a 10 mm ring expansion of CTV). CONCLUSION: We have proposed a new proton FLASH optimization method called SDDRO-DMF that directly optimizes FED using phenomenological or mechanistic models of DMF, and have demonstrated the efficacy of SDDO-DMF in reducing the high-dose volume or/and the high-dose value for OAR, compared to IMPT and a state-of-the-art method SDDRO.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/38873848/) · [DOI](https://doi.org/10.1002/mp.17251) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11783338/)


---

### Technical note: Dosimetry and FLASH potential of UHDR proton PBS for small lung tumors: Bragg-peak-based delivery versus transmission beam and IMPT.

*van Marlen P, van de Water S, Slotman BJ, Dahele M, Verbakel W* — Medical physics (2024)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Physics &amp; Dosimetry</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Beam Delivery &amp; Technology</span>


**TL;DR.** High-energy transmission beams (TBs) are currently the main delivery method for proton pencil beam scanning ultrahigh dose-rate (UHDR) FLASH radiotherapy. TBs place the Bragg-peaks behind the target, outside the patient, making delivery practical and achievement of high dose-rates more likely.


??? note "Abstract"
    BACKGROUND: High-energy transmission beams (TBs) are currently the main delivery method for proton pencil beam scanning ultrahigh dose-rate (UHDR) FLASH radiotherapy. TBs place the Bragg-peaks behind the target, outside the patient, making delivery practical and achievement of high dose-rates more likely. However, they lead to higher integral dose compared to conventional intensity-modulated proton therapy (IMPT), in which Bragg-peaks are placed within the tumor. It is hypothesized that, when energy changes are not required and high beam currents are possible, Bragg-peak-based beams can not only achieve more conformal dose distributions than TBs, but also have more FLASH-potential. PURPOSE: This works aims to verify this hypothesis by taking three different Bragg-peak-based delivery techniques and comparing them with TB and IMPT-plans in terms of dosimetry and FLASH-potential for single-fraction lung stereotactic body radiotherapy (SBRT). METHODS: For a peripherally located lung target of various sizes, five different proton plans were made using &quot;matRad&quot; and inhouse-developed algorithms for spot/energy-layer/beam reduction and minimum monitor unit maximization: (1) IMPT-plan, reference for dosimetry, (2) TB-plan, reference for FLASH-amount, (3) pristine Bragg-peak plan (non-depth-modulated Bragg-peaks), (4) Bragg-peak plan using generic ridge filter, and (5) Bragg-peak plan using 3D range-modulated ridge filter. RESULTS: Bragg-peak-based plans are able to achieve sufficient plan quality and high dose-rates. IMPT-plans resulted in lowest OAR-dose and integral dose (also after a FLASH sparing-effect of 30%) compared to both TB-plans and Bragg-peak-based plans. Bragg-peak-based plans vary only slightly between themselves and generally achieve lower integral dose than TB-plans. However, TB-plans nearly always resulted in lower mean lung dose than Bragg-peak-based plans and due to a higher amount of FLASH-dose for TB-plans, this difference increased after including a FLASH sparing-effect. CONCLUSION: This work indicates that there is no benefit in using Bragg-peak-based beams instead of TBs for peripherally located, UHDR stereotactic lung radiotherapy, if lung dose is the priority.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/38795376/) · [DOI](https://doi.org/10.1002/mp.17185)


---

### Combined optimization of spot positions and weights for better FLASH proton therapy.

*Lansonneur P, Magliari A, Rosa L, Perez J, Niemelä P, Folkerts M* — Physics in medicine and biology (2024)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Physics &amp; Dosimetry</span>


**TL;DR.** Objective.In Intensity Modulated Proton Therapy (IMPT), the weights of individual pencil-beams or spots are optimized to fulfil dosimetric constraints. Theses spots are usually located on a regular lattice and their positions are fixed during optimization.


??? note "Abstract"
    Objective.In Intensity Modulated Proton Therapy (IMPT), the weights of individual pencil-beams or spots are optimized to fulfil dosimetric constraints. Theses spots are usually located on a regular lattice and their positions are fixed during optimization. In many cases, the range of spot weights may however be limited, leading sometimes to sub-optimal plan quality. An emblematic use case is the delivery of a plan at ultra-high dose rate (FLASH-RT), for which the spot weights are typically constrained to high values.Approach. To improve further the quality of IMPT FLASH plans, we propose here a novel algorithm to optimize both the spot weights and positions directly based on the objectives defined by the treatment planner.Main results. For all cases considered, optimizing the spot positions lead to an enhanced dosimetric score, while maintaining a high dose rate.Significance. Overall, this approach resulted in a substantial plan quality improvement compared to optimizing only the spot weights, and in a similar execution time.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/38749462/) · [DOI](https://doi.org/10.1088/1361-6560/ad4c53)


---

### Feasibility and constraints of Bragg peak FLASH proton therapy treatment planning.

*Lövgren N, Fagerström Kristensen I, Petersson K* — Frontiers in oncology (2024)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Clinical &amp; Translational</span> <span class="badge tag">Beam Delivery &amp; Technology</span>


**TL;DR.** FLASH proton therapy (FLASH-PT) requires ultra-high dose rate (≥ 40 Gy/s) protons to be delivered in a short timescale whilst conforming to a patient-specific target. This study investigates the feasibility and constraints of Bragg peak FLASH-PT treatment planning, and compares the in silico results produced to plans for intensity modulated proton therapy (IMPT).


??? note "Abstract"
    INTRODUCTION: FLASH proton therapy (FLASH-PT) requires ultra-high dose rate (≥ 40 Gy/s) protons to be delivered in a short timescale whilst conforming to a patient-specific target. This study investigates the feasibility and constraints of Bragg peak FLASH-PT treatment planning, and compares the in silico results produced to plans for intensity modulated proton therapy (IMPT). MATERIALS AND METHOD: Bragg peak FLASH-PT and IMPT treatment plans were generated for bone (n=3), brain (n=3), and lung (n=4) targets using the MIROpt research treatment planning system and the Conformal FLASH library developed by Applications SA from the open-source version of UCLouvain. FLASH-PT beams were simulated using monoenergetic spot-scanned protons traversing through a conformal energy modulator, a range shifter, and an aperture. A dose rate constraint of ≥ 40 Gy/s was included in each FLASH-PT plan optimisation. RESULTS: Space limitations in the FLASH-PT adapted beam nozzle imposed a maximum target width constraint, excluding 4 cases from the study. FLASH-PT plans did not satisfy the imposed target dose constraints (D95% ≥ 95% and D2%≤ 105%) but achieved clinically acceptable doses to organs at risk (OARs). IMPT plans adhered to all target and OAR dose constraints. FLASH-PT plans showed a reduction in both target homogeneity (p &lt; 0.001) and dose conformity (non-significant) compared to IMPT. CONCLUSION: Without accounting for a sparing effect, IMPT plans were superior in target coverage, dose conformity, target homogeneity, and OAR sparing compared to FLASH-PT. Further research is warranted in treatment planning optimisation and beam delivery for clinical implementation of Bragg peak FLASH-PT.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/38737902/) · [DOI](https://doi.org/10.3389/fonc.2024.1369065) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11082391/)


---

### Imaging and characterization of optical emission fromex vivotissue during conventional and UHDR PBS proton therapy.

*Vasyltsiv R, Rahman M, Harms J, Clark M, Gladstone DJ, Pogue BW et al.* — Physics in medicine and biology (2024)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Beam Delivery &amp; Technology</span>


**TL;DR.** Objective. Imaging of optical photons emitted from tissue during radiotherapy is a promising technique for real-time visualization of treatment delivery, offering applications in dose verification, treatment monitoring, and retrospective treatment plan comparison.


??? note "Abstract"
    Objective. Imaging of optical photons emitted from tissue during radiotherapy is a promising technique for real-time visualization of treatment delivery, offering applications in dose verification, treatment monitoring, and retrospective treatment plan comparison. This research aims to explore the feasibility of intensified imaging of tissue luminescence during proton therapy (PT), under both conventional and ultra-high dose rate (UHDR) conditions.Approach. Conventional and UHDR pencil beam scanning (PBS) PT irradiation of freshex vivoporcine tissue and tissue-mimicking plastic phantom was imaged using intensified complementary metal-oxide-semiconductor(CMOS) cameras. The optical emission from tissue was characterized during conventional irradiation using both blue and red-sensitive intensifiers to ensure adequate spectral coverage. Spectral characterization was performed using bandpass filters between the lens and sensor. Imaging of conventional proton fields (240 MeV, 10 nA) was performed at 100 Hz frame rate, while UHDR PBS proton delivery (250 MeV, 99 nA) was recorded at 1 kHz frame rate. Dependence of optical emission yield on proton energy was studied using an optical tissue-mimicking plastic phantom and a range shifter. Finally, we demonstrated fast beam tracking capability of fast camera towardsin vivomonitoring of FLASH PT.Main results. Under conventional treatment dose rates optical emission was imaged with single spot resolution. Spot profiles were found to agree with the treatment planning system calculation within &gt;90% for all spectral bands and spot intensity was found to vary with spectral filtration. The resultant polychromatic emission presented a maximum intensity at 650 nm and decreasing signal at lower wavelengths, which is consistent with expected attenuation patterns of high fat and muscle tissue. For UHDR beam imaging, optical yield increased with higher proton energy. Imaging at 1 kHz allowed continuous monitoring of delivery during porcine tissue irradiation, with clear identification of individual dwell positions. The number of dwell positions matched the treatment plan in total and per row showing adequate temporal capability of iCMOS imaging.Significance. For the first time, this study characterizes optical emission from tissue during PT and demonstrates our capability of fast optical tracking of pencil proton beam on the tissue anatomy in both conventional and UHDR setting. Similar to the Cherenkov imaging in radiotherapy, this imaging modality could enable a seamless, independent validation of PT treatments.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/38422545/) · [DOI](https://doi.org/10.1088/1361-6560/ad2ee6) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10945384/)


---

### Pencil Beam Scanning Proton Bragg Peak Conformal FLASH in Prostate Cancer Stereotactic Body Radiotherapy.

*Kaulfers T, Lattery G, Cheng C, Zhao X, Selvaraj B, Wu H et al.* — Cancers (2024)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Physics &amp; Dosimetry</span> <span class="badge tag">Beam Delivery &amp; Technology</span>


**TL;DR.** Bragg peak FLASH radiotherapy (RT) uses a distal tracking method to eliminate exit doses and can achieve superior OAR sparing. This study explores the application of this novel method in stereotactic body radiotherapy prostate FLASH-RT.


??? note "Abstract"
    Bragg peak FLASH radiotherapy (RT) uses a distal tracking method to eliminate exit doses and can achieve superior OAR sparing. This study explores the application of this novel method in stereotactic body radiotherapy prostate FLASH-RT. An in-house platform was developed to enable intensity-modulated proton therapy (IMPT) planning using a single-energy Bragg peak distal tracking method. The patients involved in the study were previously treated with proton stereotactic body radiotherapy (SBRT) using the pencil beam scanning (PBS) technique to 40 Gy in five fractions. FLASH plans were optimized using a four-beam arrangement to generate a dose distribution similar to the conventional opposing beams. All of the beams had a small angle of two degrees from the lateral direction to increase the dosimetry quality. Dose metrics were compared between the conventional PBS and the Bragg peak FLASH plans. The dose rate histogram (DRVH) and FLASH metrics of 40 Gy/s coverage (V40Gy/s) were investigated for the Bragg peak plans. There was no significant difference between the clinical and Bragg peak plans in rectum, bladder, femur heads, large bowel, and penile bulb dose metrics, except for Dmax. For the CTV, the FLASH plans resulted in a higher Dmax than the clinical plans (116.9% vs. 103.3%). For the rectum, the V40Gy/s reached 94% and 93% for 1 Gy dose thresholds in composite and single-field evaluations, respectively. Additionally, the FLASH ratio reached close to 100% after the application of the 5 Gy threshold in composite dose rate assessment. In conclusion, the Bragg peak distal tracking method can yield comparable plan quality in most OARs while preserving sufficient FLASH dose rate coverage, demonstrating that the ultra-high dose technique can be applied in prostate FLASH SBRT.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/38398188/) · [DOI](https://doi.org/10.3390/cancers16040798) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10886659/)


---

### A Novel Inverse Algorithm To Solve the Integrated Optimization of Dose, Dose Rate, and Linear Energy Transfer of Proton FLASH Therapy With Sparse Filters.

*Harrison N, Kang M, Liu R, Charyyev S, Wahl N, Liu W et al.* — International journal of radiation oncology, biology, physics (2024)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Beam Delivery &amp; Technology</span> <span class="badge tag">Modeling &amp; Mechanisms</span>


**TL;DR.** The recently proposed Integrated Physical Optimization Intensity Modulated Proton Therapy (IPO-IMPT) framework allows simultaneous optimization of dose, dose rate, and linear energy transfer (LET) for ultra-high dose rate (FLASH) treatment planning. Finding solutions to IPO-IMPT is difficult because of computational intensiveness.


??? note "Abstract"
    PURPOSE: The recently proposed Integrated Physical Optimization Intensity Modulated Proton Therapy (IPO-IMPT) framework allows simultaneous optimization of dose, dose rate, and linear energy transfer (LET) for ultra-high dose rate (FLASH) treatment planning. Finding solutions to IPO-IMPT is difficult because of computational intensiveness. Nevertheless, an inverse solution that simultaneously specifies the geometry of a sparse filter and weights of a proton intensity map is desirable for both clinical and preclinical applications. Such solutions can reduce effective biologic dose to organs at risk in patients with cancer as well as reduce the number of animal irradiations needed to derive extra biologic dose models in preclinical studies. METHODS AND MATERIALS: Unlike the initial forward heuristic, this inverse IPO-IMPT solution includes simultaneous optimization of sparse range compensation, sparse range modulation, and spot intensity. The daunting computational tasks vital to this endeavor were resolved iteratively with a distributed computing framework to enable Simultaneous Intensity and Energy Modulation and Compensation (SIEMAC). SIEMAC was demonstrated on a human patient with central lung cancer and a minipig. RESULTS: SIEMAC simultaneously improves maps of spot intensities and patient-field-specific sparse range compensators and range modulators. For the patient with lung cancer, at our maximum nozzle current of 300 nA, dose rate coverage above 100 Gy/s increased from 57% to 96% in the lung and from 93% to 100% in the heart, and LET coverage above 4 keV/µm dropped from 68% to 9% in the lung and from 26% to &lt;1% in the heart. For a simple minipig plan, the full-width half-maximum of the dose, dose rate, and LET distributions decreased by 30%, 1.6%, and 57%, respectively, again with similar target dose coverage, thus reducing uncertainty in these quantities for preclinical studies. CONCLUSIONS: The inverse solution to IPO-IMPT demonstrated the capability to simultaneously modulate subspot proton energy and intensity distributions for clinical and preclinical studies.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/38104869/) · [DOI](https://doi.org/10.1016/j.ijrobp.2023.11.061)


---

### 3D-conformal very-high energy electron therapy as candidate modality for FLASH-RT: A treatment planning study for glioblastoma and lung cancer.

*Böhlen TT, Germond JF, Traneus E, Vallet V, Desorgher L, Ozsahin EM et al.* — Medical physics (2023)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Physics &amp; Dosimetry</span> <span class="badge tag">Beam Delivery &amp; Technology</span>


**TL;DR.** Pre-clinical ultra-high dose rate (UHDR) electron irradiations on time scales of 100 ms have demonstrated a remarkable sparing of brain and lung tissues while retaining tumor efficacy when compared to conventional dose rate irradiations. While clinically-used gantries and intensity modulation techniques are too slow to match such time scales, novel very-high energy electron (VHEE, 50-250 MeV) radi…


??? note "Abstract"
    BACKGROUND: Pre-clinical ultra-high dose rate (UHDR) electron irradiations on time scales of 100 ms have demonstrated a remarkable sparing of brain and lung tissues while retaining tumor efficacy when compared to conventional dose rate irradiations. While clinically-used gantries and intensity modulation techniques are too slow to match such time scales, novel very-high energy electron (VHEE, 50-250 MeV) radiotherapy (RT) devices using 3D-conformed broad VHEE beams are designed to deliver UHDR treatments that fulfill these timing requirements. PURPOSE: To assess the dosimetric plan quality obtained using VHEE-based 3D-conformal RT (3D-CRT) for treatments of glioblastoma and lung cancer patients and compare the resulting treatment plans to those delivered by standard-of-care intensity modulated photon RT (IMRT) techniques. METHODS: Seven glioblastoma patients and seven lung cancer patients were planned with VHEE-based 3D-CRT using 3 to 16 coplanar beams with equidistant angular spacing and energies of 100 and 200 MeV using a forward planning approach. Dose distributions, dose-volume histograms, coverage (V95% ) and homogeneity (HI98% ) for the planning target volume (PTV), as well as near-maximum doses (D2% ) and mean doses (Dmean ) for organs-at-risk (OAR) were evaluated and compared to clinical IMRT plans. RESULTS: Mean differences of V95% and HI98% of all VHEE plans were within 2% or better of the IMRT reference plans. Glioblastoma plan dose metrics obtained with VHEE configurations of 200 MeV and 3-16 beams were either not significantly different or were significantly improved compared to the clinical IMRT reference plans. All OAR plan dose metrics evaluated for VHEE plans created using 5 beams of 100 MeV were either not significantly different or within 3% on average, except for Dmean for the body, Dmean for the brain, D2% for the brain stem, and D2% for the chiasm, which were significantly increased by 1, 2, 6, and 8 Gy, respectively (however below clinical constraints). Similarly, the dose metrics for lung cancer patients were also either not significantly different or were significantly improved compared to the reference plans for VHEE configurations with 200 MeV and 5 to 16 beams with the exception of D2% and Dmean to the spinal canal (however below clinical constraints). For the lung cancer cases, the VHEE configurations using 100 MeV or only 3 beams resulted in significantly worse dose metrics for some OAR. Differences in dose metrics were, however, strongly patient-specific and similar for some patient cases. CONCLUSIONS: VHEE-based 3D-CRT may deliver conformal treatments to simple, mostly convex target shapes in the brain and the thorax with a limited number of critical adjacent OAR using a limited number of beams (as low as 3 to 7). Using such treatment techniques, a dosimetric plan quality comparable to that of standard-of-care IMRT can be achieved. Hence, from a treatment planning perspective, 3D-conformal UHDR VHEE treatments delivered on time scales of 100 ms represent a promising candidate technique for the clinical transfer of the FLASH effect.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/37427669/) · [DOI](https://doi.org/10.1002/mp.16586)


---

### A Novel Ultrahigh-Dose-Rate Proton Therapy Technology: Spot-Scanning Proton Arc Therapy + FLASH (SPLASH).

*Liu G, Zhao L, Li X, Zhang S, Dai S, Lu X et al.* — International journal of radiation oncology, biology, physics (2023)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Beam Delivery &amp; Technology</span> <span class="badge tag">Clinical &amp; Translational</span>


**TL;DR.** To take full advantage of FLASH dose rate (40 Gy/s) and high-dose conformity, we introduce a novel optimization and delivery technique, the spot-scanning proton arc therapy (SPArc) + FLASH (SPLASH). METHODS AND MATERIALS: SPLASH framework was implemented in an open-source proton planning platform (MatRad, Department of Medical Physics in Radiation Oncology, German Cancer Research Center).


??? note "Abstract"
    PURPOSE: To take full advantage of FLASH dose rate (40 Gy/s) and high-dose conformity, we introduce a novel optimization and delivery technique, the spot-scanning proton arc therapy (SPArc) + FLASH (SPLASH). METHODS AND MATERIALS: SPLASH framework was implemented in an open-source proton planning platform (MatRad, Department of Medical Physics in Radiation Oncology, German Cancer Research Center). It optimizes with the clinical dose-volume constraint based on dose distribution and the dose-average dose rate by minimizing the monitor unit constraint on spot weight and accelerator beam current sequentially, enabling the first dynamic arc therapy with voxel-based FLASH dose rate. This new optimization framework minimizes the overall cost function value combined with plan quality and voxel-based dose-rate constraints. Three representative cases (brain, liver, and prostate cancer) were used for testing purposes. Dose-volume histogram, dose-rate-volume histogram, and dose-rate map were compared among intensity modulated proton radiation therapy (IMPT), SPArc, and SPLASH. RESULTS: SPLASH/SPArc could offer superior plan quality over IMPT in terms of dose conformity. The dose-rate-volume histogram results indicated SPLASH could significantly improve V40 Gy/s in the target and region of interest for all tested cases compared with SPArc and IMPT. The optimal beam current per spot is simultaneously generated, which is within the existing proton machine specifications in the research version (&lt;200 nA). CONCLUSIONS: SPLASH offers the first voxel-based ultradose-rate and high-dose conformity treatment using proton beam therapy. Such a technique has the potential to fit the needs of a broad range of disease sites and simplify clinical workflow without applying a patient-specific ridge filter, which has never before been demonstrated.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/37196836/) · [DOI](https://doi.org/10.1016/j.ijrobp.2023.05.012)


---

### Feasibility study of hybrid inverse planning with transmission beams and single-energy spread-out Bragg peaks for proton FLASH radiotherapy.

*Ma C, Yang X, Chang CW, Liu R, Bohannon D, Lin L et al.* — Medical physics (2023)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Physics &amp; Dosimetry</span>


**TL;DR.** Ultra-high dose rate (FLASH) proton planning with only transmission beams (TBs) has limitations in normal tissue sparing. The single-energy spread-out Bragg peaks (SESOBPs) of the FLASH dose rate have been demonstrated feasible for proton FLASH planning.


??? note "Abstract"
    BACKGROUND: Ultra-high dose rate (FLASH) proton planning with only transmission beams (TBs) has limitations in normal tissue sparing. The single-energy spread-out Bragg peaks (SESOBPs) of the FLASH dose rate have been demonstrated feasible for proton FLASH planning. PURPOSE: To investigate the feasibility of combining TBs and SESOBPs for proton FLASH treatment. METHODS: A hybrid inverse optimization method was developed to combine the TBs and SESOBPs (TB-SESOBP) for FLASH planning. The SESOBPs were generated field-by-field from spreading out the BPs by pre-designed general bar ridge filters (RFs) and placed at the central target by range shifters (RSs) to obtain a uniform dose within the target. The SESOBPs and TBs were fully placed field-by-field allowing automatic spot selection and weighting in the optimization process. A spot reduction strategy was conducted in the optimization process to push up the minimum MU/spot assuring the plan deliverability at beam current of 165 nA. The TB-SESOBP plans were validated in comparison with the TB only (TB-only) plans and the plans with the combination of TBs and BPs (TB-BP plans) regarding 3D dose and dose rate (dose-averaged dose rate) distributions for five lung cases. The FLASH dose rate coverage (V40Gy/s ) was evaluated in the structure volume receiving &gt; 10% of the prescription dose. RESULTS: Compared to the TB-only plans, the mean spinal cord D1.2cc drastically reduced by 41% (P &lt; 0.05), the mean lung V7Gy and V7.4 Gy moderately reduced by up to 17% (P &lt; 0.05), and the target dose homogeneity slightly increased in the TB-SESOBP plans. Comparable dose homogeneity was achieved in both TB-SESOBP and TB-BP plans. Besides, prominent improvements were achieved in lung sparing for the cases of relatively large targets by the TB-SESOBP plans compared to the TB-BP plans. The targets and the skin were fully covered with the FLASH dose rate in all three plans. For the OARs, V40Gy/s  = 100% was achieved by the TB-only plans while V40Gy/s  &gt; 85% was obtained by the other two plans. CONCLUSION: We have demonstrated that the hybrid TB-SESOBP planning was feasible to achieve FLASH dose rate for proton therapy. With pre-designed general bar RFs, the hybrid TB-SESOBP planning could be implemented for proton adaptive FLASH radiotherapy. As an alternative FLASH planning approach to TB-only planning, the hybrid TB-SESOBP planning has great potential in dosimetrically improving OAR sparing while maintaining high target dose homogeneity.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/36932635/) · [DOI](https://doi.org/10.1002/mp.16370) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11700378/)


---

### An Integrated Physical Optimization Framework for Proton Stereotactic Body Radiation Therapy FLASH Treatment Planning Allows Dose, Dose Rate, and Linear Energy Transfer Optimization Using Patient-Specific Ridge Filters.

*Liu R, Charyyev S, Wahl N, Liu W, Kang M, Zhou J et al.* — International journal of radiation oncology, biology, physics (2023)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Modeling &amp; Mechanisms</span> <span class="badge tag">Clinical &amp; Translational</span>


**TL;DR.** Patient-specific ridge filters provide a passive means to modulate proton energy to obtain a conformal dose. Here we describe a new framework for optimization of filter design and spot maps to meet the unique demands of ultrahigh-dose-rate (FLASH) radiation therapy.


??? note "Abstract"
    PURPOSE: Patient-specific ridge filters provide a passive means to modulate proton energy to obtain a conformal dose. Here we describe a new framework for optimization of filter design and spot maps to meet the unique demands of ultrahigh-dose-rate (FLASH) radiation therapy. We demonstrate an integrated physical optimization Intensity-modulated proton therapy (IMPT) (IPO-IMPT) approach for optimization of dose, dose-averaged dose rate (DADR), and dose-averaged linear energy transfer (LETd). METHODS AND MATERIALS: We developed an inverse planning software to design patient-specific ridge filters that spread the Bragg peak from a fixed-energy, 250-MeV beam to a proximal beam-specific planning target volume. The software defines patient-specific ridge filter pin shapes and uses a Monte Carlo calculation engine, based on Geant4, to provide dose and LET influence matrices. Plan optimization, using matRAD, accommodates the IPO-IMPT objective function considering dose, dose rate, and LET simultaneously with minimum monitor unit constraints. The framework enables design of both regularly spaced and sparse-optimized ridge filters, from which some pins are omitted to allow faster delivery and selective LET optimization. To demonstrate the framework, we designed ridge filters for 3 example patients with lung cancer and optimized the plans using IPO-IMPT. RESULTS: The IPO-IMPT framework selectively spared the organs at risk by reducing LET and increasing dose rate, relative to IMPT planning. Sparse-optimized ridge filters were superior to regularly spaced ridge filters in dose rate. Depending on which parameter is prioritized, volume distributions and histograms for dose, DADR, and LETd, using evaluation structures specific to heart, lung, and esophagus, show high levels of FLASH dose-rate coverage and/or reduced LETd, while maintaining dose coverage within the beam specific planning target volume. CONCLUSIONS: This proof-of-concept study demonstrates the feasibility of using an IPO-IMPT framework to accomplish proton FLASH stereotactic body proton therapy, accounting for dose, DADR, and LETd simultaneously.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/36736634/) · [DOI](https://doi.org/10.1016/j.ijrobp.2023.01.048)


---

### Pencil-beam Delivery Pattern Optimization Increases Dose Rate for Stereotactic FLASH Proton Therapy.

*José Santo R, Habraken SJM, Breedveld S, Hoogeman MS* — International journal of radiation oncology, biology, physics (2023)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Beam Delivery &amp; Technology</span>


**TL;DR.** FLASH dose rates &gt;40 Gy/s are readily available in proton therapy (PT) with cyclotron-accelerated beams and pencil-beam scanning (PBS). The PBS delivery pattern will affect the local dose rate, as quantified by the PBS dose rate (PBS-DR), and therefore needs to be accounted for in FLASH-PT with PBS, but it is not yet clear how.


??? note "Abstract"
    PURPOSE: FLASH dose rates &gt;40 Gy/s are readily available in proton therapy (PT) with cyclotron-accelerated beams and pencil-beam scanning (PBS). The PBS delivery pattern will affect the local dose rate, as quantified by the PBS dose rate (PBS-DR), and therefore needs to be accounted for in FLASH-PT with PBS, but it is not yet clear how. Our aim was to optimize patient-specific scan patterns for stereotactic FLASH-PT of early-stage lung cancer and lung metastases, maximizing the volume irradiated with PBS-DR &gt;40 Gy/s of the organs at risk voxels irradiated to &gt;8 Gy (FLASH coverage). METHODS AND MATERIALS: Plans to 54 Gy/3 fractions with 3 equiangular coplanar 244 MeV proton shoot-through transmission beams for 20 patients were optimized with in-house developed software. Planning target volume-based planning with a 5 mm margin was used. Planning target volume ranged from 4.4 to 84 cc. Scan-pattern optimization was performed with a Genetic Algorithm, run in parallel for 20 independent populations (islands). Mapped crossover, inversion, swap, and shift operators were applied to achieve (local) optimality on each island, with migration between them for global optimality. The cost function was chosen to maximize the FLASH coverage per beam at &gt;8 Gy, &gt;40 Gy/s, and 40 nA beam current. The optimized patterns were evaluated on FLASH coverage, PBS-DR distribution, and population PBS-DR-volume histograms, compared with standard line-by-line scanning. Robustness against beam current variation was investigated. RESULTS: The optimized patterns have a snowflake-like structure, combined with outward swirling for larger targets. A population median FLASH coverage of 29.0% was obtained for optimized patterns compared with 6.9% for standard patterns, illustrating a significant increase in FLASH coverage for optimized patterns. For beam current variations of 5 nA, FLASH coverage varied between -6.1%-point and 2.2%-point for optimized patterns. CONCLUSIONS: Significant improvements on the PBS-DR and, hence, on FLASH coverage and potential healthy-tissue sparing are obtained by sequential scan-pattern optimization. The optimizer is flexible and may be further fine-tuned, based on the exact conditions for FLASH.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/36057377/) · [DOI](https://doi.org/10.1016/j.ijrobp.2022.08.053)


---

### Dose and dose rate objectives in Bragg peak and shoot-through beam orientation optimization for FLASH proton therapy.

*Ramesh P, Gu W, Ruan D, Sheng K* — Medical physics (2022)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Physics &amp; Dosimetry</span>


**TL;DR.** The combined use of Bragg peak (BP) and shoot-through (ST) beams has previously been shown to increase the normal tissue volume receiving FLASH dose rates while maintaining dose conformality compared to conventional intensity-modulated proton therapy (IMPT) methods. However, the fixed beam optimization method has not considered the effects of beam orientation on the dose and dose rates.


??? note "Abstract"
    PURPOSE: The combined use of Bragg peak (BP) and shoot-through (ST) beams has previously been shown to increase the normal tissue volume receiving FLASH dose rates while maintaining dose conformality compared to conventional intensity-modulated proton therapy (IMPT) methods. However, the fixed beam optimization method has not considered the effects of beam orientation on the dose and dose rates. To maximize the proton FLASH effect, here, we incorporate dose rate objectives into our beam orientation optimization framework. METHODS: From our previously developed group-sparsity dose objectives, we add upper and lower dose rate terms using a surrogate dose-averaged dose rate definition and solve using the fast-iterative shrinking threshold algorithm. We compare the dosimetry for three head-and-neck cases between four techniques: (1) spread-out BP IMPT (BP), (2) dose rate optimization using BP beams only (BP-DR), (3) dose rate optimization using ST beams only (ST-DR), and (4) dose rate optimization using combined BP and ST (BPST-DR), with the goal of sparing organs at risk without loss of tumor coverage and maintaining high dose rate within a 10 mm region of interest (ROI) surrounding the clinical target volume (CTV). RESULTS: For BP, BP-DR, ST-DR, and BPST-DR, CTV homogeneity index and Dmax were found to be on average 0.886, 0.867, 0.687, and 0.936 and 107%, 109%, 135%, and 101% of prescription, respectively. Although ST-DR plans were not able to meet dosimetric standards, BPST-DR was able to match or improve either maximum or mean dose in the right submandibular gland, left and right parotids, constrictors, larynx, and spinal cord compared to BP plans. Volume of ROIs receiving greater than 40 Gy/s (   V γ 0  )  ${V_{\gamma 0}})$  was 51.0%, 91.4%, 95.5%, and 92.1% on average. CONCLUSIONS: The dose rate techniques, particularly BPST-DR, were able to significantly increase dose rate without compromising physical dose compared with BP. Our algorithm efficiently selects beams that are optimal for both dose and dose rate.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/36222217/) · [DOI](https://doi.org/10.1002/mp.16009) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9829523/)


---

### Dose rate and dose robustness for proton transmission FLASH-RT treatment in lung cancer.

*Wei S, Lin H, Huang S, Shi C, Xiong W, Zhai H et al.* — Frontiers in oncology (2022)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Physics &amp; Dosimetry</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Beam Delivery &amp; Technology</span>


**TL;DR.** To evaluate the plan quality and robustness of both dose and dose rate of proton pencil beam scanning (PBS) transmission FLASH delivery in lung cancer treatment. METHODS AND MATERIALS: An in-house FLASH planning platform was used to optimize 10 lung cancer patients previously consecutively treated with proton stereotactic body radiation therapy (SBRT) to receive 3 and 5 transmission beams (Trx-3fd…


??? note "Abstract"
    PURPOSES: To evaluate the plan quality and robustness of both dose and dose rate of proton pencil beam scanning (PBS) transmission FLASH delivery in lung cancer treatment. METHODS AND MATERIALS: An in-house FLASH planning platform was used to optimize 10 lung cancer patients previously consecutively treated with proton stereotactic body radiation therapy (SBRT) to receive 3 and 5 transmission beams (Trx-3fds and Trx-5fds, respectively) to 34 Gy in a single fraction. Perturbation scenarios (n=12) for setup and range uncertainties (5 mm and 3.5%) were introduced, and dose-volume histogram and dose-rate-volume histogram bands were generated. Conventional proton SBRT clinical plans were used as a reference. RTOG 0915 dose metrics and 40 Gy/s dose rate coverage (V40Gy/s) were used to assess the dose and dose rate robustness. RESULTS: Trx-5fds yields a comparable iCTV D2% of 105.3%, whereas Trx-3fds resulted in inferior D2% of 111.9% to the clinical SBRT plans with D2% of 105.6% (p&lt;0.05). Both Trx-5fds and Trx-3fds plans had slightly worse dose metrics to organs at risk than SBRT plans. Trx-5fds achieved superior dosimetry robustness for iCTV, esophagus, and spinal cord doses than both Trx-3fds and conventional SBRT plans. There was no significant difference in dose rate robustness for V40Gy/s coverage between Trx-3fds and Trx-5fds. Dose rate distribution has similar distributions to the dose when perturbation exists. CONCLUSION: Transmission plans yield overall modestly inferior plan quality compared to the conventional proton SBRT plans but provide improved robustness and the potential for a toxicity-sparing FLASH effect. By using more beams (5- versus 3-field), both dose and dose rate robustness for transmission plans can be achieved.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/36059710/) · [DOI](https://doi.org/10.3389/fonc.2022.970602) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9435957/)


---

### Advanced pencil beam scanning Bragg peak FLASH-RT delivery technique can enhance lung cancer planning treatment outcomes compared to conventional multiple-energy proton PBS techniques.

*Wei S, Lin H, Isabelle Choi J, Shi C, Simone CB, Kang M* — Radiotherapy and oncology : journal of the European Society for Therapeutic Radiology and Oncology (2022)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Physics &amp; Dosimetry</span> <span class="badge tag">Beam Delivery &amp; Technology</span>


**TL;DR.** To investigate the dosimetric characteristics between an advanced proton pencil beam scanning (PBS) Bragg peak FLASH technique and conventional PBS planning technique in lung tumors. To evaluate the &quot;FLASHness&quot; of single-field in a multiple-field delivery scheme for a hypofractionation regimen and move a step forward to clinical application.


??? note "Abstract"
    PURPOSE: To investigate the dosimetric characteristics between an advanced proton pencil beam scanning (PBS) Bragg peak FLASH technique and conventional PBS planning technique in lung tumors. To evaluate the &quot;FLASHness&quot; of single-field in a multiple-field delivery scheme for a hypofractionation regimen and move a step forward to clinical application. METHODS: Single-energy PBS Bragg peak FLASH treatment plans were optimized based on a novel Bragg peak tracking technique to enable Bragg peaks to stop at the distal edge of the target. Inverse treatment planning using multiple-field optimization (MFO) can achieve sufficient FLASH dose rate and intensity-modulated proton therapy (IMPT)-equivalent dosimetric quality. The dose rate of organs-at-risk (OARs) and the target were calculated under FLASH machine parameters. A group of 10 consecutive lung SBRT patients was optimized to 34 Gy/fraction using a standard treatment of PBS technique with multiple energy layers as references to the Bragg peak plans. The dosimetric quality was compared between Bragg peak FLASH and conventional plans based on RTOG0915 dose metrics. FLASH dose rate ratios (V40Gy/s) were calculated as a metric of the FLASH-sparing effect. RESULTS: For higher dose thresholds, the Bragg peak plans achieved greater V40Gy/s FLASH coverage for all major OARs. The V40Gy/s was close to 100% for all OARs when the dose thresholds were &gt; 5 Gy for full plan and single beam evaluations. The less &quot;FLASHness&quot; region was associated with a low dose distribution, mainly occurring in the PBS field penumbra region. The conventional IMPT treatment plans yielded slightly superior target dose uniformity with a D2%(%) of 108.02% versus that of Bragg peak 300 MU plans of 111.81% (p &lt; 0.01) and that of Bragg peak 1200 MU plans of 115.95% (p &lt; 0.01). No significant difference in dose metrics was found between Bragg peak and IMPT treatment plans for the spinal cord, esophagus, heart, or lung-GTV (all p &gt; 0.05). CONCLUSION: Hypofractionated lung Bragg peak plans can maintain comparable plan quality to conventional PBS while achieving sufficient FLASH dose rate coverage for major OARs for each field under the multiple-field delivery scheme. The novel Bragg peak FLASH technique has the potential to enhance lung cancer planning treatment outcomes compared to standard PBS treatment techniques.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/35961583/) · [DOI](https://doi.org/10.1016/j.radonc.2022.08.005)


---

### Use of single-energy proton pencil beam scanning Bragg peak for intensity-modulated proton therapy FLASH treatment planning in liver-hypofractionated radiation therapy.

*Wei S, Lin H, Shi C, Xiong W, Chen CC, Huang S et al.* — Medical physics (2022)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Clinical &amp; Translational</span> <span class="badge tag">Beam Delivery &amp; Technology</span>


**TL;DR.** The transmission proton FLASH technique delivers high doses to the normal tissue distal to the target, which is less conformal compared to the Bragg peak technique. To investigate FLASH radiotherapy (RT) planning using single-energy Bragg peak beams with a similar beam arrangement as clinical intensity-modulated proton therapy (IMPT) in a liver stereotactic body radiation therapy (SBRT) and to cha…


??? note "Abstract"
    PURPOSE: The transmission proton FLASH technique delivers high doses to the normal tissue distal to the target, which is less conformal compared to the Bragg peak technique. To investigate FLASH radiotherapy (RT) planning using single-energy Bragg peak beams with a similar beam arrangement as clinical intensity-modulated proton therapy (IMPT) in a liver stereotactic body radiation therapy (SBRT) and to characterize the plan quality, dose sparing of organs-at-risk (OARs), and FLASH dose rate percentage. MATERIALS AND METHODS: An in-house platform was developed to enable inverse IMPT-FLASH planning using single-energy Bragg peaks. A universal range shifter and range compensators were utilized to effectively align the Bragg peak to the distal edge of the target. Two different minimum MU settings of 400 and 800 MU/spot (Bragg-400 MU and Bragg-800 MU) plans were investigated on 10 consecutive hepatocellular carcinoma patients previously treated by IMPT-SBRT to evaluate the FLASH dose and dose rate coverage for OARs. The IMPT-FLASH using single-energy Bragg peaks delivered 50 Gy in five fractions with similar or identical beam arrangement to the clinical IMPT-SBRT plans. NRG GI003 dose constraint metrics were used. Three dose rate calculation methods, including average dose rate (ADR), dose threshold dose rate (DTDR), and dose-ADR (DADR), were all studied. RESULTS: The novel spot map optimization can fulfill the inverse planning using single-energy Bragg peaks. All the Bragg peak FLASH plans achieved similar results for the liver-gross tumor volume (GTV) Dmean and heart  D 0.5  c m 3   ${D_{0.5\,{\rm{c}}{{\rm{m}}^3}}}$  , compared to SBRT-IMPT. The Bragg-800 MU plans resulted in 18.3% higher clinical target volume (CTV)  D 2  c m 3   ${D_{2\,{\rm{c}}{{\rm{m}}^{\rm{3}}}}}$  compared with SBRT (p &lt; 0.05), and no significant difference was found between Bragg-400 MU and SBRT plans. For the CTV Dmax , SBRT plans resulted in 10.3% (p &lt; 0.01) less than Bragg-400 MU plans and 16.6% (p &lt; 0.01) less than Bragg-800 MU plans. The Bragg-800 MU plans generally achieved higher ADR, DADR, and DTDR dose rates than Bragg-400 MU plans, and DADR mostly led to the highest V40 Gy/s compared to other dose rate calculation methods, whereas ADR led to the lowest. The lower dose rate portions in certain OARs are related to the lower dose deposited due to the farther distances from targets, especially in the penumbra of the beams. CONCLUSION: Single-energy Bragg peak IMPT-FLASH plans eliminate the exit dose in normal tissues, maintaining comparable dose metrics to the conventional IMPT-SBRT plans, while achieving a sufficient FLASH dose rate for liver cancers. This study demonstrates the feasibility of and sufficiently high dose rate when applying the Bragg peak FLASH treatment for a liver cancer hypofractionated FLASH therapy. The advancement of this novel method has the potential to optimize treatment for liver cancer patients.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/35929404/) · [DOI](https://doi.org/10.1002/mp.15894)


---

### Single-fraction 34 Gy Lung Stereotactic Body Radiation Therapy Using Proton Transmission Beams: FLASH-dose Calculations and the Influence of Different Dose-rate Methods and Dose/Dose-rate Thresholds.

*van Marlen P, Verbakel WFAR, Slotman BJ, Dahele M* — Advances in radiation oncology (2022)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Physics &amp; Dosimetry</span> <span class="badge tag">Beam Delivery &amp; Technology</span>


**TL;DR.** Research suggests that in addition to the dose-rate, a dose threshold is also important for the reduction in normal tissue toxicity with similar tumor control after ultrahigh dose-rate radiation therapy (UHDR-RT). In this analysis we aimed to identify factors that might limit the ability to achieve this &quot;FLASH&quot;-effect in a scenario attractive for UHDR-RT (high fractional beam dose, small target, f…


??? note "Abstract"
    PURPOSE: Research suggests that in addition to the dose-rate, a dose threshold is also important for the reduction in normal tissue toxicity with similar tumor control after ultrahigh dose-rate radiation therapy (UHDR-RT). In this analysis we aimed to identify factors that might limit the ability to achieve this &quot;FLASH&quot;-effect in a scenario attractive for UHDR-RT (high fractional beam dose, small target, few organs-at-risk): single-fraction 34 Gy lung stereotactic body radiation therapy. METHODS AND MATERIALS: Clinical volumetric-modulated arc therapy (VMAT) plans, intensity modulated proton therapy (IMPT) plans and transmission beam (TB) plans were compared for 6 small and 1 large lung lesion. The TB-plan dose-rate was calculated using 4 methods and the FLASH-percentage (percentage of dose delivered at dose-rates ≥40/100 Gy/s and ≥4/8 Gy) was determined for various variables: a minimum spot time (minST) of 0.5/2 ms, maximum nozzle current (maxN) of 200/40 0nA, and 2 gantry current (GC) techniques (energy-layer based, spot-based \[SB\]). RESULTS: Based on absolute doses 5-beam TB and VMAT-plans are similar, but TB-plans have higher rib, skin, and ipsilateral lung dose than IMPT. Dose-rate calculation methods not considering scanning achieve FLASH-percentages between ∼30% to 80%, while methods considering scanning often achieve &lt;30%. FLASH-percentages increase for lower minST/higher maxN and when using SB GC instead of energy-layer based GC, often approaching the percentage of dose exceeding the dose-threshold. For the small lesions average beam irradiation times (including scanning) varied between 0.06 to 0.31 seconds and total irradiation times between 0.28 to 1.57 seconds, for the large lesion beam times were between 0.16 to 1.47 seconds with total irradiation times of 1.09 to 5.89 seconds. CONCLUSIONS: In a theoretically advantageous scenario for FLASH we found that TB-plan dosimetry was similar to that of VMAT, but inferior to that of IMPT, and that decreasing minST or using SB GC increase the estimated amount of FLASH. For the appropriate machine/delivery parameters high enough dose-rates can be achieved regardless of calculation method, meaning that a possible FLASH dose-threshold will likely be the primary limiting factor.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/35634574/) · [DOI](https://doi.org/10.1016/j.adro.2022.100954) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9130077/)


---

### Design of static and dynamic ridge filters for FLASH-IMPT: A simulation study.

*Zhang G, Gao W, Peng H* — Medical physics (2022)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Modeling &amp; Mechanisms</span> <span class="badge tag">Beam Delivery &amp; Technology</span>


**TL;DR.** This paper focused on the design and optimization of ridge filter-based intensity-modulated proton therapy (IMPT), and its potential applications for FLASH. Differing from the standard pencil beam scanning (PBS) mode, no energy/layer switching is required and total treatment time can be shortened.


??? note "Abstract"
    PURPOSE: This paper focused on the design and optimization of ridge filter-based intensity-modulated proton therapy (IMPT), and its potential applications for FLASH. Differing from the standard pencil beam scanning (PBS) mode, no energy/layer switching is required and total treatment time can be shortened. METHODS: Unique dose-influence matrices were generated as a proton beam traverses through slabs of different thicknesses (i.e., modulation by different layers). To establish the references for comparison, conventional IMPT plans (single field) were created using a large-scale nonlinear solver. The spot weights from the reference IMPT plans were used as inputs for optimizing the design of ridge filters. Two designs were evaluated: model A (static) and model B (dynamic). The ridge filter designs were first verified (by GEANT4 simulation) in a water phantom and then in an H&amp;N case. A direct comparison was made between the GEANT4 simulation results of two models and their respective references, with regard to plan quality, dose-averaged dose rate, and total treatment time. RESULTS: In both the water phantom and the H&amp;N case, two models are able to modulate dose distributions with high conformity, showing no significant difference relative to the reference plans. Dose rate-volume histograms suggest that in order to achieve a dose rate of 40 Gy/s over 90% PTV, the beam intensity needs to be 2.5 × 1011 protons/s for both models. For a fraction dose of 10 Gy, the total treatment time (including both irradiation time and dead time) can be shortened by a factor of 4.9 (model A) and 6.5 (model B), relative to the reference plans. CONCLUSION: Two proposed designs (both static and dynamic) can be used for PBS-IMPT requiring no layer switching. They are promising candidates for FLASH-IMPT capable of reducing treatment time and achieving high dose rates while maintaining dose conformity simultaneously.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/35595708/) · [DOI](https://doi.org/10.1002/mp.15717)


---

### A Universal Range Shifter and Range Compensator Can Enable Proton Pencil Beam Scanning Single-Energy Bragg Peak FLASH-RT Treatment Using Current Commercially Available Proton Systems.

*Kang M, Wei S, Choi JI, Lin H, Simone CB* — International journal of radiation oncology, biology, physics (2022)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Physics &amp; Dosimetry</span> <span class="badge tag">Beam Delivery &amp; Technology</span>


**TL;DR.** Transmission beams have been proposed for ultra-high dose (or FLASH) proton planning, limiting the organ sparing potentials of proton therapy. By pulling back the ranges of the highest energy proton beams and compensating proton ranges to adapt to the target distally, the exit dose of proton beams can be eliminated to better protect organs at risk while still preserving FLASH dose rate delivery.


??? note "Abstract"
    PURPOSE: Transmission beams have been proposed for ultra-high dose (or FLASH) proton planning, limiting the organ sparing potentials of proton therapy. By pulling back the ranges of the highest energy proton beams and compensating proton ranges to adapt to the target distally, the exit dose of proton beams can be eliminated to better protect organs at risk while still preserving FLASH dose rate delivery. METHOD AND MATERIALS: An inverse planning tool was developed to optimize intensity modulated proton therapy using a single-energy layer for FLASH radiation therapy planning. The range pull-backs were calculated to stop single-energy proton beams at the distal edge of the target. The spot map and weights of each field were optimized to achieve a sufficient dose rate using proton beam Bragg peaks. A C-shape target in phantom, along with 6 consecutive lung cancer patients previously treated using proton stereotactic body radiation therapy were planned using this novel Bragg Peak method and also transmission technique. Dosimetry characteristics and 3-dimensional dose rate were investigated. RESULTS: The minimum monitor units (MU) for transmission and Bragg peak plans were 400 MU/spot and 1200 MU/spot, respectively, corresponding to spot peak dose rates of 670 GyRBE (relative biological effectiveness) per second and 1950 GyRBE per second. Bragg peak plans yield a generally comparable target uniformity while significantly reducing dose spillage volume from the low to medium dose level. For all the 6 lung cases delivery of 34 GyRBE in 1 fraction, assessing Radiation Therapy Oncology Group 0915 constraints, the lung V7GyRBE volume was reduced by up to 32% (P = .001) for Bragg peak plans. The transmission plans tended to generate 2.4% higher FLASH dose rate coverage (V40GyRBE/s) versus Bragg peak plans over the major organs at risk. However, Bragg peak plans could also reach the FLASH radiation therapy threshold of V40GyRBE/s using a higher MU/spot and sophisticated dose-rate optimization algorithm. CONCLUSIONS: This first proof-of-concept study has demonstrated this novel method of combining range pull-back and powerful inverse optimization capable of achieving FLASH dose rate based on currently available machine parameters using a single-energy Bragg peak. Similar target coverage and uniformity can be maintained by Bragg peak FLASH plans while substantially improving the sparing of organs at risk compared with transmission plans.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/35101597/) · [DOI](https://doi.org/10.1016/j.ijrobp.2022.01.009)


---

### Simultaneous dose and dose rate optimization (SDDRO) of the FLASH effect for pencil-beam-scanning proton therapy.

*Gao H, Liu J, Lin Y, Gan GN, Pratx G, Wang F et al.* — Medical physics (2022)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span>


**TL;DR.** Compared to CONV-RT (with conventional dose rate), FLASH-RT (with ultra-high dose rate) can provide biological dose sparing for organs-at-risk (OARs) via the so-called FLASH effect, in addition to physical dose sparing. However, the FLASH effect only occurs, when both dose and dose rate meet certain minimum thresholds.


??? note "Abstract"
    PURPOSE: Compared to CONV-RT (with conventional dose rate), FLASH-RT (with ultra-high dose rate) can provide biological dose sparing for organs-at-risk (OARs) via the so-called FLASH effect, in addition to physical dose sparing. However, the FLASH effect only occurs, when both dose and dose rate meet certain minimum thresholds. This work will develop a simultaneous dose and dose rate optimization (SDDRO) method accounting for both FLASH dose and dose rate constraints during treatment planning for pencil-beam-scanning proton therapy. METHODS: SDDRO optimizes the FLASH effect (specific to FLASH-RT) as well as the dose distribution (similar to CONV-RT). The nonlinear dose rate constraint is linearized, and the reformulated optimization problem is efficiently solved via iterative convex relaxation powered by alternating direction method of multipliers. To resolve and quantify the generic tradeoff of FLASH-RT between FLASH and dose optimization, we propose the use of FLASH effective dose based on dose modifying factor (DMF) owing to the FLASH effect. RESULTS: FLASH-RT via transmission beams (TB) (IMPT-TB or SDDRO) and CONV-RT via Bragg peaks (BP) (IMPT-BP) were evaluated for clinical prostate, lung, head-and-neck (HN), and brain cases. Despite the use of TB, which is generally suboptimal to BP for normal tissue sparing, FLASH-RT via SDDRO considerably reduced FLASH effective dose for high-dose OAR adjacent to the target. For example, in the lung SBRT case, the max esophageal dose constraint 27 Gy was only met by SDDRO (24.8 Gy), compared to IMPT-BP (35.3 Gy) or IMPT-TB (36.6 Gy); in the brain SRS case, the brain constraint V12Gy≤15cc was also only met by SDDRO (13.7cc), compared to IMPT-BP (43.9cc) or IMPT-TB (18.4cc). In addition, SDDRO substantially improved the FLASH coverage from IMPT-TB, e.g., an increase from 37.2% to 67.1% for lung, from 39.1% to 58.3% for prostate, from 65.4% to 82.1% for HN, from 50.8% to 73.3% for the brain. CONCLUSIONS: Both FLASH dose and dose rate constraints are incorporated into SDDRO for FLASH-RT that jointly optimizes the FLASH effect and physical dose distribution. FLASH effective dose via FLASH DMF is introduced to reconcile the tradeoff between physical dose sparing and FLASH sparing, and quantify the net effective gain from CONV-RT to FLASH-RT.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/34800301/) · [DOI](https://doi.org/10.1002/mp.15356) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8917068/)


---

### FLASH Radiotherapy Using Single-Energy Proton PBS Transmission Beams for Hypofractionation Liver Cancer: Dose and Dose Rate Quantification.

*Wei S, Lin H, Choi JI, Press RH, Lazarev S, Kabarriti R et al.* — Frontiers in oncology (2021)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Physics &amp; Dosimetry</span> <span class="badge tag">Beam Delivery &amp; Technology</span>


**TL;DR.** This work aims to study the dose and ultra-high-dose rate characteristics of transmission proton pencil beam scanning (PBS) FLASH radiotherapy (RT) for hypofractionation liver cancer based on the parameters of a commercially available proton system operating under FLASH mode. METHODS AND MATERIALS: An in-house treatment planning software (TPS) was developed to perform intensity-modulated proton th…


??? note "Abstract"
    PURPOSE: This work aims to study the dose and ultra-high-dose rate characteristics of transmission proton pencil beam scanning (PBS) FLASH radiotherapy (RT) for hypofractionation liver cancer based on the parameters of a commercially available proton system operating under FLASH mode. METHODS AND MATERIALS: An in-house treatment planning software (TPS) was developed to perform intensity-modulated proton therapy (IMPT) FLASH-RT planning. Single-energy transmission proton PBS plans of 4.5 Gy × 15 fractions were optimized for seven consecutive hepatocellular carcinoma patients, using 2 and 5 fields combined with 1) the minimum MU/spot chosen between 100 and 400, and minimum spot time (MST) of 2 ms, and 2) the minimum MU/spot of 100, and MST of 0.5 ms, based upon considerations in target uniformities, OAR dose constraints, and OAR FLASH dose rate coverage. Then, the 3D average dose rate distribution was calculated. The dose metrics for the mean dose of Liver-GTV and other major OARs were characterized to evaluate the dose quality for the different combinations of field numbers and minimum spot times compared to that of conventional IMPT plans. Dose rate quality was evaluated using 40 Gy/s volume coverage (V40Gy/s). RESULTS: All plans achieved favorable and comparable target uniformities, and target uniformity improved as the number of fields increased. For OARs, no significant dose differences were observed between plans of different field numbers and the same MST. For plans using shorter MST and the same field numbers, better sparing was generally observed in most OARs and was statistically significant for the chest wall. However, the FLASH dose rate coverage V40Gy/s was increased by 20% for 2-field plans compared to 5-field plans in most OARs with 2-ms MST, which was less evident in the 0.5-ms cases. For 2-field plans, dose metrics and V40Gy/s of select OARs have large variations due to the beam angle selection and variable distances to the targets. The transmission plans generally yielded inferior dosimetric quality to the conventional IMPT plans. CONCLUSION: This is the first attempt to assess liver FLASH treatment planning and demonstrates that it is challenging for hypofractionation with smaller fractional doses (4.5 Gy/fraction). Using fewer fields can allow higher minimum MU/spot, resulting in higher OAR FLASH dose rate coverages while achieving similar plan quality compared to plans with more fields. Shorter MST can result in better plan quality and comparable or even better FLASH dose rate coverage.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/35096620/) · [DOI](https://doi.org/10.3389/fonc.2021.813063) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8794777/)


---

### A Novel Proton Pencil Beam Scanning FLASH RT Delivery Method Enables Optimal OAR Sparing and Ultra-High Dose Rate Delivery: A Comprehensive Dosimetry Study for Lung Tumors.

*Wei S, Lin H, Choi JI, Simone CB, Kang M* — Cancers (2021)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Physics &amp; Dosimetry</span> <span class="badge tag">Beam Delivery &amp; Technology</span>


**TL;DR.** While transmission proton beams have been demonstrated to achieve ultra-high dose rate FLASH therapy delivery, they are unable to spare normal tissues distal to the target. This study aims to compare FLASH treatment planning using single energy Bragg peak proton beams versus transmission proton beams in lung tumors and to evaluate Bragg peak plan optimization, characterize plan quality, and quanti…


??? note "Abstract"
    PURPOSE: While transmission proton beams have been demonstrated to achieve ultra-high dose rate FLASH therapy delivery, they are unable to spare normal tissues distal to the target. This study aims to compare FLASH treatment planning using single energy Bragg peak proton beams versus transmission proton beams in lung tumors and to evaluate Bragg peak plan optimization, characterize plan quality, and quantify organ-at-risk (OAR) sparing. MATERIALS AND METHODS: Both Bragg peak and transmission plans were optimized using an in-house platform for 10 consecutive lung patients previously treated with proton stereotactic body radiation therapy (SBRT). To bring the dose rate up to the FLASH-RT threshold, Bragg peak plans with a minimum MU/spot of 1200 and transmission plans with a minimum MU/spot of 400 were developed. Two common prescriptions, 34 Gy in 1 fraction and 54 Gy in 3 fractions, were studied with the same beam arrangement for both Bragg peak and transmission plans (n = 40 plans). RTOG 0915 dosimetry metrics and dose rate metrics based on different dose rate calculations, including average dose rate (ADR), dose-averaged dose rate (DADR), and dose threshold dose rate (DTDR), were investigated. We then evaluated the effect of beam angular optimization on the Bragg peak plans to explore the potential for superior OAR sparing. RESULTS: Bragg peak plans significantly reduced doses to several OAR dose parameters, including lung V7.4Gy and V7Gy by 32.0% (p &lt; 0.01) and 30.4% (p &lt; 0.01) for 34Gy/fx plans, respectively; and by 40.8% (p &lt; 0.01) and 41.2% (p &lt; 0.01) for 18Gy/fx plans, respectively, compared with transmission plans. Bragg peak plans have ~3% less in DADR and ~10% differences in mean OARs in DTDR and DADR relative to transmission plans due to the larger portion of lower dose regions of Bragg peak plans. With angular optimization, optimized Bragg peak plans can further reduce the lung V7Gy by 20.7% (p &lt; 0.01) and V7.4Gy by 19.7% (p &lt; 0.01) compared with Bragg peak plans without angular optimization while achieving a similar 3D dose rate distribution. CONCLUSION: The single-energy Bragg peak plans achieve superior dosimetry performances in OARs to transmission plans with comparable dose rate performances for lung cancer FLASH therapy. Beam angle optimization can further improve the OAR dosimetry parameters with similar 3D FLASH dose rate coverage.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/34830946/) · [DOI](https://doi.org/10.3390/cancers13225790) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8616118/)


---

### FLASH radiotherapy: Considerations for multibeam and hypofractionation dose delivery.

*MacKay R, Burnet N, Lowe M, Rothwell B, Kirkby N, Kirkby K et al.* — Radiotherapy and oncology : journal of the European Society for Therapeutic Radiology and Oncology (2021)  

<span class="badge tag">Treatment Planning &amp; Optimization</span>


[PubMed](https://pubmed.ncbi.nlm.nih.gov/34563608/) · [DOI](https://doi.org/10.1016/j.radonc.2021.09.011)


---

### Quantitative Assessment of 3D Dose Rate for Proton Pencil Beam Scanning FLASH Radiotherapy and Its Application for Lung Hypofractionation Treatment Planning.

*Kang M, Wei S, Choi JI, Simone CB, Lin H* — Cancers (2021)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Beam Delivery &amp; Technology</span>


**TL;DR.** To quantitatively assess target and organs-at-risk (OAR) dose rate based on three proposed proton PBS dose rate metrics and study FLASH intensity-modulated proton therapy (IMPT) treatment planning using transmission beams. An in-house FLASH planning platform was developed to optimize transmission (shoot-through) plans for nine consecutive lung cancer patients previously planned with proton SBRT.


??? note "Abstract"
    To quantitatively assess target and organs-at-risk (OAR) dose rate based on three proposed proton PBS dose rate metrics and study FLASH intensity-modulated proton therapy (IMPT) treatment planning using transmission beams. An in-house FLASH planning platform was developed to optimize transmission (shoot-through) plans for nine consecutive lung cancer patients previously planned with proton SBRT. Dose and dose rate calculation codes were developed to quantify three types of dose rate calculation methods (dose-averaged dose rate (DADR), average dose rate (ADR), and dose-threshold dose rate (DTDR)) based on both phantom and patient treatment plans. Two different minimum MU/spot settings were used to optimize two different dose regimes, 34-Gy in one fraction and 45-Gy in three fractions. The OAR sparing and target coverage can be optimized with good uniformity (hotspot &lt; 110% of prescription dose). ADR, accounting for the spot dwelling and scanning time, gives the lowest dose rate; DTDR, not considering this time but a dose-threshold, gives an intermediate dose rate, whereas DADR gives the highest dose rate without considering any time or dose-threshold. All three dose rates attenuate along the beam direction, and the highest dose rate regions often occur on the field edge for ADR and DTDR, whereas DADR has a better dose rate uniformity. The differences in dose rate metrics have led a large variation for OARs dose rate assessment, posing challenges to FLASH clinical implementation. This is the first attempt to study the impact of the dose rate models, and more investigations and evidence for the details of proton PBS FLASH parameters are needed to explore the correlation between FLASH efficacy and the dose rate metrics.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/34298762/) · [DOI](https://doi.org/10.3390/cancers13143549) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8303986/)


---

### SDDRO-joint: simultaneous dose and dose rate optimization with the joint use of transmission beams and Bragg peaks for FLASH proton therapy.

*Lin Y, Lin B, Fu S, Folkerts MM, Abel E, Bradley J et al.* — Physics in medicine and biology (2021)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span>


**TL;DR.** Cancer radiotherapy (RT) with the irradiation at ultra-high dose rates, namely FLASH-RT, can substantially reduce radiation-induced normal tissue toxicities while maintaining tumor response. Currently, clinical FLASH-RT on deep-seated tumors can only be performed with proton beams.


??? note "Abstract"
    Cancer radiotherapy (RT) with the irradiation at ultra-high dose rates, namely FLASH-RT, can substantially reduce radiation-induced normal tissue toxicities while maintaining tumor response. Currently, clinical FLASH-RT on deep-seated tumors can only be performed with proton beams. One way to achieve ultra-high dose rates at depth is through the use of high-energy transmission beams (TB), where the Bragg peaks (BP) fall outside the body. However, planning with TB alone does not fully leverage the degrees of freedom for dose shaping as traditional intensity modulated proton therapy (IMPT) which uses the BP of multi-energy proton beams at the tumor target. This work will develop a simultaneous dose and dose rate optimization (SDDRO) method with the joint use of TB and BP, namely SDDRO-Joint. Specifically, BP are placed inside tumor targets to improve the target dose conformality and sparse the normal-tissue dose, while TB primarily cover the tumor boundary to achieve ultra-high dose rate coverage of organs-at-risk (OAR) close to tumor targets. The sparing of OAR and other normal tissues via SDDRO-Joint is jointly by TB and BP, i.e. the FLASH sparing by TB and the dose sparing by BP. The results suggest that the addition of BP substantially increased the target dose conformality for SDDRO. Noticeably SDDRO-Joint also provided slightly higher conformal index values than the conventional IMPT method with BP alone.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/34010818/) · [DOI](https://doi.org/10.1088/1361-6560/ac02d8) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9288107/)


---

### Ultra-High Dose Rate Transmission Beam Proton Therapy for Conventionally Fractionated Head and Neck Cancer: Treatment Planning and Dose Rate Distributions.

*van Marlen P, Dahele M, Folkerts M, Abel E, Slotman BJ, Verbakel W* — Cancers (2021)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Beam Delivery &amp; Technology</span>


**TL;DR.** Transmission beam (TB) proton therapy (PT) uses single, high energy beams with Bragg-peak behind the target, sharp penumbras and simplified planning/delivery. TB facilitates ultra-high dose-rates (UHDRs, e.g., ≥40 Gy/s), which is a requirement for the FLASH-effect.


??? note "Abstract"
    Transmission beam (TB) proton therapy (PT) uses single, high energy beams with Bragg-peak behind the target, sharp penumbras and simplified planning/delivery. TB facilitates ultra-high dose-rates (UHDRs, e.g., ≥40 Gy/s), which is a requirement for the FLASH-effect. We investigated (1) plan quality for conventionally-fractionated head-and-neck cancer treatment using spot-scanning proton TBs, intensity-modulated PT (IMPT) and photon volumetric-modulated arc therapy (VMAT); (2) UHDR-metrics. VMAT, 3-field IMPT and 10-field TB-plans, delivering 70/54.25 Gy in 35 fractions to boost/elective volumes, were compared (n = 10 patients). To increase spot peak dose-rates (SPDRs), TB-plans were split into three subplans, with varying spot monitor units and different gantry currents. Average TB-plan organs-at-risk (OAR) sparing was comparable to IMPT: mean oral cavity/body dose were 4.1/2.5 Gy higher (9.3/2.0 Gy lower than VMAT); most other OAR mean doses differed by &lt;2 Gy. Average percentage of dose delivered at UHDRs was 46%/12% for split/non-split TB-plans and mean dose-averaged dose-rate 46/21 Gy/s. Average total beam-on irradiation time was 1.9/3.8 s for split/non-split plans and overall time including scanning 8.9/7.6 s. Conventionally-fractionated proton TB-plans achieved comparable OAR-sparing to IMPT and better than VMAT, with total beam-on irradiation times &lt;10s. If a FLASH-effect can be demonstrated at conventional dose/fraction, this would further improve plan quality and TB-protons would be a suitable delivery system.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/33924627/) · [DOI](https://doi.org/10.3390/cancers13081859) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8070061/)


---

### High quality proton portal imaging using deep learning for proton radiation therapy: a phantom study.

*Charyyev S, Lei Y, Harms J, Eaton B, McDonald M, Curran WJ et al.* — Biomedical physics &amp; engineering express (2020)  

<span class="badge oa">Open access</span> <span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Modeling &amp; Mechanisms</span>


**TL;DR.** Purpose; For shoot-through proton treatments, like FLASH radiotherapy, there will be protons exiting the patient which can be used for proton portal imaging (PPI), revealing valuable information for the validation of tumor location in the beam&#x27;s-eye-view at native gantry angles. However, PPI has poor inherent contrast and spatial resolution.


??? note "Abstract"
    Purpose; For shoot-through proton treatments, like FLASH radiotherapy, there will be protons exiting the patient which can be used for proton portal imaging (PPI), revealing valuable information for the validation of tumor location in the beam&#x27;s-eye-view at native gantry angles. However, PPI has poor inherent contrast and spatial resolution. To deal with this issue, we propose a deep-learning-based method to use kV digitally reconstructed radiographs (DRR) to improve PPI image quality. Method; We used a residual generative adversarial network (GAN) framework to learn the nonlinear mapping between PPIs and DRRs. Residual blocks were used to force the model to focus on the structural differences between DRR and PPI. To assess the accuracy of our method, we used 149 images for training and 30 images for testing. PPIs were acquired using a double-scattered proton beam. The DRRs acquired from CT acted as learning targets in the training process and were used to evaluate results from the proposed method using a six-fold cross-validation scheme. Results; Qualitatively, the corrected PPIs showed enhanced spatial resolution and captured fine details present in the DRRs that are missed in the PPIs. The quantitative results for corrected PPIs show average normalized mean error (NME), normalized mean absolute error (NMAE), peak signal-to-noise ratio (PSNR) and structural similarity (SSIM) index of -0.1%, 0.3%, 39.14 dB, and 0.987, respectively. Conclusion; The results indicate the proposed method can generate high quality corrected PPIs and this work shows the potential to use a deep-learning model to make PPI available in proton radiotherapy. This will allow for beam&#x27;s-eye-view (BEV) imaging with the particle used for treatment, leading to a valuable alternative to orthogonal x-rays or cone-beam CT for patient position verification.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/33438674/) · [DOI](https://doi.org/10.1088/2057-1976/ab8a74) · [Full text (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11682722/)


---

### Simultaneous dose and dose rate optimization (SDDRO) for FLASH proton therapy.

*Gao H, Lin B, Lin Y, Fu S, Langen K, Liu T et al.* — Medical physics (2020)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span>


**TL;DR.** FLASH radiotherapy (RT) can potentially reduce normal tissue toxicity while preserving tumoricidal effectiveness to improve the therapeutic ratio. The key of FLASH for sparing normal tissues is to irradiate tissues with an ultra-high dose rate (i.e., ≥40 Gy/s), for which proton RT can be used.


??? note "Abstract"
    PURPOSE: FLASH radiotherapy (RT) can potentially reduce normal tissue toxicity while preserving tumoricidal effectiveness to improve the therapeutic ratio. The key of FLASH for sparing normal tissues is to irradiate tissues with an ultra-high dose rate (i.e., ≥40 Gy/s), for which proton RT can be used. However, currently available treatment plan optimization method only optimizes the dose distribution and does not directly optimize the dose rate. The contribution of this work to FLASH proton RT is the development of a novel treatment optimization method, that is, simultaneous dose and dose rate optimization (SDDRO), to optimize tissue-receiving dose rate distribution as well as dose distribution. METHODS: Distinguished from existing methods, SDDRO accounts for dose rate constraint and optimizes dose rate distribution. In terms of mathematical formulation, SDDRO is a constrained optimization problem with dose-volume constraint on dose distribution, minimum dose rate constraint on dose-averaged tissue-receiving dose rates, minimum monitor unit constraint on spot weight, and maximum intensity constraint on beam intensity. In terms of optimization algorithm, SDDRO is solved by iterative convex relaxation and alternating direction method of multipliers. SDDRO algorithms are presented for both scenarios with either constant or variable beam intensity. RESULTS: SDDRO was compared with intensity modulated proton therapy (IMPT) (dose optimization alone, and no dose rate optimization) using three lung cases. SDDRO substantially improved the dose rate distribution compared to IMPT, for example, increasing of the region-of-interest (ROI) volume (ROI = CTV_10mm: the ring sandwiched by 10 mm outer and inner expansion of CTV boundary) receiving at least 40 Gy/s from ~30-50% to at least 98%, and the lung volume receiving at least 40 Gy/s from ~30-40% to ~70-90%. Moreover, both dose and dose rate distributions from SDDRO were further considerably improved via the combined use of hypofractionation and multiple beams. CONCLUSIONS: We have developed a joint dose and dose rate optimization method for FLASH proton RT, namely SDDRO, which is first-of-its-kind to the best of our knowledge. The results suggest that (a) SDDRO can substantially improve the FLASH-dose rate coverage (e.g., in terms of dose rate volume histogram) compared to IMPT for the purpose of normal tissue sparing while preserving the dose distribution and (b) the combination of hypofractionation and multiple beams can further considerably improve the SDDRO plan quality in terms of both dose and dose rate distribution.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/33068294/) · [DOI](https://doi.org/10.1002/mp.14531)


---

### Bringing FLASH to the Clinic: Treatment Planning Considerations for Ultrahigh Dose-Rate Proton Beams.

*van Marlen P, Dahele M, Folkerts M, Abel E, Slotman BJ, Verbakel WFAR* — International journal of radiation oncology, biology, physics (2020)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Physics &amp; Dosimetry</span> <span class="badge tag">Radiobiology</span>


**TL;DR.** Preclinical research into ultrahigh dose rate (eg, ≥40 Gy/s) &quot;FLASH&quot;-radiation therapy suggests a decrease in side effects compared with conventional irradiation while maintaining tumor control. When FLASH is delivered using a scanning proton beam, tissue becomes subject to a spatially dependent range of dose rates.


??? note "Abstract"
    PURPOSE: Preclinical research into ultrahigh dose rate (eg, ≥40 Gy/s) &quot;FLASH&quot;-radiation therapy suggests a decrease in side effects compared with conventional irradiation while maintaining tumor control. When FLASH is delivered using a scanning proton beam, tissue becomes subject to a spatially dependent range of dose rates. This study systematically investigates dose rate distributions and delivery times for proton FLASH plans using stereotactic lung irradiation as the paradigm. METHODS AND MATERIALS: Stereotactic lung radiation therapy FLASH-plans, using 244 MeV scanning proton transmission beams, with the Bragg peak behind the body, were made for 7 patients. Evaluated parameters were dose rate distribution within a beam, overall irradiation time, number of times tissue is irradiated, and quality of the FLASH-plans compared with the clinical volumetric-modulated arc therapy (VMAT) plans. RESULTS: Sparing of lungs, thoracic wall, and heart in the FLASH-plans was equal to or better than that in the VMAT-plans. For a spot peak dose rate (SPDR, the dose rate in the middle of the spot) of 100 Gy/s, ∼40% of dose is delivered at FLASH dose rates, and for SPDR = 360 Gy/s this increased to ∼75%. One-hundred percent FLASH dose rate cannot be achieved owing to small contributions from distant spots with lower dose rates. The total irradiation time varied between 300 to 730 ms, and around 85% of the dose-receiving body volume was irradiated by either 1 or 2 beams. CONCLUSIONS: Clinical implementation of FLASH using scanning proton beams requires multiple treatment planning considerations: dosimetric, temporal, and spatial parameters all seem important. The FLASH efficiency of a scanning proton beam increases with SPDR. The methodology proposed in this proof-of-principle study provides a framework for evaluating the FLASH characteristics of scanning proton beam plans and can be adapted as FLASH parameters are better defined. It currently seems logical to optimize plans for the shortest delivery time, maximum amount of high dose rate coverage, and maximum amount of single beam and continuous irradiation.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/31759074/) · [DOI](https://doi.org/10.1016/j.ijrobp.2019.11.011)


---

### Towards FLASH proton therapy: the impact of treatment planning and machine characteristics on achievable dose rates.

*van de Water S, Safai S, Schippers JM, Weber DC, Lomax AJ* — Acta oncologica (Stockholm, Sweden) (2019)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Modeling &amp; Mechanisms</span> <span class="badge tag">Clinical &amp; Translational</span>


**TL;DR.** This study aimed at evaluating spatially varying instantaneous dose rates for different intensity-modulated proton therapy (IMPT) planning strategies and delivery scenarios, and comparing these with FLASH dose rates (&gt;40 Gy/s). Material and methods: In order to quantify dose rates in three-dimensions, we proposed the &#x27;dose-averaged dose rate&#x27; (DADR) metric, defined for each voxel as the dose-weigh…


??? note "Abstract"
    Background: This study aimed at evaluating spatially varying instantaneous dose rates for different intensity-modulated proton therapy (IMPT) planning strategies and delivery scenarios, and comparing these with FLASH dose rates (&gt;40 Gy/s). Material and methods: In order to quantify dose rates in three-dimensions, we proposed the &#x27;dose-averaged dose rate&#x27; (DADR) metric, defined for each voxel as the dose-weighted mean of the instantaneous dose rates of all spots (i.e., pencil beams). This concept was applied to four head-and-neck cases, each planned with clinical (4 fields) and various spot-reduced IMPT techniques: &#x27;standard&#x27; (4 fields), &#x27;arc&#x27; (120 fields) and &#x27;arc-shoot-through&#x27; (120 fields; 229 MeV only). For all plans, different delivery scenarios were simulated: constant beam intensity, variable beam intensity for a clinical Varian ProBeam system, varied per energy layer or per spot, and theoretical spot-wise variable beam intensity (i.e., no monitor/safety limitations). DADR distributions were calculated assuming 2-Gy or 6-Gy fractions. Results: Spot-reduced plans contained 17-52 times fewer spots than clinical plans, with no deterioration of plan quality. For the clinical plans, the mean DADR in normal tissue for 2-Gy fractionation was 1.7 Gy/s (median over all patients) at maximum, whereas in standard spot-reduced plans it was 0.7, 4.4, 7.1, and 12.1 Gy/s, for the constant, energy-layer-wise, spot-wise, and theoretical spot-wise delivery scenarios, respectively. Similar values were observed for arc plans. Arc-shoot-through planning resulted in DADR values of 3.0, 6.0, 14.1, and 24.4 Gy/s, for the abovementioned scenarios. Hypofractionation (3×) generally resulted in higher dose rates, up to 73.2 Gy/s for arc-shoot-through plans. The DADR was inhomogeneously distributed with highest values at beam entrance and at the Bragg peak. Conclusion: FLASH dose rates were not achieved for conventional planning and clinical spot-scanning machines. As such, increased spot-wise beam intensities, spot-reduced planning, hypofractionation and arc-shoot-through plans were required to achieve FLASH compatible dose rates.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/31241377/) · [DOI](https://doi.org/10.1080/0284186X.2019.1627416)


---

### Radiotherapy treatment planning of prostate cancer using magnetic resonance imaging alone.

*Lee YK, Bollet M, Charles-Edwards G, Flower MA, Leach MO, McNair H et al.* — Radiotherapy and oncology : journal of the European Society for Therapeutic Radiology and Oncology (2003)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Clinical &amp; Translational</span>


**TL;DR.** Accurate anatomical delineation of the gross tumour volume (GTV) is crucial for effective radiotherapy (RT) treatment of prostate cancers. Although reference to pelvic magnetic resonance (MR) for improved delineation of the prostate is a regular practice in some clinics, MR has not replaced CT due to its geometrical distortions and lack of electron-density information.


??? note "Abstract"
    PURPOSE: Accurate anatomical delineation of the gross tumour volume (GTV) is crucial for effective radiotherapy (RT) treatment of prostate cancers. Although reference to pelvic magnetic resonance (MR) for improved delineation of the prostate is a regular practice in some clinics, MR has not replaced CT due to its geometrical distortions and lack of electron-density information. The possibility and practicality of using MR only for RT treatment planning were studied. MATERIALS AND METHODS: The addition of electron-density information to MR images for conformal radiotherapy (CRT) planning of the prostate was quantified by comparing dose distributions created on the homogeneous density- and bulk-density assigned images to original CT for four patients. To quantify the MR geometrical distortions measurements of a phantom imaged in CT (Siemens Somatom Plus 4) and FLASH 3D T1-weighted MR (1.5 T whole body Siemens Magnetom Vision) were compared. Dose statistics from CRT treatment plans made on CT and MR for five patient data were compared to determine if MR-only treatment plans can be made. RESULTS: The differences between dose-plans on bulk-density assigned images when compared to CT were less than 2% when water and bone values were assigned. Dose differences greater than 2% were observed when images of homogeneous-density assignment were compared to the CT. Phantom measurements showed that the distortions in the FLASH 3D T1-weighted MR averaged 2 mm in the volume of interest for prostate RT planning. For the CT and MR prostate planning study, doses delivered to the planning target volume (PTV) in CT and MR were always inside a 93-107% dose range normalised to the isocentre. Also, the doses to the organs-at-risk in the MR images were similar to the doses delivered to the volumes in the registered CT image when the organ volumes between the two images were similar. CONCLUSIONS: Negligible differences were observed in dose distribution between CRT plans using bone+water CT number bulk-assigned image and original CT. Also, the MR distortions were reduced to negligible amounts using large bandwidth MR sequence for prostate CRT planning. MR treatment planning was demonstrated using a large bandwidth sequence and bulk-assigned images. The development of higher quality, low distortion MR sequence will allow regular practice of this technique.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/12648793/) · [DOI](https://doi.org/10.1016/s0167-8140(02)00440-1)


---

### Optimized treatment planning for prostate cancer comparing IMPT, VHEET and 15 MV IMXT.

*Yeboah C, Sandison GA* — Physics in medicine and biology (2002)  

<span class="badge tag">Treatment Planning &amp; Optimization</span> <span class="badge tag">Radiobiology</span> <span class="badge tag">Beam Delivery &amp; Technology</span>


**TL;DR.** The merits of intensity-modulated very-high energy electron therapy (VHEET) and intensity-modulated proton therapy (IMPT) in relation to intensity-modulated x-ray therapy (IMXT) with respect to the treatment of the prostate have been quantified. Optimized dose distributions were designed for 5-11 beams of 250 MeV VHEET and 15 MV IMXT as well as 1-9 beam ports of IMPT.


??? note "Abstract"
    The merits of intensity-modulated very-high energy electron therapy (VHEET) and intensity-modulated proton therapy (IMPT) in relation to intensity-modulated x-ray therapy (IMXT) with respect to the treatment of the prostate have been quantified. Optimized dose distributions were designed for 5-11 beams of 250 MeV VHEET and 15 MV IMXT as well as 1-9 beam ports of IMPT. In the case of the comparison between 250 MeV VHEET and 15 MV IMXT, it was found that the quality of target coverage achievable with VHEET was comparable to or sometimes better than that provided by IMXT. However, VHEET provided an improvement over IMXT in the dose sparing of the sensitive structures and normal tissues. Compared to IMXT, VHEET decreased the mean rectal dose and bladder dose by up to 10% of the prescribed target dose, while reducing by up to 12% of the prescribed target dose the integral dose to normal tissues. In quantifying the merits of IMPT relative to IMXT, it was found that using intensity-modulated proton beams for inverse planning instead of intensity-modulated photon beams improved target dose homogeneity by up to 1.3% of the prescribed target dose, while reducing the mean rectal dose, bladder dose, and normal tissue integral dose by up to 27%, 30% and 28% of the prescribed target dose respectively. The comparison of optimized planning for IMPT and VHEET showed that the quality of target coverage achievable with IMPT is comparable to or better (by up to 1.3% of the prescribed target dose) than that provided by VHEET. Compared to VHEET, IMPT delivered a mean rectal dose and a bladder dose that was lower by up to 17% and 23% of prescribed target dose respectively, and also reduced the integral dose to normal tissues by up to 17% of the prescribed target dose. These results indicate that of the three modalities the greatest dose escalation will be possible with IMPT, then VHEET, and then IMXT. It follows that IMPT will result in the highest probability of complication-free tumour control, while IMXT will provide the lowest probability.


[PubMed](https://pubmed.ncbi.nlm.nih.gov/12164585/) · [DOI](https://doi.org/10.1088/0031-9155/47/13/305)


---
