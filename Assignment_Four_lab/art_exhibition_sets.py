# Initial sets
moma_artworks = {
    "Starry Night",
    "The Persistence of Memory",
    "The Scream",
    "Girl with a Pearl Earring"
}

louvre_artworks = {
    "Mona Lisa",
    "The Scream",
    "Liberty Leading the People",
    "Girl with a Pearl Earring"
}

rijksmuseum_artworks = {
    "The Night Watch",
    "Girl with a Pearl Earring",
    "The Milkmaid",
    "Starry Night"
}

 
moma_artworks.add("Composition with Red, Blue, and Yellow")

 
shared_masterpieces = moma_artworks.intersection(
    louvre_artworks,
    rijksmuseum_artworks
)
 
louvre_artworks.update({
    "Raft of the Medusa",
    "Liberty Leading the People"
})

rijksmuseum_artworks.update({
    "The Jewish Bride",
    "The Milkmaid"
})
 
all_unique_artworks = moma_artworks.union(
    louvre_artworks,
    rijksmuseum_artworks
)
 
rijksmuseum_artworks.discard("The Milkmaid")
 
exclusive_moma_artworks = moma_artworks.difference(
    louvre_artworks,
    rijksmuseum_artworks
)

# Output
print("MoMA Artworks:", moma_artworks)
print("Shared Masterpieces:", shared_masterpieces)
print("All Unique Artworks:", all_unique_artworks)
print("Rijksmuseum Artworks After Removal:", rijksmuseum_artworks)
print("Exclusive MoMA Artworks:", exclusive_moma_artworks)
