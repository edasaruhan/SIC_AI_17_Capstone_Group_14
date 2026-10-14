import pandas as pd
import numpy as np
import os
import sys
import time
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score,
    roc_curve,
    accuracy_score,
    f1_score
)
from lightgbm import LGBMClassifier

def main():
    print("=" * 60)
    print("   TrollLens - Makine Öğrenmesi Model Eğitimi (LightGBM)   ")
    print("=" * 60)

    # 1. Veri Setini Yükleme
    data_path = os.path.join("archive", "troll_lens_subset.csv")
    if not os.path.exists(data_path):
        print(f"HATA: Veri dosyası bulunamadı: {data_path}")
        sys.exit(1)

    print(f"\n[1/6] Veri seti yükleniyor: {data_path}")
    start_time = time.time()
    df = pd.read_csv(data_path, low_memory=False)
    print(f"  -> {len(df):,} satır başarıyla yüklendi ({time.time() - start_time:.2f} saniye).")

    # 2. Veri Temizliği (Data Cleaning)
    print("\n[2/6] Veri temizliği yapılıyor...")
    # Sayısal sütunlardaki eksik değerleri 0 ile doldur
    num_cols = ['quote_count', 'like_count', 'retweet_count', 'hashtags', 'urls', 'user_mentions']
    for col in num_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # is_retweet sütununu 0/1 integer'a çevir
    if 'is_retweet' in df.columns:
        df['is_retweet'] = df['is_retweet'].astype(int)

    # Tarih sütununu datetime yap
    df['tweet_time'] = pd.to_datetime(df['tweet_time'], errors='coerce')
    df = df.dropna(subset=['tweet_time', 'info_op'])
    df['info_op'] = df['info_op'].astype(int)

    # 3. Özellik Mühendisliği (Feature Engineering)
    print("\n[3/6] Özellik mühendisliği uygulanıyor...")
    
    # Zaman bazlı davranış özellikleri (Davranışsal imza)
    df['hour'] = df['tweet_time'].dt.hour
    df['day_of_week'] = df['tweet_time'].dt.dayofweek
    df['is_weekend'] = (df['day_of_week'] >= 5).astype(int)

    # Günün zaman dilimi: 1: Sabah (05-11), 2: Öğle (12-16), 3: Akşam (17-21), 4: Gece (22-04)
    def time_period(h):
        if 5 <= h < 12:
            return 1
        elif 12 <= h < 17:
            return 2
        elif 17 <= h < 22:
            return 3
        else:
            return 4

    df['time_of_day'] = df['hour'].apply(time_period)

    # Toplam etkileşim metrikleri
    df['total_engagement'] = df['like_count'] + df['retweet_count'] + df['quote_count']
    
    # Oran bazlı davranışsal özellikler
    df['retweet_to_like_ratio'] = df['retweet_count'] / (df['like_count'] + 1.0)
    df['tags_and_urls'] = df['hashtags'] + df['urls']

    feature_cols = [
        'is_retweet', 'quote_count', 'like_count', 'retweet_count',
        'hashtags', 'urls', 'user_mentions', 'hour', 'day_of_week',
        'is_weekend', 'time_of_day', 'total_engagement',
        'retweet_to_like_ratio', 'tags_and_urls'
    ]

    X = df[feature_cols]
    y = df['info_op']

    print(f"  -> Kullanılan özellikler ({len(feature_cols)} adet): {feature_cols}")
    print(f"  -> Sınıf Dağılımı: Organik (0) = {(y == 0).sum():,}, Troll (1) = {(y == 1).sum():,}")

    # 4. Eğitim ve Test Kümelerine Ayırma (Train-Test Split)
    print("\n[4/6] Veri seti %80 Eğitim, %20 Test olarak ayrılıyor (Stratified Split)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"  -> Eğitim Kümesi: {len(X_train):,} örnek")
    print(f"  -> Test Kümesi  : {len(X_test):,} örnek")

    # 5. Model Eğitimi (Model Training)
    print("\n[5/6] Model (LightGBM Classifier) eğitiliyor...")
    model = LGBMClassifier(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=7,
        num_leaves=63,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        n_jobs=-1,
        verbose=-1
    )

    t0 = time.time()
    model.fit(X_train, y_train)
    train_duration = time.time() - t0
    print(f"  -> Eğitim tamamlandı! Geçen süre: {train_duration:.2f} saniye.")

    # 6. Model Değerlendirme (Evaluation)
    print("\n[6/6] Model performansı test kümesi üzerinde değerlendiriliyor...")
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]

    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_pred_proba)

    print("\n" + "=" * 50)
    print("           MODEL TEST SONUÇLARI           ")
    print("=" * 50)
    print(f"  * Doğruluk (Accuracy) : %{acc * 100:.2f}")
    print(f"  * F1-Score            : %{f1 * 100:.2f}")
    print(f"  * ROC-AUC Skoru       : %{auc * 100:.2f}")
    print("-" * 50)
    print("\nSınıflandırma Raporu (Classification Report):\n")
    print(classification_report(y_test, y_pred, target_names=['Organik (0)', 'Troll (1)']))

    # Grafikleri oluşturup kaydetme
    os.makedirs("results", exist_ok=True)
    sns.set_theme(style="whitegrid")

    # A) Karmaşıklık Matrisi (Confusion Matrix)
    plt.figure(figsize=(6, 5))
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['Organik', 'Troll'],
                yticklabels=['Organik', 'Troll'])
    plt.title('TrollLens - Karmaşıklık Matrisi (Confusion Matrix)')
    plt.ylabel('Gerçek Sınıf')
    plt.xlabel('Tahmin Edilen Sınıf')
    plt.tight_layout()
    cm_path = os.path.join("results", "confusion_matrix.png")
    plt.savefig(cm_path, dpi=300)
    plt.close()
    print(f"  [+] Karmaşıklık Matrisi kaydedildi: {cm_path}")

    # B) ROC Eğrisi (ROC Curve)
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    plt.figure(figsize=(7, 5))
    plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC Eğrisi (AUC = {auc:.3f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate (Yanlış Pozitif Oranı)')
    plt.ylabel('True Positive Rate (Doğru Pozitif Oranı)')
    plt.title('TrollLens - ROC Eğrisi')
    plt.legend(loc="lower right")
    plt.tight_layout()
    roc_path = os.path.join("results", "roc_curve.png")
    plt.savefig(roc_path, dpi=300)
    plt.close()
    print(f"  [+] ROC Eğrisi kaydedildi: {roc_path}")

    # C) Özellik Önem Düzeyleri (Feature Importance)
    plt.figure(figsize=(10, 6))
    importance = pd.Series(model.feature_importances_, index=feature_cols).sort_values(ascending=True)
    importance.plot(kind='barh', color='teal')
    plt.title('TrollLens - Hangi Özellikler Troll Tespitinde En Etkili?')
    plt.xlabel('Önem Puanı (Feature Importance)')
    plt.tight_layout()
    fi_path = os.path.join("results", "feature_importance.png")
    plt.savefig(fi_path, dpi=300)
    plt.close()
    print(f"  [+] Özellik Önem Grafiği kaydedildi: {fi_path}")

    # Modeli diske kaydetme
    model_save_path = os.path.join("results", "troll_lens_model.pkl")
    joblib.dump(model, model_save_path)
    print(f"  [+] Eğitilmiş model kaydedildi: {model_save_path}")

    print("\n" + "=" * 60)
    print("Model eğitimi ve değerlendirmesi başarıyla tamamlandı!")
    print("Ödev raporunuz için gerekli tüm grafikler 'results/' klasörüne kaydedildi.")
    print("=" * 60)

if __name__ == "__main__":
    main()
