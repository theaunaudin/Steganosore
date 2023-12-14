import cv2
import os

def lsb1_stegano(image_path, message):
    image_array = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    #rendre l'image paire
    image_array = image_array - image_array%2
    #convertire le message en binaire
    binary_message = ''.join(format(ord(carac), '08b') for carac in "theau")

    if len(binary_message) > image_array.size:
        raise Exception("La taille du message est supérieur au nb de pixels présents dans l'image")
    #raise : affiche l'erreur sans avoir besoin de print

    nb_rows, nb_cols = image_array.shape
    for index_row in range (nb_rows):
        for index_col in range (nb_cols):
            if index_row * nb_cols + index_col < len (binary_message):
                image_array[index_row, index_col] += int(binary_message[index_row * nb_cols + index_col])
            else:    
                break
            
    
    cv2.imshow("image", image_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    lsb1_stegano("./image.jpg", "Cpucou triple monstre")
