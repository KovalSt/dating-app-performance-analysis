# 📊 Dating App Performance Analysis & Anomaly Detection

📥 **[Dating_dashboard.pdf](https://github.com/user-attachments/files/29648485/Dating_dashboard.pdf)**

## 🎥 Dashboard Demo
*https://github.com/user-attachments/assets/7af72bde-4731-4535-a089-06e0e18557e8*

## 🎯 Business Context & Project Objective
This project analyzes the user behavior, conversion funnels, and retention metrics of a mobile dating application (dataset: 50,000 unique users). The primary goal is to evaluate product engagement, identify critical churn points, and detect behavioral anomalies to provide actionable data-driven recommendations for the Product and Anti-Fraud teams.

## 🖼️ Dashboard Previews
*<img width="1272" height="713" alt="Screenshot 2026-07-03 205159" src="https://github.com/user-attachments/assets/69812516-be9c-4280-91ca-2063d5c1c223" />
<img width="1274" height="714" alt="Screenshot 2026-07-03 205136" src="https://github.com/user-attachments/assets/5b11ee5b-6e9f-48eb-a975-d0e359fc9276" />
<img width="1281" height="715" alt="Screenshot 2026-07-03 204932" src="https://github.com/user-attachments/assets/61306dca-6eeb-48e8-a327-8e4b47d96473" />*

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
