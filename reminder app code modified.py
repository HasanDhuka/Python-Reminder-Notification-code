from win10toast import ToastNotifier
import time
import winsound

toaster = ToastNotifier()

def show_notification(title, message):
    """ Display a notification message """
    toaster.show_toast(title, message, duration=10, threaded=True)

def play_notification_sound():
    """ Play a notification sound """
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS | winsound.SND_ASYNC)

if __name__ == "__main__":
    Title = input("\nTitle of Reminder: ")
    Msg = input("Hey user please enter a message: ")
    minutes = float(input("How many minutes: "))

    seconds = minutes * 60

    print("\nReminder Set Successfully!\n")
    time.sleep(seconds)

    # Show notification
    show_notification(Title, Msg)

    # Play notification sound
    play_notification_sound()

    # Wait until the notification is closed
    while toaster.notification_active:
        time.sleep(0.1)
