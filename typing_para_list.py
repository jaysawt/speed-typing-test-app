import random


typing_material = ["""Once upon a time in the quaint village of Everbrook, nestled amidst lush green forests and sparkling rivers, lived a young girl named Amelia. She had an insatiable curiosity, always seeking adventure beyond the village's boundaries. One day, she stumbled upon an ancient map hidden in her grandmother's attic, depicting a mysterious island rumored to hold a magical artifact that granted eternal wisdom.
Driven by excitement and fueled by stories of the artifact's powers, Amelia embarked on a perilous journey, braving treacherous terrains and daunting challenges. Along the way, she encountered peculiar creatures and faced her deepest fears. But Amelia's determination and kind heart won her the loyalty of unlikely companions, including a mischievous talking fox and a wise old owl.
As she ventured deeper into the unknown, Amelia's innocence was tested, and her true character shone through. She resisted the temptation of dark forces and chose compassion over personal gain. Finally, after days of arduous travel, Amelia arrived at the fabled island.
The island was a breathtaking sight: lush gardens, radiant waterfalls, and ethereal glowing flowers adorned the landscape. Guided by the map, Amelia found the ancient temple housing the artifact. But she was met with a guardian, a fearsome dragon who challenged her worthiness.
With courage and grace, Amelia stood her ground, proving her purity of heart. Moved by her sincerity, the dragon granted her access to the artifact. As Amelia touched it, a rush of wisdom flooded her mind, unveiling the secrets of the universe.
Having acquired profound knowledge, Amelia returned to Everbrook. Instead of hoarding her newfound wisdom, she selflessly shared it with her fellow villagers, transforming their lives and bringing prosperity to the village.
From that day forward, Amelia became the village's cherished sage, guiding generations to come. Her story spread far and wide, inspiring many to embrace kindness, empathy, and the pursuit of knowledge.
And so, the little girl with a heart full of dreams became a beacon of light, forever etched in the annals of Everbrook's history, reminding everyone that true magic lies not in artifacts but in the compassion and wisdom found within each soul.""",
'''
In the small village of Whisperbrook, a mysterious mist enveloped the streets every twilight. Locals believed it hid an enigmatic portal to another realm. One daring girl, Lily, discovered a glowing amulet in the forest, granting her passage. Beyond, she found a magical kingdom on the brink of darkness. Armed with courage, she united the fractured factions, ending a centuries-old war.
As gratitude, the kingdom's ruler bestowed upon Lily the amulet's true power—to bring harmony to worlds. From then on, she became the bridge between realms, ensuring peace and prosperity for both her village and the enchanted kingdom. However, whispers of jealousy and envy began to spread, challenging Lily's quest for unity. With adversaries seeking to exploit the amulet's might, Lily faced her greatest test of character yet. Undeterred, she remained steadfast, reminding all that true strength lay not in power, but in the ability to embrace differences and find common ground. Her unwavering spirit and compassion transformed not only the two realms but also the hearts of all who witnessed her noble journey. The legacy of Lily, the bridge between worlds, would be eternally cherished and celebrated, an emblem of hope for generations to come in the magical lands of Whisperbrook and beyond.
''',
'''
In the future city of Lumos Prime, citizens lived beneath the earth's surface, sheltered from a scorching sun. Young inventor, Alex, created a machine to harness solar energy, dreaming of a brighter world. His innovation drew scorn from those profiting underground.
Ignoring threats, Alex unveiled his device, illuminating Lumos Prime's darkest corners. The once-hidden beauty captivated all, and unity flourished. With renewable energy now abundant, Lumos Prime soared into a new era of enlightenment. The city's skies cleared, revealing a dazzling celestial display.
Alex's vision had birthed hope, proving that one courageous soul could ignite an entire metropolis. His invention inspired countless other breakthroughs, propelling Lumos Prime to become a beacon of sustainability and progress for the world.
''',
'''
In the kingdom of Frostoria, a prince named Julian, cursed by an evil sorceress, transformed into a snow leopard at each winter's eve. Desperate to break the spell, he embarked on a quest to find the legendary Crystal of Thawing. Joined by a spirited thief named Isabella, they faced treacherous mountains and dark enchantments. Their journey kindled an unexpected bond. When they finally reached the crystal, Julian chose self-sacrifice to save Isabella from the curse's clutches. Touched by his love, the sorceress relented, restoring Julian to human form, and they lived happily ever after.
High in the clouds resided Cloudhaven, a celestial realm of floating islands and mystical beings. Among them, a wingless fairy named Aurora yearned to soar the skies. Guided by an ancient oracle, she undertook daunting trials to gain celestial wings. Each test tested her resilience and taught valuable lessons. In the final trial, she risked all to save a fallen star. Her selflessness and courage won the favor of the heavens, gifting her iridescent wings. Aurora's triumph not only fulfilled her dream but also rekindled the realm's faith in compassion, forever changing Cloudhaven's fate.
''',
'''
Far beneath the ocean waves lived Maris, a mermaid gifted with a mesmerizing voice. She longed to explore the human world but feared losing her enchanting melody. One night, drawn by a celestial melody, she surfaced to find a shipwrecked sailor, Lucas. Entranced by her voice, he yearned to meet the singer. Maris faced a heartrending choice—to reveal herself or protect her identity. She decided honesty, transforming her tail to legs. In the human world, Lucas and Maris' love bloomed, proving that the sweetest melodies are those sung by the heart.
In the small village of Whisperbrook, a mysterious mist enveloped the streets every twilight. Locals believed it hid an enigmatic portal to another realm. One daring girl, Lily, discovered a glowing amulet in the forest, granting her passage. Beyond, she found a magical kingdom on the brink of darkness. Armed with courage, she united the fractured factions, ending a centuries-old war.
''',
    ]


def content():
    x = random.choice(typing_material)
    y = x.replace('\n', '')
    return y


