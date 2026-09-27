from __future__ import annotations
import cv2
import numpy as np
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from whisper_hunter.detection import detect_whispers

out = Path(__file__).resolve().parents[1] / 'synthetic_whisper_detection.png'
img = np.full((720,1280,3),(72,70,68),np.uint8)
for (x,y), color, label in [
    ((260,260),(180,170,245),'1F'),
    ((620,360),(90,70,215),'3F'),
    ((980,450),(30,20,150),'5F'),
]:
    cv2.circle(img,(x,y),14,color,4)
    cv2.line(img,(x-16,y),(x+16,y),color,3)
    cv2.line(img,(x,y-16),(x,y+16),color,3)
for c in detect_whispers(img):
    x,y,w,h=c.bbox
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
    cv2.putText(img,f'{c.favor}F {c.confidence:.2f}',(x,y-8),cv2.FONT_HERSHEY_SIMPLEX,.5,(255,255,255),1,cv2.LINE_AA)
cv2.imwrite(str(out),img)
print(out)
