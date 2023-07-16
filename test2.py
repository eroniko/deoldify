from deoldify.visualize import *

# Modeli yükleme
colorizer = get_image_colorizer(artistic=False)

# Görüntüyü renklendirme
input_path = 'test.jpg'
output_path = 'colorized_test.jpg'
render_factor = 35  # Bu değer, renklendirme yoğunluğunu kontrol eder. Değer arttıkça renkler daha doygun hale gelir.

# Görüntüyü renklendir ve kaydet
colorized_image = colorizer.get_transformed_image(path=input_path, render_factor=render_factor)
colorized_image.save(output_path)

print(f"Renklendirilmiş görüntü {output_path} konumuna kaydedildi.")
