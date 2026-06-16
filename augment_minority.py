import os
import random
from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps

def augment_minority_class(target_dir, num_desired=145):

    target_path = Path(target_dir)
    
    # pega apenas as imagens originais
    original_images = [f for f in target_path.iterdir() if f.is_file() and not f.name.startswith("aug_")]
        
    current_count = len(original_images)
    
    needed = num_desired - current_count
    
    if needed <= 0:
        return
        
    print(f"Gerando {needed} novas imagens sintéticas...")

    # transformações possíveis
    def apply_random_transform(img):
        # espelhamento horizontal
        if random.random() > 0.5:
            img = ImageOps.mirror(img)
            
        # rotação leve (-15 a 15 graus)
        angle = random.uniform(-15, 15)
        img = img.rotate(angle, resample=Image.BILINEAR)
        
        # brilho aleatório (0.8x a 1.2x)
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(random.uniform(0.8, 1.2))
        
        # contraste aleatório (0.8x a 1.2x)
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(random.uniform(0.8, 1.2))
        
        return img

    for i in range(needed):
        # escolhe uma imagem original aleatória para servir de base
        base_img_path = random.choice(original_images)
        try:
            with Image.open(base_img_path) as img:
                # converte para rgb
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                    
                aug_img = apply_random_transform(img)
                
                # salva a nova imagem
                new_name = f"aug_{i:04d}_{base_img_path.name}"
                aug_img.save(target_path / new_name, format="JPEG", quality=90)
        except Exception as e:
            print(f"Erro ao processar {base_img_path.name}: {e}")
            
    print(f"A pasta '{target_path.name}' agora tem {num_desired} imagens.")

if __name__ == '__main__':
    PASTA_MINORITARIA_TREINO = "/home/marv/Documentos/laydown_cls_dataset/train/com_laydown"

    augment_minority_class(PASTA_MINORITARIA_TREINO, num_desired=116)
