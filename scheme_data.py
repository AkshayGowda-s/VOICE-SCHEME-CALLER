# scheme_data.py

schemes = {
    "women": [
        {
            "name": "Pradhan Mantri Matru Vandana Yojana (PMMVY)",
            "description": "Provides ₹5,000 financial assistance to pregnant and lactating women for the first live birth.",
            "eligibility": "Women aged 19 years or above who are pregnant for the first time.",
            "documents_required": [
                "Mother and Child Protection (MCP) card",
                "Identity proof (Aadhaar card)",
                "Bank account details"
            ]
        },
        {
            "name": "Mahila E-Haat",
            "description": "Online platform to support women entrepreneurs to showcase and sell their products.",
            "eligibility": "Women entrepreneurs or SHGs (Self Help Groups) or NGOs with women members.",
            "documents_required": [
                "Business details or SHG/NGO registration",
                "Bank account details",
                "Identity proof"
            ]
        },
        {
            "name": "Working Women Hostel Scheme",
            "description": "Provides safe and affordable accommodation for working women away from home.",
            "eligibility": "Working women whose gross income does not exceed the prescribed limit.",
            "documents_required": [
                "Employment certificate/salary slip",
                "ID proof and address proof",
                "Passport-sized photographs"
            ]
        }
    ],
    
    "farmers": [
        {
            "name": "PM-Kisan Samman Nidhi",
            "description": "Provides ₹6,000 per year to eligible farmers in three installments.",
            "eligibility": "Small and marginal farmers owning up to 2 hectares of land.",
            "documents_required": [
                "Land ownership documents",
                "Aadhaar card",
                "Bank account details"
            ]
        },
        {
            "name": "Pradhan Mantri Fasal Bima Yojana (PMFBY)",
            "description": "Crop insurance scheme providing financial support in case of crop loss.",
            "eligibility": "All farmers growing notified crops in notified areas, including tenant farmers.",
            "documents_required": [
                "Land ownership or tenancy agreement",
                "Aadhaar card",
                "Sowing declaration"
            ]
        },
        {
            "name": "Kisan Credit Card (KCC)",
            "description": "Provides short-term credit support to farmers for crop production and allied needs.",
            "eligibility": "Farmers engaged in agriculture and allied activities.",
            "documents_required": [
                "Land records",
                "Identity and address proof",
                "Photographs"
            ]
        }
    ],
    
    "senior": [
        {
            "name": "Indira Gandhi National Old Age Pension Scheme (IGNOAPS)",
            "description": "Provides ₹200 to ₹500 per month to senior citizens below the poverty line.",
            "eligibility": "Citizens aged 60 years or above, belonging to BPL families.",
            "documents_required": [
                "Age proof (Aadhaar, voter ID)",
                "BPL card",
                "Bank account details"
            ]
        },
        {
            "name": "Varishtha Pension Bima Yojana",
            "description": "Pension scheme offering guaranteed returns for senior citizens.",
            "eligibility": "Citizens aged 60 years and above.",
            "documents_required": [
                "Age proof",
                "PAN card",
                "Bank account details"
            ]
        },
        {
            "name": "Rashtriya Vayoshri Yojana",
            "description": "Free assisted-living aids and devices for senior citizens with disabilities.",
            "eligibility": "Senior citizens from BPL category with age-related disabilities.",
            "documents_required": [
                "Disability certificate",
                "Age and income proof",
                "BPL card"
            ]
        }
    ]
}
