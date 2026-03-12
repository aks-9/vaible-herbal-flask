"""
Blog posts data for the Resources > News & Blogs section.
Topics relevant to B2B herbal ingredients buyers.
"""

POSTS = [
    {
        "id": 1,
        "title": "How to Evaluate a COA: What Buyers Should Check Before Approving a Batch",
        "category": "quality-systems",
        "date": "2026-02-10",
        "summary": "A Certificate of Analysis is only as useful as your ability to read it critically. This guide walks through the key parameters buyers should verify — and the red flags that often get missed.",
        "content": (
            "A Certificate of Analysis (COA) is the primary document that connects a supplier's quality claims to the actual batch you receive. Most buyers check the obvious fields — assay percentage, appearance, moisture — but stop short of the more telling details that distinguish a strong COA from a weak one.\n\n"
            "Start with the test methods. A COA that lists HPLC, TLC, or titration results without specifying the method reference (USP, IP, EP, or in-house) gives you no way to verify reproducibility. Ask for the method number or monograph reference. If a supplier cannot provide it, that is a gap in their quality documentation.\n\n"
            "Check the limits, not just the results. A heavy metals result of 0.8 ppm means nothing without knowing the acceptance limit — is it 2 ppm or 0.5 ppm? Always compare results against specifications, not against a previous batch. Batches can pass internally while still sitting outside your formulation's requirements.\n\n"
            "Look at microbiological parameters closely. Total Plate Count, Yeast & Mould, and pathogen-specific tests (Salmonella, E. coli) should all be present for plant-derived materials. A COA that shows only TPC without yeast/mould or pathogen tests is incomplete for food, nutraceutical, or cosmetic applications. Request a re-test COA if the document date is more than 12 months old."
        ),
        "tags": ["COA", "Quality Control", "Batch Evaluation", "Traceability"],
    },
    {
        "id": 2,
        "title": "Dry Extracts vs. Liquid Extracts: A Buyer's Guide to Selecting the Right Form",
        "category": "process",
        "date": "2026-02-14",
        "summary": "The choice between dry and liquid extract forms affects formulation compatibility, dosing accuracy, shelf life, and logistics. Here is how to make the right call for your application.",
        "content": (
            "The extract form you specify has downstream consequences that are easy to underestimate at the sourcing stage. Dry extracts (powdered or granulated) and liquid extracts each have specific advantages depending on your application, processing environment, and supply chain constraints.\n\n"
            "Dry extracts are favoured for tablet, capsule, and powder blend applications. They are easier to weigh, blend, and dose accurately. Standardised dry extracts — where a specific marker compound is held within a defined percentage range — give formulators more consistency batch to batch. Storage and shipping are simpler: no refrigeration, lower weight, lower freight cost per kg of active.\n\n"
            "Liquid extracts work better in topical formulations (creams, serums, toners), beverages, and applications where the carrier solvent (water, glycerin, ethanol) is compatible with the end product. The concentration is typically lower than dry extracts, so volume-to-effect ratios need careful calculation. Shelf life is shorter and cold-chain logistics may apply depending on the solvent and preservative system used.\n\n"
            "For B2B buyers, the most important question is standardisation: is the extract standardised to a specific marker, and is that marker relevant to your intended claim or application? A dry extract standardised to 5% withanolides (ashwagandha) gives you very different formulation options compared to a 1:5 liquid extract of the same botanical. Always align the form selection with your specification first, then with your processing and formulation requirements."
        ),
        "tags": ["Dry Extracts", "Liquid Extracts", "Extraction", "Formulation"],
    },
    {
        "id": 3,
        "title": "Understanding HPLC in Herbal Testing: Why the Method Reference Matters",
        "category": "analytical",
        "date": "2026-02-18",
        "summary": "HPLC is the most common method for marker compound quantification in herbal extracts, but test results are only comparable when the method is clearly defined. Here is what buyers need to understand.",
        "content": (
            "High-Performance Liquid Chromatography (HPLC) is the backbone of quantitative herbal testing. When a COA reports that an ashwagandha extract contains '5% withanolides by HPLC', that number depends entirely on the method conditions: the column type, mobile phase gradient, detector wavelength, reference standard, and calculation formula used.\n\n"
            "Different methods can produce very different results on the same sample. An ashwagandha extract tested by a water-acetonitrile gradient method may yield 4.8% withanolides, while a slightly different acetonitrile-buffer gradient using the same sample could yield 5.6%. Neither is wrong in isolation — but they are not directly comparable. When evaluating supplier COAs, always ask which pharmacopeial standard the method is aligned to (USP, IP, EP), or request a copy of the in-house validated method.\n\n"
            "Reference standards are equally important. A method using a well-characterised reference standard (e.g. USP Reference Standard for withaferin A) will produce more reliable and reproducible results than one using a less-characterised in-house standard. Ask suppliers for the source of their reference standards and whether they are traceable to a pharmacopeial or ISO-accredited source.\n\n"
            "For buyers sourcing from multiple suppliers, specifying the exact HPLC method in your incoming specification — rather than just the marker and limit — removes ambiguity and makes inter-supplier comparisons meaningful. This is a simple step that significantly improves your QC process."
        ),
        "tags": ["HPLC", "Analytical Testing", "Marker Compounds", "Method Validation"],
    },
    {
        "id": 4,
        "title": "EU Botanical Regulations: What Importers Need to Know Before Placing an Order",
        "category": "regulatory",
        "date": "2026-02-22",
        "summary": "Exporting herbal ingredients into the EU requires navigating multiple regulatory frameworks simultaneously. This overview covers the key requirements that affect documentation, labelling, and product eligibility.",
        "content": (
            "The EU herbal ingredient space is governed by several overlapping regulatory frameworks depending on the end-use category: Novel Food Regulation (EU 2015/2283), the Traditional Herbal Medicinal Products Directive (THMPD 2004/24/EC), the Cosmetic Products Regulation (EC 1223/2009), and EFSA health claim regulations, among others. Understanding which framework applies to your product category is the first and most critical step.\n\n"
            "For food supplement ingredients, the Novel Food catalogue is the key reference. If an ingredient does not have a history of significant consumption in the EU prior to May 1997, it is classified as Novel Food and requires pre-market authorisation. Many popular Indian botanicals — ashwagandha, moringa seed extract, certain tulsi preparations — have faced Novel Food queries. Check the EU Novel Food catalogue before assuming an ingredient is permissible.\n\n"
            "Documentation requirements for EU importers include a full specification sheet, COA with method references, heavy metals and pesticide residue test results aligned to EU MRLs (Commission Regulation EC 396/2005), and in many cases a 2-year stability data package. For organic ingredients, EU Organic certification (EC 834/2007 or successor regulation) is required — third-party Indian certifiers must be listed on the EU's approved third-country body list.\n\n"
            "Suppliers who understand EU requirements can pre-prepare documentation packages that reduce your import clearance workload. When evaluating Indian suppliers for EU supply, ask specifically whether they have EU-ready documentation — a specification sheet formatted to EU standards, an allergen statement, a non-GMO declaration, and pesticide residue testing against EU MRLs rather than Indian standards."
        ),
        "tags": ["EU Regulation", "Novel Food", "Import Compliance", "Documentation"],
    },
    {
        "id": 5,
        "title": "Traceability in Herbal Supply Chains: Why It Matters and How to Verify It",
        "category": "quality-systems",
        "date": "2026-02-26",
        "summary": "Supply chain traceability is a regulatory expectation in most major markets and a practical risk management tool. Here is how to assess whether your supplier's traceability system is robust enough.",
        "content": (
            "Traceability in herbal supply chains means being able to link a finished batch of extract back to the raw botanical source: the farm or collection region, the harvest season, the incoming batch number, and the processing steps applied. In practice, many suppliers can provide a batch number but cannot trace it further upstream than their own warehouse receiving record.\n\n"
            "A reliable traceability system has three components: raw material traceability (farm/region, harvest date, incoming batch number), in-process traceability (which raw material batches were used in which production batch, any blending ratios), and finished goods traceability (COA, packing records, dispatch documentation). When evaluating a supplier, ask for a sample traceability report for an existing batch and see how far upstream the chain actually goes.\n\n"
            "For GMP-certified suppliers, traceability records are a formal requirement under WHO GMP Guidelines and ICH Q7. If a supplier holds a GMP certificate from a recognised certifying body, they should be able to provide documented traceability. Ask for the GMP certificate and check which standard it was issued against — EUGMP, WHO GMP, or ISO 22000-level standards all have traceability requirements built in.\n\n"
            "Traceability becomes especially important in the event of a market recall or quality dispute. A supplier who can quickly isolate which raw material batch caused a quality deviation — and provide documentation to support a corrective action — is worth far more to a B2B buyer than one who can only confirm 'the batch was tested and passed'. Build traceability expectations into your supplier qualification process from the start."
        ),
        "tags": ["Traceability", "GMP", "Supply Chain", "Risk Management"],
    },
    {
        "id": 6,
        "title": "Solvent Selection in Botanical Extraction: How It Affects Your Final Product",
        "category": "process",
        "date": "2026-03-02",
        "summary": "The extraction solvent determines which compounds are pulled from the plant matrix, and residual solvent levels in the finished extract are a key safety and regulatory parameter. This post covers what buyers need to understand.",
        "content": (
            "Every herbal extract starts with a solvent — water, ethanol, methanol, acetone, hexane, or a combination — that selects which constituents are extracted from the raw plant material. The solvent choice is one of the most consequential decisions in the extraction process, affecting both efficacy (which compounds are present) and safety (what residues remain).\n\n"
            "Water is the safest solvent from a residue perspective and is common in traditional decoction-style preparations. However, water does not efficiently extract lipophilic compounds (fat-soluble constituents like curcuminoids, terpenoids, or certain alkaloids). Ethanol and ethanol-water combinations are the most widely used solvents for botanical extraction — they are generally recognised as safe (GRAS), leave minimal residues at typical concentrations, and extract a broader range of polar and semi-polar compounds than water alone.\n\n"
            "Methanol and hexane are used in certain industrial extractions but carry stricter residue limits under ICH Q3C guidelines. Methanol is a Class 2 solvent with a permitted daily exposure (PDE) limit of 3.0 mg/day. Hexane is also Class 2 with a PDE of 2.9 mg/day. For extracts destined for food supplement or pharmaceutical applications, residual solvent testing aligned to ICH Q3C is expected — check whether your supplier conducts this testing and what limits they work to.\n\n"
            "When requesting a specification for a botanical extract, always ask about the extraction solvent and residual solvent test results. If the supplier cannot tell you what solvent was used or cannot provide residual solvent data, that is a significant documentation gap. For EU or US market supply, residual solvent data is often a mandatory part of the technical dossier."
        ),
        "tags": ["Extraction", "Solvents", "ICH Q3C", "Residual Solvents", "Process"],
    },
    {
        "id": 7,
        "title": "Building a Supplier Qualification Checklist for Herbal Ingredients",
        "category": "regulatory",
        "date": "2026-03-06",
        "summary": "Qualifying a new herbal ingredient supplier requires more than checking whether they can deliver. A structured qualification checklist helps you evaluate documentation capability, quality systems, and long-term reliability.",
        "content": (
            "Supplier qualification for herbal ingredients is more demanding than for synthetic actives because the product itself is inherently variable — different harvests, different growing conditions, different quality profiles. A supplier qualification checklist needs to account for this variability and assess whether the supplier has systems in place to manage it consistently.\n\n"
            "The documentation tier is the first evaluation layer: Does the supplier have a current GMP certificate? Can they provide a full specification sheet, not just a COA? Do they have method references for all tests listed? Do they have allergen, non-GMO, and BSE/TSE statements available? Are heavy metals and pesticide residue test results available for recent batches? A supplier who cannot readily provide all of these is not ready for regulated-market supply.\n\n"
            "The quality systems tier goes deeper: What is the supplier's incoming raw material qualification process? How do they handle batch failures — do they have documented non-conformance procedures? What is their sampling plan for finished goods release testing? Do they conduct stability studies, and over what shelf life? Ask for a sample quality system document — a standard operating procedure, a batch record template, or a change control procedure — to assess the maturity of their QMS.\n\n"
            "The operational tier covers capacity and supply security: What is their production capacity for your required volume? Do they have alternate raw material sources documented? What is their lead time, and how does it change in seasonal shortage periods? A reliable supplier is one who communicates proactively about these constraints — not one who only discloses them when they affect your order."
        ),
        "tags": ["Supplier Qualification", "GMP", "QMS", "Regulatory", "Documentation"],
    },
    {
        "id": 8,
        "title": "Sustainable Sourcing of Wild-Harvested Botanicals: What B2B Buyers Should Ask",
        "category": "sustainability",
        "date": "2026-03-10",
        "summary": "Wild-harvested botanicals account for a significant share of the global herbal supply chain, but unsustainable collection practices are a growing regulatory and reputational concern. Here is how buyers can build responsible sourcing into their procurement process.",
        "content": (
            "A significant proportion of globally traded herbal raw materials — including many popular adaptogens, roots, and bark-based materials — come from wild-harvested sources rather than cultivated crops. Wild harvesting is often the only practical option for rare or slow-growing plants, but it introduces sustainability risks that buyers in regulated markets are increasingly required to manage.\n\n"
            "The most immediate concern is species identity and ecological pressure. Adulteration of wild-harvested materials with related or inferior species is common, particularly when demand outpaces supply. Suppliers who wild-harvest should be able to demonstrate botanical authentication — macroscopic and microscopic identity testing, and ideally DNA barcoding for high-risk botanicals. If a supplier cannot verify species identity at the raw material intake stage, the downstream quality risk is significant.\n\n"
            "For buyers supplying into the EU or UK, CITES (Convention on International Trade in Endangered Species) compliance is legally required for certain plant species. Check whether your botanical is listed on CITES Appendix I, II, or III — a supplier exporting a CITES-listed species without proper permits is exposing you to import seizure and legal risk. Many Indian herbs with international trade significance (certain species of Saussurea, Taxus, Nardostachys) are CITES-listed.\n\n"
            "Beyond compliance, buyers can drive positive change by asking suppliers about their wild-harvest sourcing policies: Do they work with collectors under a formal agreement that includes harvest quantity limits? Do they have a FairWild or equivalent certification? Is there a documented replanting or habitat management component? These are not just ethical questions — they are supply security questions. Suppliers who manage their wild-harvest sources responsibly are less likely to face sudden supply disruptions from over-collection or regulatory action."
        ),
        "tags": ["Sustainability", "Wild Harvesting", "CITES", "Responsible Sourcing", "Supply Chain"],
    },
]


def get_all_posts():
    """Return all blog posts, sorted newest first."""
    return sorted(POSTS, key=lambda p: p["date"], reverse=True)


def get_post_by_id(post_id):
    """Return a single post by id, or None if not found."""
    for post in POSTS:
        if post["id"] == post_id:
            return post
    return None
