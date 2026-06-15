from ultralytics import YOLO
import torch
import yaml

if __name__ == '__main__':
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

    caminho_yaml = "datasets/containers_dataset/data.yaml"

    with open(caminho_yaml, 'r') as f :
        dados = yaml.safe_load(f)

    dados['path'] = "datasets/containers_dataset"
    dados['train'] = "train/images"
    dados['val'] = "valid/images"

    with open(caminho_yaml, 'w') as f:
        yaml.dump(dados, f)


    modelo = YOLO("yolo26n.pt")

    modelo.train(
        device      = DEVICE,
        data        = "datasets/containers_dataset/data.yaml",
        epochs      = 50,
        imgsz       = 416,
        batch       = 16,
        workers     = 4,
        patience    = 15,
        optimizer   = "AdamW",
        lr0         = 0.001,
        cache       = True,
        project     = "runs/detect",
        name        = "train",
        exist_ok    = True,
    )