import pandas as pd
import numpy as np

# Define a token for backspace/delete operations
DELETE_TOKEN = '[DELETE_CHAR]'

def clean_key(key):
    """
    Cleans up key names:
    - Replaces 'Space' with a literal space ' '.
    - Explicitly marks 'Backspace', 'Delete', 'Back' keys for deletion logic.
    - Removes non-printable modifier/meta keys.
    - Converts remaining keys to lowercase.
    """
    key = str(key)
    if key == 'Space':
        return ' '
    # Special handling for delete keys
    elif key in ['Backspace', 'Delete', 'Back']:
        return DELETE_TOKEN
    # Exclude non-printable modifier/meta keys (Modifier and navigation keys)
    elif key in ['Shift', 'Tab', 'Control', 'Alt', 'LControl', 'RControl', 'LShift', 'RShift', 'Return', 'CapsLock', 'Escape', 'Enter', 'Menu', 'Prior', 'Next', 'End', 'Home', 'Left', 'Up', 'Right', 'Down', 'Insert', 'Snapshot', 'Scroll', 'Pause', 'NumLock', 'LMenu', 'RMenu', 'LWin', 'RWin', 'Apps','arrowdown','arrowleft','arrowright','arrowup']:
        return ''
    # Converts remaining keys to lowercase.
    return key.lower()


def reconstruct_sentence_with_deletion(group):
    """
    Iterates through the sequence of keys and applies the deletion logic 
    whenever a [DELETE_CHAR] token is encountered.
    """
    output_chars = []
    
    # Process the sequence of keys from the 'key1' column (which forms the body of the text)
    for key in group['cleaned_key1']:
        if key == DELETE_TOKEN:
            # If the output list is not empty, delete the last printable character
            if output_chars:
                output_chars.pop()
        elif key:
            # Only append if the key is not an empty string (i.e., not a modifier)
            output_chars.append(key)
            
    # Process the final key (key2 of the last row)
    # The last key of the session is the key2 of the final digraph.
    final_key = group['cleaned_key2'].iloc[-1]
    if final_key == DELETE_TOKEN:
        if output_chars:
            output_chars.pop()
    elif final_key:
        output_chars.append(final_key)

    return "".join(output_chars).strip()

# --- SCRIPT EXECUTION ---
try:
    df_free = pd.read_csv("data/keystrokes/raw/1free-text.csv")
except FileNotFoundError:
    print("User-specified path not found. Attempting to load from current directory...")
    df_free = pd.read_csv("free-text.csv")

# 1. Apply cleaning to key1 and key2
df_free['cleaned_key1'] = df_free['key1'].apply(clean_key)
df_free['cleaned_key2'] = df_free['key2'].apply(clean_key)


# 2. Apply the reconstruction logic grouped by participant and session
sentence_series = df_free.groupby(['participant', 'session']).apply(reconstruct_sentence_with_deletion)

# 3. Final Output Processing
unique_sentences = sentence_series.unique()
# Remove any empty strings resulting from sessions with only modifier/delete keys
unique_sentences = [s.strip() for s in unique_sentences if s.strip()]

print(f"Total unique reconstructed sentences (with backspace applied): {len(unique_sentences)}")

# 4. Save the resulting unique sentences to a CSV file
unique_sentences_df = pd.DataFrame(unique_sentences, columns=['reconstructed_sentence'])
output_filename = "reconstructed_sentences_fixed.csv"
unique_sentences_df.to_csv(output_filename, index=False)
print(f"Output saved to {output_filename}")

 


