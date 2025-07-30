

# Write code below 💖

## 💖 Little Mousey Survival Adventure ##

print("🐭✨ Welcome to Mousey's Descent! ✨🐭")

print("You've stumbled into a mysterious terminal… one that controls the fate of a fragile little mouse trapped in a fRAT house.")
print(" ")
print(" ")
print("You must guide it through vents, past dangers, toward safety....or let it meet a most tragic doom.")
print("Mousey has a faint little heart.")
print("Wrong choices will stress it out!")
print(" ")
print(" ")

# Trackers
survive = 0    # Survival points
death = 0      # RIP meter
stress = 8     # Mousey’s mental health
d4 = 0  # if RIP before reaching Squeak 4

# Squeak 1
print("Squeak 1: Into the Vents")
print(" ")
d1 = int(input("Mousey falls into a vent with 3 duct paths... (1 = Left, 2 = Right, 3 = Straight): "))
if d1 == 1:
    survive += 1
    stress -= 3
    death += 1
    print("💀 The duct collapses and Mousey dangles over a snake enclosure. One hiss and it's lights out. 🪦🔥")
elif d1 == 2:
    survive += 4
    stress -= 1
    print("🍃 The duct smells earthy. Mousey relaxes... maybe cheese is near?")
elif d1 == 3:
    survive += 4
    stress -= 1
    print("💨 A cool mist fills the air. Mousey's whiskers twitch. Water?")
else:
    stress -= 4
    print("😱 Mousey hesitates. Stress spikes in the confusion!")

print(f"🧠 Mousey's stress level: {stress}")
print(" ")

# Squeak 2
print("Squeak 2: The Slippery tumble")
print(" ")
if death < 5 and stress > 0:
    d2 = int(input("Mousey dangles by its tail as it slips into a collapsed vent... (1 = Swing Left, 2 = Swing Right, 3 = Fall In): "))
    if d2 == 1:
        survive += 2
        stress -= 2
        print("🌀 Mousey somersaults and belly-flops. Surprisingly graceful.")
    elif d2 == 2:
        death += 5
        print("⚠️ Mousey smacks straight into the HVAC fan. Like a wrecking ball. RIP 🪦🔥")
    elif d2 == 3:
        stress -= 2
        survive += 1
        print("🧠 Bonk! Mousey lands on its noggin, stunned but safe.")
    else:
        stress += 2
        survive += 2
        death += 1
        print("😖 Mousey flinches. Wrong move. Fear grows.")
    print(f"🧠 Mousey's stress level: {stress}")
    print(" ")
elif stress <= 0 and death >= 5:
    print("💀 Mousey can't continue. It’s over, little one.")


# Squeak 3
if death < 4 and stress > 0:
    print("Squeak 3: Is it Cake?")
    print(" ")
    d3 = int(input(
        "Mousey finds a mysterious umbrella-shaped chunk of mush... (1 = Eat, 2 = Lick, 3 = Sniff): "))
    if d3 == 1:
        survive -= 4
        stress -= 1
        death += 2
        print("😌 Tummy full, heart soothed. Mousey purrs.")
    elif d3 == 2:
        survive -= 2
        stress -= 2
        print("🥴 A weird aftertaste... but Mousey feels slightly calmer.")
    elif d3 == 3:
        survive -= 1
        stress -= 3
        death += 1
        print("🤧 Sniff sniff... eww. That is not cheese. But catharsis achieved.")
    else:
        stress += 3
        print("🤯 Mousey panics! Its mind hurts! Mousey squeaks in sadness!.")
    print(f"🧠 Mousey's stress level: {stress}")
    print(" ")
else:
    print("💀 Mousey is too weak. Everything fades to grey... RIP")

# Squeak 4
if death < 4 and stress > 0:
    print("Squeak 4: A Crack of Hope")
    print(" ")
    d4 = int(input(
        "The air feels heavy. Mousey sees two cracks... (1 = Crack One, 2 = Crack Two): "))
    if d4 == 1:
        survive += 3
        stress -= 2
        print("🌿 Crack One opens to a garden... but cats lurk. The risk is real.")
    elif d4 == 2:
        survive += 3
        stress -= 2
        print("🗑️ Crack Two drops Mousey into a trash pile... soft landing. And safety.")
    else:
        stress += 2
        print("😵 Mousey freezes, squeaking anxiously. Indecision is death in a vent.")
else:
    print("🕳️ Mousey is unresponsive. Its tiny limbs twitch once... then stillness.")


# Endings
print("Ending")
print(" ")
if stress >= 12:
    print("💔 Mousey suffers from Stress-Induced Fear and Anxiety. Descent complete.")
elif death >= 5:
    print("💀 Death toll tolls for Mousey. Poor squish met a grisly fate.")
elif d4 == 1:
    print("🌸 Mousey escapes into a garden... only to be eyed by a stray cat. A bittersweet ending.")
elif d4 == 2:
    print("🏆 Trash pile ending! Smelly, but Mousey is safe. The best ending.")
else:
    print("🐭 Mousey will be remembered by the ducts...forever squeaking. RIP")
