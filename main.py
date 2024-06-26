from pyscript import document
from random import shuffle


select = document.querySelector  # Alias della funzione che seleziona elemento/i HTML
nations = open("nations.csv", encoding="utf-8").readlines()
to_guess = None  # Nome della nazione da indovinare


def set_answer_buttons(enabled):
    """Abilita/disabilita i pulsanti di risposta."""
    for i in (1, 2, 3):
        target = select("#answer-button" + str(i))
        target.disabled = not enabled


def check_answer(event):
    """Controlla se l'utente ha premuto sul pulsante corretto e un messaggio di feedback."""
    user_choice = event.srcElement  # Sorgente dell'evento, es, "answer-button1"
    set_answer_buttons(False)

    if user_choice.innerText == to_guess:  # Controlla la scelta dell'utente
        message = f"Risposta esatta!\n{to_guess.strip()}!"
        icon_filename = "./images/true.svg"
    else:
        message = f"Risposta sbagliata!\nLa risposta esatta era {to_guess}"
        icon_filename = "./images/false.svg"

    select("#message-text").innerText = message
    select("#message-img").src = icon_filename
    select("#message-container").style.display = "block"


def play(event=None):
    """Estrae una nazione da indovinare e altre due nazioni casuali."""
    global nations, to_guess

    shuffle(nations)  # Mescola tutte le nazioni
    answers = nations[:3]  # Prende le prime tre nazioni come possibili risposte
    to_guess = answers[0]  # Sceglie la prima come nazione estratta
    to_guess_filename = f"./images/flags/{to_guess.replace(' ', '_')}.png"
    select("#flag-image").src = to_guess_filename
    shuffle(answers)  # Mescola le tre risposte
    set_answer_buttons(enabled=True)  # Abilita tutti i pulsanti di risposta

    for i, nation in enumerate(answers):
        select("#answer-button" + str(i + 1)).innerText = nation

    select("#message-container").style.display = "none"
    select("#loading-button").style.display = "none"
    select("#main-container").style.display = "block"


play()
