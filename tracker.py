import cv2

# Video dosyasını yükle (veya 0 kullanarak kameradan canlı alabilirsiniz)
video_path = 0
cap = cv2.VideoCapture(video_path)
track=3
if (track==1):
 tracker = cv2.TrackerMIL_create()
if (track==2):
 tracker = cv2.TrackerCSRT_create()
if (track==3):
 tracker = cv2.TrackerKCF_create()


# İlk kareyi oku
ret, frame = cap.read()

# ROI'yi seç
roi = cv2.selectROI("Select Object", frame)
tracker.init(frame, roi)


while True:
    # Bir sonraki kareyi oku
    ret, frame = cap.read()
    if not ret:
        break

    # KCF tracker'ı güncelle
    success, roi = tracker.update(frame)

    # Takip başarılıysa, nesneyi çerçeve içine al
    if success:
        (x, y, w, h) = tuple(map(int, roi))
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Pencerede görüntüyü göster
    cv2.imshow("Tracking", frame)

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Video ve pencereyi serbest bırak
cap.release()
cv2.destroyAllWindows()
