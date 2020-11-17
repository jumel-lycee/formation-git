import logging

def affiche(message):
    return logging.warning(message)

def erreur(message):
    return logging.error(message)

logging.debug('Message')
logging.warning('Attention')



