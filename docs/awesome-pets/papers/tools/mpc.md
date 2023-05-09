# Secure Multi-Party Computation (MPC)

![](https://badgen.net/badge/:update-to/:Apr-2023/red) ![](https://badgen.net/badge/:papers/:48/blue) 

> "The design of scure protocols that implement arbitrarily desired functionalities is a major part of mordern cryptography."
> -- Foundation of Cryptography, Volumn 2, Oded Goldreich. 

MPC has evolved from a theoretical curiosity in the 1980s to a tool for building real systems today. Over the past decade, MPC has been one of the most active research areas in both theoretical and applied cryptography. In the following, we try to show the newest and interesting advances in mpc (both theory & applicaiton), and also the infulential papers in history. 

Note: one paper may be included in several categories (e.g. a paper may introduce a new protocol for both OT and VOLE, we decide to include it in both categories).

## Table of Contents

- [offline-techniques](#offline-techniques)
  * [ot](#oblivious-transfer) : oblivious transfer
  * [vole](#vector-oblivious-linear-evaluation): (subfield) (vector) oblivious linear evaluation
  * [pcg](#pseudorandom-correlation-generator): pseudorandom correlation generator
- [online-techniques](#online-techniques)
  * [semi-honest secret sharing](#semi-honest-secret-sharing)
  * [malicious secret sharing](#malicious-secret-sharing)

## Offline Techniques

### Oblivious transfer
- Endemic Oblivious Transfer via Random Oracles, Revisited  
  *Zhelei Zhou, Bingsheng Zhang, Hong-Sheng Zhou, Kui Ren*  
  EuroCrypt 2023, [eprint](https://eprint.iacr.org/2022/1525), ZZZR23  

- SoftSpokenOT: Quieter OT Extension from Small-Field Silent VOLE in the Minicrypt Model  
  *Lawrence Roy*  
  Crypto 2022, [eprint](https://eprint.iacr.org/2022/192), Roy22

- Silver: Silent VOLE and Oblivious Transfer from Hardness of Decoding Structured LDPC Codes  
  *Geoffroy Couteau, Peter Rindal, Srinivasan Raghuraman*  
  Crypto 2021, [eprint](https://eprint.iacr.org/2021/1150), CRR21

- The Rise of Paillier: Homomorphic Secret Sharing and Public-Key Silent OT  
  *Claudio Orlandi, Peter Scholl, Sophia Yakoubov*  
  EuroCrypt 2021, [eprint](https://eprint.iacr.org/2021/262), OSY21

- Batching Base Oblivious Transfers  
  *Ian McQuoid, Mike Rosulek, Lawrence Roy*  
  AsiaCrypt 2021, [eprint](https://eprint.iacr.org/2021/682), MRR21

- Efficient and Round-Optimal Oblivious Transfer and Commitment with Adaptive Security  
  *Ran Canetti, Pratik Sarkar, Xiao Wang*  
  AsiaCrypt 2020, [eprint](https://eprint.iacr.org/2020/545), CSW20  

- Efficient Two-Round OT Extension and Silent Non-Interactive Secure Computation  
  *Elette Boyle, Geoffroy Couteau, Niv Gilboa, Yuval Ishai, Lisa Kohl, Peter Rindal, Peter Scholl*  
  CCS 2019, [eprint](https://eprint.iacr.org/2019/1159), BCGI+19 (with Peter Rindal)
  
- Endemic Oblivious Transfer  
  *Daniel Masny, Peter Rindal*  
  CCS 2019, [eprint](https://eprint.iacr.org/2019/706), MR19 
  
- Efficient Pseudorandom Correlation Generators: Silent OT Extension and More  
  *Elette Boyle, Geoffroy Couteau, Niv Gilboa, Yuval Ishai, Lisa Kohl, Peter Scholl*  
  Crypto 2019, [eprint](https://eprint.iacr.org/2019/448), BCGI+19 (without Peter Rindal)

- Equational Security Proofs of Oblivious Transfer Protocols
  *Baiyu Li, Daniele Micciancio*  
  PKC 2018, [eprint](https://eprint.iacr.org/2016/624), LM18  

- Actively Secure 1-out-of-N OT Extension with Application to Private Set Intersection  
  *Michele Orrù, Emmanuela Orsini, Peter Scholl*  
  CT-RSA 2017, [eprint](https://eprint.iacr.org/2016/933), OOS17

- Actively Secure OT Extension with Optimal Overhead  
  *Marcel Keller, Emmanuela Orsini, Peter Scholl*  
  Crypto 2015, [eprint](https://eprint.iacr.org/2015/546), KOS15
  
- The Simplest Protocol for Oblivious Transfer  
  *Tung Chou, Claudio Orlandi*  
  LatinCrypt 2015, [eprint](https://eprint.iacr.org/2015/267), CO15
  
- More Efficient Oblivious Transfer and Extensions for Faster Secure Computation  
  *Gilad Asharov, Yehuda Lindell, Thomas Schneider, Michael Zohner*  
  CCS 2013, [eprint](https://eprint.iacr.org/2013/552), ALSZ13
  
- A Framework for Efficient and Composable Oblivious Transfer  
  *Chris Peikert, Vinod Vaikuntanathan, Brent Waters*  
  Crypto 2008, [eprint](https://eprint.iacr.org/2007/348), PVW08  

- Extending Oblivious Transfers Efficiently  
  *Yuval Ishai, Joe Kilian, Kobbi Nissim, Erez Petrank*  
  Crypto 2003, [eprint](https://www.iacr.org/archive/crypto2003/27290145/27290145.pdf), IKNP03

- Oblivious Transfer and Polynomial Evaluation  
  *Moni Naor, Benny Pinkas*  
  STOC 1999, [eprint](https://dl.acm.org/doi/pdf/10.1145/301250.301312), NP99

### vector Oblivious Linear Evaluation
- Actively Secure Arithmetic Computation and VOLE with Constant Computational Overhead  
  *Benny Applebaum, Niv Konstantini*  
  EuroCrypt 2023, [eprint](https://eprint.iacr.org/2023/270), AK23  

- Two-Round Oblivious Linear Evaluation from Learning with Errors  
	*Pedro Branco, Nico Do ̈ttling, Paulo Mateus*  
	PKC 2022, [eprint](https://eprint.iacr.org/2020/635), BDM22

- Correlated Pseudorandomness from Expand-Accumulate Codes  
	*Elette Boyle, Geoffroy Couteau, Niv Gilboa, Yuval Ishai, Lisa Kohl, Nicolas Resch, Peter Scholl*  
	Crypto 2022, [eprint](https://eprint.iacr.org/2022/1014), BCG+22
	
- Silver: Silent VOLE and Oblivious Transfer from Hardness of Decoding Structured LDPC Codes  
  *Geoffroy Couteau, Peter Rindal, Srinivasan Raghuraman*  
  Crypto 2021, [eprint](https://eprint.iacr.org/2021/1150), CRR21
  
- Two-Round Oblivious Linear Evaluation from Learning with Errors  
  *Pedro Branco, Nico Döttling, Paulo Mateus*  
  PKC 2022, [eprint](https://eprint.iacr.org/2020/635), BDM20
  
- Efficient Protocols for Oblivious Linear Function Evaluation from Ring-LWE  
  *Carsten Baum, Daniel Escudero, Alberto Pedrouzo-Ulloa, Peter Scholl, Juan Ramón Troncoso-Pastoriza*  
  SCN 2020, [eprint](https://eprint.iacr.org/2020/970), BEPS+20
  
- Distributed vector-OLE: Improved constructions and implementation  
  *Phillipp Schoppmann, Adrià Gascón, Leonie Reichert, Mariana Raykova*  
  CCS 2019, [eprint](https://eprint.iacr.org/2019/1084), SGRR19
  
- Compressing vector OLE  
  *Elette Boyle, Geoffroy Couteau, Niv Gilboa, Yuval Ishai*  
  CCS 2018, [eprint](https://eprint.iacr.org/2019/273), BCGI18
  
- Secure Arithmetic Computation with Constant Computational Overhead  
  *Benny Applebaum, Ivan Damgård, Yuval Ishai, Michael Nielsen, Lior Zichron*  
  Crypto 2017, [eprint](https://eprint.iacr.org/2017/617), ADI+17  

- Maliciously secure oblivious linear function evaluation with constant overhead  
  *Satrajit Ghosh, Jesper Buus Nielsen, Tobias Nilges*  
  AsiaCrypt 2017, [eprint](https://eprint.iacr.org/2017/409), GNN17
  
- TinyOLE: Efficient actively secure two-party computation from oblivious linear function evaluation, 2017,   
  *Nico Döttling, Satrajit Ghosh, Jesper Buus Nielsen, Tobias Nilges, Roberto Trifiletti*  
  CCS 2017, [eprint](https://eprint.iacr.org/2017/790), DGNN+17
  
- Oblivious Transfer and Polynomial Evaluation  
  *Moni Naor, Benny Pinkas*  
  STOC 1999, [eprint](https://dl.acm.org/doi/pdf/10.1145/301250.301312), NP99
  

### Pseudorandom-Correlation Generator

- Correlated Pseudorandomness from Expand-Accumulate Codes  
  *Elette Boyle, Geoffroy Couteau, Niv Gilboa, Yuval Ishai, Lisa Kohl, Nicolas Resch, Peter Scholl*  
  Crypto 2022, [eprint](https://eprint.iacr.org/2022/1014), BCG+22

## Online Techniques

### Semi-Honest Secret Sharing

- ABY2.0: Improved Mixed-Protocol Secure Two-Party Computation  
  *Arpita Patra, Thomas Schneider, Ajith Suresh, Hossein Yalame*  
  Usenix Security 2021, [eprint](https://eprint.iacr.org/2020/1225), PSSY21

- MP-SPDZ: A Versatile Framework for Multi-Party Computation  
  *Marcel Keller*  
  CCS 2020, [eprint](https://eprint.iacr.org/2020/521), Kel20

- ABY3: A Mixed Protocol Framework for Machine Learning  
  *Payman Mohassel, Peter Rindal*  
  CCS 2018, [eprint](https://eprint.iacr.org/2018/403), MR18

- ABY - A Framework for Efficient Mixed-Protocol Secure Two-Party Computation  
  *Daniel Demmler, Thomas Schneider, Michael Zohner*  
  NDSS 2017, [eprint](https://www.ndss-symposium.org/wp-content/uploads/2017/09/08_2_1.pdf), DSZ17

- Secure Computation with Fixed-Point Numbers  
  *Octavian Catrina, Amitabh Saxena*  
  FC 2010, [eprint](https://ifca.ai/pub/fc10/31_47.pdf), CS10

- The Round Complexity of Secure Protocols  
  *Donald Beaver, Silvio Micali, Phillip Rogaway*  
  STOC 1990, [eprint](http://web.cs.ucdavis.edu/~rogaway/papers/bmr90), BMR90
  
- Completeness Theorems for Non-Cryptographic Fault Tolerant Distributed Computation  
  *Michael Ben-Or, Shafi Goldwasser, Avi Wigderson*  
  STOC 1988, [eprint](https://dl.acm.org/doi/10.1145/62212.62213), BGW88

- How to play any mental game?  
  *Oded Goldreich, Silvio Micali, Avi Wigderson*  
  STOC 1987, [eprint](https://dl.acm.org/doi/10.1145/28395.28420), GMW87
  
- How to generate and exchange secrets?  
  *Andrew Chi-Chih Yao*  
  FOCS 1986, [eprint](https://ieeexplore.ieee.org/document/4568207), Yao86

### Malicious Secret Sharing

- MHz2k: MPC from HE over Z2k with New Packing, Simpler Reshare, and Better ZKP  
  *Jung Hee Cheon, Dongwoo Kim, and Keewoo Lee*  
  Crypto 2021, [eprint](https://eprint.iacr.org/2021/1383), CKL21

- High-Performance Multi-party Computation for Binary Circuits Based on Oblivious Transfer  
  *Sai Sheshank Burra, Enrique Larraia, Jesper Buus Nielsen, Peter Sebastian Nordholt, Claudio Orlandi, Emmanuela Orsini, Peter Scholl, Nigel P. Smart*  
  JCryptpo 2021, [eprint](https://eprint.iacr.org/2015/472), BLNN+21

- Overdrive2k: Efficient Secure MPC over Z2k from Somewhat Homomorphic Encryption  
  *Emmanuela Orsini, Nigel P. Smart, Frederik Vercauteren*  
  CT-RSA 2020, [eprint](https://eprint.iacr.org/2019/153), OSV20

- MonZ2k: Fast Maliciously Secure Two Party Computation on Z2k  
  *Dario Catalano, Mario Di Raimondo, Dario Fiore, and Irene Giacomelli*  
  PKC 2020, [eprint](https://eprint.iacr.org/2019/211), CRFG20

- Covert Security with Public Verifiability: Faster, Leaner, and Simpler  
  *Cheng Hong, Jonathan Katz, Vladimir Kolesnikov, Wen-jie Lu, Xiao Wang*  
  EuroCrypt 2019, [eprint](https://eprint.iacr.org/2018/1108), HKKL+19

- Two-Thirds Honest-Majority MPC for Malicious Adversaries at Almost the Cost of Semi-Honest  
  *Jun Furukawa, Yehuda Lindell*  
  CCS 2019, [eprint](https://eprint.iacr.org/2019/658), FL19

- Communication Lower Bounds for Statistically Secure MPC, With or Without Preprocessing  
  *Ivan Damgård, Kasper Green Larsen, Jesper Buus Nielsen*  
  Crypto 2019, [eprint](https://eprint.iacr.org/2019/220), DLN19

- New Primitives for Actively-Secure MPC over Rings with Applications to Private Machine Learning  
  *Ivan Damgård, Daniel Escudero, Tore Frederiksen, Marcel Keller, Peter Scholl, Nikolaj Volgushev*  
  SP 2019, [eprint](https://eprint.iacr.org/2019/599), DEFK+19

- Adaptively Secure MPC with Sublinear Communication Complexity  
  *Ran Cohen, Abhi Shelat, Daniel Wichs*  
  Crypto 2019, [eprint](https://eprint.iacr.org/2018/1161), CSW19 