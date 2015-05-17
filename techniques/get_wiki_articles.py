# Script to get wikipedia articles and append them to a file 

import wikipedia

page_titles = ["Autobiography_of_Weni", "Sebek-khu_Stele", "Merneptah_Stele", "Bubastite_Portal", "Mesha_stele",
"Kurkh_Monoliths", "Black_Obelisk_of_Shalmaneser_III", "Saba'a_Stele", "Tel_Dan_Stele", "Nimrud_Slab",
"Nimrud_Tablet_K.3751", "Sargon_II's_Prism_A", "Siloam_inscription", "Lachish_relief", "LMLK_seals", "Azekah_Inscription",
"Sennacherib's_Annals", "Esarhaddon's_Treaty_with_Ba'al_of_Tyre", "Ekron_inscription", "Cylinders_of_Nabonidus", 
"Cylinder_of_Cyrus", "Nebuchadnezzar_Chronicle", "Nabonidus_Chronicle", "Temple_Warning_inscription", 
"Trumpeting_Place_inscription", "Arch_of_Titus", "Niagra_Falls", "Whitney_Houston", "Michael_Jackson", "Cheese", "Fruit", 
"Vessel", "Highway", "Archeology", "Squid", "Apple", "Pear", "Mango", "Apricot", "Jersey", "Africa", "Canada", 
"United_States_of_America", "Single-cell_DNA_template_strand_sequencing", "Deception", "Lie", "Truth", "The_Beatles", 
"The_Rolling_Stones", "Shania_Twain", "Twin", "Triplet", "Diabetes", "Cancer", "Respiratory_Disease", "Disease", "Malaria", 
"Hammock", "Whistler", "Vancouver", "Toronto", "Edmonton", "War", "Peace", "Trivia", "Tea", "Coffee", "Bagel", "Hot_Dog", 
"Airplane", "Helicopter", "Twizzlers", "Chocolate", "Almond", "Pecan", "Pelican", "Snail", "Drosophila", 
"Common_green_bottle_fly", "Croissant", "Hobnob_biscuit", "Tim_Tam", "Oboe", "Clarinet", "Bassoon", "Saxophone", "Percussion", 
"Piano", "Harpsicord", "Pencil", "Atom", "Carbon", "Molecule", "Electricity", "Newton", "Einstein", "Max_Planck", "Chair",
"Table", "Marijuana", "Cocaine", "Mushroom", "Ferris_wheel", "Shark", "Dive", "Hotel", "Nonbuilding_structure", "Las_Vegas_Strip",
"Peter_Mundy", "Plovdiv", "Candy", "Confection", "Convection", "Sugar_substitutes", "Dessert", "Desert", 
"Kruger_National_Park", "Zimbabwe", "Peace_park", "Elephant", "Proboscis", "Incisor", "Keystone_species", "Testosterone", 
"Estrogen", "Endangered_species", "Poaching", "South_Asia", "West_Africa", "Taxonomy_(biology)", "Pliocene", "Pineapple", 
"Friend", "Enemy", "Terrorist", "Attack", "Health", "Nutrition", "Fool", "Fleet", "Ship", "Navy", "Seal", "Titanium", 
"Einsteinium", "Antimony", "Arsenic", "Aluminum", "Selenium", "Hydrogyn", "Oxygen", "Nitrogen", "Nickel", "Neodemium",
"Neptunium", "Germanium", "Iron", "Uranium", "Europeum", "Vanadium", "Radium", "Gold", "Galium", "Iodine", "Thorium", "Thalium",
"Strontium", "Silica", "Bronze", "Olympic", "Paralympic", "Athlete", "Symbol", "Symbolism", "Heavy", "Light", "Dark", "Night", 
"Day", "Afternoon", "Morning", "Banana", "Oatmeal", "Life", "Artifical Intelligence", "Fungi", "Protist", "Gene", "DNA",
"RNA", "Guanine", "Adenine", "Thymine", "Uridine", "Deoxyribose", "Anti-parallel", "Parallel"]

filename = "training_data_from_wiki"
open(filename, 'w')
count = 0
for page_title in page_titles:
    try: 
        article_data = wikipedia.page(page_title).content.encode("ascii", "ignore")
        with open(filename, "a") as myfile:
            myfile.write(article_data)
            count = count + 1
    except:
        pass
      
print(count)
        
