# working with vedios
import cv2
import datetime

# cap = cv2.VideoCapture('project_demo.mp4')
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # use this to open Device Camera
flag = 0
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 10.0, (640, 480))  # ( for recording video )
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# cap.set(3, 300) ( for setting property )
# cap.set(4, 400)
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
try:
    while cap.isOpened():
        flag = 1
        ret, frame = cap.read()
        out.write(frame)
        # grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) ( for grey scale image)
        text = str(datetime.datetime.now().time()).split('.')[0]
        d = datetime.datetime.strptime(text, "%H:%M:%S")
        text = d.strftime("%I:%M:%S %p")
        cv2.putText(frame, text, (430, 470), fontFace=cv2.FONT_ITALIC, fontScale=1, color=(255, 0, 0),
                    thickness=3, lineType=cv2.LINE_AA)
        cv2.putText(frame, str(datetime.datetime.today()), (430, 430), fontFace=cv2.FONT_ITALIC, fontScale=1,
                    color=(255, 0, 0),
                    thickness=3, lineType=cv2.LINE_AA)
        cv2.imshow('live', frame)

        # print(chr(k))s
        if cv2.waitKey(1) == ord('q'):
            break
    out.release()
    cap.release()
    cv2.destroyAllWindows()
    if flag == 0:
        print("Sorry Incorrect Path!!!")
    else:
        raise EOFError
except:
    print("Video displayed successfully :)")
