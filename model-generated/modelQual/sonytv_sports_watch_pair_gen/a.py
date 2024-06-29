
import random

sports_watches = ["Polar Grit X2 Pro", "Apple Watch Ultra 2", "Garmin Enduro 2", "Oura Ring", "Amazfit Helio Ring"]
sony_tvs = ["Bravia A80L", "Bravia XR X90L", "Sony X90L"]

random_pairing = (random.choice(sports_watches), random.choice(sony_tvs))

print(random_pairing)