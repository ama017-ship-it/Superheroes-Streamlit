import random
import streamlit as st
    


Superman = {
"Hero": {"Power": "Flight", "Home": "Metropolis"},
"Villian" : {"Name": "General Zod", "Power": "Kryptonian Strength", "Home": "Krypton"},
"Franchise": "DC Comics"
}

Batman = {
"Hero": {"Power": "Martial Arts", "Home": "Gotham"},
"Villian": { "Name": "Joker", "Power": "Chaos", "Home": "Gotham"},
"Franchise": "DC Comics"
}

WonderWoman = {
"Hero": {"Power": "Super Strength", "Home": "Themyscira"}, 
"Villian": {"Name": "Cheetah", "Power": "Deception", "Home": "Various"},
"Franchise": "DC Comics"
}

Flash = {
"Hero": {"Power": "Super Speed", "Home": "Central City"},
"Villian": {"Name": "Reverse Flash", "Power": "Speed Manipulation", "Home": "Central City"},
"Franchise": "DC Comics"
}

Aquaman = {
"Hero": {"Power": "Aquatic Abilities", "Home": "Atlantis"},
"Villian": {"Name": "Black Manta", "Power": "Advanced Technology", "Home": "Various"},
"Franchise": "DC Comics"
}

Hulk = {
"Hero": {"Power": "Super Strength", "Home": "Earth"},
"Villian": {"Name": "Abomination", "Power": "Super Strength", "Home": "Earth"},
"Franchise": "Marvel Comics"
}

IronMan = {
"Hero": {"Power": "Genius Intellect", "Home": "Earth"},
"Villian": {"Name": "Mandarin", "Power": "Advanced Technology", "Home": "Earth"},
"Franchise": "Marvel Comics"
}

Thor = {
"Hero": {"Power": "God of Thunder", "Home": "Asgard"},
"Villian": {"Name": "Loki", "Power": "Magic and Deception", "Home": "Asgard"},
"Franchise": "Marvel Comics"
}

CaptainAmerica = {
"Hero": {"Power": "Super Soldier", "Home": "Earth"},
"Villian": {"Name": "Red Skull", "Power": "Strategic Genius", "Home": "Earth"},
"Franchise": "Marvel Comics"
}

st.title("Superhero Information")

st.write("Select a superhero to view their information:")

if st.button("Captain America Info"):
    st.write(CaptainAmerica)

elif st.button("Iron Man Info"):
    st.write(IronMan)

elif st.button("Thor Info"):
    st.write(Thor)

elif st.button("Hulk Info"):
    st.write(Hulk)

elif st.button("Aquaman Info"):
    st.write(Aquaman)

elif st.button("Flash Info"):
    st.write(Flash)

elif st.button("Wonder Woman Info"):
    st.write(WonderWoman)

elif st.button("Batman Info"):
    st.write(Batman)

elif st.button("Superman Info"):
    st.write(Superman)

else:
    if st.button("Get Random Hero Info"):
        heroes = [Superman, Batman, WonderWoman, Flash, Aquaman, Hulk, IronMan, Thor, CaptainAmerica]
        selected_hero = random.choice(heroes)
        st.write(selected_hero)