import pickle
import dlib
import cv2
import numpy as np
from datetime import datetime

import logging

from threading import Thread

# camera_link = "rtsp://admin:XTKDRI@192.168.0.163/"
path_write = 'C:\\TccControleAcesso\\controleDeAcesso\\controleDeAcesso\\core\\static\\ia\\dlib.jpeg'
path_read = 'C:\\TccControleAcesso\\controleDeAcesso\\controleDeAcesso\\core\\static\\ia\\teste.jpeg'

class Recognize():

    def __init__(self):
        self.detectorFace = dlib.get_frontal_face_detector()
        self.detectorPontos = dlib.shape_predictor("C:\\TccControleAcesso\\controleDeAcesso\\machineLearning\\sources\\shape_predictor_68_face_landmarks.dat")
        self.reconhecimentoFacial = dlib.face_recognition_model_v1("C:\\TccControleAcesso\\controleDeAcesso\\machineLearning\\sources\\dlib_face_recognition_resnet_model_v1.dat")
        self.indices = pickle.load(open("C:\\TccControleAcesso\\controleDeAcesso\\machineLearning\\recognition\\categories.pickle", 'rb'))
        self.descritoresFaciais = np.load("C:\\TccControleAcesso\\controleDeAcesso\\machineLearning\\recognition\\descritores_rn.npy")
        self.limiar = 0.5
        self.logger = logging.getLogger(__name__)

    def fuck(self, imagem):
        # facesDetectadas = False
        facesDetectadas = self.detectorFace(imagem, 2)
        if facesDetectadas:
            face = facesDetectadas[0]
            e, t, d, b = (int(face.left()), int(face.top()), int(face.right()), int(face.bottom()))
            pontosFaciais = self.detectorPontos(imagem, face)
            descritorFacial = self.reconhecimentoFacial.compute_face_descriptor(imagem, pontosFaciais)
            listaDescritorFacial = [fd for fd in descritorFacial]
            npArrayDescritorFacial = np.asarray(listaDescritorFacial, dtype=np.float64)
            npArrayDescritorFacial = npArrayDescritorFacial[np.newaxis, :]

            distancias = np.linalg.norm(npArrayDescritorFacial - self.descritoresFaciais, axis=1)
            # print("Distâncias: {}".format(distancias))
            minimo = np.argmin(distancias)
            # print(minimo)
            distanciaMinima = distancias[minimo]
            # print(distanciaMinima)

            if distanciaMinima <= self.limiar:
                nome = self.indices[minimo]
            else:
                nome = 'Unknown'

            cv2.rectangle(imagem, (e, t), (d, b), (0, 255, 255), 2)
            texto = "{} {:.4f}%".format(nome, (1.0 - distanciaMinima))
            cv2.putText(imagem, texto, (d, t), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 255))

        cv2.imwrite(path_write, imagem)

    def run(self):
        self.logger.warning('exibindo...')
        # ret, imagem = cv2.VideoCapture("rtsp://admin:XTKDRI@192.168.0.163/").read()

        # cap = cv2.VideoCapture(camera_link)
        while(True):
            # ret, frame = cv2.VideoCapture(camera_link).read()
            frame = cv2.imread(path_read)
            if frame is not None:
                imagem = cv2.resize(frame, (400, 300))

                # imagem = self.fuck(imagem)
                Thread(name="Thread", target=self.fuck(imagem)).start()
                self.logger.warning(datetime.now().time())

                # cv2.imshow("Camera", imagem)
                # k = cv2.waitKey(30) & 0xff
                # if k == 27:
                #     break

            # cv2.VideoCapture(camera_link).release()
        cv2.destroyAllWindows()
        self.logger.warning('finished...')


recognize = Recognize()
recognize.run()
