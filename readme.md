# Imagining Reality - Hackathon Submission

## Team Details

**Team Name:** Imagining Reality  
**Team Members:** Aryan Bains, Shivani, Prabhdeep Singh Narula, Muskan Kaur  

## Project Overview

This project optimizes real-time bidding (RTB) by predicting Click-Through Rate (CTR), Conversion Rate (CVR), and market prices to maximize advertiser ROI.

### Key Insights from Exploratory Data Analysis (EDA):
- CTR (0.01–0.2%) and CVR (<0.1%) vary by time, region, and ad slot visibility.
- FirstView slots had **3× higher CTR** compared to others.
- Time-based trends showed **higher CTR during evenings (6–10 PM)**.
- Budget distribution imbalance: **70% of the spend came from 3/5 advertisers**.

### Model Selection & Optimization:
- **CTR Prediction:** Logistic Regression (speed + interpretability) with TF-IDF for User-Agent text.
- **CVR Prediction:** LightGBM (handles class imbalance via focal loss) with feature importance pruning.
- **Paying Price Prediction:** Linear Regression using AdslotFloorPrice, AdExchange, and historical bid averages.
- **Hyperparameter Tuning:** Bayesian Optimization for LightGBM; L1/L2 regularization for Logistic Regression.

### Evaluation & Results:
- **Score Improvement:** +28% vs. fixed bidding, +15% vs. CTR-only.
- **Budget Utilization:** Achieved **99% spend** with adaptive thresholds.
- **Latency:** Avg. **3.2ms/bid** (under the 5ms real-time constraint).
- **CTR Model AUC:** 0.72; **CVR Model AUC:** 0.68.

## Instructions to Run the Code

### Installation

#### Prerequisites
- Python **3.8+**
- pip (Python package manager)
- Virtual environment (recommended)

#### Install Dependencies
```sh
pip install -r requirements.txt
```

### Usage

#### 1. Prepare the Dataset
Ensure dataset files are placed inside the `python/data/` directory.

#### 2. Run the Main Script
```sh
cd bidder/submission/code/python
python main.py
```

#### 3. Model Training (Optional)
If training from scratch is needed:
```sh
python model.py
```

#### 4. Evaluate the Model
```sh
python evaluate.py
```

## Troubleshooting

### Module Import Errors
If you encounter `ModuleNotFoundError`, ensure you're running the script from the correct directory:
```sh
cd bidder/submission/code/python
python main.py
```

If the issue persists, manually add the project path in `main.py`:
```python
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
```

## Description of the Approach

### 1. Exploratory Data Analysis (EDA)
- Analyzed **bid, impression, click, and conversion logs** to identify patterns.
- Found CTR (0.01–0.2%) and CVR (<0.1%) vary by **AdvertiserID, Region, and AdslotVisibility**.
- Sparse conversions required **stratified sampling**.
- **FirstView ad slots** had 3× higher CTR than others.
- **City-level trends** influenced conversions for specific campaigns (e.g., Tire).

### 2. Feature Engineering
- Extracted **hour/day** from timestamps.
- Parsed **User-Agent** into device type (mobile/desktop) and OS.
- Created historical aggregates:
  - **CTR per Domain**
  - **CVR per Region**
  - **Avg. PayingPrice per AdslotID**
- Encoded hashed URL/Domain via **frequency encoding**.
- Derived **AdslotArea (width × height)** and combined it with AdslotFloorPrice.
- **Bid-to-market price ratio (BiddingPrice/PayingPrice)** to avoid overbidding.
- **Dimensionality reduction via PCA** for sparse features.

### 3. Model Selection
- **CTR Prediction:** Logistic Regression with TF-IDF for User-Agent text.
- **CVR Prediction:** LightGBM (with focal loss to handle class imbalance).
- **Paying Price Prediction:** Linear Regression using AdslotFloorPrice, Adexchange, and historical bid averages.
- **Neural Networks were rejected due to high latency constraints.**

### 4. Hyperparameter Tuning
- **Logistic Regression:** Grid-searched L1/L2 regularization and class weights.
- **LightGBM:** Bayesian Optimization for `num_leaves=32`, `learning_rate=0.05`, `min_data_in_leaf=100`.
- **Linear Regression:** Lasso regularization (`alpha=0.1`) to reduce multicollinearity.
- Used **5-fold time-series cross-validation** to prevent data leakage.

### 5. Evaluation Strategy
- **Primary Metric:** Score = Clicks + N × Conversions (per advertiser).
- **Secondary Metrics:**
  - Budget utilization (%)
  - Execution time/bid (<5ms)
  - AUC-ROC (CTR/CVR models)
- **Validation:** Time-based split (train: June–Nov, test: Dec).
- **Baseline Comparisons:**
  - **Fixed Bidding:** Constant bid price.
  - **CTR-Only:** Bid proportional to CTR.
- **Simulated real-time auctions** using historical logs to track budget spend and score.

### 6. Validation Results
- **Score Improvement:** +28% vs. fixed bidding, +15% vs. CTR-only.
- **Budget Utilization:** **99% spend** achieved with adaptive thresholds.
- **Latency:** **3.2ms/bid** (below the 5ms constraint).
- **CTR Model AUC:** 0.72
- **CVR Model AUC:** 0.68 (despite sparse conversions).
- **FirstView ad slots** contributed **42% of total clicks**.
- **Campaigns with N>0 (Tire, Software) saw 2.1× higher score gains** vs. N=0 campaigns.

## Additional Information

### Tech Stack
- **Languages & Libraries:** Python, NumPy, pandas, LightGBM, Matplotlib, Bayesian Optimization.
- **Data Sources:** Bid request logs, click/conversion logs, ad slot details.

### Key Challenges & Solutions
- **Handling extreme class imbalance** in CVR prediction → Used **focal loss** in LightGBM.
- **Optimizing latency** to ensure real-time bidding feasibility → Used **Logistic Regression & Linear Regression**.
- **Feature selection & encoding efficiency** → Applied **frequency encoding & PCA**.

## Contact
For any queries, feel free to reach out to the team members.

---
**Team Imagining Reality**  
_Hackathon Submission_
