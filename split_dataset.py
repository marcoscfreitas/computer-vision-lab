import os
import shutil
import random
from pathlib import Path

def split_dataset(source_dir, output_dir, train_ratio=0.8):

    source_path = Path(source_dir)
    output_path = Path(output_dir)
    
    # cria as pastas train e val
    train_dir = output_path / 'train'
    val_dir = output_path / 'val'
    
    # define as classes
    allowed_classes = ['com_laydown', 'sem_laydown']
    classes = [d for d in source_path.iterdir() if d.is_dir() and d.name in allowed_classes]

    for class_dir in classes:
        class_name = class_dir.name
        
        # cria as pastas da classe dentro de train e val
        (train_dir / class_name).mkdir(parents=True, exist_ok=True)
        (val_dir / class_name).mkdir(parents=True, exist_ok=True)
        
        # pega todas as imagens dessa classe
        images = [f for f in class_dir.iterdir() if f.is_file() and f.suffix.lower() in ['.jpg', '.jpeg', '.png']]
            
        # ordena as imagens pelo nome
        images.sort()
        
        # calcula onde cortar a lista para separar treino e validação
        split_index = int(len(images) * train_ratio)
        
        train_images = images[:split_index]
        val_images = images[split_index:]
        
        # copia os arquivos para a pasta de treino
        for img in train_images:
            shutil.copy2(img, train_dir / class_name / img.name)
            
        # copia os arquivos para a pasta de validação
        for img in val_images:
            shutil.copy2(img, val_dir / class_name / img.name)
            
        print(f"Classe '{class_name}': {len(train_images)} imagens para treino, {len(val_images)} imagens para validação.")
        
if __name__ == '__main__':
    PASTA_ORIGEM = "/home/marv/Documentos/imagens_separadas" 
    PASTA_DESTINO = "/home/marv/Documentos/laydown_cls_dataset" 
    
    split_dataset(PASTA_ORIGEM, PASTA_DESTINO, train_ratio=0.8)
