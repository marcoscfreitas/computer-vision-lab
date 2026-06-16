from ultralytics import YOLO
import torch

# define cuda
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Usando o dispositivo: {DEVICE}")

def train_model():
    # carrega o modelo pré-treinado de classificação
    model = YOLO("yolo26n-cls.pt")

    # inicia o treinamento
    results = model.train(
        data="/home/marv/Documentos/laydown_cls_dataset",
        epochs=100, 
        imgsz=224, 
        device=DEVICE,
        project="laydown_classification",
        name="modelo_v1"
    )

def predict_image(image_path):
    # carrega o modelo treinado
    model = YOLO("runs/classify/laydown_classification/modelo_v1/weights/best.pt")
    
    # faz a predição
    results = model(image_path)
    
    # exibe os resultados e as probabilidades de cada classe
    for result in results:
        top1_class = result.names[result.probs.top1]
        confidence = result.probs.top1conf.item()
        print(f"Classe predita: {top1_class} (Confiança: {confidence:.2f})")

if __name__ == "__main__":
    # rodando treinamento
    train_model()
    
    # inferencia
    #predict_image("/home/marv/Documentos/imagens_separadas/teste/")
