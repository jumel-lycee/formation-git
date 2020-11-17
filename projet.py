import logging

def affiche(message):
    return logging.warning(message)

def erreur(message):
    logging.info(message)
    return logging.error(message)


logging.debug('Message')
logging.warning('Attention')
# un commentaire
#2 commentaires

