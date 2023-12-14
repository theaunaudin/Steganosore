import string

def chiffre_cesar_nombre(liste_a_dechiffrer, clef):
    liste_dechiffree=[]
    for index in range (0, len(liste_a_dechiffrer)):
        liste_a_dechiffrer[index] = liste_a_dechiffrer[index] + clef
        liste_dechiffree.append(liste_a_dechiffrer[index])
        index += 1
    return liste_dechiffree

print(chiffre_cesar_nombre([1,8,4,9,9,15,28], 5))

def chiffre_cesar_lettres(message, clef):
    alphabet = string.printable
    liste_indice = []
    message_dechiffre = []
    transfo_lettre = 0
    for index in range (0, len(message)):
        transfo_lettre = message[index]
        liste_indice.append(transfo_lettre)
    for index2 in range (0, len(liste_indice)):
        lettre = liste_indice[index2]
        message_dechiffre.append(lettre)
        print(message_dechiffre)
    return message_dechiffre

def cesar_ciffer(message, key):
    
    list_of_crypted_caracs = []
    
    for carac in message:
        crypted_index = (string.printable.index(carac) + key) % len(string.printable)
        crypted_carac = string.printable[crypted_index]
        
        list_of_crypted_caracs.append(crypted_carac)
    
    crypted_message = "".join(list_of_crypted_caracs)
    return crypted_message

def chiffrement_vigenere(message, suite_de_cle):
    
    while len(message) > len(suite_de_cle):
        suite_de_cle += suite_de_cle
    
    crypted_vigenere_message = []
    intermediaire = ''
    
    for index in range(0, len(message)):
        intermediaire = message[index]
        lettre_descriptee = cesar_ciffer(intermediaire, suite_de_cle[index])
        crypted_vigenere_message.append(lettre_descriptee)
        
    crypted_vigenere = "".join(crypted_vigenere_message)
    
    return crypted_vigenere
    

def vigenere_decrypt(crypted_message, suite_de_cle):
    
    for index in range (0, len(suite_de_cle)):
        suite_de_cle[index] = -suite_de_cle[index]
        suite_de_cle.append(suite_de_cle)
        
    return chiffrement_vigenere(crypted_message, suite_de_cle)

def vigenere_mot_de_passe(message, mot_de_passe):
    
    suite_de_cle = [string.printable.index(i) for i in mot_de_passe]
    
    message_chiffre = []
    
    while len(message) > len(suite_de_cle):
        suite_de_cle += suite_de_cle
        
    intermediaire = []
    
    for index in range(0, len(message)):
        intermediaire = message[index]
        lettre_descriptee = cesar_ciffer(intermediaire, suite_de_cle[index])
        message_chiffre.append(lettre_descriptee)
        
    crypted_vigenere = "".join(message_chiffre)
    
    return crypted_vigenere
    
def vigenere_mot_de_passe_correc_prof(message, password):
    
    list_of_keys = [string.printable.index(password_carac) for password_carac in password]
    list_of_crypted_caracs = [cesar_ciffer(carac, list_of_keys[index_carac % len(list_of_keys)]) for index_carac, carac in enumerate(message)]
            
    return "".join(list_of_crypted_caracs)