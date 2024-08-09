import keyboard
import pyautogui
import time

def get_edit_key():
    print("Press the key you want to use for editing (e.g., 'C').")

    detected_key = None
    while True:
        try:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN and event.name != 'esc':
                detected_key = event.name
                print(f"Key '{detected_key}' selected as the Edit Bind.")
                return detected_key
        
        except Exception as e:
            print(f"Error detecting key: {e}")
            return None
        
        time.sleep(0.1)

def simulate_edit_on_release(edit_key):
    if not edit_key:
        print("No valid key bind selected.")
        return
    
    print(f"Simulating Edit on Release for key '{edit_key}'.")

    edit_delay = 0.05
    detection_delay = 1.1

    last_release_time = 0
    last_detection_time = 0
    key_held = False

    while True:
        current_time = time.time()

        try:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN and event.name == edit_key:
                if not key_held:
                    key_held = True
                    last_detection_time = current_time
            elif event.event_type == keyboard.KEY_UP and event.name == edit_key:
                if key_held:
                    if current_time - last_release_time >= edit_delay:
                        pyautogui.press(edit_key)
                        last_release_time = current_time
                    key_held = False

            if current_time - last_detection_time >= detection_delay:
                last_detection_time = current_time
        
        except Exception as e:
            print(f"Error simulating key press: {e}")
            break

        time.sleep(0.01)
if __name__ == "__main__":
    try:
        edit_key = get_edit_key()
        if edit_key:
            simulate_edit_on_release(edit_key)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
