import cv2
import torch

# Load a local TorchScript model
model = torch.jit.load('model.pt')
model.eval()

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Convert frame to tensor
    img = torch.from_numpy(frame).permute(2, 0, 1).float() / 255.0
    with torch.no_grad():
        outputs = model(img.unsqueeze(0))
    print(outputs)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
