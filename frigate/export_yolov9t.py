#!/usr/bin/env python3
"""Export YOLOv9 tiny ONNX model for Frigate (320x320, OpenVINO)."""

from ultralytics import YOLO

model = YOLO("yolov9t.pt")  # downloads pretrained weights automatically
model.export(format="onnx", imgsz=320, simplify=True)
print("\nDone! Model saved as: yolov9t.onnx")
print("Upload it to your NAS at: <CONFIG_ROOT>/frigate/model_cache/yolov9t.onnx")
