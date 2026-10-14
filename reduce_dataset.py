import pandas as pd
import sys
import os

# Ayarlar
chunk_size = 100000
# Orijinal 8GB veriyi ~475MB seviyesine indirmek için tabakalı örnekleme oranı (%6.25)
sample_fraction = 0.0625
input_file = os.path.join("archive", "all_tweets_hashed.csv")
output_file = os.path.join("archive", "troll_lens_subset.csv")

header_written = False

print(f"{input_file} dosyası {chunk_size} satırlık parçalar halinde işlenmeye başlanıyor...")
print(f"Tabakalı (stratified) örnekleme oranı: {sample_fraction}")

try:
    # Veriyi parça parça oku
    for i, chunk in enumerate(pd.read_csv(input_file, chunksize=chunk_size, lineterminator='\n', low_memory=False)):
        
        # info_op sütunu üzerinden tabakalı örnekleme işlemi
        if 'info_op' in chunk.columns:
            # Eksik verileri filtreleyelim
            chunk = chunk.dropna(subset=['info_op'])
            
            # info_op dağılımını koruyarak örneklem al
            sampled_chunk = chunk.groupby('info_op', group_keys=False).apply(lambda x: x.sample(frac=sample_fraction, random_state=42))
        else:
            # Fallback (eğer info_op yoksa rastgele örneklem)
            sampled_chunk = chunk.sample(frac=sample_fraction, random_state=42)
            
        # Alt küme verisini yeni dosyaya yaz
        sampled_chunk.to_csv(output_file, mode='a', index=False, header=not header_written)
        header_written = True
        
        # Süreç hakkında bilgi ver
        if i % 10 == 0:
            print(f"{i}. parça işlendi...")

    print("Veri küçültme işlemi tamamlandı! Alt küme şuraya kaydedildi:", output_file)

except Exception as e:
    print("Bir hata oluştu:", e)
    sys.exit(1)
