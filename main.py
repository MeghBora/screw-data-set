from icrawler.builtin import GoogleImageCrawler
import os

output_folder = "screw_images"
os.makedirs(output_folder, exist_ok=True)

# Screw types to search for
screw_types = [
    "flathead screw", "phillips screw", "hex screw", "torx screw",
    "carriage bolt", "lag bolt", "flange bolt",
    "hex nut", "wing nut", "lock nut",
    "flat washer", "lock washer", "spring washer",
    "blind rivet", "solid rivet", "tubular rivet",
    "cotter pin", "dowel pin", "split pin"
]

for screw in screw_types:
    screw_folder = os.path.join(output_folder, screw.replace(" ", "_"))
    os.makedirs(screw_folder, exist_ok=True)

    crawler = GoogleImageCrawler(storage={"root_dir": screw_folder})
    crawler.crawl(keyword=screw, max_num=200)

    print(f"✅ Downloaded {screw} images in {screw_folder}")
        # ✅ Resize images to 100x100
    for img_file in os.listdir(screw_folder):
        img_path = os.path.join(screw_folder, img_file)
        try:
            img = Image.open(img_path)
            img = img.resize((100, 100))  # Resize to 100x100
            img.save(img_path)
        except Exception as e:
            print(f"❌ Skipping {img_file}: {e}")

print("🎉 Image collection complete!")

