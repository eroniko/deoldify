#from deoldify.visualize import *
#import os
#
## Modeli yükleme
#colorizer = get_stable_image_colorizer(artistic=False)
#
## Görüntüyü renklendirme
#input_folder = 'img/'
#output_folder = 'result/'
#render_factor = 35  # Bu değer, renklendirme yoğunluğunu kontrol eder. Değer arttıkça renkler daha doygun hale gelir.
#
## Görüntüyü renklendir ve kaydet
#for i, filename in enumerate(os.listdir(input_folder)):
#    if filename.endswith(".jpg") or filename.endswith(".png"): # Sadece .jpg ve .png dosyalarını işler
#        input_path = os.path.join(input_folder, filename)
#        output_path = os.path.join(output_folder, f'colorized_test_{i}{os.path.splitext(filename)[1]}')
#        colorized_image = colorizer.get_transformed_image(path=input_path, render_factor=render_factor)
#        colorized_image.save(output_path)
#        print(f"Renklendirilmiş görüntü {output_path} konumuna kaydedildi.")


from deoldify.visualize import *
import os

# Modeli yükleme
colorizer = get_artistic_image_colorizer(render_factor=21)

# Görüntüyü renklendirme
input_folder = 'img/'
output_folder = 'result/'
render_factor = 35  # Bu değer, renklendirme yoğunluğunu kontrol eder. Değer arttıkça renkler daha doygun hale gelir.

# Görüntüyü renklendir ve kaydet
for i, filename in enumerate(os.listdir(input_folder)):
    if filename.endswith(".jpg") or filename.endswith(".png"): # Sadece .jpg ve .png dosyalarını işler
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f'colorized_test_{i}{os.path.splitext(filename)[1]}')
        colorized_image = colorizer.get_transformed_image(path=input_path, render_factor=render_factor)
        colorized_image.save(output_path)
        print(f"Renklendirilmiş görüntü {output_path} konumuna kaydedildi.")
