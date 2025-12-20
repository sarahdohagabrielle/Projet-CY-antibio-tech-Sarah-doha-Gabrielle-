## Overview

This project analyzes microbiome data from mice. It reads CSV files containing bacterial counts from different sample types (fecal, cecal, ileal) and generates plots and CSV outputs for each type.

---

## Features

* Reads CSV data automatically, detects delimiters (`;` or `,`)
* Processes fecal data and generates line plots over time
* Processes cecal and ileal and generates violin plots to compare Placebo vs ABX treatments
* Saves filtered data in CSV files
* Creates all necessary folders automatically

---

## Project Structure

```text
project/
│
├── main.py              # Main execution script
├── input/               # Folder for input CSV files
├── output/              # Folder where CSV outputs are saved
└── images/              # Folder where plots are saved
```

---


## CSV File Format

Your CSV should include :

* `mouse_ID` → unique identifier for each mouse
* `sample_type` → type of sample (`fecal`, `cecal`, `ileal`)
* `treatment` → treatment applied (`Placebo` or `ABX`)
* `experimental_day` → day of the experiment (integer)
* `counts_live_bacteria_per_wet_g` → bacterial count

> Example:

```csv
mouse_ID;sample_type;treatment;experimental_day;counts_live_bacteria_per_wet_g
M1;fecal;ABX;1;12000
M2;cecal;Placebo;1;8000
```

### What happens when you run it:

1. The program checks and creates necessary folders (`output/`, `images/`)
2. It will reads the input CSV file
3. Generates:

   * Fecal line plot and CSV
   * Cecal violin plot and CSV
   * Ileal violin plot and CSV
4. Saves outputs in `output/` and `images/`

---
## notes and limitations

* The script does not handle missing values or wrong rows. 

* The input must strictly follow the schema as described

* Case Sensitivity: "Placebo" is different from "placebo"
