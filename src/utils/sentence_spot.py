import pandas as pd
df_free = pd.read_csv("data/keystrokes/raw/free-text.csv")

"""
Cleans up key names:
    - Replaces 'Space' with a literal space ' '.
    - Removes non-printable modifier/meta keys.
    - Converts remaining keys to lowercase.

"""

def clean_key(key):
    if key == 'Space':
        return ' '
    #Exclude from sentence reconstruction
    elif key in ['Shift', 'Tab', 'Control', 'Alt', 'LControl', 'RControl', 'LShift', 'RShift', 'Return', 'Backspace', 'Delete', 'CapsLock', 'Escape','arrowup','arrowleft','arrowdown','arrowright']:
        return ''

    return str(key).lower()

# --- STEP 1: Process Key1 ---
df_free['cleaned_key1'] = df_free['key1'].apply(clean_key)

# --- STEP 2: Reconstruct the Sentence ---
"""
1. Joins the 'cleaned_key1' values from all rows (captures most of the sentence).
2. Appends the cleaned 'key2' value from the *very last row* of the group. 
"""

def reconstruct_sentence(group):
    sentence_part_1 = "".join(group['cleaned_key1'])
    last_key2 = clean_key(group['key2'].iloc[-1])
    full_sentence = sentence_part_1 + last_key2
    
    return full_sentence.strip()

sentence_series = df_free.groupby(['participant', 'session']).apply(reconstruct_sentence)

# --- STEP 3: Final Output ---
unique_sentences = sentence_series.unique()
unique_sentences = [s.strip() for s in unique_sentences if s.strip()]

print(f"Total unique reconstructed sentences: **{len(unique_sentences)}**")
print("\nFirst 10 Unique Reconstructed Sentences:")
for i, sentence in enumerate(unique_sentences[:10]):
    print(f"{i+1}. {sentence}")

unique_sentences_df = pd.DataFrame(unique_sentences, columns=['reconstructed_sentence'])
unique_sentences_df.to_csv("reconstructed_sentences.csv", index=False)