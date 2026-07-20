## Smartphone Addiction Across Generations: An Analysis of Usage Pattern and Mental Health

### Project Overview
This project investigates the relationship between daily smartphone usage, addiction levels, sleep
habits, and health outcomes across two datasets: a teen-focused survey of 3,000 students and a
broader mobile addiction dataset of 3,000 respondents spanning multiple countries, occupations,
and age groups. By combining these sources into a unified relational database, the analysis aims
to identify patterns that are consistent across different age groups.

#### Data Sources 

**Dataset 1 : Teen Screentime usage and Addiction impact (3000 rows in CSV format)**   
Source: Kaggle.com – dataset uploaded by Sumedh Patil
Link : https://www.kaggle.com/datasets/sumedh1507/teen-phone-addiction

Key Fields: Age, Gender, Daily Usage hours, Addiction level, Sleep hours, Academic performance, Anxiety level, Time on Social media, Time on Gaming, Exercise hours performance, Anxiety level, Time on Social media, Time on Gaming, Exercise hours

**Dataset 2: Global Mobile Addiction (3000 rows in CSV format)**       
Source: Kaggle.com – dataset uploaded by Khushi Yadav
Link: https://www.kaggle.com/datasets/khushikyad001/global-mobile-phone-addiction-dataset

Key Fields: Age, Gender, Daily Screentime hours, Social Media Usage hours, Gaming Usage hours,Streaming Usage hours, Sleep hours, Physical Activity hours, Mental Health Score, Depression Score, Anxiety Score, Self-reported addiction level


### Repo Structure 

```

├── Data/
│   ├── teen_screentime_addiction.csv
│   └── global_mobile_addiction.csv
├── Notebook/
│   ├── teen_screentime_addiction.ipynb
│   ├── global_mobile_addiction.ipynb
│   └── merged_analysis.ipynb
├── functions.py              ← shared functions live here
├── requirements.txt
└── README.md

```

### Tech Stack

- Python 3
- pandas, numpy
- matplotlib, seaborn
- Jupyter Notebook


### How to Use

1. Clone [this repository](https://github.com/shivahari04/smartphone_addiction_analysis).
2. Install the required Python packages:  
   pip install -r requirements.txt
3. Open Notebook folder


### Description

This dataset focuses on understanding the patterns and effects of smartphone usage among teenagers, with a special focus on:

Addiction Levels    
Academic performance    
Daily Usage Hours        
Sleep Hours        
Time distribution (social media, gaming, education)      
Mental and Physical Health  


**Research Questions**

1. Can Addiction level impact Academic performance?
2. Will Higher phone usage impacts academic performance?
3. Can lack of sleep impact academic performance?

**Key Findings** 

***Daily usage is the strongest predictor of addiction*** — a correlation of **0.60** was found between daily usage hours and addiction level, the strongest relationship in the entire dataset     
***Addiction rises steeply with usage*** — addiction level climbs from ~4–5 (out of 10) at low usage, plateauing at the maximum score of 10 beyond 8 hours of daily use   
***Sleep has a weak negative effect on addiction*** — a correlation of **-0.22** suggests more sleep is slightly associated with lower addiction, but the relationship is too weak to draw firm conclusions  
***Academic performance shows no significant relationship*** with either addiction level or sleep hours — scores remained consistently between 70–80 regardless of usage or sleep patterns   
***Usage is normally distributed*** — most students use their phones for around 5 hours per day, with the majority falling in the 3–8 hour range   

**Visualizations**

| Chart | Type |
|:-------:|:------:|
| Daily Usage vs Addiction Level | Line chart | 
| Sleep Hours vs Academic Performance | Line chart | 
| Addiction Level vs Academic Performance | Scatter plot |
| Daily Usage Distribution | Histogram |
| Correlation Matrix | Heatmap |


**Limitations**

- Dataset source is unclear and may be synthetic
- No demographic data (race, ethnicity, socioeconomic status) limits generalization
- Self-reported addiction scores may be subjective



*This project was developed with the assistance of Claude AI as a guided learning tool — used for understanding Python concepts and troubleshooting.*


### Author
  **Sivakami Visvanathan (Shiva)** — *Aspiring Data Analyst*

