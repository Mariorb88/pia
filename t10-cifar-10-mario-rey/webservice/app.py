# pip install fastapi uvicorn python-multipart pillow torch torchvision
# http://127.0.0.1:8000/docs para testear el servicio web

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import torch
import torchvision.transforms as transforms
import io


from modelo import Net  # Asegúrate de tener la definición de tu red neuronal aquí

app = FastAPI()

# Cargar modelo
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = Net().to(device)
model.load_state_dict(torch.load("cifar_net.pth", map_location=device))
model.eval()

# Transformación CIFAR-10
transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465),
                         (0.2023, 0.1994, 0.2010))
])

# Clases CIFAR-10
classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')


@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    input_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(input_tensor)
        _, predicted = torch.max(outputs, 1)
        label = classes[predicted.item()]
    
    return JSONResponse(content={"prediction": label})



if __name__ == '__main__':
    app.run(debug=True)
