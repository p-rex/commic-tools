import os
import argparse
from PIL import Image

def split_image(image_path, output_dir):
    # 画像を開く
    img = Image.open(image_path)
    width, height = img.size

    # 画像を左右に分割
    left_image = img.crop((0, 0, width // 2, height))
    right_image = img.crop((width // 2, 0, width, height))

    # 画像ファイル名の取得
    base_name = os.path.basename(image_path)
    file_name, ext = os.path.splitext(base_name)

    # 出力ファイルのパス
    left_image_path = os.path.join(output_dir, f"{file_name}_2{ext}")
    right_image_path = os.path.join(output_dir, f"{file_name}_1{ext}")

    # 左右の画像を保存
    left_image.save(left_image_path)
    right_image.save(right_image_path)

    print(f"Saved: {left_image_path}, {right_image_path}")

def process_images(input_dir, output_dir):
    # 出力ディレクトリが存在しない場合は作成
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 入力ディレクトリ内のJPEGファイルを処理
    for file_name in sorted(os.listdir(input_dir)):
        if file_name.endswith(".jpg"):
            image_path = os.path.join(input_dir, file_name)
            split_image(image_path, output_dir)

def main():
    # コマンドライン引数の解析
    parser = argparse.ArgumentParser(description="画像を左右に分割するスクリプト")
    parser.add_argument("input_dir", help="画像が保存されているディレクトリのパス")
    parser.add_argument("output_dir", help="分割後の画像を保存するディレクトリのパス")

    args = parser.parse_args()

    # 引数からディレクトリのパスを取得
    input_dir = args.input_dir
    output_dir = args.output_dir

    # 画像を処理
    process_images(input_dir, output_dir)

if __name__ == "__main__":
    main()
