import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import uuid
from datetime import datetime, timedelta

np.random.seed(42)
# --- 1. ПІДКЛЮЧЕННЯ ДО DWH (PostgreSQL) ---
db_url = 'postgresql://postgres:123456789@localhost:5432/social_discovery_dwh'
engine = create_engine(db_url)
print("✅ Підключення до бази успішне!")

# --- 2. EXTRACT & TRANSFORM ---
NUM_USERS = 50000
NUM_EVENTS = 2000000 

print("Генерація користувачів...")
dates = pd.date_range(start="2025-01-01", end="2025-06-30")

probs = [2.0 if d.month == 2 else 1.0 for d in dates]
probs = np.array(probs) / sum(probs)

# Використовуємо UUID замість чисел і додаємо різноманітність статей
users_data = {
    'user_id': [str(uuid.uuid4()) for _ in range(NUM_USERS)],
    'age': np.random.randint(18, 50, size=NUM_USERS),
    'gender': np.random.choice(
        ['Male', 'Female', 'Non-binary', 'Genderfluid', 'Transgender', 'Prefer Not to Say'], 
        size=NUM_USERS, 
        p=[0.45, 0.40, 0.05, 0.03, 0.02, 0.05]
    ),
    'country': np.random.choice(['Urban', 'Suburban', 'Rural', 'Metro', 'Small Town', 'Remote Area'], size=NUM_USERS),
    'registration_date': np.random.choice(dates, size=NUM_USERS, p=probs)
}
df_users = pd.DataFrame(users_data)

print("Генерація подій (Експоненційний розподіл активності)...")
# Продуктові типи подій
event_types = ['swipe_left', 'swipe_right', 'match', 'message_sent']
# 80% - відмови (ліворуч), 18.5% - інтерес (праворуч), 1.1% - взаємність (метч), 0.4% - початок діалогу
event_probs = [0.800, 0.185, 0.011, 0.004] 

events_data = {
    'event_id': [str(uuid.uuid4()) for _ in range(NUM_EVENTS)],
    'user_id': np.random.choice(df_users['user_id'], size=NUM_EVENTS),
    'event_type': np.random.choice(event_types, size=NUM_EVENTS, p=event_probs)
}
df_events = pd.DataFrame(events_data)

# Головна магія: додаємо експоненційний спад
days_offset = np.clip(np.random.exponential(scale=3.0, size=NUM_EVENTS), 0, 30).astype(int)

# Прив'язуємо події до дати реєстрації юзера + зміщення в днях
user_reg_dates = df_users.set_index('user_id')['registration_date']
df_events['event_date'] = df_events['user_id'].map(user_reg_dates) + pd.to_timedelta(days_offset, unit='D')


# --- 3. GENERATE: Транзакції (Логічна монетизація) ---
print("💰 Генеруємо розумні покупки Premium-підписок...")
transactions_data = []

# Визначаємо рівень залученості юзерів (використовуємо множини (set) для швидкості)
chatted_users = set(df_events[df_events['event_type'] == 'message_sent']['user_id'])
matched_users = set(df_events[df_events['event_type'] == 'match']['user_id'])

paying_user_ids = []

for uid in df_users['user_id']:
    if uid in chatted_users:
        prob = 0.20 # 20% конверсія для тих, хто спілкується
    elif uid in matched_users:
        prob = 0.05 # 5% конверсія для тих, хто має метчі, але мовчить
    else:
        prob = 0.01 # 1% для "сліпих" свайперів (купують, щоб побачити свої лайки)
        
    if np.random.rand() < prob:
        paying_user_ids.append(uid)

paying_users = df_users[df_users['user_id'].isin(paying_user_ids)]

for idx, row in paying_users.iterrows():
    tx_date = row['registration_date'] + timedelta(days=np.random.randint(0, 7), minutes=np.random.randint(0, 1440))
    transactions_data.append({
        'transaction_id': str(uuid.uuid4()),
        'user_id': row['user_id'],
        'subscription_type': np.random.choice(['Weekly', 'Monthly'], p=[0.7, 0.3]),
        'amount': np.random.choice([4.99, 14.99], p=[0.7, 0.3]),
        'transaction_date': tx_date
    })

df_tx = pd.DataFrame(transactions_data)


# --- 4. LOAD: Відправка в базу даних ---
print("⏳ Завантаження даних у PostgreSQL (це може зайняти хвилину)...")

df_users.to_sql('dim_users', engine, if_exists='replace', index=False)
print(f"✅ Таблиця юзерів ({len(df_users)} рядків) завантажена!")

# Використовуємо chunksize для швидшого завантаження великих масивів
df_events.to_sql('fact_events', engine, if_exists='replace', index=False, chunksize=50000)
print(f"✅ Таблиця подій ({len(df_events)} рядків) завантажена!")

df_tx.to_sql('fact_transactions', engine, if_exists='replace', index=False)
print(f"✅ Таблиця транзакцій ({len(df_tx)} оплат) завантажена!")

print("🚀 ETL ПАЙПЛАЙН УСПІШНО ЗАВЕРШЕНО!")