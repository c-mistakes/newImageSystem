from PySide6.QtCore import QSize, QRect, QBuffer, QIODevice
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pathlib import Path
import base64
from PySide6.QtGui import QImageReader

"""实现基本图像显示功能"""
@csrf_exempt
def imageShow(request):
    if request.method == "GET":
        path = request.GET.get('path')
        area_x = int(request.GET.get('area_x'))
        area_y = int(request.GET.get('area_y'))
        width = int(request.GET.get('width'))
        height = int(request.GET.get('height'))
        # scale = request.GET.get('scale')
        # rotation = request.GET.get('rotation')
        # opacity = request.GET.get('opacity')
        # brightness = request.GET.get('brightness')
        # tone_scale = request.GET.get('tone-scale')
        current_path = Path(path)
        str_path = str(current_path)
        if current_path.exists():
            img = QImageReader(str_path)
            img.setAllocationLimit(0)
            #给出一个指定分辨率的图像到前端
            img.setScaledSize(QSize(2560, 1440))
            # img.setClipRect(QRect(int(area_x), int(area_y), int(width), int(height)))
            result = img.read()
            print(result)
            img_data = changeBase64(result)
            return JsonResponse(img_data, safe=False)
    return JsonResponse({'code': 0})

def changeBase64(image, format='tiff'):
    buffer = QBuffer()
    buffer.open(QIODevice.WriteOnly)
    image.save(buffer, format)
    byte_array = buffer.data()
    base_data = base64.b64encode(byte_array).decode('utf-8')
    return base_data