# 📊 Dating App Performance Analysis & Anomaly Detection

## 🎯 Business Context & Project Objective
This project analyzes the user behavior, conversion funnels, and retention metrics of a mobile dating application (dataset: 50,000 unique users). The primary goal is to evaluate product engagement, identify critical churn points, and detect behavioral anomalies to provide actionable data-driven recommendations for the Product and Anti-Fraud teams.

## 🔍 Key Product Insights

* **Monetization & Stable Conversion (Executive Summary):** The app generated **$19,880** in revenue with an ARPU of **$0.40**. Despite seasonal volume fluctuations, the core algorithmic engagement remains highly stable across the first half of the year: `Swipe Right Rate` holds at ~19%, `Match Rate` at ~6%, and post-match `Message Rate` peaks at ~35%.
* **Critical Retention Drop-off (Funnel & Heatmaps):** The User Retention Heatmap reveals a steep drop-off between Day 5 and Day 10. While baseline retention on Day 7 is ~66%, the deep-dive cohort analysis shows that **Core Value Retention** is much lower: Match Retention drops to ~1.3% and Message Retention drops to ~0.4% by Day 7. Users remain in the app but transition into "passive swipers" without generating meaningful interactions.
* **The February Seasonal Anomaly (Anti-Fraud & Risk):** A massive spike in user activity was detected in February 2025. Drill-through analysis isolated the cause: a 100% surge in negative actions (`swipe_left` jumped from ~7.5K to ~15K daily). While total matches proportionally increased, messaging volume remained completely flat. This indicates a massive influx of low-intent users or potential bot activity typical for the Valentine's Day season.

## 💡 Actionable Recommendations

* **Optimize the Day-5 Onboarding Experience:** Implement targeted push notifications, gamification, or temporary premium features (e.g., "Free Super Likes") specifically on Day 5 and Day 6 to stimulate active messaging and flatten the critical Day 10 churn curve.
* **Adjust Seasonal Acquisition Strategy:** The February data proves that high-volume seasonal traffic strains the system (2x server load from left-swipes) without converting into active chats or revenue. Marketing should shift focus from "volume of registrations" to "profile completion quality" during peak seasons.
* **Implement Anti-Fraud Velocity Limits:** The unnatural flat plateau of 15K+ daily left-swipes in February strongly suggests automated scraping or bot activity. The Risk Management team should deploy dynamic velocity limits (e.g., maximum swipe limits per hour for non-premium accounts) to protect the ecosystem.

## 🛠 Technical Stack & Implementation

* **Tool:** Microsoft Power BI
* **Data Modeling:** Star schema implementation with a centralized Date Table.
* **DAX Engineering:** Developed custom measures for dynamic cohort analysis, retention heatmaps, and velocity tracking.
* **UX/UI Design:** Implemented seamless Page Navigation and Drill-through functionalities to allow stakeholders to transition intuitively from high-level Executive KPIs to granular daily behavioral trends.