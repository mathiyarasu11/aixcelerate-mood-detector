train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad"),
]

# Level 1: Count Happy and Sad sentences
def count_moods(data):
    happy_count = 0
    sad_count = 0
    for sentence, mood in data:
        if mood == "Happy":
            happy_count += 1
        elif mood == "Sad":
            sad_count += 1
    return (happy_count, sad_count)

print("Train data counts:", count_moods(train_data))

# Level 2: Guess mood using 7 clue words each (since roll number ends in 7)
happy_words = ["won", "surprise", "party", "tasty", "excited", "selected", "favourite"]
sad_words = ["lost", "failed", "cancelled", "missed", "upset", "stopped", "lonely"]

def guess_mood(sentence):
    clean_sentence = sentence.lower()
    for p in ".,!?;:'\"":
        clean_sentence = clean_sentence.replace(p, "")
    
    words = clean_sentence.split()
    
    happy_score = 0
    sad_score = 0
    
    for word in words:
        if word in happy_words:
            happy_score += 1
        if word in sad_words:
            sad_score += 1
            
    if happy_score > sad_score:
        return "Happy"
    elif sad_score > happy_score:
        return "Sad"
    else:
        # Tie-breaker: Choose "Happy" by default because train_data has more Happy sentences (8 vs 7).
        return "Happy"

# Level 3: Test on practice data
practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy"),
]

correct = 0
for sentence, actual_mood in practice_data:
    predicted_mood = guess_mood(sentence)
    print(f"Sentence: '{sentence}' | Predicted: {predicted_mood} | Actual: {actual_mood}")
    if predicted_mood == actual_mood:
        correct += 1

accuracy = (correct / len(practice_data)) * 100
print(f"Accuracy: {accuracy}%")