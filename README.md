# PRNU_Device_Recognition

## Goal:
The aim of this project is to develop a system for identifying the origin of photos among five different devices, utilizing Photo Response Non-Uniformity (PRNU) as a distinguishing factor.

## Instructions:
1. **Download the Dataset**: Obtain the dataset from [this link](https://rb.gy/5v8jdf).

2. **Navigate to the Digital Folder**: Go to the `/digital` directory.

3. **Run the Script**: Execute the script `movephoto.py`.
   
    ```bash
    python movephoto.py
    ```

4. **Generate CSV File**: Run the script `makecsv.py`.
   
    ```bash
    python makecsv.py
    ```

5. **Calculate PRNU Accuracy**: Execute the script `prnuaccuracy.py`.
   
    ```bash
    python prnuaccuracy.py
    ```

6. **Recognize photo by PRNU**: Run the script `prnurecognize.py`.
   
    ```bash
    python prnurecognize.py
    ```

## Acknowledgments:
Special thanks to [lesc.dinfo.unifi.it](https://lesc.dinfo.unifi.it/materials/datasets/) for providing the Vision dataset. For this project, only data from five devices are utilized. All downloadable materials are sourced from this website.

### information
This project was developed for the Digital Forensics course at the University of Catania. It may contain errors or imperfections.

## Citation:
If you use the code in this repository, please consider citing:

[Bertolami Carmelo], [Student], [Unict], [01/06/2024].
