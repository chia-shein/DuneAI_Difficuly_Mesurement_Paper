# DuneAI_Difficuly_Mesurement_Paper
## Descriptions
This code is for a paper published based on [DuneAI model](https://github.com/primakov/DuneAI-Automated-detection-and-segmentation-of-non-small-cell-lung-cancer-computed-tomography-images), which [paper](https://www.nature.com/articles/s41467-022-30841-3) was published in Nature Communications.
## Running Device: (Platform: [TWCC](https://www.twcc.ai/))
* **Hardware Details:**\
CPU:　Intel® Xeon® Platinum 8280L 28 Cores 2.7GHz.\
Mem: ECC DDR4 2933 Mhz.\
GPU: NVIDIA V100.

* 1 GPU + 04 cores + 090GB memory.
## Example Datasets
* Paper provide 3 test patients with NSCLC case from NSCLC-Radiomics-Interobserver1.
  Manual **Segmentations** in **nrrd format**.
## NIH data download details
1. Download first:
     * NBIA Data Retriever-[window version](https://cbiit-download.nci.nih.gov/nbia/releases/ForTCIA/NBIADataRetriever_4.4/NBIA%20Data%20Retriever-4.4.msi).
     * [NSCLC-RADIOMICS-INTEROBSERVER1-Aug-31-2020-NBIA-manifest](https://www.cancerimagingarchive.net/wp-content/uploads/NSCLC-RADIOMICS-INTEROBSERVER1-Aug-31-2020-NBIA-manifest.tcia) TCIA file.
## Requirements
Docker Image: tensorflow-24.08-tf2-py3:latest.
```console
u5453836@bechl2ctr1733907726803-rsl4p:~$ pip install -r requirements.txt
u5453836@bechl2ctr1733907726803-rsl4p:~$
```
## Implement steps:
1. Image pre-processing
2. Tumor Segmentation
3. Results
## Code's modify details


