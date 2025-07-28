## Hi, this is B 🐝 ##
## Hope this adds a little sunshine 🌞 and brings joy 🌈#


print("🍵 A tiny mood-matcher to pair your vibes")
print("a pocket-sized pick-me-up 🌈")
print("     ")
print("Just a handful of oddball questions")
print("to see where your feels are fluttering")
print("and offer a small, cozy activity to match.")
print("     ")
print("Lets begin!")
print("     ")
print("     ")


# Mood trackers
the_buzz = 0        # anxiety
the_big_sad = 0     # depression
the_spin = 0        # panic
the_crunch = 0      # stress

# Q1
q1 = int(input("Q1: How did you sleep? (1 = What Sleep?!, 2 = Dreamy, 3 = Like a log, 4 = In intervals): "))
if q1 == 1:
    the_crunch += 2
    the_buzz += 2
elif q1 == 2:
    the_big_sad += 1
elif q1 == 3:
    the_spin += 1
elif q1 == 4:
    the_buzz += 1
    the_crunch += 1
print("     ")
print("     ")
# Q2
q2 = int(input("Q2: When you woke up, your mind whispered? (1 = “Let's do this”, 2 = “Not again”, 3 = “Why bother?”, 4 = “Can we disappear?”): "))
if q2 == 1:
    the_spin += 2
elif q2 == 2:
    the_big_sad += 2
elif q2 == 3:
    the_buzz += 2
    the_crunch += 2
elif q2 == 4:
    the_big_sad += 1
    the_crunch += 2
print("     ")
print("     ")
# Q3
q3 = int(input("Q3: Choose your current body vibe: (1 = Heavy, 2 = Tight, 3 = Floaty, 4 = Buzzing): "))
if q3 == 1:
    the_big_sad += 4
elif q3 == 2:
    the_crunch += 4
elif q3 == 3:
    the_spin += 4
elif q3 == 4:
    the_buzz += 4
print("     ")
print("     ")
# Q4
q4 = int(input("Q4: Which creature do you resonate with right now? (1 = Sloth, 2 = Octopus, 3 = Pigeon, 4 = Raccoon in a dumpster): "))
if q4 == 1:
    the_big_sad += 2
elif q4 == 2:
    the_buzz += 2
elif q4 == 3:
    the_crunch += 2
elif q4 == 4:
    the_spin += 2
print("     ")
print("     ")
# Q5
q5 = int(input("Q5: Your brain feels like: (1 = Soup, 2 = Static, 3 = Spreadsheet, 4 = Wallpaper): "))
if q5 == 1:
    the_buzz += 3
elif q5 == 2:
    the_spin += 3
elif q5 == 3:
    the_crunch += 3
elif q5 == 4:
    the_big_sad += 3
print("     ")
print("     ")
# Q6
q6 = int(input(
    "Q6: How is your sky today? (1 = Clear, 2 = Cloudy, 3 = Thunderstorm, 4 = Foggy): "))
if q6 == 1:
    the_spin += 3
elif q6 == 2:
    the_buzz += 3
elif q6 == 3:
    the_crunch += 3
elif q6 == 4:
    the_big_sad += 3
print("     ")
print("     ")
# Q7
q7 = int(input("Q7: Final checkpoint: Pick a pocket-sized feeling to carry with you today. (1 = Stillness, 2 = Bloom, 3 = Crackle, 4 = Drift): "))
if q7 == 1:
    the_crunch -= 3
elif q7 == 2:
    the_big_sad -= 3
elif q7 == 3:
    the_spin -= 3
elif q7 == 4:
    the_buzz -= 3
print("     ")
print("     ")

# Mood decoder (shhhh secret!)
max_score = the_buzz
vibe = "the_buzz"

if the_big_sad > max_score:
    max_score = the_big_sad
    vibe = "the_big_sad"
if the_spin > max_score:
    max_score = the_spin
    vibe = "the_spin"
if the_crunch > max_score:
    max_score = the_crunch
    vibe = "the_crunch"

# Micro-Activities
# Tiny cope-up techniques

if vibe == "the_buzz":
    print("Try this: Build a pillow fort or doodle your name in 10 weird fonts. Channel that buzz into harmless mischief.")
elif vibe == "the_big_sad":
    print("Try this: Rewatch a childhood cartoon or make a mini playlist of ‘sigh’ songs. Let comfort drip in slowly.")
elif vibe == "the_spin":
    print("Try this: Blow bubbles, real or imaginary, or sort something small by color. Let your brain hold something soft.")
else:
    print("Try this: Rip paper with purpose, stack things into tiny towers, or press your palm against a cool surface.")


# End of my little project, Thank you #
