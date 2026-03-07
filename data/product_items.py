# Product item lists per category
# Format per line: Name | Botanical name | Part used | Industries (CSV) | Functions (CSV)

def _parse(text):
    items = []
    for line in text.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split(" | ")]
        if len(parts) < 5:
            continue
        name, botanical, part_used, industries, functions = parts[:5]
        items.append({
            "name": name,
            "botanical": botanical,
            "part_used": part_used,
            "industries": [x.strip() for x in industries.split(",") if x.strip()],
            "functions": [x.strip() for x in functions.split(",") if x.strip()],
        })
    return items


# ---------------------------------------------------------------------------
# Herbal Dry Extracts
# ---------------------------------------------------------------------------
_DRY_EXTRACTS = _parse("""
Amla | Phyllanthus emblica | Fruit | Nutraceuticals, Food, Pharma | Antioxidant, Immunity support
Ashwagandha | Withania somnifera | Root | Nutraceuticals, Pharma | Stress balance, Vitality
Turmeric (Curcumin) | Curcuma longa | Rhizome | Pharma, Food, Cosmetics | Inflammation balance
Green Tea | Camellia sinensis | Leaf | Nutraceuticals, Beverages | Polyphenol antioxidant
Giloy | Tinospora cordifolia | Stem | Nutraceuticals, Ayurveda | Immune modulation
Brahmi | Bacopa monnieri | Whole plant | Nutraceuticals, Pharma | Cognitive support
Shatavari | Asparagus racemosus | Root | Nutraceuticals, Ayurveda | Hormonal balance
Safed Musli | Chlorophytum borivilianum | Root | Nutraceuticals | Vitality support
Ginseng | Panax ginseng | Root | Nutraceuticals | Energy & endurance
Neem Leaf | Azadirachta indica | Leaf | Pharma, Cosmetics | Purification support
Neem Bark | Azadirachta indica | Bark | Pharma, Cosmetics | Skin protection
Tulsi | Ocimum sanctum | Leaf | Nutraceuticals, Pharma | Immune support
Mulethi (Licorice) | Glycyrrhiza glabra | Root | Pharma, Food | Soothing agent
Ginger | Zingiber officinale | Rhizome | Food, Nutraceuticals | Digestive support
Fenugreek | Trigonella foenum-graecum | Seed | Food, Nutraceuticals | Metabolic support
Gymnema | Gymnema sylvestre | Leaf | Nutraceuticals | Glycemic balance
Bitter Gourd | Momordica charantia | Fruit | Nutraceuticals | Sugar management
Banaba | Lagerstroemia speciosa | Leaf | Nutraceuticals | Glucose metabolism
Vijaysar | Pterocarpus marsupium | Wood | Nutraceuticals | Metabolic wellness
Triphala | Terminalia spp. | Fruit blend | Nutraceuticals | Digestive wellness
Haritaki | Terminalia chebula | Fruit | Nutraceuticals | Gut health
Baheda | Terminalia belerica | Fruit | Nutraceuticals | Detox support
Jeera (Cumin) | Cuminum cyminum | Fruit | Food, Nutraceuticals | Digestive aid
Fennel | Foeniculum vulgare | Seed | Food, Nutraceuticals | Digestive comfort
Black Pepper | Piper nigrum | Fruit | Food, Pharma | Bioavailability enhancer
Pipli | Piper longum | Fruit | Ayurveda | Respiratory support
Vasaka | Adhatoda vasica | Leaf | Pharma | Respiratory comfort
Boswellia | Boswellia serrata | Gum resin | Nutraceuticals, Pharma | Joint comfort
Guggul | Commiphora mukul | Resin | Nutraceuticals | Lipid balance
Hadjod | Cissus quadrangularis | Stem | Nutraceuticals | Bone health
Kalmegh | Andrographis paniculata | Aerial parts | Pharma, Nutraceuticals | Liver support
Kutki | Picrorhiza kurroa | Root | Pharma, Ayurveda | Hepatic wellness
Bhumi Amla | Phyllanthus niruri | Whole plant | Pharma | Liver detox
Manjistha | Rubia cordifolia | Root | Cosmetics, Ayurveda | Skin purification
Aloe Vera | Aloe barbadensis | Leaf | Cosmetics, Nutraceuticals | Skin hydration
Bhringraj | Eclipta alba | Whole plant | Cosmetics | Hair nourishment
Rosehip | Rosa canina | Fruit | Cosmetics, Nutraceuticals | Antioxidant support
Pomegranate | Punica granatum | Fruit | Nutraceuticals, Food | Polyphenol support
Grape Seed | Vitis vinifera | Seed | Nutraceuticals | Antioxidant protection
Pine Bark | Pinus pinaster | Bark | Nutraceuticals | Vascular support
Bilberry | Vaccinium myrtillus | Fruit | Nutraceuticals | Eye health support
Cranberry | Vaccinium macrocarpon | Fruit | Nutraceuticals | Urinary wellness
Milk Thistle | Silybum marianum | Seed | Nutraceuticals, Pharma | Liver protection
Echinacea | Echinacea purpurea | Herb | Nutraceuticals | Immune support
Elderberry | Sambucus nigra | Fruit | Nutraceuticals | Seasonal wellness
Valerian | Valeriana officinalis | Root | Nutraceuticals | Sleep support
Chamomile | Matricaria chamomilla | Flower | Nutraceuticals, Cosmetics | Soothing support
Hibiscus | Hibiscus sabdariffa | Flower | Nutraceuticals, Beverages | Antioxidant
Moringa | Moringa oleifera | Leaf | Nutraceuticals, Food | Nutrient density
Spirulina | Arthrospira platensis | Whole algae | Nutraceuticals | Protein & antioxidant
Maca | Lepidium meyenii | Root | Nutraceuticals | Endurance support
Tribulus | Tribulus terrestris | Fruit | Nutraceuticals | Vitality support
Astragalus | Astragalus membranaceus | Root | Nutraceuticals | Immune support
Schisandra | Schisandra chinensis | Fruit | Nutraceuticals | Adaptogenic support
Gotu Kola | Centella asiatica | Leaf | Nutraceuticals, Cosmetics | Skin & cognition
Red Clover | Trifolium pratense | Flower | Nutraceuticals | Hormonal balance
Dong Quai | Angelica sinensis | Root | Nutraceuticals | Women's support
Sea Buckthorn | Hippophae rhamnoides | Fruit | Nutraceuticals | Omega support
Artichoke | Cynara scolymus | Leaf | Nutraceuticals | Liver wellness
Dandelion Root | Taraxacum officinale | Root | Nutraceuticals | Liver support
Rhodiola | Rhodiola rosea | Root | Nutraceuticals | Stress resilience
Senna | Cassia angustifolia | Leaf | Nutraceuticals | Bowel support
Psyllium Husk | Plantago ovata | Husk | Nutraceuticals | Fiber support
Flaxseed | Linum usitatissimum | Seed | Food, Nutraceuticals | Omega support
Cocoa | Theobroma cacao | Seed | Food, Nutraceuticals | Mood support
Green Coffee | Coffea arabica | Seed | Nutraceuticals | Metabolic support
Garlic | Allium sativum | Bulb | Nutraceuticals, Food | Heart health support
Onion | Allium cepa | Bulb | Food, Nutraceuticals | Flavonoid support
Saw Palmetto | Serenoa repens | Fruit | Nutraceuticals | Prostate wellness
Passionflower | Passiflora incarnata | Aerial parts | Nutraceuticals | Calmative support
Epimedium | Epimedium brevicornum | Leaf | Nutraceuticals | Performance support
Kaunch Seed | Mucuna pruriens | Seed | Nutraceuticals | Neurological support
Jamun Seed | Syzygium cumini | Seed | Nutraceuticals | Glycemic balance
Arjun Bark | Terminalia arjuna | Bark | Nutraceuticals | Cardiac wellness
Punarnava | Boerhaavia diffusa | Root | Ayurveda | Fluid balance
Jatamansi | Nardostachys jatamansi | Root | Ayurveda | Stress support
Ashoka Bark | Saraca indica | Bark | Ayurveda | Women's wellness
Bael | Aegle marmelos | Fruit | Ayurveda, Nutraceuticals | Digestive balance
Saffron | Crocus sativus | Stigma | Nutraceuticals, Cosmetics | Mood & skin support
Cardamom | Elettaria cardamomum | Seed | Food, Nutraceuticals | Digestive comfort
Cinnamon | Cinnamomum verum | Bark | Food, Nutraceuticals | Metabolic support
Clove | Syzygium aromaticum | Flower bud | Food, Pharma | Oral wellness
Ginger Root Concentrate | Zingiber officinale | Rhizome | Nutraceuticals, Pharma | Adaptogenic support
Black Cohosh | Actaea racemosa | Root | Nutraceuticals | Women's wellness
Licorice DGL | Glycyrrhiza glabra | Root | Nutraceuticals | Gut comfort
Horsetail | Equisetum arvense | Herb | Nutraceuticals | Silica support
Marshmallow Root | Althaea officinalis | Root | Nutraceuticals | Soothing support
Feverfew | Tanacetum parthenium | Leaf | Nutraceuticals | Head comfort
Olive Leaf | Olea europaea | Leaf | Nutraceuticals | Antioxidant support
Devil's Claw | Harpagophytum procumbens | Root | Nutraceuticals | Joint comfort
White Willow Bark | Salix alba | Bark | Nutraceuticals | Pain balance
Blueberry | Vaccinium corymbosum | Fruit | Nutraceuticals | Antioxidant
Acai Berry | Euterpe oleracea | Fruit | Nutraceuticals | Energy support
Moringa Seed | Moringa oleifera | Seed | Nutraceuticals | Nutrient support
Papaya Leaf | Carica papaya | Leaf | Nutraceuticals | Digestive enzyme support
Orange Peel | Citrus sinensis | Peel | Nutraceuticals, Food | Flavonoid support
Lemon Peel | Citrus limon | Peel | Nutraceuticals, Food | Antioxidant
Chicory Root | Cichorium intybus | Root | Nutraceuticals | Prebiotic support
Guarana | Paullinia cupana | Seed | Nutraceuticals | Energy support
Barley Grass | Hordeum vulgare | Leaf | Nutraceuticals | Detox support
Wheatgrass | Triticum aestivum | Leaf | Nutraceuticals | Chlorophyll support
Tongkat Ali | Eurycoma longifolia | Root | Nutraceuticals | Vitality support
Ashwagandha Root Concentrate | Withania somnifera | Root | Nutraceuticals, Pharma | Adaptogenic support
""")

# ---------------------------------------------------------------------------
# Herbal Liquid Extracts
# ---------------------------------------------------------------------------
_LIQUID_EXTRACTS = _parse("""
Amla Liquid | Phyllanthus emblica | Fruit | Nutraceuticals, Beverages | Antioxidant, Immunity support
Ashwagandha Liquid | Withania somnifera | Root | Nutraceuticals, Pharma | Adaptogenic support
Aloe Vera Liquid | Aloe barbadensis | Leaf | Cosmetics, Beverages | Hydration, Skin soothing
Giloy Liquid | Tinospora cordifolia | Stem | Nutraceuticals | Immune modulation
Brahmi Liquid | Bacopa monnieri | Leaf | Nutraceuticals, Pharma | Cognitive wellness
Green Tea Liquid | Camellia sinensis | Leaf | Beverages, Nutraceuticals | Polyphenol antioxidant
Turmeric Liquid | Curcuma longa | Rhizome | Nutraceuticals, Cosmetics | Anti-inflammatory support
Neem Leaf Liquid | Azadirachta indica | Leaf | Cosmetics, Nutraceuticals | Purification
Tulsi Liquid | Ocimum sanctum | Leaf | Nutraceuticals | Immune support, Respiratory balance
Mulethi Liquid | Glycyrrhiza glabra | Root | Pharma, Nutraceuticals | Soothing, Flavoring
Ginger Liquid | Zingiber officinale | Rhizome | Beverages, Nutraceuticals | Digestive support
Fennel Liquid | Foeniculum vulgare | Seed | Beverages, Nutraceuticals | Digestive comfort
Cinnamon Liquid | Cinnamomum verum | Bark | Beverages, Nutraceuticals | Flavor, Metabolic support
Cardamom Liquid | Elettaria cardamomum | Seed | Beverages, Nutraceuticals | Aroma, Digestion
Black Pepper Liquid | Piper nigrum | Fruit | Nutraceuticals, Food | Bioavailability enhancer
Bael Liquid | Aegle marmelos | Fruit | Beverages, Nutraceuticals | Digestive balance
Baheda Liquid | Terminalia belerica | Fruit | Nutraceuticals | Detox support
Haritaki Liquid | Terminalia chebula | Fruit | Nutraceuticals | Gut motility
Banaba Liquid | Lagerstroemia speciosa | Leaf | Nutraceuticals | Glucose metabolism
Bitter Gourd Liquid | Momordica charantia | Fruit | Nutraceuticals | Metabolic wellness
Gurmar Liquid | Gymnema sylvestre | Leaf | Nutraceuticals | Glycemic balance
Noni Liquid | Morinda citrifolia | Fruit | Nutraceuticals, Beverages | Vitality support
Pomegranate Liquid | Punica granatum | Fruit | Beverages, Nutraceuticals | Antioxidant
Cranberry Liquid | Vaccinium macrocarpon | Fruit | Nutraceuticals | Urinary wellness
Blueberry Liquid | Vaccinium corymbosum | Fruit | Beverages, Nutraceuticals | Antioxidant
Acai Berry Liquid | Euterpe oleracea | Fruit | Beverages, Nutraceuticals | Energy support
Goji Berry Liquid | Lycium barbarum | Fruit | Nutraceuticals | Antioxidant
Rose Liquid | Rosa damascena | Flower | Cosmetics, Beverages | Soothing aroma
Hibiscus Liquid | Hibiscus sabdariffa | Flower | Beverages, Nutraceuticals | Antioxidant
Horsetail Liquid | Equisetum arvense | Herb | Nutraceuticals | Silica support
Schisandra Liquid | Schisandra chinensis | Fruit | Nutraceuticals | Adaptogenic support
Rhodiola Liquid | Rhodiola rosea | Root | Nutraceuticals | Stress resilience
Astragalus Liquid | Astragalus membranaceus | Root | Nutraceuticals | Immune support
Ginseng Liquid | Panax ginseng | Root | Nutraceuticals | Energy support
Maca Liquid | Lepidium meyenii | Root | Nutraceuticals | Endurance support
Fenugreek Liquid | Trigonella foenum-graecum | Seed | Beverages, Nutraceuticals | Metabolic wellness
Yerba Mate Liquid | Ilex paraguariensis | Leaf | Beverages, Nutraceuticals | Energy support
Coffee Bean Liquid | Coffea arabica | Seed | Beverages, Nutraceuticals | Metabolic support
Cocoa Liquid | Theobroma cacao | Seed | Beverages, Nutraceuticals | Mood support
Sea Buckthorn Liquid | Hippophae rhamnoides | Fruit | Beverages, Nutraceuticals | Omega, Antioxidant
Moringa Leaf Liquid | Moringa oleifera | Leaf | Beverages, Nutraceuticals | Nutrient density
Spirulina Liquid | Arthrospira platensis | Algae | Nutraceuticals | Protein, Antioxidant
Kelp Liquid | Laminaria japonica | Algae | Nutraceuticals | Mineral support
Green Coffee Liquid | Coffea robusta | Seed | Nutraceuticals | Metabolic support
Chicory Root Liquid | Cichorium intybus | Root | Beverages, Nutraceuticals | Prebiotic support
Dandelion Root Liquid | Taraxacum officinale | Root | Nutraceuticals | Liver support
Licorice DGL Liquid | Glycyrrhiza glabra | Root | Nutraceuticals | Gut comfort
Psyllium Husk Liquid | Plantago ovata | Husk | Nutraceuticals | Digestive fiber support
Barley Grass Liquid | Hordeum vulgare | Leaf | Nutraceuticals | Detox support
Wheatgrass Liquid | Triticum aestivum | Leaf | Nutraceuticals | Chlorophyll support
Beetroot Liquid | Beta vulgaris | Root | Beverages, Nutraceuticals | Circulation support
Elderberry Liquid | Sambucus nigra | Fruit | Beverages, Nutraceuticals | Seasonal wellness
Garlic Extract Liquid | Allium sativum | Bulb | Nutraceuticals, Food | Heart health support
Tart Cherry Liquid | Prunus cerasus | Fruit | Beverages, Nutraceuticals | Antioxidant
Chamomile Liquid | Matricaria chamomilla | Flower | Nutraceuticals, Beverages | Soothing support
Passionflower Liquid | Passiflora incarnata | Aerial parts | Nutraceuticals | Calmative support
Valerian Liquid | Valeriana officinalis | Root | Nutraceuticals | Sleep support
Echinacea Liquid | Echinacea purpurea | Herb | Nutraceuticals | Immune support
Milk Thistle Liquid | Silybum marianum | Seed | Nutraceuticals, Pharma | Liver protection
Artichoke Liquid | Cynara scolymus | Leaf | Nutraceuticals | Liver wellness
Gotu Kola Liquid | Centella asiatica | Leaf | Nutraceuticals, Cosmetics | Skin, Cognition
Saw Palmetto Liquid | Serenoa repens | Fruit | Nutraceuticals | Prostate wellness
Dong Quai Liquid | Angelica sinensis | Root | Nutraceuticals | Women's support
Red Clover Liquid | Trifolium pratense | Flower | Nutraceuticals | Hormonal balance
Turmeric + Ginger Blend Liquid | Curcuma longa + Zingiber | Rhizome | Beverages, Nutraceuticals | Digestive, Antioxidant
Herbal Immunity Blend Liquid | Tulsi, Giloy, Amla | Leaf/Stem/Fruit | Nutraceuticals | Immune support
Herbal Digestive Blend Liquid | Jeera, Fennel, Ginger | Seed/Rhizome | Nutraceuticals | Digestive aid
Stress & Relaxation Blend Liquid | Valerian, Ashwagandha, Chamomile | Root/Leaf/Flower | Nutraceuticals | Calmative support
Adaptogen Blend Liquid | Rhodiola, Ashwagandha | Root | Nutraceuticals | Stress resilience
Skin Glow Blend Liquid | Aloe, Rosehip, Vitamin E | Leaf/Fruit/Compound | Cosmetics, Nutraceuticals | Skin nourishment
Joint Support Blend Liquid | Boswellia, Turmeric, MSM | Gum/Rhizome | Nutraceuticals | Joint wellness
""")

# ---------------------------------------------------------------------------
# Herbal Oil Extracts
# ---------------------------------------------------------------------------
_OIL_EXTRACTS = _parse("""
Neem Oil Extract | Azadirachta indica | Seed | Cosmetics, Pharma | Skin protection, Purification
Turmeric Oil Extract | Curcuma longa | Rhizome | Cosmetics, Nutraceuticals | Anti-inflammatory, Skin brightening
Brahmi Oil Extract | Bacopa monnieri | Whole plant | Cosmetics, Ayurveda | Cognitive support, Hair nourishment
Bhringraj Oil Extract | Eclipta alba | Whole plant | Cosmetics | Hair strengthening, Scalp care
Calendula Oil Extract | Calendula officinalis | Flower | Cosmetics, Pharma | Skin soothing, Wound support
Arnica Oil Extract | Arnica montana | Flower | Pharma, Cosmetics | Bruise care, Muscle comfort
Lavender Oil Extract | Lavandula angustifolia | Flower | Cosmetics, Aromatherapy | Relaxation, Skin calming
Chamomile Oil Extract | Matricaria chamomilla | Flower | Cosmetics | Soothing, Anti-redness
St. John's Wort Oil Extract | Hypericum perforatum | Flower | Pharma, Cosmetics | Nerve comfort, Skin healing
Rosehip Oil Extract | Rosa canina | Fruit | Cosmetics | Skin regeneration, Antioxidant
Aloe Vera Oil Extract | Aloe barbadensis | Leaf | Cosmetics, Nutraceuticals | Hydration, Skin healing
Gotu Kola Oil Extract | Centella asiatica | Leaf | Cosmetics | Skin firming, Scar support
Moringa Oil Extract | Moringa oleifera | Seed | Cosmetics | Moisturisation, Skin nutrition
Carrot Seed Oil Extract | Daucus carota | Seed | Cosmetics | Antioxidant, Skin rejuvenation
Ashwagandha Oil Extract | Withania somnifera | Root | Ayurveda, Cosmetics | Stress relief, Vitality
Amla Oil Extract | Phyllanthus emblica | Fruit | Cosmetics, Ayurveda | Hair nourishment, Scalp health
Hibiscus Oil Extract | Hibiscus rosa-sinensis | Flower | Cosmetics | Hair growth, Scalp conditioning
Fenugreek Oil Extract | Trigonella foenum-graecum | Seed | Cosmetics | Hair strengthening, Scalp care
Kalonji Oil Extract | Nigella sativa | Seed | Cosmetics, Nutraceuticals | Skin protection, Immune support
Clove Oil Extract | Syzygium aromaticum | Flower bud | Cosmetics, Pharma | Antimicrobial, Pain relief
Peppermint Oil Extract | Mentha piperita | Leaf | Cosmetics, Pharma | Cooling, Scalp stimulation
Neem Leaf Oil Extract | Azadirachta indica | Leaf | Cosmetics | Purification, Scalp care
Castor Oil Extract | Ricinus communis | Seed | Cosmetics, Pharma | Hair thickening, Skin barrier
Frankincense Oil Extract | Boswellia serrata | Resin | Cosmetics, Aromatherapy | Skin rejuvenation, Grounding
Sandalwood Oil Extract | Santalum album | Wood | Cosmetics, Aromatherapy | Skin soothing, Fragrance
Vetiver Oil Extract | Vetiveria zizanioides | Root | Cosmetics, Aromatherapy | Skin toning, Grounding
Ylang Ylang Oil Extract | Cananga odorata | Flower | Cosmetics, Aromatherapy | Mood balance, Hair care
Rosemary Oil Extract | Rosmarinus officinalis | Leaf | Cosmetics | Hair growth, Scalp stimulation
Tea Tree Oil Extract | Melaleuca alternifolia | Leaf | Cosmetics, Pharma | Antimicrobial, Skin cleansing
Eucalyptus Oil Extract | Eucalyptus globulus | Leaf | Pharma, Cosmetics | Respiratory support, Cooling
Lemongrass Oil Extract | Cymbopogon citratus | Leaf | Cosmetics, Aromatherapy | Toning, Refreshing
Patchouli Oil Extract | Pogostemon cablin | Leaf | Cosmetics, Aromatherapy | Skin care, Fragrance
Geranium Oil Extract | Pelargonium graveolens | Leaf | Cosmetics, Aromatherapy | Skin balancing, Mood support
Bergamot Oil Extract | Citrus bergamia | Peel | Cosmetics, Aromatherapy | Mood uplift, Skin care
Cedarwood Oil Extract | Cedrus atlantica | Wood | Cosmetics, Aromatherapy | Scalp care, Calming
Neroli Oil Extract | Citrus aurantium | Flower | Cosmetics, Aromatherapy | Skin rejuvenation, Stress relief
Jasmine Oil Extract | Jasminum officinale | Flower | Cosmetics, Aromatherapy | Mood balance, Skin care
Rose Oil Extract | Rosa damascena | Flower | Cosmetics, Aromatherapy | Skin hydration, Mood balance
Marjoram Oil Extract | Origanum majorana | Leaf | Pharma, Aromatherapy | Muscle comfort, Relaxation
Thyme Oil Extract | Thymus vulgaris | Leaf | Pharma, Cosmetics | Antimicrobial, Respiratory support
""")

# ---------------------------------------------------------------------------
# Herbal Soft Extracts
# ---------------------------------------------------------------------------
_SOFT_EXTRACTS = _parse("""
Ashwagandha Soft Extract | Withania somnifera | Root | Nutraceuticals, Pharma | Adaptogenic support, Vitality
Turmeric Soft Extract | Curcuma longa | Rhizome | Nutraceuticals, Pharma | Anti-inflammatory, Antioxidant
Boswellia Soft Extract | Boswellia serrata | Gum resin | Nutraceuticals, Pharma | Joint comfort, Inflammation balance
Brahmi Soft Extract | Bacopa monnieri | Whole plant | Nutraceuticals, Pharma | Cognitive support, Memory
Ginger Soft Extract | Zingiber officinale | Rhizome | Nutraceuticals, Food | Digestive support, Anti-nausea
Gymnema Soft Extract | Gymnema sylvestre | Leaf | Nutraceuticals, Pharma | Glycemic balance
Shatavari Soft Extract | Asparagus racemosus | Root | Nutraceuticals, Ayurveda | Hormonal balance, Vitality
Amla Soft Extract | Phyllanthus emblica | Fruit | Nutraceuticals | Antioxidant, Vitamin C support
Giloy Soft Extract | Tinospora cordifolia | Stem | Nutraceuticals, Ayurveda | Immune modulation
Moringa Soft Extract | Moringa oleifera | Leaf | Nutraceuticals | Nutrient density
Green Tea Soft Extract | Camellia sinensis | Leaf | Nutraceuticals | Polyphenol antioxidant
Milk Thistle Soft Extract | Silybum marianum | Seed | Nutraceuticals, Pharma | Liver protection
Grape Seed Soft Extract | Vitis vinifera | Seed | Nutraceuticals, Cosmetics | Antioxidant, Vascular support
Valerian Soft Extract | Valeriana officinalis | Root | Nutraceuticals | Sleep support, Calmative
Ginseng Soft Extract | Panax ginseng | Root | Nutraceuticals, Pharma | Energy support, Adaptogen
Mulethi Soft Extract | Glycyrrhiza glabra | Root | Pharma, Nutraceuticals | Soothing, Gut comfort
Hadjod Soft Extract | Cissus quadrangularis | Stem | Nutraceuticals | Bone health, Joint support
Neem Soft Extract | Azadirachta indica | Leaf | Pharma, Cosmetics | Skin purification
Bilberry Soft Extract | Vaccinium myrtillus | Fruit | Nutraceuticals | Eye health, Antioxidant
Schisandra Soft Extract | Schisandra chinensis | Fruit | Nutraceuticals | Adaptogenic support
Rhodiola Soft Extract | Rhodiola rosea | Root | Nutraceuticals, Pharma | Stress resilience
Echinacea Soft Extract | Echinacea purpurea | Herb | Nutraceuticals | Immune support
Saw Palmetto Soft Extract | Serenoa repens | Fruit | Nutraceuticals | Prostate wellness
Fenugreek Soft Extract | Trigonella foenum-graecum | Seed | Nutraceuticals | Metabolic support, Galactagogue
Gotu Kola Soft Extract | Centella asiatica | Leaf | Cosmetics, Nutraceuticals | Skin healing, Cognitive support
Garlic Soft Extract | Allium sativum | Bulb | Nutraceuticals, Pharma | Cardiovascular support
Dandelion Root Soft Extract | Taraxacum officinale | Root | Nutraceuticals | Liver support, Diuretic
Artichoke Soft Extract | Cynara scolymus | Leaf | Nutraceuticals | Liver wellness, Digestion
Passionflower Soft Extract | Passiflora incarnata | Aerial parts | Nutraceuticals | Calmative, Sleep support
Elderberry Soft Extract | Sambucus nigra | Fruit | Nutraceuticals | Immune support, Antioxidant
Black Cohosh Soft Extract | Actaea racemosa | Root | Nutraceuticals | Women's wellness
Tribulus Soft Extract | Tribulus terrestris | Fruit | Nutraceuticals | Vitality, Performance support
Maca Soft Extract | Lepidium meyenii | Root | Nutraceuticals | Energy, Endurance
Pine Bark Soft Extract | Pinus pinaster | Bark | Nutraceuticals | Vascular support, Antioxidant
Pomegranate Soft Extract | Punica granatum | Fruit | Nutraceuticals | Antioxidant, Heart health
""")

# ---------------------------------------------------------------------------
# Essential Oils
# ---------------------------------------------------------------------------
_ESSENTIAL_OILS = _parse("""
Lavender Essential Oil | Lavandula angustifolia | Flower | Aromatherapy, Cosmetics, Pharma | Relaxation, Skin calming, Sleep support
Peppermint Essential Oil | Mentha piperita | Leaf | Aromatherapy, Food, Pharma | Cooling, Digestive comfort, Mental clarity
Eucalyptus Essential Oil | Eucalyptus globulus | Leaf | Pharma, Aromatherapy | Respiratory support, Antimicrobial
Tea Tree Essential Oil | Melaleuca alternifolia | Leaf | Cosmetics, Pharma | Antimicrobial, Skin cleansing
Rose Essential Oil | Rosa damascena | Flower | Cosmetics, Perfumery, Aromatherapy | Skin hydration, Mood balance
Jasmine Essential Oil | Jasminum grandiflorum | Flower | Perfumery, Cosmetics, Aromatherapy | Mood uplift, Skin care
Sandalwood Essential Oil | Santalum album | Wood | Perfumery, Cosmetics, Aromatherapy | Skin soothing, Grounding
Bergamot Essential Oil | Citrus bergamia | Peel | Aromatherapy, Perfumery | Mood uplift, Stress relief
Frankincense Essential Oil | Boswellia serrata | Resin | Aromatherapy, Cosmetics | Grounding, Skin rejuvenation
Ylang Ylang Essential Oil | Cananga odorata | Flower | Perfumery, Aromatherapy, Cosmetics | Mood balance, Hair care
Lemon Essential Oil | Citrus limon | Peel | Aromatherapy, Food, Cosmetics | Uplifting, Antimicrobial
Orange Essential Oil | Citrus sinensis | Peel | Aromatherapy, Food, Cosmetics | Mood uplift, Antioxidant
Clove Essential Oil | Syzygium aromaticum | Flower bud | Pharma, Aromatherapy, Food | Analgesic, Antimicrobial
Geranium Essential Oil | Pelargonium graveolens | Leaf | Cosmetics, Aromatherapy, Perfumery | Skin balancing, Mood support
Cedarwood Essential Oil | Cedrus atlantica | Wood | Aromatherapy, Cosmetics | Scalp care, Calming
Patchouli Essential Oil | Pogostemon cablin | Leaf | Perfumery, Cosmetics, Aromatherapy | Skin care, Grounding
Vetiver Essential Oil | Vetiveria zizanioides | Root | Perfumery, Aromatherapy | Grounding, Skin toning
Neroli Essential Oil | Citrus aurantium | Flower | Perfumery, Cosmetics, Aromatherapy | Stress relief, Skin rejuvenation
Rosemary Essential Oil | Rosmarinus officinalis | Leaf | Aromatherapy, Cosmetics, Food | Hair growth, Mental clarity
Thyme Essential Oil | Thymus vulgaris | Leaf | Pharma, Aromatherapy, Food | Antimicrobial, Respiratory support
Chamomile (German) Essential Oil | Matricaria chamomilla | Flower | Cosmetics, Pharma, Aromatherapy | Skin soothing, Anti-inflammatory
Chamomile (Roman) Essential Oil | Anthemis nobilis | Flower | Aromatherapy, Cosmetics | Calming, Digestive comfort
Marjoram Essential Oil | Origanum majorana | Leaf | Pharma, Aromatherapy | Muscle comfort, Relaxation
Oregano Essential Oil | Origanum vulgare | Leaf | Pharma, Food, Aromatherapy | Antimicrobial, Antioxidant
Basil Essential Oil | Ocimum basilicum | Leaf | Aromatherapy, Food | Mental clarity, Digestive support
Cinnamon Leaf Essential Oil | Cinnamomum verum | Leaf | Pharma, Aromatherapy, Food | Antimicrobial, Warming
Cinnamon Bark Essential Oil | Cinnamomum verum | Bark | Pharma, Food, Aromatherapy | Warming, Metabolic support
Ginger Essential Oil | Zingiber officinale | Rhizome | Pharma, Aromatherapy, Food | Digestive support, Warming
Cardamom Essential Oil | Elettaria cardamomum | Seed | Aromatherapy, Food, Perfumery | Digestive comfort, Aroma
Black Pepper Essential Oil | Piper nigrum | Fruit | Pharma, Food, Aromatherapy | Warming, Circulatory support
Lemongrass Essential Oil | Cymbopogon citratus | Leaf | Aromatherapy, Cosmetics, Food | Refreshing, Toning
Citronella Essential Oil | Cymbopogon nardus | Leaf | Aromatherapy, Pharma | Insect repellent, Refreshing
Palmarosa Essential Oil | Cymbopogon martinii | Leaf | Cosmetics, Aromatherapy, Perfumery | Skin moisturising, Balancing
Grapefruit Essential Oil | Citrus paradisi | Peel | Aromatherapy, Cosmetics | Uplifting, Toning
Lime Essential Oil | Citrus aurantifolia | Peel | Aromatherapy, Food, Cosmetics | Refreshing, Antioxidant
Mandarin Essential Oil | Citrus reticulata | Peel | Aromatherapy, Food | Calming, Digestive support
Spearmint Essential Oil | Mentha spicata | Leaf | Aromatherapy, Food | Refreshing, Digestive comfort
Wintergreen Essential Oil | Gaultheria procumbens | Leaf | Pharma, Aromatherapy | Muscle comfort, Analgesic
Juniper Berry Essential Oil | Juniperus communis | Berry | Aromatherapy, Pharma | Detox support, Purifying
Cypress Essential Oil | Cupressus sempervirens | Leaf | Aromatherapy, Cosmetics | Circulation support, Toning
Clary Sage Essential Oil | Salvia sclarea | Flower | Aromatherapy, Cosmetics | Hormonal balance, Relaxation
Helichrysum Essential Oil | Helichrysum italicum | Flower | Cosmetics, Aromatherapy | Skin regeneration, Anti-aging
Myrrh Essential Oil | Commiphora myrrha | Resin | Aromatherapy, Cosmetics, Pharma | Skin healing, Grounding
Frankincense Carterii Essential Oil | Boswellia carterii | Resin | Aromatherapy, Cosmetics | Rejuvenation, Meditation
Niaouli Essential Oil | Melaleuca quinquenervia | Leaf | Pharma, Aromatherapy | Respiratory support, Antimicrobial
Cajeput Essential Oil | Melaleuca cajuputi | Leaf | Pharma, Aromatherapy | Respiratory support, Analgesic
Fennel Essential Oil | Foeniculum vulgare | Seed | Aromatherapy, Food, Pharma | Digestive support, Detox
Anise Essential Oil | Pimpinella anisum | Seed | Food, Pharma | Digestive comfort, Flavoring
Caraway Essential Oil | Carum carvi | Seed | Food, Pharma | Digestive aid, Flavoring
Coriander Essential Oil | Coriandrum sativum | Seed | Food, Aromatherapy | Digestive support, Refreshing
Dill Essential Oil | Anethum graveolens | Seed | Food, Pharma | Digestive comfort, Calming
Cumin Essential Oil | Cuminum cyminum | Seed | Food, Aromatherapy | Digestive support, Warming
Carrot Seed Essential Oil | Daucus carota | Seed | Cosmetics, Aromatherapy | Skin rejuvenation, Detox
Turmeric Essential Oil | Curcuma longa | Rhizome | Cosmetics, Aromatherapy | Anti-inflammatory, Skin brightening
Ajwain Essential Oil | Trachyspermum ammi | Seed | Pharma, Food | Digestive support, Antimicrobial
Tulsi Essential Oil | Ocimum sanctum | Leaf | Pharma, Aromatherapy | Immune support, Respiratory comfort
Neem Essential Oil | Azadirachta indica | Seed | Cosmetics, Pharma | Skin protection, Insecticidal
Garlic Essential Oil | Allium sativum | Bulb | Pharma, Food | Heart health, Antimicrobial
Onion Essential Oil | Allium cepa | Bulb | Pharma, Food | Antimicrobial, Antioxidant
Hyssop Essential Oil | Hyssopus officinalis | Leaf | Pharma, Aromatherapy | Respiratory support, Expectorant
Elemi Essential Oil | Canarium luzonicum | Resin | Cosmetics, Aromatherapy | Skin rejuvenation, Grounding
Oud Essential Oil | Aquilaria malaccensis | Wood | Perfumery | Grounding, Luxurious fragrance
Davana Essential Oil | Artemisia pallens | Herb | Perfumery, Aromatherapy | Mood balance, Fragrance
Kewra Essential Oil | Pandanus fascicularis | Flower | Perfumery, Food | Aroma, Flavoring
Spikenard Essential Oil | Nardostachys jatamansi | Root | Aromatherapy, Cosmetics | Stress relief, Grounding
Valerian Essential Oil | Valeriana officinalis | Root | Pharma, Aromatherapy | Sleep support, Calmative
Camphor Essential Oil | Cinnamomum camphora | Wood | Pharma, Cosmetics | Analgesic, Respiratory support
Litsea Cubeba Essential Oil | Litsea cubeba | Fruit | Aromatherapy, Cosmetics | Uplifting, Refreshing
Petitgrain Essential Oil | Citrus aurantium | Leaf | Aromatherapy, Perfumery | Calming, Mood balance
Amyris Essential Oil | Amyris balsamifera | Wood | Aromatherapy, Perfumery | Grounding, Relaxation
Cassia Essential Oil | Cinnamomum cassia | Bark | Food, Pharma | Warming, Antimicrobial
Violet Leaf Essential Oil | Viola odorata | Leaf | Perfumery, Cosmetics | Delicate floral, Skin care
Immortelle Essential Oil | Helichrysum italicum | Flower | Cosmetics, Aromatherapy | Anti-aging, Skin repair
Balsam Fir Essential Oil | Abies balsamea | Needle | Aromatherapy | Respiratory support, Grounding
Spruce Essential Oil | Picea mariana | Needle | Aromatherapy | Grounding, Respiratory support
Pine Essential Oil | Pinus sylvestris | Needle | Aromatherapy, Pharma | Respiratory support, Refreshing
Fir Needle Essential Oil | Abies sibirica | Needle | Aromatherapy | Forest-fresh, Respiratory support
Siberian Fir Essential Oil | Abies sibirica | Needle | Aromatherapy, Pharma | Respiratory support, Energising
""")

# ---------------------------------------------------------------------------
# Carrier Oils
# ---------------------------------------------------------------------------
_CARRIER_OILS = _parse("""
Sweet Almond Oil | Prunus dulcis | Seed | Cosmetics, Pharma | Skin moisturising, Emollient
Jojoba Oil | Simmondsia chinensis | Seed | Cosmetics | Skin balancing, Hair nourishment
Argan Oil | Argania spinosa | Seed | Cosmetics | Anti-aging, Skin nourishment
Rosehip Seed Oil | Rosa canina | Seed | Cosmetics | Skin regeneration, Antioxidant
Coconut Oil (Fractionated) | Cocos nucifera | Fruit | Cosmetics, Food | Moisturising, Emollient
Coconut Oil (Virgin) | Cocos nucifera | Fruit | Cosmetics, Food | Moisturising, Antimicrobial
Hemp Seed Oil | Cannabis sativa | Seed | Cosmetics, Food | Omega balance, Skin health
Avocado Oil | Persea americana | Fruit | Cosmetics, Food | Deep moisturising, Emollient
Sunflower Seed Oil | Helianthus annuus | Seed | Cosmetics, Food | Skin softening, Lightweight
Grapeseed Oil | Vitis vinifera | Seed | Cosmetics | Antioxidant, Lightweight emollient
Castor Oil | Ricinus communis | Seed | Cosmetics, Pharma | Hair thickening, Skin barrier
Black Seed Oil | Nigella sativa | Seed | Nutraceuticals, Cosmetics | Immune support, Skin protection
Moringa Oil | Moringa oleifera | Seed | Cosmetics | Skin nutrition, Moisturising
Neem Oil | Azadirachta indica | Seed | Cosmetics, Pharma | Skin protection, Antimicrobial
Sesame Oil | Sesamum indicum | Seed | Cosmetics, Food, Ayurveda | Skin nourishment, Warming
Olive Oil | Olea europaea | Fruit | Cosmetics, Food | Skin softening, Antioxidant
Apricot Kernel Oil | Prunus armeniaca | Seed | Cosmetics | Skin softening, Emollient
Peach Kernel Oil | Prunus persica | Seed | Cosmetics | Skin nourishment, Lightweight
Hazelnut Oil | Corylus avellana | Seed | Cosmetics | Astringent, Skin toning
Macadamia Oil | Macadamia integrifolia | Seed | Cosmetics | Skin regeneration, Emollient
Sea Buckthorn Oil | Hippophae rhamnoides | Fruit/Seed | Cosmetics, Nutraceuticals | Antioxidant, Skin rejuvenation
Tamanu Oil | Calophyllum inophyllum | Seed | Cosmetics | Skin healing, Anti-inflammatory
Marula Oil | Sclerocarya birrea | Seed | Cosmetics | Anti-aging, Antioxidant
Baobab Oil | Adansonia digitata | Seed | Cosmetics | Skin elasticity, Moisturising
Pumpkin Seed Oil | Cucurbita pepo | Seed | Cosmetics, Food | Antioxidant, Zinc-rich
Flaxseed Oil | Linum usitatissimum | Seed | Cosmetics, Food | Omega-3 support, Skin nourishment
Chia Seed Oil | Salvia hispanica | Seed | Cosmetics, Food | Omega-3 support, Skin hydration
Safflower Oil | Carthamus tinctorius | Seed | Cosmetics, Food | Lightweight emollient, Skin softening
Rice Bran Oil | Oryza sativa | Bran | Cosmetics, Food | Skin brightening, Antioxidant
Kukui Nut Oil | Aleurites moluccana | Seed | Cosmetics | Skin repair, Lightweight moisturising
Meadowfoam Seed Oil | Limnanthes alba | Seed | Cosmetics | Emollient, Skin protection
Evening Primrose Oil | Oenothera biennis | Seed | Cosmetics, Nutraceuticals | Hormonal balance, Skin health
Borage Oil | Borago officinalis | Seed | Cosmetics, Nutraceuticals | GLA source, Skin health
Pomegranate Seed Oil | Punica granatum | Seed | Cosmetics | Antioxidant, Skin regeneration
Raspberry Seed Oil | Rubus idaeus | Seed | Cosmetics | UV filter, Antioxidant
Passion Fruit Seed Oil | Passiflora incarnata | Seed | Cosmetics | Lightweight, Skin nourishment
Watermelon Seed Oil | Citrullus lanatus | Seed | Cosmetics | Lightweight emollient, Antioxidant
Kalahari Melon Seed Oil | Citrullus lanatus | Seed | Cosmetics | Skin nourishment, Lightweight
Abyssinian Oil | Crambe abyssinica | Seed | Cosmetics | High-shine, Skin conditioning
Meadow Buttercup Seed Oil | Ranunculus acris | Seed | Cosmetics | Emollient, Skin softening
Perilla Seed Oil | Perilla frutescens | Seed | Cosmetics, Food | Omega-3 support, Skin health
Mafura Oil | Trichilia emetica | Seed | Cosmetics | Emollient, Skin repair
Pracaxi Oil | Pentaclethra macroloba | Seed | Cosmetics | Skin regeneration, Wound healing
Manketti Oil | Ricinodendron rautanenii | Seed | Cosmetics | Antioxidant, Skin nourishment
Babassu Oil | Orbignya oleifera | Seed | Cosmetics | Lightweight moisturising, Emollient
Ucuuba Butter (Liquid) | Virola surinamensis | Seed | Cosmetics | Skin softening, Emollient
Canola Oil (Refined) | Brassica napus | Seed | Food, Cosmetics | Emollient, Carrier base
Almond Sweet Oil (Refined) | Prunus dulcis | Seed | Cosmetics, Pharma | Skin softening, Emollient
Carrot Seed Oil | Daucus carota | Seed | Cosmetics | Antioxidant, Skin rejuvenation
Vitamin E Oil (Tocopherol) | Wheat germ | Germ | Cosmetics, Nutraceuticals | Antioxidant, Skin protection
Wheat Germ Oil | Triticum aestivum | Germ | Cosmetics, Nutraceuticals | Antioxidant, Vitamin E-rich
Andiroba Oil | Carapa guianensis | Seed | Cosmetics, Pharma | Insect repellent, Anti-inflammatory
Buriti Oil | Mauritia flexuosa | Fruit | Cosmetics | Beta-carotene rich, Skin protection
Cupuacu Butter (Liquid) | Theobroma grandiflorum | Seed | Cosmetics | Deep moisturising, Emollient
Pequi Oil | Caryocar brasiliense | Seed | Cosmetics | Antioxidant, Skin nourishment
Tucuma Oil | Astrocaryum tucuma | Seed | Cosmetics | Emollient, Moisturising
""")

# ---------------------------------------------------------------------------
# Herbal Powders
# ---------------------------------------------------------------------------
_HERBAL_POWDERS = _parse("""
Amla Powder | Phyllanthus emblica | Fruit | Nutraceuticals, Food, Cosmetics | Antioxidant, Vitamin C support
Ashwagandha Powder | Withania somnifera | Root | Nutraceuticals, Pharma | Adaptogenic support, Stress balance
Turmeric Powder | Curcuma longa | Rhizome | Food, Nutraceuticals, Cosmetics | Anti-inflammatory, Antioxidant
Neem Leaf Powder | Azadirachta indica | Leaf | Pharma, Cosmetics | Purification, Skin care
Moringa Powder | Moringa oleifera | Leaf | Nutraceuticals, Food | Nutrient density, Energy support
Triphala Powder | Terminalia spp. | Fruit blend | Nutraceuticals, Ayurveda | Digestive wellness, Detox
Brahmi Powder | Bacopa monnieri | Whole plant | Nutraceuticals | Cognitive support, Memory
Shatavari Powder | Asparagus racemosus | Root | Nutraceuticals, Ayurveda | Hormonal balance, Vitality
Giloy Powder | Tinospora cordifolia | Stem | Nutraceuticals | Immune modulation
Tulsi Powder | Ocimum sanctum | Leaf | Nutraceuticals | Immune support, Respiratory wellness
Ginger Powder | Zingiber officinale | Rhizome | Food, Nutraceuticals | Digestive support, Warming
Mulethi Powder | Glycyrrhiza glabra | Root | Pharma, Food | Soothing, Expectorant
Fenugreek Powder | Trigonella foenum-graecum | Seed | Food, Nutraceuticals | Metabolic support, Galactagogue
Cinnamon Powder | Cinnamomum verum | Bark | Food, Nutraceuticals | Metabolic support, Flavor
Cardamom Powder | Elettaria cardamomum | Seed | Food, Nutraceuticals | Digestive comfort, Aroma
Clove Powder | Syzygium aromaticum | Flower bud | Food, Pharma | Antimicrobial, Analgesic
Black Pepper Powder | Piper nigrum | Fruit | Food, Pharma | Bioavailability enhancer, Warming
Fennel Powder | Foeniculum vulgare | Seed | Food, Nutraceuticals | Digestive comfort, Galactagogue
Cumin Powder | Cuminum cyminum | Seed | Food, Nutraceuticals | Digestive aid, Iron support
Coriander Powder | Coriandrum sativum | Seed | Food, Nutraceuticals | Digestive aid, Flavoring
Haritaki Powder | Terminalia chebula | Fruit | Nutraceuticals, Ayurveda | Gut health, Detox
Baheda Powder | Terminalia belerica | Fruit | Nutraceuticals | Detox support, Respiratory wellness
Bhringraj Powder | Eclipta alba | Whole plant | Cosmetics | Hair nourishment, Scalp care
Manjistha Powder | Rubia cordifolia | Root | Cosmetics, Ayurveda | Skin purification, Blood cleansing
Neem Bark Powder | Azadirachta indica | Bark | Pharma | Antimicrobial, Oral care
Arjun Bark Powder | Terminalia arjuna | Bark | Nutraceuticals | Cardiac wellness
Ashoka Bark Powder | Saraca indica | Bark | Ayurveda | Women's wellness
Punarnava Powder | Boerhaavia diffusa | Root | Ayurveda | Fluid balance, Kidney support
Vacha Powder | Acorus calamus | Root | Ayurveda | Cognitive support, Digestive aid
Sarpagandha Powder | Rauvolfia serpentina | Root | Pharma | Blood pressure support
Muktashukti Bhasma Blend Powder | Oyster shell | Shell | Ayurveda | Calcium support, Antacid
Kalmegh Powder | Andrographis paniculata | Aerial parts | Pharma, Nutraceuticals | Liver support
Bhumi Amla Powder | Phyllanthus niruri | Whole plant | Pharma | Liver detox, Urinary support
Kutki Powder | Picrorhiza kurroa | Root | Pharma | Hepatic wellness
Guduchi Satva Powder | Tinospora cordifolia | Stem | Ayurveda | Immune support, Antipyretic
Gudmar Powder | Gymnema sylvestre | Leaf | Nutraceuticals | Glycemic balance
Bael Powder | Aegle marmelos | Fruit | Ayurveda | Digestive wellness
Safed Musli Powder | Chlorophytum borivilianum | Root | Nutraceuticals | Vitality, Strength
Kaunch Seed Powder | Mucuna pruriens | Seed | Nutraceuticals | Neurological support, Dopamine precursor
Jamun Seed Powder | Syzygium cumini | Seed | Nutraceuticals | Glycemic balance
Vijaysar Powder | Pterocarpus marsupium | Wood | Nutraceuticals | Metabolic wellness
Guggul Powder | Commiphora mukul | Resin | Nutraceuticals | Lipid balance, Joint support
Boswellia Powder | Boswellia serrata | Gum resin | Nutraceuticals, Pharma | Joint comfort
Hadjod Powder | Cissus quadrangularis | Stem | Nutraceuticals | Bone health
Nirgundi Powder | Vitex negundo | Leaf | Ayurveda | Joint mobility, Anti-inflammatory
Rasna Powder | Pluchea lanceolata | Root | Ayurveda | Joint support
Jatamansi Powder | Nardostachys jatamansi | Root | Ayurveda | Stress support, Sleep aid
Tagar Powder | Valeriana wallichii | Root | Ayurveda | Calmative support
Anantmool Powder | Hemidesmus indicus | Root | Ayurveda | Blood purification
Pashanbheda Powder | Bergenia ligulata | Root | Ayurveda | Urinary wellness
Shikakai Powder | Acacia concinna | Pods | Cosmetics | Natural hair cleanser
Reetha Powder | Sapindus mukorossi | Fruit | Cosmetics | Natural surfactant, Hair care
Multani Mitti (Fullers Earth) | Montmorillonite clay | Clay | Cosmetics | Skin cleansing, Pore reduction
Lodhra Powder | Symplocos racemosa | Bark | Cosmetics, Ayurveda | Skin toning, Astringent
Rose Petal Powder | Rosa damascena | Flower | Cosmetics, Nutraceuticals | Skin soothing, Antioxidant
Hibiscus Flower Powder | Hibiscus sabdariffa | Flower | Cosmetics, Nutraceuticals | Hair care, Antioxidant
Lavender Flower Powder | Lavandula angustifolia | Flower | Cosmetics, Aromatherapy | Skin calming, Fragrance
Chamomile Flower Powder | Matricaria chamomilla | Flower | Cosmetics, Nutraceuticals | Soothing, Anti-redness
Spirulina Powder | Arthrospira platensis | Algae | Nutraceuticals, Food | Protein, Antioxidant
Wheat Grass Powder | Triticum aestivum | Leaf | Nutraceuticals, Food | Chlorophyll, Detox support
Barley Grass Powder | Hordeum vulgare | Leaf | Nutraceuticals, Food | Detox, Enzyme support
Psyllium Husk Powder | Plantago ovata | Husk | Nutraceuticals | Fiber support, Cholesterol balance
Flaxseed Powder | Linum usitatissimum | Seed | Food, Nutraceuticals | Fiber, Omega-3 support
Chia Seed Powder | Salvia hispanica | Seed | Food, Nutraceuticals | Fiber, Omega support
Pomegranate Peel Powder | Punica granatum | Peel | Cosmetics, Nutraceuticals | Antioxidant, Skin care
Milk Thistle Powder | Silybum marianum | Seed | Nutraceuticals | Liver protection
Green Tea Powder (Matcha) | Camellia sinensis | Leaf | Food, Nutraceuticals, Cosmetics | Antioxidant, Alertness
Senna Leaf Powder | Cassia angustifolia | Leaf | Pharma | Bowel support
Ashwagandha Leaf Powder | Withania somnifera | Leaf | Nutraceuticals | Adaptogenic support
Noni Powder | Morinda citrifolia | Fruit | Nutraceuticals | Vitality, Antioxidant
Acai Berry Powder | Euterpe oleracea | Fruit | Nutraceuticals | Antioxidant, Energy support
Maca Powder | Lepidium meyenii | Root | Nutraceuticals | Endurance, Energy support
Gotu Kola Powder | Centella asiatica | Leaf | Nutraceuticals, Cosmetics | Skin healing, Cognitive support
Peppermint Leaf Powder | Mentha piperita | Leaf | Food, Nutraceuticals | Digestive comfort, Cooling
Rosemary Powder | Rosmarinus officinalis | Leaf | Food, Cosmetics | Antioxidant, Hair care
Saffron Powder | Crocus sativus | Stigma | Food, Nutraceuticals, Cosmetics | Mood support, Skin brightening
Garlic Powder | Allium sativum | Bulb | Food, Nutraceuticals | Cardiovascular support, Antimicrobial
Onion Powder | Allium cepa | Bulb | Food, Nutraceuticals | Antioxidant, Flavoring
Tomato Powder | Solanum lycopersicum | Fruit | Food, Nutraceuticals | Lycopene, Antioxidant
Banana Powder | Musa paradisiaca | Fruit | Food, Nutraceuticals | Prebiotic, Energy support
Apple Powder | Malus domestica | Fruit | Food, Nutraceuticals | Fiber, Antioxidant
Beetroot Powder | Beta vulgaris | Root | Food, Nutraceuticals | Circulation support, Energy
Carrot Powder | Daucus carota | Root | Food, Nutraceuticals | Beta-carotene, Antioxidant
Spinach Powder | Spinacia oleracea | Leaf | Food, Nutraceuticals | Iron support, Phytonutrients
Pumpkin Powder | Cucurbita pepo | Fruit | Food, Nutraceuticals | Antioxidant, Fiber support
Mango Powder (Amchur) | Mangifera indica | Fruit | Food, Nutraceuticals | Vitamin C, Antioxidant
Papaya Powder | Carica papaya | Fruit | Food, Nutraceuticals | Digestive enzyme support
Tamarind Powder | Tamarindus indica | Fruit | Food, Nutraceuticals | Antioxidant, Digestive aid
Kokum Powder | Garcinia indica | Fruit | Food, Nutraceuticals | Antioxidant, Digestive support
Bilberry Powder | Vaccinium myrtillus | Fruit | Nutraceuticals | Eye health, Antioxidant
Elderberry Powder | Sambucus nigra | Fruit | Nutraceuticals | Immune support, Antioxidant
Cranberry Powder | Vaccinium macrocarpon | Fruit | Nutraceuticals | Urinary wellness
Sea Buckthorn Powder | Hippophae rhamnoides | Fruit | Nutraceuticals | Omega support, Antioxidant
Licorice Root Powder | Glycyrrhiza glabra | Root | Pharma, Food | Soothing, Expectorant
Valerian Root Powder | Valeriana officinalis | Root | Nutraceuticals | Sleep support
Tribulus Powder | Tribulus terrestris | Fruit | Nutraceuticals | Vitality, Performance support
Cacao Powder | Theobroma cacao | Seed | Food, Nutraceuticals | Antioxidant, Mood support
""")

# ---------------------------------------------------------------------------
# Butters
# ---------------------------------------------------------------------------
_BUTTERS = _parse("""
Shea Butter | Vitellaria paradoxa | Seed | Cosmetics | Deep moisturising, Skin softening
Cocoa Butter | Theobroma cacao | Seed | Cosmetics, Food | Emollient, Skin barrier
Mango Butter | Mangifera indica | Seed | Cosmetics | Skin softening, Moisturising
Kokum Butter | Garcinia indica | Seed | Cosmetics | Emollient, Skin firming
Murumuru Butter | Astrocaryum murumuru | Seed | Cosmetics | Moisture retention, Emollient
Cupuacu Butter | Theobroma grandiflorum | Seed | Cosmetics | Deep moisturising, Hair conditioning
Illipe Butter | Shorea stenoptera | Seed | Cosmetics | Emollient, Skin nourishment
Sal Butter | Shorea robusta | Seed | Cosmetics | Emollient, Skin conditioning
Ucuuba Butter | Virola surinamensis | Seed | Cosmetics | Skin softening, Emollient
Bacuri Butter | Platonia insignis | Seed | Cosmetics | Skin repair, Moisturising
Pistachio Butter | Pistacia vera | Seed | Cosmetics, Food | Antioxidant, Skin nourishment
Mowrah Butter | Madhuca latifolia | Seed | Cosmetics | Emollient, Skin conditioning
Aloe Butter | Aloe barbadensis + hydrogenated base | Leaf | Cosmetics | Soothing, Skin healing
Hemp Butter | Cannabis sativa | Seed | Cosmetics | Omega balance, Skin health
Avocado Butter | Persea americana | Fruit | Cosmetics | Deep moisturising, Emollient
Macadamia Butter | Macadamia integrifolia | Seed | Cosmetics | Emollient, Skin softening
Coconut Butter | Cocos nucifera | Fruit | Cosmetics, Food | Moisturising, Antimicrobial
Tamanu Butter | Calophyllum inophyllum | Seed | Cosmetics | Skin healing, Anti-inflammatory
Kpangnan Butter | Pentadesma butyracea | Seed | Cosmetics | Moisturising, Emollient
Mafura Butter | Trichilia emetica | Seed | Cosmetics | Emollient, Skin repair
Baobab Butter | Adansonia digitata | Seed | Cosmetics | Skin elasticity, Moisturising
Ximenia Butter | Ximenia americana | Seed | Cosmetics | Skin softening, Emollient
Borneo Tallow Butter | Shorea macrophylla | Seed | Cosmetics | Emollient, Skin nourishment
Tucuma Butter | Astrocaryum tucuma | Seed | Cosmetics | Emollient, Hair conditioning
Neem Butter | Azadirachta indica | Seed | Cosmetics, Pharma | Skin protection, Antimicrobial
""")

# ---------------------------------------------------------------------------
# Ayurvedic Oils
# ---------------------------------------------------------------------------
_AYURVEDIC_OILS = _parse("""
Brahmi Oil | Bacopa monnieri + Sesame base | Whole plant | Ayurveda, Cosmetics | Cognitive support, Hair nourishment
Bhringraj Oil | Eclipta alba + Sesame base | Whole plant | Ayurveda, Cosmetics | Hair strengthening, Scalp care
Mahanarayan Oil | Multi-herb classical formula | Roots/Herbs | Ayurveda | Joint support, Muscle comfort
Dhanwantharam Oil | Classical Ayurvedic formula | Roots/Herbs | Ayurveda | Vata balance, Musculoskeletal support
Ksheerabala Oil | Sida cordifolia + Milk base | Root | Ayurveda | Neurological support, Vata balance
Bala Oil | Sida cordifolia + Sesame base | Root | Ayurveda | Strength support, Nourishment
Ksheera Bala 101 Oil | Sida cordifolia multi-processed | Root | Ayurveda | Deep nourishment, Neurological support
Triphala Oil | Triphala + Sesame base | Fruit blend | Ayurveda, Cosmetics | Detox support, Hair care
Neem Oil (Ayurvedic) | Azadirachta indica + Sesame base | Seed | Ayurveda, Cosmetics | Skin purification, Antimicrobial
Jatyadi Oil | Multi-herb formula | Herbs | Ayurveda, Pharma | Wound healing, Skin repair
Kumkumadi Oil | Saffron + Multi-herb in Sesame | Stigma/Herbs | Ayurveda, Cosmetics | Skin brightening, Anti-aging
Nalpamaradi Oil | Ficus spp. + Turmeric in Sesame | Bark/Rhizome | Ayurveda, Cosmetics | Skin glow, Tan reduction
Karpoora Taila | Camphor + Sesame base | Wood | Ayurveda, Pharma | Analgesic, Cooling
Pinda Oil | Multi-herb formula | Herbs | Ayurveda | Pain relief, Muscle comfort
Murivenna Oil | Multi-herb classical formula | Herbs | Ayurveda, Pharma | Bone healing, Joint support
Kottamchukkadi Oil | Dry ginger + Black pepper formula | Rhizome/Fruit | Ayurveda | Vata-Kapha balance, Joint care
Narayana Oil | Multi-herb Ayurvedic formula | Roots/Herbs | Ayurveda | Joint mobility, Strength support
Sahacharadi Oil | Strobilanthes ciliatus + formula | Root | Ayurveda | Vata balance, Lower limb strength
Balaswagandhadi Oil | Ashwagandha + Bala formula | Root | Ayurveda | Vata balance, Nourishment
Gandha Oil | Multi-herb aromatic formula | Herbs | Ayurveda | Vata balance, Relaxation
Tila Oil | Pure sesame base | Seed | Ayurveda | Warming, Vata pacifying
Chandanadi Oil | Sandalwood + Multi-herb formula | Wood/Herbs | Ayurveda, Cosmetics | Skin cooling, Pitta balance
Eladi Oil | Cardamom + Multi-herb formula | Seed/Herbs | Ayurveda, Cosmetics | Skin care, Kapha balance
Lakshadi Oil | Multi-herb formula for bones | Herbs | Ayurveda | Bone strength, Joint nourishment
Prabhanjanam Oil | Classical formula | Herbs | Ayurveda | Vata balance, Nerve support
Asanavilwadi Oil | Vijaysar + Bilva formula | Wood/Fruit | Ayurveda | Skin diseases, Purification
Nalpamara Oil | Ficus spp. multi-herb formula | Bark | Ayurveda | Skin health, Wound healing
Sugandhadi Oil | Aromatic multi-herb formula | Herbs | Ayurveda | Skin glow, Fragrance
Amrutadi Oil | Giloy + Multi-herb formula | Stem/Herbs | Ayurveda | Immune support, Detox
Thikthakam Ghritham (Oil variant) | Bitter herbs formula | Roots/Herbs | Ayurveda | Skin disorders, Pitta balance
Saptaparna Oil | Alstonia scholaris + formula | Bark/Herbs | Ayurveda | Anti-inflammatory, Skin care
Manjishtadi Oil | Rubia cordifolia + formula | Root/Herbs | Ayurveda, Cosmetics | Skin brightening, Blood purification
Prasarini Oil | Paederia foetida + formula | Herb | Ayurveda | Vata balance, Joint support
Mahanarayana Oil (Concentrated) | Multi-herb high potency | Roots/Herbs | Ayurveda | Deep joint penetration
Ashwagandha Oil | Withania somnifera + Sesame | Root | Ayurveda | Strength, Vitality, Vata balance
Shatavari Oil | Asparagus racemosus + Sesame | Root | Ayurveda | Women's wellness, Hormonal balance
Triphala Sesame Oil | Triphala + Sesame | Fruit blend | Ayurveda | Digestive support, Hair care
Licorice Oil | Glycyrrhiza glabra + Sesame | Root | Ayurveda, Cosmetics | Soothing, Skin brightening
Karanja Oil | Pongamia pinnata + formula | Seed/Herbs | Ayurveda | Skin diseases, Wound healing
Tulsi Oil | Ocimum sanctum + Sesame | Leaf | Ayurveda | Immune support, Skin care
Vacha Oil | Acorus calamus + formula | Root | Ayurveda | Cognitive support, Vata balance
Kalabhra Compound Oil | Multi-herb classical | Roots/Herbs | Ayurveda | Comprehensive Vata care
Gokshura Oil | Tribulus terrestris + Sesame | Fruit | Ayurveda | Urinary support, Vitality
Yashtimadhu Oil | Glycyrrhiza glabra + Sesame | Root | Ayurveda | Soothing, Anti-inflammatory
Sarpagandha Oil | Rauvolfia serpentina + formula | Root | Ayurveda | Blood pressure support, Stress relief
Kushtha Oil | Saussurea lappa + formula | Root | Ayurveda | Skin care, Anti-inflammatory
Vidanga Oil | Embelia ribes + formula | Fruit | Ayurveda | Digestive support, Antiparasitic
Chavya Oil | Piper chaba + formula | Root/Stem | Ayurveda | Digestive support, Warming
Shatadhauta Ghrita (Oil variant) | Ghee 100x washed | Dairy | Ayurveda, Cosmetics | Skin healing, Cooling
Badam Rogan | Prunus amygdalus + formula | Seed | Ayurveda | Hair nourishment, Brain support
Methi Oil | Trigonella foenum-graecum + Sesame | Seed | Ayurveda | Hair care, Scalp nourishment
Castor Medicated Oil | Ricinus communis + herbs | Seed/Herbs | Ayurveda | Vata balance, Constipation support
Camphor Medicated Oil | Cinnamomum camphora + base | Wood | Ayurveda, Pharma | Analgesic, Cooling
Eucalyptus Medicated Oil | Eucalyptus globulus + base | Leaf | Pharma, Ayurveda | Respiratory support, Cooling
Peppermint Medicated Oil | Mentha piperita + base | Leaf | Pharma, Ayurveda | Cooling, Pain relief
Mustard Medicated Oil | Brassica nigra + herbs | Seed/Herbs | Ayurveda | Warming, Circulatory support
Garlic Medicated Oil | Allium sativum + Sesame | Bulb | Ayurveda | Heart health, Warming
Ginger Medicated Oil | Zingiber officinale + Sesame | Rhizome | Ayurveda | Digestive support, Warming
Clove Medicated Oil | Syzygium aromaticum + base | Flower bud | Pharma, Ayurveda | Analgesic, Antimicrobial
Noni Medicated Oil | Morinda citrifolia + formula | Fruit | Ayurveda | Vitality support, Skin care
Moringa Medicated Oil | Moringa oleifera + Sesame | Leaf/Seed | Ayurveda, Cosmetics | Nutrient support, Skin care
Saffron Medicated Oil | Crocus sativus + Sesame | Stigma | Ayurveda, Cosmetics | Skin brightening, Mood support
Guduchi Oil | Tinospora cordifolia + Sesame | Stem | Ayurveda | Immune support, Detox
Boswellia Oil | Boswellia serrata + Sesame | Gum resin | Ayurveda, Pharma | Joint comfort, Anti-inflammatory
Turmeric Medicated Oil | Curcuma longa + Sesame | Rhizome | Ayurveda, Cosmetics | Anti-inflammatory, Skin care
""")

# ---------------------------------------------------------------------------
# Crystals (Phytochemical Isolates)
# ---------------------------------------------------------------------------
_CRYSTALS = _parse("""
Menthol Crystals | Mentha piperita | Leaf | Pharma, Food, Cosmetics | Cooling, Analgesic, Flavoring
Camphor Crystals | Cinnamomum camphora | Wood | Pharma, Cosmetics | Analgesic, Antimicrobial, Cooling
Borneol Crystals | Dryobalanops aromatica | Wood | Pharma, Aromatherapy | Analgesic, Antimicrobial, Bioenhancer
Thymol Crystals | Thymus vulgaris | Leaf | Pharma, Food | Antimicrobial, Antifungal, Oral care
Curcumin Crystals | Curcuma longa | Rhizome | Nutraceuticals, Pharma, Cosmetics | Anti-inflammatory, Antioxidant
Berberine Crystals | Berberis aristata | Root | Pharma, Nutraceuticals | Metabolic support, Antimicrobial
Piperine Crystals | Piper nigrum | Fruit | Nutraceuticals, Pharma | Bioavailability enhancer, Digestive support
Quercetin Crystals | Sophora japonica | Flower | Nutraceuticals, Pharma | Antioxidant, Anti-inflammatory
Resveratrol Crystals | Polygonum cuspidatum | Root | Nutraceuticals | Antioxidant, Anti-aging
Catechin Crystals | Camellia sinensis | Leaf | Nutraceuticals | Antioxidant, Cardiovascular support
Silymarin Crystals | Silybum marianum | Seed | Pharma, Nutraceuticals | Liver protection, Antioxidant
Andrographolide Crystals | Andrographis paniculata | Aerial parts | Pharma | Liver support, Immune modulation
Glycyrrhizin Crystals | Glycyrrhiza glabra | Root | Pharma, Food | Sweetening, Anti-inflammatory
Guggulsterone Crystals | Commiphora mukul | Resin | Nutraceuticals, Pharma | Lipid balance, Metabolic support
Boswellic Acid Crystals | Boswellia serrata | Gum resin | Pharma, Nutraceuticals | Joint comfort, Anti-inflammatory
Withanolide Crystals | Withania somnifera | Root | Pharma, Nutraceuticals | Adaptogenic, Neuroprotective
Bacoside Crystals | Bacopa monnieri | Whole plant | Pharma | Cognitive support, Neuroprotective
Forskolin Crystals | Coleus forskohlii | Root | Nutraceuticals, Pharma | Metabolic support, cAMP activator
""")

# ---------------------------------------------------------------------------
# Floral Waters (Hydrosols)
# ---------------------------------------------------------------------------
_FLORAL_WATERS = _parse("""
Rose Hydrosol | Rosa damascena | Flower | Cosmetics, Food | Skin toning, Hydration, Soothing
Lavender Hydrosol | Lavandula angustifolia | Flower | Cosmetics, Aromatherapy | Skin calming, Relaxation
Chamomile Hydrosol | Matricaria chamomilla | Flower | Cosmetics, Pharma | Anti-redness, Soothing
Neroli Hydrosol | Citrus aurantium | Flower | Cosmetics, Aromatherapy | Skin rejuvenation, Stress relief
Peppermint Hydrosol | Mentha piperita | Leaf | Cosmetics, Food | Cooling, Refreshing
Tulsi Hydrosol | Ocimum sanctum | Leaf | Cosmetics | Skin purification, Antimicrobial
Vetiver Hydrosol | Vetiveria zizanioides | Root | Cosmetics, Aromatherapy | Skin toning, Grounding
Sandalwood Hydrosol | Santalum album | Wood | Cosmetics, Aromatherapy | Skin soothing, Fragrance
Geranium Hydrosol | Pelargonium graveolens | Leaf | Cosmetics, Aromatherapy | Skin balancing, Mood support
Lemon Hydrosol | Citrus limon | Peel | Cosmetics, Food | Brightening, Refreshing
Eucalyptus Hydrosol | Eucalyptus globulus | Leaf | Pharma, Cosmetics | Respiratory support, Cooling
Tea Tree Hydrosol | Melaleuca alternifolia | Leaf | Cosmetics, Pharma | Antimicrobial, Skin cleansing
Jasmine Hydrosol | Jasminum officinale | Flower | Cosmetics, Aromatherapy | Mood uplift, Skin care
Clary Sage Hydrosol | Salvia sclarea | Flower | Cosmetics, Aromatherapy | Hormonal balance, Relaxation
Frankincense Hydrosol | Boswellia serrata | Resin | Cosmetics, Aromatherapy | Skin rejuvenation, Meditation
Ylang Ylang Hydrosol | Cananga odorata | Flower | Cosmetics, Aromatherapy | Mood balance, Hair care
Rosemary Hydrosol | Rosmarinus officinalis | Leaf | Cosmetics | Hair growth, Scalp stimulation
Helichrysum Hydrosol | Helichrysum italicum | Flower | Cosmetics, Aromatherapy | Skin repair, Anti-aging
Thyme Hydrosol | Thymus vulgaris | Leaf | Pharma, Cosmetics | Antimicrobial, Scalp care
Hibiscus Hydrosol | Hibiscus sabdariffa | Flower | Cosmetics, Food | Antioxidant, Skin brightening
Orange Blossom Hydrosol | Citrus sinensis | Flower | Cosmetics, Food | Calming, Skin softening
Cardamom Hydrosol | Elettaria cardamomum | Seed | Food, Cosmetics | Aroma, Digestive support
""")

# ---------------------------------------------------------------------------
# Granules
# ---------------------------------------------------------------------------
_GRANULES = _parse("""
Ashwagandha Granules | Withania somnifera | Root | Nutraceuticals | Adaptogenic support, Stress balance
Amla Granules | Phyllanthus emblica | Fruit | Nutraceuticals, Food | Antioxidant, Vitamin C support
Triphala Granules | Terminalia spp. | Fruit blend | Nutraceuticals | Digestive wellness, Detox
Brahmi Granules | Bacopa monnieri | Whole plant | Nutraceuticals | Cognitive support, Memory
Moringa Granules | Moringa oleifera | Leaf | Nutraceuticals, Food | Nutrient density
Green Tea Granules | Camellia sinensis | Leaf | Nutraceuticals, Beverages | Antioxidant, Energy
Turmeric Granules | Curcuma longa | Rhizome | Nutraceuticals, Food | Anti-inflammatory, Antioxidant
Ginger Granules | Zingiber officinale | Rhizome | Food, Nutraceuticals | Digestive support, Warming
Giloy Granules | Tinospora cordifolia | Stem | Nutraceuticals | Immune modulation
Shatavari Granules | Asparagus racemosus | Root | Nutraceuticals | Hormonal balance, Vitality
Fenugreek Granules | Trigonella foenum-graecum | Seed | Nutraceuticals | Metabolic support
Gymnema Granules | Gymnema sylvestre | Leaf | Nutraceuticals | Glycemic balance
Milk Thistle Granules | Silybum marianum | Seed | Nutraceuticals | Liver protection
Valerian Granules | Valeriana officinalis | Root | Nutraceuticals | Sleep support
Echinacea Granules | Echinacea purpurea | Herb | Nutraceuticals | Immune support
Psyllium Husk Granules | Plantago ovata | Husk | Nutraceuticals | Fiber support, Cholesterol balance
Spirulina Granules | Arthrospira platensis | Algae | Nutraceuticals, Food | Protein, Antioxidant
Beetroot Granules | Beta vulgaris | Root | Nutraceuticals, Food | Circulation support, Energy
Pomegranate Granules | Punica granatum | Fruit | Nutraceuticals | Antioxidant, Heart health
Elderberry Granules | Sambucus nigra | Fruit | Nutraceuticals | Immune support, Antioxidant
Sea Buckthorn Granules | Hippophae rhamnoides | Fruit | Nutraceuticals | Omega support, Antioxidant
Maca Granules | Lepidium meyenii | Root | Nutraceuticals | Endurance, Energy support
Tribulus Granules | Tribulus terrestris | Fruit | Nutraceuticals | Vitality, Performance support
Cinnamon Granules | Cinnamomum verum | Bark | Food, Nutraceuticals | Metabolic support, Flavor
Mulethi Granules | Glycyrrhiza glabra | Root | Pharma, Food | Soothing, Expectorant
Neem Granules | Azadirachta indica | Leaf | Pharma | Purification, Antimicrobial
Tart Cherry Granules | Prunus cerasus | Fruit | Nutraceuticals | Antioxidant, Recovery support
Haritaki Granules | Terminalia chebula | Fruit | Nutraceuticals | Gut health, Detox
""")

# ---------------------------------------------------------------------------
# Resin
# ---------------------------------------------------------------------------
_RESIN = _parse("""
Shilajit Resin | Mineral exudate (Humus) | Exudate | Ayurveda, Nutraceuticals | Vitality, Adaptogenic support
Guggul Resin | Commiphora mukul | Resin | Nutraceuticals, Pharma | Lipid balance, Anti-inflammatory
Boswellia Resin | Boswellia serrata | Gum resin | Pharma, Nutraceuticals | Joint comfort, Anti-inflammatory
Frankincense Resin | Boswellia carterii | Resin | Aromatherapy, Pharma | Grounding, Skin rejuvenation
Myrrh Resin | Commiphora myrrha | Resin | Pharma, Aromatherapy, Cosmetics | Wound healing, Antimicrobial
Dragon's Blood Resin | Dracaena draco | Resin | Cosmetics, Pharma | Skin healing, Antioxidant
Benzoin Resin | Styrax benzoin | Resin | Aromatherapy, Pharma, Cosmetics | Skin soothing, Preservative
Galbanum Resin | Ferula galbaniflua | Resin | Aromatherapy, Perfumery | Grounding, Skin care
Elemi Resin | Canarium luzonicum | Resin | Cosmetics, Aromatherapy | Skin rejuvenation, Grounding
Dammar Resin | Shorea spp. | Resin | Industrial, Aromatherapy | Varnish, Incense
Labdanum Resin | Cistus ladanifer | Resin | Perfumery, Aromatherapy | Musky fragrance, Skin care
Opopanax Resin | Commiphora guidottii | Resin | Perfumery, Aromatherapy | Exotic fragrance, Grounding
Copal Resin | Bursera fagaroides | Resin | Aromatherapy | Incense, Purification
Pine Resin | Pinus sylvestris | Resin | Industrial, Pharma | Turpentine base, Antimicrobial
Mastic Resin | Pistacia lentiscus | Resin | Pharma, Food | Oral care, Digestive support
Amber Resin | Pinus succinifera (fossil) | Resin | Aromatherapy, Cosmetics | Grounding, Skin care
""")

# ---------------------------------------------------------------------------
# Oleoresins
# ---------------------------------------------------------------------------
_OLEORESINS = _parse("""
Capsicum Oleoresin | Capsicum annuum | Fruit | Food, Pharma | Pungency, Heat, Color
Black Pepper Oleoresin | Piper nigrum | Fruit | Food, Pharma, Nutraceuticals | Pungency, Bioavailability enhancer
Ginger Oleoresin | Zingiber officinale | Rhizome | Food, Pharma | Pungency, Digestive support
Turmeric Oleoresin | Curcuma longa | Rhizome | Food, Cosmetics, Nutraceuticals | Color, Anti-inflammatory
Paprika Oleoresin | Capsicum annuum (sweet) | Fruit | Food, Cosmetics | Red-orange color, Antioxidant
Celery Seed Oleoresin | Apium graveolens | Seed | Food, Pharma | Flavor, Diuretic support
Coriander Oleoresin | Coriandrum sativum | Seed | Food | Flavor, Digestive support
Cardamom Oleoresin | Elettaria cardamomum | Seed | Food, Pharma | Aroma, Digestive comfort
Clove Oleoresin | Syzygium aromaticum | Flower bud | Food, Pharma | Pungency, Antimicrobial
Cinnamon Oleoresin | Cinnamomum verum | Bark | Food, Pharma | Flavor, Warming
Nutmeg Oleoresin | Myristica fragrans | Seed | Food | Flavor, Digestive support
Mace Oleoresin | Myristica fragrans | Aril | Food, Pharma | Flavor, Antimicrobial
Fennel Oleoresin | Foeniculum vulgare | Seed | Food, Pharma | Aroma, Digestive comfort
Cumin Oleoresin | Cuminum cyminum | Seed | Food | Flavor, Digestive aid
Oregano Oleoresin | Origanum vulgare | Leaf | Food, Pharma | Antimicrobial, Antioxidant
Rosemary Oleoresin | Rosmarinus officinalis | Leaf | Food, Cosmetics | Antioxidant preservative, Flavor
Thyme Oleoresin | Thymus vulgaris | Leaf | Food, Pharma | Antimicrobial, Antioxidant
Garlic Oleoresin | Allium sativum | Bulb | Food, Pharma | Pungency, Cardiovascular support
Onion Oleoresin | Allium cepa | Bulb | Food | Flavor, Antioxidant
Dill Oleoresin | Anethum graveolens | Seed | Food | Flavor, Digestive comfort
Marjoram Oleoresin | Origanum majorana | Leaf | Food, Pharma | Flavor, Muscle comfort
Sage Oleoresin | Salvia officinalis | Leaf | Food, Cosmetics | Antioxidant, Flavor
Basil Oleoresin | Ocimum basilicum | Leaf | Food | Flavor, Antioxidant
Fenugreek Oleoresin | Trigonella foenum-graecum | Seed | Food, Nutraceuticals | Flavor, Metabolic support
""")


# ---------------------------------------------------------------------------
# Master ITEMS dict — keyed by category slug
# ---------------------------------------------------------------------------
ITEMS = {
    "dry-extracts":    _DRY_EXTRACTS,
    "liquid-extracts": _LIQUID_EXTRACTS,
    "oil-extracts":    _OIL_EXTRACTS,
    "soft-extracts":   _SOFT_EXTRACTS,
    "essential-oils":  _ESSENTIAL_OILS,
    "carrier-oils":    _CARRIER_OILS,
    "herbal-powders":  _HERBAL_POWDERS,
    "butters":         _BUTTERS,
    "ayurvedic-oils":  _AYURVEDIC_OILS,
    "crystals":        _CRYSTALS,
    "floral-waters":   _FLORAL_WATERS,
    "granules":        _GRANULES,
    "resin":           _RESIN,
    "oleoresins":      _OLEORESINS,
}


def get_items(slug):
    """Return product items list for a category slug, or empty list."""
    return ITEMS.get(slug, [])


def get_all_industries(slug):
    """Return sorted unique industry values for a category."""
    seen = set()
    result = []
    for item in get_items(slug):
        for ind in item["industries"]:
            if ind not in seen:
                seen.add(ind)
                result.append(ind)
    return sorted(result)


def get_all_functions(slug):
    """Return sorted unique function values for a category."""
    seen = set()
    result = []
    for item in get_items(slug):
        for fn in item["functions"]:
            if fn not in seen:
                seen.add(fn)
                result.append(fn)
    return sorted(result)
